"""Type stubs for apiwx.core module.

This module provides type information for the core wxPython wrapper classes
and utilities in apiwx v0.5.0, enabling proper type checking and IDE support.
"""

from typing import Any, Callable, Optional, Union, TypeVar, Generic, Type, overload, Protocol
from threading import Timer
import wx

T = TypeVar('T')

class Slots(list[Callable[..., None]]):
    """List-based container for multiple event handler slots with timeout.
    
    This class extends the built-in list to manage multiple callable
    event handlers (slots) for a single wxPython signal.
    """
    
    control: Union[wx.Control, wx.Window]
    signal: wx.PyEventBinder
    
    @property
    def timeout(self) -> float | None: ...
    @timeout.setter
    def timeout(self, value: float | None) -> None: ...
    
    def __init__(
        self,
        control: Union[wx.Control, wx.Window],
        signal: wx.PyEventBinder,
        timeout: float | None = ...
    ) -> None: ...
    
    def append(self, slot: Callable[..., None]) -> None: ...
    def __iadd__(self, slot: Callable[..., None]) -> 'Slots': ...
    def __isub__(self, slot: Callable[..., None]) -> 'Slots': ...
    def __lshift__(self, slot: Callable[..., None]) -> 'Slots': ...
    
    def _execute_slots_safely(self, *args: Any, **kwds: Any) -> None: ...
    def _slot_timeout(self) -> None: ...

class UIAttributes:
    """Mixin class providing PEP 8 compliant property aliases for wxPython.
    
    This class provides snake_case property aliases for common wxPython
    attributes and methods, making the interface more Pythonic.
    """
    
    @property
    def size(self) -> tuple[int, int]: ...
    @size.setter
    def size(self, value: tuple[int, int]) -> None: ...
    
    @property
    def clientsize(self) -> tuple[int, int]: ...
    @clientsize.setter
    def clientsize(self, value: tuple[int, int]) -> None: ...
    
    @property
    def size_max(self) -> tuple[int, int]: ...
    @size_max.setter
    def size_max(self, value: tuple[int, int]) -> None: ...
    
    @property
    def size_min(self) -> tuple[int, int]: ...
    @size_min.setter
    def size_min(self, value: tuple[int, int]) -> None: ...
    
    @property
    def pos(self) -> tuple[int, int]: ...
    @pos.setter
    def pos(self, value: tuple[int, int]) -> None: ...
    
    @property
    def color_foreground(self) -> str: ...
    @color_foreground.setter
    def color_foreground(self, value: str) -> None: ...
    
    @property
    def color_background(self) -> str: ...
    @color_background.setter
    def color_background(self, value: str) -> None: ...
    
    @property
    def text(self) -> str: ...
    @text.setter  
    def text(self, value: str | None) -> None: ...
    
    @property
    def bind_events(self) -> list[wx.PyEventBinder]: ...
    
    @property
    def font(self) -> str: ...
    @font.setter
    def font(self, value: str | wx.Font) -> None: ...
    
    @property
    def parent(self) -> Union[wx.Window, None]: ...
    
    @property
    def toplevel(self) -> Union[wx.TopLevelWindow, None]: ...
    
    def exists_slots(self, signal: wx.PyEventBinder) -> bool: ...
    def connect(
        self, 
        signal: wx.PyEventBinder, 
        slot: Callable[..., None], 
        timeout: float | None = ...
    ) -> None: ...
    def show(self) -> None: ...
    def hide(self) -> None: ...
    def enable(self) -> None: ...
    def disable(self) -> None: ...
    def destroy(self) -> None: ...
    def is_shown(self) -> bool: ...
    def is_enabled(self) -> bool: ...
    
    @classmethod
    def raise_attribute_error(cls, methodname: str, specclass: type) -> None: ...

class UIInitializeComponent:
    """Mixin class for tracking component initialization arguments.
    
    This class provides functionality to save and retrieve the arguments
    used during component initialization for debugging and serialization.
    """
    
    def save_initialize_arguments(self, *args: Any, **kwds: Any) -> None: ...
    
    @property
    def init_args(self) -> tuple: ...
    
    @property
    def init_kwds(self) -> dict: ...

