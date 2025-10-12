# apiwx v0.5.6 Release Notes

**Release Date:** October 12, 2025  
**Version:** 0.5.6  
**Package Size:** Wheel: 112.0KB | Source: 1015.3KB

## 🎉 What's New in v0.5.6

### 📍 StaticText Positioning Mixins
We're excited to introduce a powerful new mixin system for intelligent text positioning! The new `mixins_statictext.py` module provides automatic text alignment capabilities within parent windows.

#### Key Features:

**🎯 Nine Alignment Options**
- Complete text alignment system with intuitive string shortcuts
- Support for all standard positions: top-left, center, bottom-right, etc.
- Enum-based (`TextAlign.CENTER`) and string-based (`"c"`) alignment specification

**🔄 Dynamic Positioning** 
- `LocateByParent` mixin automatically positions text within parent window boundaries
- Smart layout management with automatic repositioning on parent window resize
- Real-time alignment updates with simple property changes

**🎨 Flexible API**
- Both enum and string-based alignment specification for developer convenience
- Clean integration with existing apiwx mixin architecture
- Full type safety and IDE support

### 📦 New Components

#### TextAlign Enum
```python
class TextAlign(enum.Enum):
    TOP = "t"          # Top center
    TOPLEFT = "tl"     # Top left corner
    LEFT = "l"         # Middle left
    BOTTOMLEFT = "bl"  # Bottom left corner
    BOTTOM = "b"       # Bottom center
    BOTTOMRIGHT = "br" # Bottom right corner
    RIGHT = "r"        # Middle right
    TOPRIGHT = "tr"    # Top right corner
    CENTER = "c"       # Center of parent
```

#### LocateByParent Mixin
```python
class AlignedText(apiwx.WrappedStaticText[LocateByParent]):
    pass

# Create center-aligned text
center_text = AlignedText(window, label="Centered", align="c")

# Dynamic alignment changes
center_text.align = TextAlign.TOPRIGHT  # Move to top-right
center_text.align = "bl"                # Move to bottom-left
```

### 🚀 Usage Examples

#### Basic Text Positioning
```python
import apiwx
from apiwx.mixins_statictext import LocateByParent, TextAlign

app = apiwx.WrappedApp("Text Demo")
window = apiwx.WrappedWindow(app, title="Alignment Demo", size=(400, 300))

class AlignedText(apiwx.WrappedStaticText[LocateByParent]):
    pass

# Create aligned text components
title = AlignedText(window, label="Title", align=TextAlign.TOP)
subtitle = AlignedText(window, label="Subtitle", align="c")
footer = AlignedText(window, label="Footer", align="b")

app.mainloop()
```

#### Advanced Layout Management
```python
# Create multiple text elements with different alignments
class SmartWindow(apiwx.WrappedWindow):
    def __init__(self, app):
        super().__init__(app, title="Smart Layout", size=(500, 400))
        
        # Corner labels
        self.top_left = AlignedText(self, label="TL", align="tl")
        self.top_right = AlignedText(self, label="TR", align="tr") 
        self.bottom_left = AlignedText(self, label="BL", align="bl")
        self.bottom_right = AlignedText(self, label="BR", align="br")
        
        # Center content
        self.center_title = AlignedText(self, label="Center Title", align="c")
```

### 🔧 Technical Implementation

#### Enhanced Mixin System Integration
- Seamless integration with existing apiwx mixin architecture
- Full compatibility with other mixins (can combine with FixSize, etc.)
- Proper type hints and IDE support throughout

#### Smart Position Calculation
- Automatic X/Y coordinate calculation based on parent window size
- Intelligent text sizing considerations for accurate positioning
- Support for dynamic repositioning when parent window changes

#### Error Handling and Validation
- Comprehensive validation for alignment string inputs
- Clear error messages for invalid alignment specifications
- Graceful fallback handling for edge cases

### 🧪 Testing and Quality Assurance

#### Comprehensive Test Suite
- New test module: `test_statictext_mixins.py`
- Tests for all nine alignment positions
- Validation of enum and string-based alignment methods
- Error handling and edge case testing
- Integration testing with existing mixin system

