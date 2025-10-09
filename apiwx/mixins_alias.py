"""Mixins Alias Module for apiwx.

This module provides convenient type aliases for commonly used mixin
class combinations in the apiwx framework. It defines pre-configured
mixin types that combine core wrapped classes with various mixin
behaviors like Singleton, Multiton, AutoDetect, and specialized
component behaviors.

The module handles both relative and absolute imports to ensure
compatibility across different usage contexts. All aliases follow
the naming pattern of combining the base class name with descriptive
behavior names.

Common Alias Categories:
    - App aliases: Application-level mixins with singleton patterns
    - Window aliases: Window classes with panel detection and sizing
    - Panel aliases: Panel classes with children detection and transitions
    - Button aliases: Button classes with click behaviors and guards

Example Usage:
    >>> from apiwx.mixins_alias import AppBase, WindowWithPanel
    >>> from apiwx.mixins_alias import PanelDetectChildren
    >>> 
    >>> # Create singleton application
    >>> app = AppBase()
    >>> 
    >>> # Create window with automatic panel detection
    >>> window = WindowWithPanel(parent=None, title="Main Window")
    >>> 
    >>> # Create panel that detects child components
    >>> panel = PanelDetectChildren(parent=window)
"""

from typing import TypeAlias

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
    from .mixins_app import (
        DetectWindow,
    )

except ImportError: 
    from mixins_app import (
        DetectWindow,
    )

try:
    from .mixins_window import (
        DetectPanel,
        ByPanelSize,
    )

except ImportError:
    from mixins_window import (
        DetectPanel,
        ByPanelSize,
    )

try:
    from .mixins_panel import (
        DetectChildren,
        WithBoarder,
    )

except ImportError:
    from mixins_panel import (
        DetectChildren,
        WithBoarder,
    )

try:
    from .mixins_base import (
        Singleton,
        Multiton,
    )

except ImportError:
    from mixins_base import (
        Singleton,
        Multiton,
    )

try:
    from .mixins_common import (
        AutoDetect,
        FixSize,
    )

except ImportError:
    from mixins_common import (
        AutoDetect,
        FixSize,
    )

try:
    from .mixins_core import (
        BaseMixins,
    )

except ImportError:
    from mixins_core import (
        BaseMixins,
    )

try:
    from .mixins_button import (
        SingleClickDisable,
        DoubleClickOnly,
        ClickGuard,
    )

