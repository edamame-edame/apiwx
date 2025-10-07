"""Color constants for wxPython GUI applications.

This module provides a convenient Colors class that wraps wxPython's built-in
color constants, making them easily accessible and well-documented for GUI
development.

The Colors class contains predefined color constants with their hexadecimal
values for quick reference during development.

Example:
    >>> from apiwx.colors import Colors
    >>> background_color = Colors.WHITE
    >>> text_color = Colors.BLACK
    >>> accent_color = Colors.BLUE

Available Colors:
    Standard colors: BLACK, WHITE, RED, BLUE, GREEN, CYAN, YELLOW
    Utility colors: LIGHT_GREY, NullColour
"""


from wx import (
    BLACK, WHITE, RED, BLUE, GREEN, CYAN, YELLOW, LIGHT_GREY,
    NullColour
)


class Colors:
    """Collection of wxPython color constants with documentation.
    
    This class provides easy access to commonly used wxPython color constants.
    Each color constant is documented with its hexadecimal representation
    for developer reference.
    
    All color constants are direct references to wxPython's built-in color
    objects, ensuring compatibility and consistency with the wxPython 
    framework.
    
    Attributes:
        BLACK: Pure black color (#000000)
        WHITE: Pure white color (#FFFFFF)
        RED: Pure red color (#FF0000)
        BLUE: Pure blue color (#0000FF)
        GREEN: Pure green color (#00FF00)
        CYAN: Cyan color (#00FFFF)
        YELLOW: Pure yellow color (#FFFF00)
        LIGHT_GREY: Light grey color (#D3D3D3)
        NullColour: Special null color for default/unspecified colors
    
    Example:
        >>> panel.color_background = Colors.WHITE
        >>> button.color_foreground = Colors.BLACK
        >>> border_color = Colors.LIGHT_GREY
    """
    
    BLACK = BLACK
    """Pure black color (#000000)."""
    
    WHITE = WHITE
    """Pure white color (#FFFFFF)."""
    
    RED = RED
    """Pure red color (#FF0000)."""
    
    BLUE = BLUE
    """Pure blue color (#0000FF)."""
    
    GREEN = GREEN
    """Pure green color (#00FF00)."""
    
    CYAN = CYAN
    """Cyan color (#00FFFF)."""
    
    YELLOW = YELLOW
    """Pure yellow color (#FFFF00)."""
    
    LIGHT_GREY = LIGHT_GREY
    """Light grey color (#D3D3D3)."""
    
    NullColour = NullColour
    """Special null color for default/unspecified colors."""


# Export list for explicit module interface
__all__ = [
    'Colors',
]

