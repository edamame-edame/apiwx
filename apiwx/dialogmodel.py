"""File dialog wrapper for wxPython with enhanced functionality.

This module provides simplified and enhanced file dialog functionality
compatible with C# Windows Forms OpenFileDialog and SaveFileDialog patterns.
It includes open file, save file, and folder selection dialogs with
comprehensive error handling and logging.

Key Features:
    - OpenFileDialog - File selection for opening
    - SaveFileDialog - File selection for saving  
    - FolderBrowserDialog - Folder selection
    - Multiple file selection support
    - File type filters with wildcards
    - Default directory and filename settings
    - Consistent API with other apiwx  classes

Classes:
    BaseFileDialog: Base functionality for all file dialogs
    OpenFileDialog: File selection for opening files
    SaveFileDialog: File selection for saving files  
    FolderBrowserDialog: Folder selection dialog
"""
import wx
import os
from typing import Optional, List, Tuple, Union
from pathlib import Path

try:
    from . import debug
    from .debug import LogLevel
except ImportError:
    import debug
    from debug import LogLevel


class DialogResult:
    """Result constants for dialog operations, matching C# conventions."""
    OK = wx.ID_OK
    CANCEL = wx.ID_CANCEL
    YES = wx.ID_YES  
    NO = wx.ID_NO


class BaseFileDialog:
    """Base class for file dialogs with common functionality.
    
    This class provides the foundation for all file dialog types,
    including common properties and methods that match C# dialog patterns.
    """
    
    def __init__(self, parent: Optional[wx.Window] = None):
        """Initialize base file dialog.
        
        Args:
            parent: Parent window for the dialog, or None for auto-detection.
        """
        self._parent = parent or self._get_parent()
        self._title = "Select File"
        self._initial_directory = ""
        self._filename = ""
        self._filter = "All files (*.*)|*.*"
        self._filter_index = 0
        self._dialog_result = DialogResult.CANCEL
        
    @staticmethod
    def _get_parent() -> Optional[wx.Window]:
        """Get the best parent window for the dialog."""
        try:
            # Try to get the top-level window
            app = wx.GetApp()
            if app:
                top_window = app.GetTopWindow()
                if top_window:
                    return top_window
        except:
            pass
        return None
    
    @property
    def title(self) -> str:
        """Get or set the dialog title."""
        return self._title
    
    @title.setter
    def title(self, value: str):
        """Set the dialog title."""
        self._title = value
    
    @property
    def initial_directory(self) -> str:
        """Get or set the initial directory."""
        return self._initial_directory
    
    @initial_directory.setter
    def initial_directory(self, value: str):
        """Set the initial directory."""
        if value and os.path.isdir(value):
            self._initial_directory = value
        else:
            debug.uilog("DIALOG", f"Invalid directory: {value}", LogLevel.WARNING)
    
    @property
    def filename(self) -> str:
        """Get or set the default filename."""
        return self._filename
    
    @filename.setter
    def filename(self, value: str):
        """Set the default filename."""
        self._filename = value
    
    @property
    def filter(self) -> str:
        """Get or set the file filter string."""
        return self._filter
    
    @filter.setter
    def filter(self, value: str):
        """Set the file filter string.
        
        Format: "Description (*.ext)|*.ext|All files (*.*)|*.*"
        Example: "Text files (*.txt)|*.txt|All files (*.*)|*.*"
        """
        self._filter = value
    
    @property
    def filter_index(self) -> int:
        """Get or set the selected filter index (0-based)."""
        return self._filter_index
    
    @filter_index.setter
    def filter_index(self, value: int):
        """Set the selected filter index."""
        self._filter_index = max(0, value)
    
    @property
    def dialog_result(self) -> int:
        """Get the result of the last dialog operation."""
        return self._dialog_result