class UIIndexor(int, UIAttributes):
    """Integer-based indexing with UI object integration.
    
    This class extends int to provide UI object integration capabilities
    for indexed access patterns.
    """
    
    @property
    def uiobject(self) -> UIAttributes: ...
    
    def __new__(cls, value: int, index_list: dict['UIIndexor', UIAttributes]) -> 'UIIndexor': ...
    def __getattribute__(self, name: str) -> Any: ...

class WrappedApp(wx.App, UIAttributes, UIInitializeComponent):
    """Enhanced wx.App with PEP 8 compliant interface.
    
    This class provides a Pythonic wrapper around wxPython's App class
    with improved attribute access and initialization tracking.
    """
    
    @property
    def app_name(self) -> str: ...
    
    def __init__(self, name: str = ..., redirect: bool = ..., **kwargs: Any) -> None: ...
    def mainloop(self) -> None: ...

class WrappedWindow(wx.Frame, UIAttributes, UIInitializeComponent):
    """Enhanced wx.Frame with improved attribute access.
    
    This class provides a Pythonic wrapper around wxPython's Frame class
    with property-based access patterns and PEP 8 compliance.
    """
    
    @property
    def slots_on_close(self) -> Slots: ...
    @property
    def slots_on_activate(self) -> Slots: ...
    @property
    def slots_on_iconize(self) -> Slots: ...
    @property
    def slots_on_maximize(self) -> Slots: ...
    
    def __init__(
        self,
        parent: Optional[Union[WrappedApp, 'WrappedWindow']] = ...,
        size: tuple[int, int] = ...,
        pos: tuple[int, int] = ...,
        title: str = ...,
        color: Optional[Any] = ...,
        **kwargs: Any
    ) -> None: ...

class WrappedPanel(wx.Panel, UIAttributes, UIInitializeComponent):
    """Enhanced wx.Panel with convenient properties.
    
    This class provides a Pythonic wrapper around wxPython's Panel class
    with improved attribute access and initialization tracking.
    """
    
    def __init__(
        self,
        parent: Optional[WrappedWindow] = ...,
        size: tuple[int, int] = ...,
        pos: tuple[int, int] = ...,
        **kwargs: Any
    ) -> None: ...

class WrappedStaticText(wx.StaticText, UIAttributes, UIInitializeComponent):
    """Enhanced wx.StaticText with PEP 8 compliant interface."""
    
    def __init__(
        self,
        parent: Optional[WrappedPanel] = ...,
        size: tuple[int, int] = ...,
        pos: tuple[int, int] = ...,
        text: str = ...,
        **kwargs: Any
    ) -> None: ...

class WrappedTextBox(wx.TextCtrl, UIAttributes, UIInitializeComponent):
    """Enhanced wx.TextCtrl with improved attribute access."""
    
    @property
    def slots_on_text(self) -> Slots: ...
    @property
    def slots_on_enter(self) -> Slots: ...
    
    def __init__(
        self,
        parent: Optional[WrappedPanel] = ...,
        size: tuple[int, int] = ...,
        pos: tuple[int, int] = ...,
        value: str = ...,
        **kwargs: Any
    ) -> None: ...

class WrappedButton(wx.Button, UIAttributes, UIInitializeComponent):
    """Enhanced wx.Button with event slot system."""
    
    @property
    def slots_on_click(self) -> Slots: ...
    
    def __init__(
        self,
        parent: Optional[WrappedPanel] = ...,
        size: tuple[int, int] = ...,
        pos: tuple[int, int] = ...,
        label: str = ...,
        **kwargs: Any
    ) -> None: ...

class WrappedCheckBox(wx.CheckBox, UIAttributes, UIInitializeComponent):
    """Enhanced wx.CheckBox with event slot system."""
    
    @property
    def slots_on_check(self) -> Slots: ...
    
    def __init__(
        self,
        parent: Optional[WrappedPanel] = ...,
        size: tuple[int, int] = ...,
        pos: tuple[int, int] = ...,
        label: str = ...,
        **kwargs: Any
    ) -> None: ...

