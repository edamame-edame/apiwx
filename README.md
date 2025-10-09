

# apiwx

**apiwx** is a modern, user-friendly wrapper for wxPython that makes GUI development easier and more intuitive. It provides simplified APIs, automatic component management, powerful **mixin system**, comprehensive message boxes, **integrated type stubs**, and comprehensive Python version compatibility testing.

## 🎉 What's New in v0.5.2

- **🔄 Terminology Standardization**: Complete migration from "generics" to "mixins" terminology
- **📚 Industry Alignment**: Now uses standard Python mixin conventions
- **🔧 Zero Breaking Changes**: All existing code continues to work unchanged
- **🎯 Enhanced Documentation**: Clearer examples and better developer experience
- **🏗️ Improved Type Support**: Comprehensive type stubs with VSCode integration

## Quick Start

### Installation

```bash
pip install apiwx
```

The installation automatically includes complete type stubs for full IDE support - no additional packages needed!

### Requirements

- Python 3.11 or higher (recommended)
- Python 3.12+ fully supported and tested
- wxPython 4.2.0 or higher (automatically installed with apiwx)

> **Note**: apiwx uses modern Python type annotations and union operators that require Python 3.11+ for full compatibility. Python 3.10 is not currently supported due to advanced type annotation features used throughout the codebase.

### Your First App

```python
import apiwx

# Create a simple app with just a few lines
app = apiwx.WrappedApp("My First App")
window = apiwx.WrappedWindow(app, title="Hello World", size=(400, 300))
panel = apiwx.WrappedPanel(window)
button = apiwx.WrappedButton(panel, label="Click Me!", pos=(150, 100))

# Add button functionality
def on_click(event):
    apiwx.show_info("Hello from apiwx!")

button.slots_on_click += on_click

app.mainloop()
```

## Key Features

### 🚀 **Integrated Type Stubs (New in v0.5.1)**
apiwx now includes **built-in type stubs** that are automatically installed:

- **Zero Configuration**: Type stubs included in main package - no separate installation needed
- **Universal VSCode Support**: "Go to Definition" (F12) shows clean type stubs across all environments
- **PEP 561 Compliance**: Full compatibility with mypy, pylance, pyright, and other type checkers
- **Complete Coverage**: 21 comprehensive type stub files covering all modules and mixins
- **Intelligent Class Definitions**: Real instantiable classes for mixin aliases with full parameter support

```python
# Full type support out of the box
app: apiwx.AppBase = apiwx.AppBase("MyApp")
window: apiwx.WindowWithPanel = apiwx.WindowWithPanel(app, title="Demo")
panel: apiwx.PanelWithBoarder = apiwx.PanelWithBoarder(
    window,
    boarder_color="#FF0000",    # <- Auto-completed with type hints
    boarder_thickness=2,        # <- Type checked
    boarder_offset=5            # <- Full IntelliSense support
)
```

### Professional IDE Support
Enhanced development experience with comprehensive type information:

- **Superior IntelliSense**: Advanced autocompletion and parameter hints
- **Go to Definition**: F12 shows clean type declarations instead of implementation
- **Enhanced Type Safety**: Static analysis and error detection with proper mixin support
- **Mixin System**: Advanced metaclass-based mixins with full type introspection

### Simplified GUI Components
No more complex wxPython constructors - just simple, intuitive classes:

```python
# Before (raw wxPython)
frame = wx.Frame(None, wx.ID_ANY, "Title", size=(800, 600))
panel = wx.Panel(frame)
button = wx.Button(panel, wx.ID_ANY, "Click", pos=(10, 10), size=(100, 30))

# After (apiwx)
app = apiwx.WrappedApp("MyApp")
frame = apiwx.WrappedWindow(app, title="Title", size=(800, 600))
panel = apiwx.WrappedPanel(frame)
button = apiwx.WrappedButton(panel, label="Click", pos=(10, 10), size=(100, 30))
```

### Easy Event Handling
Connect events with simple syntax:

```python
button = apiwx.WrappedButton(panel, label="Save")

def save_file(event):
    # Your save logic here
    apiwx.show_info("File saved successfully!")

# Easy event connection with slots
button.slots_on_click += save_file

# Or use the connect method
button.connect(apiwx.EVT_BUTTON, save_file)

# Enable/disable controls easily
button.enable()   # New in v0.3.2
button.disable()  # New in v0.3.2
```

