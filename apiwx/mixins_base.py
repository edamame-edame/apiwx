"""Advanced mixins type system for apiwx with metaclass management.

This module provides BaseMixins classes (Singleton, Multiton) that function
as metaclass replacements rather than inheritance mixins. These mixins
enable dynamic class creation with sophisticated instance lifecycle management
for wxPython components.

Key classes:
    - Singleton: Ensures only one instance per class
    - Multiton: Manages multiple tracked instances per class

The mixins operate by replacing the target class's metaclass, allowing
fundamental control over instance creation and behavior while maintaining
clean separation from the inheritance hierarchy.
"""
import typing


try:
    from . import debug
    from . import core
    from .mixins_core import BaseMixins, MixinsType

except ImportError:
    import debug
    import core
    from mixins_core import BaseMixins, MixinsType


class Singleton(BaseMixins):
    """Singleton Pattern - Metaclass-Replacing Mixin.

    Implements the Singleton design pattern by replacing the target 
    class's metaclass to ensure only one instance is ever created.

    Behavior:
        - First instantiation creates and stores the instance
        - Subsequent instantiations return the same instance
        - Constructor arguments from first call are preserved

    Metaclass Replacement:
        >>> MyClass = SomeClass[Singleton]
        >>> assert type(MyClass) == Singleton # Singleton is now the metaclass
        >>> 
        >>> obj1 = MyClass("first") # Creates instance
        >>> obj2 = MyClass("second") # Returns same instance
        >>> assert obj1 is obj2 # True
        >>> assert obj1.name == "first" # Preserves first constructor args

    MRO Behavior:
        Singleton does NOT appear in MRO (it's the metaclass, not a parent 
        class):
        
        >>> MyClass.__mro__ # ['SomeClass<Singleton>', 'SomeClass', 'object']
        # Note: 'Singleton' not in MRO - this is correct
    """

    @property
    def instance(cls) -> typing.Any | None:
        """Get the singleton instance if it exists, else None"""
        return getattr(cls, '_instance', None)

    def __call__(cls, *args, **kwds):
        if not hasattr(cls, '_instance') or cls._instance is None:
            debug.internallog(
                "SNGLTON", 
                f"Creating singleton instance for {cls.__name__}."
            )
            cls._instance = super().__call__(*args, **kwds)

        return cls._instance


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
        >>> MyClass = SomeClass[Multiton]
        >>> assert type(MyClass) == Multiton # Multiton is now the metaclass
        >>> 
        >>> obj1 = MyClass("first") # Creates first instance
        >>> obj2 = MyClass("second") # Creates second instance
        >>> assert obj1 is not obj2 # True - different instances
        >>> assert obj1.name == "first" and obj2.name == "second" # Separate 
        ...     states

    MRO Behavior:
        Multiton does NOT appear in MRO (it's the metaclass, not a parent 
        class):
        
        >>> MyClass.__mro__ # ['SomeClass<Multiton>', 'SomeClass', 'object']
        # Note: 'Multiton' not in MRO - this is correct

    Instance Management:
        - `_instances`: Dictionary tracking all created instances
        - `_instance_counter`: Total count of instances created
    """

    def __call__(cls, *args, **kwds):
        # Initialize _instances dict if not exists for this specific class
        if not hasattr(cls, '_instances'):
            cls._instances = {}

        # Initialize _instance_counter if not exists for this specific class
        if not hasattr(cls, '_instance_counter'):
            cls._instance_counter = 0

        # Use instance counter as index
        index = core.UIIndexor(
            cls._instance_counter,
            cls._instances
        )

        # Increase counter
        cls._instance_counter += 1

        # Create new instance if not exists
        if index not in cls._instances:
            debug.internallog(
                "MULTITON", 
                f"Creating multiton instance for {cls.__name__}[{index}]."
            )
            # Create the instance and store it
            cls._instances[index] = super().__call__(*args, **kwds)
            # Also set it as an attribute for easy access
            setattr(cls, f"instance_{index}", cls._instances[index])

        else:
            debug.internallog(
                "MULTITON", 
                f"Refusing multiton instance for {cls.__name__}[{index}]."
            )

        # Return the instance
        return cls._instances[index]