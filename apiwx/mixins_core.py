"""Mixin type system for apiwx framework.

This module provides the core mixin type system that enables dynamic
composition of functionality for wxPython wrapper classes. It implements
a metaclass-based approach that supports both regular mixins and
metaclass-replacing BaseMixins patterns.

The system allows developers to create flexible and reusable UI components
by applying mixin types that modify class behavior, add functionality,
or replace the metaclass entirely for advanced patterns like Singleton
or Multiton.

Key Components:
    - MixinsType: Main metaclass for mixin type functionality
    - BaseMixins: Base class for metaclass-replacing mixins

Example:
    >>> class MyWindow(wx.Frame, metaclass=MixinsType):
    ...     pass
    >>> 
    >>> # Apply regular mixin functionality
    >>> EnhancedWindow = MyWindow[SomeMixin]
    >>> 
    >>> # Apply metaclass-replacing mixin
    >>> SingletonWindow = MyWindow[Singleton]
"""
import typing
import types
import wx.siplib as sip

try:
    from . import debug
except:
    import debug


class MixinsType(sip.wrappertype):
    """Metaclass for mixin type system in wxPython applications.

    MixinsType provides a metaclass that enables mixin programming patterns
    for wxPython wrapper classes. It allows dynamic composition of 
    functionality through mixin type parameters, supporting both regular 
    mixins and metaclass-replacing BaseMixins.

    The class extends wx.siplib.wrappertype to maintain compatibility with
    wxPython's SIP-generated wrapper classes while adding mixin capabilities.

    Key Features:
        - Mixin type instantiation: MyClass[MixinType]
        - Namespace merging from mixin types
        - BaseMixins support for metaclass replacement
        - Automatic method collection and integration
        - Debug logging for mixin operations

    Mixin Types:
        - Regular Mixins: Add functionality without changing metaclass
        - BaseMixins: Replace metaclass entirely (Singleton, Multiton, etc.)

    Attributes:
        __mixin_classes__: Tuple containing all applied mixin types.

    Example:
        >>> class MyWindow(wx.Frame, metaclass=MixinsType):
        ...     pass
        >>> 
        >>> # Apply regular mixin
        >>> EnhancedWindow = MyWindow[SomeMixin]
        >>> 
        >>> # Apply BaseMixins (metaclass replacement)
        >>> SingletonWindow = MyWindow[Singleton]
        >>> assert type(SingletonWindow) == Singleton
        >>> 
        >>> # Multiple mixins
        >>> ComplexWindow = MyWindow[Mixin1, Mixin2]
    """
    __mixin_classes__: tuple[type] = ()


    def __getitem__(cls, mixins: type | tuple[type]) -> type:
        # If is single type, convert to tuple.
        if not isinstance(mixins, tuple):
            mixins = (mixins,)

        # Check mixins validity.
        base_mixins, mixins = cls._get_base_mixins(mixins)

        if base_mixins is not None:
            metaclass = base_mixins

        else:
            metaclass = cls.__class__

        # Create new class.
        new_cls: 'MixinsType' = types.new_class(
            f"{cls.__name__}<{','.join([t.__name__ for t in mixins])}>",
            cls.__mro__,
            {'metaclass': metaclass},
            lambda ns: ns.update(cls.__dict__)
        )

        # Add __mixin_classes__ attribute if not exists.
        if not hasattr(new_cls, '__mixin_classes__'):
            new_cls.__mixin_classes__ = ()

        if (new_cls.__mixin_classes__ and
                isinstance(new_cls.__mixin_classes__[0], BaseMixins)):
            raise TypeError(
                "BaseMixins-derived class is already set as metaclass, "
                "cannot add another BaseMixins."
            )

        # Add mixins to __mixin_classes__.
        new_cls.__mixin_classes__ = (
            (base_mixins,) + new_cls.__mixin_classes__
        )

        # Create new class namespace.
        new_cls._mro_mixins_namespace(mixins)

        debug.internaldebug_log(
            "MIXINS", 
            f"Created new mixins class: {new_cls.__name__} "
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
                "MIXINS", f"mixins.__new__[] = {cls.meta__new__}"
            )

            # Then, call meta__new__ methods.
            for meta_new in cls.meta__new__:
                meta_new(cls, instance, *args, **kwds)

        if hasattr(cls, "meta__init__"):
            debug.internaldebug_log(
                "MIXINS", f"mixins.__init__[] = {cls.meta__init__}"
            )

            # Finally, call meta__init__ methods.
            for meta_init in cls.meta__init__:
                meta_init(instance, *args, **kwds)

        return instance


    def _get_base_mixins(
        cls, _mixins: tuple[type]
    ) -> tuple[typing.Type['BaseMixins'] | None, tuple[type]]:
        base_mixins = []
        mixins: tuple[type] = ()

        for mixin_type in _mixins:
            if issubclass(mixin_type, BaseMixins):
                base_mixins.append(mixin_type)

            elif isinstance(mixin_type, type):
                mixins += (mixin_type,)

        if len(base_mixins) > 1:
            raise ValueError(
                "Only one BaseMixins-derived class is allowed "
                "per mixin instantiation."
            )

        return base_mixins[0] if base_mixins else None, mixins


    def _mro_mixins_namespace(
        cls: 'MixinsType', 
        mixins: tuple[type]
    ) -> dict:
        # Create added namespace.
        added_namespace = {}

        # Iterate mixins.
        for mixin_type in mixins:
            # Already added.
            if mixin_type in cls.__mixin_classes__:
                debug.internaldebug_log(
                    "MIXINS", 
                    f"Mixin '{mixin_type.__name__}' already in "
                    f"__mixin_classes__, skipping"
                )
                continue
            
            # Add mixins type.
            cls.__mixin_classes__ += (mixin_type, )

            if isinstance(mixin_type, sip.wrappertype):
                # UI type conflict.
                raise TypeError("Mixin type cannot be a wrapper type")

            elif isinstance(mixin_type, BaseMixins):
                ... # Target is BaseMixins, skip.

            else:
                cls._namespace_editor(mixin_type, added_namespace)

        cls._link_namespace(added_namespace)

        return None


    def _namespace_editor(
        cls: 'MixinsType', 
        mixin_type: type, 
        namespace: dict
    ):
        # Check all attributes.
        for attr_name in MixinsType.get_all_members(mixin_type):
            # Get attribute.
            attribute = getattr(mixin_type, attr_name)

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
                        "MIXINS",
                        f"Attribute '{attr_name}' already exists"
                        f" in class '{cls.__name__}', skipping addition"
                        f" from mixin '{mixin_type.__name__}'")
    

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


    def hasmixins(cls, mixins: type | tuple[type]) -> bool:
        if not isinstance(mixins, tuple):
            mixins = (mixins,)

        for mixin_type in mixins:
            if not mixin_type in cls.__mixin_classes__:
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


class BaseMixins(MixinsType):
    """Base class for metaclass-replacing mixins.

    BaseMixins is a special type of mixin that replaces the metaclass 
    of the target class rather than just modifying its structure. This allows 
    for fundamental changes to class behavior, particularly instance creation 
    and lifecycle management.

    BaseMixins vs Regular Mixins:
        - BaseMixins: Replaces the metaclass entirely 
          (e.g., Singleton, Multiton)
        - Regular Mixins: Only modifies class structure without changing 
          metaclass

    When using BaseMixins-derived classes, the metaclass is completely 
    replaced:
        >>> class MyClass(metaclass=MixinsType):
        ...     pass
        >>> SingletonClass = MyClass[Singleton]
        >>> assert type(SingletonClass) == Singleton  # Metaclass is replaced

    MRO Behavior:
        BaseMixins classes do NOT appear in the MRO of generated classes 
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
        BaseMixins subclasses should implement:
        - __call__(): Custom instance creation logic
        - Class-level state management (e.g., _instance, _instances)

    Example:
        >>> class Singleton(BaseMixins):
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