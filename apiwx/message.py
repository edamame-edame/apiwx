"""
# apiwx - Message box wrapper for wxPython
Simplified and enhanced message box functionality with consistent API
"""
import wx
from typing import Optional, Union, Tuple, Any
from enum import Enum, auto

try:
    from . import debug
    from .debug import LogLevel
except ImportError:
    import debug
    from debug import LogLevel


class MessageType(Enum):
    """Message box types with predefined styles"""
    INFO = auto()
    WARNING = auto()
    ERROR = auto()
    QUESTION = auto()
    SUCCESS = auto()


class MessageResult(Enum):
    """Standardized message box results"""
    OK = wx.ID_OK
    CANCEL = wx.ID_CANCEL
    YES = wx.ID_YES
    NO = wx.ID_NO
    CLOSE = wx.ID_CLOSE
    HELP = wx.ID_HELP
    UNKNOWN = -1


class MessageBox:
    """
    # Enhanced message box wrapper for wxPython
    ### Usage
    ```python
    # Simple info message
    MessageBox.info("Operation completed successfully!")

    # Yes/No question
    result = MessageBox.question("Do you want to save changes?")
    if result == MessageResult.YES:
    save_changes()

    # Custom message with multiple buttons
    result = MessageBox.custom(
    "Choose an action:",
    "Custom Dialog",
    buttons=MessageButtons.YES_NO_CANCEL,
    default_button=MessageResult.YES
    )
    ```
    """

    @staticmethod
    def _get_parent() -> Optional[wx.Window]:
        """Get the best parent window for the message box"""
        try:
            app = wx.GetApp()

            if app:
                top_window = app.GetTopWindow()

            if top_window:
                return top_window
            
        except:
            pass

        return None

    @staticmethod
    def _get_style_for_type(msg_type: MessageType) -> int:
        """Get wx style flags for message type"""
        styles = {
            MessageType.INFO: wx.ICON_INFORMATION | wx.OK,
            MessageType.WARNING: wx.ICON_WARNING | wx.OK,
            MessageType.ERROR: wx.ICON_ERROR | wx.OK,
            MessageType.QUESTION: wx.ICON_QUESTION | wx.YES_NO,
            MessageType.SUCCESS: wx.ICON_INFORMATION | wx.OK,
        }

        return styles.get(msg_type, wx.ICON_INFORMATION | wx.OK)

    @staticmethod
    def _show_message(
            message: str,
            title: str = "Message",
            style: int = wx.OK | wx.ICON_INFORMATION,
            parent: Optional[wx.Window] = None
        ) -> MessageResult:
        """Core message box display function"""
        if parent is None:
            parent = MessageBox._get_parent()

        try:
            dlg = wx.MessageDialog(parent, message, title, style)
            result = dlg.ShowModal()
            dlg.Destroy()

            # Convert wx result to our enum
            try:
                return MessageResult(result)
            
            except ValueError:
                debug.uilog("MESSAGE", f"Unknown result code: {result}", LogLevel.WARNING)

            return MessageResult.UNKNOWN

        except Exception as e:
            debug.uilog("MESSAGE", f"Error showing message: {e}", LogLevel.ERROR)

            return MessageResult.UNKNOWN

    @staticmethod
    def info(
            message: str,
            title: str = "Information",
            parent: Optional[wx.Window] = None
        ) -> MessageResult:
        """Show information message"""

        debug.uilog("MESSAGE", f"Info: {title} - {message[:50]}...", LogLevel.INFO)
        
        return MessageBox._show_message(
            message,
            title,
            wx.OK | wx.ICON_INFORMATION,
            parent
        )

    @staticmethod
    def warning(
            message: str,
            title: str = "Warning",
            parent: Optional[wx.Window] = None
        ) -> MessageResult:
        """Show warning message"""

        debug.uilog("MESSAGE", f"Warning: {title} - {message[:50]}...", LogLevel.WARNING)

        return MessageBox._show_message(
            message,
            title,
            wx.OK | wx.ICON_WARNING,
            parent
        )

    @staticmethod
    def error(
            message: str,
            title: str = "Error",
            parent: Optional[wx.Window] = None
        ) -> MessageResult:
        """Show error message"""

        debug.uilog("MESSAGE", f"Error: {title} - {message[:50]}...", LogLevel.ERROR)

        return MessageBox._show_message(
            message,
            title,
            wx.OK | wx.ICON_ERROR,
            parent
        )

    @staticmethod
    def question(
            message: str,
            title: str = "Question",
            parent: Optional[wx.Window] = None
        ) -> MessageResult:
        """Show yes/no question"""

        debug.uilog("MESSAGE", f"Question: {title} - {message[:50]}...")

        return MessageBox._show_message(
            message,
            title,
            wx.YES_NO | wx.ICON_QUESTION,
            parent
        )

    @staticmethod
    def success(
        message: str,
        title: str = "Success",
        parent: Optional[wx.Window] = None
    ) -> MessageResult:
        """Show success message"""

        debug.uilog("MESSAGE", f"Success: {title} - {message[:50]}...")

        return MessageBox._show_message(
            message,
            title,
            wx.OK | wx.ICON_INFORMATION,
            parent
        )