### Built-in Message Boxes
Show messages and get user input with one line:

```python
# Simple messages
apiwx.show_info("Operation completed!")
apiwx.show_warning("Please check your input.")
apiwx.show_error("Something went wrong.")

# Get user input
name = apiwx.get_text_input("What's your name?", "User Input")
if name:
    apiwx.show_info(f"Hello, {name}!")

# Ask questions
if apiwx.ask_question("Do you want to save changes?"):
    save_changes()
```

### Smart Button Behaviors with Mixin System
Add advanced behaviors with the powerful mixin system:

```python
# Button that disables itself after clicking (prevents double-clicks)
button = apiwx.WrappedButton[apiwx.SingleClickDisable](
    panel, label="Submit", disable_duration=2.0, auto_re_enable=True
)

# Button that requires double-click for confirmation
delete_btn = apiwx.WrappedButton[apiwx.DoubleClickOnly](
    panel, label="Delete", double_click_timeout=0.5
)

# Button with click confirmation guard
confirm_btn = apiwx.WrappedButton[apiwx.ClickGuard](
    panel, label="Delete All", guard_message="Click again to confirm"
)

# Check what mixins are applied (New in v0.3.2, updated in v0.5.2)
from apiwx.mixins_core import MixinsType
if MixinsType.hasmixins(type(button), apiwx.SingleClickDisable):
    print("Button has single-click disable behavior")
```

### Advanced Component Detection
Automatic component detection and management:

```python
# App with automatic window detection
app = apiwx.WrappedApp[apiwx.Singleton, apiwx.DetectWindow]("MyApp")

# Window with automatic panel detection and sizing
window = apiwx.WrappedWindow[apiwx.DetectPanel, apiwx.ByPanelSize](
    app, title="Smart Window"
)

# Panel with automatic child detection
panel = apiwx.WrappedPanel[apiwx.DetectChildren](window)

# Window with panel transition support (New alias in v0.3.2)
transit_window = apiwx.WindowSizeTransitWithPanel(app, title="Transition Window")
```

### Enhanced Type Support with Mixin System
apiwx v0.5.2 includes a completely redesigned mixin system with full type support:

```python
# Full type hints and IDE support with working mixins
from apiwx import WrappedApp, WrappedWindow, WrappedButton, Singleton
from typing import Optional

# Singleton app with type safety
app: WrappedApp = WrappedApp[Singleton]("TypedApp")
window: WrappedWindow = WrappedWindow(app, title="Typed Window")

# Enhanced button with type checking and mixin introspection
button: WrappedButton = WrappedButton[apiwx.SingleClickDisable](
    parent=window,
    label="Click Me",
    size=(120, 40),
    pos=(10, 10),
    disable_duration=3.0
)

# Check applied mixins at runtime (Redesigned in v0.5.2)
if button.hasmixins(apiwx.SingleClickDisable):
    print("Single-click disable behavior is active")

# Get all mixins classes
mixins_list = button.__mixin_classes__
print(f"Applied mixins: {mixins_list}")
```

## Available Components

### Core GUI Components
- **WrappedApp** - Application container
- **WrappedWindow** - Main windows and frames
- **WrappedPanel** - Container panels
- **WrappedButton** - Clickable buttons
- **WrappedStaticText** - Text labels
- **WrappedTextBox** - Text input fields
- **WrappedCheckBox** - Checkboxes
- **WrappedListBox** - List selections
- **WrappedComboBox** - Dropdown selections
- **WrappedSlider** - Value sliders
- **And many more...**

### Event System (Enhanced in v0.5.2)
- **Slots** - Event handling system for connecting callbacks and managing event slots

### Mixin System (Redesigned in v0.5.2)
Add advanced behaviors to components with the comprehensive mixin system:

#### Base Patterns
- **Singleton/Multiton** - Instance management patterns (using standardized mixins)
- **AutoDetect** - Automatic component detection and management
- **FixSize** - Fixed sizing behavior

#### Button Mixins  
- **SingleClickDisable** - Prevent double-clicking with auto re-enable
- **DoubleClickOnly** - Require double-click confirmation
- **ClickGuard** - Click confirmation prompts with customizable messages

