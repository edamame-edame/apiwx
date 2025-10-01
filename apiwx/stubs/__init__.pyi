"""Type stubs for apiwx package."""

from typing import Any, Callable, Optional, Union, TypeVar, Generic, Type, overload
import wx

# Version information
__version__: str = "0.3.1"

# Type variables
T = TypeVar('T')

# --- Core Wrappers & UI ---
class WrappedApp:
    def __init__(self, name: str = ..., redirect: bool = ...) -> None: ...
    def mainloop(self) -> None: ...
    @property
    def name(self) -> str: ...

class WrappedWindow:
    def __init__(
        self,
        parent: Optional[Union[WrappedApp, 'WrappedWindow']] = ...,
        size: tuple[int, int] = ...,
        pos: tuple[int, int] = ...,
        title: str = ...,
        color: Optional[Any] = ...,
        **kwargs: Any
    ) -> None: ...
    @property
    def size(self) -> tuple[int, int]: ...
    @size.setter
    def size(self, value: tuple[int, int]) -> None: ...
    @property
    def color_background(self) -> Any: ...
    @color_background.setter
    def color_background(self, value: Any) -> None: ...

class WrappedPanel:
    def __init__(
        self,
        parent: Optional[WrappedWindow] = ...,
        size: tuple[int, int] = ...,
        pos: tuple[int, int] = ...,
        **kwargs: Any
    ) -> None: ...

class WrappedButton:
    def __init__(
        self,
        parent: Optional[WrappedPanel] = ...,
        size: tuple[int, int] = ...,
        pos: tuple[int, int] = ...,
        label: str = ...,
        **kwargs: Any
    ) -> None: ...
    @property
    def slots_on_click(self) -> Any: ...

class WrappedStaticText:
    def __init__(
        self,
        parent: Optional[WrappedPanel] = ...,
        size: tuple[int, int] = ...,
        pos: tuple[int, int] = ...,
        label: str = ...,
        **kwargs: Any
    ) -> None: ...

class WrappedTextBox:
    def __init__(
        self,
        parent: Optional[WrappedPanel] = ...,
        size: tuple[int, int] = ...,
        pos: tuple[int, int] = ...,
        value: str = ...,
        **kwargs: Any
    ) -> None: ...

class WrappedCheckBox:
    def __init__(
        self,
        parent: Optional[WrappedPanel] = ...,
        size: tuple[int, int] = ...,
        pos: tuple[int, int] = ...,
        label: str = ...,
        **kwargs: Any
    ) -> None: ...

class WrappedRadioBox:
    def __init__(
        self,
        parent: Optional[WrappedPanel] = ...,
        size: tuple[int, int] = ...,
        pos: tuple[int, int] = ...,
        label: str = ...,
        **kwargs: Any
    ) -> None: ...

class WrappedListBox:
    def __init__(
        self,
        parent: Optional[WrappedPanel] = ...,
        size: tuple[int, int] = ...,
        pos: tuple[int, int] = ...,
        **kwargs: Any
    ) -> None: ...

class WrappedComboBox:
    def __init__(
        self,
        parent: Optional[WrappedPanel] = ...,
        size: tuple[int, int] = ...,
        pos: tuple[int, int] = ...,
        **kwargs: Any
    ) -> None: ...

class WrappedSlider:
    def __init__(
        self,
        parent: Optional[WrappedPanel] = ...,
        size: tuple[int, int] = ...,
        pos: tuple[int, int] = ...,
        **kwargs: Any
    ) -> None: ...

class WrappedGauge:
    def __init__(
        self,
        parent: Optional[WrappedPanel] = ...,
        size: tuple[int, int] = ...,
        pos: tuple[int, int] = ...,
        **kwargs: Any
    ) -> None: ...

class WrappedListCtrl:
    def __init__(
        self,
        parent: Optional[WrappedPanel] = ...,
        size: tuple[int, int] = ...,
        pos: tuple[int, int] = ...,
        **kwargs: Any
    ) -> None: ...

class WrappedScrolledWindow:
    def __init__(
        self,
        parent: Optional[WrappedPanel] = ...,
        size: tuple[int, int] = ...,
        pos: tuple[int, int] = ...,
        **kwargs: Any
    ) -> None: ...

class WrappedChoice:
    def __init__(
        self,
        parent: Optional[WrappedPanel] = ...,
        size: tuple[int, int] = ...,
        pos: tuple[int, int] = ...,
        **kwargs: Any
    ) -> None: ...

class WrappedImage:
    def __init__(
        self,
        parent: Optional[WrappedPanel] = ...,
        size: tuple[int, int] = ...,
        pos: tuple[int, int] = ...,
        **kwargs: Any
    ) -> None: ...

# --- Font, Debug, Panel Transform, Events ---
class FontManager:
    def __init__(self) -> None: ...

class Logger:
    def __init__(self, name: str) -> None: ...

class LogLevel:
    DEBUG: int
    INFO: int
    WARNING: int
    ERROR: int
    CRITICAL: int

def uilog(message: str, level: int = ...) -> None: ...
def uidebug_log(message: str) -> None: ...
def uiinfo_log(message: str) -> None: ...
def uiwarning_log(message: str) -> None: ...
def uierror_log(message: str) -> None: ...
def uicritical_log(message: str) -> None: ...
def uidebug_set_level(level: int) -> None: ...
def uidebug_get_level() -> int: ...
def uilog_output_remaining() -> None: ...

