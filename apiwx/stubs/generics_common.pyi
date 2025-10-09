"""Type stubs for apiwx.generics_common module.

This module provides type information for shared generic classes and mixins
that can be used across different wxPython UI components, enabling proper
type checking and IDE support.
"""

import typing
import types
from typing import TypeVar, Generic, Type, Dict, Any, Tuple, Union
from . import core

T = TypeVar('T')

class FixSize:
    """Mixin class to fix the size of UI components.

    FixSize prevents resizing of windows or panels by setting both
    minimum and maximum size constraints to the current size. This
    ensures the component maintains a fixed size throughout its
    lifecycle.
    """
    
    def __init__(self: core.UIAttributes, *args: Any, **kwds: Any) -> None: ...

class AutoDetect(Generic[T]):
    """Generic type for automatic detection of UI components.

    AutoDetect provides automatic detection and management of UI components
    based on specified target types. It scans object attributes to identify
    instances or classes that match the detection criteria and maintains
    a registry of child components.
    """
    
    detect_target: Tuple[Type[T], ...]
    children: Dict[core.UIIndexor, core.UIAttributes]
    
    def __init__(self, *args: Any, **kwds: Any) -> None: ...
    
    @classmethod
    def __class_getitem__(cls, target: Union[Type[T], Tuple[Type[T], ...]]) -> Type['AutoDetect[T]']: ...
    
    def detect_children(self) -> Dict[core.UIIndexor, core.UIAttributes]: ...
    def get_child(self, index: int) -> core.UIAttributes: ...
    def get_children_by_type(self, target_type: Type[T]) -> Dict[core.UIIndexor, T]: ...