class MessageButtons(Enum):
    """Predefined button combinations"""
    OK = wx.OK
    OK_CANCEL = wx.OK | wx.CANCEL
    YES_NO = wx.YES_NO
    YES_NO_CANCEL = wx.YES_NO | wx.CANCEL
    CLOSE = wx.CLOSE


class CustomMessageBox:
    """
    # Advanced message box with full customization
    ### Usage
    ```python
    result = CustomMessageBox(
    message="Are you sure you want to delete all files?",
    title="Confirm Deletion",
    buttons=MessageButtons.YES_NO_CANCEL,
    icon=wx.ICON_EXCLAMATION,
    default_button=MessageResult.NO
    ).show()
    ```
    """

    def __init__(
            self,
            message: str,
            title: str = "Message",
            buttons: Union[MessageButtons, int] = MessageButtons.OK,
            icon: int = wx.ICON_INFORMATION,
            default_button: Optional[MessageResult] = None,
            parent: Optional[wx.Window] = None
        ):
        self.message = message
        self.title = title
        self.buttons = buttons.value if isinstance(buttons, MessageButtons) else buttons
        self.icon = icon
        self.default_button = default_button
        self.parent = parent or MessageBox._get_parent()

    def show(self) -> MessageResult:
        """Show the custom message box"""
        style = self.buttons | self.icon

        # Set default button if specified
        if self.default_button:
            if self.default_button == MessageResult.NO:
                style |= wx.NO_DEFAULT

            elif self.default_button == MessageResult.CANCEL:
                style |= wx.CANCEL_DEFAULT

        debug.uilog("MESSAGE", f"Custom: {self.title} - {self.message[:50]}...")

        return MessageBox._show_message(
            self.message,
            self.title,
            style,
            self.parent
        )


class ProgressMessageBox:
    """
    # Message box that can be updated during long operations
    ### Usage
    ```python
    progress = ProgressMessageBox("Processing files...", "Please Wait")
    progress.show()

    # Update during operation
    for i in range(100):
    progress.update_message(f"Processing file {i+1}/100...")
    # do work

    progress.close()
    ```
    """

    def __init__(
            self,
            message: str,
            title: str = "Processing",
            parent: Optional[wx.Window] = None
        ):
        self.message = message
        self.title = title
        self.parent = parent or MessageBox._get_parent()
        self._dialog = None
        self._is_shown = False

    def show(self):
        """Show the progress message box"""
        if self._dialog is None:
            try:
                # Use a progress dialog for better user experience
                self._dialog = wx.ProgressDialog(
                    self.title,
                    self.message,
                    maximum=100,
                    parent=self.parent,
                    style=wx.PD_AUTO_HIDE | wx.PD_APP_MODAL
                )
    
                self._is_shown = True
    
                debug.uilog("MESSAGE", f"Progress dialog shown: {self.title}")
    
            except Exception as e:
                debug.uilog("MESSAGE", f"Error showing progress dialog: {e}")

    def update_message(self, message: str, progress: Optional[int] = None):
        """Update the message and optionally progress"""
        if self._dialog and self._is_shown:
            try:
                if progress is not None:
                    self._dialog.Update(progress, message)

                else:
                    self._dialog.Pulse(message)
                    debug.uilog("MESSAGE", f"Progress updated: {message[:30]}...")

            except Exception as e:
                    debug.uilog("MESSAGE", f"Error updating progress: {e}")

    def close(self):
        """Close the progress dialog"""
        if self._dialog:
            try:
                self._dialog.Destroy()
                debug.uilog("MESSAGE", "Progress dialog closed")

            except Exception as e:
                debug.uilog("MESSAGE", f"Error closing progress dialog: {e}")

            finally:
                self._dialog = None
                self._is_shown = False


