"""Type stubs for apiwx.generics_panel module.

This module provides type information for generic type definitions, mixins, 
and type variables for wxPython panel objects and their child components, 
enabling proper type checking and IDE support.
"""

from typing import Type, Optional, Any
from .core import Panel, Button, TextBox, StaticText, UIAttributes
from .generics_common import AutoDetect

class WithBoarder:
    """Mixin class to add border drawing functionality to UI components.

    WithBoarder provides configurable border drawing capabilities for wxPython
    UI components. It manages border properties (color, thickness, offset) and
    automatically draws borders on paint events.
    """
    
    @property
    def default_boarder_color(self) -> str: 
        """Get the default border color."""
        ...
    
    @property
    def boarder_color(self) -> str: 
        """Get the current border color."""
        ...
    
    @boarder_color.setter
    def boarder_color(self, value: Optional[str]) -> None: 
        """Set the border color."""
        ...
    
    @property
    def default_boarder_thickness(self) -> int: 
        """Get the default border thickness."""
        ...
    
    @property
    def boarder_thickness(self) -> int: 
        """Get the current border thickness."""
        ...
    
    @boarder_thickness.setter
    def boarder_thickness(self, value: Optional[int]) -> None: 
        """Set the border thickness."""
        ...
    
    @property
    def default_boarder_offset(self) -> int: 
        """Get the default border offset."""
        ...
    
    @property
    def boarder_offset(self) -> int: 
        """Get the current border offset."""
        ...
    
    @boarder_offset.setter
    def boarder_offset(self, value: Optional[int]) -> None: 
        """Set the border offset."""
        ...
    
    def _draw_boarder(self, event: Any) -> None: 
        """Draw the border on paint event."""
        ...
    
    def __init__(self, *args: Any, **kwds: Any) -> None: 
        """Initialize the WithBoarder mixin."""
        ...

# Type alias for auto-detecting panel child components
DetectChildren: Type[AutoDetect[UIAttributes]]
"""Type variable for auto-detecting panel child components.

This type alias provides automatic type detection for child components
within wxPython panel objects. It enables type checkers to properly identify
and validate child components for better type safety and IDE support in
panel-based applications.
"""