"""Test module for MutableListView functionality and improved mixins.

This module tests the new MutableListView component, the improved LocateByParent
mixin with better size calculations, and other enhanced mixin functionalities.
"""

import sys
import os

# Add the parent directory to the path to import apiwx
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

try:
    import apiwx
    from apiwx.mutablelistview import MutableListView, AbstractMutableListNode
    from apiwx.mixins_statictext import TextAlign, LocateByParent
    from apiwx import App, Window, Panel, StaticText
except ImportError as e:
    print(f"Import error: {e}")
    print("Please ensure apiwx is installed or run from the correct directory")
    sys.exit(1)


def test_abstract_mutable_list_node():
    """Test AbstractMutableListNode base functionality."""
    print("Testing AbstractMutableListNode...")
    
    app = apiwx.App("Node Test")
    window = apiwx.Window(app, title="Test Window", size=(400, 300))
    
    # Create a concrete implementation
    class TestNode(AbstractMutableListNode):
        def __init__(self, parent, value):
            super().__init__(parent)
            self.value = value
            
        def to_node(self):
            return self.value
            
        @classmethod
        def from_node(cls, parent, node):
            return cls(parent, node)
    
    # Test node creation and methods
    node1 = TestNode(window, "test_value_1")
    node2 = TestNode(window, "test_value_2")
    
    # Test to_node method
    assert node1.to_node() == "test_value_1", "to_node should return the node value"
    assert node2.to_node() == "test_value_2", "to_node should return the node value"
    
    # Test equality operator
    assert node1 == "test_value_1", "Node should equal its value"
    assert not (node1 == "test_value_2"), "Node should not equal different value"
    assert not (node1 == node2), "Different nodes should not be equal"
    
    # Test from_node class method
    node3 = TestNode.from_node(window, "test_value_3")
    assert node3.to_node() == "test_value_3", "from_node should create node with correct value"
    
    print("✅ AbstractMutableListNode test passed")


def test_mutable_list_view_basic():
    """Test basic MutableListView functionality."""
    print("Testing MutableListView basic functionality...")
    
    app = apiwx.App("ListView Test")
    window = apiwx.Window(app, title="ListView Test", size=(500, 400))
    
    # Create a simple node type
    class SimpleNode(AbstractMutableListNode):
        def __init__(self, parent, value):
            super().__init__(parent)
            self.value = value
            self.label = apiwx.StaticText(self, label=f"Item: {value}")
            
        def to_node(self):
            return self.value
            
        @classmethod
        def from_node(cls, parent, node):
            return cls(parent, node)
    
    # Create list view
    list_view = MutableListView(
        window,
        size=(300, 200),
        pos=(10, 10),
        node_view_type=SimpleNode
    )
    
    # Test initial state
    assert len(list_view.node_view_list) == 0, "List should be empty initially"
    assert list_view.node_view_type == SimpleNode, "Node type should be set correctly"
    
    # Test append
    list_view.append("item1")
    list_view.append("item2")
    list_view.append("item3")
    
    assert len(list_view.node_view_list) == 3, "List should have 3 items after appending"
    
    # Check that nodes are created correctly
    assert list_view.node_view_list[0].to_node() == "item1", "First item should be 'item1'"
    assert list_view.node_view_list[1].to_node() == "item2", "Second item should be 'item2'"
    assert list_view.node_view_list[2].to_node() == "item3", "Third item should be 'item3'"
    
    print("✅ MutableListView basic functionality test passed")


