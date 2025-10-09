"""Type stubs for apiwx.generics_core module.

This module provides type information for the core generic type system that
enables dynamic composition of functionality for wxPython wrapper classes.
"""

import typing
import types
from typing import Any, TypeVar, Union, Tuple, Dict
import wx.siplib as sip

T = TypeVar('T')
GenericType = TypeVar('GenericType')

class GenericsType(sip.wrappertype):
    """Metaclass for generic type system in wxPython applications.

    GenericsType provides a metaclass that enables generic programming patterns
    for wxPython wrapper classes. It allows dynamic composition of 
    functionality through generic type parameters, supporting both regular 
    generics and metaclass-replacing BaseGenerics.
    """
    
    __generic_classes__: tuple[type, ...]
    
    def __getitem__(cls, generics: Union[type, Tuple[type, ...]]) -> type: ...
    def __call__(cls, *args: Any, **kwds: Any) -> Any: ...
    
    def _get_base_generics(
        cls, 
        generics: Tuple[type, ...]
    ) -> Tuple[Union[type, None], Tuple[type, ...]]: ...
    
    def _mro_generics_namespace(
        cls, 
        generics: Tuple[type, ...]
    ) -> Dict[str, Any]: ...
    
    def _namespace_editor(
        cls,
        namespace: Dict[str, Any],
        generics: Tuple[type, ...]
    ) -> Dict[str, Any]: ...
    
    def _link_namespace(cls, namespace: Dict[str, Any]) -> None: ...
    
    def hasgenerics(cls, generics: Union[type, Tuple[type, ...]]) -> bool: ...
    
    @staticmethod
    def get_all_members(cls: type) -> Dict[str, Any]: ...

class BaseGenerics(GenericsType):
    """Base class for metaclass-replacing generic patterns.
    
    This class serves as the base for generic types that need to replace
    the metaclass entirely, such as Singleton and Multiton patterns.
    When applied as a generic, it becomes the new metaclass for the target class.
    
    BaseGenerics provides the foundation for advanced generic patterns that
    require complete control over class creation and instance management.
    
    Examples of BaseGenerics subclasses:
        - Singleton: Ensures only one instance exists
        - Multiton: Manages multiple named instances
        - Factory: Controls object creation patterns
        
    Usage:
        >>> class MyClass(SomeBase, metaclass=GenericsType):
        ...     pass
        >>> 
        >>> # Apply BaseGenerics - this replaces the metaclass
        >>> SingletonClass = MyClass[Singleton]  
        >>> assert type(SingletonClass) == Singleton
        >>> 
        >>> # Multiple instances return the same object
        >>> obj1 = SingletonClass()
        >>> obj2 = SingletonClass()
        >>> assert obj1 is obj2
    """
    pass