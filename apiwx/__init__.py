"""apiwx - A comprehensive wxPython wrapper library v0.5.0.

This package provides a simplified, type-safe interface to wxPython with
advanced features including generic type support, automatic component
detection, and enhanced UI utilities.

Basic Usage:
    >>> from apiwx import (
    ...     WrappedApp, WrappedWindow, WrappedPanel, WrappedButton,
    ...     ALIGN_CENTER, Colors, Options, get_option
    ... )
    >>> 
    >>> # Create an application and main window
    >>> app = WrappedApp("MyApp")
    >>> frame = WrappedWindow(
    ...     app, size=(800, 600), pos=(100, 100), 
    ...     title="Demo", color=Colors.WHITE
    ... )
    >>> 
    >>> # Add a panel and a button
    >>> panel = WrappedPanel(frame, size=(800, 600), pos=(0, 0))
    >>> button = WrappedButton(
    ...     panel, size=(120, 40), pos=(20, 20), label="Click Me"
    ... )
    >>> 
    >>> # Connect an event slot
    >>> def on_click(event):
    ...     print("Button clicked!")
    >>> button.slots_on_click += on_click
    >>> 
    >>> # Use constants and colors
    >>> frame.size = (640, 480)
    >>> frame.color_background = Colors.LIGHT_GREY
    >>> 
    >>> # Use UI argument utilities
    >>> opt = get_option("theme", default="dark")
    >>> 
    >>> app.mainloop()

Main Export Categories:
    Core Wrappers: WrappedApp, WrappedWindow, WrappedPanel, WrappedButton, etc.
    Constants & Flags: ALIGN_*, WindowStyle, ControlStyle, BorderStyle, etc.
    Colors: Colors class with predefined color constants
    Generics: Singleton, Multiton, AutoDetect, DetectChildren, etc.
    Type Aliases: AppBase, WindowWithPanel, PanelDetectChildren, etc.
    UI Utilities: FontManager, MessageBox, Options, logging functions
    Event System: Signals, slots, and event handling utilities

For detailed documentation, see individual module docstrings.
"""

# Constants, Flags, and Colors
try:
    # Try relative import (for installed package)
    from .constants import *
    from .styleflags import *
    from .colors import *

except ImportError:
    # Fall back to absolute import (for direct execution)
    from constants import *
    from styleflags import *
    from colors import *


# Core Wrappers and UI Components
try:
    from .core import (
        WrappedApp,
        WrappedWindow,
        WrappedPanel,
        WrappedStaticText,
        WrappedTextBox,
        WrappedButton,
        WrappedCheckBox,
        WrappedRadioBox,
        WrappedListBox,
        WrappedComboBox,
        WrappedSlider,
        WrappedGauge,
        WrappedListCtrl,
        WrappedScrolledWindow,
        WrappedChoice,
        WrappedImage,
    )

except ImportError:
    from core import (
        WrappedApp,
        WrappedWindow,
        WrappedPanel,
        WrappedStaticText,
        WrappedTextBox,
        WrappedButton,
        WrappedCheckBox,
        WrappedRadioBox,
        WrappedListBox,
        WrappedComboBox,
        WrappedSlider,
        WrappedGauge,
        WrappedListCtrl,
        WrappedScrolledWindow,
        WrappedChoice,
        WrappedImage,
    )


# Font Management, Debug, Panel Transform, and Events
try:
    from .fontmanager import (
        FontManager
    )

except ImportError:
    from fontmanager import (
        FontManager
    )

try:
    from .debug import (
        Logger,
        LogLevel,
        uilog,
        uidebug_log,
        uiinfo_log,
        uiwarning_log,
        uierror_log,
        uicritical_log,
        uidebug_set_level,
        uidebug_get_level,
        uilog_output_remaining,
        internallog,
        internaldebug_log,
        internalinfo_log,
        internalwarning_log,
        internalerror_log,
        internalcritical_log,
        internal_set_level,
        internal_get_level,
        internallog_output_remaining,
    )

except ImportError:
    from debug import (
        Logger,
        LogLevel,
        uilog,
        uidebug_log,
        uiinfo_log,
        uiwarning_log,
        uierror_log,
        uicritical_log,
        uidebug_set_level,
        uidebug_get_level,
        uilog_output_remaining,
        internallog,
        internaldebug_log,
        internalinfo_log,
        internalwarning_log,
        internalerror_log,
        internalcritical_log,
        internal_set_level,
        internal_get_level,
        internallog_output_remaining,
    )

try:
    from .framestyle import *

except ImportError:
    from framestyle import *

try:
    from .paneltransmodel import (
        PanelTransModel, NotTransition
    )

except ImportError:
    from paneltransmodel import (
        PanelTransModel, NotTransition
    )

try:
    from .signals import *

except ImportError:
    from signals import *


# UI Arguments and Options
try:
    from .uiarg import (
        Options,
        exist_option,
        get_option,
        get_var,
    )

except ImportError:
    from uiarg import (
        Options,
        exist_option,
        get_option,
        get_var,
    )


# Generic Type System Exports
try:
    from .generics_common import (
        AutoDetect,
        FixSize,
    )

except ImportError:
    from generics_common import (
        AutoDetect,
        FixSize,
    )

try:
    from .generics_base import (
        Singleton,
        Multiton,
    )

except ImportError:
    from generics_base import (
        Singleton,
        Multiton,
    )