class OpenFileDialog(BaseFileDialog):
    """File selection dialog for opening files.
    
    This class provides functionality similar to C# OpenFileDialog,
    allowing users to select one or multiple files for opening.
    
    Example:
        >>> dialog = OpenFileDialog()
        >>> dialog.title = "Open Document"
        >>> dialog.filter = "Text files (*.txt)|*.txt|All files (*.*)|*.*"
        >>> dialog.multiselect = True
        >>> 
        >>> if dialog.show_dialog() == DialogResult.OK:
        ...     for filename in dialog.filenames:
        ...         print(f"Selected: {filename}")
    """
    
    def __init__(self, parent: Optional[wx.Window] = None):
        """Initialize OpenFileDialog.
        
        Args:
            parent: Parent window for the dialog.
        """
        super().__init__(parent)
        self._title = "Open File"
        self._multiselect = False
        self._filenames: List[str] = []
        self._check_file_exists = True
        
    @property
    def multiselect(self) -> bool:
        """Get or set whether multiple files can be selected."""
        return self._multiselect
    
    @multiselect.setter
    def multiselect(self, value: bool):
        """Set multiselect mode."""
        self._multiselect = value
    
    @property
    def check_file_exists(self) -> bool:
        """Get or set whether to check if files exist."""
        return self._check_file_exists
    
    @check_file_exists.setter
    def check_file_exists(self, value: bool):
        """Set file existence checking."""
        self._check_file_exists = value
    
    @property
    def filenames(self) -> List[str]:
        """Get the list of selected filenames."""
        return self._filenames.copy()
    
    @property
    def selected_filename(self) -> str:
        """Get the first selected filename (for compatibility)."""
        return self._filenames[0] if self._filenames else ""
    
    def show_dialog(self) -> int:
        """Show the open file dialog.
        
        Returns:
            DialogResult.OK if user selected files, DialogResult.CANCEL if cancelled.
        """
        style = wx.FD_OPEN
        if self._multiselect:
            style |= wx.FD_MULTIPLE
        if self._check_file_exists:
            style |= wx.FD_FILE_MUST_EXIST
            
        try:
            with wx.FileDialog(
                self._parent,
                message=self._title,
                defaultDir=self._initial_directory,
                defaultFile=self._filename,
                wildcard=self._filter,
                style=style
            ) as dialog:
                
                dialog.SetFilterIndex(self._filter_index)
                
                if dialog.ShowModal() == wx.ID_OK:
                    self._filenames = dialog.GetPaths()
                    self._filter_index = dialog.GetFilterIndex()
                    self._dialog_result = DialogResult.OK
                    
                    debug.uilog("DIALOG", 
                               f"Files selected: {len(self._filenames)} file(s)")
                    return DialogResult.OK
                else:
                    self._filenames = []
                    self._dialog_result = DialogResult.CANCEL
                    debug.uilog("DIALOG", "File selection cancelled")
                    return DialogResult.CANCEL
                    
        except Exception as e:
            debug.uilog("DIALOG", f"Error showing open file dialog: {e}", 
                       LogLevel.ERROR)
            self._filenames = []
            self._dialog_result = DialogResult.CANCEL
            return DialogResult.CANCEL


class SaveFileDialog(BaseFileDialog):
    """File selection dialog for saving files.
    
    This class provides functionality similar to C# SaveFileDialog,
    allowing users to select a location and filename for saving.
    
    Example:
        >>> dialog = SaveFileDialog()
        >>> dialog.title = "Save Document"
        >>> dialog.filter = "Text files (*.txt)|*.txt|All files (*.*)|*.*"
        >>> dialog.filename = "document.txt"
        >>> 
        >>> if dialog.show_dialog() == DialogResult.OK:
        ...     print(f"Save to: {dialog.selected_filename}")
    """
    
    def __init__(self, parent: Optional[wx.Window] = None):
        """Initialize SaveFileDialog.
        
        Args:
            parent: Parent window for the dialog.
        """
        super().__init__(parent)
        self._title = "Save File"
        self._overwrite_prompt = True
        self._create_prompt = False
        self._selected_filename = ""
        
    @property
    def overwrite_prompt(self) -> bool:
        """Get or set whether to prompt before overwriting files."""
        return self._overwrite_prompt
    
    @overwrite_prompt.setter
    def overwrite_prompt(self, value: bool):
        """Set overwrite prompting."""
        self._overwrite_prompt = value
    
    @property
    def create_prompt(self) -> bool:
        """Get or set whether to prompt before creating new files."""
        return self._create_prompt
    
    @create_prompt.setter
    def create_prompt(self, value: bool):
        """Set create prompting."""
        self._create_prompt = value
    
    @property
    def selected_filename(self) -> str:
        """Get the selected filename for saving."""
        return self._selected_filename
    
    def show_dialog(self) -> int:
        """Show the save file dialog.
        
        Returns:
            DialogResult.OK if user selected a file, DialogResult.CANCEL if cancelled.
        """
        style = wx.FD_SAVE
        if self._overwrite_prompt:
            style |= wx.FD_OVERWRITE_PROMPT
            
        try:
            with wx.FileDialog(
                self._parent,
                message=self._title,
                defaultDir=self._initial_directory,
                defaultFile=self._filename,
                wildcard=self._filter,
                style=style
            ) as dialog:
                
                dialog.SetFilterIndex(self._filter_index)
                
                if dialog.ShowModal() == wx.ID_OK:
                    self._selected_filename = dialog.GetPath()
                    self._filter_index = dialog.GetFilterIndex()
                    self._dialog_result = DialogResult.OK
                    
                    debug.uilog("DIALOG", 
                               f"Save file selected: {self._selected_filename}")
                    return DialogResult.OK
                else:
                    self._selected_filename = ""
                    self._dialog_result = DialogResult.CANCEL
                    debug.uilog("DIALOG", "Save file selection cancelled")
                    return DialogResult.CANCEL
                    
        except Exception as e:
            debug.uilog("DIALOG", f"Error showing save file dialog: {e}", 
                       LogLevel.ERROR)
            self._selected_filename = ""
            self._dialog_result = DialogResult.CANCEL
            return DialogResult.CANCEL


