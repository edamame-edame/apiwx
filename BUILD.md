# Build Automation for apiwx

This directory contains automated build scripts and configuration for the apiwx project.

## Files

- `build.json` - Main build configuration
- `build.py` - Automated build script
- `pyproject.toml` - Modern Python project configuration (optional)
- `Makefile` - Cross-platform build commands (optional)

## Quick Start

### 1. Basic Build (current version)
```bash
python build.py
```

### 2. Build with Version Update
```bash
python build.py --version 0.1.15
```

### 3. Build Options
```bash
# Skip tests during build
python build.py --version 0.1.15 --no-tests

# Skip cleaning previous builds
python build.py --version 0.1.15 --no-clean

# Use custom config file
python build.py --config custom-build.json
```

## Configuration (build.json)

### Project Settings
```json
{
  "project": {
    "name": "apiwx",
    "description": "wxPython API wrapper with advanced generics system",
    "author": "edamame",
    "license": "MIT"
  }
}
```

### Build Settings
```json
{
  "build": {
    "clean_before_build": true,     // Clean before building
    "create_wheel": true,           // Create .whl package
    "create_source": true,          // Create .tar.gz source
    "run_tests_before_build": true, // Run tests first
    "output_directory": "dist",     // Output folder
    "build_directory": "build"      // Build folder
  }
}
```

### Version Management
The script automatically updates version numbers in multiple files:
- `setup.cfg` - Package metadata
- `apiwx/__init__.py` - Module version and docstring

### Test Integration
```json
{
  "test": {
    "test_command": "python test/run_tests.py",
    "require_100_percent_success": true,
    "timeout_seconds": 60
  }
}
```

### Validation
The build process includes:
- ✅ File existence validation
- ✅ Version consistency checking
- ✅ Test suite execution (100% success required)
- ✅ Package import verification
- ✅ Build artifact validation

## Build Process

1. **Environment Validation** - Check required files exist
2. **Version Update** (if specified) - Update version in all files
3. **Test Execution** - Run full test suite
4. **Build Cleaning** - Remove previous build artifacts
5. **Package Building** - Create wheel and source distributions
6. **Post-Build Validation** - Verify packages and imports

## Output

The script creates:
- `dist/apiwx-{version}-py3-none-any.whl` - Installable wheel package
- `dist/apiwx-{version}.tar.gz` - Source distribution
- `build/` directory - Build artifacts

## Error Handling

- ❌ Stops on validation errors
- ❌ Stops on test failures (if 100% success required)
- ❌ Stops on build command failures
- ✅ Provides detailed error messages and logs

## Examples

### Release Build
```bash
# Complete release build with version update
python build.py --version 0.2.0
```

### Development Build
```bash
# Quick build without version change or tests
python build.py --no-tests --no-clean
```

### CI/CD Integration
```bash
# Automated build for continuous integration
python build.py --version $BUILD_VERSION
```

## Customization

Edit `build.json` to customize:
- Commands used for each build step
- Files to update with version numbers
- Test requirements and timeouts
- Build outputs and validation steps