"""
Generics Alias Module for apiwx

This module provides convenient type aliases for commonly used generic class combinations
in the apiwx framework. It defines pre-configured generic types that combine core wrapped
classes with various generic behaviors like Singleton, Multiton, AutoDetect, and specialized
component behaviors.

The module handles both relative and absolute imports to ensure compatibility across
different usage contexts. All aliases follow the naming pattern of combining the base
class name with descriptive behavior names.

Common Alias Categories:
- App aliases: Application-level generics with singleton patterns
- Window aliases: Window classes with panel detection and sizing behaviors
- Panel aliases: Panel classes with children detection and transition behaviors  
- Button aliases: Button classes with click behaviors and guards

Example Usage:
    from apiwx.generics_alias import AppBase, WindowWithPanel, PanelDetectChildren
    
    # Create singleton application
    app = AppBase()
    
    # Create window with automatic panel detection
    window = WindowWithPanel(parent=None, title="Main Window")
    
    # Create panel that detects child components
    panel = PanelDetectChildren(parent=window)
    
"""

try:
    from .core import (
        WrappedApp,
        WrappedWindow,
        WrappedPanel,
        WrappedButton,
        WrappedTextBox,
        WrappedStaticText,
        WrappedCheckBox,
        WrappedRadioBox,
        WrappedListBox,
        WrappedComboBox,
        WrappedSlider,
        WrappedGauge,
        WrappedListCtrl,
        WrappedScrolledWindow,
        WrappedChoice,
        WrappedImage,
    )

except ImportError:
    from core import (
        WrappedApp,
        WrappedWindow,
        WrappedPanel,
        WrappedButton,
        WrappedTextBox,
        WrappedStaticText,
        WrappedCheckBox,
        WrappedRadioBox,
        WrappedListBox,
        WrappedComboBox,
        WrappedSlider,
        WrappedGauge,
        WrappedListCtrl,
        WrappedScrolledWindow,
        WrappedChoice,
        WrappedImage,
    )

try:
    from .generics_app import (
        DetectWindow,
    )

except ImportError: 
    from generics_app import (
        DetectWindow,
    )

try:
    from .generics_window import (
        DetectPanel,
        ByPanelSize,
    )

except ImportError:
    from generics_window import (
        DetectPanel,
        ByPanelSize,
    )

try:
    from .generics_panel import (
        DetectChildren,
        WithBoarder,
    )

except ImportError:
    from generics_panel import (
        DetectChildren,
        WithBoarder,
    )

try:
    from .generics_base import (
        Singleton,
        Multiton,
    )

except ImportError:
    from generics_base import (
        Singleton,
        Multiton,
    )

try:
    from .generics_common import (
        AutoDetect,
        FixSize,
    )

except ImportError:
    from generics_common import (
        AutoDetect,
        FixSize,
    )

try:
    from .generics_core import (
        BaseGenerics,
    )

except ImportError:
    from generics_core import (
        BaseGenerics,
    )

try:
    from .generics_button import (
        DetectButton,
        SingleClickDisable,
        DoubleClickOnly,
        ClickGuard,
    )

except ImportError:
    from generics_button import (
        DetectButton,
        SingleClickDisable,
        DoubleClickOnly,
        ClickGuard,
    )

try:
    from .paneltransmodel import (
        NotTransition,
        SupportTransit,
    )

except ImportError:
    from paneltransmodel import (
        NotTransition,
        SupportTransit,
    )


AppBase = WrappedApp[Singleton]
""" WrappedApp<Singleton> """

AppDetectWindow = AppBase[DetectWindow]
""" WrappedApp<Singleton<DetectWindow>> """


WindowWithPanel = WrappedWindow[DetectPanel]
""" WrappedWindow<DetectPanel> """

WindowByPanelSize = WindowWithPanel[ByPanelSize]
""" WrappedWindow<DetectPanel<ByPanelSize>> """

WindowPanelTransit = WindowWithPanel[SupportTransit]
""" WrappedWindow<DetectPanel<SupportTransit>> """


PanelDetectChildren = WrappedPanel[DetectChildren]
""" WrappedPanel<DetectChildren> """

PanelWithBoarder = WrappedPanel[WithBoarder]
""" WrappedPanel<WithBoarder> """

PanelNoTransition = WrappedPanel[NotTransition]
""" WrappedPanel<NotTransition> """


ButtonDetect = WrappedButton[DetectButton]
""" WrappedButton<DetectButton> """

ButtonSingleClickDisable = WrappedButton[SingleClickDisable]
""" WrappedButton<SingleClickDisable> """

ButtonDoubleClickOnly = WrappedButton[DoubleClickOnly]
""" WrappedButton<DoubleClickOnly> """

ButtonClickGuard = WrappedButton[ClickGuard]
""" WrappedButton<ClickGuard> """