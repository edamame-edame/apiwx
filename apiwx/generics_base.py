"""
# apiwx.generics_base - Advanced Generics Type System

## Overview

This module provides an advanced generics type system for apiwx, enabling dynamic class creation with sophisticated inheritance patterns and metaclass management. The system allows for type-safe generic programming with wxPython components.

## Core Components

### BaseGenerics - Metaclass-Replacing Generics
The base class for generics that **replace the metaclass** of target classes rather than just modifying their structure. This enables fundamental changes to class behavior, particularly instance creation and lifecycle management.

#### Design Philosophy:
- **BaseGenerics**: Replaces metaclass entirely (Singleton, Multiton, etc.)
- **Regular Generics**: Only modifies class structure without changing metaclass

#### Metaclass Replacement Behavior:
```python
# Original class with GenericsType metaclass
class MyClass(metaclass=GenericsType):
    pass

# BaseGenerics usage - metaclass is replaced
SingletonClass = MyClass[Singleton]
assert type(SingletonClass) == Singleton # Metaclass replaced by Singleton
```

#### MRO Implications:
BaseGenerics classes do NOT appear in the Method Resolution Order (MRO) because they function as metaclasses:
```python
SingletonClass.__mro__ # ['MyClass<Singleton>', 'MyClass', 'object']
# Note: 'Singleton' is NOT in MRO - this is CORRECT behavior
# Singleton operates as metaclass, not parent class
```

### GenericsType Metaclass
A sophisticated metaclass that provides:
- Dynamic generic class creation via `__getitem__()` syntax
- Custom metaclass generation for specialized generic types
- Method Resolution Order (MRO) management
- Namespace injection for generic parameters

## Key Features

### 1. Single Base Generics Constraint
The system enforces that only **one** `BaseGenerics`-derived class can be used per generic instantiation:

```python
class SpecialGeneric(BaseGenerics):
    pass

class AnotherGeneric(BaseGenerics):
    pass

# Valid: Single base generics
MyClass[SpecialGeneric]

# Invalid: Multiple base generics (raises ValueError)
MyClass[SpecialGeneric, AnotherGeneric]
```

### 2. Custom Metaclass Generation
When a `BaseGenerics`-derived class is detected, the system creates a custom metaclass that:

1. **Inherits from both the base generics class and GenericsType**
2. **Preserves all GenericsType functionality**
3. **Extends behavior with generics-specific features**

```python
# Generated metaclass hierarchy:
CustomGenericsType_SpecialGeneric
├── SpecialGeneric (base_generics)
│ └── BaseGenerics
└── GenericsType
    └── sip.wrappertype
    └── type
    └── object
```

### 3. Dynamic Class Creation Flow

```mermaid
graph TD
    A[MyClass[Generic]] --> B{Detect BaseGenerics?}
    B -->|Yes| C[Validate Single Generic]
    B -->|No| D[Use Standard GenericsType]
    C -->|Valid| E[Create Custom Metaclass]
    C -->|Multiple| F[Raise ValueError]
    E --> G[Generate New Class with Custom Metaclass]
    D --> H[Generate New Class with Standard Metaclass]
    G --> I[Apply MRO and Namespace Updates]
    H --> I
```

### 4. Type Safety and Validation
- **Runtime type checking** ensures only valid generic parameters
- **Inheritance validation** prevents invalid class hierarchies
- **Namespace isolation** prevents naming conflicts

### 5. Debug and Introspection
The system provides comprehensive debug logging:
- MRO (Method Resolution Order) tracking
- Namespace update monitoring
- Generic class detection logging
- Custom metaclass creation tracking

## Usage Examples

### IMPORTANT: BaseGenerics Design Pattern

**Critical Understanding**: BaseGenerics classes (Singleton, Multiton) function as **metaclass replacements**, not inheritance mixins. This is a fundamental design decision with important implications:

#### Metaclass vs Inheritance:
```python
# WRONG expectation: Inheritance-based thinking
SomeClass[Singleton].__mro__ # Expecting: [..., 'Singleton', ...]

# CORRECT behavior: Metaclass-based reality
SomeClass[Singleton].__mro__ # Actual: ['SomeClass<Singleton>', 'SomeClass', 'object']
type(SomeClass[Singleton]) # Actual: <class 'Singleton'> (metaclass)
```

#### Why This Design:
1. **Instance Control**: Metaclasses control instance creation at the most fundamental level
2. **Clean Separation**: Pattern logic is separate from class hierarchy
3. **Flexibility**: Allows combining with regular inheritance without conflicts
4. **Performance**: Direct metaclass operation is more efficient than inheritance chains

#### Testing Implications:
When testing BaseGenerics functionality, do NOT expect the generic class to appear in MRO. Test the actual behavior (singleton/multiton logic) instead of the inheritance structure.

### Basic Generic Class
```python
from apiwx.generics_base import BaseGenerics, GenericsType

class MyGeneric(BaseGenerics):
    def generic_method(self):
    return "from generic"

class MyClass(metaclass=GenericsType):
    def base_method(self):
    return "from base"

# Create specialized version
SpecializedClass = MyClass[MyGeneric]
instance = SpecializedClass()

# Access both base and generic methods
print(instance.base_method()) # "from base"
print(instance.generic_method()) # "from generic"
```

### Advanced Generic with Custom Behavior
```python
class ConfigurableGeneric(BaseGenerics):
    @classmethod
    def configure(cls, **options):
    cls._options = options

    def get_config(self, key):
    return getattr(self.__class__, '_options', {}).get(key)

class ConfigurableWidget(metaclass=GenericsType):
    def __init__(self):
    self.setup()

    def setup(self):
    if hasattr(self, 'get_config'):
    self.theme = self.get_config('theme') or 'default'

# Usage
ConfigurableGeneric.configure(theme='dark', size='large')
DarkWidget = ConfigurableWidget[ConfigurableGeneric]
widget = DarkWidget() # Automatically configured with dark theme
```

## Error Handling

### Multiple Base Generics Error
```python
class Generic1(BaseGenerics): pass
class Generic2(BaseGenerics): pass

try:
    MyClass[Generic1, Generic2]
except ValueError as e:
    # "Multiple base generics found: [Generic1, Generic2]. Only one base generics class is allowed."
    print(e)
```

### Invalid Generic Type Error
```python
class NotAGeneric: pass

try:
    MyClass[NotAGeneric]
    # This won't raise error but won't get special treatment
except Exception as e:
    print(e)
```

## Technical Details

### Metaclass Creation Process
1. **Detection**: Scan generic parameters for `BaseGenerics` subclasses
2. **Validation**: Ensure only one base generics class exists
3. **Generation**: Create custom metaclass using `types.new_class()`
4. **Integration**: Combine base generics functionality with GenericsType
5. **Application**: Apply custom metaclass to target class

### Method Resolution Order (MRO)
The generated classes follow Python's C3 linearization algorithm:
```python
# For MyClass[SpecialGeneric]
MRO = [
    MyClass[SpecialGeneric],
    MyClass,
    SpecialGeneric,
    BaseGenerics,
    object
]
```

### Namespace Management
- **Isolated namespaces** prevent conflicts between generic parameters
- **Namespace injection** allows generic classes to add methods/properties
- **Late binding** ensures proper method resolution at runtime

## Performance Considerations

- **Lazy evaluation**: Generic classes are created only when accessed
- **Caching**: Generated classes are cached to avoid regeneration
- **Minimal overhead**: Runtime performance impact is negligible
- **Memory efficiency**: Shared base class data reduces memory usage

## Compatibility

- **Python 3.13+**: Full compatibility with modern Python features
- **wxPython 4.0+**: Compatible with wxPython's sip-based architecture
- **Type hints**: Full support for modern Python type hinting
- **IDE integration**: Compatible with code completion and static analysis

"""
import typing