def test_mutable_list_view_remove():
    """Test MutableListView remove functionality."""
    print("Testing MutableListView remove functionality...")
    
    app = apiwx.App("ListView Remove Test")
    window = apiwx.Window(app, title="Remove Test", size=(500, 400))
    
    class RemoveTestNode(AbstractMutableListNode):
        def __init__(self, parent, value):
            super().__init__(parent)
            self.value = value
            
        def to_node(self):
            return self.value
            
        @classmethod
        def from_node(cls, parent, node):
            return cls(parent, node)
    
    # Create list view and add items
    list_view = MutableListView(
        window,
        size=(300, 200),
        pos=(10, 10),
        node_view_type=RemoveTestNode
    )
    
    # Add some items
    items = ["A", "B", "C", "D"]
    for item in items:
        list_view.append(item)
    
    assert len(list_view.node_view_list) == 4, "Should have 4 items initially"
    
    # Test remove
    list_view.remove("B")
    assert len(list_view.node_view_list) == 3, "Should have 3 items after removing one"
    
    # Check remaining items
    remaining_values = [node.to_node() for node in list_view.node_view_list]
    assert remaining_values == ["A", "C", "D"], "Should have correct remaining items"
    
    # Test remove non-existent item (should not crash)
    list_view.remove("X")
    assert len(list_view.node_view_list) == 3, "Length should remain the same"
    
    print("✅ MutableListView remove functionality test passed")


def test_mutable_list_view_scrolling():
    """Test MutableListView with scrolling."""
    print("Testing MutableListView scrolling functionality...")
    
    app = apiwx.App("Scroll Test")
    window = apiwx.Window(app, title="Scroll Test", size=(400, 300))
    
    class ScrollTestNode(AbstractMutableListNode):
        def __init__(self, parent, value):
            super().__init__(parent)
            self.value = value
            
        def to_node(self):
            return self.value
            
        @classmethod
        def from_node(cls, parent, node):
            return cls(parent, node)
    
    # Create vertical scrolling list view
    vlist_view = MutableListView(
        window,
        size=(150, 100),
        pos=(10, 10),
        node_view_type=ScrollTestNode,
        style=apiwx.styleflags.VSCROLL,
        scroll_rate=(5, 10)
    )
    
    # Create horizontal scrolling list view
    hlist_view = MutableListView(
        window,
        size=(150, 100),
        pos=(200, 10),
        node_view_type=ScrollTestNode,
        style=apiwx.styleflags.HSCROLL,
        scroll_rate=(10, 5)
    )
    
    # Add many items to test scrolling
    for i in range(20):
        vlist_view.append(f"V-Item-{i}")
        hlist_view.append(f"H-Item-{i}")
    
    assert len(vlist_view.node_view_list) == 20, "Vertical list should have 20 items"
    assert len(hlist_view.node_view_list) == 20, "Horizontal list should have 20 items"
    
    print("✅ MutableListView scrolling functionality test passed")


def test_improved_locate_by_parent():
    """Test improved LocateByParent with better size calculations."""
    print("Testing improved LocateByParent functionality...")
    
    app = apiwx.App("LocateByParent Test")
    window = apiwx.Window(app, title="Alignment Test", size=(400, 300))
    
    class ImprovedAlignedText(apiwx.StaticText[LocateByParent]):
        pass
    
    # Test text with proper initialization
    center_text = ImprovedAlignedText(window, label="Center Text", align="c")
    
    # Verify the text property is set correctly
    assert hasattr(center_text, 'text'), "Text should have text property"
    assert center_text.align == TextAlign.CENTER, "Alignment should be CENTER"
    
    # Test SetText method (improved size calculation)
    center_text.SetLabel("Updated Text")  # Use SetLabel instead of SetText
    assert center_text.align == TextAlign.CENTER, "Alignment should remain CENTER after text update"
    
    # Test different alignments with text updates
    alignments_to_test = [
        ("tl", TextAlign.TOPLEFT),
        ("tr", TextAlign.TOPRIGHT), 
        ("bl", TextAlign.BOTTOMLEFT),
        ("br", TextAlign.BOTTOMRIGHT),
        ("t", TextAlign.TOP),
        ("b", TextAlign.BOTTOM),
        ("l", TextAlign.LEFT),
        ("r", TextAlign.RIGHT),
        ("c", TextAlign.CENTER)
    ]
    
    for align_str, align_enum in alignments_to_test:
        test_text = ImprovedAlignedText(window, label=f"{align_str} text", align=align_str)
        assert test_text.align == align_enum, f"Alignment should be {align_enum}"
        
        # Test text update with alignment
        test_text.SetLabel(f"Updated {align_str}")  # Use SetLabel instead of SetText
        assert test_text.align == align_enum, f"Alignment should remain {align_enum} after text update"
    
    print("✅ Improved LocateByParent test passed")


