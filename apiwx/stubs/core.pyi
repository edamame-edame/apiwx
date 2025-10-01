"""Type stubs for apiwx.core module."""

from typing import Any, Callable, Optional, Union, TypeVar, Generic, Type, overload, Protocol
import wx

T = TypeVar('T')

class Slots(list[Callable[..., None]]):
    """Multiple slots for single signal."""
    
    def __init__(
        self,
        control: Union[wx.Control, wx.Window],
        signal: wx.PyEventBinder
    ) -> None: ...
    
    def append(self, slot: Callable[..., None]) -> None: ...
    def __iadd__(self, slot: Callable[..., None]) -> 'Slots': ...
    def __isub__(self, slot: Callable[..., None]) -> 'Slots': ...
    def __lshift__(self, slot: Callable[..., None]) -> 'Slots': ...

class UIAttributes:
    """wx attributes for PEP8 aliases and useful methods."""
    
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

class WrappedApp(wx.App, UIAttributes):
    """Wrapped wxPython App class."""
    
    def __init__(self, name: str = ..., redirect: bool = ...) -> None: ...
    def mainloop(self) -> None: ...
    @property
    def name(self) -> str: ...

class WrappedWindow(wx.Frame, UIAttributes):
    """Wrapped wxPython Frame/Window class."""
    
    def __init__(
        self,
        parent: Optional[Union[WrappedApp, 'WrappedWindow']] = ...,
        size: tuple[int, int] = ...,
        pos: tuple[int, int] = ...,
        title: str = ...,
        color: Optional[Any] = ...,
        **kwargs: Any
    ) -> None: ...

class WrappedPanel(wx.Panel, UIAttributes):
    """Wrapped wxPython Panel class."""
    
    def __init__(
        self,
        parent: Optional[WrappedWindow] = ...,
        size: tuple[int, int] = ...,
        pos: tuple[int, int] = ...,
        **kwargs: Any
    ) -> None: ...

class WrappedButton(wx.Button, UIAttributes):
    """Wrapped wxPython Button class."""
    
    def __init__(
        self,
        parent: Optional[WrappedPanel] = ...,
        size: tuple[int, int] = ...,
        pos: tuple[int, int] = ...,
        label: str = ...,
        **kwargs: Any
    ) -> None: ...
    
    @property
    def slots_on_click(self) -> Slots: ...

class WrappedStaticText(wx.StaticText, UIAttributes):
    """Wrapped wxPython StaticText class."""
    
    def __init__(
        self,
        parent: Optional[WrappedPanel] = ...,
        size: tuple[int, int] = ...,
        pos: tuple[int, int] = ...,
        label: str = ...,
        **kwargs: Any
    ) -> None: ...

class WrappedTextBox(wx.TextCtrl, UIAttributes):
    """Wrapped wxPython TextCtrl class."""
    
    def __init__(
        self,
        parent: Optional[WrappedPanel] = ...,
        size: tuple[int, int] = ...,
        pos: tuple[int, int] = ...,
        value: str = ...,
        **kwargs: Any
    ) -> None: ...

class WrappedCheckBox(wx.CheckBox, UIAttributes):
    """Wrapped wxPython CheckBox class."""
    
    def __init__(
        self,
        parent: Optional[WrappedPanel] = ...,
        size: tuple[int, int] = ...,
        pos: tuple[int, int] = ...,
        label: str = ...,
        **kwargs: Any
    ) -> None: ...

class WrappedRadioBox(wx.RadioBox, UIAttributes):
    """Wrapped wxPython RadioBox class."""
    
    def __init__(
        self,
        parent: Optional[WrappedPanel] = ...,
        size: tuple[int, int] = ...,
        pos: tuple[int, int] = ...,
        label: str = ...,
        **kwargs: Any
    ) -> None: ...

class WrappedListBox(wx.ListBox, UIAttributes):
    """Wrapped wxPython ListBox class."""
    
    def __init__(
        self,
        parent: Optional[WrappedPanel] = ...,
        size: tuple[int, int] = ...,
        pos: tuple[int, int] = ...,
        **kwargs: Any
    ) -> None: ...

class WrappedComboBox(wx.ComboBox, UIAttributes):
    """Wrapped wxPython ComboBox class."""
    
    def __init__(
        self,
        parent: Optional[WrappedPanel] = ...,
        size: tuple[int, int] = ...,
        pos: tuple[int, int] = ...,
        **kwargs: Any
    ) -> None: ...

class WrappedSlider(wx.Slider, UIAttributes):
    """Wrapped wxPython Slider class."""
    
    def __init__(
        self,
        parent: Optional[WrappedPanel] = ...,
        size: tuple[int, int] = ...,
        pos: tuple[int, int] = ...,
        **kwargs: Any
    ) -> None: ...

class WrappedGauge(wx.Gauge, UIAttributes):
    """Wrapped wxPython Gauge class."""
    
    def __init__(
        self,
        parent: Optional[WrappedPanel] = ...,
        size: tuple[int, int] = ...,
        pos: tuple[int, int] = ...,
        **kwargs: Any
    ) -> None: ...

class WrappedListCtrl(wx.ListCtrl, UIAttributes):
    """Wrapped wxPython ListCtrl class."""
    
    def __init__(
        self,
        parent: Optional[WrappedPanel] = ...,
        size: tuple[int, int] = ...,
        pos: tuple[int, int] = ...,
        **kwargs: Any
    ) -> None: ...

class WrappedScrolledWindow(wx.ScrolledWindow, UIAttributes):
    """Wrapped wxPython ScrolledWindow class."""
    
    def __init__(
        self,
        parent: Optional[WrappedPanel] = ...,
        size: tuple[int, int] = ...,
        pos: tuple[int, int] = ...,
        **kwargs: Any
    ) -> None: ...

class WrappedChoice(wx.Choice, UIAttributes):
    """Wrapped wxPython Choice class."""
    
    def __init__(
        self,
        parent: Optional[WrappedPanel] = ...,
        size: tuple[int, int] = ...,
        pos: tuple[int, int] = ...,
        **kwargs: Any
    ) -> None: ...

class WrappedImage(wx.StaticBitmap, UIAttributes):
    """Wrapped wxPython StaticBitmap for images."""
    
    def __init__(
        self,
        parent: Optional[WrappedPanel] = ...,
        size: tuple[int, int] = ...,
        pos: tuple[int, int] = ...,
        **kwargs: Any
    ) -> None: ...