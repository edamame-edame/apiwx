""""""


import enum
from typing import (
    Union, List
)

import wx as _wx

try:
    from . import core

except ImportError:
    import core

try:
    from . import mixins_core
    
except ImportError:
    import mixins_core


class DialogResult(enum.IntEnum):
    """Enumeration for dialog result codes."""
    OK = _wx.ID_OK
    CANCEL = _wx.ID_CANCEL
    YES = _wx.ID_YES
    NO = _wx.ID_NO


class FileFolderDialogAttributes:
    """FileDialog and FolderDialog common attributes mixin."""
    @property
    def title(self: Union[_wx.FileDialog, _wx.DirDialog]) -> str:
        """Get the dialog title.

        Returns:
            str: The title of the dialog.
        """
        return self.GetTitle()
    
    @title.setter
    def title(self: Union[_wx.FileDialog, _wx.DirDialog], value: str) -> None:
        """Set the dialog title.

        Args:
            value (str): The new title for the dialog.
        """
        self.SetTitle(value)


    @property
    def message(self: Union[_wx.FileDialog, _wx.DirDialog]) -> str:
        """Get the dialog message.

        Returns:
            str: The message of the dialog.
        """
        return self.GetMessage()
    
    @message.setter
    def message(self: Union[_wx.FileDialog, _wx.DirDialog], value: str) -> None:
        """Set the dialog message.

        Args:
            value (str): The new message for the dialog.
        """
        self.SetMessage(value)


    def show_dialog(self: Union[_wx.FileDialog, _wx.DirDialog]) -> DialogResult:
        """Show the file dialog.

        Returns:
            DialogResult: The result code of the dialog (e.g., wx.ID_OK or wx.ID_CANCEL).
        """
        if self.__class__ == FileDialog:
            raise NotImplementedError(
                "Direct instantiation of FileDialog is not allowed. \n"
                "Please subclass FileDialog and use show_dialog() method."
            )
        
        return DialogResult(self.ShowModal())


