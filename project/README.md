# Project Build Tools

This directory contains build-related tools for the apiwx project.

## File Structure

- `auto_build.py` - Main build automation script
- `build.json` - Build configuration file
- `build.bat` - Windows batch file
- `build_quick.py` - Interactive build helper

## Usage

### 1. Run from VS Code
Select from the Run and Debug panel (Ctrl+Shift+D):

- **Build Wheel Package** - Build wheel without tests
- **Build Wheel with Version** - Build with version specification
- **Build with Tests** - Build with test execution

### 2. Run from Command Line

```bash
# Basic build (without tests)
python project/auto_build.py --no-tests

# Build with version specification
python project/auto_build.py --version 0.1.18 --no-tests

# Build with tests
python project/auto_build.py

# Show help
python project/auto_build.py --help
```

### 3. Interactive Mode

```bash
python project/build_quick.py
```

Select build options from an interactive menu.

## Build Artifacts

- Wheel (.whl) and source distribution (.tar.gz) files are created in the `dist/` directory
- Type stub files (.pyi) are properly included

## Configuration

Customize build settings in `build.json`:

- Test execution toggle
- Build artifact types
- Version update target files
- Timeout settings, etc.