"""Type stubs for apiwx.mixins_base module.

This module provides type information for BaseMixins classes (Singleton, 
Multiton) that function as metaclass replacements for advanced instance 
lifecycle management patterns.
"""

import typing
from typing import Any, Optional, Dict
from .mixins_core import BaseMixins

class Singleton(BaseMixins):
    """Singleton Pattern - Metaclass-Replacing Mixin.

    Implements the Singleton design pattern by replacing the target 
    class's metaclass to ensure only one instance is ever created.

    Behavior:
        - First instantiation creates and stores the instance
        - Subsequent instantiations return the same instance
        - Constructor arguments from first call are preserved

    Metaclass Replacement:
        When applied as a mixin type, Singleton becomes the metaclass
        of the target class, not a parent class in the inheritance hierarchy.
    """
    
    @property
    def instance(cls) -> Optional[Any]: 
        """Get the singleton instance if it exists, else None."""
        ...
    
    def __call__(cls, *args: Any, **kwds: Any) -> Any: ...

class Multiton(BaseMixins):
    """Multiton Pattern - Metaclass-Replacing Mixin.

    Implements the Multiton design pattern by replacing the target 
    class's metaclass to manage multiple instances with custom lifecycle 
    logic.

    Behavior:
        - Each instantiation creates a new instance
        - Instances are tracked in _instances dictionary
        - Instance counter tracks total number of instances created

    Metaclass Replacement:
        When applied as a mixin type, Multiton becomes the metaclass
        of the target class, not a parent class in the inheritance hierarchy.
    """
    
    @property
    def instances(cls) -> Dict[str, Any]: 
        """Get dictionary of all tracked instances."""
        ...
    
    @property
    def instance_count(cls) -> int: 
        """Get total number of instances created."""
        ...
    
    def __call__(cls, *args: Any, **kwds: Any) -> Any: ...