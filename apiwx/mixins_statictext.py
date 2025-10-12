"""StaticText mixin behaviors for apiwx components.

This module provides specialized mixin classes for WrappedStaticText components
that enhance text positioning and alignment capabilities. These mixins enable
automatic text positioning within parent containers and dynamic layout management.

Key Components:
    TextAlign: Enumeration for text alignment options (top, center, bottom, etc.)
    LocateByParent: Mixin for automatic text positioning within parent window

The StaticText mixins are designed to work seamlessly with the apiwx mixin system,
providing enhanced text layout capabilities while maintaining the clean, intuitive
API that apiwx is known for.

Usage Example:
    >>> import apiwx
    >>> from apiwx.mixins_statictext import LocateByParent, TextAlign
    >>> 
    >>> app = apiwx.WrappedApp("Text Alignment Demo")
    >>> window = apiwx.WrappedWindow(app, title="Demo", size=(400, 300))
    >>> 
    >>> # Create aligned text using mixin
    >>> class AlignedText(apiwx.WrappedStaticText[LocateByParent]):
    ...     pass
    >>> 
    >>> # Center-aligned text
    >>> center_text = AlignedText(window, label="Centered", align="c")
    >>> 
    >>> # Top-right aligned text
    >>> tr_text = AlignedText(window, label="Top Right", align=TextAlign.TOPRIGHT)
    >>> 
    >>> app.mainloop()

Features:
    - Nine alignment positions (top-left, top, top-right, left, center, right, bottom-left, bottom, bottom-right)
    - String-based or enum-based alignment specification
    - Automatic positioning calculation based on parent window size
    - Dynamic repositioning support for window resize events
    - Clean integration with existing apiwx mixin architecture

The module follows apiwx coding standards and provides comprehensive type hints
for enhanced IDE support and development experience.
"""


import enum
import typing

try:
    from . import core
    from . import debug

except ImportError:
    import core
    import debug


class TextAlign(enum.Enum):
    TOP="t"
    TOPLEFT="tl"
    LEFT="l"
    BOTTOMLEFT="bl"
    BOTTOM="b"
    BOTTOMRIGHT="br"
    RIGHT="r"
    TOPRIGHT="tr"
    CENTER="c"
    
    @classmethod
    def from_value(cls, value: str) -> 'TextAlign':
        """Get TextAlign enum member from its value string.
        
        Args:
            value (str): The value string to look up.
            
        Returns:
            TextAlign: The corresponding enum member.
            
        Raises:
            ValueError: If the value is not found.
        """
        for member in cls:
            if member.value == value:
                return member
        raise ValueError(f"No TextAlign member with value '{value}'")


class LocateByParent:
    """Mixin to align text within a parent window based on specified alignment.
    LocateByParent allows positioning of static text components within their
    parent window according to a chosen alignment option. The alignment can be
    set using the TextAlign enum or corresponding string keys.
    The mixin automatically updates the text position when the parent window
    is resized or when the text content changes.

    Properties:
        align: Text alignment within the parent window (TextAlign or str)

    Example:
        >>> class AlignedText(core.WrappedStaticText[LocateByParent]):
        ...     def __init__(self, parent):
        ...         super().__init__(parent, label="Hello", align="c")
        ...         # Text will be centered within the parent window
        >>> 
        >>> # Change alignment after creation
        >>> text = AlignedText(parent)
        >>> text.align = TextAlign.BOTTOMRIGHT  # Move to bottom-right"""
    
    @property
    def align(self) -> TextAlign:
        """Get the current text alignment.

        Returns:
            TextAlign: The current text alignment setting.
        """
        return self._align

    @align.setter
    def align(self, value: TextAlign | str):
        """Set the text alignment.

        Args:
            value (TextAlign | str): The desired text alignment, either as
                a TextAlign enum member or a string key.
        """
        self.update_location(value)
    
    def __init__(
            self: typing.Type[typing.Self] | core.WrappedStaticText,
            *args,
            label: str,
            align: TextAlign | str,
            **kwds):
        # Super class init was called from WrappedWindow.__init__.
        # So do nothing here.
        ...

        # Below code was called after super class init.
        if not isinstance(align, TextAlign):
            # Handle string input by looking up the value
            align = TextAlign.from_value(align)
        
        self._align = align

        self.layout() # Make sure the initial layout is set.

    def SetText(self, label: str):
        """Set the text label and update its position.

        Args:
            label (str): The new text label to display.
        """
        super().SetLabel(label)

        self.update_location(self._align)

    def update_location(self, align: TextAlign | str):
        """Update the location of the text based on alignment.

        This method should be called whenever the parent window is resized
        or when the text content changes to ensure correct positioning.
        """
        if not isinstance(align, TextAlign):
            align = TextAlign.from_value(align)

        self._align = align

        # Calculate X position
        if 'l' in align.value:  # LEFT alignment
            x = 0
        elif 'r' in align.value:  # RIGHT alignment
            x = self.parent.size[0] - self.size[0]
        else:  # CENTER alignment
            x = (self.parent.size[0] - self.size[0]) // 2

        # Calculate Y position
        if 't' in align.value:  # TOP alignment
            y = 0
        elif 'b' in align.value:  # BOTTOM alignment
            y = self.parent.size[1] - self.size[1]
        else:  # CENTER alignment (vertical)
            y = (self.parent.size[1] - self.size[1]) // 2

        self.pos = (x, y)
        
        return