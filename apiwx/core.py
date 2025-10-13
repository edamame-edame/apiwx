"""Core wxPython wrapper classes and utilities for PEP 8 compliance.

This module provides the fundamental building blocks for apiwx, a library that
offers PEP 8 compliant interfaces for wxPython applications. It includes:

- Slots: Multi-slot event handling system with timeout support
- UIAttributes: Mixin class providing snake_case property aliases
- UIInitializeComponent: Mixin for tracking initialization arguments
- UIIndexor: Integer-based indexing with UI object integration
- WrappedApp: Enhanced wx.App with PEP 8 compliant interface
- WrappedWindow: Enhanced wx.Frame with improved attribute access
- WrappedPanel: Enhanced wx.Panel with convenient properties
- Various wrapped controls (StaticText, TextBox, Button, etc.)

The wrapped classes maintain full compatibility with wxPython while providing
more Pythonic interfaces through property-based access patterns and
snake_case naming conventions.

Key Features:
    - Event slot system with automatic connection and timeout protection
    - Property-based attribute access (size, pos, color_background, etc.)
    - Exception-safe event handling with comprehensive logging
    - Initialization argument tracking for debugging and serialization
    - Generic type system integration for enhanced functionality

Example:
    import wx
    from apiwx.core import WrappedApp, WrappedWindow, WrappedButton
    
    app = WrappedApp("MyApp")
    frame = WrappedWindow(app, size=(800, 600), title="Demo")
    
    # Use PEP 8 compliant properties
    frame.color_background = "#FFFFFF"
    frame.pos = (100, 100)
    
    # Add event handlers using slots
    frame.slots_on_close += lambda event: print("Closing...")
    
    app.mainloop()

Note:
    This module requires wxPython 4.0+ and Python 3.11+ for full functionality.
    Some features may require specific wxPython control types to function 
    properly.

Authors:
    apiwx development team

License:
    See LICENSE file in the project root for license information.
"""

# Standard library imports
import os
import sys
import typing
import webbrowser
from threading import Timer

# Third-party imports
import wx as _wx

# Local imports
try:
    from . import debug
    from . import signals
    from . import framestyle
    from . import constants

except ImportError:
    import debug
    import signals
    import framestyle
    import constants

try:
    from .mixins_core import MixinsType
    from .fontmanager import FontManager

except ImportError:
    from mixins_core import MixinsType
    from fontmanager import FontManager


class Slots(list[typing.Callable[..., None]]):
    """List-based container for multiple event handler slots with timeout.
    
    This class extends the built-in list to manage multiple callable
    event handlers (slots) for a single wxPython signal. It provides
    automatic signal connection on the first slot addition and supports
    convenient operators for slot management.
    
    The class automatically connects to the wxPython signal when the first
    slot is added and safely executes all slots when the signal is triggered,
    catching and logging any exceptions that occur during slot execution.
    
    A configurable timeout mechanism prevents slots from running indefinitely.
    If slot execution exceeds the timeout, a TimeoutError is raised.
    
    Attributes:
        control: The wxPython control or window that owns the signal.
        signal: The wxPython event binder (signal) this slots container 
                manages.
        timeout: Maximum time (in seconds) allowed for slot execution.
        
    Example:
        class MyFrame(wx.Frame, UIAttributes):
            def __init__(self, parent):
                super().__init__(parent)
                
                # Add multiple event handlers with custom timeout
                self.slots_on_close.timeout = 10.0  # 10 second timeout
                self.slots_on_close += self.on_close_handler1
                self.slots_on_close += self.on_close_handler2
                
                # Alternative syntax
                self.slots_on_size << self.on_size_handler
                
            def on_close_handler1(self, event):
                print("First close handler")
                
            def on_close_handler2(self, event):
                print("Second close handler")
                
            def on_size_handler(self, event):
                print("Size changed")
    """

    @property
    def timeout(self) -> float | None:
        return self._timeout
    
    @timeout.setter
    def timeout(self, value: float | None):
        self._timeout = value


    def __init__(
        self,
        control: _wx.Control | _wx.Window,
        signal: _wx.PyEventBinder,
        timeout: float = 5.0):
        # init super class
        super().__init__()
    
        # set control and signal
        self.control = control
        self.signal = signal

        # watchdog for slot execution
        self._slot_watchdog: Timer | None = None

        # timeout for slot execution
        self._timeout = timeout


    def append(self, slot: typing.Callable[..., None]):
        # is the first slot ?
        if(not self.control.exists_slots(self.signal)):
            # create connection
            self.control.connect(
                self.signal,
                self._execute_slots_safely
            )

        return super().append(slot)


    def __iadd__(self, slot: typing.Callable[..., None]):
        # add slot
        self.append(slot)
        # return self
        return self


    def __isub__(self, slot: typing.Callable[..., None]):
        # remove slot
        self.remove(slot)
        # return self
        return self


    def __lshift__(self, slot: typing.Callable[..., None]):
        return self.__iadd__(slot)


    def _execute_slots_safely(self, *args, **kwds):  # TODO: async support ?
        """Execute all slots safely, catching and logging exceptions."""
        # cancel previous watchdog
        if self._slot_watchdog is not None:
            self._slot_watchdog.cancel()
            self._slot_watchdog = None

        # create a new watchdog
        if self._timeout is not None:
            self._slot_watchdog = Timer(self._timeout, self._slot_timeout)
            self._slot_watchdog.start()

        # execute all slots
        for slot in self:
            try:
                slot(*args, **kwds)

            except Exception as e:
                debug.uilog(
                    "EXCEPT",
                    f"Slot exception was ignored."
                    f" ({e.__class__} was occurred in {slot.__name__})"
                )

        # cancel watchdog after execution
        if self._slot_watchdog is not None:
            self._slot_watchdog.cancel()
            self._slot_watchdog = None


    def _slot_timeout(self):
        """Handle slot execution timeout by raising TimeoutError."""
        raise TimeoutError("Slot execution timed out")


