# Release Notes for apiwx v0.3.1

**Release Date:** October 1, 2025

## Summary

This release introduces comprehensive type declaration files (.pyi) to improve IDE support and developer experience. The primary focus is on enabling proper "Go to Definition" functionality in VS Code and other IDEs, where users will now see clean type declarations instead of implementation details.

## New Features

### Type Declaration Files (.pyi)
- Added comprehensive type stubs for all major modules
- Introduced dedicated `stubs/` directory structure within the apiwx package
- Created type declarations for:
  - Core wrapper classes (WrappedApp, WrappedWindow, WrappedPanel, etc.)
  - Generics system (AutoDetect, FixSize, Singleton, Multiton)
  - UI utilities (FontManager, Logger, Options)
  - Constants and enums (Colour, WindowStyle, BorderStyle, etc.)
  - Message box functionality
  - Debug and logging utilities

### PEP 561 Compliance
- Added `py.typed` marker files for proper type checker recognition
- Configured package distribution to include type declaration files
- Ensured compatibility with mypy, pyright, and other static type checkers

## Improvements

### Developer Experience
- **IDE Integration:** "Go to Definition" (F12) in VS Code now shows type declarations instead of implementation
- **IntelliSense:** Improved autocompletion and parameter hints
- **Type Safety:** Better static analysis and error detection during development
- **Documentation:** Type signatures provide clear API documentation

### Package Structure
- Organized type declarations separately from source code
- Maintained backward compatibility with existing imports
- Clean separation between implementation and interface definitions

## Technical Details

### File Structure Changes
```
apiwx/
├── stubs/           # New: Type declaration files
│   ├── __init__.pyi
│   ├── core.pyi
│   ├── generics_app.pyi
│   ├── generics_common.pyi
│   └── py.typed
├── py.typed         # PEP 561 marker file
└── [existing source files]
```

### Packaging Updates
- Updated `pyproject.toml` to include type declaration files in distribution
- Configured proper package data inclusion for `.pyi` files
- Maintained development mode installation compatibility

## Compatibility

- **Python Version:** Requires Python 3.13+
- **wxPython:** Compatible with wxPython 4.2.0+
- **Backward Compatibility:** All existing APIs remain unchanged
- **IDE Support:** Enhanced support for VS Code, PyCharm, and other Python IDEs

## Installation

```bash
pip install apiwx==0.3.1
```

For development installation:
```bash
pip install -e .
```

## Migration Notes

No code changes are required for existing users. The type declaration files are automatically included in the package and will be recognized by compatible IDEs and type checkers.

## Known Issues

None at this time.

## Credits

This release focuses on improving developer experience through better tooling integration and type safety enhancements.