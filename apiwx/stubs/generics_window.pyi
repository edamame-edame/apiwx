"""Type stubs for apiwx.generics_window module.

This module provides type information for generic type definitions and mixin 
classes for wxPython window objects, enabling proper type checking and IDE support.
"""

from typing import Type, Tuple
from .core import WrappedWindow, WrappedPanel
from .generics_common import AutoDetect

class ByPanelSize:
    """Generic mixin to manage window size based on client panel size.

    ByPanelSize provides size management functionality for wxPython windows
    where the window size is controlled by the internal panel (client area)
    size rather than the total window size including decorations.
    """
    
    @property
    def size(self: WrappedWindow) -> Tuple[int, int]: 
        """Get the client area size of the window."""
        ...
    
    @size.setter
    def size(self: WrappedWindow, value: Tuple[int, int]) -> None: 
        """Set the client area size of the window."""
        ...
    
    def __init__(self: WrappedWindow, *args, **kwds) -> None: 
        """Initialize the ByPanelSize mixin."""
        ...

# Type alias for auto-detecting panel components in windows
DetectPanel: Type[AutoDetect[WrappedPanel]]
"""Type variable for auto-detecting panel components in windows.

This type alias provides automatic type detection for panel components
that are used within wxPython window objects. It enables type checkers
to properly identify and validate panel components for better type safety
and IDE support in window-based applications.
"""