class UIAttributes:
    """Mixin class providing PEP 8 compliant aliases for wxPython attributes.
    
    This mixin class provides Python-style property names and utility methods
    for wxPython controls and windows. It offers snake_case property names
    as alternatives to wxPython's CamelCase method names for better PEP 8
    compliance.
    
    The class includes properties for:
    - Size and position management (size, pos, clientsize, etc.)
    - Color properties (color_foreground, color_background)
    - Text and font properties
    - Event binding utilities
    - Common control methods (show, hide, enable, disable)
    
    Usage:
        class MyFrame(wx.Frame, UIAttributes):
            def __init__(self, parent):
                super().__init__(parent)
                # Use PEP 8 compliant property names
                self.size = (800, 600)
                self.color_background = "#FFFFFF"
                
    Note:
        This class should be used as a mixin alongside wxPython classes.
        Some properties require specific wxPython base classes to function
        properly (e.g., text property requires wx.Control).
        
    References:
        PEP 8: https://peps.python.org/pep-0008/
        wxPython: https://docs.wxpython.org/
    """
    @property
    def size(self: _wx.Window) -> tuple[int, int]:
        return (tuple(self.GetSize()))

    @size.setter
    def size(self: _wx.Window, value: tuple[int, int]):
        self.SetSize(*value)


    @property
    def clientsize(self: _wx.Window) -> tuple[int, int]:
        return tuple(self.GetClientSize())

    @clientsize.setter
    def clientsize(self: _wx.Window, value: tuple[int, int]):
        self.SetClientSize(*value)


    @property
    def size_max(self: _wx.Window) -> tuple[int, int]:
        return tuple(self.GetMaxSize())

    @size_max.setter
    def size_max(self: _wx.Window, value: tuple[int, int]):
        self.SetMaxSize(_wx.Size(*value))


    @property
    def size_min(self: _wx.Window) -> tuple[int, int]:
        return tuple(self.GetMinSize())

    @size_min.setter
    def size_min(self: _wx.Window, value: tuple[int, int]):
        self.SetMinSize(_wx.Size(*value))


    @property
    def pos(self: _wx.Window) -> tuple[int, int]:
        return self.GetPosition().Get()

    @pos.setter
    def pos(self: _wx.Window, value: tuple[int, int]):
        self.SetPosition(_wx.Point(*value))


    @property
    def color_foreground(self: _wx.Window) -> str:
        return "#" + ''.join(
            map(
                lambda hexstr: (
                        str.replace(
                            str(hexstr), "0x", ""
                        )
                    ),
                self.GetForegroundColour()
            )
        )

    @color_foreground.setter
    def color_foreground(self: _wx.Window, value: str):
        self.SetForegroundColour(value)


    @property
    def color_background(self: _wx.Window) -> str:
        return "#" + ''.join(
            map(
                lambda hexstr: (
                        str.replace(
                            str(hexstr), "0x", ""
                        )
                    ),
                self.GetBackgroundColour()
            )
        )

    @color_background.setter
    def color_background(self: _wx.Window, value: str):
        self.SetBackgroundColour(value)


    @property
    def text(self: _wx.Control) -> str:
        if not isinstance(self, _wx.Control):
            self.raise_attribute_error(
                "text", "wx.Control"
            )

        return self.GetLabelText()

    @text.setter
    def text(self: _wx.Control, value: str | None) -> str:
        if not isinstance(self, _wx.Control):
            self.raise_attribute_error(
                "text", "wx.Control"
            )

        self.SetLabelText(value)


    _bind_events: list[_wx.PyEventBinder]


    @property
    def bind_events(self) -> list[_wx.PyEventBinder]:
        if not hasattr(self, '_bind_events'):
            self._bind_events = []

        return self._bind_events


    @property
    def font(self: _wx.TextAttr) -> str:
        if not isinstance(self, _wx.TextAttr):
            self.raise_attribute_error(
                "font", "wx.TextAttr"
            )

        return FontManager.getkey_from_font(self.GetFont())

    @font.setter
    def font(self: _wx.TextAttr, value: str | _wx.Font):
        if not isinstance(self, _wx.TextAttr):
            self.raise_attribute_error(
                "font", "wx.TextAttr"
            )

        if isinstance(value, _wx.Font):
            font = value

        else:
            font = FontManager.get(value)

        if font is None:
            raise ValueError(
                f"Font '{value}' is not found in FontManager."
            )

        self.SetFont(font)


    @property
    def parent(self: _wx.Window) -> (
            typing.Type['UIAttributes']
            | _wx.Window
            | None
        ):
        return self.Parent
    

    @property
    def toplevel(self: _wx.Window) -> (
            typing.Type['WrappedWindow']
            | _wx.TopLevelWindow
        ):
        return self.GetTopLevelParent()


    def exists_slots(self, signal: _wx.PyEventBinder):
        return signal in self.bind_events


    def connect(
        self: _wx.Control | typing.Type['UIAttributes'],
        signal: _wx.PyEventBinder,
        slot: typing.Callable[..., None]):
        # check class
        if not isinstance(self, _wx.Window):
            self.raise_attribute_error(
                "connect", "wx.Window"
            )

        # already binded ?
        if signal in self.bind_events:
            raise RuntimeError("BaseSlot must bind only once.")

        # bind base slots
        self.Bind(signal, slot)

        # add signal no
        self.bind_events.append(signal)


    def show(self: _wx.Window):
        return self.Show()


    def hide(self: _wx.Window):
        return self.Hide()
    

    def enable(self: _wx.Window):
        return self.Enable()
    
    
    def disable(self: _wx.Window):
        return self.Disable()
    

    def destroy(self: _wx.Window):
        return self.Destroy()


    def is_shown(self: _wx.Window) -> bool:
        return self.IsShown()
    

    def layout(self: _wx.Window):
        return self.Layout()


    @classmethod
    def raise_attribute_error(cls, methodname: str, specclass):
        raise AttributeError(
            f"The `{methodname}()` method is only valid"
            f" for objects of the `{specclass}` class."
        )


class UIInitializeComponent():
    """Mixin class for saving and accessing initialization arguments.
    
    This mixin provides functionality to save __init__ method arguments
    for later access. Useful for wxPython classes that need to track
    their initialization parameters for debugging, serialization, or
    reconstruction purposes.
    
    The saved arguments can be accessed through the init_args and
    init_kwds properties after calling save_initialize_arguments().
    
    Example:
        class MyWidget(wx.Panel, UIInitializeComponent):
            def __init__(self, parent, size=(100, 50), **kwargs):
                super().__init__(parent, **kwargs)
                self.save_initialize_arguments(parent, size=size, **kwargs)
                
            def recreate(self):
                # Access saved arguments
                return MyWidget(*self.init_args, **self.init_kwds)
    """

    def save_initialize_arguments(self, *args, **kwds):
        """Save initialization arguments for later use.
        
        Stores the provided positional and keyword arguments internally
        for access via init_args and init_kwds properties. This is useful
        for wxPython classes that need to track their initialization 
        parameters.
        
        Args:
            *args: Positional arguments to save.
            **kwds: Keyword arguments to save.
        """
        # save args and kwds
        if not hasattr(self, '_init_args'):
            self._init_args = ()

        self._init_args += args

        if not hasattr(self, '_init_kwds'):
            self._init_kwds = {}

        self._init_kwds.update(kwds)


    @property
    def init_args(self) -> tuple:
        if not hasattr(self, '_init_args'):
            self._init_args = ()

        return self._init_args


    @property
    def init_kwds(self) -> dict:
        if not hasattr(self, '_init_kwds'):
            self._init_kwds = {}

        return self._init_kwds


