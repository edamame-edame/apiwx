# apiwx-stubs

Type stubs for the [apiwx](https://github.com/edamame-edame/apiwx) library.

## Overview

This package provides type information for the apiwx library according to PEP 561. 
The apiwx library is a simplified, type-safe interface to wxPython with advanced 
features including generic type support and automatic component detection.

## Installation

```bash
pip install apiwx-stubs
```

This package is automatically recognized by type checkers like mypy, pylance, and pyright.

## Usage

Install both the runtime library and type stubs:

```bash
pip install apiwx apiwx-stubs
```

Type checking will work automatically:

```python
import apiwx

# Type checker will provide full type information
app = apiwx.AppBase("MyApp")
window = apiwx.WindowWithPanel(app, title="My Window")
```

## Features

- Complete type coverage for all apiwx modules
- Generic type support for advanced component combinations  
- PEP 561 compliant type stub distribution
- Compatible with mypy, pylance, pyright, and other type checkers

## Requirements

- Python 3.11+
- apiwx runtime library

## License

MIT License - same as the apiwx library.