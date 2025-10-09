"""Type stubs for apiwx.styleflags module.

This module provides type information for wxPython style flag constants
organized into logical categories for better IDE support and type checking.
"""

class WindowStyle:
    """Basic window and frame style constants.
    
    This class provides convenient access to common window and frame
    style flags used in wxPython applications.
    """
    DEFAULT_FRAME_STYLE: int
    HSCROLL: int
    VSCROLL: int
    LC_REPORT: int

class ControlStyle:
    """Control-specific style constants.
    
    This class provides style flags specific to UI controls
    like sliders, gauges, and other widgets.
    """
    SL_HORIZONTAL: int
    GA_HORIZONTAL: int

class BorderStyle:
    """Border appearance style constants.
    
    This class provides different border styles that can be
    applied to windows and controls.
    """
    SIMPLE: int
    SUNKEN: int
    RAISED: int
    NONE: int

class TraversalStyle:
    """Keyboard traversal and input style constants.
    
    This class provides flags that control keyboard navigation
    and character input behavior.
    """
    TAB_TRAVERSAL: int
    WANTS_CHARS: int

class ExtraWindowStyle:
    """Extended window behavior style constants.
    
    This class provides additional window behavior flags
    for validation, event handling, and UI updates.
    """
    VALIDATE_RECURSIVELY: int
    BLOCK_EVENTS: int
    TRANSIENT: int
    PROCESS_IDLE: int
    PROCESS_UI_UPDATES: int

class FrameStyle:
    """Frame-specific style constants.
    
    This class provides style flags specific to frame windows,
    including tool windows and floating frames.
    """
    FRAME_SHAPED: int
    FRAME_TOOL_WINDOW: int
    FRAME_NO_TASKBAR: int
    FRAME_FLOAT_ON_PARENT: int

class DialogStyle:
    """Dialog window style constants.
    
    This class provides style flags specific to dialog windows
    and modal dialogs.
    """
    DEFAULT_DIALOG_STYLE: int
    RESIZE_BORDER: int
    DIALOG_NO_PARENT: int
    DIALOG_EX_METAL: int

class ControlBorderStyle:
    """Control border style constants.
    
    This class provides border styles specifically designed
    for UI controls and widgets.
    """
    NONE: int
    SIMPLE: int
    SUNKEN: int
    RAISED: int
    STATIC: int
    THEME: int

class MiscFlag:
    """Miscellaneous style and behavior flags.
    
    This class provides various flags including fullscreen
    options and other miscellaneous style flags.
    """
    FULLSCREEN_NOMENUBAR: int
    FULLSCREEN_NOTOOLBAR: int
    FULLSCREEN_NOSTATUSBAR: int
    FULLSCREEN_NOBORDER: int
    FULLSCREEN_NOCAPTION: int
    FULLSCREEN_ALL: int

__all__: list[str]