class UIIndexor(int, UIAttributes):
    _index_list: dict['UIIndexor', UIAttributes]


    @property
    def uiobject(self) -> UIAttributes:
        return self._index_list[self]


    def __new__(cls, value: int, index_list: dict['UIIndexor', UIAttributes]):
        # create new instance
        indexor = super().__new__(cls, value)

        # save index list
        indexor._index_list = index_list

        # return instance
        return indexor


    def __getattribute__(self, name):
        if name in UIAttributes.__dict__:
            attribute = getattr(self.uiobject, name)

        else:
            attribute = super().__getattribute__(name)

        return attribute


class WrappedApp(
    _wx.App,
    UIAttributes, UIInitializeComponent,
    metaclass = MixinsType):
    """Enhanced wx.App wrapper with PEP 8 compliant interface.
    
    This class provides a Python-style interface to wxPython's wx.App class,
    offering snake_case property names and enhanced functionality while
    maintaining full compatibility with the underlying wxPython App object.
    
    The wrapper adds:
    - PEP 8 compliant property names (app_name, app_displayname, etc.)
    - Initialization argument tracking via UIInitializeComponent
    - Generic type system support for enhanced functionality
    - Consistent event handling through UIAttributes
    
    Args:
        name (str): Application name for identification and display
        
    Attributes:
        app_name (str): Application name (alias for AppName)
        app_displayname (str): Display name (alias for AppDisplayName)
        
    Example:
        >>> app = WrappedApp("MyApplication")
        >>> app.app_name = "Updated Name"
        >>> app.mainloop()
        
    Note:
        This class should be instantiated only once per application,
        following wxPython's single App instance requirement.
    """

    @property
    def app_name(self) -> str:
        return self.AppName

    @app_name.setter
    def app_name(self, value: str):
        self.AppName = value


    @property
    def app_displayname(self) -> str:
        return self.AppDisplayName

    @app_displayname.setter
    def app_displayname(self, value: str):
        self.AppDisplayName = value


    @property
    def assertmode(self) -> _wx.AppAssertMode:
        return self.AssertMode

    @assertmode.setter
    def assertmode(self, value: _wx.AppAssertMode):
        self.AssertMode = value


    @property
    def displaymode(self) -> _wx.VideoMode:
        return self.DisplayMode


    @property
    def eventhandler_enabled(self) -> bool:
        return self.EvtHandlerEnabled

    @eventhandler_enabled.setter
    def eventhandler_enabled(self, value: bool):
        self.EvtHandlerEnabled = value


    @property
    def instance(self) -> 'WrappedApp':
        return _wx.App.GetInstance()


    def __init__(self, name: str, *args, **kwds):
        # init super class
        super().__init__()

        # set application name
        self.appname = name

        # save args and kwds
        self.save_initialize_arguments(name, *args, **kwds)


    def mainloop(self):
        # run application
        exit_code = self.MainLoop()

        debug.internallog_output_remaining()

        return exit_code


class WrappedWindow(
    _wx.Frame,
    UIAttributes, UIInitializeComponent,
    metaclass = MixinsType):
    """Enhanced wx.Frame wrapper with PEP 8 compliant interface.
    
    This class provides a Python-style interface to wxPython's wx.Frame class,
    offering snake_case property names and enhanced functionality while
    maintaining full compatibility with the underlying Frame object.
    
    The wrapper adds:
    - PEP 8 compliant property names (clientsize, slots_on_close, etc.)
    - Event slot system for convenient event handling
    - Initialization argument tracking for debugging and serialization
    - Generic type system support for enhanced functionality
    
    Args:
        app: Parent application instance
        size (tuple[int, int] | None): Window size as (width, height)
        pos (tuple[int, int] | None): Window position as (x, y)
        title (str | None): Window title text
        color (tuple[int, int, int] | None): Background color as RGB tuple
        style (int | None): wxPython window style flags
        
    Attributes:
        clientsize (wx.Size): Client area size (alias for ClientSize)
        slots_on_close (Slots): Event slots for window close events
        
    Example:
        >>> app = WrappedApp("MyApp")
        >>> window = WrappedWindow(app, size=(800, 600), title="Main Window")
        >>> window.slots_on_close += lambda evt: print("Closing...")
        >>> window.show()
    """

    @property
    def app(self) -> WrappedApp:
        return self._app


    @property
    def clientsize(self) -> _wx.Size:
        return self.ClientSize

    @clientsize.setter
    def clientsize(self, value: _wx.Size):
        self.ClientSize = value


    @property
    def title(self) -> str:
        return self.Title

    @title.setter
    def title(self, value: str):
        self.Title = value


    @property
    def slots_on_close(self):
    # lazy init
        if not hasattr(self, '_slots_on_close'):
            self._slots_on_close = Slots(
                self,
                signals.EVT_CLOSE
            )

        return self._slots_on_close


    @slots_on_close.setter
    def slots_on_close(self, value: Slots):
        ... # read only (apply on Slots.__iadd__)


    @property
    def slots_on_destroy(self):
        # lazy init
        if not hasattr(self, '_slots_on_destroy'):
            self._slots_on_destroy = Slots(
                self,
                signals.EVT_WINDOW_DESTROY
            )

        return self._slots_on_destroy

    @slots_on_destroy.setter
    def slots_on_destroy(self, value: Slots):
        ... # read only (apply on Slots.__iadd__)


    @property
    def slots_on_move(self):
        # lazy init
        if not hasattr(self, '_slots_on_move'):
            self._slots_on_move = Slots(
                self,
                signals.EVT_MOVE
            )

        return self._slots_on_move

    @slots_on_move.setter
    def slots_on_move(self, value: Slots):
        ... # read only (apply on Slots.__iadd__)


    @property
    def slots_on_size(self):
    # lazy init
        if not hasattr(self, '_slots_on_size'):
            self._slots_on_size = Slots(
                self,
                signals.EVT_SIZE
            )

        return self._slots_on_size

    @slots_on_size.setter
    def slots_on_size(self, value: Slots):
        ... # read only (apply on Slots.__iadd__)


    def __init__(
        self,
        app: WrappedApp,
        size: tuple[int, int] = _wx.DefaultSize,
        pos: tuple[int, int] = _wx.DefaultPosition,
        title: str | None = None,
        color: str | None = None,
        style: int = _wx.DEFAULT_FRAME_STYLE,
        *args, **kwds):

        # link with app
        self._app = app

        # init superclass
        super().__init__(
            None,
            size = size, pos = pos,
            title = title,
            style = _wx.DEFAULT_FRAME_STYLE | style
        )

        # set color
        if color is not None:
            self.color_background = color

        # save args and kwds
        self.save_initialize_arguments(
            app,
            size, pos,
            title = title,
            color = color,
            style = style,
            *args, **kwds
        )