#### Window & Panel Mixins
- **DetectPanel** - Automatic panel detection in windows
- **DetectChildren** - Child component detection in panels
- **WithBoarder** - Automatic border management
- **ByPanelSize** - Automatic window sizing based on panel content
- **SupportTransit** - Panel transition support
- **NotTransition** - Exclude panels from transition management

#### App Mixins
- **DetectWindow** - Automatic window detection in applications

#### Mixin Aliases (Enhanced in v0.5.2)
Convenient pre-built classes that combine common mixin behaviors:

**Application Classes:**
- **AppBase** - `WrappedApp[Singleton]` - Single instance applications
- **AppDetectWindow** - `WrappedApp[Singleton, DetectWindow]` - With automatic window detection

**Window Classes:**
- **WindowWithPanel** - `WrappedWindow[DetectPanel]` - Auto-detects child panels
- **WindowByPanelSize** - `WrappedWindow[DetectPanel, ByPanelSize]` - Sizes by panel content
- **WindowPanelTransit** - `WrappedWindow[SupportTransit]` - Panel transition support
- **WindowSizeTransitWithPanel** - `WrappedWindow[SupportTransit, ByPanelSize]` - Combined features

**Panel Classes:**
- **PanelDetectChildren** - `WrappedPanel[DetectChildren]` - Auto-detects child components  
- **PanelWithBoarder** - `WrappedPanel[WithBoarder]` - Built-in border drawing
- **PanelNoTransition** - `WrappedPanel[NotTransition]` - Excluded from transitions

**Button Classes:**
- **ButtonSingleClickDisable** - `WrappedButton[SingleClickDisable]` - Prevents double-clicks
- **ButtonDoubleClickOnly** - `WrappedButton[DoubleClickOnly]` - Requires double-click
- **ButtonClickGuard** - `WrappedButton[ClickGuard]` - Click confirmation protection

```python
# Easy instantiation with full type support
app = apiwx.AppBase("MyApp")
window = apiwx.WindowWithPanel(app, title="Demo") 
panel = apiwx.PanelWithBoarder(
    window,
    boarder_color="#FF0000",     # Fully typed parameters
    boarder_thickness=2,         # IntelliSense support
    boarder_offset=5             # Auto-completion
)
button = apiwx.ButtonClickGuard(
    panel,
    label="Delete",
    require_double_click=True,   # Typed mixin parameters
    guard_message="Click again to confirm"
)
```

### Message Boxes & Dialogs
- **show_info()** - Information messages
- **show_warning()** - Warning messages
- **show_error()** - Error messages
- **ask_question()** - Yes/No questions
- **get_text_input()** - Text input dialog
- **get_number_input()** - Numeric input dialog
- **get_choice_input()** - Selection dialog

### Advanced Features
- **Enhanced Mixin System** - Add behaviors to components with proper introspection
- **Robust Logging System** - Built-in debug logging with multiple levels
- **Font Management** - Easy font handling and management
- **Color Constants** - Predefined color palette and utilities
- **Panel Transition Management** - Multi-panel visibility control with transitions
- **Type Introspection** - Runtime mixin detection with `hasmixins()` method
- **Convenient UI Controls** - `enable()` and `disable()` methods for all components

## Common Patterns

### Creating a Simple Form

```python
import apiwx

app = apiwx.WrappedApp("Form Example")
window = apiwx.WrappedWindow(app, title="User Form", size=(400, 300))
panel = apiwx.WrappedPanel(window)

# Form elements
name_label = apiwx.WrappedStaticText(panel, text="Name:", pos=(20, 20))
name_input = apiwx.WrappedTextBox(panel, pos=(80, 20), size=(200, 25))

email_label = apiwx.WrappedStaticText(panel, text="Email:", pos=(20, 60))
email_input = apiwx.WrappedTextBox(panel, pos=(80, 60), size=(200, 25))

submit_button = apiwx.WrappedButton(panel, label="Submit", pos=(150, 120))

def submit_form(event):
    name = name_input.text
    email = email_input.text
    
    if not name or not email:
        apiwx.show_warning("Please fill in all fields.")
        return
    
    apiwx.show_info(f"Form submitted!\nName: {name}\nEmail: {email}")

submit_button.slots_on_click += submit_form

app.mainloop()
```

