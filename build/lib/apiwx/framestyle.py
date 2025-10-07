"""wxPython Frame style constants and border definitions.

This module provides a centralized collection of wxPython style constants
used for window and frame styling. It re-exports commonly used style flags
from wxPython to provide a convenient single import location for frame
styling operations.

The module includes two main categories of constants:

Window Style Constants (from wx/window.h):
    - Border styles: SIMPLE_BORDER, SUNKEN_BORDER, RAISED_BORDER, NO_BORDER
    - Behavior styles: TAB_TRAVERSAL, WANTS_CHARS
    - Scrolling styles: VSCROLL, HSCROLL

Extended Window Styles (from wxWindow::SetExtraStyle):
    - Validation: WS_EX_VALIDATE_RECURSIVELY
    - Event handling: WS_EX_BLOCK_EVENTS
    - Window behavior: WS_EX_TRANSIENT, WS_EX_PROCESS_IDLE, 
      WS_EX_PROCESS_UI_UPDATES

Example:
    from apiwx.framestyle import SIMPLE_BORDER, TAB_TRAVERSAL
    
    # Create a frame with simple border and tab traversal
    frame = wx.Frame(
        parent=None,
        style=SIMPLE_BORDER | TAB_TRAVERSAL
    )

Note:
    These constants are direct re-exports from wxPython and maintain the
    same values and behavior as their original wxPython counterparts.
"""

from wx import (
    # Window border styles (from wx/window.h)
    SIMPLE_BORDER,
    SUNKEN_BORDER,
    RAISED_BORDER,
    NO_BORDER,
    
    # Window behavior styles (from wx/window.h)
    TAB_TRAVERSAL,
    WANTS_CHARS,
    
    # Scrolling styles (from wx/window.h)
    VSCROLL,
    HSCROLL,
    
    # Extended window styles (from wxWindow::SetExtraStyle)
    WS_EX_VALIDATE_RECURSIVELY,
    WS_EX_BLOCK_EVENTS,
    WS_EX_TRANSIENT,
    WS_EX_PROCESS_IDLE,
    WS_EX_PROCESS_UI_UPDATES,
)


__all__ = [
    # Window border styles
    'SIMPLE_BORDER',
    'SUNKEN_BORDER', 
    'RAISED_BORDER',
    'NO_BORDER',
    
    # Window behavior styles
    'TAB_TRAVERSAL',
    'WANTS_CHARS',
    
    # Scrolling styles
    'VSCROLL',
    'HSCROLL',
    
    # Extended window styles
    'WS_EX_VALIDATE_RECURSIVELY',
    'WS_EX_BLOCK_EVENTS',
    'WS_EX_TRANSIENT',
    'WS_EX_PROCESS_IDLE',
    'WS_EX_PROCESS_UI_UPDATES',
]