class WrappedPanel(
    _wx.Panel,
    UIAttributes, UIInitializeComponent,
    metaclass = MixinsType):
    """Enhanced wx.Panel wrapper with PEP 8 compliant interface.
    
    This class provides a Python-style interface to wxPython's wx.Panel class,
    offering snake_case property names and enhanced functionality while
    maintaining full compatibility with the underlying Panel object.
    
    The wrapper adds:
    - PEP 8 compliant property names and event slot system
    - Enhanced event handling with slots (move, size, paint, etc.)
    - Initialization argument tracking for debugging
    - Generic type system support for mixin functionality
    
    Args:
        parent: Parent window or panel
        size (tuple[int, int] | None): Panel size as (width, height)
        pos (tuple[int, int] | None): Panel position as (x, y)
        color (tuple[int, int, int] | None): Background color as RGB tuple
        style (int | None): wxPython panel style flags
        
    Attributes:
        slots_on_move (Slots): Event slots for panel move events
        slots_on_size (Slots): Event slots for panel resize events
        slots_on_paint (Slots): Event slots for panel paint events
        
    Example:
        >>> panel = WrappedPanel(parent_window, size=(400, 300))
        >>> panel.slots_on_paint += lambda evt: print("Panel repainted")
        >>> panel.color_background = (255, 255, 255)
    """

    @property
    def slots_on_move(self):
        # lazy init
        if not hasattr(self, '_slots_on_move'):
            self._slots_on_move = Slots(
                self,
                signals.EVT_MOVE
            )

        return self._slots_on_move

    @slots_on_move.setter
    def slots_on_move(self, value: Slots):
        ... # read only (apply on Slots.__iadd__)


    @property
    def slots_on_size(self):
    # lazy init
        if not hasattr(self, '_slots_on_size'):
            self._slots_on_size = Slots(
                self,
                signals.EVT_SIZE
            )

        return self._slots_on_size

    @slots_on_size.setter
    def slots_on_size(self, value: Slots):
        ... # read only (apply on Slots.__iadd__)


    @property
    def slots_on_paint(self):
    # lazy init
        if not hasattr(self, '_slots_on_paint'):
            self._slots_on_paint = Slots(
                self,
                signals.EVT_PAINT
            )

        return self._slots_on_paint

    @slots_on_paint.setter
    def slots_on_paint(self, value: Slots):
        ... # read only (apply on Slots.__iadd__)


    def __init__(
        self,
        parent: WrappedWindow,
        size: tuple[int, int] = _wx.DefaultSize,
        pos: tuple[int, int] = _wx.DefaultPosition,
        color: str | None = None,
        style: int = framestyle.TAB_TRAVERSAL,
        * args, **kwds):

        # init superclass
        super().__init__(
            parent,
            size = size, pos = pos,
            style = style
        )

        # set color
        if color is not None:
            self.color_background = color

        # save args and kwds
        self.save_initialize_arguments(
            parent,
            size, pos,
            color = color,
            style = style,
            *args, **kwds
        )


class WrappedStaticText(
    _wx.StaticText,
    UIAttributes, UIInitializeComponent,
    metaclass = MixinsType):
    """Enhanced wx.StaticText wrapper with PEP 8 compliant interface.
    
    This class provides a Python-style interface to wxPython's wx.StaticText 
    class, offering snake_case property names and enhanced functionality while
    maintaining full compatibility with the underlying StaticText object.
    
    The wrapper adds:
    - PEP 8 compliant property names and attribute access
    - Enhanced event handling capabilities
    - Initialization argument tracking for debugging
    - Generic type system support for mixin functionality
    
    Args:
        parent: Parent window or panel
        size (tuple[int, int] | None): Control size as (width, height)
        pos (tuple[int, int] | None): Control position as (x, y)
        label (str | None): Text label to display
        style (int | None): wxPython StaticText style flags
        
    Example:
        >>> label = WrappedStaticText(panel, label="Hello World")
        >>> label.text = "Updated text"
        >>> label.color_foreground = (255, 0, 0)
    """

    def __init__(
        self,
        parent: _wx.Window,
        size: tuple[int, int] = _wx.DefaultSize,
        pos: tuple[int, int] = _wx.DefaultPosition,
        label: str | None = None,
        font: tuple[int, int, int, bool, bool] | str | None = None,
        color_foreground: str | None = None,
        color_background: str | None = None,
        style: int = 0,
        *args, **kwds):

        # init superclass
        super().__init__(
            parent,
            label = label,
            size = size, pos = pos,
            style = style
        )

        # set font
        if font is not None:
            self.SetFont(FontManager.instance[font])

        if color_background is not None:
            self.color_background = color_background

        if color_foreground is not None:
            self.color_foreground = color_foreground

        # save args and kwds
        self.save_initialize_arguments(
            parent,
            size, pos,
            label = label,
            font = font,
            color_foreground = color_foreground,
            color_background = color_background,
            style = style,
            *args, **kwds
        )


class AsLink():
    @property
    def slots_on_click(self):
        # lazy init
        if not hasattr(self, '_slots_on_click'):
            self._slots_on_click = Slots(
                self,
                signals.EVT_LEFT_DOWN
            )

        return self._slots_on_click

    @slots_on_click.setter
    def slots_on_click(self, value: Slots):
        ... # read only (apply on Slots.__iadd__)


    def __init__(self, *args, **kwds):

        # super class init was called from WrappedWindow.__init__
        # so do nothing here
        ...

        # below code was called after super class init

        # connect slots for paint boarder
        self.slots_on_click += (
            self.access
        )


    def access(self, *args, **kwds):
        if os.path.isdir(self.text):
        # open folder
            if sys.platform == "win32":
                os.startfile(self.text)

            elif sys.platform == "darwin":
                os.system(f"open '{self.text}'")

            else:
                os.system(f"xdg-open '{self.text}'")

        else:
            # open link
            webbrowser.open(self.text)


