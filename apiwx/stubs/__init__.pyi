"""Type stubs for apiwx package v0.5.0.

This package provides comprehensive type information for the apiwx library,
a simplified, type-safe interface to wxPython with advanced features including
generic type support, automatic component detection, and enhanced UI utilities.
"""

from typing import Any, Callable, Optional, Union, TypeVar, Generic, Type, overload
from typing import TypeAlias
import wx

# Version information
__version__: str = "0.5.0"

# Type variables
T = TypeVar('T')

# === Constants, Flags, and Colors ===
from .constants import *
from .styleflags import *
from .colors import *
from .framestyle import *

# === Core Wrappers and UI Components ===
from .core import (
    WrappedApp, WrappedWindow, WrappedPanel, WrappedStaticText,
    WrappedTextBox, WrappedButton, WrappedCheckBox, WrappedRadioBox,
    WrappedListBox, WrappedComboBox, WrappedSlider, WrappedGauge,
    WrappedListCtrl, WrappedScrolledWindow, WrappedChoice, WrappedImage,
    UIIndexor
)

# === Font Management ===
from .fontmanager import FontManager

# === Debug and Logging ===
from .debug import (
    Logger, LogLevel,
    uilog, uidebug_log, uiinfo_log, uiwarning_log, uierror_log, uicritical_log,
    uidebug_set_level, uidebug_get_level, uilog_output_remaining,
    internallog, internaldebug_log, internalinfo_log, internalwarning_log,
    internalerror_log, internalcritical_log, internal_set_level,
    internal_get_level, internallog_output_remaining
)

# === Panel Transition Model ===
from .paneltransmodel import PanelTransModel, NotTransition, SupportTransit

# === Signals and Events ===
from .signals import *

# === UI Arguments and Options ===
from .uiarg import Options, exist_option, get_option, get_var

# === Generic Type System ===
from .generics_common import AutoDetect, FixSize
from .generics_base import Singleton, Multiton
from .generics_app import DetectWindow
from .generics_window import ByPanelSize, DetectPanel
from .generics_panel import WithBoarder, DetectChildren
from .generics_button import SingleClickDisable, DoubleClickOnly, ClickGuard

# === Type Aliases ===
from .generics_alias import (
    AppBase, AppDetectWindow,
    WindowWithPanel, WindowByPanelSize, WindowPanelTransit, WindowSizeTransitWithPanel,
    PanelDetectChildren, PanelWithBoarder, PanelNoTransition,
    ButtonClickGuard, ButtonSingleClickDisable, ButtonDoubleClickOnly
)

# === Message Box Functionality ===
from .message import (
    MessageBox, MessageResult, MessageType, CustomMessageBox, MessageButtons,
    ProgressMessageBox, InputDialog,
    show_info, show_warning, show_error, ask_question, show_success,
    get_text_input, get_number_input, get_choice_input
)

# === Paint Tools ===
from .painttool import *

# Package exports (comprehensive __all__ for v0.5.0)
__all__: list[str]