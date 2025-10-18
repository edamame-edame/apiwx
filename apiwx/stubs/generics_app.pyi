"""Type stubs for apiwx.generics_app module.

This module provides type information for generic type definitions and type 
variables for wxPython application objects, enabling proper type checking 
and IDE support.
"""

from typing import Type
from .core import Window
from .generics_common import AutoDetect

# Type alias for auto-detecting window class
DetectWindow: Type[AutoDetect[Window]]
"""Type variable for auto-detecting window class.

This type alias provides automatic type detection for window classes
used in wxPython applications. It allows type checkers to infer the
correct window type based on the usage context.
"""