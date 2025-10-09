"""Mixin type definitions for wxPython wx.Panel components.

This module provides mixin type definitions, mixins, and type variables
for wxPython panel objects and their child components. It includes border
drawing functionality and auto-detection types for panel children that
can be used with type checkers and IDEs to provide better type safety
and code completion.

Key Components:
    - WithBoarder: Mixin class for adding border drawing functionality
    - DetectChildren: Type variable for auto-detecting panel child components

The module enables developers to create enhanced panel components with
visual borders and automatic child component type detection for improved
development experience and type safety.
"""
try:
    from . import core
    from . import mixins_common
    from . import painttool
    from . import debug

except ImportError:
    import core
    import mixins_common
    import painttool
    import debug


class WithBoarder():
    """Mixin class to add border drawing functionality to UI components.

    WithBoarder provides configurable border drawing capabilities for wxPython
    UI components. It manages border properties (color, thickness, offset) and
    automatically draws borders on paint events. The class is designed to be
    used as a mixin with other UI component classes.

    The border is drawn as a rectangle around the component's edges with
    customizable appearance. Border drawing is automatically connected to
    the paint event and removed after the first draw to optimize performance.

    Properties:
        boarder_color: Color of the border (default: "#000000")
        boarder_thickness: Thickness of the border in pixels (default: 3)
        boarder_offset: Offset from component edges in pixels (default: 0)

    Example:
        >>> class BorderedPanel(core.WrappedPanel[WithBoarder]):
        ...     def __init__(self, parent):
        ...         super().__init__(parent, boarder_color="#FF0000", 
        ...                         boarder_thickness=5)
        ...         # Panel will automatically draw a red border
        >>> 
        >>> # Customize border after creation
        >>> panel = BorderedPanel(parent)
        >>> panel.boarder_color = "#0000FF"  # Change to blue
        >>> panel.boarder_thickness = 2      # Make thinner
    """
    @property
    def default_boarder_color(self) -> str:
        """Get the default border color.

        Returns:
            str: Default border color value ("#000000").
        """
        return "#000000"

    @property
    def boarder_color(self) -> str:
        """Get the current border color.

        Returns:
            str: Current border color, or default if not set.
        """
        if not hasattr(self, '_boarder_color'):
            return self.default_boarder_color

        return self._boarder_color

    @boarder_color.setter
    def boarder_color(self, value: str | None):
        """Set the border color.

        Args:
            value (str | None): Border color value or None for default.
        """
        if(value is None):
            value = self.default_boarder_color

        self._boarder_color = value


    @property
    def default_boarder_thickness(self) -> int:
        """Get the default border thickness.

        Returns:
            int: Default border thickness value (3 pixels).
        """
        return 3

    @property
    def boarder_thickness(self) -> int:
        """Get the current border thickness.

        Returns:
            int: Current border thickness in pixels, or default if not set.
        """
        if not hasattr(self, '_boarder_thickness'):
            return self.default_boarder_thickness

        return self._boarder_thickness

    @boarder_thickness.setter
    def boarder_thickness(self, value: int | None):
        """Set the border thickness.

        Args:
            value (int | None): Border thickness in pixels or None for default.
        """
        if(value is None):
            value = self.default_boarder_thickness

        self._boarder_thickness = value


    @property
    def default_boarder_offset(self) -> int:
        """Get the default border offset.

        Returns:
            int: Default border offset value (0 pixels).
        """
        return 0

    @property
    def boarder_offset(self) -> int:
        """Get the current border offset.

        Returns:
            int: Current border offset in pixels, or default if not set.
        """
        if not hasattr(self, '_boarder_offset'):
            return self.default_boarder_offset

        return self._boarder_offset

    @boarder_offset.setter
    def boarder_offset(self, value: int | None):
        """Set the border offset.

        Args:
            value (int | None): Border offset in pixels or None for default.
        """
        if(value is None):
            value = self.default_boarder_offset

        self._boarder_offset = value


    def __init__(
        self,
        *args,
        boarder_color: str | None = None,
        boarder_thickness: int | None = None,
        boarder_offset: int | None = None,
        **kwds):
        """Initialize the WithBoarder mixin.

        Sets up border drawing functionality with configurable properties
        and connects the border drawing method to the paint event.

        Args:
            *args: Variable length argument list passed to parent class.
            boarder_color (str | None): Border color or None for default.
            boarder_thickness (int | None): Border thickness or None for
                default.
            boarder_offset (int | None): Border offset or None for default.
            **kwds: Arbitrary keyword arguments passed to parent class.
        """
        # Super class init was called from WrappedWindow.__init__.
        # So do nothing here.
        ...

        # Below code was called after super class init.

        # Set boarder color.
        self.boarder_color = boarder_color

        # Set boarder thickness.
        self.boarder_thickness = boarder_thickness

        # Set boarder offset from panel frame.
        self.boarder_offset = boarder_offset

        # Connect slots for paint boarder.
        self.slots_on_paint += (
            self.draw_boarder
        )


    def draw_boarder(self, *args, **kwds):
        """Draw the border around the component.

        This method is automatically called during paint events to draw
        the configured border. After drawing, it removes itself from the
        paint event slots to optimize performance.

        Args:
            *args: Variable length argument list from paint event.
            **kwds: Arbitrary keyword arguments from paint event.
        """
        debug.uilog(
            "BOARDER",
            f"Draw boarder: {self.boarder_color}, "
            f"{self.boarder_thickness}, "
            f"{self.boarder_offset}")

        # Get panel size.
        width, height = self.size

        # Create draw context.
        device_context = painttool.PaintDC(
            self
        )

        # Set pen color to boarder_color.
        device_context.SetPen(
            painttool.Pen(
                self.boarder_color,
                self.boarder_thickness
            )
        )

        # Set fill color to transparent.
        device_context.SetBrush(
            painttool.TRANSPARENT_BRUSH
        )

        x0 = self.boarder_offset + self.boarder_thickness // 2
        y0 = self.boarder_offset + self.boarder_thickness // 2
        x = width - int(self.boarder_offset + self.boarder_thickness // 2)
        y = height - int(self.boarder_offset + self.boarder_thickness // 2)

        # Draw rectangle.
        device_context.DrawRectangle(
            x0, y0, x, y
        )

        debug.uilog("DRAWRECT", f"Rect(x0, x, y0, y) = ({x0}, {x}, {y0}, {y})")

        # Remove draw slot.
        self.slots_on_paint -= (
            self.draw_boarder
        )


DetectChildren = mixins_common.AutoDetect[
    core.WrappedPanel,
    core.WrappedTextBox,
    core.WrappedButton,
    core.WrappedCheckBox,
    core.WrappedComboBox,
    core.WrappedChoice,
    core.WrappedStaticText,
    core.WrappedImage,
    core.WrappedListBox,
    core.WrappedListCtrl,
    core.WrappedRadioBox,
    core.WrappedScrolledWindow,
    core.WrappedSlider,
]
"""Type variable for auto-detecting panel child components.

This type alias provides automatic type detection for common UI components
that are typically used as children within wxPython panels. It enables
type checkers to properly identify and validate panel child components
for better type safety and IDE support.

Supported child component types:
    - WrappedPanel: Nested panel containers
    - WrappedTextBox: Text input fields
    - WrappedButton: Clickable buttons
    - WrappedCheckBox: Checkbox controls
    - WrappedComboBox: Dropdown combo boxes
    - WrappedChoice: Choice selection controls
    - WrappedStaticText: Static text labels
    - WrappedImage: Image display components
    - WrappedListBox: List selection boxes
    - WrappedListCtrl: Advanced list controls
    - WrappedRadioBox: Radio button groups
    - WrappedScrolledWindow: Scrollable containers
    - WrappedSlider: Slider input controls
"""

