import os
import sys
import typing
import webbrowser
import wx as _wx


try:
    from . import debug
except ImportError:
    import debug

try:
    from .generics_core import GenericsType
    from .fontmanager import FontManager

except ImportError:
    from generics_core import GenericsType
    from fontmanager import FontManager

try:
    from . import signals
    from . import framestyle
except ImportError:
    import signals
    import framestyle


class Slots(list[typing.Callable[..., None]]):
    '''
    # Multiple slots for single signal
    ### ( For wxPython classes )

    Usage:
    ```python

    class MyFrame(wx.Frame, UIAttributes):
    def __init__(self, *args, **kwds):
    super().__init__(*args, **kwds)

    # Add slots to EVT_CLOSE signal
    self.slots_on_close += self.on_close_slot1
    self.slots_on_close += self.on_close_slot2

    # Add slots to EVT_SIZE signal
    self.slots_on_size += self.on_size_slot1
    self.slots_on_size += self.on_size_slot2

    def on_close_slot1(self, event):
    print("Close slot 1")

    def on_close_slot2(self, event):
    print("Close slot 2")

    def on_size_slot1(self, event):
    print("Size slot 1")

    def on_size_slot2(self, event):
    print("Size slot 2")

    ```
    '''
    def __init__(
        self,
        control: _wx.Control | _wx.Window,
        signal: _wx.PyEventBinder):
        # init super class
        super().__init__()
    
        # set control and signal
        self.control = control
        self.signal = signal


    def append(self, slot: typing.Callable[..., None]):
        # is the first slot ?
        if(not self.control.exists_slots(self.signal)):
            # create connection
            self.control.connect(
                self.signal,
                self._safety_slot_call
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


    def _safety_slot_call(self, *args, **kwds): # TODO: async support ?
        for slot in self:
            try:
                slot(*args, **kwds)

            except Exception as e:
                debug.uilog(
                    "EXCEPT",
                    f"Slot exception was ignored."
                    f" ({e.__class__} was occurred in {slot.__name__})"
                )


class UIAttributes:
    '''
    ### wx attributes for PEP8 aliases
    ### and some useful methods
    ##### ( For wxPython classes )

    This class is used as a mixin class.
    ( For example, `class MyFrame(wx.Frame, UIAttributes): ...` )

    PEP8 documents ... https://peps.python.org/pep-0008/

    wxPython documents ... https://docs.wxpython.org/

    '''
    @property
    def size(self: _wx.Window) -> tuple[int, int]:
        return (
            tuple(self.GetSize())
        )

    @size.setter
    def size(self: _wx.Window, value: tuple[int, int]):
        self.SetSize(*value)


    @property
    def clientsize(self: _wx.Window) -> tuple[int, int]:
        return (
            tuple(self.GetClientSize())
        )

    @clientsize.setter
    def clientsize(self: _wx.Window, value: tuple[int, int]):
        self.SetClientSize(*value)


    @property
    def size_max(self: _wx.Window) -> tuple[int, int]:
        return (
            tuple(self.GetMaxSize())
        )

    @size_max.setter
    def size_max(self: _wx.Window, value: tuple[int, int]):
        self.SetMaxSize(_wx.Size(*value))


    @property
    def size_min(self: _wx.Window) -> tuple[int, int]:
        return (
            tuple(self.GetMinSize())
        )

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
        return f"#{
            ''.join(
            map(
                lambda hexstr: (
                        str.replace(
                            str(hexstr), "0x", ""
                        )
                    ),
                    self.GetForegroundColour()
                )
            )
        }"

    @color_foreground.setter
    def color_foreground(self: _wx.Window, value: str):
        self.SetForegroundColour(value)


    @property
    def color_background(self: _wx.Window) -> str:
        return f"#{
            ''.join(
                map(
                    lambda hexstr: (
                        str.replace(
                            str(hexstr), "0x", ""
                        )
                    ),
                    self.GetBackgroundColour()
                )
            )
        }"

    @color_background.setter
    def color_background(self: _wx.Window, value: str):
        self.SetBackgroundColour(value)


    @property
    def text(self: _wx.Control) -> str:
        if not isinstance(self, _wx.Control):
            self.not_exist_attribute(
                "text", "wx.Control"
            )

        return self.GetLabelText()

    @text.setter
    def text(self: _wx.Control, value: str | None) -> str:
        if not isinstance(self, _wx.Control):
            self.not_exist_attribute(
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
            self.not_exist_attribute(
                "font", "wx.TextAttr"
            )

        return FontManager.getkey_from_font(self.GetFont())

    @font.setter
    def font(self: _wx.TextAttr, value: str | _wx.Font):
        if not isinstance(self, _wx.TextAttr):
            self.not_exist_attribute(
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


    def exists_slots(self, signal: _wx.PyEventBinder):
        return signal in self.bind_events


    def connect(
        self: _wx.Control | typing.Type['UIAttributes'],
        signal: _wx.PyEventBinder,
        slot: typing.Callable[..., None]):
        # check class
        if not isinstance(self, _wx.Window):
            self.not_exist_attribute(
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


    def is_shown(self: _wx.Window) -> bool:
        return self.IsShown()


    @classmethod
    def not_exist_attribute(cls, methodname: str, specclass):
        raise AttributeError(
            f"The `{methodname}()` method is only valid"
            f" for objects of the `{specclass}` class."
        )


class UIInitializeComponent():
    '''
    # Save arguments of `__init__()` method
    ### ( For wxPython classes )
    '''

    def save_initialize_arguments(self, *args, **kwds):
        '''
        # Save arguments of `__init__()` method
        ### ( For wxPython classes )
        '''
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
    metaclass = GenericsType):
    '''
    # wx.App wrapped class
    This class exist only for PEP8 aliases.
    ( Same with `wx.App` )

    PEP8 documents ... https://peps.python.org/pep-0008/

    '''

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
    metaclass = GenericsType):
    '''
    # wx.Frame wrapped class
    This class exist only for PEP8 aliases.
    ( Same with `wx.Frame` )

    PEP8 documents ... https://peps.python.org/pep-0008/

    '''

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
        size: tuple[int, int], pos: tuple[int, int],
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
    metaclass = GenericsType):
    '''
    # wx.Panel wrapped class
    This class exist only for PEP8 aliases.
    ( Same with `wx.Panel` )

    PEP8 documents ... https://peps.python.org/pep-0008/

    '''

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
        size: tuple[int, int], pos: tuple[int, int],
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
    metaclass = GenericsType):
    '''
    # wx.StaticText wrapped class
    This class exist only for PEP8 aliases.
    ( Same with `wx.StaticText` )

    PEP8 documents ... https://peps.python.org/pep-0008/

    '''

    def __init__(
        self,
        parent: _wx.Window,
        size: tuple[int, int], pos: tuple[int, int],
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
    metaclass = GenericsType):
    '''
    # wx.TextCtrl wrapped class
    This class exist only for PEP8 aliases.
    ( Same with `wx.TextCtrl` )

    PEP8 documents ... https://peps.python.org/pep-0008/

    '''

    @property
    def value(self) -> str:
        return self.GetValue()

    @value.setter
    def value(self, value: str):
        self.SetValue(value)


    def __init__(
        self,
        parent: _wx.Window,
        size: tuple[int, int], pos: tuple[int, int],
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
    metaclass = GenericsType):
    '''
    # wx.Button wrapped class
    This class exist only for PEP8 aliases.
    ( Same with `wx.Button` )

    PEP8 documents ... https://peps.python.org/pep-0008/

    '''

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
        size: tuple[int, int], pos: tuple[int, int],
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
    metaclass = GenericsType):
    '''
    # wx.CheckBox wrapped class
    This class exist only for PEP8 aliases.
    ( Same with `wx.CheckBox` )

    PEP8 documents ... https://peps.python.org/pep-0008/

    '''
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
        size: tuple[int, int], pos: tuple[int, int],
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
    metaclass = GenericsType):
    '''
    # wx.RadioBox wrapped class
    This class exist only for PEP8 aliases.
    ( Same with `wx.RadioBox` )

    PEP8 documents ... https://peps.python.org/pep-0008/

    '''

    @property
    def selection(self) -> int:
        return self.GetSelection()

    @selection.setter
    def selection(self, value: int):
        self.SetSelection(value)


    def __init__(
        self,
        parent: _wx.Window,
        size: tuple[int, int], pos: tuple[int, int],
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
    metaclass = GenericsType):
    '''
    # wx.ListBox wrapped class
    This class exist only for PEP8 aliases.
    ( Same with `wx.ListBox` )

    PEP8 documents ... https://peps.python.org/pep-0008/

    '''

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
        size: tuple[int, int], pos: tuple[int, int],
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
    metaclass = GenericsType):
    '''
    # wx.ComboBox wrapped class
    This class exist only for PEP8 aliases.
    ( Same with `wx.ComboBox` )

    PEP8 documents ... https://peps.python.org/pep-0008/

    '''

    @property
    def value(self) -> str:
        return self.GetValue()

    @value.setter
    def value(self, value: str):
        self.SetValue(value)


    def __init__(
        self,
        parent: _wx.Window,
        size: tuple[int, int], pos: tuple[int, int],
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
    metaclass = GenericsType):
    '''
    # wx.Slider wrapped class
    This class exist only for PEP8 aliases.
    ( Same with `wx.Slider` )

    PEP8 documents ... https://peps.python.org/pep-0008/

    '''

    @property
    def value(self) -> int:
        return self.GetValue()

    @value.setter
    def value(self, value: int):
        self.SetValue(value)


    def __init__(
        self,
        parent: _wx.Window,
        size: tuple[int, int], pos: tuple[int, int],
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
    metaclass = GenericsType):
    '''
    # wx.Gauge wrapped class
    This class exist only for PEP8 aliases.
    ( Same with `wx.Gauge` )

    PEP8 documents ... https://peps.python.org/pep-0008/

    '''

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
        size: tuple[int, int], pos: tuple[int, int],
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
    metaclass = GenericsType):
    '''
    # wx.ListCtrl wrapped class
    This class exist only for PEP8 aliases.
    ( Same with `wx.ListCtrl` )

    PEP8 documents ... https://peps.python.org/pep-0008/

    '''

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
        size: tuple[int, int], pos: tuple[int, int],
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
    metaclass = GenericsType):
    '''
    # wx.ScrolledWindow wrapped class
    This class exist only for PEP8 aliases.
    ( Same with `wx.ScrolledWindow` )

    PEP8 documents ... https://peps.python.org/pep-0008/

    '''

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

        self.SetScrollRate(
            self._scroll_rate
        )


    def __init__(
        self,
        parent: _wx.Window,
        size: tuple[int, int], pos: tuple[int, int],
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
    metaclass = GenericsType):
    '''
    # wx.Choice wrapped class
    This class exist only for PEP8 aliases.
    ( Same with `wx.Choice` )

    PEP8 documents ... https://peps.python.org/pep-0008/

    '''

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
        size: tuple[int, int], pos: tuple[int, int],
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
    metaclass = GenericsType):
    '''
    # wx.StaticBitmap wrapped class
    This class exist only for PEP8 aliases.
    ( Same with `wx.StaticBitmap` )

    PEP8 documents ... https://peps.python.org/pep-0008/

    '''

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
        size: tuple[int, int], pos: tuple[int, int],
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

