"""Type stubs for mixins_statictext module."""

from typing import Any, Union
from typing_extensions import Self
from enum import Enum


class TextAlign(Enum):
    """Text alignment options for StaticText components."""
    TOPLEFT = "tl"
    TOPRIGHT = "tr"
    BOTTOMLEFT = "bl"
    BOTTOMRIGHT = "br"
    TOP = "t"
    BOTTOM = "b"
    LEFT = "l"
    RIGHT = "r"
    CENTER = "c"


class LocateByParent:
    """Mixin for positioning StaticText relative to parent window."""
    
    _align: TextAlign
    
    def __init__(
        self,
        parent: Any,
        label: str = ...,
        align: Union[TextAlign, str] = ...,
        **kwds: Any
    ) -> None: ...
    
    @property
    def align(self) -> TextAlign: ...
    
    @align.setter
    def align(self, align: Union[TextAlign, str]) -> None: ...
    
    def SetText(self, label: str) -> None:
        """Set the text label and update its position."""
        ...
    
    def update_location(self, align: Union[TextAlign, str]) -> None:
        """Update the location of the text based on alignment."""
        ...