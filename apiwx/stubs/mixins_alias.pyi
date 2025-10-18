"""Type stubs for apiwx.mixins_alias module.

This module provides type information for convenient type aliases for commonly 
used mixin class combinations in the apiwx framework, enabling proper type 
checking and IDE support.
"""

from typing import TypeAlias, Type, Any, Optional, Union
from .core import (
    App, Window, Panel, Button,
    TextBox, StaticText, CheckBox, RadioBox,
    ListBox, ComboBox, Slider, Gauge,
    ListCtrl, ScrolledWindow, Choice, Image
)
from .mixins_app import DetectWindow
from .mixins_window import DetectPanel, ByPanelSize
from .mixins_panel import DetectChildren, WithBoarder
from .mixins_base import Singleton, Multiton
from .mixins_common import AutoDetect, FixSize
from .mixins_core import BaseMixins
from .mixins_button import SingleClickDisable, DoubleClickOnly, ClickGuard
from .paneltransmodel import NotTransition, SupportTransit

# Application classes with mixin combinations
class AppBase(App):
    """Singleton application instance.
    
    This class creates a App with Singleton behavior, ensuring
    only one application instance can exist at a time.
    
    Equivalent to: App[Singleton]
    """
    def __init__(self, name: str = ..., redirect: bool = ...) -> None: ...

class AppDetectWindow(App):
    """Singleton application with window detection.
    
    This class creates a App with both Singleton behavior and
    automatic window detection capabilities.
    
    Equivalent to: App[Singleton, DetectWindow]
    """
    def __init__(self, name: str = ..., redirect: bool = ...) -> None: ...

# Window classes with mixin combinations
class WindowWithPanel(Window):
    """Window with automatic panel detection.
    
    This class creates a Window that automatically detects
    and manages child panels.
    
    Equivalent to: Window[DetectPanel]
    """
    def __init__(
        self,
        parent: Optional[Union[App, Window]] = ...,
        size: tuple[int, int] = ...,
        pos: tuple[int, int] = ...,
        title: str = ...,
        **kwargs: Any
    ) -> None: ...

class WindowByPanelSize(Window):
    """Window with panel detection and size management.
    
    This class creates a Window with panel detection and
    size management based on the client panel size.
    
    Equivalent to: Window[DetectPanel, ByPanelSize]
    """
    def __init__(
        self,
        parent: Optional[Union[App, Window]] = ...,
        size: tuple[int, int] = ...,
        pos: tuple[int, int] = ...,
        title: str = ...,
        **kwargs: Any
    ) -> None: ...

class WindowPanelTransit(Window):
    """Window with panel transition support.
    
    This class creates a Window that supports panel transitions
    and multi-panel management.
    
    Equivalent to: Window[SupportTransit]
    """
    def __init__(
        self,
        parent: Optional[Union[App, Window]] = ...,
        size: tuple[int, int] = ...,
        pos: tuple[int, int] = ...,
        title: str = ...,
        **kwargs: Any
    ) -> None: ...

class WindowSizeTransitWithPanel(Window):
    """Window with combined panel detection, sizing, and transitions.
    
    This class creates a Window with comprehensive panel management
    including detection, sizing, and transition support.
    
    Equivalent to: Window[SupportTransit, ByPanelSize]
    """
    def __init__(
        self,
        parent: Optional[Union[App, Window]] = ...,
        size: tuple[int, int] = ...,
        pos: tuple[int, int] = ...,
        title: str = ...,
        **kwargs: Any
    ) -> None: ...

# Panel classes with generic combinations
class PanelDetectChildren(Panel):
    """Panel with automatic child component detection.
    
    This class creates a Panel that automatically detects
    and manages child UI components.
    
    Equivalent to: Panel[DetectChildren]
    """
    def __init__(
        self,
        parent: Optional[Window] = ...,
        size: tuple[int, int] = ...,
        pos: tuple[int, int] = ...,
        **kwargs: Any
    ) -> None: ...

class PanelWithBoarder(Panel):
    """Panel with border drawing functionality.
    
    This class creates a Panel with configurable border
    drawing capabilities.
    
    Equivalent to: Panel[WithBoarder]
    """
    def __init__(
        self,
        parent: Optional[Window] = ...,
        size: tuple[int, int] = ...,
        pos: tuple[int, int] = ...,
        boarder_color: Optional[str] = ...,
        boarder_thickness: Optional[int] = ...,
        boarder_offset: Optional[int] = ...,
        **kwargs: Any
    ) -> None: ...

class PanelNoTransition(Panel):
    """Panel excluded from transition management.
    
    This class creates a Panel that is explicitly excluded
    from panel transition systems.
    
    Equivalent to: Panel[NotTransition]
    """
    def __init__(
        self,
        parent: Optional[Window] = ...,
        size: tuple[int, int] = ...,
        pos: tuple[int, int] = ...,
        **kwargs: Any
    ) -> None: ...

class ButtonSingleClickDisable(Button):
    """Button that disables after single click.
    
    This class creates a Button that automatically disables
    itself after being clicked to prevent double-clicks.
    
    Equivalent to: Button[SingleClickDisable]
    """
    def __init__(
        self,
        parent: Optional[Panel] = ...,
        size: tuple[int, int] = ...,
        pos: tuple[int, int] = ...,
        label: str = ...,
        disable_duration: Optional[float] = ...,
        auto_re_enable: bool = ...,
        **kwargs: Any
    ) -> None: ...

class ButtonDoubleClickOnly(Button):
    """Button that requires double-click to activate.
    
    This class creates a Button that only responds to
    double-clicks, ignoring single clicks.
    
    Equivalent to: Button[DoubleClickOnly]
    """
    def __init__(
        self,
        parent: Optional[Panel] = ...,
        size: tuple[int, int] = ...,
        pos: tuple[int, int] = ...,
        label: str = ...,
        double_click_timeout: Optional[float] = ...,
        show_single_click_feedback: bool = ...,
        **kwargs: Any
    ) -> None: ...

class ButtonClickGuard(Button):
    """Button with comprehensive click protection.
    
    This class creates a Button with multiple click protection
    mechanisms including guards and confirmations.
    
    Equivalent to: Button[ClickGuard]
    """
    def __init__(
        self,
        parent: Optional[Panel] = ...,
        size: tuple[int, int] = ...,
        pos: tuple[int, int] = ...,
        label: str = ...,
        require_double_click: bool = ...,
        disable_duration: float = ...,
        guard_message: Optional[str] = ...,
        **kwargs: Any
    ) -> None: ...

# TypeAlias definitions for backward compatibility
AppBase_Alias: TypeAlias = AppBase
AppDetectWindow_Alias: TypeAlias = AppDetectWindow
WindowWithPanel_Alias: TypeAlias = WindowWithPanel
WindowByPanelSize_Alias: TypeAlias = WindowByPanelSize
WindowPanelTransit_Alias: TypeAlias = WindowPanelTransit
WindowSizeTransitWithPanel_Alias: TypeAlias = WindowSizeTransitWithPanel
PanelDetectChildren_Alias: TypeAlias = PanelDetectChildren
PanelWithBoarder_Alias: TypeAlias = PanelWithBoarder
PanelNoTransition_Alias: TypeAlias = PanelNoTransition
ButtonSingleClickDisable_Alias: TypeAlias = ButtonSingleClickDisable
ButtonDoubleClickOnly_Alias: TypeAlias = ButtonDoubleClickOnly
ButtonClickGuard_Alias: TypeAlias = ButtonClickGuard

__all__: list[str]