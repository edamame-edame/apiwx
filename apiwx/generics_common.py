"""Common generic type definitions for wxPython components.

This module provides shared generic classes and mixins that can be used
across different wxPython UI components. It includes utilities for size
management, automatic component detection, and dynamic type creation.

Key classes:
    - FixSize: Mixin to prevent component resizing
    - AutoDetect: Generic type for automatic UI component detection

These generics enable flexible composition patterns and automatic component
management in wxPython applications.
"""
import typing
import types


try:
    from . import core
    from . import debug
    from . import generics_core

except ImportError:
    import core
    import debug
    import generics_core


class FixSize:
    """Mixin class to fix the size of UI components.

    FixSize prevents resizing of windows or panels by setting both
    minimum and maximum size constraints to the current size. This
    ensures the component maintains a fixed size throughout its
    lifecycle.

    The class should be used as a mixin with UI components that
    inherit from core.UIAttributes. It automatically applies size
    constraints during initialization.

    Example:
        >>> class FixedWindow(core.WrappedWindow[FixSize]):
        ...     def __init__(self):
        ...         super().__init__()
        ...         # Window size is now fixed and cannot be resized
        >>> 
        >>> class FixedPanel(core.WrappedPanel[FixSize]):
        ...     def __init__(self, parent):
        ...         super().__init__(parent)
        ...         # Panel size is now fixed and cannot be resized
    """
    def __init__(self: core.UIAttributes, *args, **kwds):
        # Fix the size of the window/panel.
        self.size_max = self.size
        self.size_min = self.size


class AutoDetect:
    """Generic type for automatic detection of UI components.

    AutoDetect provides automatic detection and management of UI components
    based on specified target types. It scans object attributes to identify
    instances or classes that match the detection criteria and maintains
    a registry of child components.

    The class supports generic syntax for specifying detection targets:
    AutoDetect[TargetType] creates a specialized detector for TargetType.

    Attributes:
        detect_target: Tuple of target types to detect.
        children: Dictionary of detected child components indexed by UIIndexor.

    Example:
        >>> # Single target detection - detect window components
        >>> DetectWindow = AutoDetect[core.WrappedWindow]
        >>> 
        >>> # Multiple target detection - detect various UI components
        >>> DetectChildren = AutoDetect[
        ...     core.WrappedPanel,
        ...     core.WrappedButton,
        ...     core.WrappedTextBox
        ... ]
        >>> 
        >>> # Use in a class with generics
        >>> class MyApp(core.WrappedApp[DetectWindow]):
        ...     def __init__(self):
        ...         super().__init__()
        ...         # Windows are automatically detected and managed
    """
    detect_target: tuple[core.UIAttributes, ...] = ()

    def __new__(
        cls: typing.Type['AutoDetect'], 
        instance: 'AutoDetect', 
        *args, 
        **kwds
    ):
        # Create object.
        # Super class init was called from WrappedApp.__new__.
        # So do nothing here.
        ...

        # Below code was called after super class init.

        # Init children namelist.
        instance._children_namelist = []

        members = cls.get_all_members()

        debug.internaldebug_log("CHILDREN", f"__dict__ = {members}")

        # Scan attributes.
        for attr_name in members:
            # Check target instance.
            if (cls.is_detectable_class(members[attr_name])
             or cls.is_detectable_instance(members[attr_name])):
                # Add to children namelist.
                instance._children_namelist.append(attr_name)

        debug.internaldebug_log(
            "CHILDREN", 
            f"__children_namelist__ = {instance._children_namelist}"
        )

        # End of __new__.
        return instance

    def __init__(self, *args, **kwds):
        # Create object.
        # Super class init was called from WrappedApp.__new__.
        # So do nothing here.
        ...

        # Below code was called after super class init.

        # Init children counter.
        self._children_counter = 0

        # Scan children namelist.
        for child_name in self._children_namelist:
            # Get child window.
            child = getattr(self, child_name)

            # Check detectable subclass.
            if self.is_detectable_class(child):
                # Create instance.
                child = child(self)

            if self.is_detectable_instance(child):
                # Increase counter.
                index = core.UIIndexor(
                    self._children_counter,
                    self.children
                )
                
                self._children_counter += 1

                # Set index attribute.
                setattr(
                    self, 
                    f"child_{index}", 
                    index
                )

                debug.uilog(
                    "CHILDREN", 
                    f"Created, child_{index} = {child_name}	({child})"
                )

                # Add to children dict.
                self.children[index] = child

    def __class_getitem__(
        cls, 
        detect_target: tuple[core.UIAttributes, ...] | core.UIAttributes
    ) -> type:
        if not isinstance(detect_target, tuple):
            detect_target = (detect_target,)

        for target in detect_target:
            if not issubclass(target, core.UIAttributes):
                raise TypeError(
                    'detect_target must be an instance of core.UIAttributes '
                    'or a tuple of core.UIAttributes'
                )

        # Create new class namespace.
        new_cls_namespace = cls.get_all_members()

        # Add detect target.
        new_cls_namespace["detect_target"] = detect_target

        # Create new class.
        target_names = ', '.join([t.__name__ for t in detect_target])
        class_name = f"{cls.__name__}<{target_names}>"
        new_cls = types.new_class(
            class_name,
            cls.__mro__,
            {},
            lambda ns: ns.update(new_cls_namespace)
        )

        return new_cls

    @property
    def children(self) -> dict[core.UIIndexor, typing.Type]:
        # Lazy init.
        if not hasattr(self, '_children'):
            self._children = {}

        return self._children

    @classmethod
    def is_detectable_class(cls, classobj: typing.Type) -> bool:
        return (
            # Check type instance.
            (isinstance(classobj, type))
            # Check target subclass.
            and (issubclass(classobj, cls.detect_target))
        )
    

    @classmethod
    def is_detectable_instance(cls, instance: object) -> bool:
        return (
            # Check object instance.
            (isinstance(instance, object))
            # Check target instance.
            and (isinstance(instance, cls.detect_target))
        )
    

    @classmethod
    def get_all_members(cls) -> dict[str, typing.Any]:
        return (
            generics_core
             .GenericsType
              .get_all_members(cls)
        )

