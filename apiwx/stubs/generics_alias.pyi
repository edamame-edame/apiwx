"""Type stubs for apiwx.generics_alias module.

This module provides type information for convenient type aliases for commonly 
used generic class combinations in the apiwx framework, enabling proper type 
checking and IDE support.
"""

from typing import TypeAlias, Type, Any, Optional, Union
from .core import (
    WrappedApp, WrappedWindow, WrappedPanel, WrappedButton,
    WrappedTextBox, WrappedStaticText, WrappedCheckBox, WrappedRadioBox,
    WrappedListBox, WrappedComboBox, WrappedSlider, WrappedGauge,
    WrappedListCtrl, WrappedScrolledWindow, WrappedChoice, WrappedImage
)
from .generics_app import DetectWindow
from .generics_window import DetectPanel, ByPanelSize
from .generics_panel import DetectChildren, WithBoarder
from .generics_base import Singleton, Multiton
from .generics_common import AutoDetect, FixSize
from .generics_core import BaseGenerics
from .generics_button import SingleClickDisable, DoubleClickOnly, ClickGuard
from .paneltransmodel import NotTransition, SupportTransit

# Application classes with generic combinations
class AppBase(WrappedApp):
    """Singleton application instance.
    
    This class creates a WrappedApp with Singleton behavior, ensuring
    only one application instance can exist at a time.
    
    Equivalent to: WrappedApp[Singleton]
    """
    def __init__(self, name: str = ..., redirect: bool = ...) -> None: ...

class AppDetectWindow(WrappedApp):
    """Singleton application with window detection.
    
    This class creates a WrappedApp with both Singleton behavior and
    automatic window detection capabilities.
    
    Equivalent to: WrappedApp[Singleton, DetectWindow]
    """
    def __init__(self, name: str = ..., redirect: bool = ...) -> None: ...

# Window classes with generic combinations
class WindowWithPanel(WrappedWindow):
    """Window with automatic panel detection.
    
    This class creates a WrappedWindow that automatically detects
    and manages child panels.
    
    Equivalent to: WrappedWindow[DetectPanel]
    """
    def __init__(
        self,
        parent: Optional[Union[WrappedApp, WrappedWindow]] = ...,
        size: tuple[int, int] = ...,
        pos: tuple[int, int] = ...,
        title: str = ...,
        **kwargs: Any
    ) -> None: ...

class WindowByPanelSize(WrappedWindow):
    """Window with panel detection and size management.
    
    This class creates a WrappedWindow with panel detection and
    size management based on the client panel size.
    
    Equivalent to: WrappedWindow[DetectPanel, ByPanelSize]
    """
    def __init__(
        self,
        parent: Optional[Union[WrappedApp, WrappedWindow]] = ...,
        size: tuple[int, int] = ...,
        pos: tuple[int, int] = ...,
        title: str = ...,
        **kwargs: Any
    ) -> None: ...

class WindowPanelTransit(WrappedWindow):
    """Window with panel transition support.
    
    This class creates a WrappedWindow that supports panel transitions
    and multi-panel management.
    
    Equivalent to: WrappedWindow[SupportTransit]
    """
    def __init__(
        self,
        parent: Optional[Union[WrappedApp, WrappedWindow]] = ...,
        size: tuple[int, int] = ...,
        pos: tuple[int, int] = ...,
        title: str = ...,
        **kwargs: Any
    ) -> None: ...

class WindowSizeTransitWithPanel(WrappedWindow):
    """Window with combined panel detection, sizing, and transitions.
    
    This class creates a WrappedWindow with comprehensive panel management
    including detection, sizing, and transition support.
    
    Equivalent to: WrappedWindow[SupportTransit, ByPanelSize]
    """
    def __init__(
        self,
        parent: Optional[Union[WrappedApp, WrappedWindow]] = ...,
        size: tuple[int, int] = ...,
        pos: tuple[int, int] = ...,
        title: str = ...,
        **kwargs: Any
    ) -> None: ...

# Panel classes with generic combinations
class PanelDetectChildren(WrappedPanel):
    """Panel with automatic child component detection.
    
    This class creates a WrappedPanel that automatically detects
    and manages child UI components.
    
    Equivalent to: WrappedPanel[DetectChildren]
    """
    def __init__(
        self,
        parent: Optional[WrappedWindow] = ...,
        size: tuple[int, int] = ...,
        pos: tuple[int, int] = ...,
        **kwargs: Any
    ) -> None: ...

class PanelWithBoarder(WrappedPanel):
    """Panel with border drawing functionality.
    
    This class creates a WrappedPanel with configurable border
    drawing capabilities.
    
    Equivalent to: WrappedPanel[WithBoarder]
    """
    def __init__(
        self,
        parent: Optional[WrappedWindow] = ...,
        size: tuple[int, int] = ...,
        pos: tuple[int, int] = ...,
        boarder_color: Optional[str] = ...,
        boarder_thickness: Optional[int] = ...,
        boarder_offset: Optional[int] = ...,
        **kwargs: Any
    ) -> None: ...

class PanelNoTransition(WrappedPanel):
    """Panel excluded from transition management.
    
    This class creates a WrappedPanel that is explicitly excluded
    from panel transition systems.
    
    Equivalent to: WrappedPanel[NotTransition]
    """
    def __init__(
        self,
        parent: Optional[WrappedWindow] = ...,
        size: tuple[int, int] = ...,
        pos: tuple[int, int] = ...,
        **kwargs: Any
    ) -> None: ...

class ButtonSingleClickDisable(WrappedButton):
    """Button that disables after single click.
    
    This class creates a WrappedButton that automatically disables
    itself after being clicked to prevent double-clicks.
    
    Equivalent to: WrappedButton[SingleClickDisable]
    """
    def __init__(
        self,
        parent: Optional[WrappedPanel] = ...,
        size: tuple[int, int] = ...,
        pos: tuple[int, int] = ...,
        label: str = ...,
        disable_duration: Optional[float] = ...,
        auto_re_enable: bool = ...,
        **kwargs: Any
    ) -> None: ...

class ButtonDoubleClickOnly(WrappedButton):
    """Button that requires double-click to activate.
    
    This class creates a WrappedButton that only responds to
    double-clicks, ignoring single clicks.
    
    Equivalent to: WrappedButton[DoubleClickOnly]
    """
    def __init__(
        self,
        parent: Optional[WrappedPanel] = ...,
        size: tuple[int, int] = ...,
        pos: tuple[int, int] = ...,
        label: str = ...,
        double_click_timeout: Optional[float] = ...,
        show_single_click_feedback: bool = ...,
        **kwargs: Any
    ) -> None: ...

class ButtonClickGuard(WrappedButton):
    """Button with comprehensive click protection.
    
    This class creates a WrappedButton with multiple click protection
    mechanisms including guards and confirmations.
    
    Equivalent to: WrappedButton[ClickGuard]
    """
    def __init__(
        self,
        parent: Optional[WrappedPanel] = ...,
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