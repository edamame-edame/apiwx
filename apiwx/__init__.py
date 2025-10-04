"""
apiwx package v0.4.0

Usage:
    from apiwx import (
    WrappedApp, WrappedWindow, WrappedPanel, WrappedButton,
    ALIGN_CENTER, Colour, Options, get_option
    )

    # Create an application and main window
    app = WrappedApp("MyApp")
    frame = WrappedWindow(app, size=(800, 600), pos=(100, 100), title="Demo", color=Colour.WHITE)

    # Add a panel and a button
    panel = WrappedPanel(frame, size=(800, 600), pos=(0, 0))
    button = WrappedButton(panel, size=(120, 40), pos=(20, 20), label="Click Me")

    # Connect an event slot
    def on_click(event):
    print("Button clicked!")
    button.slots_on_click += on_click

    # Use constants and colors
    frame.size = (640, 480)
    frame.color_background = Colour.LIGHT_GREY

    # Use UI argument utilities
    opt = get_option("theme", default="dark")

    app.mainloop()

Main Exports:
    - Core wxPython wrapper classes (Wrapped*)
    - Constants, flags, colors
    - FontManager, framestyle, signals, PanelTransModel
    - UI argument utilities (Options, exist_option, get_option, get_var)

See each module for details.
"""
# --- Constants, Flags, Colors ---
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

# --- Core Wrappers & UI ---
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

# --- Font, Debug, Panel Transform, Events --- 
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

# --- UI Arguments ---
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

# --- Generics Exports ---
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
    "WrappedListCtrl", "WrappedScrolledWindow", "WrappedChoice", "WrappedImage",
    # Font, Debug, Panel Transform, Events
    "FontManager", "PanelTransModel",
    # UI Arguments
    "Options", "exist_option", "get_option", "get_var",
    # Constants, Flags, Colors
    "ALIGN_LEFT", "ALIGN_TOP", "ALIGN_RIGHT", "ALIGN_BOTTOM", "ALIGN_CENTER",
    "WindowStyle", "ControlStyle", "BorderStyle", "TraversalStyle", "ExtraWindowStyle", "FrameStyle", "DialogStyle", "ControlBorderStyle", "MiscFlag",
    "Colors",
    # Generics
    "AutoDetect", "FixSize",
    # Base Generics
    "Singleton", "Multiton",
    # App, Window, Panel Generics
    "DetectWindow",
    "ByPanelSize", "DetectPanel",
    "WithBoarder", "DetectChildren",
    "NotTransition",
    # Button Generics
    "SingleClickDisable", "DoubleClickOnly", "ClickGuard",
    # Generics Aliases
    "AppBase", "AppDetectWindow",
    "WindowWithPanel", "WindowByPanelSize", "WindowPanelTransit", "WindowSizeTransitWithPanel",
    "PanelDetectChildren", "PanelWithBoarder", "PanelNoTransition",
    "ButtonClickGuard", "ButtonSingleClickDisable", "ButtonDoubleClickOnly",
    # Message Box Functionality
    "MessageBox", "MessageResult", "MessageType", "CustomMessageBox",
    "MessageButtons", "ProgressMessageBox", "InputDialog",
    "show_info", "show_warning", "show_error", "ask_question", "show_success",
    "get_text_input", "get_number_input", "get_choice_input",
    # Debug & Logging
    "Logger", "LogLevel", "uilog", "uidebug_log", "uiinfo_log", "uiwarning_log",
    "uierror_log", "uicritical_log", "uidebug_set_level", "uidebug_get_level", "uilog_output_remaining",
    "internallog", "internaldebug_log", "internalinfo_log", "internalwarning_log",
    "internalerror_log", "internalcritical_log", "internal_set_level", "internal_get_level", "internallog_output_remaining",
]

__version__ = "0.4.0"

