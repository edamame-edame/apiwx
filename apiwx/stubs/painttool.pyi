"""Type stubs for apiwx.painttool module.

This module provides type information for paint tool utilities that
re-export commonly used wxPython drawing classes and constants for 
simplified painting operations in wxPython applications.
"""

import wx

# Drawing context for paint operations
PaintDC: type[wx.PaintDC]

# Drawing tools
Pen: type[wx.Pen]

# Brush style constants for various patterns
BRUSHSTYLE_BDIAGONAL_HATCH: int
BRUSHSTYLE_CROSS_HATCH: int
BRUSHSTYLE_FDIAGONAL_HATCH: int
BRUSHSTYLE_HORIZONTAL_HATCH: int
BRUSHSTYLE_VERTICAL_HATCH: int
BRUSHSTYLE_CROSSDIAG_HATCH: int
BRUSHSTYLE_SOLID: int
BRUSHSTYLE_FIRST_HATCH: int
BRUSHSTYLE_LAST_HATCH: int

# Stipple pattern styles
BRUSHSTYLE_STIPPLE_MASK_OPAQUE: int
BRUSHSTYLE_STIPPLE_MASK: int
BRUSHSTYLE_STIPPLE: int

# Predefined brushes
TRANSPARENT_BRUSH: wx.Brush

__all__: list[str]