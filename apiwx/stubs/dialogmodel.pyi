"""Type stubs for dialogmodel module."""

import wx
from typing import Optional, List, Tuple, Union


class DialogResult:
    """Result constants for dialog operations."""
    OK: int
    CANCEL: int
    YES: int
    NO: int


class BaseFileDialog:
    """Base class for file dialogs with common functionality."""
    
    def __init__(self, parent: Optional[wx.Window] = ...) -> None: ...
    
    @staticmethod
    def _get_parent() -> Optional[wx.Window]: ...
    
    @property
    def title(self) -> str: ...
    @title.setter
    def title(self, value: str) -> None: ...
    
    @property
    def initial_directory(self) -> str: ...
    @initial_directory.setter
    def initial_directory(self, value: str) -> None: ...
    
    @property
    def filename(self) -> str: ...
    @filename.setter
    def filename(self, value: str) -> None: ...
    
    @property
    def filter(self) -> str: ...
    @filter.setter
    def filter(self, value: str) -> None: ...
    
    @property
    def filter_index(self) -> int: ...
    @filter_index.setter
    def filter_index(self, value: int) -> None: ...
    
    @property
    def dialog_result(self) -> int: ...


class OpenFileDialog(BaseFileDialog):
    """File selection dialog for opening files."""
    
    def __init__(self, parent: Optional[wx.Window] = ...) -> None: ...
    
    @property
    def multiselect(self) -> bool: ...
    @multiselect.setter
    def multiselect(self, value: bool) -> None: ...
    
    @property
    def check_file_exists(self) -> bool: ...
    @check_file_exists.setter
    def check_file_exists(self, value: bool) -> None: ...
    
    @property
    def filenames(self) -> List[str]: ...
    
    @property
    def selected_filename(self) -> str: ...
    
    def show_dialog(self) -> int: ...


class SaveFileDialog(BaseFileDialog):
    """File selection dialog for saving files."""
    
    def __init__(self, parent: Optional[wx.Window] = ...) -> None: ...
    
    @property
    def overwrite_prompt(self) -> bool: ...
    @overwrite_prompt.setter
    def overwrite_prompt(self, value: bool) -> None: ...
    
    @property
    def create_prompt(self) -> bool: ...
    @create_prompt.setter
    def create_prompt(self, value: bool) -> None: ...
    
    @property
    def selected_filename(self) -> str: ...
    
    def show_dialog(self) -> int: ...


class FolderBrowserDialog:
    """Folder selection dialog."""
    
    def __init__(self, parent: Optional[wx.Window] = ...) -> None: ...
    
    @staticmethod
    def _get_parent() -> Optional[wx.Window]: ...
    
    @property
    def description(self) -> str: ...
    @description.setter
    def description(self, value: str) -> None: ...
    
    @property
    def selected_path(self) -> str: ...
    @selected_path.setter
    def selected_path(self, value: str) -> None: ...
    
    @property
    def show_new_folder_button(self) -> bool: ...
    @show_new_folder_button.setter
    def show_new_folder_button(self, value: bool) -> None: ...
    
    @property
    def dialog_result(self) -> int: ...
    
    def show_dialog(self) -> int: ...


# Convenience functions
def open_file_dialog(
    title: str = ...,
    filter: str = ...,
    initial_directory: str = ...,
    multiselect: bool = ...,
    parent: Optional[wx.Window] = ...
) -> Tuple[int, List[str]]: ...

def save_file_dialog(
    title: str = ...,
    filter: str = ...,
    initial_directory: str = ...,
    filename: str = ...,
    parent: Optional[wx.Window] = ...
) -> Tuple[int, str]: ...

def folder_browser_dialog(
    description: str = ...,
    selected_path: str = ...,
    parent: Optional[wx.Window] = ...
) -> Tuple[int, str]: ...