class FileDialog(
        _wx.FileDialog,
        core.UIAttributes,
        core.UIInitializeComponent,
        FileFolderDialogAttributes,
        metaclass=mixins_core.MixinsType):
    """File dialog wrapper with enhanced initialization."""
    @property
    def filter(self) -> str:
        """Get the dialog file filter.

        Returns:
            str: The file filter of the file dialog.
        """
        return self.GetWildcard()
    
    @filter.setter
    def filter(self, value: str) -> None:
        """Set the dialog file filter.

        Args:
            value (str): The new file filter for the file dialog.
        """
        self.SetWildcard(value)


    @property
    def filename(self) -> str:
        """Get the selected filename.

        Returns:
            str: The selected filename in the file dialog.
        """
        return (self.filenames[0]
                 if self.multiselect
                 else self.GetPath())

    @property
    def safe_filename(self) -> str:
        """Get the selected only filename.

        Returns:
            str: The selected only filename in the file dialog.
        """
        return (self.safe_filenames[0]
                if self.multiselect
                else self.GetFilename())

    @property
    def filenames(self) -> List[str]:
        """Get the list of selected filenames.

        Returns:
            List[str]: The list of selected filenames in the file dialog.
        """
        return self.GetPaths()
    

    @property
    def safe_filenames(self) -> List[str]:
        """Get the list of selected only filenames.

        Returns:
            List[str]: The list of selected only filenames in the file dialog.
        """
        return self.GetFilenames()
    
    
    @property
    def initial_filename(self) -> str:
        """Get the initial filename of the dialog.

        Returns:
            str: The initial filename set in the file dialog.
        """
        return self._initial_filename or ""
    

    @property
    def multiselect(self: Union[_wx.FileDialog, _wx.DirDialog]) -> bool:
        """Check if multiselect is enabled.

        Returns:
            bool: True if multiselect is enabled, False otherwise.
        """
        return bool(self.GetWindowStyle() & _wx.FD_MULTIPLE)
    
    @multiselect.setter
    def multiselect(self: Union[_wx.FileDialog, _wx.DirDialog], value: bool) -> None:
        """Enable or disable multiselect.

        Args:
            value (bool): True to enable multiselect, False to disable.
        """
        style = self.GetWindowStyle()

        if value:
            style |= _wx.FD_MULTIPLE
        else:
            style &= ~_wx.FD_MULTIPLE

        self.SetWindowStyle(style)


    @property
    def check_path_exists(self: Union[_wx.FileDialog, _wx.DirDialog]) -> bool:
        """Check if the dialog is set to check for path existence.

        Returns:
            bool: True if the dialog checks for path existence, False otherwise.
        """
        return bool(self.GetWindowStyle() & _wx.FD_FILE_MUST_EXIST)

    @check_path_exists.setter
    def check_path_exists(self: Union[_wx.FileDialog, _wx.DirDialog], value: bool) -> None:
        """Set the dialog to check for path existence.

        Args:
            value (bool): True to enable path existence check, False to disable.
        """
        style = self.GetWindowStyle()

        if value:
            style |= _wx.FD_FILE_MUST_EXIST
        else:
            style &= ~_wx.FD_FILE_MUST_EXIST

        self.SetWindowStyle(style)


    def __init__(
            self,
            parent: _wx.Window | None = None,
            title: str = "",
            message: str = "",
            filter: str = "All files (*.*)|*.*",
            size: _wx.Size | None = None,
            pos: _wx.Point | None = None,
            multiselect: bool = False,
            initial_directory: str | None = None,
            initial_filename: str | None = None,
            basestyle: int = _wx.FD_DEFAULT_STYLE):
        
        style = basestyle

        if multiselect:
            style |= _wx.FD_MULTIPLE
        
        if size is None:
            size = _wx.DefaultSize

        if pos is None:
            pos = _wx.DefaultPosition

        self._initial_directory = initial_directory
        self._initial_filename = initial_filename

        super().__init__(
            parent=parent,
            name=title,
            message=message,
            wildcard=filter,
            style=style,
            size=size,
            pos=pos,
            defaultDir=initial_directory or "",
            defaultFile=initial_filename or "",
        )

    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        self.Destroy()
    

class OpenFileDialog(FileDialog):
    """Open file dialog wrapper."""
    def __init__(
            self,
            parent: _wx.Window | None = None,
            title: str = "Open File",
            message: str = "Choose a file to open",
            filter: str = "All files (*.*)|*.*",
            size: _wx.Size | None = None,
            pos: _wx.Point | None = None,
            multiselect: bool = False,
            initial_directory: str | None = None,
            initial_filename: str | None = None):
        
        super().__init__(
            parent=parent,
            title=title,
            message=message,
            filter=filter,
            size=size,
            pos=pos,
            multiselect=multiselect,
            initial_directory=initial_directory,
            initial_filename=initial_filename,
            basestyle=_wx.FD_OPEN | _wx.FD_FILE_MUST_EXIST,
        )


class SaveFileDialog(FileDialog):
    """Save file dialog wrapper."""
    def __init__(
            self,
            parent: _wx.Window | None = None,
            title: str = "Save File",
            message: str = "Choose a location to save the file",
            filter: str = "All files (*.*)|*.*",
            size: _wx.Size | None = None,
            pos: _wx.Point | None = None,
            initial_directory: str | None = None,
            initial_filename: str | None = None):
        
        super().__init__(
            parent=parent,
            title=title,
            message=message,
            filter=filter,
            size=size,
            pos=pos,
            multiselect=False,
            initial_directory=initial_directory,
            initial_filename=initial_filename,
            basestyle=_wx.FD_SAVE | _wx.FD_OVERWRITE_PROMPT,
        )