### Working with Enhanced Type Declarations and Mixins

```python
import apiwx
from typing import Optional

# Type-aware development with working mixins
app: apiwx.WrappedApp = apiwx.WrappedApp[apiwx.Singleton]("MyApp")
window: apiwx.WrappedWindow = apiwx.WrappedWindow[apiwx.DetectPanel](app, title="Type Demo")

# IDE provides full IntelliSense and error checking
def create_smart_button(parent: apiwx.WrappedPanel, 
                       label: str,
                       callback: Optional[callable] = None) -> apiwx.WrappedButton:
    # Button with single-click disable behavior
    button = apiwx.WrappedButton[apiwx.SingleClickDisable](
        parent, label=label, pos=(10, 10), disable_duration=2.0
    )
    
    if callback:
        button.slots_on_click += callback
    
    # Check mixins at runtime (Redesigned in v0.5.2)
    if button.hasmixins(apiwx.SingleClickDisable):
        print(f"Button '{label}' has single-click disable protection")
    
    return button

# Use convenience methods (New in v0.3.2)
def toggle_button_state(button: apiwx.WrappedButton):
    if button.is_enabled():
        button.disable()
    else:
        button.enable()
```

### Using Enhanced Mixins for Advanced Functionality

```python
import apiwx

app = apiwx.WrappedApp[apiwx.Singleton]("Mixins Demo")
window = apiwx.WrappedWindow[apiwx.DetectPanel]("Advanced Buttons")
panel = apiwx.WrappedPanel[apiwx.DetectChildren](window)

# Button that disables after click to prevent double-submission
submit_btn = apiwx.WrappedButton[apiwx.SingleClickDisable](
    panel, 
    label="Submit Form", 
    pos=(10, 10),
    disable_duration=3.0,
    auto_re_enable=True
)

# Button requiring double-click for dangerous operations
delete_btn = apiwx.WrappedButton[apiwx.DoubleClickOnly](
    panel, 
    label="Delete All", 
    pos=(10, 50),
    double_click_timeout=0.5
)

# Button with confirmation guard
reset_btn = apiwx.WrappedButton[apiwx.ClickGuard](
    panel, 
    label="Reset Data", 
    pos=(10, 90),
    guard_message="Click again to confirm reset"
)

# Runtime mixin introspection (Redesigned in v0.5.2)
def check_button_behaviors():
    buttons = [submit_btn, delete_btn, reset_btn]
    
    for btn in buttons:
        print(f"Button '{btn.text}' mixins:")
        if btn.hasmixins(apiwx.SingleClickDisable):
            print("  - Has single-click disable")
        if btn.hasmixins(apiwx.DoubleClickOnly):
            print("  - Requires double-click")
        if btn.hasmixins(apiwx.ClickGuard):
            print("  - Has click guard")

# Window with panel transition support (New in v0.3.2)
transit_window = apiwx.WindowSizeTransitWithPanel(
    app, title="Transition Demo", size=(400, 300)
)

app.mainloop()
```

### Progress Dialog for Long Operations

```python
import apiwx
import time

def long_operation():
    progress = apiwx.ProgressMessageBox("Processing", "Please wait...", maximum=100)
    
    for i in range(100):
        time.sleep(0.05)  # Simulate work
        progress.update(i + 1, f"Processing item {i + 1}/100")
        if progress.was_cancelled():
            break
    
    progress.close()
    apiwx.show_info("Operation completed!")

# Call this from a button click or menu
```

### Using Colors and Styles

```python
import apiwx

app = apiwx.WrappedApp("Styled App")
window = apiwx.WrappedWindow(app, title="Colors Demo", size=(400, 300))
panel = apiwx.WrappedPanel(window)

# Using built-in colors
panel.color_background = apiwx.Colour.LIGHT_GREY
title = apiwx.WrappedStaticText(panel, text="Welcome!", pos=(150, 50))
title.color_text = apiwx.Colour.DARK_BLUE

# Styled button
button = apiwx.WrappedButton(panel, label="Colorful Button", pos=(130, 100))
button.color_background = apiwx.Colour.LIGHT_GREEN

app.mainloop()
```