def internallog(message: str, level: int = ...) -> None: ...
def internaldebug_log(message: str) -> None: ...
def internalinfo_log(message: str) -> None: ...
def internalwarning_log(message: str) -> None: ...
def internalerror_log(message: str) -> None: ...
def internalcritical_log(message: str) -> None: ...
def internal_set_level(level: int) -> None: ...
def internal_get_level() -> int: ...
def internallog_output_remaining() -> None: ...

class PanelTransModel:
    def __init__(self) -> None: ...

class NotTransition:
    def __init__(self) -> None: ...

# --- UI Arguments ---
class Options:
    def __init__(self, **kwargs: Any) -> None: ...

def exist_option(key: str) -> bool: ...
def get_option(key: str, default: Any = ...) -> Any: ...
def get_var(key: str) -> Any: ...

# --- Constants, Flags, Colors ---
ALIGN_LEFT: int
ALIGN_TOP: int
ALIGN_RIGHT: int
ALIGN_BOTTOM: int
ALIGN_CENTER: int

class WindowStyle:
    DEFAULT_FRAME_STYLE: int
    DEFAULT_DIALOG_STYLE: int

class ControlStyle:
    DEFAULT: int

class BorderStyle:
    NONE: int
    SIMPLE: int
    RAISED: int
    SUNKEN: int

class TraversalStyle:
    WANT_CHARS: int

class ExtraWindowStyle:
    BLOCK_EVENTS: int

class FrameStyle:
    CAPTION: int
    MINIMIZE_BOX: int
    MAXIMIZE_BOX: int
    CLOSE_BOX: int
    SYSTEM_MENU: int
    RESIZE_BORDER: int

class DialogStyle:
    CAPTION: int
    CLOSE_BOX: int
    SYSTEM_MENU: int

class ControlBorderStyle:
    NONE: int
    SIMPLE: int

class MiscFlag:
    EXPAND: int
    ALL: int

class Colour:
    WHITE: Any
    BLACK: Any
    RED: Any
    GREEN: Any
    BLUE: Any
    YELLOW: Any
    CYAN: Any
    MAGENTA: Any
    LIGHT_GREY: Any
    DARK_GREY: Any

class Colors:
    WHITE: Any
    BLACK: Any
    RED: Any
    GREEN: Any
    BLUE: Any
    YELLOW: Any
    CYAN: Any
    MAGENTA: Any
    LIGHT_GREY: Any
    DARK_GREY: Any

# --- Generics ---
class AutoDetect(Generic[T]):
    def __init__(self, target_class: Type[T]) -> None: ...

class FixSize:
    def __init__(self, width: int, height: int) -> None: ...

# --- Base Generics ---
class Singleton:
    def __init__(self) -> None: ...

class Multiton:
    def __init__(self) -> None: ...

# --- App, Window, Panel Generics ---
DetectWindow: Type[AutoDetect[WrappedWindow]]

class ByPanelSize:
    def __init__(self) -> None: ...

DetectPanel: Type[AutoDetect[WrappedPanel]]

class WithBoarder:
    def __init__(self) -> None: ...

DetectChildren: Type[AutoDetect[Any]]

# --- Button Generics ---
class SingleClickDisable:
    def __init__(self) -> None: ...

class DoubleClickOnly:
    def __init__(self) -> None: ...

class ClickGuard:
    def __init__(self) -> None: ...

DetectButton: Type[AutoDetect[WrappedButton]]

# --- Generics Aliases ---
AppBase: Type[WrappedApp]
AppDetectWindow: Type[WrappedApp]
WindowWithPanel: Type[WrappedWindow]
WindowByPanelSize: Type[WrappedWindow]
WindowPanelTransit: Type[WrappedWindow]
PanelDetectChildren: Type[WrappedPanel]
PanelWithBoarder: Type[WrappedPanel]
PanelNoTransition: Type[WrappedPanel]
ButtonClickGuard: Type[WrappedButton]
ButtonSingleClickDisable: Type[WrappedButton]
ButtonDoubleClickOnly: Type[WrappedButton]
ButtonDetect: Type[WrappedButton]

# --- Message Box Functionality ---
class MessageBox:
    def __init__(self) -> None: ...

class MessageResult:
    OK: int
    CANCEL: int
    YES: int
    NO: int

class MessageType:
    INFO: int
    WARNING: int
    ERROR: int
    QUESTION: int

class CustomMessageBox:
    def __init__(self) -> None: ...

class MessageButtons:
    OK: int
    OK_CANCEL: int
    YES_NO: int
    YES_NO_CANCEL: int

class ProgressMessageBox:
    def __init__(self) -> None: ...

class InputDialog:
    def __init__(self) -> None: ...

def show_info(message: str, title: str = ...) -> int: ...
def show_warning(message: str, title: str = ...) -> int: ...
def show_error(message: str, title: str = ...) -> int: ...
def ask_question(message: str, title: str = ...) -> int: ...
def show_success(message: str, title: str = ...) -> int: ...
def get_text_input(message: str, title: str = ..., default: str = ...) -> Optional[str]: ...
def get_number_input(message: str, title: str = ..., default: int = ...) -> Optional[int]: ...
def get_choice_input(message: str, choices: list[str], title: str = ...) -> Optional[str]: ...