class WrappedTextBox(
    _wx.TextCtrl,
    UIAttributes, UIInitializeComponent,
    metaclass = MixinsType):
    """Enhanced wx.TextCtrl wrapper with PEP 8 compliant interface.
    
    This class provides a Python-style interface to wxPython's wx.TextCtrl 
    class, offering snake_case property names and enhanced functionality while
    maintaining full compatibility with the underlying TextCtrl object.
    
    The wrapper adds:
    - PEP 8 compliant property names (value property for text content)
    - Enhanced event handling capabilities
    - Initialization argument tracking for debugging
    - Generic type system support for mixin functionality
    
    Args:
        parent: Parent window or panel
        size (tuple[int, int] | None): Control size as (width, height)
        pos (tuple[int, int] | None): Control position as (x, y)
        value (str | None): Initial text value
        style (int | None): wxPython TextCtrl style flags
        
    Attributes:
        value (str): Text content (alias for GetValue/SetValue)
        
    Example:
        >>> textbox = WrappedTextBox(panel, value="Initial text")
        >>> textbox.value = "Updated text"
        >>> print(textbox.value)
    """

    @property
    def value(self) -> str:
        return self.GetValue()

    @value.setter
    def value(self, value: str):
        self.SetValue(value)


    def __init__(
        self,
        parent: _wx.Window,
        size: tuple[int, int] = _wx.DefaultSize,
        pos: tuple[int, int] = _wx.DefaultPosition,
        value: str | None = None,
        font: tuple[int, int, int, bool, bool] | str | None = None,
        color_foreground: str | None = None,
        color_background: str | None = None,
        style: int = 0,
        *args, **kwds):

        # init superclass
        super().__init__(
            parent,
            value = value,
            size = size, pos = pos,
            style = style
        )

        # set font
        if font is not None:
            self.SetFont(FontManager.instance[font])

        # set color
        if color_background is not None:
            self.color_background = color_background

        if color_foreground is not None:
            self.color_foreground = color_foreground

        # save args and kwds
        self.save_initialize_arguments(
            parent,
            size, pos,
            value = value,
            font = font,
            color_foreground = color_foreground,
            color_background = color_background,
            style = style,
            *args, **kwds
        )


class WrappedButton(
    _wx.Button,
    UIAttributes, UIInitializeComponent,
    metaclass = MixinsType):
    """Enhanced wx.Button wrapper with PEP 8 compliant interface.
    
    This class provides a Python-style interface to wxPython's wx.Button class,
    offering snake_case property names and enhanced functionality while
    maintaining full compatibility with the underlying Button object.
    
    The wrapper adds:
    - PEP 8 compliant property names and event slot system
    - Enhanced click event handling with slots
    - Initialization argument tracking for debugging
    - Generic type system support for enhanced button behaviors
    
    Args:
        parent: Parent window or panel
        size (tuple[int, int] | None): Button size as (width, height)
        pos (tuple[int, int] | None): Button position as (x, y)
        label (str | None): Button text label
        font (font object | None): Button text font
        color_foreground (tuple[int, int, int] | None): Text color as RGB tuple
        color_background (tuple[int, int, int] | None): Background color as 
                                                        RGB tuple
        style (int | None): wxPython button style flags
        
    Attributes:
        slots_on_click (Slots): Event slots for button click events
        
    Example:
        >>> button = WrappedButton(panel, label="Click Me", size=(100, 30))
        >>> button.slots_on_click += lambda evt: print("Button clicked!")
        >>> button.color_background = (200, 200, 200)
    """

    @property
    def slots_on_click(self):
        # lazy init
        if not hasattr(self, '_slots_on_click'):
            self._slots_on_click = Slots(
                self,
                signals.EVT_BUTTON
            )

        return self._slots_on_click

    @slots_on_click.setter
    def slots_on_click(self, value: Slots):
        ... # read only (apply on Slots.__iadd__)


    def __init__(
        self,
        parent: _wx.Window,
        size: tuple[int, int] = _wx.DefaultSize,
        pos: tuple[int, int] = _wx.DefaultPosition,
        label: str | None = None,
        font: tuple[int, int, int, bool, bool] | str | None = None,
        color_foreground: str | None = None,
        color_background: str | None = None,
        style: int = 0,
        *args, **kwds):

        # init superclass
        super().__init__(
            parent,
            label = label,
            size = size, pos = pos,
            style = style
        )

        # set font
        if font is not None:
            self.SetFont(FontManager.instance[font])

        # set color
        if color_background is not None:
            self.color_background = color_background

        if color_foreground is not None:
            self.color_foreground = color_foreground

        # save args and kwds
        self.save_initialize_arguments(
            parent,
            size, pos,
            label = label,
            font = font,
            color_foreground = color_foreground,
            color_background = color_background,
            style = style,
            *args, **kwds
        )


class WrappedCheckBox(
    _wx.CheckBox,
    UIAttributes, UIInitializeComponent,
    metaclass = MixinsType):
    """Enhanced wx.CheckBox wrapper with PEP 8 compliant interface.
    
    This class provides a Python-style interface to wxPython's wx.CheckBox 
    class, offering snake_case property names and enhanced functionality while
    maintaining full compatibility with the underlying CheckBox object.
    
    The wrapper adds:
    - PEP 8 compliant property names (value property for checked state)
    - Enhanced event handling capabilities
    - Initialization argument tracking for debugging
    - Generic type system support for mixin functionality
    
    Args:
        parent: Parent window or panel
        size (tuple[int, int] | None): Control size as (width, height)
        pos (tuple[int, int] | None): Control position as (x, y)
        label (str | None): Checkbox label text
        style (int | None): wxPython CheckBox style flags
        
    Attributes:
        value (bool): Checked state (alias for GetValue/SetValue)
        
    Example:
        >>> checkbox = WrappedCheckBox(panel, label="Enable feature")
        >>> checkbox.value = True
        >>> if checkbox.value:
        ...     print("Feature enabled")
    """
    @property
    def value(self) -> bool:
        return self.GetValue()

    @value.setter
    def value(self, value: bool):
        self.SetValue(value)


    @property
    def validator(self)	-> _wx.Validator:
        return self.GetValidator()

    @validator.setter
    def validator(self, value: _wx.Validator):
        self.SetValidator(value)


    def __init__(
        self,
        parent: _wx.Window,
        size: tuple[int, int] = _wx.DefaultSize,
        pos: tuple[int, int] = _wx.DefaultPosition,
        label: str | None = None,
        font: tuple[int, int, int, bool, bool] | str | None = None,
        color_foreground: str | None = None,
        color_background: str | None = None,
        style: int = 0,
        *args, **kwds):

        # init superclass
        super().__init__(
            parent,
            label = label,
            size = size, pos = pos,
            style = style
        )

        # set font
        if font is not None:
            self.SetFont(FontManager.instance[font])

        # set color
        if color_background is not None:
            self.color_background = color_background

        if color_foreground is not None:
            self.color_foreground = color_foreground

        # save args and kwds
        self.save_initialize_arguments(
            parent,
            size, pos,
            label = label,
            font = font,
            color_foreground = color_foreground,
            color_background = color_background,
            style = style,
            *args, **kwds
        )


