"""Mixin type definitions for wxPython wx.App.

This module provides mixin type definitions and type variables for
wxPython application objects. It includes auto-detection types for
window classes that can be used with type checkers and IDEs to provide
better type safety and code completion.
"""
try:
    from . import core
    from . import mixins_common

except ImportError:
    import core
    import mixins_common


class DetectWindow(mixins_common.AutoDetect[
        core.Window
    ]):
    """Type variable for auto-detecting window class.

    This type alias provides automatic type detection for window classes
    used in wxPython applications. It allows type checkers to infer the
    correct window type based on the usage context.
    """