## Learning More

### Type Declaration Benefits

apiwx v0.5.2 includes comprehensive type stubs with redesigned mixin system:

- **Perfect IDE Integration**: Go to Definition (F12) shows clean type interfaces
- **Enhanced Development Speed**: Superior autocompletion and parameter hints  
- **Advanced Error Prevention**: Static type checking with mixin support
- **Runtime Introspection**: Working `hasmixins()` method for runtime type checking
- **Living Documentation**: Type signatures serve as built-in API documentation

### Module Organization

- **`core.py`** - Main wrapper classes with enhanced UI controls (`enable()`, `disable()`)
- **`message.py`** - Message boxes and dialogs with comprehensive options
- **`mixins_*.py`** - Mixin behaviors for different component types (fixed system)
- **`mixins_core.py`** - Core mixins system with working `hasmixins()` method
- **`mixins_alias.py`** - Convenient aliases like `WindowSizeTransitWithPanel`
- **`debug.py`** - Advanced logging and debugging utilities
- **`colors.py`** - Color constants and utilities
- **`fontmanager.py`** - Font management system
- **`paneltransmodel.py`** - Panel transition management (updated with `hasmixins` calls)
- **`stubs/`** - Type declaration files (.pyi) for superior IDE support

### Documentation
- Each module contains detailed docstrings
- Use Python's `help()` function for detailed information:
  ```python
  import apiwx
  help(apiwx.WrappedButton)
  help(apiwx.show_info)
  ```

## Why Choose apiwx?

- **Beginner-Friendly** - Simplified API that's easy to learn
- **Highly Productive** - Write less code, get more done with smart defaults
- **Professional Code Quality** - 100% PEP 8/257 compliant for enterprise standards (v0.5.0)
- **Robustly Type-Safe** - Comprehensive type declarations with working mixin system
- **Extremely Flexible** - Use simple wrappers or advanced mixin behaviors
- **Thoroughly Modern** - Contemporary Python patterns and superior IDE support
- **Rock-Solid Reliable** - Built on the mature wxPython framework with extensive testing
- **Desktop-Focused** - Designed specifically for desktop GUI applications
- **Runtime Introspection** - Full mixin support with `hasmixins()` method
- **Python 3.12 Ready** - Fully tested and optimized for the latest Python versions
- **Internationally Accessible** - Complete documentation available in multiple languages
- **Enterprise Ready** - Professional coding standards and comprehensive quality assurance

## Advanced Usage

For complex applications, explore:
- **Enhanced Mixin System** for component behavior customization with runtime introspection
- **Professional Type Declarations** for superior IDE support and development experience
- **Panel Transition Management** for multi-view applications with smooth transitions
- **Advanced Debug Logging** for development and troubleshooting with multiple log levels
- **Smart Font Management** for consistent typography across components
- **Rich Message Dialogs** for comprehensive user interaction and feedback
- **Component Introspection** using `hasmixins()` for runtime behavior detection
- **Convenient UI Controls** with `enable()` and `disable()` methods
- **Python 3.12 Features** including typing.override decorator and modern type syntax
- **Comprehensive Testing Framework** with 9-category test coverage for reliability assurance

## Examples

Check the project repository for complete examples and tutorials showing:
- Simple desktop applications with enhanced controls
- Form handling and validation with smart behaviors
- Multi-panel applications with transition management
- Advanced component behaviors using the redesigned mixin system
- Type-safe development patterns with runtime introspection
- Integration with other Python libraries
- Real-world usage of `hasmixins()` method for dynamic behavior detection
- Python 3.12 compatibility examples with modern language features
- Comprehensive testing patterns for GUI applications

### Compatibility and Testing

### Python Version Support
- **Python 3.11**: Full support (recommended baseline)
- **Python 3.12**: Fully tested and supported with comprehensive test suite
- **Python 3.13**: Ready for testing (compatibility framework in place)

### Code Quality Standards (New in v0.5.0)
apiwx v0.5.0 achieves the highest code quality standards:

- **PEP 8 Compliance**: 100% adherence to Python style guidelines
- **PEP 257 Compliance**: Complete docstring convention compliance
- **Line Length Standards**: All code follows 79-character limit
- **Consistent Formatting**: Uniform indentation and spacing throughout
- **Professional Documentation**: Enhanced docstrings with proper formatting
- **Type Safety**: Maintained full type annotation integrity during compliance updates

### Testing Framework
apiwx includes a comprehensive testing framework with 9 major test categories:

1. **Core Components Testing** - Basic GUI component functionality
2. **Mixin System Testing** - Advanced behavior system validation
3. **Message System Testing** - Dialog and notification functionality
4. **Event Handling Testing** - User interaction and event processing
5. **Type System Testing** - Type annotations and IDE support
6. **Import System Testing** - Module loading and dependency management
7. **UI Control Testing** - enable/disable and state management
8. **Panel Management Testing** - Multi-panel and transition systems
9. **Python Version Compatibility** - Version-specific feature testing

All tests maintain 100% pass rate across supported Python versions, ensuring reliable cross-version compatibility and professional code quality standards.

## Latest Updates

### Version 0.5.0 (Current) - October 8, 2025
- **CODE QUALITY EXCELLENCE**: Achieved 100% PEP 8 and PEP 257 compliance across all source files
- **COMPREHENSIVE PEP COMPLIANCE**: Fixed 25 PEP 8 violations (E501 line length) in 18 core modules
- **ENHANCED DOCUMENTATION**: Improved docstring quality and code readability throughout
- **FULL TESTING VERIFICATION**: All test suites pass with 100% success rate (11/11 comprehensive tests)
- **ROBUST FUNCTIONALITY**: Maintained complete functional compatibility while improving code quality
- **PROFESSIONAL STANDARDS**: Consistent coding style and documentation standards implementation
- **MODERN PYTHON PRACTICES**: Enhanced type annotations and coding patterns following latest PEP guidelines

### Version 0.4.0
- **PYTHON 3.12 SUPPORT**: Comprehensive testing and full compatibility with Python 3.12
- **EXTENSIVE TESTING**: Added comprehensive test suite covering all 9 major functionality areas
- **INTERNATIONALIZATION**: Added complete English documentation for international developers
- **COMPATIBILITY VERIFICATION**: All Python 3.12 specific features tested and confirmed working
- **ENHANCED RELIABILITY**: Rigorous testing framework ensures consistent behavior across Python versions
- **DOCUMENTATION EXPANSION**: Complete technical documentation in both Japanese and English
- **MODERN PYTHON FEATURES**: Support for Python 3.12's typing.override decorator and PEP 695 syntax

### Version 0.3.3
- **CRITICAL FIX**: Resolved `__init__.py` import structure and class name inconsistencies
- **IMPROVEMENT**: Enhanced error handling and module initialization
- **TESTING**: Added comprehensive compatibility testing framework
- **STABILITY**: Improved package reliability and installation process

### Version 0.3.2
- **CRITICAL REDESIGN**: Redesigned mixin system - `hasmixins()` method with improved architecture
- **CRITICAL FIX**: Fixed `__mixin_classes__` attribute being properly set during creation
- **ENHANCEMENT**: Added `enable()` and `disable()` convenience methods to all UI components
- **IMPROVEMENT**: Reorganized import structure for better reliability and error handling
- **NEW ALIAS**: Added `WindowSizeTransitWithPanel` for combined window behaviors
- **CLEANUP**: Removed deprecated `DetectButton` and cleaned up mixin aliases
- **TESTING**: Added comprehensive test suite with 100% pass rate
- **COMPATIBILITY**: Maintained full backward compatibility while fixing core issues

### Version 0.3.1
- Added comprehensive type declaration files (.pyi)
- Enhanced VS Code and IDE integration
- Improved "Go to Definition" functionality
- PEP 561 compliance for type checkers
- Better development experience with full IntelliSense support

## International Documentation

apiwx v0.4.0 includes comprehensive documentation in multiple languages:
- **Japanese**: Complete technical documentation and development notes
- **English**: Full translations for international developer community
- **Technical Memos**: Detailed compatibility notes and implementation guides
- **Quick Reference**: Rapid access guides for common development patterns

This ensures apiwx is accessible to developers worldwide, with complete technical documentation available in both Japanese and English.

## License

MIT License - free for both personal and commercial use.