class WrappedRadioBox(
    _wx.RadioBox,
    UIAttributes, UIInitializeComponent,
    metaclass = MixinsType):
    """Enhanced wx.RadioBox wrapper with PEP 8 compliant interface.
    
    This class provides a Python-style interface to wxPython's wx.RadioBox 
    class, offering snake_case property names and enhanced functionality while
    maintaining full compatibility with the underlying RadioBox object.
    
    The wrapper adds:
    - PEP 8 compliant property names (selection property for choice index)
    - Enhanced event handling capabilities
    - Initialization argument tracking for debugging
    - Generic type system support for mixin functionality
    
    Args:
        parent: Parent window or panel
        size (tuple[int, int] | None): Control size as (width, height)
        pos (tuple[int, int] | None): Control position as (x, y)
        label (str | None): RadioBox title text
        choices (list[str] | None): List of radio button labels
        style (int | None): wxPython RadioBox style flags
        
    Attributes:
        selection (int): Selected item index (GetSelection/SetSelection alias)
        
    Example:
        >>> choices = ["Option 1", "Option 2", "Option 3"]
        >>> radiobox = WrappedRadioBox(panel, label="Choose:", choices=choices)
        >>> radiobox.selection = 1  # Select "Option 2"
    """

    @property
    def selection(self) -> int:
        return self.GetSelection()

    @selection.setter
    def selection(self, value: int):
        self.SetSelection(value)


    def __init__(
        self,
        parent: _wx.Window,
        size: tuple[int, int] = _wx.DefaultSize,
        pos: tuple[int, int] = _wx.DefaultPosition,
        label: str | None = None,
        choices: list[str] | None = None,
        major_dimension: int = 0,
        style: int = 0,
        *args, **kwds):

        # init superclass
        super().__init__(
            parent,
            label = label,
            choices = choices if choices is not None else [],
            size = size, pos = pos,
            majorDimension = major_dimension,
            style = style
        )

        # save args and kwds
        self.save_initialize_arguments(
            parent,
            size, pos,
            label = label,
            choices = choices if choices is not None else [],
            major_dimension = major_dimension,
            style = style,
            *args, **kwds
        )


class WrappedListBox(
    _wx.ListBox,
    UIAttributes, UIInitializeComponent,
    metaclass = MixinsType):
    """Enhanced wx.ListBox wrapper with PEP 8 compliant interface.
    
    This class provides a Python-style interface to wxPython's wx.ListBox 
    class, offering snake_case property names and enhanced functionality while
    maintaining full compatibility with the underlying ListBox object.
    
    The wrapper adds:
    - PEP 8 compliant property names for selection management
    - Enhanced event handling capabilities
    - Initialization argument tracking for debugging
    - Generic type system support for mixin functionality
    
    Args:
        parent: Parent window or panel
        size (tuple[int, int] | None): Control size as (width, height)
        pos (tuple[int, int] | None): Control position as (x, y)
        choices (list[str] | None): List of selectable items
        style (int | None): wxPython ListBox style flags
        
    Attributes:
        selection (int): Selected item index
        selections (list[int]): Multiple selected indices (for multi-select)
        
    Example:
        >>> items = ["Item 1", "Item 2", "Item 3"]
        >>> listbox = WrappedListBox(panel, choices=items)
        >>> listbox.selection = 0  # Select first item
    """

    @property
    def selection(self) -> int:
        return self.GetSelection()

    @selection.setter
    def selection(self, value: int):
        self.SetSelection(value)


    @property
    def selections(self) -> list[int]:
        return self.GetSelections()

    @selections.setter
    def selections(self, value: list[int]):
        for index in value:
            self.SetSelection(index)


    def __init__(
        self,
        parent: _wx.Window,
        size: tuple[int, int] = _wx.DefaultSize,
        pos: tuple[int, int] = _wx.DefaultPosition,
        choices: list[str] | None = None,
        style: int = 0,
        *args, **kwds):

    # init superclass
        super().__init__(
            parent,
            choices = choices if choices is not None else [],
            size = size, pos = pos,
            style = style
        )

        # save args and kwds
        self.save_initialize_arguments(
            parent,
            size, pos,
            choices = choices if choices is not None else [],
            style = style,
            *args, **kwds
        )


class WrappedComboBox(
    _wx.ComboBox,
    UIAttributes, UIInitializeComponent,
    metaclass = MixinsType):
    """Enhanced wx.ComboBox wrapper with PEP 8 compliant interface.
    
    This class provides a Python-style interface to wxPython's wx.ComboBox 
    class, offering snake_case property names and enhanced functionality while
    maintaining full compatibility with the underlying ComboBox object.
    
    The wrapper adds:
    - PEP 8 compliant property names (value, selection properties)
    - Enhanced event handling capabilities
    - Initialization argument tracking for debugging
    - Generic type system support for mixin functionality
    
    Args:
        parent: Parent window or panel
        size (tuple[int, int] | None): Control size as (width, height)
        pos (tuple[int, int] | None): Control position as (x, y)
        value (str | None): Initial text value
        choices (list[str] | None): List of dropdown choices
        style (int | None): wxPython ComboBox style flags
        
    Attributes:
        value (str): Current text value
        selection (int): Selected choice index
        
    Example:
        >>> choices = ["Choice 1", "Choice 2", "Choice 3"]
        >>> combo = WrappedComboBox(panel, choices=choices)
        >>> combo.value = "Custom text"
        >>> combo.selection = 1
    """

    @property
    def value(self) -> str:
        return self.GetValue()

    @value.setter
    def value(self, value: str):
        self.SetValue(value)


    def __init__(
        self,
        parent: _wx.Window,
        size: tuple[int, int] = _wx.DefaultSize,
        pos: tuple[int, int] = _wx.DefaultPosition,
        value: str | None = None,
        choices: list[str] | None = None,
        style: int = 0,
        *args, **kwds):

        # init superclass
        super().__init__(
            parent,
            value = value if value is not None else "",
            choices = choices if choices is not None else [],
            size = size, pos = pos,
            style = style
        )

        # save args and kwds
        self.save_initialize_arguments(
            parent,
            size, pos,
            value = value if value is not None else "",
            choices = choices if choices is not None else [],
            style = style,
            *args, **kwds
        )


class WrappedSlider(
    _wx.Slider,
    UIAttributes, UIInitializeComponent,
    metaclass = MixinsType):
    """Enhanced wx.Slider wrapper with PEP 8 compliant interface.
    
    This class provides a Python-style interface to wxPython's wx.Slider 
    class, offering snake_case property names and enhanced functionality while
    maintaining full compatibility with the underlying Slider object.
    
    The wrapper adds:
    - PEP 8 compliant property names (value, min_value, max_value properties)
    - Enhanced event handling capabilities
    - Initialization argument tracking for debugging
    - Generic type system support for mixin functionality
    
    Args:
        parent: Parent window or panel
        size (tuple[int, int] | None): Control size as (width, height)
        pos (tuple[int, int] | None): Control position as (x, y)
        value (int | None): Initial slider value
        min_value (int): Minimum slider value
        max_value (int): Maximum slider value
        style (int | None): wxPython Slider style flags
        
    Attributes:
        value (int): Current slider value
        min_value (int): Minimum value range
        max_value (int): Maximum value range
        
    Example:
        >>> slider = WrappedSlider(panel, value=50, min_value=0, max_value=100)
        >>> slider.value = 75
        >>> print(f"Value: {slider.value}")
    """

    @property
    def value(self) -> int:
        return self.GetValue()

    @value.setter
    def value(self, value: int):
        self.SetValue(value)


    def __init__(
        self,
        parent: _wx.Window,
        size: tuple[int, int] = _wx.DefaultSize,
        pos: tuple[int, int] = _wx.DefaultPosition,
        value: int = 0,
        min_value: int = 0,
        max_value: int = 100,
        style: int = _wx.SL_HORIZONTAL,
        *args, **kwds):

        # init superclass
        super().__init__(
            parent,
            value = value,
            minValue = min_value,
            maxValue = max_value,
            size = size, pos = pos,
            style = style
        )

        # save args and kwds
        self.save_initialize_arguments(
            parent,
            size, pos,
            value = value,
            min_value = min_value,
            max_value = max_value,
            style = style,
            *args, **kwds
        )


