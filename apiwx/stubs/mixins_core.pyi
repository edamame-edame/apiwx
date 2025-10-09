"""Type stubs for apiwx.mixins_core module.

This module provides type information for the core mixin type system that
enables dynamic composition of functionality for wxPython wrapper classes.
"""

import typing
import types
from typing import Any, TypeVar, Union, Tuple, Dict
import wx.siplib as sip

T = TypeVar('T')
MixinType = TypeVar('MixinType')

class MixinsType(sip.wrappertype):
    """Metaclass for mixin type system in wxPython applications.

    MixinsType provides a metaclass that enables mixin programming patterns
    for wxPython wrapper classes. It allows dynamic composition of 
    functionality through mixin type parameters, supporting both regular 
    mixins and metaclass-replacing BaseMixins.
    """
    
    __mixin_classes__: tuple[type, ...]
    
    def __getitem__(cls, mixins: Union[type, Tuple[type, ...]]) -> type: ...
    def __call__(cls, *args: Any, **kwds: Any) -> Any: ...
    
    def _get_base_mixins(
        cls, 
        mixins: Tuple[type, ...]
    ) -> Tuple[Union[type, None], Tuple[type, ...]]: ...
    
    def _mro_mixins_namespace(
        cls, 
        mixins: Tuple[type, ...]
    ) -> Dict[str, Any]: ...
    
    def _namespace_editor(
        cls,
        namespace: Dict[str, Any],
        mixins: Tuple[type, ...]
    ) -> Dict[str, Any]: ...
    
    def _link_namespace(cls, namespace: Dict[str, Any]) -> None: ...
    
    def hasmixins(cls, mixins: Union[type, Tuple[type, ...]]) -> bool: ...
    
    @staticmethod
    def get_all_members(cls: type) -> Dict[str, Any]: ...

class BaseMixins(MixinsType):
    """Base class for metaclass-replacing mixin patterns.
    
    This class serves as the base for mixin types that need to replace
    the metaclass entirely, such as Singleton and Multiton patterns.
    When applied as a mixin, it becomes the new metaclass for the target class.
    
    BaseMixins provides the foundation for advanced mixin patterns that
    require complete control over class creation and instance management.
    
    Examples of BaseMixins subclasses:
        - Singleton: Ensures only one instance exists
        - Multiton: Manages multiple named instances
        - Factory: Controls object creation patterns
        
    Usage:
        >>> class MyClass(SomeBase, metaclass=MixinsType):
        ...     pass
        >>> 
        >>> # Apply BaseMixins - this replaces the metaclass
        >>> SingletonClass = MyClass[Singleton]  
        >>> assert type(SingletonClass) == Singleton
        >>> 
        >>> # Multiple instances return the same object
        >>> obj1 = SingletonClass()
        >>> obj2 = SingletonClass()
        >>> assert obj1 is obj2
    """
    pass