class WrappedRadioBox(wx.RadioBox, UIAttributes, UIInitializeComponent):
    """Enhanced wx.RadioBox with event slot system."""
    
    @property
    def slots_on_select(self) -> Slots: ...
    
    def __init__(
        self,
        parent: Optional[WrappedPanel] = ...,
        size: tuple[int, int] = ...,
        pos: tuple[int, int] = ...,
        label: str = ...,
        choices: list[str] = ...,
        **kwargs: Any
    ) -> None: ...

class WrappedListBox(wx.ListBox, UIAttributes, UIInitializeComponent):
    """Enhanced wx.ListBox with event slot system."""
    
    @property
    def slots_on_select(self) -> Slots: ...
    @property
    def slots_on_double_click(self) -> Slots: ...
    
    def __init__(
        self,
        parent: Optional[WrappedPanel] = ...,
        size: tuple[int, int] = ...,
        pos: tuple[int, int] = ...,
        choices: list[str] = ...,
        **kwargs: Any
    ) -> None: ...

class WrappedComboBox(wx.ComboBox, UIAttributes, UIInitializeComponent):
    """Enhanced wx.ComboBox with event slot system."""
    
    @property
    def slots_on_select(self) -> Slots: ...
    @property
    def slots_on_text(self) -> Slots: ...
    
    def __init__(
        self,
        parent: Optional[WrappedPanel] = ...,
        size: tuple[int, int] = ...,
        pos: tuple[int, int] = ...,
        value: str = ...,
        choices: list[str] = ...,
        **kwargs: Any
    ) -> None: ...

class WrappedSlider(wx.Slider, UIAttributes, UIInitializeComponent):
    """Enhanced wx.Slider with event slot system."""
    
    @property
    def slots_on_scroll(self) -> Slots: ...
    
    def __init__(
        self,
        parent: Optional[WrappedPanel] = ...,
        size: tuple[int, int] = ...,
        pos: tuple[int, int] = ...,
        value: int = ...,
        min_value: int = ...,
        max_value: int = ...,
        **kwargs: Any
    ) -> None: ...

class WrappedGauge(wx.Gauge, UIAttributes, UIInitializeComponent):
    """Enhanced wx.Gauge with improved attribute access."""
    
    def __init__(
        self,
        parent: Optional[WrappedPanel] = ...,
        size: tuple[int, int] = ...,
        pos: tuple[int, int] = ...,
        range: int = ...,
        **kwargs: Any
    ) -> None: ...

class WrappedListCtrl(wx.ListCtrl, UIAttributes, UIInitializeComponent):
    """Enhanced wx.ListCtrl with event slot system."""
    
    @property
    def slots_on_select(self) -> Slots: ...
    @property
    def slots_on_item_activated(self) -> Slots: ...
    
    def __init__(
        self,
        parent: Optional[WrappedPanel] = ...,
        size: tuple[int, int] = ...,
        pos: tuple[int, int] = ...,
        **kwargs: Any
    ) -> None: ...

class WrappedScrolledWindow(wx.ScrolledWindow, UIAttributes, UIInitializeComponent):
    """Enhanced wx.ScrolledWindow with improved attribute access."""
    
    def __init__(
        self,
        parent: Optional[WrappedPanel] = ...,
        size: tuple[int, int] = ...,
        pos: tuple[int, int] = ...,
        **kwargs: Any
    ) -> None: ...

class WrappedChoice(wx.Choice, UIAttributes, UIInitializeComponent):
    """Enhanced wx.Choice with event slot system."""
    
    @property
    def slots_on_choice(self) -> Slots: ...
    
    def __init__(
        self,
        parent: Optional[WrappedPanel] = ...,
        size: tuple[int, int] = ...,
        pos: tuple[int, int] = ...,
        choices: list[str] = ...,
        **kwargs: Any
    ) -> None: ...

class WrappedImage(wx.StaticBitmap, UIAttributes, UIInitializeComponent):
    """Enhanced wx.StaticBitmap for image display."""
    
    def __init__(
        self,
        parent: Optional[WrappedPanel] = ...,
        size: tuple[int, int] = ...,
        pos: tuple[int, int] = ...,
        bitmap: Optional[wx.Bitmap] = ...,
        **kwargs: Any
    ) -> None: ...