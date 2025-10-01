"""Type stubs for apiwx.generics_app module."""

from typing import TypeVar, Type
from .core import WrappedWindow
from .generics_common import AutoDetect

# A type variable for auto detect window class
DetectWindow: Type[AutoDetect[WrappedWindow]]