class FolderDialog(
        _wx.DirDialog,
        core.UIAttributes,
        core.UIInitializeComponent,
        FileFolderDialogAttributes,
        metaclass=mixins_core.MixinsType):
    """Folder dialog wrapper with enhanced initialization."""
    @property
    def initial_directory(self) -> str:
        """Get the initial directory of the dialog.

        Returns:
            str: The initial directory set in the file dialog.
        """
        if not hasattr(self, '_initial_directory'):
            self._initial_directory = None
        
        return self._initial_directory or ""
    
    
    @property
    def selected_path(self) -> str:
        """Get the selected path.

        Returns:
            str: The selected path in the folder dialog.
        """
        return (self.selected_paths[0]
                 if self.multiselect
                 else self.GetPath())
    
    
    @property
    def selected_paths(self) -> List[str]:
        """Get the list of selected paths.

        Returns:
            List[str]: The list of selected paths in the folder dialog.
        """
        return self.GetPaths()
    

    @property
    def multiselect(self: Union[_wx.FileDialog, _wx.DirDialog]) -> bool:
        """Check if multiselect is enabled.

        Returns:
            bool: True if multiselect is enabled, False otherwise.
        """
        return bool(self.GetWindowStyle() & _wx.DD_MULTIPLE)
    
    @multiselect.setter
    def multiselect(self: Union[_wx.FileDialog, _wx.DirDialog], value: bool):
        """Enable or disable multiselect.

        Args:
            value (bool): True to enable multiselect, False to disable.
        """
        style = self.GetWindowStyle()

        if value:
            style |= _wx.DD_MULTIPLE
        else:
            style &= ~_wx.DD_MULTIPLE

        self.SetWindowStyle(style)


    @property
    def show_new_folder_button(self: Union[_wx.FileDialog, _wx.DirDialog]) -> bool:
        """Show or hide the 'New Folder' button.

        Args:
            show (bool): True to show the button, False to hide it.
        """
        return bool(self.GetWindowStyle() & _wx.DD_NEW_DIR_BUTTON)

    @show_new_folder_button.setter
    def show_new_folder_button(self: Union[_wx.FileDialog, _wx.DirDialog], show: bool) -> None:
        """Show or hide the 'New Folder' button.

        Args:
            show (bool): True to show the button, False to hide it.
        """
        style = self.GetWindowStyle()

        if show:
            style |= _wx.DD_NEW_DIR_BUTTON
        else:
            style &= ~_wx.DD_NEW_DIR_BUTTON

        self.SetWindowStyle(style)


    @property
    def root_folder(self) -> str:
        """Get the root folder of the dialog.

        Returns:
            str: The root folder set in the folder dialog.
        """
        return self._initial_directory or ""


    def __init__(
            self,
            parent: _wx.Window | None = None,
            title: str = "Select Folder",
            message: str = "Choose a folder",
            default_path: str | None = None,
            size: _wx.Size | None = None,
            pos: _wx.Point | None = None):
        
        if size is None:
            size = _wx.DefaultSize

        if pos is None:
            pos = _wx.DefaultPosition

        self._initial_directory = default_path

        super().__init__(
            parent=parent,
            message=message,
            defaultPath=default_path or "",
            style=_wx.DD_DEFAULT_STYLE,
            pos=pos,
            size=size,
            name=title,
        )

    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        self.Destroy()


class FolderBrowserDialog(FolderDialog):
    """Folder browser dialog wrapper."""
    def __init__(
            self,
            parent: _wx.Window | None = None,
            title: str = "Select Folder",
            message: str = "Choose a folder",
            default_path: str | None = None,
            size: _wx.Size | None = None,
            pos: _wx.Point | None = None):
        
        super().__init__(
            parent=parent,
            title=title,
            message=message,
            default_path=default_path,
            size=size,
            pos=pos,
        )


__all__ = [
    "DialogResult",
    "OpenFileDialog",
    "SaveFileDialog",
    "FolderBrowserDialog",
]