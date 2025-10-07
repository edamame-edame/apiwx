"""Style flag constants for wxPython UI components.

This module provides organized access to wxPython style flag constants
through convenience classes. It groups related style flags into logical
categories to improve code readability and maintainability when creating
wxPython UI components.

Style Categories:
    WindowStyle: Basic window and frame styles
    ControlStyle: Control-specific style flags
    BorderStyle: Border appearance styles
    TraversalStyle: Keyboard traversal and input styles
    ExtraWindowStyle: Extended window behavior styles
    FrameStyle: Frame-specific style options
    DialogStyle: Dialog window styles
    ControlBorderStyle: Control border styles
    MiscFlag: Miscellaneous flags and fullscreen options

Usage:
    >>> from apiwx.styleflags import WindowStyle, BorderStyle
    >>> frame_style = WindowStyle.DEFAULT_FRAME_STYLE
    >>> border_style = BorderStyle.SUNKEN
    >>> window = wx.Frame(None, style=frame_style | border_style)
"""

from wx import (
    # Basic window and frame styles
    DEFAULT_FRAME_STYLE,
    HSCROLL,
    VSCROLL,
    LC_REPORT,
    
    # Control styles
    SL_HORIZONTAL,
    GA_HORIZONTAL,
    
    # Border styles
    SIMPLE_BORDER,
    SUNKEN_BORDER,
    RAISED_BORDER,
    NO_BORDER,
    
    # Traversal styles
    TAB_TRAVERSAL,
    WANTS_CHARS,
    
    # Extended window styles
    WS_EX_VALIDATE_RECURSIVELY,
    WS_EX_BLOCK_EVENTS,
    WS_EX_TRANSIENT,
    WS_EX_PROCESS_IDLE,
    WS_EX_PROCESS_UI_UPDATES,
    
    # Frame styles
    FRAME_SHAPED,
    FRAME_TOOL_WINDOW,
    FRAME_NO_TASKBAR,
    FRAME_FLOAT_ON_PARENT,
    
    # Dialog styles
    DEFAULT_DIALOG_STYLE,
    RESIZE_BORDER,
    DIALOG_NO_PARENT,
    DIALOG_EX_METAL,
    
    # Control border styles
    BORDER_NONE,
    BORDER_SIMPLE,
    BORDER_SUNKEN,
    BORDER_RAISED,
    BORDER_STATIC,
    BORDER_THEME,
    
    # Fullscreen flags
    FULLSCREEN_NOMENUBAR,
    FULLSCREEN_NOTOOLBAR,
    FULLSCREEN_NOSTATUSBAR,
    FULLSCREEN_NOBORDER,
    FULLSCREEN_NOCAPTION,
    FULLSCREEN_ALL,
)


class WindowStyle:
    """Basic window and frame style constants.
    
    This class provides convenient access to common window and frame
    style flags used in wxPython applications.
    """
    DEFAULT_FRAME_STYLE = DEFAULT_FRAME_STYLE
    HSCROLL = HSCROLL
    VSCROLL = VSCROLL
    LC_REPORT = LC_REPORT


class ControlStyle:
    """Control-specific style constants.
    
    This class provides style flags specific to UI controls
    like sliders, gauges, and other widgets.
    """
    SL_HORIZONTAL = SL_HORIZONTAL
    GA_HORIZONTAL = GA_HORIZONTAL


class BorderStyle:
    """Border appearance style constants.
    
    This class provides different border styles that can be
    applied to windows and controls.
    """
    SIMPLE = SIMPLE_BORDER
    SUNKEN = SUNKEN_BORDER
    RAISED = RAISED_BORDER
    NONE = NO_BORDER


class TraversalStyle:
    """Keyboard traversal and input style constants.
    
    This class provides flags that control keyboard navigation
    and character input behavior.
    """
    TAB_TRAVERSAL = TAB_TRAVERSAL
    WANTS_CHARS = WANTS_CHARS


class ExtraWindowStyle:
    """Extended window behavior style constants.
    
    This class provides additional window behavior flags
    for validation, event handling, and UI updates.
    """
    VALIDATE_RECURSIVELY = WS_EX_VALIDATE_RECURSIVELY
    BLOCK_EVENTS = WS_EX_BLOCK_EVENTS
    TRANSIENT = WS_EX_TRANSIENT
    PROCESS_IDLE = WS_EX_PROCESS_IDLE
    PROCESS_UI_UPDATES = WS_EX_PROCESS_UI_UPDATES


class FrameStyle:
    """Frame-specific style constants.
    
    This class provides style flags specific to frame windows,
    including tool windows and floating frames.
    """
    FRAME_SHAPED = FRAME_SHAPED
    FRAME_TOOL_WINDOW = FRAME_TOOL_WINDOW
    FRAME_NO_TASKBAR = FRAME_NO_TASKBAR
    FRAME_FLOAT_ON_PARENT = FRAME_FLOAT_ON_PARENT


class DialogStyle:
    """Dialog window style constants.
    
    This class provides style flags specific to dialog windows
    and modal dialogs.
    """
    DEFAULT_DIALOG_STYLE = DEFAULT_DIALOG_STYLE
    RESIZE_BORDER = RESIZE_BORDER
    DIALOG_NO_PARENT = DIALOG_NO_PARENT
    DIALOG_EX_METAL = DIALOG_EX_METAL


class ControlBorderStyle:
    """Control border style constants.
    
    This class provides border styles specifically designed
    for UI controls and widgets.
    """
    NONE = BORDER_NONE
    SIMPLE = BORDER_SIMPLE
    SUNKEN = BORDER_SUNKEN
    RAISED = BORDER_RAISED
    STATIC = BORDER_STATIC
    THEME = BORDER_THEME


class MiscFlag:
    """Miscellaneous style and behavior flags.
    
    This class provides various flags including fullscreen
    options and other miscellaneous style flags.
    """
    FULLSCREEN_NOMENUBAR = FULLSCREEN_NOMENUBAR
    FULLSCREEN_NOTOOLBAR = FULLSCREEN_NOTOOLBAR
    FULLSCREEN_NOSTATUSBAR = FULLSCREEN_NOSTATUSBAR
    FULLSCREEN_NOBORDER = FULLSCREEN_NOBORDER
    FULLSCREEN_NOCAPTION = FULLSCREEN_NOCAPTION
    FULLSCREEN_ALL = FULLSCREEN_ALL


# Export all style classes for convenient access
__all__ = [
    'WindowStyle',
    'ControlStyle',
    'BorderStyle',
    'TraversalStyle',
    'ExtraWindowStyle',
    'FrameStyle',
    'DialogStyle',
    'ControlBorderStyle',
    'MiscFlag',
]


# Example usage and common patterns
if __name__ == "__main__":
    print("apiwx.styleflags - Style flag constants for wxPython")
    print("This module provides organized access to wxPython style flags")
    print("\nExample usage:")
    print("  from apiwx.styleflags import WindowStyle, BorderStyle")
    print("  # Create a frame with default style and sunken border")
    print("  style = WindowStyle.DEFAULT_FRAME_STYLE | BorderStyle.SUNKEN")
    print("  frame = wx.Frame(None, style=style)")
    print("\nAvailable style classes:")
    for cls_name in __all__:
        cls_obj = globals()[cls_name]
        attrs = [attr for attr in dir(cls_obj) 
                if not attr.startswith('_')]
        print(f"  {cls_name}: {len(attrs)} constants")
