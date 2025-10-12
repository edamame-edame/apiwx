# Release Notes - apiwx v0.5.7

## Release Date
December 2024

## 🎉 What's New in v0.5.7

### 📋 MutableListView Component
- **New Dynamic List Management System**: Added `MutableListView` class for creating scrollable, dynamic list interfaces with panel-based UI components
- **AbstractMutableListNode Base Class**: Abstract base class with Multiton mixin support for creating custom list item components
- **Flexible Node Operations**: Easy append/remove operations with automatic panel layout and refresh
- **Scrolling Support**: Full horizontal and vertical scrolling with customizable scroll rates and styling options

### 🔧 Enhanced LocateByParent Mixin
- **Improved Size Calculation**: Fixed sizing issues in text positioning with better size handling
- **SetText Method Enhancement**: Automatic text repositioning when updating text content
- **Better Integration**: Improved compatibility with core text components and layout management

### 💡 Enhanced IDE Support
- **Better Type Hints**: Enhanced type annotations and overload definitions across the mixin system
- **Improved Development Experience**: Better IntelliSense support for mixin parameters and method signatures
- **Enhanced Typing**: Added `typing.overload` imports and improved type safety throughout the system

### 🎯 New Features Detail

#### MutableListView Usage
```python
from apiwx import MutableListView, AbstractMutableListNode

# Create custom node type
class TaskNode(AbstractMutableListNode):
    def __init__(self, parent, task_data):
        super().__init__(parent)
        self.task_data = task_data
        # Add UI components...
        
    def to_node(self):
        return self.task_data
        
    @classmethod
    def from_node(cls, parent, task_data):
        return cls(parent, task_data)

# Create scrollable list view
task_list = MutableListView(
    window,
    size=(450, 300),
    node_view_type=TaskNode,
    style=apiwx.styleflags.VSCROLL
)

# Add/remove items dynamically
task_list.append({"name": "New Task", "completed": False})
task_list.remove(completed_task)
```

#### Enhanced LocateByParent
```python
# Improved text positioning with automatic updates
class AlignedText(apiwx.WrappedStaticText[LocateByParent]):
    pass

text = AlignedText(window, label="Initial Text", align="c")
text.SetText("Updated Text")  # Automatically repositions
```

## 🔧 Technical Improvements

### API Enhancements
- **Abstract Method Consistency**: Fixed `from_node` classmethod signature in `AbstractMutableListNode`
- **Type Safety**: Enhanced type checking and validation throughout the mutable list system
- **Error Handling**: Improved error messages and validation for invalid inputs

### Documentation Updates
- **Comprehensive Examples**: Added detailed MutableListView examples to README.md
- **Type Stub Updates**: Complete type stubs for new components with proper inheritance
- **API Documentation**: Enhanced docstrings with usage patterns and parameter descriptions

### Integration Improvements
- **Package Exports**: Added `MutableListView` and `AbstractMutableListNode` to main package exports
- **Stub Integration**: Full type stub support for improved IDE experience
- **Mixin Compatibility**: Enhanced integration between new components and existing mixin system

## 📦 Package Information

### New Exports
- `MutableListView`: Dynamic scrollable list component
- `AbstractMutableListNode`: Base class for list item components

### Updated Modules
- `mutablelistview.py`: New module with list management components
- `mixins_statictext.py`: Enhanced LocateByParent with better size calculations
- `mixins_alias.py`: Improved type hints and IDE support
- `constants.py`: Enhanced alignment constants with type safety

## 🧪 Testing

### Comprehensive Test Suite
- **MutableListView Tests**: Complete test coverage for list operations and scrolling
- **LocateByParent Tests**: Validation of improved positioning and text updates
- **Integration Tests**: Mixin compatibility and error handling verification
- **Type Safety Tests**: Validation of enhanced type checking

### Test Results
- ✅ All tests passing on Python 3.13
- ✅ Complete functionality verification
- ✅ Error handling validation
- ✅ Type safety confirmation

## 🔄 Migration Guide

### For Existing Users
- **No Breaking Changes**: All existing functionality remains compatible
- **Optional Features**: New MutableListView components are additive
- **Enhanced Features**: LocateByParent improvements are backward compatible

### New Component Usage
```python
# Import new components
from apiwx import MutableListView, AbstractMutableListNode

# Create dynamic lists as shown in examples above
# No changes needed for existing code
```

## 🚀 Performance

### Optimizations
- **Efficient List Management**: Optimized panel layout and refresh operations
- **Memory Management**: Proper cleanup of removed list items
- **Scrolling Performance**: Smooth scrolling with configurable rates

## 🐛 Bug Fixes

### LocateByParent Issues
- **Fixed**: Size calculation problems in text positioning
- **Fixed**: Improved SetText method for proper repositioning
- **Enhanced**: Better integration with parent window resizing

### Type System Improvements
- **Fixed**: `from_node` method signature in AbstractMutableListNode
- **Enhanced**: Type safety across mixin system
- **Improved**: IDE support with better type hints

## 📈 Development Stats

- **New Files**: 3 (mutablelistview.py, test files, stubs)
- **Updated Files**: 6 (mixins, __init__.py, README.md, etc.)
- **New Classes**: 2 (MutableListView, AbstractMutableListNode)
- **New Methods**: 8+ (append, remove, SetText enhancements, etc.)
- **Test Cases**: 20+ comprehensive test scenarios

## 🔮 Future Roadmap

### Planned Enhancements
- **Advanced List Features**: Drag-and-drop reordering, filtering, sorting
- **Performance Optimizations**: Virtual scrolling for large lists
- **Enhanced Styling**: More customization options for list appearance
- **Additional Mixins**: More positioning and layout mixins

---

**Full Changelog**: [v0.5.6...v0.5.7](https://github.com/yuki-js/apiwx/compare/v0.5.6...v0.5.7)

**Documentation**: Updated README.md with comprehensive examples  
**Testing**: All tests passing, ready for production use  
**Compatibility**: Python 3.11+ (tested on 3.13)