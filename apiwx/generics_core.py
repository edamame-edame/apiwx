"""Generic type system for apiwx framework.

This module provides the core generic type system that enables dynamic
composition of functionality for wxPython wrapper classes. It implements
a metaclass-based approach that supports both regular generics and
metaclass-replacing BaseGenerics patterns.

The system allows developers to create flexible and reusable UI components
by applying generic types that modify class behavior, add functionality,
or replace the metaclass entirely for advanced patterns like Singleton
or Multiton.

Key Components:
    - GenericsType: Main metaclass for generic type functionality
    - BaseGenerics: Base class for metaclass-replacing generics

Example:
    >>> class MyWindow(wx.Frame, metaclass=GenericsType):
    ...     pass
    >>> 
    >>> # Apply regular generic functionality
    >>> EnhancedWindow = MyWindow[SomeGeneric]
    >>> 
    >>> # Apply metaclass-replacing generic
    >>> SingletonWindow = MyWindow[Singleton]
"""
import typing
import types
import wx.siplib as sip

try:
    from . import debug
except:
    import debug


class GenericsType(sip.wrappertype):
    """Metaclass for generic type system in wxPython applications.

    GenericsType provides a metaclass that enables generic programming patterns
    for wxPython wrapper classes. It allows dynamic composition of 
    functionality through generic type parameters, supporting both regular 
    generics and metaclass-replacing BaseGenerics.

    The class extends wx.siplib.wrappertype to maintain compatibility with
    wxPython's SIP-generated wrapper classes while adding generic capabilities.

    Key Features:
        - Generic type instantiation: MyClass[GenericType]
        - Namespace merging from generic types
        - BaseGenerics support for metaclass replacement
        - Automatic method collection and integration
        - Debug logging for generic operations

    Generic Types:
        - Regular Generics: Add functionality without changing metaclass
        - BaseGenerics: Replace metaclass entirely (Singleton, Multiton, etc.)

    Attributes:
        __generic_classes__: Tuple containing all applied generic types.

    Example:
        >>> class MyWindow(wx.Frame, metaclass=GenericsType):
        ...     pass
        >>> 
        >>> # Apply regular generic
        >>> EnhancedWindow = MyWindow[SomeGeneric]
        >>> 
        >>> # Apply BaseGenerics (metaclass replacement)
        >>> SingletonWindow = MyWindow[Singleton]
        >>> assert type(SingletonWindow) == Singleton
        >>> 
        >>> # Multiple generics
        >>> ComplexWindow = MyWindow[Generic1, Generic2]
    """
    __generic_classes__: tuple[type] = ()


    def __getitem__(cls, generics: type | tuple[type]) -> type:
        # If is single type, convert to tuple.
        if not isinstance(generics, tuple):
            generics = (generics,)

        # Check generics validity.
        base_generics, generics = cls._get_base_generics(generics)

        if base_generics is not None:
            metaclass = base_generics

        else:
            metaclass = cls.__class__

        # Create new class.
        new_cls: 'GenericsType' = types.new_class(
            f"{cls.__name__}<{','.join([t.__name__ for t in generics])}>",
            cls.__mro__,
            {'metaclass': metaclass},
            lambda ns: ns.update(cls.__dict__)
        )

        # Add __generic_classes__ attribute if not exists.
        if not hasattr(new_cls, '__generic_classes__'):
            new_cls.__generic_classes__ = ()

        if (new_cls.__generic_classes__ and
                isinstance(new_cls.__generic_classes__[0], BaseGenerics)):
            raise TypeError(
                "BaseGenerics-derived class is already set as metaclass, "
                "cannot add another BaseGenerics."
            )

        # Add generics to __generic_classes__.
        new_cls.__generic_classes__ = (
            (base_generics,) + new_cls.__generic_classes__
        )

        # Create new class namespace.
        new_cls._mro_generics_namespace(generics)

        debug.internaldebug_log(
            "GENERICS", 
            f"Created new generics class: {new_cls.__name__} "
            f"with metaclass {type(new_cls)} and bases {new_cls.__bases__}"
        )

        return new_cls


    def __call__(cls, *args, **kwds):
        # First, create instance.
        instance = super().__call__(*args, **kwds)

        # Get init_args and init_kwds.
        if hasattr(instance, 'init_args'):
            args += instance.init_args

        if hasattr(instance, 'init_kwds'):
            kwds.update(instance.init_kwds)

        if hasattr(cls, "meta__new__"):
            debug.internaldebug_log(
                "GENERICS", f"generics.__new__[] = {cls.meta__new__}"
            )

            # Then, call meta__new__ methods.
            for meta_new in cls.meta__new__:
                meta_new(cls, instance, *args, **kwds)

        if hasattr(cls, "meta__init__"):
            debug.internaldebug_log(
                "GENERICS", f"generics.__init__[] = {cls.meta__init__}"
            )

            # Finally, call meta__init__ methods.
            for meta_init in cls.meta__init__:
                meta_init(instance, *args, **kwds)

        return instance


    def _get_base_generics(
        cls, _generics: tuple[type]
    ) -> tuple[typing.Type['BaseGenerics'] | None, tuple[type]]:
        base_generics = []
        generics: tuple[type] = ()

        for generic_type in _generics:
            if issubclass(generic_type, BaseGenerics):
                base_generics.append(generic_type)

            elif isinstance(generic_type, type):
                generics += (generic_type,)

        if len(base_generics) > 1:
            raise ValueError(
                "Only one BaseGenerics-derived class is allowed "
                "per generic instantiation."
            )

        return base_generics[0] if base_generics else None, generics


    def _mro_generics_namespace(
        cls: 'GenericsType', 
        generics: tuple[type]
    ) -> dict:
        # Create added namespace.
        added_namespace = {}

        # Iterate generics.
        for generic_type in generics:
            # Already added.
            if generic_type in cls.__generic_classes__:
                debug.internaldebug_log(
                    "GENERICS", 
                    f"Generic '{generic_type.__name__}' already in "
                    f"__generic_classes__, skipping"
                )
                continue
            
            # Add generics type.
            cls.__generic_classes__ += (generic_type, )

            if isinstance(generic_type, sip.wrappertype):
                # UI type conflict.
                raise TypeError("Generic type cannot be a wrapper type")

            elif isinstance(generic_type, BaseGenerics):
                ... # Target is BaseGenerics, skip.

            else:
                cls._namespace_editor(generic_type, added_namespace)

        cls._link_namespace(added_namespace)

        return None


    def _namespace_editor(
        cls: 'GenericsType', 
        generic_type: type, 
        namespace: dict
    ):
        # Check all attributes.
        for attr_name in GenericsType.get_all_members(generic_type):
            # Get attribute.
            attribute = getattr(generic_type, attr_name)

            if attr_name == '__new__':
                if not hasattr(cls, 'meta__new__'):
                    cls.meta__new__ = []

                cls.meta__new__.append(attribute)

            elif attr_name == '__init__':
                if not hasattr(cls, 'meta__init__'):
                    cls.meta__init__ = []

                cls.meta__init__.append(attribute)

            elif attr_name.startswith('__') and attr_name.endswith('__'):
                continue # Skip special methods and attributes.
        
            else:
                # Add to namespace if not exists.
                if attr_name not in namespace:
                    namespace[attr_name] = attribute

                else:
                    # Skip existing attributes.
                    debug.internallog(
                        "GENERICS",
                        f"Attribute '{attr_name}' already exists"
                        f" in class '{cls.__name__}', skipping addition"
                        f" from generic '{generic_type.__name__}'")
    

    def _link_namespace(cls, namespace: dict[str, ]):
        # Iterate added namespace.
        for attr_name in namespace:
            # Get attribute.
            attribute = namespace[attr_name]
            # Set attribute to class.
            setattr(cls, attr_name, attribute)

        debug.internaldebug_log(
            "NAMESPC",
            f"namespace was created: {cls.__name__}.__dict__ = {cls.__dict__}"
        )

        return 


    def hasgenerics(cls, generics: type | tuple[type]) -> bool:
        if not isinstance(generics, tuple):
            generics = (generics,)

        for generic_type in generics:
            if not generic_type in cls.__generic_classes__:
                return False

        return True
    

    @staticmethod
    def get_all_members(cls) -> dict[str, typing.Any]:
        members = {}

        for base in reversed(cls.__mro__):
            if base is object:
                continue # Skip object class.

            members.update(base.__dict__)

        debug.internaldebug_log(
            "MEMBERS",
            f"All members of {cls.__name__}: {members}"
        )

        return members


