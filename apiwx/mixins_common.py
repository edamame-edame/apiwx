"""Common mixin type definitions for wxPython components.

This module provides shared mixin classes and utilities that can be used
across different wxPython UI components. It includes utilities for size
management, automatic component detection, and dynamic type creation.

Key classes:
    - FixSize: Mixin to prevent component resizing
    - AutoDetect: Mixin type for automatic UI component detection

These mixins enable flexible composition patterns and automatic component
management in wxPython applications.
"""
import typing
import types


try:
    from . import core
    from . import debug
    from . import mixins_core
    from . import mixins_base

except ImportError:
    import core
    import debug
    import mixins_core
    import mixins_base


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
        >>> class FixedWindow(core.Window[FixSize]):
        ...     def __init__(self):
        ...         super().__init__()
        ...         # Window size is now fixed and cannot be resized
        >>> 
        >>> class FixedPanel(core.Panel[FixSize]):
        ...     def __init__(self, parent):
        ...         super().__init__(parent)
        ...         # Panel size is now fixed and cannot be resized
    """
    def __init__(self: core.UIAttributes, *args, **kwds):
        # Fix the size of the window/panel.
        self.size_max = self.size
        self.size_min = self.size


class AutoDetect:
    """Mixin type for automatic detection of UI components.

    AutoDetect provides automatic detection and management of UI components
    based on specified target types. It scans object attributes to identify
    instances or classes that match the detection criteria and maintains
    a registry of child components.

    The class supports mixin syntax for specifying detection targets:
    AutoDetect[TargetType] creates a specialized detector for TargetType.

    Attributes:
        detect_target: Tuple of target types to detect.
        children: Dictionary of detected child components indexed by UIIndexor.

    Example:
        >>> # Single target detection - detect window components
        >>> DetectWindow = AutoDetect[core.Window]
        >>> 
        >>> # Multiple target detection - detect various UI components
        >>> DetectChildren = AutoDetect[
        ...     core.Panel,
        ...     core.Button,
        ...     core.TextBox
        ... ]
        >>> 
        >>> # Use in a class with mixins
        >>> class MyApp(core.App[DetectWindow]):
        ...     def __init__(self):
        ...         super().__init__()
        ...         # Windows are automatically detected and managed
    """
    detect_target: tuple[core.UIAttributes, ...] = ()

    def __new__(
        cls: typing.Type['AutoDetect'], 
        instance: 'AutoDetect', 
        *args, 
        **kwds):
        # Create object.
        # Super class init was called from App.__new__.
        # So do nothing here.
        ...

        # Below code was called after super class init.

        # Init children namelist for class-level detection.
        instance._children_namelist = []

        # Scan class-level attributes using get_all_members from the instance's actual class
        class_members = mixins_core.MixinsType.get_all_members(cls)
        debug.internaldebug_log("CHILDREN", f"Class scanning {cls.__name__}, actual class: {cls.__name__}")
        debug.internaldebug_log("CHILDREN", f"Class members = {class_members}")

        debug.internaldebug_log(
            "CHILDREN", 
            f"Target is = {instance.detect_target}"
        )

        # Scan class attributes.
        for attr_name in class_members:
            # Check target instance.
            if (cls.is_detectable_class(class_members[attr_name])
             or cls.is_detectable_instance(class_members[attr_name])):
                # Add to children namelist.
                instance._children_namelist.append(attr_name)

        debug.internaldebug_log(
            "CHILDREN", 
            f"Class-level __children_namelist__ = {instance._children_namelist}"
        )

        # End of __new__.
        return instance

    def __init__(self, *args, **kwds):
        # Create object.
        # Super class init was called from App.__new__.
        # So do nothing here.
        ...

        # Below code was called after super class init.

        # Init children counter.
        self._children_counter = 0

        # Add instance-level detection for attributes that might be added after __new__
        instance_members = self.get_instance_members()
        debug.internaldebug_log("CHILDREN", f"Instance members = {instance_members}")

        # Scan instance attributes that weren't found in class-level scan
        for attr_name in instance_members:
            if attr_name not in self._children_namelist:
                # Check target instance.
                if (self.is_detectable_class(instance_members[attr_name])
                 or self.is_detectable_instance(instance_members[attr_name])):
                    # Add to children namelist.
                    self._children_namelist.append(attr_name)

        debug.internaldebug_log(
            "CHILDREN", 
            f"Final __children_namelist__ = {self._children_namelist}"
        )

        # Scan children namelist.
        for child_name in self._children_namelist:
            # Get child window.
            child = getattr(self, child_name)

            debug.internaldebug_log(
                "CHILDREN", 
                f"Item found, {child_name} = {child}"
            )

            # Check detectable subclass.
            if self.is_detectable_class(child):
                # Create instance.
                child = child(self)

                debug.uilog(
                    "CHILDREN", 
                    f"Constructed, {child_name} = {child}"
                )

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
            and (not mixins_core.MixinsType.hasmixins(
                        classobj, mixins_base.Multiton))
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
            mixins_core
             .MixinsType
              .get_all_members(cls)
        )

    def get_instance_members(self) -> dict[str, typing.Any]:
        """Get all instance members for runtime detection.

        This method retrieves all instance attributes that can be detected
        at runtime, including those added after __new__ but before or during
        __init__.

        Returns:
            dict[str, typing.Any]: Dictionary of instance attribute names
            and their values.
        """
        instance_members = {}
        
        # Get instance __dict__ if available
        if hasattr(self, '__dict__'):
            instance_members.update(self.__dict__)
        
        debug.internaldebug_log(
            "MEMBERS",
            f"Instance members of {self.__class__.__name__}: {instance_members}"
        )
        
        return instance_members


    def search_child_indexor(self, target_class: typing.Type[core.UIAttributes]) -> tuple[core.UIIndexor, ...]:
        """Search and return all child indexors.

        This method scans the instance for attributes that are of type
        core.UIIndexor and returns them as a tuple. It is useful for
        retrieving all registered child components that have been
        automatically detected and indexed.

        Returns:
            tuple[core.UIIndexor, ...]: A tuple containing all child
            indexors found in the instance.
        """
        indexors = []

        for indexor in self.children:
            child = self.children[indexor]

            if isinstance(child, target_class):
                indexors.append(indexor)

        return tuple(indexors)