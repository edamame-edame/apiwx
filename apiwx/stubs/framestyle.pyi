"""Type stubs for apiwx.framestyle module.

This module provides type information for wxPython frame style constants
and border definitions, enabling proper type checking and IDE support.
"""

# Window border styles (from wx/window.h)
SIMPLE_BORDER: int
SUNKEN_BORDER: int
RAISED_BORDER: int
NO_BORDER: int

# Window behavior styles (from wx/window.h)
TAB_TRAVERSAL: int
WANTS_CHARS: int

# Scrolling styles (from wx/window.h)
VSCROLL: int
HSCROLL: int

# Extended window styles (from wxWindow::SetExtraStyle)
WS_EX_VALIDATE_RECURSIVELY: int
WS_EX_BLOCK_EVENTS: int
WS_EX_TRANSIENT: int
WS_EX_PROCESS_IDLE: int
WS_EX_PROCESS_UI_UPDATES: int

__all__: list[str]