#### Quality Metrics
- ✅ 100% test pass rate for all StaticText mixin functionality
- ✅ Full type safety with comprehensive type hints
- ✅ Complete documentation with usage examples
- ✅ Integration with existing apiwx export system

### 📚 Documentation Updates

#### README.md Enhancements
- New "Intelligent Text Positioning" section with comprehensive examples
- Updated mixin system documentation to include StaticText mixins
- Complete usage patterns and best practices
- Integration examples with other apiwx components

#### Code Documentation
- Complete module-level docstring for `mixins_statictext.py`
- Detailed class and method documentation
- Comprehensive examples in docstrings
- Type hints throughout for enhanced IDE support

### 🔄 Migration and Compatibility

#### Backward Compatibility
- ✅ 100% backward compatible with existing apiwx code
- ✅ No breaking changes to existing mixin systems
- ✅ Seamless integration with current apiwx patterns

#### New Exports
The following new components are now available in the main apiwx namespace:
- `TextAlign` - Enumeration for text alignment options
- `LocateByParent` - Mixin for automatic text positioning

```python
import apiwx

# New imports available
from apiwx import TextAlign, LocateByParent

# Or access through main namespace
alignment = apiwx.TextAlign.CENTER
```

### 🏗️ Development Experience

#### Enhanced IDE Support
- Full IntelliSense support for all new components
- Type-safe alignment specification with enum autocomplete
- Comprehensive parameter hints and documentation
- Real-time error detection for invalid alignments

#### Developer Productivity
- Rapid UI prototyping with pre-built alignment patterns
- Reduced boilerplate code for common text positioning tasks
- Intuitive API design following apiwx conventions
- Consistent naming patterns across all components

## 📋 Complete Feature Matrix

| Feature | v0.5.5 | v0.5.6 | Notes |
|---------|--------|--------|-------|
| Type Aliases | ✅ | ✅ | 12 convenient aliases |
| AutoDetect Indexor Search | ✅ | ✅ | Child component detection |
| Panel Transitions | ✅ | ✅ | Enhanced documentation |
| **StaticText Positioning** | ❌ | ✅ | **NEW: Nine alignment options** |
| **Dynamic Text Layout** | ❌ | ✅ | **NEW: Automatic repositioning** |
| **Flexible Alignment API** | ❌ | ✅ | **NEW: String and enum support** |

## 🔄 Upgrade Path

Upgrading from v0.5.5 to v0.5.6 is seamless and requires no code changes. Simply install the new version:

```bash
pip install --upgrade apiwx
```

To start using the new StaticText positioning features:

```python
# Import the new components
from apiwx.mixins_statictext import LocateByParent, TextAlign

# Create aligned text components
class AlignedText(apiwx.WrappedStaticText[LocateByParent]):
    pass

# Use with your existing code
text = AlignedText(parent, label="Hello", align="c")
```

## 🐛 Bug Fixes and Improvements

### Code Quality
- Enhanced error handling for text alignment validation
- Improved type hints throughout StaticText mixin system
- Better integration with existing mixin architecture

### Documentation
- Complete module documentation for new components
- Enhanced README with practical usage examples
- Improved inline code documentation and examples

### Testing
- Comprehensive test coverage for all new functionality
- Integration tests with existing mixin systems
- Edge case validation and error handling tests

## 🔮 Looking Forward

The addition of StaticText positioning mixins in v0.5.6 continues apiwx's mission of making wxPython development more intuitive and productive. This release establishes the foundation for future layout and positioning enhancements.

### Upcoming Features (Planned)
- Extended layout mixins for other UI components
- Advanced positioning algorithms for complex layouts
- Animation support for dynamic text positioning
- Integration with responsive design patterns

## 📞 Support and Community

- **Documentation:** Complete examples and usage patterns in README.md
- **Issues:** Report issues on GitHub with detailed reproduction steps
- **Testing:** Comprehensive test suite ensures reliability across Python versions
- **Compatibility:** Supports Python 3.11+ with full type safety

---

**Download apiwx v0.5.6:**
- Wheel: `apiwx-0.5.6-py3-none-any.whl` (112.0KB)
- Source: `apiwx-0.5.6.tar.gz` (1015.3KB)

**Happy coding with enhanced text positioning capabilities! 🎉**