except ImportError:
    from mixins_button import (
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



# Application type aliases (PEP 613 compliant)
AppBase: TypeAlias = WrappedApp[Singleton]
"""Singleton application instance.

This type alias creates a WrappedApp with Singleton behavior, ensuring
only one application instance can exist at a time.

Type: WrappedApp[Singleton]

Args:
    name (str): The application name

Example:
    >>> app = AppBase("MyApp")
    >>> # Only one instance will exist, subsequent calls return same instance
"""

AppDetectWindow: TypeAlias = WrappedApp[Singleton, DetectWindow]
"""Singleton application with window detection.

This type alias creates a WrappedApp with both Singleton behavior and
automatic window detection capabilities.

Type: WrappedApp[Singleton, DetectWindow]

Args:
    name (str): The application name

Features:
    - Singleton pattern: Only one instance can exist
    - Window detection: Automatically detects and manages child windows

Example:
    >>> app = AppDetectWindow("MyApp")
    >>> # Application with automatic window management
"""


# Window aliases
WindowWithPanel: TypeAlias = WrappedWindow[DetectPanel]
"""Window with automatic panel detection.

This type alias creates a WrappedWindow that automatically detects
and manages child panels.

Type: WrappedWindow[DetectPanel]

Args:
    app: The parent application instance
    size (tuple[int, int] | None): Window size as (width, height)
    pos (tuple[int, int] | None): Window position as (x, y)
    title (str | None): Window title text
    color (tuple[int, int, int] | None): Background color as RGB tuple
    style (int | None): wxPython window style flags

Features:
    - Panel detection: Automatically detects and manages child panels

Example:
    >>> window = WindowWithPanel(app, size=(800, 600), title="Main Window")
"""

WindowByPanelSize: TypeAlias = WindowWithPanel[ByPanelSize]
"""Window with panel detection and size management.

This type alias creates a WrappedWindow with panel detection and
size management based on the client panel size.

Type: WrappedWindow[DetectPanel, ByPanelSize]

Args:
    app: The parent application instance
    size (tuple[int, int] | None): Window size as (width, height)
    pos (tuple[int, int] | None): Window position as (x, y)
    title (str | None): Window title text
    color (tuple[int, int, int] | None): Background color as RGB tuple
    style (int | None): wxPython window style flags

Features:
    - Panel detection: Automatically detects and manages child panels
    - Size management: Adjusts window size based on panel content

Example:
    >>> window = WindowByPanelSize(app, title="Auto-sized Window")
"""

WindowPanelTransit: TypeAlias = WrappedWindow[SupportTransit]
"""Window with panel transition support.

This type alias creates a WrappedWindow that supports panel
transitions and visibility management.

Type: WrappedWindow[SupportTransit]

Args:
    app: The parent application instance
    size (tuple[int, int] | None): Window size as (width, height)
    pos (tuple[int, int] | None): Window position as (x, y)
    title (str | None): Window title text
    color (tuple[int, int, int] | None): Background color as RGB tuple
    style (int | None): wxPython window style flags

Features:
    - Panel transitions: Supports smooth panel switching and visibility 
      management

Example:
    >>> window = WindowPanelTransit(app, size=(800, 600), 
    ...                            title="Transition Window")
"""

WindowSizeTransitWithPanel: TypeAlias = WrappedWindow[
    SupportTransit, ByPanelSize
]
"""Window with panel transitions and size management.

This type alias creates a WrappedWindow with both panel transition
support and size management based on client panel size.

Type: WrappedWindow[SupportTransit, ByPanelSize]

Args:
    app: The parent application instance
    size (tuple[int, int] | None): Window size as (width, height)
    pos (tuple[int, int] | None): Window position as (x, y)
    title (str | None): Window title text
    color (tuple[int, int, int] | None): Background color as RGB tuple
    style (int | None): wxPython window style flags

Features:
    - Panel transitions: Supports smooth panel switching and visibility 
      management
    - Size management: Adjusts window size based on panel content

Example:
    >>> window = WindowSizeTransitWithPanel(app, title="Dynamic Window")
"""


# Panel aliases
PanelDetectChildren: TypeAlias = WrappedPanel[DetectChildren]
"""Panel with automatic child component detection.

This type alias creates a WrappedPanel that automatically detects
and manages child UI components.

Type: WrappedPanel[DetectChildren]

Args:
    parent: The parent window or panel
    size (tuple[int, int] | None): Panel size as (width, height)
    pos (tuple[int, int] | None): Panel position as (x, y)
    color (tuple[int, int, int] | None): Background color as RGB tuple
    style (int | None): wxPython panel style flags

Features:
    - Child detection: Automatically detects and manages child UI components
    - Component indexing: Provides indexed access to child components

Example:
    >>> panel = PanelDetectChildren(window, size=(400, 300))
    >>> # Child components will be automatically detected and indexed
"""

PanelWithBoarder: TypeAlias = WrappedPanel[WithBoarder]
"""Panel with border drawing functionality.

This type alias creates a WrappedPanel with automatic border
drawing capabilities around the panel edges.

Type: WrappedPanel[WithBoarder]

Args:
    parent: The parent window or panel
    size (tuple[int, int] | None): Panel size as (width, height)
    pos (tuple[int, int] | None): Panel position as (x, y)
    color (tuple[int, int, int] | None): Background color as RGB tuple
    style (int | None): wxPython panel style flags
    boarder_color (tuple[int, int, int] | None): Border color as RGB tuple
    boarder_thickness (int): Border line thickness in pixels
    boarder_offset (int): Border offset from panel edges in pixels

Features:
    - Border drawing: Automatic border rendering around panel edges
    - Customizable appearance: Color, thickness, and offset control

Example:
    >>> panel = PanelWithBoarder(
    ...     window, 
    ...     size=(300, 200),
    ...     boarder_color=(255, 0, 0),
    ...     boarder_thickness=2
    ... )
"""

PanelNoTransition: TypeAlias = WrappedPanel[NotTransition]
"""Panel excluded from transition management.

This type alias creates a WrappedPanel that is excluded from
automatic panel transition systems.

Type: WrappedPanel[NotTransition]

Args:
    parent: The parent window or panel
    size (tuple[int, int] | None): Panel size as (width, height)
    pos (tuple[int, int] | None): Panel position as (x, y)
    color (tuple[int, int, int] | None): Background color as RGB tuple
    style (int | None): wxPython panel style flags

Features:
    - Transition exclusion: Panel is excluded from automatic transition 
      management
    - Always visible: Remains visible during panel transitions

Example:
    >>> panel = PanelNoTransition(window, size=(200, 100))
    >>> # Panel will not participate in transition animations
"""


# Button aliases
ButtonSingleClickDisable: TypeAlias = WrappedButton[SingleClickDisable]
"""Button that disables after single click.

This type alias creates a WrappedButton that automatically disables
itself after being clicked once to prevent double-clicking.

Type: WrappedButton[SingleClickDisable]

Args:
    parent: The parent window or panel
    size (tuple[int, int] | None): Button size as (width, height)
    pos (tuple[int, int] | None): Button position as (x, y)
    label (str | None): Button text label
    font (font object | None): Button text font
    color_foreground (tuple[int, int, int] | None): Text color as RGB tuple
    color_background (tuple[int, int, int] | None): Background color as 
        RGB tuple
    style (int | None): wxPython button style flags
    disable_duration (float | None): Duration to disable button (seconds)
    auto_re_enable (bool): Whether to automatically re-enable button

Features:
    - Single click disable: Automatically disables after first click
    - Configurable duration: Set disable duration or manual re-enable
    - Double-click prevention: Prevents accidental multiple submissions

Example:
    >>> button = ButtonSingleClickDisable(
    ...     panel,
    ...     label="Submit",
    ...     disable_duration=2.0
    ... )
"""

ButtonDoubleClickOnly: TypeAlias = WrappedButton[DoubleClickOnly]
"""Button that responds only to double-clicks.

This type alias creates a WrappedButton that ignores single clicks
and only responds to double-click events.

Type: WrappedButton[DoubleClickOnly]

Args:
    parent: The parent window or panel
    size (tuple[int, int] | None): Button size as (width, height)
    pos (tuple[int, int] | None): Button position as (x, y)
    label (str | None): Button text label
    font (font object | None): Button text font
    color_foreground (tuple[int, int, int] | None): Text color as RGB tuple
    color_background (tuple[int, int, int] | None): Background color as 
        RGB tuple
    style (int | None): wxPython button style flags
    double_click_timeout (float | None): Maximum time between clicks 
        (seconds)
    show_single_click_feedback (bool): Whether to show feedback on single 
        clicks

Features:
    - Double-click only: Ignores single clicks, requires double-click
    - Timeout control: Configure maximum time between clicks
    - Visual feedback: Optional feedback for single click attempts

Example:
    >>> button = ButtonDoubleClickOnly(
    ...     panel,
    ...     label="Delete",
    ...     double_click_timeout=0.5
    ... )
"""

ButtonClickGuard: TypeAlias = WrappedButton[ClickGuard]
"""Button with click protection mechanisms.

This type alias creates a WrappedButton with built-in protection
against accidental or rapid multiple clicks.

Type: WrappedButton[ClickGuard]

Args:
    parent: The parent window or panel
    size (tuple[int, int] | None): Button size as (width, height)
    pos (tuple[int, int] | None): Button position as (x, y)
    label (str | None): Button text label
    font (font object | None): Button text font
    color_foreground (tuple[int, int, int] | None): Text color as RGB tuple
    color_background (tuple[int, int, int] | None): Background color as 
        RGB tuple
    style (int | None): wxPython button style flags
    require_double_click (bool): Whether to require double-click confirmation
    disable_duration (float): Duration to disable after click (seconds)
    guard_message (str | None): Message to display during guard period

Features:
    - Click protection: Guards against accidental or rapid clicks
    - Optional double-click: Can require double-click for confirmation
    - Guard messaging: Shows custom message during protection period
    - Disable duration: Configurable protection time period

Example:
    >>> button = ButtonClickGuard(
    ...     panel,
    ...     label="Dangerous Action",
    ...     require_double_click=True,
    ...     guard_message="Click again to confirm"
    ... )
"""


# Export all type aliases for convenient access
__all__ = [
    # Application aliases
    'AppBase',
    'AppDetectWindow',
    
    # Window aliases
    'WindowWithPanel',
    'WindowByPanelSize',
    'WindowPanelTransit',
    'WindowSizeTransitWithPanel',
    
    # Panel aliases
    'PanelDetectChildren',
    'PanelWithBoarder',
    'PanelNoTransition',
    
    # Button aliases
    'ButtonSingleClickDisable',
    'ButtonDoubleClickOnly',
    'ButtonClickGuard',
]


# Example usage and common patterns
if __name__ == "__main__":
    print("apiwx.mixins_alias - Type aliases for mixin combinations")
    print("This module provides convenient aliases for common mixin types")
    print("\nExample usage:")
    print("  from apiwx.mixins_alias import AppBase, WindowWithPanel")
    print("  app = AppBase()  # Singleton application")
    print("  window = WindowWithPanel(None, 'Title')  # Window with panels")
    print("\nAvailable aliases:")
    
    categories = {
        "Application": ["AppBase", "AppDetectWindow"],
        "Window": ["WindowWithPanel", "WindowByPanelSize", 
                  "WindowPanelTransit", "WindowSizeTransitWithPanel"],
        "Panel": ["PanelDetectChildren", "PanelWithBoarder", 
                 "PanelNoTransition"],
        "Button": ["ButtonSingleClickDisable", "ButtonDoubleClickOnly", 
                  "ButtonClickGuard"],
    }
    
    for category, aliases in categories.items():
        print(f"  {category}: {len(aliases)} aliases")
        for alias in aliases:
            print(f"    - {alias}")
    
    print(f"\nTotal aliases: {len(__all__)}")