"""Type stubs for apiwx.message module.

This module provides type information for enhanced message box functionality
including message boxes, custom dialogs, progress dialogs, and input dialogs
with comprehensive error handling and logging.
"""

from typing import Optional, Union
from enum import Enum
import wx

class MessageType(Enum):
    """Message box types with predefined styles."""
    INFO: MessageType
    WARNING: MessageType
    ERROR: MessageType
    QUESTION: MessageType
    SUCCESS: MessageType

class MessageResult(Enum):
    """Standardized message box results."""
    OK: int
    CANCEL: int
    YES: int
    NO: int
    CLOSE: int
    HELP: int
    UNKNOWN: int

class MessageBox:
    """Enhanced message box wrapper for wxPython."""
    
    @staticmethod
    def _get_parent() -> Optional[wx.Window]: ...
    
    @staticmethod
    def _get_style_for_type(msg_type: MessageType) -> int: ...
    
    @staticmethod
    def _show_message(
        message: str,
        title: str = ...,
        style: int = ...,
        parent: Optional[wx.Window] = ...
    ) -> MessageResult: ...
    
    @staticmethod
    def info(
        message: str,
        title: str = ...,
        parent: Optional[wx.Window] = ...
    ) -> MessageResult: ...
    
    @staticmethod
    def warning(
        message: str,
        title: str = ...,
        parent: Optional[wx.Window] = ...
    ) -> MessageResult: ...
    
    @staticmethod
    def error(
        message: str,
        title: str = ...,
        parent: Optional[wx.Window] = ...
    ) -> MessageResult: ...
    
    @staticmethod
    def question(
        message: str,
        title: str = ...,
        parent: Optional[wx.Window] = ...
    ) -> MessageResult: ...
    
    @staticmethod
    def success(
        message: str,
        title: str = ...,
        parent: Optional[wx.Window] = ...
    ) -> MessageResult: ...

class MessageButtons(Enum):
    """Predefined button combinations for message dialogs."""
    OK: int
    OK_CANCEL: int
    YES_NO: int
    YES_NO_CANCEL: int
    CLOSE: int

class CustomMessageBox:
    """Advanced message box with full customization."""
    
    message: str
    title: str
    buttons: int
    icon: int
    default_button: Optional[MessageResult]
    parent: Optional[wx.Window]
    
    def __init__(
        self,
        message: str,
        title: str = ...,
        buttons: Union[MessageButtons, int] = ...,
        icon: int = ...,
        default_button: Optional[MessageResult] = ...,
        parent: Optional[wx.Window] = ...
    ) -> None: ...
    
    def show(self) -> MessageResult: ...

class ProgressMessageBox:
    """Progress message box for long-running operations."""
    
    message: str
    title: str
    parent: Optional[wx.Window]
    _dialog: Optional[wx.ProgressDialog]
    _is_shown: bool
    
    def __init__(
        self,
        message: str,
        title: str = ...,
        parent: Optional[wx.Window] = ...
    ) -> None: ...
    
    def show(self) -> None: ...
    def update_message(self, message: str, progress: Optional[int] = ...) -> None: ...
    def close(self) -> None: ...

class InputDialog:
    """Input dialog for getting text from user."""
    
    @staticmethod
    def get_text(
        message: str,
        title: str = ...,
        default_value: str = ...,
        parent: Optional[wx.Window] = ...
    ) -> Optional[str]: ...
    
    @staticmethod
    def get_number(
        message: str,
        title: str = ...,
        default_value: int = ...,
        min_value: int = ...,
        max_value: int = ...,
        parent: Optional[wx.Window] = ...
    ) -> Optional[int]: ...
    
    @staticmethod
    def get_choice(
        message: str,
        choices: list[str],
        title: str = ...,
        parent: Optional[wx.Window] = ...
    ) -> Optional[str]: ...

# Convenience functions
def show_info(message: str, title: str = ...) -> MessageResult: ...
def show_warning(message: str, title: str = ...) -> MessageResult: ...
def show_error(message: str, title: str = ...) -> MessageResult: ...
def ask_question(message: str, title: str = ...) -> bool: ...
def show_success(message: str, title: str = ...) -> MessageResult: ...
def get_text_input(message: str, title: str = ..., default: str = ...) -> Optional[str]: ...
def get_number_input(
    message: str,
    title: str = ...,
    default: int = ...,
    min_val: int = ...,
    max_val: int = ...
) -> Optional[int]: ...
def get_choice_input(message: str, choices: list[str], title: str = ...) -> Optional[str]: ...

__all__: list[str]