class FolderBrowserDialog:
    """Folder selection dialog.
    
    This class provides functionality similar to C# FolderBrowserDialog,
    allowing users to select a folder/directory.
    
    Example:
        >>> dialog = FolderBrowserDialog()
        >>> dialog.description = "Select output folder"
        >>> dialog.selected_path = "C:\\Users"
        >>> 
        >>> if dialog.show_dialog() == DialogResult.OK:
        ...     print(f"Selected folder: {dialog.selected_path}")
    """
    
    def __init__(self, parent: Optional[wx.Window] = None):
        """Initialize FolderBrowserDialog.
        
        Args:
            parent: Parent window for the dialog.
        """
        self._parent = parent or self._get_parent()
        self._description = "Select Folder"
        self._selected_path = ""
        self._show_new_folder_button = True
        self._dialog_result = DialogResult.CANCEL
        
    @staticmethod
    def _get_parent() -> Optional[wx.Window]:
        """Get the best parent window for the dialog."""
        try:
            app = wx.GetApp()
            if app:
                top_window = app.GetTopWindow()
                if top_window:
                    return top_window
        except:
            pass
        return None
    
    @property
    def description(self) -> str:
        """Get or set the description text shown in the dialog."""
        return self._description
    
    @description.setter
    def description(self, value: str):
        """Set the description text."""
        self._description = value
    
    @property
    def selected_path(self) -> str:
        """Get or set the selected folder path."""
        return self._selected_path
    
    @selected_path.setter
    def selected_path(self, value: str):
        """Set the initial selected folder path."""
        if value and os.path.isdir(value):
            self._selected_path = value
        else:
            debug.uilog("DIALOG", f"Invalid folder path: {value}", LogLevel.WARNING)
    
    @property
    def show_new_folder_button(self) -> bool:
        """Get or set whether to show the 'New Folder' button."""
        return self._show_new_folder_button
    
    @show_new_folder_button.setter
    def show_new_folder_button(self, value: bool):
        """Set new folder button visibility."""
        self._show_new_folder_button = value
    
    @property
    def dialog_result(self) -> int:
        """Get the result of the last dialog operation."""
        return self._dialog_result
    
    def show_dialog(self) -> int:
        """Show the folder browser dialog.
        
        Returns:
            DialogResult.OK if user selected a folder, DialogResult.CANCEL if cancelled.
        """
        style = wx.DD_DEFAULT_STYLE
        if not self._show_new_folder_button:
            style = wx.DD_DIR_MUST_EXIST
            
        try:
            with wx.DirDialog(
                self._parent,
                message=self._description,
                defaultPath=self._selected_path,
                style=style
            ) as dialog:
                
                if dialog.ShowModal() == wx.ID_OK:
                    self._selected_path = dialog.GetPath()
                    self._dialog_result = DialogResult.OK
                    
                    debug.uilog("DIALOG", 
                               f"Folder selected: {self._selected_path}")
                    return DialogResult.OK
                else:
                    self._dialog_result = DialogResult.CANCEL
                    debug.uilog("DIALOG", "Folder selection cancelled")
                    return DialogResult.CANCEL
                    
        except Exception as e:
            debug.uilog("DIALOG", f"Error showing folder dialog: {e}", 
                       LogLevel.ERROR)
            self._dialog_result = DialogResult.CANCEL
            return DialogResult.CANCEL


# Convenience functions for quick usage (matching apiwx message.py pattern)
def open_file_dialog(
    title: str = "Open File",
    filter: str = "All files (*.*)|*.*",
    initial_directory: str = "",
    multiselect: bool = False,
    parent: Optional[wx.Window] = None
) -> Tuple[int, List[str]]:
    """Quick open file dialog.
    
    Args:
        title: Dialog title.
        filter: File filter string.
        initial_directory: Initial directory to show.
        multiselect: Whether to allow multiple file selection.
        parent: Parent window.
        
    Returns:
        Tuple of (result, filenames_list).
    """
    dialog = OpenFileDialog(parent)
    dialog.title = title
    dialog.filter = filter
    dialog.initial_directory = initial_directory
    dialog.multiselect = multiselect
    
    result = dialog.show_dialog()
    return result, dialog.filenames


def save_file_dialog(
    title: str = "Save File",
    filter: str = "All files (*.*)|*.*",
    initial_directory: str = "",
    filename: str = "",
    parent: Optional[wx.Window] = None
) -> Tuple[int, str]:
    """Quick save file dialog.
    
    Args:
        title: Dialog title.
        filter: File filter string.
        initial_directory: Initial directory to show.
        filename: Default filename.
        parent: Parent window.
        
    Returns:
        Tuple of (result, selected_filename).
    """
    dialog = SaveFileDialog(parent)
    dialog.title = title
    dialog.filter = filter
    dialog.initial_directory = initial_directory
    dialog.filename = filename
    
    result = dialog.show_dialog()
    return result, dialog.selected_filename


def folder_browser_dialog(
    description: str = "Select Folder",
    selected_path: str = "",
    parent: Optional[wx.Window] = None
) -> Tuple[int, str]:
    """Quick folder browser dialog.
    
    Args:
        description: Description text for the dialog.
        selected_path: Initial folder path.
        parent: Parent window.
        
    Returns:
        Tuple of (result, selected_path).
    """
    dialog = FolderBrowserDialog(parent)
    dialog.description = description
    dialog.selected_path = selected_path
    
    result = dialog.show_dialog()
    return result, dialog.selected_path
