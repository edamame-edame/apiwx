"""apiwx - A comprehensive wxPython wrapper library v0.5.2.

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
    Mixins: Singleton, Multiton, AutoDetect, DetectChildren, etc.
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
        Slots,
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
        WrappedBoxSizer,
    )

except ImportError:
    from core import (
        Slots,
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
        WrappedBoxSizer,
    )

# Mutable List View Components
try:
    from .mutablelistview import (
        AbstractMutableListNode,
        MutableListView,
    )

except ImportError:
    from mutablelistview import (
        AbstractMutableListNode,
        MutableListView,
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
        PanelTransModel, NotTransition, SupportTransit
    )

except ImportError:
    from paneltransmodel import (
        PanelTransModel, NotTransition, SupportTransit
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


# Mixin Type System Exports
try:
    from .mixins_common import (
        AutoDetect,
        FixSize,
    )

except ImportError:
    from mixins_common import (
        AutoDetect,
        FixSize,
    )

try:
    from .mixins_base import (
        Singleton,
        Multiton,
    )

except ImportError:
    from mixins_base import (
        Singleton,
        Multiton,
    )

try:
    from .mixins_app import (
        DetectWindow,
    )

except ImportError:
    from mixins_app import (
        DetectWindow,
    )

try:
    from .mixins_window import (
        ByPanelSize,
        DetectPanel,
    )

except ImportError:
    from mixins_window import (
        ByPanelSize,
        DetectPanel,
    )

try:
    from .mixins_panel import (
        WithBoarder,
        DetectChildren,
    )

except ImportError:
    from mixins_panel import (
        WithBoarder,
        DetectChildren,
    )

try:
    from .mixins_button import (
        SingleClickDisable,
        DoubleClickOnly,
        ClickGuard,
    )

except ImportError:
    from mixins_button import (
        SingleClickDisable,
        DoubleClickOnly,
        ClickGuard,
    )

try:
    from .mixins_statictext import (
        TextAlign,
        LocateByParent,
    )

except ImportError:
    from mixins_statictext import (
        TextAlign,
        LocateByParent,
    )

try:
    from .mixins_alias import (
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
    from mixins_alias import (
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

# === File Dialog Functionality ===
try:
    from .dialogmodel import (
        DialogResult,
        BaseFileDialog,
        OpenFileDialog,
        SaveFileDialog,
        FolderBrowserDialog,
        open_file_dialog,
        save_file_dialog,
        folder_browser_dialog,
    )

except ImportError:
    from dialogmodel import (
        DialogResult,
        BaseFileDialog,
        OpenFileDialog,
        SaveFileDialog,
        FolderBrowserDialog,
        open_file_dialog,
        save_file_dialog,
        folder_browser_dialog,
    )


__all__ = [
    # Core Wrappers
    "Slots",
    "WrappedApp", "WrappedWindow", "WrappedPanel", "WrappedStaticText",
    "WrappedTextBox", "WrappedButton", "WrappedCheckBox", "WrappedRadioBox",
    "WrappedListBox", "WrappedComboBox", "WrappedSlider", "WrappedGauge",
    "WrappedListCtrl", "WrappedScrolledWindow", "WrappedChoice", 
    "WrappedImage", "WrappedBoxSizer",
    
    # Mutable List View Components
    "AbstractMutableListNode", "MutableListView",
    
    # Font, Debug, Panel Transform, Events
    "FontManager", "PanelTransModel", "NotTransition", "SupportTransit",
    
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
    
    # Mixins
    "AutoDetect", "FixSize",
    
    # Base Mixins
    "Singleton", "Multiton",
    
    # App, Window, Panel Mixins
    "DetectWindow", "ByPanelSize", "DetectPanel", "WithBoarder", 
    "DetectChildren", "NotTransition",
    
    # Button Mixins
    "SingleClickDisable", "DoubleClickOnly", "ClickGuard",
    
    # StaticText Mixins
    "TextAlign", "LocateByParent",
    
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
    
    # File Dialog Classes
    "DialogResult", "BaseFileDialog", "OpenFileDialog", "SaveFileDialog", 
    "FolderBrowserDialog",
    
    # File Dialog Functions
    "open_file_dialog", "save_file_dialog", "folder_browser_dialog",
    
    # Debug & Logging Functions
    "Logger", "LogLevel", "uilog", "uidebug_log", "uiinfo_log", 
    "uiwarning_log", "uierror_log", "uicritical_log", "uidebug_set_level", 
    "uidebug_get_level", "uilog_output_remaining",
    
    # Internal Logging Functions
    "internallog", "internaldebug_log", "internalinfo_log", 
    "internalwarning_log", "internalerror_log", "internalcritical_log", 
    "internal_set_level", "internal_get_level", "internallog_output_remaining",
]


__version__ = "0.5.10"

# Type stub information for PEP 561 compliance
# Type stubs are included in the apiwx.stubs subpackage
__stub_package__ = "apiwx.stubs"

