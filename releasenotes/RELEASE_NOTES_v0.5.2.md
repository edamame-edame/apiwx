# Release Notes - apiwx v0.5.2

**Release Date:** October 10, 2025  
**Version:** 0.5.2  
**Build Status:** ✅ Stable Release

## 🔄 Major Changes: Terminology Standardization

### Generics → Mixins Migration

apiwx v0.5.2 introduces a comprehensive terminology update from "generics" to "mixins" throughout the entire framework, aligning with industry standards and improving code clarity.

#### What Changed

**Core System Renaming:**
- `GenericsType` → `MixinsType` (metaclass)
- `BaseGenerics` → `BaseMixins` (base class for metaclass-replacing mixins)
- `hasgenerics()` → `hasmixins()` (method for checking applied mixins)
- `__generic_classes__` → `__mixin_classes__` (attribute storing applied mixins)

**Module Structure:**
- All `generics_*.py` modules now have `mixins_*.py` equivalents
- All `generics_*.pyi` type stubs now have `mixins_*.pyi` equivalents
- Updated imports and exports throughout the framework

**Documentation Updates:**
- README.md updated with mixin terminology
- All docstrings and comments updated
- Examples and usage patterns reflect new terminology

## ✨ Key Features

### 🎯 Backward Compatibility
- **Zero Breaking Changes**: All existing code continues to work unchanged
- Main API (`WrappedApp`, `WrappedWindow`, `Singleton`, etc.) remains identical
- Import statements unchanged for end users
- Type aliases (`AppBase`, `WindowWithPanel`, etc.) function identically

### 🔧 Enhanced Type Support
- **Comprehensive Type Stubs**: 21 `.pyi` files covering entire API surface
- **VSCode Integration**: Perfect "Go to Definition" support
- **PEP 561 Compliance**: Integrated type stubs for optimal IDE experience
- **Type Safety**: Full static type checking support

### 🏗️ Improved Architecture
- **Industry Standard Terms**: "Mixins" align with Python community conventions
- **Clearer Documentation**: More intuitive naming for new developers
- **Consistent API**: Unified terminology across all modules

## 📦 Technical Details

### Mixin System
The mixin system provides powerful composition patterns:

```python
# Singleton pattern
app = apiwx.AppBase('MyApp')  # Singleton application

# Multiple mixins
button = apiwx.WrappedButton[apiwx.SingleClickDisable, apiwx.ClickGuard](
    parent, label="Protected Button"
)

# Check applied mixins
from apiwx.mixins_core import MixinsType
has_singleton = MixinsType.hasmixins(type(app), apiwx.Singleton)
print(f"Has Singleton mixin: {has_singleton}")  # True

# Access mixin classes
print(f"Applied mixins: {app.__mixin_classes__}")
```

### Available Mixins

**Core Mixins:**
- `Singleton` - Ensures single instance per class
- `Multiton` - Manages multiple tracked instances
- `AutoDetect` - Automatic UI component detection
- `FixSize` - Prevents component resizing

**UI-Specific Mixins:**
- `SingleClickDisable` - Temporarily disables buttons after click
- `DoubleClickOnly` - Requires double-click activation
- `ClickGuard` - Advanced click protection
- `WithBoarder` - Adds border drawing to panels
- `ByPanelSize` - Window sizing based on client area

### Type Aliases
Convenient pre-configured combinations:

```python
# Application aliases
apiwx.AppBase                    # WrappedApp[Singleton]
apiwx.AppDetectWindow           # WrappedApp[Singleton, DetectWindow]

# Window aliases  
apiwx.WindowWithPanel          # WrappedWindow[DetectPanel]
apiwx.WindowByPanelSize        # WrappedWindow[ByPanelSize]

# Panel aliases
apiwx.PanelDetectChildren      # WrappedPanel[DetectChildren]
apiwx.PanelWithBoarder         # WrappedPanel[WithBoarder]

# Button aliases
apiwx.ButtonClickGuard         # WrappedButton[ClickGuard]
apiwx.ButtonSingleClickDisable # WrappedButton[SingleClickDisable]
```

## 🔧 Migration Guide

### For Library Users
**No action required** - all existing code continues to work without modification.

### For Contributors/Advanced Users
If you've been working with internal generics modules:

```python
# Old (still works)
from apiwx.generics_core import GenericsType
result = GenericsType.hasgenerics(cls, SomeMixin)

# New (recommended)
from apiwx.mixins_core import MixinsType  
result = MixinsType.hasmixins(cls, SomeMixin)
```

## 📊 Build Information

- **Wheel Size:** 101.5KB (`apiwx-0.5.2-py3-none-any.whl`)
- **Source Size:** 390.7KB (`apiwx-0.5.2.tar.gz`)
- **Python Support:** 3.11+
- **Dependencies:** wxPython 4.1.0+

## 🧪 Testing

- ✅ **Comprehensive Test Suite**: All existing tests pass
- ✅ **Mixin System Tests**: New test suite for mixin functionality
- ✅ **Backward Compatibility**: Verified zero breaking changes
- ✅ **Type Checking**: Full mypy compliance
- ✅ **IDE Integration**: VSCode "Go to Definition" tested

## 🔗 Installation

```bash
pip install apiwx==0.5.2
```

## 📝 What's Next

Future releases will focus on:
- Enhanced mixin patterns and utilities
- Additional UI component mixins
- Performance optimizations
- Extended documentation and examples

---

**Full Changelog:** All changes maintain backward compatibility while modernizing terminology and improving developer experience.

**Contributors:** This release represents a significant step toward making apiwx more accessible and aligned with Python community standards.