try:
    from .generics_app import (
        DetectWindow,
    )

except ImportError:
    from generics_app import (
        DetectWindow,
    )

try:
    from .generics_window import (
        ByPanelSize,
        DetectPanel,
    )

except ImportError:
    from generics_window import (
        ByPanelSize,
        DetectPanel,
    )

try:
    from .generics_panel import (
        WithBoarder,
        DetectChildren,
    )

except ImportError:
    from generics_panel import (
        WithBoarder,
        DetectChildren,
    )

try:
    from .generics_button import (
        SingleClickDisable,
        DoubleClickOnly,
        ClickGuard,
    )

except ImportError:
    from generics_button import (
        SingleClickDisable,
        DoubleClickOnly,
        ClickGuard,
    )

try:
    from .generics_alias import (
        AppBase,
        AppDetectWindow,
        WindowWithPanel,
        WindowByPanelSize,
        WindowPanelTransit,
        WindowSizeTransitWithPanel,
        PanelDetectChildren,
        PanelWithBoarder,
        PanelNoTransition,
        ButtonClickGuard,
        ButtonSingleClickDisable,
        ButtonDoubleClickOnly,
    )

except ImportError:
    from generics_alias import (
        AppBase,
        AppDetectWindow,
        WindowWithPanel,
        WindowByPanelSize,
        WindowPanelTransit,
        WindowSizeTransitWithPanel,
        PanelDetectChildren,
        PanelWithBoarder,
        PanelNoTransition,
        ButtonClickGuard,
        ButtonSingleClickDisable,
        ButtonDoubleClickOnly,
    )

try:
    from .message import (
        MessageBox,
        MessageResult,
        MessageType,
        CustomMessageBox,
        MessageButtons,
        ProgressMessageBox,
        InputDialog,
        show_info,
        show_warning,
        show_error,
        ask_question,
        show_success,
        get_text_input,
        get_number_input,
        get_choice_input,
    )

except ImportError:
    from message import (
        MessageBox,
        MessageResult,
        MessageType,
        CustomMessageBox,
        MessageButtons,
        ProgressMessageBox,
        InputDialog,
        show_info,
        show_warning,
        show_error,
        ask_question,
        show_success,
        get_text_input,
        get_number_input,
        get_choice_input,
    )


__all__ = [
    # Core Wrappers
    "WrappedApp", "WrappedWindow", "WrappedPanel", "WrappedStaticText",
    "WrappedTextBox", "WrappedButton", "WrappedCheckBox", "WrappedRadioBox",
    "WrappedListBox", "WrappedComboBox", "WrappedSlider", "WrappedGauge",
    "WrappedListCtrl", "WrappedScrolledWindow", "WrappedChoice", 
    "WrappedImage",
    
    # Font, Debug, Panel Transform, Events
    "FontManager", "PanelTransModel",
    
    # UI Arguments
    "Options", "exist_option", "get_option", "get_var",
    
    # Constants and Alignment
    "ALIGN_LEFT", "ALIGN_TOP", "ALIGN_RIGHT", "ALIGN_BOTTOM", "ALIGN_CENTER",
    
    # Style Classes
    "WindowStyle", "ControlStyle", "BorderStyle", "TraversalStyle", 
    "ExtraWindowStyle", "FrameStyle", "DialogStyle", "ControlBorderStyle", 
    "MiscFlag",
    
    # Colors
    "Colors",
    
    # Generics
    "AutoDetect", "FixSize",
    
    # Base Generics
    "Singleton", "Multiton",
    
    # App, Window, Panel Generics
    "DetectWindow", "ByPanelSize", "DetectPanel", "WithBoarder", 
    "DetectChildren", "NotTransition",
    
    # Button Generics
    "SingleClickDisable", "DoubleClickOnly", "ClickGuard",
    
    # Application Aliases
    "AppBase", "AppDetectWindow",
    
    # Window Aliases
    "WindowWithPanel", "WindowByPanelSize", "WindowPanelTransit", 
    "WindowSizeTransitWithPanel",
    
    # Panel Aliases
    "PanelDetectChildren", "PanelWithBoarder", "PanelNoTransition",
    
    # Button Aliases
    "ButtonClickGuard", "ButtonSingleClickDisable", "ButtonDoubleClickOnly",
    
    # Message Box Classes
    "MessageBox", "MessageResult", "MessageType", "CustomMessageBox",
    "MessageButtons", "ProgressMessageBox", "InputDialog",
    
    # Message Box Functions
    "show_info", "show_warning", "show_error", "ask_question", "show_success",
    "get_text_input", "get_number_input", "get_choice_input",
    
    # Debug & Logging Functions
    "Logger", "LogLevel", "uilog", "uidebug_log", "uiinfo_log", 
    "uiwarning_log", "uierror_log", "uicritical_log", "uidebug_set_level", 
    "uidebug_get_level", "uilog_output_remaining",
    
    # Internal Logging Functions
    "internallog", "internaldebug_log", "internalinfo_log", 
    "internalwarning_log", "internalerror_log", "internalcritical_log", 
    "internal_set_level", "internal_get_level", "internallog_output_remaining",
]


__version__ = "0.5.1"

# Type stub information for PEP 561 compliance
# Type stubs are included in the apiwx.stubs subpackage
__stub_package__ = "apiwx.stubs"