class BaseGenerics(GenericsType):
    """Base class for metaclass-replacing generics.

    BaseGenerics is a special type of generic that replaces the metaclass 
    of the target class rather than just modifying its structure. This allows 
    for fundamental changes to class behavior, particularly instance creation 
    and lifecycle management.

    BaseGenerics vs Regular Generics:
        - BaseGenerics: Replaces the metaclass entirely 
          (e.g., Singleton, Multiton)
        - Regular Generics: Only modifies class structure without changing 
          metaclass

    When using BaseGenerics-derived classes, the metaclass is completely 
    replaced:
        >>> class MyClass(metaclass=GenericsType):
        ...     pass
        >>> SingletonClass = MyClass[Singleton]
        >>> assert type(SingletonClass) == Singleton  # Metaclass is replaced

    MRO Behavior:
        BaseGenerics classes do NOT appear in the MRO of generated classes 
        because they function as metaclasses, not parent classes:
        
        >>> SingletonClass.__mro__  
        # ('MyClass<Singleton>', 'MyClass', 'object')
        
        Note: 'Singleton' is NOT in MRO - this is correct behavior

    Use Cases:
        - Singleton Pattern: Replace instance creation to return same instance
        - Multiton Pattern: Manage multiple instances with custom logic
        - Factory Pattern: Custom object creation mechanisms
        - Lifecycle Management: Control object construction/destruction

    Implementation Requirements:
        BaseGenerics subclasses should implement:
        - __call__(): Custom instance creation logic
        - Class-level state management (e.g., _instance, _instances)

    Example:
        >>> class Singleton(BaseGenerics):
        ...     def __call__(cls, *args, **kwargs):
        ...         if not hasattr(cls, '_instance'):
        ...             cls._instance = super().__call__(*args, **kwargs)
        ...         return cls._instance
        >>> 
        >>> # Usage
        >>> MyClass = SomeClass[Singleton]  # Singleton becomes metaclass
        >>> obj1 = MyClass()  # Creates instance
        >>> obj2 = MyClass()  # Returns same instance
        >>> assert obj1 is obj2  # True
    """
    pass