"""Alignment and layout constants for wxPython GUI applications.

This module provides alignment constants and combinations commonly used
in wxPython layout management. It includes basic alignment constants
from wxPython and convenient composite constants for corner alignments.

The module also provides type hints for literal alignment values to
improve type safety and IDE support when working with alignment parameters.

Basic Alignments:
    ALIGN_LEFT, ALIGN_RIGHT: Horizontal alignment
    ALIGN_TOP, ALIGN_BOTTOM: Vertical alignment  
    ALIGN_CENTER: Center alignment (both horizontal and vertical)

Composite Alignments:
    ALIGN_LEFT_TOP, ALIGN_LEFT_BOTTOM: Left side with vertical positioning
    ALIGN_RIGHT_TOP, ALIGN_RIGHT_BOTTOM: Right side with vertical positioning

Example:
    >>> from apiwx.constants import ALIGN_CENTER, ALIGN_LEFT_TOP
    >>> button.alignment = ALIGN_CENTER
    >>> panel.child_alignment = ALIGN_LEFT_TOP

Type Safety:
    The literal_alignment type can be used for type hints to ensure
    only valid alignment constants are used in function parameters.
"""


from typing import Literal

from wx import (
    # Basic alignment constants from wxPython
    ALIGN_LEFT,
    ALIGN_TOP,
    ALIGN_RIGHT,
    ALIGN_BOTTOM,
    ALIGN_CENTER,
)


# Composite alignment constants for common corner positioning
ALIGN_LEFT_TOP = (ALIGN_LEFT | ALIGN_TOP)
"""Left-aligned and top-positioned alignment combination."""

ALIGN_LEFT_BOTTOM = (ALIGN_LEFT | ALIGN_BOTTOM)
"""Left-aligned and bottom-positioned alignment combination."""

ALIGN_RIGHT_TOP = (ALIGN_RIGHT | ALIGN_TOP)
"""Right-aligned and top-positioned alignment combination."""

ALIGN_RIGHT_BOTTOM = (ALIGN_RIGHT | ALIGN_BOTTOM)
"""Right-aligned and bottom-positioned alignment combination."""


# Type hint for literal alignment values to ensure type safety
literal_alignment = Literal[
    ALIGN_LEFT,
    ALIGN_TOP,
    ALIGN_RIGHT,
    ALIGN_BOTTOM,
    ALIGN_CENTER,
    ALIGN_LEFT_TOP,
    ALIGN_LEFT_BOTTOM,
    ALIGN_RIGHT_TOP,
    ALIGN_RIGHT_BOTTOM,
]
"""Type annotation for valid alignment constants.

This type can be used in function signatures to restrict alignment
parameters to only valid alignment constants, providing better type
safety and IDE autocomplete support.

Example:
    >>> def set_alignment(align: literal_alignment) -> None:
    ...     # Function will only accept valid alignment constants
    ...     pass
"""


# Export list for explicit module interface
__all__ = [
    # Basic alignment constants
    'ALIGN_LEFT',
    'ALIGN_TOP', 
    'ALIGN_RIGHT',
    'ALIGN_BOTTOM',
    'ALIGN_CENTER',
    
    # Composite alignment constants
    'ALIGN_LEFT_TOP',
    'ALIGN_LEFT_BOTTOM',
    'ALIGN_RIGHT_TOP',
    'ALIGN_RIGHT_BOTTOM',
    
    # Type hint
    'literal_alignment',
]

