# apiwx v0.1.16 Release Notes

## 📦 Release Summary
**Version:** 0.1.16  
**Release Date:** September 28, 2025  
**Total Test Modules:** 8  
**Test Success Rate:** 100%  
**Build Status:** ✅ Success

## 🆕 New Features

### 1. Enhanced Message Box System (`message.py`)
- **Complete Message Box Wrapper**: Info, Warning, Error, Question, Success messages
- **Custom Message Boxes**: Multiple button combinations with custom icons
- **Progress Dialogs**: Real-time progress updates for long operations
- **Input Dialogs**: Text, number, and choice input with validation
- **Convenience Functions**: One-line functions for quick usage

**Key Classes:**
- `MessageBox` - Core message box functionality
- `CustomMessageBox` - Advanced customization options
- `ProgressMessageBox` - Long-running operation support
- `InputDialog` - User input collection
- `MessageResult` / `MessageType` / `MessageButtons` - Enums for consistency

### 2. Advanced Button Generics (`generics_button.py`)
- **SingleClickDisable**: Auto-disable after click with timer re-enable
- **DoubleClickOnly**: Requires double-click for activation with timeout
- **ClickGuard**: Confirmation-style clicking with guard messages
- **DetectButton**: Auto-detection and generics application

**Features:**
- Threading-based timers for UI responsiveness
- Configurable timeouts and durations
- Visual feedback systems
- Event interception and handler management

### 3. Enhanced Debug/Logging System with Log Levels
- **LogLevel Enum**: DEBUG, INFO, WARNING, ERROR, CRITICAL levels
- **Level-based Filtering**: Runtime filtering based on minimum log level
- **Dynamic Level Adjustment**: Change log levels at runtime
- **Enhanced Log Format**: Includes level information in output
- **Convenience Functions**: Level-specific logging functions

**New Functions:**
- `uidebug_log()`, `uiinfo_log()`, `uiwarning_log()`, `uierror_log()`, `uicritical_log()`
- `uidebug_set_level()`, `uidebug_get_level()`
- Similar functions for internal logging
- Runtime parameter: `log_level=LEVEL` in command line arguments

## 🔧 Technical Improvements

### Test Infrastructure
- **8 Comprehensive Test Modules** covering all functionality
- **100% Success Rate** across all test scenarios
- **New Test Module**: `test_log_levels.py` for log level functionality
- **Integration Testing**: Cross-module functionality validation

### Documentation & Examples
- **Complete Demo Applications**:
  - `message_demo.py` - Interactive message box demonstration
  - `log_level_demo.py` - Log level functionality showcase
- **Updated README.md** with new feature documentation
- **Comprehensive Docstrings** with usage examples

### Build & Packaging
- **Automated Build System** with validation
- **Version Management** across multiple configuration files
- **Package Size Growth**: From 29.6KB (v0.1.15) to 44.9KB (v0.1.16)
- **Enhanced Export Management** for all new functions

## 📊 Test Results Summary

```
================================================================================
TEST SUMMARY
================================================================================
Total tests: 8
Passed: 8
Failed: 0
Success rate: 100.0%
Total time: 0.52s

Detailed Results:
  test_debug           [PASS] 0.09s - Basic debug functionality
  test_log_levels      [PASS] 0.38s - Enhanced log level features
  test_generics        [PASS] 0.00s - Core generics system
  test_metaclass       [PASS] 0.00s - Metaclass behavior
  test_gui             [PASS] 0.01s - GUI components
  test_button_generics [PASS] 0.01s - Button-specific generics
  test_message         [PASS] 0.00s - Message box functionality
  test_performance     [PASS] 0.03s - Performance benchmarks
```

## 🎯 Usage Examples

### Message Box System
```python
from apiwx.message import show_info, ask_question, get_text_input

# Simple messages
show_info("Operation completed successfully!")
show_warning("Please check your input.")
show_error("An error occurred.")

# Interactive dialogs
if ask_question("Do you want to save changes?"):
    save_changes()

user_name = get_text_input("Enter your name:", "User Input")
```

### Button Generics
```python
from apiwx import Button
from apiwx.generics_button import SingleClickDisable, DoubleClickOnly, ClickGuard

# Auto-disable button
button = Button[SingleClickDisable](
    panel, size=(120, 40), pos=(20, 20), 
    label="Click Me", disable_duration=2.0
)

# Double-click required button
button = Button[DoubleClickOnly](
    panel, size=(120, 40), pos=(20, 20),
    label="Double Click", double_click_timeout=0.5
)

# Confirmation button
button = Button[ClickGuard](
    panel, size=(120, 40), pos=(20, 20),
    label="Delete", guard_message="Click again to confirm"
)
```

### Enhanced Logging
```python
from apiwx.debug import LogLevel, uidebug_set_level, uiinfo_log, uierror_log

# Set log level to filter messages
uidebug_set_level(LogLevel.WARNING)  # Only WARNING and above

# Use level-specific logging
uiinfo_log("APP", "Application started")
uierror_log("APP", "Critical error occurred")

# Runtime arguments
# --ui_debug log_level=ERROR log_dir=./logs
```

## 🏗️ Architecture Highlights

### Modular Design
- **Separation of Concerns**: Each feature in dedicated modules
- **Consistent API**: Unified interface patterns across all features
- **Extensibility**: Easy addition of new generics and message types

### Performance Optimizations
- **Thread-safe Operations**: All background operations use proper threading
- **Efficient Filtering**: Log level filtering prevents unnecessary processing
- **Minimal Overhead**: Generics system adds minimal runtime cost

### Developer Experience
- **Rich Documentation**: Comprehensive examples and docstrings
- **Intuitive APIs**: Simple function calls for common operations
- **Flexible Configuration**: Runtime parameter customization
- **Comprehensive Testing**: High confidence in reliability

## 📈 Package Statistics

- **Lines of Code Added**: ~1,500+ lines across new modules
- **Test Coverage**: 100% success rate across 8 test modules
- **New Public APIs**: 25+ new functions and classes
- **Demo Applications**: 2 comprehensive examples
- **Documentation**: Complete usage examples and API docs

## 🔮 Future Compatibility

This release maintains full backward compatibility with existing code while adding powerful new features. All existing functionality continues to work unchanged, and new features integrate seamlessly with the existing generics system.

---

**Install:** `pip install apiwx==0.1.16`  
**Source:** Available as both wheel (.whl) and source distribution (.tar.gz)  
**Tested:** Python 3.13, wxPython 4.2+, Windows 11  
**License:** MIT