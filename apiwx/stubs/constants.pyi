"""Type stubs for apiwx.constants module.

This module provides type information for alignment constants and layout
management utilities, enabling proper type checking and IDE support.
"""

from typing import Literal
from wx import ALIGN_LEFT, ALIGN_TOP, ALIGN_RIGHT, ALIGN_BOTTOM, ALIGN_CENTER

# Basic alignment constants from wxPython
ALIGN_LEFT: int
ALIGN_TOP: int
ALIGN_RIGHT: int
ALIGN_BOTTOM: int
ALIGN_CENTER: int

# Composite alignment constants for common corner positioning
ALIGN_LEFT_TOP: int
"""Left-aligned and top-positioned alignment combination."""

ALIGN_LEFT_BOTTOM: int
"""Left-aligned and bottom-positioned alignment combination."""

ALIGN_RIGHT_TOP: int
"""Right-aligned and top-positioned alignment combination."""

ALIGN_RIGHT_BOTTOM: int
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
"""

__all__: list[str]