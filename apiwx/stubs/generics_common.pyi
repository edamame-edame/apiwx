"""Type stubs for apiwx.generics_common module."""

from typing import TypeVar, Generic, Type

T = TypeVar('T')

class AutoDetect(Generic[T]):
    """A type variable for auto detect target class."""
    
    def __init__(self, target_class: Type[T]) -> None: ...

class FixSize:
    """Fixed size configuration."""
    
    def __init__(self, width: int, height: int) -> None: ...
    
    @property
    def width(self) -> int: ...
    
    @property
    def height(self) -> int: ...