try:
    from . import debug
    from . import core
    from .generics_core import BaseGenerics, GenericsType

except ImportError:
    import debug
    import core
    from generics_core import BaseGenerics, GenericsType


class Singleton(BaseGenerics):
    '''
    # Singleton Pattern - Metaclass-Replacing Generic

    Implements the Singleton design pattern by replacing the target class's metaclass
    to ensure only one instance is ever created.

    ## Behavior:
    - First instantiation creates and stores the instance
    - Subsequent instantiations return the same instance
    - Constructor arguments from first call are preserved

    ## Metaclass Replacement:
    ```python
    MyClass = SomeClass[Singleton]
    assert type(MyClass) == Singleton # Singleton is now the metaclass

    obj1 = MyClass("first") # Creates instance
    obj2 = MyClass("second") # Returns same instance
    assert obj1 is obj2 # True
    assert obj1.name == "first" # Preserves first constructor args
    ```

    ## MRO Behavior:
    Singleton does NOT appear in MRO (it's the metaclass, not a parent class):
    ```python
    MyClass.__mro__ # ['SomeClass<Singleton>', 'SomeClass', 'object']
    # Note: 'Singleton' not in MRO - this is correct
    ```
    '''
    _instance: typing.ClassVar[typing.Any | None]

    @property
    def instance(cls) -> typing.Any | None:
        """Get the singleton instance if it exists, else None"""
        return getattr(cls, '_instance', None)

    def __call__(cls, *args, **kwds):
        if not hasattr(cls, '_instance') or cls._instance is None:
            debug.internallog("SNGLTON", f"Creating singleton instance for {cls.__name__}.")
            cls._instance = super().__call__(*args, **kwds)

        return cls._instance


