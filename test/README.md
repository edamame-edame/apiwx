# apiwx Test Suite

This directory contains comprehensive tests for the apiwx project, covering all major functionality including generics system, metaclasses, GUI components, and performance.

## Test Structure

### Test Files

- **`test_generics.py`** - Tests the core generics system functionality
  - Basic generics creation and usage
  - Inheritance and Method Resolution Order (MRO)
  - Namespace injection from generic parameters
  - Generic parameter validation

- **`test_metaclass.py`** - Tests metaclass functionality and BaseGenerics patterns
  - Singleton pattern implementation
  - Multiton pattern implementation  
  - Custom BaseGenerics patterns
  - Universal metaclass behavior

- **`test_gui.py`** - Tests GUI component functionality
  - Application creation and management
  - Window creation with various configurations
  - Panel creation and embedding
  - Component hierarchy and parent-child relationships

- **`test_debug.py`** - Tests the debug and logging system
  - Internal and UI logging functionality
  - Log categories and output
  - Debug system integration with other components

- **`test_performance.py`** - Performance and scalability tests
  - Generic class creation performance
  - Metaclass call performance
  - Memory usage patterns
  - Scalability with multiple parameters

- **`run_tests.py`** - Test runner for executing all tests

## Running Tests

### Run All Tests
```bash
# From the project root directory
python test/run_tests.py
```

### Run Specific Test Module
```bash
# Run a specific test category
python test/run_tests.py generics
python test/run_tests.py metaclass
python test/run_tests.py gui
python test/run_tests.py debug
python test/run_tests.py performance
```

### Run Individual Test Files
```bash
# Run tests directly
python test/test_generics.py
python test/test_metaclass.py
python test/test_gui.py
python test/test_debug.py
python test/test_performance.py
```

## Test Requirements

### Dependencies
- Python 3.13+
- wxPython 4.0+
- apiwx package (from parent directory)

### Environment Setup
Tests automatically add the parent directory to the Python path, so they can be run from the test directory without additional setup.

## Test Coverage

The test suite covers:

### ✅ Core Functionality
- Generic type system (`__getitem__` syntax)
- Dynamic class creation with `types.new_class()`
- Method Resolution Order (MRO) management
- Namespace injection and attribute resolution

### ✅ Metaclass System
- Custom metaclass generation (`GenericsType` → `CustomMeta`)
- BaseGenerics pattern integration
- Singleton and Multiton pattern implementations
- Universal safe super() replacement mechanism

### ✅ GUI Components
- wxPython wrapper class functionality
- Component hierarchy (App → Window → Panel → Controls)
- Generic parameter application to GUI classes

### ✅ Debug System
- Internal logging (`debug.internallog`)
- UI logging (`uilog`, `uilog_output_remaining`)
- Integration with metaclass operations
- Log category management

### ✅ Performance
- Generic class creation timing
- Metaclass instantiation performance
- Memory usage patterns
- Scalability with multiple generic parameters

## Expected Test Results

### Normal Execution
Most tests should pass without issues. Some expected behaviors:

- **GUI Tests**: May show warnings about missing GUI context (expected in headless environment)
- **Performance Tests**: Timing may vary based on system performance
- **Debug Tests**: Should generate log output in log files

### Known Limitations
- GUI component tests require wxPython to be properly installed
- Some tests create actual GUI objects but don't display them
- Performance benchmarks are relative and system-dependent

## Test Output Format

Tests use a consistent output format:
```
=== Test Category ===
Test description and steps...
✅ Test passed!
❌ Test failed: error message
```

## Continuous Integration

The test suite is designed to be CI-friendly:
- Exit codes: 0 for success, 1 for failure
- Clear pass/fail indicators
- Detailed error reporting
- Individual test isolation

## Contributing

When adding new features to apiwx:

1. Add corresponding tests to the appropriate test file
2. Update this README if new test categories are added
3. Ensure tests pass in both GUI and headless environments
4. Include performance considerations for new functionality

## Troubleshooting

### Common Issues

**ImportError: No module named 'apiwx'**
- Ensure you're running from the correct directory
- Check that the parent directory contains the apiwx package

**wxPython GUI Errors**
- Tests are designed to work in headless environments
- GUI errors in test environment are often expected

**Performance Test Failures**
- Performance thresholds may need adjustment based on system
- Focus on relative performance rather than absolute numbers