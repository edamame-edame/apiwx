"""Command line argument parser for apiwx applications.

This module provides utilities for parsing command line arguments specific
to apiwx-based wxPython applications. It handles debug flags, logging options,
and other apiwx-specific command line parameters.

The module defines available options through an enum and provides functions
to check for option existence, extract option values, and parse variable
assignments from the command line.

Functions:
    exist_option: Check if a specific option exists in command line
    get_option: Extract option values and parameters from command line
    get_var: Parse variable assignments from option parameters

Example:
    >>> if exist_option(Options.UI_DEBUG):
    ...     print("UI Debug mode enabled")
    >>> log_options = get_option(Options._INTERNAL_LOG)
    >>> log_level = get_var(log_options, "log_level")
"""
import sys
import enum


class Options(enum.Enum):
    """Available command line options for apiwx applications.
    
    This enum defines the supported command line options that can be
    used with apiwx applications for debugging and configuration.
    
    Attributes:
        UI_DEBUG: Enable UI debugging mode
        _INTERNAL_LOG: Enable internal logging with configurable parameters
    """
    UI_DEBUG = '--ui-debug'
    _INTERNAL_LOG = '--internal-log'


def exist_option(option: Options) -> bool:
    """Check if a specific option exists in the command line arguments.
    
    Args:
        option (Options): The option to check for in sys.argv.
        
    Returns:
        bool: True if the option is present in command line arguments,
              False otherwise.
              
    Example:
        >>> if exist_option(Options.UI_DEBUG):
        ...     print("Debug mode is enabled")
    """
    return option.value in sys.argv


def get_option(option: Options) -> list[str]:
    """Extract option values and parameters from command line arguments.
    
    This function extracts all arguments that follow the specified option
    until another recognized option is encountered or the end of arguments
    is reached.
    
    Args:
        option (Options): The option to extract values for.
        
    Returns:
        list[str]: List of argument values for the specified option.
                   Returns empty list if option is not found.
                   
    Example:
        >>> args = get_option(Options._INTERNAL_LOG)
        >>> # If command line was: --internal-log log_level=DEBUG verbose
        >>> # Returns: ['--internal-log', 'log_level=DEBUG', 'verbose']
    """
    if option.value not in sys.argv:
        return []
        
    option_list = sys.argv[
        sys.argv.index(option.value): len(sys.argv)
    ]

    for other in Options:
        if other.value in option_list:
            if other == option:
                continue
            
            option_list = (
                option_list[
                    0: option_list.index(
                        other.value
                    )
                ]
            )

    return option_list


def get_var(option_list: list[str], varname: str) -> str | None:
    """Parse variable assignments from option parameters.
    
    This function searches through a list of option parameters to find
    variable assignments in the format "varname=value" and returns the
    value portion.
    
    Args:
        option_list (list[str]): List of option parameters to search through.
        varname (str): The variable name to look for (without the = sign).
        
    Returns:
        str | None: The value assigned to the variable if found,
                    None if the variable is not found.
                    
    Example:
        >>> options = ['--internal-log', 'log_level=DEBUG', 'verbose=true']
        >>> level = get_var(options, 'log_level')
        >>> # Returns: 'DEBUG'
        >>> missing = get_var(options, 'missing_var')
        >>> # Returns: None
    """
    for option_var in option_list:
        if varname in option_var:
            return option_var.replace(f"{varname}=", "")

    return None


# Export public API
__all__ = [
    'Options',
    'exist_option',
    'get_option',
    'get_var',
]


# Example usage and testing
if __name__ == "__main__":
    print("apiwx.uiarg - Command line argument parser")
    print("This module provides argument parsing for apiwx applications")
    print("\nExample usage:")
    print("  python script.py --ui-debug --internal-log log_level=DEBUG")
    print("\nIn your code:")
    print("  from apiwx.uiarg import Options, exist_option, get_option")
    print("  if exist_option(Options.UI_DEBUG):")
    print("      print('Debug mode enabled')")
    print("  log_args = get_option(Options._INTERNAL_LOG)")
    print("  log_level = get_var(log_args, 'log_level')")
    
    print("\nCurrent command line arguments:")
    print(f"  sys.argv = {sys.argv}")
    
    print("\nChecking for known options:")
    for option in Options:
        exists = exist_option(option)
        print(f"  {option.name}: {'Found' if exists else 'Not found'}")
        if exists:
            values = get_option(option)
            print(f"    Values: {values}")