class WrappedGauge(
    _wx.Gauge,
    UIAttributes, UIInitializeComponent,
    metaclass = MixinsType):
    """Enhanced wx.Gauge wrapper with PEP 8 compliant interface.
    
    This class provides a Python-style interface to wxPython's wx.Gauge 
    class, offering snake_case property names and enhanced functionality while
    maintaining full compatibility with the underlying Gauge object.
    
    The wrapper adds:
    - PEP 8 compliant property names (value, range properties)
    - Enhanced progress tracking and visualization
    - Initialization argument tracking for debugging
    - Generic type system support for mixin functionality
    
    Args:
        parent: Parent window or panel
        size (tuple[int, int] | None): Control size as (width, height)
        pos (tuple[int, int] | None): Control position as (x, y)
        range (int | None): Maximum gauge value (default 100)
        style (int | None): wxPython Gauge style flags
        
    Attributes:
        value (int): Current gauge value
        range (int): Maximum gauge value
        
    Example:
        >>> gauge = WrappedGauge(panel, range=100)
        >>> gauge.value = 50  # Set to 50% progress
        >>> print(f"Progress: {gauge.value}/{gauge.range}")
    """

    @property
    def value(self) -> int:
        return self.GetValue()

    @value.setter
    def value(self, value: int):
        self.SetValue(value)


    @property
    def range(self) -> int:
        return self.GetRange()

    @range.setter
    def range(self, value: int):
        self.SetRange(value)


    def __init__(
        self,
        parent: _wx.Window,
        size: tuple[int, int] = _wx.DefaultSize,
        pos: tuple[int, int] = _wx.DefaultPosition,
        range: int = 100,
        style: int = _wx.GA_HORIZONTAL,
        *args, **kwds):

        # init superclass
        super().__init__(
            parent,
            range = range,
            size = size, pos = pos,
            style = style
        )

        # save args and kwds
        self.save_initialize_arguments(
            parent,
            size, pos,
            range = range,
            style = style,
            *args, **kwds
        )


class WrappedListCtrl(
    _wx.ListCtrl,
    UIAttributes, UIInitializeComponent,
    metaclass = MixinsType):
    """Enhanced wx.ListCtrl wrapper with PEP 8 compliant interface.
    
    This class provides a Python-style interface to wxPython's wx.ListCtrl 
    class, offering snake_case property names and enhanced functionality while
    maintaining full compatibility with the underlying ListCtrl object.
    
    The wrapper adds:
    - PEP 8 compliant property names (selected_item, item_count properties)
    - Enhanced list management and item handling
    - Initialization argument tracking for debugging
    - Generic type system support for mixin functionality
    
    Args:
        parent: Parent window or panel
        size (tuple[int, int] | None): Control size as (width, height)
        pos (tuple[int, int] | None): Control position as (x, y)
        style (int | None): wxPython ListCtrl style flags
        
    Attributes:
        selected_item (int): Selected item index
        item_count (int): Total number of items
        
    Example:
        >>> listctrl = WrappedListCtrl(panel, style=wx.LC_REPORT)
        >>> listctrl.InsertColumn(0, "Name")
        >>> listctrl.selected_item = 0  # Select first item
    """

    @property
    def item_count(self) -> int:
        return self.GetItemCount()

    @item_count.setter
    def item_count(self, value: int):
        self.SetItemCount(value)


    @property
    def column_count(self) -> int:
        return self.GetColumnCount()


    def __init__(
        self,
        parent: _wx.Window,
        size: tuple[int, int] = _wx.DefaultSize,
        pos: tuple[int, int] = _wx.DefaultPosition,
        style: int = _wx.LC_REPORT,
        *args, **kwds):

        # init superclass
        super().__init__(
            parent,
            size = size, pos = pos,
            style = style
        )

        # save args and kwds
        self.save_initialize_arguments(
            parent,
            size, pos,
            style = style,
            *args, **kwds
        )


class WrappedScrolledWindow(
    _wx.ScrolledWindow,
    UIAttributes, UIInitializeComponent,
    metaclass = MixinsType):
    """Enhanced wx.ScrolledWindow wrapper with PEP 8 compliant interface.
    
    This class provides a Python-style interface to wxPython's 
    wx.ScrolledWindow class, offering snake_case property names and enhanced 
    functionality while maintaining full compatibility with the underlying 
    ScrolledWindow object.
    
    The wrapper adds:
    - PEP 8 compliant property names (scroll_rate, virtual_size properties)
    - Enhanced scrolling and virtual canvas management
    - Initialization argument tracking for debugging
    - Generic type system support for mixin functionality
    
    Args:
        parent: Parent window or panel
        size (tuple[int, int] | None): Control size as (width, height)
        pos (tuple[int, int] | None): Control position as (x, y)
        style (int | None): wxPython ScrolledWindow style flags
        
    Attributes:
        scroll_rate (tuple[int, int]): Scrolling rate (x, y)
        virtual_size (tuple[int, int]): Virtual canvas size
        
    Example:
        >>> scrolled = WrappedScrolledWindow(frame)
        >>> scrolled.scroll_rate = (10, 10)
        >>> scrolled.virtual_size = (800, 600)
    """

    @property
    def virtual_size(self) -> _wx.Size:
        return self.GetVirtualSize()

    @virtual_size.setter
    def virtual_size(self, value: _wx.Size):
        self.SetVirtualSize(value)

    @property
    def scroll_rate(self) -> tuple[int, int]:
        if not hasattr(self, '_scroll_rate'):
            self._scroll_rate = None

        return self._scroll_rate

    @scroll_rate.setter
    def scroll_rate(self, value: tuple[int, int]):
        self._scroll_rate = value

        if self._scroll_rate is not None:
            self.SetScrollRate(
                *self._scroll_rate
            )


    def __init__(
        self,
        parent: _wx.Window,
        size: tuple[int, int] = _wx.DefaultSize,
        pos: tuple[int, int] = _wx.DefaultPosition,
        style: int = _wx.HSCROLL | _wx.VSCROLL,
        *args, **kwds):

        # init superclass
        super().__init__(
            parent,
            size = size, pos = pos,
            style = style
        )

        # save args and kwds
        self.save_initialize_arguments(
            parent,
            size, pos,
            style = style,
            *args, **kwds
        )


