"""Panel transition model for apiwx applications.

This module provides panel transition management functionality for wxPython
applications built with the apiwx framework. It enables smooth panel
switching and visibility management within window containers.

Key Components:
    NotTransition: Marker class to exclude panels from transition system
    SupportTransit: Mixin class for panels supporting transitions
    TransitPanelContainer: Container class for managing panel transitions
    PanelTransModel: Core model for panel state and transition logic

The transition system automatically manages panel visibility, allowing
only one panel to be visible at a time while maintaining references to
all panels for quick switching operations.
"""


try:
    from . import core
    from . import debug
    from .generics_core import GenericsType
    from . import generics_window

except ImportError:
    import core
    import debug
    from generics_core import GenericsType
    import generics_window


class NotTransition:
    """Marker class to exclude panels from transition management.

    This class serves as a generic marker to identify panels that should
    not participate in the automatic panel transition system. Panels
    with this generic will remain visible and won't be managed by the
    PanelTransModel.

    Usage:
        >>> class MyStaticPanel(WrappedPanel[NotTransition]):
        ...     pass  # This panel won't be hidden during transitions
    """
    pass


class SupportTransit(generics_window.DetectPanel):
    """Mixin class to add transition support to panels.

    This class provides panel transition functionality by automatically
    detecting child panels and managing them through a PanelTransModel
    instance. It excludes panels marked with NotTransition from the
    transition system.

    Attributes:
        panel_trans (PanelTransModel): The transition model instance.
    """

    @property
    def panel_trans(self) -> 'PanelTransModel':
        """Get the panel transition model.

        Returns:
            PanelTransModel: The transition model managing child panels.
        """
        return self._panel_trans

    def __new__(cls, instance, *args, **kwds):
        """Create a new instance with transition support.

        Args:
            cls: The class being instantiated.
            instance: The base instance to enhance.
            *args: Variable length argument list.
            **kwds: Arbitrary keyword arguments.

        Returns:
            The enhanced instance with transition support.
        """
        instance = generics_window.DetectPanel.__new__(
            cls, instance, *args, **kwds
        )

        return instance

    def __init__(self, *args, **kwds):
        """Initialize the transition support.

        Args:
            *args: Variable length argument list.
            **kwds: Arbitrary keyword arguments.
        """
        generics_window.DetectPanel.__init__(self, *args, **kwds)

        self._panel_trans = PanelTransModel()

        for child_id in self.children:
            child: core.WrappedPanel = self.children[child_id]

            if not GenericsType.hasgenerics(child, NotTransition):
                self.panel_trans.add(child_id, child)

        debug.internaldebug_log("TRANSIT",
                               "Panels: {}".format(self.panel_trans))


class TransitPanelContainer:
    """Container class for managing panel transitions.

    This mixin class provides panel transition management for WrappedWindow
    or WrappedPanel instances. It automatically detects child panels and
    sets up a transition model to manage their visibility.

    Example:
        >>> class MyWindow(WrappedWindow[DetectPanel, TransitPanelContainer]):
        ...     def __init__(self, parent):
        ...         super().__init__(parent)
        ...         # Panels are automatically managed by transition system
    """

    panel_trans: 'PanelTransModel'

    def __init__(self, *args, **kwds):
        """Initialize the panel container with transition support.

        Args:
            *args: Variable length argument list.
            **kwds: Arbitrary keyword arguments.
        """
        self.panel_trans = PanelTransModel()

        debug.internaldebug_log("TRANSIT",
                               "Panels: {}".format(self.panel_trans))

        for child_id in self.children:
            child: core.WrappedPanel = self.children[child_id]

            if not GenericsType.hasgenerics(child, NotTransition):
                self.panel_trans.add(child_id, child)


class PanelTransModel(dict[core.UIIndexor, core.WrappedPanel]):
    """Panel transition model for managing panel visibility.

    This class extends dict to provide a mapping between UI indexors and
    wrapped panels, with automatic visibility management. Only one panel
    can be visible at a time, and transitions between panels are handled
    automatically.

    The model maintains the current active panel and provides methods for
    adding, removing, and transitioning between panels.

    Attributes:
        _now (core.UIIndexor | None): The currently active panel indexor.
    """
    _now: core.UIIndexor | None

    @property
    def now(self) -> core.UIIndexor | None:
        """Get the current panel indexor.

        Returns:
            core.UIIndexor | None: The currently active panel indexor,
                or None if no panel is active.
        """
        return self._now

    @now.setter
    def now(self, indexor: core.UIIndexor | None) -> None:
        """Set the current panel indexor.

        Args:
            indexor (core.UIIndexor | None): The indexor to set as current,
                or None to hide all panels.

        Raises:
            TypeError: If indexor is not UIIndexor or None.
        """
        if (indexor is not None and 
            not isinstance(indexor, core.UIIndexor)):
            raise TypeError('indexor must be an instance of '
                          'core.UIIndexor or None')

        self.trans(indexor)

    @property
    def is_show_any(self) -> bool:
        """Check if any panel is currently shown.

        Returns:
            bool: True if a panel is currently visible, False otherwise.
        """
        return self.now is not None

    def __init__(self):
        """Initialize the panel transition model.

        Sets up an empty model with no active panel.
        """
        super(PanelTransModel, self).__init__()

        self._now = None

    def add(self, indexor: core.UIIndexor, panel: core.WrappedPanel) -> None:
        """Add a panel with the given indexor.

        Args:
            indexor (core.UIIndexor): The unique identifier for the panel.
            panel (core.WrappedPanel): The panel to add to the model.

        Raises:
            TypeError: If indexor or panel are not of correct type.
            KeyError: If indexor already exists in the model.
        """
        if not isinstance(indexor, core.UIIndexor):
            raise TypeError('indexor must be an instance of core.UIIndexor')

        if not isinstance(panel, core.WrappedPanel):
            raise TypeError('panel must be an instance of '
                          'core.WrappedPanel')

        if indexor in self:
            raise KeyError('indexor already exists')

        if GenericsType.hasgenerics(panel.__class__, NotTransition):
            return  # Do nothing for NotTransition panels

        if len(self) == 0:
            # Make sure the panel is shown first
            self._now = indexor

        else:
            # Hide the panel
            panel.Hide()

        super(PanelTransModel, self).__setitem__(indexor, panel)

    def __setitem__(self, indexor: core.UIIndexor,
                    panel: core.WrappedPanel) -> None:
        """Add a panel using dictionary syntax.

        Args:
            indexor (core.UIIndexor): The unique identifier for the panel.
            panel (core.WrappedPanel): The panel to add to the model.
        """
        self.add(indexor, panel)

    def remove(self, indexor: core.UIIndexor) -> None:
        """Remove the panel with the given indexor.

        Args:
            indexor (core.UIIndexor): The indexor of the panel to remove.
        """
        if indexor in self:
            if self.now == indexor:
                self.now = None

            super(PanelTransModel, self).__delitem__(indexor)

    def trans(self, indexor: core.UIIndexor) -> bool:
        """Transition to the panel with the given indexor.

        Args:
            indexor (core.UIIndexor): The indexor of the panel to show.

        Returns:
            bool: True if any panel is now visible, False otherwise.
        """
        if self.now is not None:
            self._now.hide()
            self._now = None

        if indexor in self:
            if indexor.show():
                self._now = indexor

        return self.is_show_any