def test_mixin_integration():
    """Test integration between new features and existing mixins."""
    print("Testing mixin integration...")
    
    app = apiwx.App("Integration Test")
    window = apiwx.Window(app, title="Integration Test", size=(600, 500))
    
    # Create a node type that uses aligned text
    class AlignedTextNode(AbstractMutableListNode):
        def __init__(self, parent, value):
            super().__init__(parent)
            self.value = value
            
            # Use improved LocateByParent mixin
            class NodeAlignedText(apiwx.StaticText[LocateByParent]):
                pass
            
            self.label = NodeAlignedText(self, label=f"Node: {value}", align="c")
            
        def to_node(self):
            return self.value
            
        @classmethod
        def from_node(cls, parent, node):
            return cls(parent, node)
    
    # Create list view with aligned text nodes
    list_view = MutableListView(
        window,
        size=(400, 300),
        pos=(100, 100),
        node_view_type=AlignedTextNode
    )
    
    # Add items
    for i in range(5):
        list_view.append(f"aligned_item_{i}")
    
    assert len(list_view.node_view_list) == 5, "Should have 5 aligned text nodes"
    
    # Verify that each node has properly aligned text
    for node in list_view.node_view_list:
        assert hasattr(node, 'label'), "Each node should have a label"
        assert node.label.align == TextAlign.CENTER, "Each label should be center-aligned"
    
    print("✅ Mixin integration test passed")


def test_error_handling():
    """Test error handling in new components."""
    print("Testing error handling...")
    
    app = apiwx.App("Error Test")
    window = apiwx.Window(app, title="Error Test", size=(300, 200))
    
    # Test AbstractMutableListNode abstract methods
    try:
        node = AbstractMutableListNode(window)
        node.to_node()  # Should raise NotImplementedError
        print("❌ Should have raised NotImplementedError for to_node")
        return False
    except NotImplementedError:
        print("✅ to_node properly raises NotImplementedError")
    
    try:
        AbstractMutableListNode.from_node(window, "test")  # Should raise NotImplementedError
        print("❌ Should have raised NotImplementedError for from_node")
        return False
    except NotImplementedError:
        print("✅ from_node properly raises NotImplementedError")
    
    # Test invalid alignment in LocateByParent
    try:
        class TestAlignedText(apiwx.StaticText[LocateByParent]):
            pass
        
        invalid_text = TestAlignedText(window, label="Test", align="invalid")
        print("❌ Should have raised error for invalid alignment")
        return False
    except ValueError:
        print("✅ Invalid alignment properly raises ValueError")
    
    print("✅ Error handling test passed")
    return True


def run_all_tests():
    """Run all tests for MutableListView and improved mixins."""
    print("="*60)
    print("Running MutableListView and Improved Mixins Tests")
    print("="*60)
    
    try:
        test_abstract_mutable_list_node()
        test_mutable_list_view_basic()
        test_mutable_list_view_remove()
        test_mutable_list_view_scrolling()
        test_improved_locate_by_parent()
        test_mixin_integration()
        if not test_error_handling():
            return False
        
        print("="*60)
        print("🎉 ALL MUTABLELISTVIEW AND MIXINS TESTS PASSED!")
        print("="*60)
        return True
        
    except Exception as e:
        print(f"❌ Test failed with error: {e}")
        import traceback
        traceback.print_exc()
        return False


if __name__ == "__main__":
    success = run_all_tests()
    sys.exit(0 if success else 1)