class Multiton(BaseGenerics):
    '''
    # Multiton Pattern - Metaclass-Replacing Generic

    Implements the Multiton design pattern by replacing the target class's metaclass
    to manage multiple instances with custom lifecycle logic.

    ## Behavior:
    - Each instantiation creates a new instance
    - Instances are tracked in _instances dictionary
    - Instance counter tracks total number of instances created

    ## Metaclass Replacement:
    ```python
    MyClass = SomeClass[Multiton]
    assert type(MyClass) == Multiton # Multiton is now the metaclass

    obj1 = MyClass("first") # Creates first instance
    obj2 = MyClass("second") # Creates second instance
    assert obj1 is not obj2 # True - different instances
    assert obj1.name == "first" and obj2.name == "second" # Separate states
    ```

    ## MRO Behavior:
    Multiton does NOT appear in MRO (it's the metaclass, not a parent class):
    ```python
    MyClass.__mro__ # ['SomeClass<Multiton>', 'SomeClass', 'object']
    # Note: 'Multiton' not in MRO - this is correct
    ```

    ## Instance Management:
    - `_instances`: Dictionary tracking all created instances
    - `_instance_counter`: Total count of instances created
    '''
    _instances: typing.ClassVar[dict[typing.Any, typing.Any]]

    _instance_counter: typing.ClassVar[int]


    def __call__(cls, *args, **kwds):
        # create _instances dict if not exists
        if not hasattr(cls, '_instances'):
            cls._instances = {}

        # create _instance_counter if not exists
        if not hasattr(cls, '_instance_counter'):
            cls._instance_counter = 0

        # use instance counter as index
        index = core.UIIndexor(
            cls._instance_counter,
            cls._instances
        )

        # increase counter
        cls._instance_counter += 1

        # create new instance if not exists
        if index not in cls._instances:
            debug.internallog("MULTITON", f"Creating multiton instance for {cls.__name__}[{index}].")
            # Create the instance and store it
            cls._instances[index] = super().__call__(*args, **kwds)
            # Also set it as an attribute for easy access
            setattr(cls, f"instance_{index}", cls._instances[index])

        else:
            debug.internallog("MULTITON", f"Refusing multiton instance for {cls.__name__}[{index}].")

        # return the instance
        return cls._instances[index]