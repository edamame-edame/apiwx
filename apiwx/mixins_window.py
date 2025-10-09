"""Mixin type definitions for wxPython window components.

This module provides mixin type definitions and mixin classes for
wxPython window objects, particularly wx.Frame and related window
components. It includes size management utilities and auto-detection
types for panel components within windows.

The module focuses on providing enhanced window management capabilities
through mixin classes that modify default window behavior, such as
size handling based on client area dimensions rather than total window
size including decorations.
"""
try:
    from . import core
    from . import mixins_common
except ImportError:
    import core
    import mixins_common


class ByPanelSize:
    """Panel size mixin to manage window size based on client panel size.

    ByPanelSize provides size management functionality for wxPython windows
    where the window size is controlled by the internal panel (client area)
    size rather than the total window size including decorations. This is
    useful when you want to specify the usable content area size directly.

    The class modifies the size property behavior to work with client size
    instead of window size, ensuring that the specified dimensions represent
    the actual usable space within the window frame.

    Properties:
        size: Gets/sets the client area size instead of total window size.

    Example:
        >>> window = WrappedWindow[ByPanelSize](
        ...     app,
        ...     panel_size=(800, 600)
        ... )
        >>> window.show()
        >>> app.mainloop()
        >>> 
        >>> # The window client area will be exactly 800x600 pixels
        >>> # regardless of window decorations (title bar, borders, etc.)
    """


    @property
    def size(self: core.WrappedWindow) -> tuple[int, int]:
        """Get the client area size of the window.

        Returns:
            tuple[int, int]: The client area size as (width, height) tuple.
        """
        return self.clientsize

    @size.setter
    def size(self: core.WrappedWindow, value: tuple[int, int]):
        """Set the client area size of the window.

        Args:
            value (tuple[int, int]): The desired client area size as
                (width, height) tuple.
        """
        self.clientsize = value


    def __init__(self: core.WrappedWindow, *args, **kwds):
        """Initialize the ByPanelSize mixin.

        This method sets up the window size management based on client area.
        The actual initialization is handled by WrappedWindow.__init__, so
        this method primarily configures the client size after the parent
        initialization is complete.

        Args:
            *args: Variable length argument list passed to parent class.
            **kwds: Arbitrary keyword arguments passed to parent class.
        """
        # Super class init was called from WrappedWindow.__init__.
        # So do nothing here.
        ...

        # Below code was called after super class init.
        # Set size (panel size is client size).
        self.clientsize = self.GetSize()

        # End of __init__.
        return


DetectPanel = mixins_common.AutoDetect[
    core.WrappedPanel
]
"""Type variable for auto-detecting panel components in windows.

This type alias provides automatic type detection for panel components
that are used within wxPython window objects. It enables type checkers
to properly identify and validate panel components for better type safety
and IDE support in window-based applications.

The type variable is specifically designed for detecting WrappedPanel
instances within window containers, facilitating automatic component
discovery and management in window-panel hierarchies.
"""

