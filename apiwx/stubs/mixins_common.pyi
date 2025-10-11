"""Type stubs for apiwx.mixins_common module.

This module provides type information for shared mixin classes and mixins
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
    """Mixin type for automatic detection of UI components.

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
    
    @classmethod
    def get_all_members(cls) -> Dict[str, Any]: ...
    
    @classmethod
    def is_detectable_class(cls, classobj: Type) -> bool: ...
    
    @classmethod
    def is_detectable_instance(cls, instance: object) -> bool: ...
    
    def get_instance_members(self) -> Dict[str, Any]:
        """Get all instance members for runtime detection.

        This method retrieves all instance attributes that can be detected
        at runtime, including those added after __new__ but before or during
        __init__.

        Returns:
            Dictionary of instance attribute names and their values.
        """
    
    def detect_children(self) -> Dict[core.UIIndexor, core.UIAttributes]: ...
    def get_child(self, index: int) -> core.UIAttributes: ...
    def get_children_by_type(self, target_type: Type[T]) -> Dict[core.UIIndexor, T]: ...
    def search_child_indexor(self, target_class: Type[core.UIAttributes]) -> Tuple[core.UIIndexor, ...]:
        """Search and return all child indexors of the specified type.

        This method scans the instance for child components that match the
        specified target class and returns their indexors as a tuple. It is
        useful for retrieving all registered child components that have been
        automatically detected and indexed.

        Args:
            target_class: The target class type to search for.

        Returns:
            Tuple containing all child indexors found for the specified type.
            Returns an empty tuple if no matching children are found.
            
            - For singleton mixin: Returns tuple with single indexor
            - For multiton mixin: Returns tuple with multiple indexors
            - For empty results: Returns empty tuple
        """