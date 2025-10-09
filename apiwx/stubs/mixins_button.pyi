"""Type stubs for apiwx.mixins_button module.

This module provides type information for advanced button behavior mixins 
that add sophisticated click handling, guard mechanisms, and state management 
to button components, enabling proper type checking and IDE support.
"""

from typing import Any, Optional, Callable
import threading

class SingleClickDisable:
    """Button generic that disables the button after a single click.
    
    This generic adds behavior to buttons that automatically disables them
    after being clicked once, preventing accidental double-clicks or rapid
    repeated clicking. The button can be configured to automatically
    re-enable after a specified duration.
    """
    
    @property
    def default_disable_duration(self) -> float: 
        """Default duration to disable button (in seconds)."""
        ...
    
    @property
    def disable_duration(self) -> float: 
        """Duration to disable button after click."""
        ...
    
    @disable_duration.setter
    def disable_duration(self, value: Optional[float]) -> None: ...
    
    @property
    def is_auto_re_enable(self) -> bool: 
        """Whether to automatically re-enable the button."""
        ...
    
    @is_auto_re_enable.setter
    def is_auto_re_enable(self, value: bool) -> None: ...
    
    def __init__(
        self,
        *args: Any,
        disable_duration: Optional[float] = ...,
        auto_re_enable: bool = ...,
        **kwds: Any
    ) -> None: ...
    
    def _on_single_click_disable(self, event: Any) -> None: 
        """Handle single click disable behavior."""
        ...
    
    def _re_enable_button(self) -> None: 
        """Re-enable the button after timeout."""
        ...

class DoubleClickOnly:
    """Button generic that requires double-click to activate.
    
    This generic modifies button behavior to only respond to double-clicks,
    ignoring single clicks. Useful for implementing confirmation patterns
    where accidental single clicks should be ignored.
    """
    
    @property
    def default_double_click_timeout(self) -> float: 
        """Default timeout for double-click detection (in seconds)."""
        ...
    
    @property
    def double_click_timeout(self) -> float: 
        """Timeout for double-click detection."""
        ...
    
    @double_click_timeout.setter
    def double_click_timeout(self, value: Optional[float]) -> None: ...
    
    def __init__(
        self,
        *args: Any,
        double_click_timeout: Optional[float] = ...,
        **kwds: Any
    ) -> None: ...
    
    def _on_double_click_only(self, event: Any) -> None: 
        """Handle double-click only behavior."""
        ...

class ClickGuard:
    """Advanced button generic with multiple protection mechanisms.
    
    This generic combines various click protection strategies including
    temporary disabling, double-click requirements, and confirmation messages.
    It provides the most comprehensive protection against accidental clicks.
    """
    
    @property
    def guard_message(self) -> Optional[str]: 
        """Message to display when requiring confirmation."""
        ...
    
    @guard_message.setter
    def guard_message(self, value: Optional[str]) -> None: ...
    
    @property
    def require_double_click(self) -> bool: 
        """Whether to require double-click for activation."""
        ...
    
    @require_double_click.setter
    def require_double_click(self, value: bool) -> None: ...
    
    @property
    def show_confirmation_dialog(self) -> bool: 
        """Whether to show confirmation dialog."""
        ...
    
    @show_confirmation_dialog.setter
    def show_confirmation_dialog(self, value: bool) -> None: ...
    
    def __init__(
        self,
        *args: Any,
        guard_message: Optional[str] = ...,
        require_double_click: bool = ...,
        show_confirmation_dialog: bool = ...,
        disable_duration: Optional[float] = ...,
        **kwds: Any
    ) -> None: ...
    
    def _on_click_guard(self, event: Any) -> None: 
        """Handle click guard behavior with multiple protection layers."""
        ...