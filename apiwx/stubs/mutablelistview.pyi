"""Type stubs for mutablelistview module."""

from typing import Any, Optional
from typing_extensions import Self
import wx

from .core import WrappedScrolledWindow
from .mixins_base import Multiton


class AbstractMutableListNode(Multiton):
    """Abstract base class for mutable list node components."""
    
    def __init__(self, parent: Any) -> None: ...
    
    def __eq__(self, value: Any) -> bool: ...
    
    def to_node(self) -> Any:
        """Convert this node to its underlying value."""
        ...
    
    @classmethod
    def from_node(cls, parent: Any, node: Any) -> Self:
        """Create a node instance from a value."""
        ...


class MutableListView(WrappedScrolledWindow):
    """A scrollable list view that manages mutable list nodes."""
    
    node_view_type: type[AbstractMutableListNode]
    node_view_list: list[AbstractMutableListNode]
    
    def __init__(
        self,
        parent: Any,
        size: tuple[int, int] = ...,
        pos: tuple[int, int] = ...,
        style: int = ...,
        node_view_type: type[AbstractMutableListNode] = ...,
        scroll_rate: tuple[int, int] = ...,
        **kwds: Any
    ) -> None: ...
    
    def append(self, node: Any) -> None:
        """Add a new node to the list."""
        ...
    
    def remove(self, node: Any) -> None:
        """Remove a node from the list."""
        ...