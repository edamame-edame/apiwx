"""Type stubs for apiwx.uiarg module.

This module provides type information for command line argument parsing
utilities specific to apiwx-based wxPython applications, including debug
flags, logging options, and other apiwx-specific command line parameters.
"""

from enum import Enum

class Options(Enum):
    """Available command line options for apiwx applications."""
    UI_DEBUG: str
    _INTERNAL_LOG: str

def exist_option(option: Options) -> bool:
    """Check if a specific option exists in the command line arguments.
    
    Args:
        option: The option to check for in sys.argv.
        
    Returns:
        True if the option is present in command line arguments, False otherwise.
    """
    ...

def get_option(option: Options) -> list[str]:
    """Extract option values and parameters from command line arguments.
    
    This function extracts all arguments that follow the specified option
    until another recognized option is encountered or the end of arguments
    is reached.
    
    Args:
        option: The option to extract values for.
        
    Returns:
        List of argument values for the specified option.
        Returns empty list if option is not found.
    """
    ...

def get_var(option_list: list[str], varname: str) -> str | None:
    """Parse variable assignments from option parameters.
    
    This function searches through a list of option parameters to find
    variable assignments in the format "varname=value" and returns the
    value portion.
    
    Args:
        option_list: List of option parameters to search through.
        varname: The variable name to look for (without the = sign).
        
    Returns:
        The value assigned to the variable if found, None if not found.
    """
    ...

__all__: list[str]