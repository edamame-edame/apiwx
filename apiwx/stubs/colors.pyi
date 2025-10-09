"""Type stubs for apiwx.colors module.

This module provides type information for wxPython color constants and the
Colors class wrapper, enabling proper type checking and IDE support.
"""

from typing import Any
from wx import Colour

# Re-export color constants with proper typing
BLACK: Colour
WHITE: Colour
RED: Colour
BLUE: Colour
GREEN: Colour
CYAN: Colour
YELLOW: Colour
LIGHT_GREY: Colour
NullColour: Colour

class Colors:
    """Collection of wxPython color constants with documentation.
    
    This class provides easy access to commonly used wxPython color constants.
    Each color constant is documented with its hexadecimal representation
    for developer reference.
    """
    
    BLACK: Colour
    """Pure black color (#000000)."""
    
    WHITE: Colour
    """Pure white color (#FFFFFF)."""
    
    RED: Colour
    """Pure red color (#FF0000)."""
    
    BLUE: Colour
    """Pure blue color (#0000FF)."""
    
    GREEN: Colour
    """Pure green color (#00FF00)."""
    
    CYAN: Colour
    """Cyan color (#00FFFF)."""
    
    YELLOW: Colour
    """Pure yellow color (#FFFF00)."""
    
    LIGHT_GREY: Colour
    """Light grey color (#D3D3D3)."""
    
    NullColour: Colour
    """Special null color for default/unspecified colors."""

__all__: list[str]