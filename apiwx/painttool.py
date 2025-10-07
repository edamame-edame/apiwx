"""Paint tool utilities for wxPython drawing operations.

This module provides convenient imports and utilities for wxPython
drawing and painting operations. It re-exports commonly used drawing
classes and constants to simplify painting code in wxPython applications.

The module focuses on providing easy access to:
    - Drawing context classes (PaintDC)
    - Drawing tools (Pen, Brush styles)
    - Predefined brush patterns and styles
    - Transparent drawing utilities

This centralized import approach reduces boilerplate code and provides
a consistent interface for drawing operations across the apiwx framework.
"""


from wx import (
    # Drawing context for paint operations
    PaintDC,
    
    # Drawing tools
    Pen,
    
    # Brush style constants for various patterns
    BRUSHSTYLE_BDIAGONAL_HATCH,
    BRUSHSTYLE_CROSS_HATCH,
    BRUSHSTYLE_FDIAGONAL_HATCH,
    BRUSHSTYLE_HORIZONTAL_HATCH,
    BRUSHSTYLE_VERTICAL_HATCH,
    BRUSHSTYLE_CROSSDIAG_HATCH,
    BRUSHSTYLE_SOLID,
    BRUSHSTYLE_FIRST_HATCH,
    BRUSHSTYLE_LAST_HATCH,
    
    # Stipple pattern styles
    BRUSHSTYLE_STIPPLE_MASK_OPAQUE,
    BRUSHSTYLE_STIPPLE_MASK,
    BRUSHSTYLE_STIPPLE,
    
    # Predefined brushes
    TRANSPARENT_BRUSH,
)


# Module-level constants and utilities
__all__ = [
    'PaintDC',
    'Pen',
    'BRUSHSTYLE_BDIAGONAL_HATCH',
    'BRUSHSTYLE_CROSS_HATCH',
    'BRUSHSTYLE_FDIAGONAL_HATCH',
    'BRUSHSTYLE_HORIZONTAL_HATCH',
    'BRUSHSTYLE_VERTICAL_HATCH',
    'BRUSHSTYLE_CROSSDIAG_HATCH',
    'BRUSHSTYLE_SOLID',
    'BRUSHSTYLE_FIRST_HATCH',
    'BRUSHSTYLE_LAST_HATCH',
    'BRUSHSTYLE_STIPPLE_MASK_OPAQUE',
    'BRUSHSTYLE_STIPPLE_MASK',
    'BRUSHSTYLE_STIPPLE',
    'TRANSPARENT_BRUSH',
]


# Example usage and common patterns
if __name__ == "__main__":
    print("apiwx.painttool - Paint utilities for wxPython")
    print("This module provides convenient imports for drawing operations")
    print("\nExample usage:")
    print("  from apiwx.painttool import PaintDC, Pen, TRANSPARENT_BRUSH")
    print("  # Create drawing context in paint event handler")
    print("  dc = PaintDC(self)")
    print("  dc.SetPen(Pen('#FF0000', 2))")
    print("  dc.SetBrush(TRANSPARENT_BRUSH)")
    print("  dc.DrawRectangle(10, 10, 100, 50)")

