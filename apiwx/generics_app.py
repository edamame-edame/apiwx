"""
# apiwx - A generic definitions for wxPython wx.App.
"""
try:
    from . import core
    from . import generics_common
except ImportError:
    import core
    import generics_common


DetectWindow = generics_common.AutoDetect[
    core.WrappedWindow
]
''' ### A type variable for auto detect window class. '''