class InputDialog:
    """
    # Input dialog for getting text from user
    ### Usage
    ```python
        name = InputDialog.get_text("Enter your name:", "User Input")

        if name:
            print(f"Hello, {name}!")

        # Number input
        age = InputDialog.get_number("Enter your age:", "Age Input", min_value=0, max_value=150)
    ```
    """

    @staticmethod
    def get_text(
            message: str,
            title: str = "Input",
            default_value: str = "",
            parent: Optional[wx.Window] = None
        ) -> Optional[str]:
        """Get text input from user"""
        if parent is None:
            parent = MessageBox._get_parent()

            try:
                dlg = wx.TextEntryDialog(parent, message, title, default_value)

                if dlg.ShowModal() == wx.ID_OK:
                    result = dlg.GetValue()
                    dlg.Destroy()
                    debug.uilog("MESSAGE", f"Text input received: {len(result)} chars")
                    return result

                else:
                    dlg.Destroy()
                    return None

            except Exception as e:
                debug.uilog("MESSAGE", f"Error getting text input: {e}")

        return None

    @staticmethod
    def get_number(
            message: str,
            title: str = "Number Input",
            default_value: int = 0,
            min_value: int = -2147483648,
            max_value: int = 2147483647,
            parent: Optional[wx.Window] = None
        ) -> Optional[int]:
        """Get number input from user"""
        if parent is None:
            parent = MessageBox._get_parent()

        try:
            dlg = wx.NumberEntryDialog(
                parent,
                message,
                "Value:",
                title,
                default_value,
                min_value,
                max_value
            )
            
            if dlg.ShowModal() == wx.ID_OK:
                result = dlg.GetValue()
                dlg.Destroy()
                debug.uilog("MESSAGE", f"Number input received: {result}")
                return result
            
            else:
                dlg.Destroy()
                return None
        
        except Exception as e:
            debug.uilog("MESSAGE", f"Error getting number input: {e}")

        return None

    @staticmethod
    def get_choice(
            message: str,
            choices: list[str],
            title: str = "Choose",
            parent: Optional[wx.Window] = None
        ) -> Optional[str]:
        """Get choice from list"""
        if parent is None:
            parent = MessageBox._get_parent()

        if not choices:
            debug.uilog("MESSAGE", "No choices provided for selection")
            return None

        try:
            dlg = wx.SingleChoiceDialog(parent, message, title, choices)

            if dlg.ShowModal() == wx.ID_OK:
                result = dlg.GetStringSelection()
                dlg.Destroy()
                debug.uilog("MESSAGE", f"Choice selected: {result}")
                return result
            
            else:
                dlg.Destroy()
                return None
            
        except Exception as e:
            debug.uilog("MESSAGE", f"Error getting choice: {e}")

        return None


# Convenience functions for quick usage
def show_info(message: str, title: str = "Information") -> MessageResult:
    """Quick info message"""
    return MessageBox.info(message, title)

def show_warning(message: str, title: str = "Warning") -> MessageResult:
    """Quick warning message"""
    return MessageBox.warning(message, title)

def show_error(message: str, title: str = "Error") -> MessageResult:
    """Quick error message"""
    return MessageBox.error(message, title)

def ask_question(message: str, title: str = "Question") -> bool:
    """Quick yes/no question - returns True for Yes"""
    result = MessageBox.question(message, title)
    return result == MessageResult.YES

def show_success(message: str, title: str = "Success") -> MessageResult:
    """Quick success message"""
    return MessageBox.success(message, title)

def get_text_input(message: str, title: str = "Input", default: str = "") -> Optional[str]:
    """Quick text input"""
    return InputDialog.get_text(message, title, default)

def get_number_input(
        message: str,
        title: str = "Number Input",
        default: int = 0,
        min_val: int = -2147483648,
        max_val: int = 2147483647
    ) -> Optional[int]:
    """Quick number input"""
    return InputDialog.get_number(message, title, default, min_val, max_val)

def get_choice_input(message: str, choices: list[str], title: str = "Choose") -> Optional[str]:
    """Quick choice input"""
    return InputDialog.get_choice(message, choices, title)


# Example usage and testing functions
if __name__ == "__main__":
    # This will run when the module is executed directly
    print("apiwx.message - Message box wrapper")
    print("This module provides enhanced message box functionality for wxPython")
    print("\nExample usage:")
    print(" from apiwx.message import show_info, ask_question")
    print(" show_info('Hello World!')")
    print(" if ask_question('Continue?'):")
    print("    print('User chose yes')")