class WrappedChoice(
    _wx.Choice,
    UIAttributes, UIInitializeComponent,
    metaclass = MixinsType):
    """Enhanced wx.Choice wrapper with PEP 8 compliant interface.
    
    This class provides a Python-style interface to wxPython's wx.Choice 
    class, offering snake_case property names and enhanced functionality while
    maintaining full compatibility with the underlying Choice object.
    
    The wrapper adds:
    - PEP 8 compliant property names (selection, choices properties)
    - Enhanced event handling capabilities
    - Initialization argument tracking for debugging
    - Generic type system support for mixin functionality
    
    Args:
        parent: Parent window or panel
        size (tuple[int, int] | None): Control size as (width, height)
        pos (tuple[int, int] | None): Control position as (x, y)
        choices (list[str] | None): List of selectable choices
        style (int | None): wxPython Choice style flags
        
    Attributes:
        selection (int): Selected choice index
        choices (list[str]): List of available choices
        
    Example:
        >>> choices = ["Red", "Green", "Blue"]
        >>> choice = WrappedChoice(panel, choices=choices)
        >>> choice.selection = 1  # Select "Green"
        >>> print(choice.choices)
    """

    @property
    def selection(self) -> int:
        return self.GetSelection()

    @selection.setter
    def selection(self, value: int):
        self.SetSelection(value)


    @property
    def choices(self) -> list[str]:
        return list(self.GetStrings())

    @choices.setter
    def choices(self, value: list[str]):
        self.SetItems(value)


    def __init__(
        self,
        parent: _wx.Window,
        size: tuple[int, int] = _wx.DefaultSize,
        pos: tuple[int, int] = _wx.DefaultPosition,
        choices: list[str] | None = None,
        style: int = 0,
        *args, **kwds):

        # init superclass
        super().__init__(
            parent,
            choices = choices if choices is not None else [],
            size = size, pos = pos,
            style = style
        )

        # save args and kwds
        self.save_initialize_arguments(
            parent,
            size, pos,
            choices = choices if choices is not None else [],
            style = style,
            *args, **kwds
        )


class WrappedImage(
    _wx.StaticBitmap,
    UIAttributes, UIInitializeComponent,
    metaclass = MixinsType):
    """Enhanced wx.StaticBitmap wrapper with PEP 8 compliant interface.
    
    This class provides a Python-style interface to wxPython's 
    wx.StaticBitmap class, offering snake_case property names and enhanced 
    functionality while maintaining full compatibility with the underlying 
    StaticBitmap object.
    
    The wrapper adds:
    - PEP 8 compliant property names (bitmap, size properties)
    - Enhanced image loading and display capabilities
    - Initialization argument tracking for debugging
    - Generic type system support for mixin functionality
    
    Args:
        parent: Parent window or panel
        size (tuple[int, int] | None): Control size as (width, height)
        pos (tuple[int, int] | None): Control position as (x, y)
        bitmap (wx.Bitmap | None): Initial bitmap to display
        style (int | None): wxPython StaticBitmap style flags
        
    Attributes:
        bitmap (wx.Bitmap): Displayed bitmap image
        size (tuple[int, int]): Control size
        
    Example:
        >>> bitmap = wx.Bitmap("image.png", wx.BITMAP_TYPE_PNG)
        >>> image = WrappedImage(panel, bitmap=bitmap)
        >>> image.size = (200, 150)  # Resize display
    """

    @property
    def bitmap(self) -> _wx.Bitmap:
        return self.GetBitmap()

    @bitmap.setter
    def bitmap(self, value: _wx.Bitmap):
        self.SetBitmap(value)


    @property
    def image(self) -> _wx.Image:
        return self.bitmap.ConvertToImage()

    @image.setter
    def image(self, value: _wx.Image | str):
        if isinstance(value, str):
            value = _wx.Image(value, _wx.BITMAP_TYPE_ANY)

        self.bitmap = _wx.Bitmap(value)


    def __init__(
        self,
        parent: _wx.Window,
        size: tuple[int, int] = _wx.DefaultSize,
        pos: tuple[int, int] = _wx.DefaultPosition,
        image_path: str | None = None,
        style: int = 0,
        *args, **kwds):

        # load image
        if image_path is not None:
            image = _wx.Image(image_path, _wx.BITMAP_TYPE_ANY)

        if size != (0, 0):
            image = image.Scale(size[0], size[1])

            bitmap = _wx.Bitmap(image)

        else:
            bitmap = _wx.NullBitmap

        # init superclass
        super().__init__(
            parent,
            bitmap = bitmap,
            size = size, pos = pos,
            style = style
        )

        # save args and kwds
        self.save_initialize_arguments(
            parent,
            size, pos,
            image_path = image_path,
            style = style,
            *args, **kwds
        )


class WrappedBoxSizer(_wx.BoxSizer):
    """Enhanced wx.Sizer wrapper with PEP 8 compliant interface.
    
    This class provides a Python-style interface to wxPython's wx.Sizer class,
    offering snake_case property names and enhanced functionality while
    maintaining full compatibility with the underlying Sizer object.
    
    The wrapper adds:
    - PEP 8 compliant property names and methods for sizer management
    - Enhanced layout and item handling capabilities
    - Initialization argument tracking for debugging
    - Generic type system support for mixin functionality
    
    Args:
        orient (int | None): Sizer orientation (wx.HORIZONTAL or wx.VERTICAL)
    """
    
    def __init__(self, orient: int):
        super().__init__(orient)

    
    def add(self, item, proportion: int = 0, flag: int = 0, border: int = 0):
        """Add an item to the sizer with specified layout options.
        
        Args:
            item: The item to add (window, sizer, or space)
            proportion (int): Proportion for resizing (default 0)
            flag (int): Layout flags (default 0)
            border (int): Border size in pixels (default 0)
        """
        return self.Add(item, proportion, flag, border)
    

# Export list for explicit module interface
__all__ = [
    # Core utility classes
    'Slots',
    'UIAttributes', 
    'UIInitializeComponent',
    'UIIndexor',
    
    # Main wrapped classes
    'WrappedApp',
    'WrappedWindow',
    'WrappedPanel',
    'WrappedButton',
    
    # Text and input controls
    'WrappedStaticText',
    'WrappedTextBox',
    
    # Selection controls  
    'WrappedCheckBox',
    'WrappedRadioBox',
    'WrappedListBox',
    'WrappedComboBox',
    'WrappedChoice',
    
    # Range controls
    'WrappedSlider',
    'WrappedGauge',
    
    # Container controls
    'WrappedListCtrl',
    'WrappedScrolledWindow',
    
    # Media controls
    'WrappedImage',
]

