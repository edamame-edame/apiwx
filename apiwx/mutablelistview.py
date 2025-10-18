"""Mutable List View Module
This module provides a `MutableListView` class that extends a scrollable
window to manage a dynamic list of child panels. Each child panel
represents a node in the list and is defined by a user-specified type
that incorporates the `Multiton` mixin for unique instance management.
The `MutableListView` allows for easy addition and removal of nodes,
as well as automatic layout management using a sizer.
It is designed to be used in wxPython applications for creating
dynamic list views with customizable node representations.
"""

import typing


try:
    from . import core
    from . import mixins_base
    from . import mixins_panel
    from . import framestyle
    from . import styleflags
    from . import constants

except ImportError:
    import core
    import mixins_base
    import mixins_panel
    import framestyle
    import styleflags
    import constants


class AbstractMutableListNode(core.Panel[mixins_base.Multiton]):
    """A panel representing a single node in a mutable list view.

    This class is designed to be used as a child panel within a
    MutableListView. It incorporates the Multiton mixin to ensure
    that each instance is unique based on its initialization parameters.

    Attributes:
        key: Unique identifier for the node instance.
    """

    def __eq__(self, value):
        if isinstance(value, AbstractMutableListNode):
            return super().__eq__(value)
        
        else:
            return value == self.to_node()


    def to_node(self):
        raise NotImplementedError(
            "to_node method must be implemented in subclasses."
        )
    
    @classmethod
    def from_node(cls, parent, node):
        raise NotImplementedError(
            "from_node method must be implemented in subclasses."
        )


class MutableListView(core.ScrolledWindow):
    node_view_type: type[AbstractMutableListNode]
    """Node view panel type (need Multiton mixin)"""


    def __init__(
            self,
            parent: core.Window | core.Panel,
            size: tuple[int, int] | None = None,
            pos: tuple[int, int] | None = None,
            color: tuple[int, int, int] | None = None,
            style: int = styleflags.VSCROLL,
            scroll_rate: tuple[int, int] = (5, 5),
            node_view_type: type[AbstractMutableListNode] =
                AbstractMutableListNode,
            **kwds):
        """Initialize the mutable list view.
        This panel automatically detects and manages child panels of a
        specified type, allowing dynamic addition and removal of items.
        Args:
            parent (Window | Panel): Parent window or panel.
            size (tuple[int, int] | None): Size of the panel.
            pos (tuple[int, int] | None): Position of the panel.
            color (tuple[int, int, int] | None): Background color.
            style (int | None): Style flags.
            node_view_type (type[Panel]): Type of child panels to manage.
            **kwds: Additional keyword arguments.
        """
        super().__init__(
            parent,
            size=size,
            pos=pos,
            color=color,
            style=style,
            **kwds
        )

        # Type of node panels to manage
        self.node_view_type = node_view_type

        # List of child panels
        self.node_view_list = []

        if style & styleflags.VSCROLL:
            # Sizer for managing layout
            self.sizer = core.BoxSizer(constants.VERTICAL)
        else:
            self.sizer = core.BoxSizer(constants.HORIZONTAL)

        self.SetSizer(self.sizer)

        self.scroll_rate = scroll_rate


    def append(self, node):
        """Append a new node panel to the list.

        Args:
            node (typing.Any): Node panel to append.
        """
        node_view = self.node_view_type.from_node(self, node)
        
        self.sizer.add(node_view, 0, core._wx.ALL, 5)

        self.node_view_list.append(
            node_view
        )

        self.layout()

        self.SetVirtualSize(
            self.sizer.GetMinSize()
        )


    def remove(self, node: AbstractMutableListNode):
        """Remove a node panel from the list.

        Args:
            node (typing.Any): Node panel to remove.
        """
        for node_view in self.node_view_list:
            if node_view.to_node() == node:
                self.node_view_list.remove(node_view)
                node_view.destroy()
                break

        self.layout()

        self.SetVirtualSize(
            self.sizer.GetMinSize()
        )


if __name__ == "__main__":
    import mixins_app, mixins_window

    class MyNode(AbstractMutableListNode):
        def __init__(self, parent, value):
            super().__init__(parent)
            self.value = value
            self.button = core.Button(
                self, label="Remove",
                size=(70, 30),
                pos=(0, 5)
            )
            self.textfield = core.StaticText(
                self, label=str(value),
                size=(parent.size[0] - 80, 30),
                pos=(80, 5)
            )

        def to_node(self):
            return self.value

        @classmethod
        def from_node(cls, parent, node):
            return cls(parent, value=node)
        
    
    class TestApp(core.App[mixins_app.DetectWindow]):
        def __init__(self):
            super().__init__("Test App")

        class TestWindow(core.Window[mixins_window.DetectPanel]):
            def __init__(self, parent):
                super().__init__(parent, title="Mutable List View Test", size=(400, 300))
                self.list_view = MutableListView(
                    self,
                    node_view_type=MyNode,
                    size=(300, 200),
                    pos=(50, 50),
                    color=(240, 240, 240)
                )

                for i in range(30):
                    self.list_view.append(i)

                self.Show()


    app = TestApp()

    app.mainloop()