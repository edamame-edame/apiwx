"""
# Generics System for apiwx
"""
import typing
import types
import wx.siplib as sip
import inspect
import collections


try:
    from .import debug

except:
    import debug


class GenericsType(sip.wrappertype):
    __generic_classes__: tuple[type] = ()


    def __getitem__(cls, generics: type | tuple[type]) -> type:
        # if is single type, convert to tuple
        if not isinstance(generics, tuple):
            generics = (generics,)

        # check generics validity
        base_generics, generics = cls._get_base_generics(generics)

        if base_generics is not None:
            metaclass = base_generics

        else:
            metaclass = cls.__class__

        # add __generic_classes__ attribute if not exists
        if not hasattr(cls, '__generic_classes__'):
            cls.__generic_classes__ = ()

        print(cls.__dict__)

        # create new class
        new_cls: 'GenericsType' = types.new_class(
            f"{cls.__name__}<{','.join([t.__name__ for t in generics])}>",
            cls.__mro__,
            {'metaclass': metaclass},
            lambda ns: ns.update(cls.__dict__)
        )

        # create new class namespace
        new_cls._mro_generics_namespace(generics)

        return new_cls


    def __call__(cls, *args, **kwds):
        # first, create instance
        instance = super().__call__(*args, **kwds)

        # get init_args and init_kwds
        if hasattr(instance, 'init_args'):
            args += instance.init_args

        if hasattr(instance, 'init_kwds'):
            kwds.update(instance.init_kwds)

        if hasattr(cls, "meta__new__"):
            debug.internaldebug_log("GENERICS", f"generics.__new__[] = {cls.meta__new__}")

            # then, call meta__new__ methods
            for meta_new in cls.meta__new__:
                meta_new(cls, instance, *args, **kwds)

        if hasattr(cls, "meta__init__"):
            debug.internaldebug_log("GENERICS", f"generics.__init__[] = {cls.meta__init__}")

            # finally, call meta__init__ methods
            for meta_init in cls.meta__init__:
                meta_init(instance, *args, **kwds)

        return instance


    def _get_base_generics(cls, _generics: tuple[type]) -> tuple[typing.Type['BaseGenerics'] | None, tuple[type]]:
        base_generics = []
        generics: tuple[type] = ()

        for generic_type in _generics:
            if issubclass(generic_type, BaseGenerics):
                base_generics.append(generic_type)

            elif isinstance(generic_type, type):
                generics += (generic_type, )

        if len(base_generics) > 1:
            raise ValueError("Only one BaseGenerics-derived class is allowed per generic instantiation.")

        return base_generics[0] if base_generics else None, generics


    def _mro_generics_namespace(cls: 'GenericsType', generics: tuple[type]) -> dict:
        # create added namespace
        added_namespace = {}

        # iterate generics
        for generic_type in generics:
            # already added
            if generic_type in cls.__generic_classes__:
                debug.internaldebug_log("GENERICS", f"Generic '{generic_type.__name__}' already in __generic_classes__, skipping")
                continue # already added
            
            # add generics type
            cls.__generic_classes__ += (generic_type, )

            if isinstance(generic_type, sip.wrappertype):
                # UI type conflict
                raise TypeError("Generic type cannot be a wrapper type")

            elif isinstance(generic_type, BaseGenerics):
                ... # target is BaseGenerics, skip

            else:
                cls._namespace_editor(generic_type, added_namespace)

        cls._link_namespace(added_namespace)

        return None


    def _namespace_editor(cls: 'GenericsType', generic_type: type, namespace: dict):
        # check all attributes
        for attr_name in generic_type.__dict__:
            # get attribute
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
                continue # skip special methods and attributes
        
            else:
                # add to namespace if not exists
                if attr_name not in namespace:
                    namespace[attr_name] = attribute

                else:
                    # skip existing attributes
                    debug.internallog(
                        "GENERICS",
                        f"Attribute '{attr_name}' already exists"
                        f" in class '{cls.__name__}', skipping addition"
                        f" from generic '{generic_type.__name__}'")
    

    def _link_namespace(cls, namespace: dict[str, ]):
        # iterate added namespace
        for attr_name in namespace:
            # get attribute
            attribute = namespace[attr_name]
            # set attribute to class
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
    

    def get_all_members(cls) -> dict:
        members = {}

        for base in reversed(cls.__mro__):
            members.update(base.__dict__)

        return members


class BaseGenerics(GenericsType):
    """
    # Base class for metaclass-replacing generics

    BaseGenerics is a special type of generic that **replaces the metaclass** of the target class
    rather than just modifying its structure. This allows for fundamental changes to class behavior,
    particularly instance creation and lifecycle management.

    ## Design Intent:

    ### BaseGenerics vs Regular Generics:
    - **BaseGenerics**: Replaces the metaclass entirely (e.g., Singleton, Multiton)
    - **Regular Generics**: Only modifies class structure without changing metaclass

    ### Metaclass Replacement Behavior:
    When using BaseGenerics-derived classes:
    ```python
    # Before: MyClass has GenericsType as metaclass
    class MyClass(metaclass=GenericsType):
    pass

    # After: MyClass[Singleton] has Singleton as metaclass
    SingletonClass = MyClass[Singleton]
    assert type(SingletonClass) == Singleton # Metaclass is replaced
    ```

    ### MRO Behavior:
    BaseGenerics classes do NOT appear in the MRO of generated classes because they
    function as metaclasses, not parent classes:
    ```python
    SingletonClass.__mro__ # ['MyClass<Singleton>', 'MyClass', 'object']
    # Note: 'Singleton' is NOT in MRO - this is correct behavior
    ```

    ### Use Cases:
    - **Singleton Pattern**: Replace instance creation to return same instance
    - **Multiton Pattern**: Manage multiple instances with custom logic
    - **Factory Pattern**: Custom object creation mechanisms
    - **Lifecycle Management**: Control object construction/destruction

    ### Implementation Requirements:
    BaseGenerics subclasses should implement:
    - `__call__()`: Custom instance creation logic
    - Class-level state management (e.g., `_instance`, `_instances`)

    ### Example:
    ```python
    class Singleton(BaseGenerics):
    def __call__(cls, *args, **kwargs):
    if not hasattr(cls, '_instance'):
    cls._instance = super().__call__(*args, **kwargs)
    return cls._instance

    # Usage
    MyClass = SomeClass[Singleton] # Singleton becomes metaclass
    obj1 = MyClass() # Creates instance
    obj2 = MyClass() # Returns same instance
    assert obj1 is obj2 # True
    ```
    """
    pass