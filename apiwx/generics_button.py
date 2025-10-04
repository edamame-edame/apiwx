"""
# apiwx - A generic definitions for wxPython wx.Button.
Button-specific generics for enhanced click behavior and control
"""
import time
import threading
try:
    from . import core
    from . import generics_common
    from . import debug
except ImportError:
    import core
    import generics_common
    import debug


class SingleClickDisable:
    """
    # Button generic that disables the button after a single click
    ### Usage
    ```python
    button = WrappedButton[SingleClickDisable](
    panel,
    size=(120, 40),
    pos=(20, 20),
    label="Click Me",
    disable_duration=2.0 # Re-enable after 2 seconds
    )

    # Connect event handler
    def on_click(event):
    print("Button was clicked!")
    button.slots_on_click += on_click
    ```
    """

    @property
    def default_disable_duration(self) -> float:
        """Default duration to disable button (in seconds)"""
        return 1.0

    @property
    def disable_duration(self) -> float:
        """Duration to disable button after click"""
        return self._disable_duration

    @disable_duration.setter
    def disable_duration(self, value: float | None):
        if value is None:
            value = self.default_disable_duration
            self._disable_duration = max(0.1, float(value))

    @property
    def is_auto_re_enable(self) -> bool:
        """Whether to automatically re-enable the button"""
        return self._auto_re_enable

    @is_auto_re_enable.setter
    def is_auto_re_enable(self, value: bool):
        self._auto_re_enable = bool(value)

    def __init__(
            self,
            *args,
            disable_duration: float | None = None,
            auto_re_enable: bool = False,
            **kwds
        ):
        # super class init was called from WrappedButton.__init__
        # so do nothing here
        ...

        # below code was called after super class init

        # set disable duration
        self.disable_duration = disable_duration

        # set auto re-enable flag
        self.is_auto_re_enable = auto_re_enable

        # store original click handlers
        self._original_click_slots = []

        # connect our click interceptor
        self.slots_on_click.insert(0, self._handle_single_click)

        debug.uilog("SINGLE_CLICK_DISABLE", f"Initialized with duration: {self.disable_duration}s, auto_re_enable: {self.is_auto_re_enable}")

    def _handle_single_click(self, event):
        """Handle single click by disabling button and scheduling re-enable"""
        debug.uilog("SINGLE_CLICK_DISABLE", "Button clicked - disabling")

        # Disable the button immediately
        self.Enable(False)

        # Schedule re-enabling if auto re-enable is enabled
        if self.is_auto_re_enable and self.disable_duration > 0:
            timer_thread = threading.Timer(self.disable_duration, self._re_enable_button)
            timer_thread.daemon = True
            timer_thread.start()

    def _re_enable_button(self):
        """Re-enable the button (called by timer)"""
        debug.uilog("SINGLE_CLICK_DISABLE", "Re-enabling button")

        try:
            # Use CallAfter for thread-safe GUI update
            import wx
            wx.CallAfter(self._do_re_enable)

        except:
            # Fallback for direct call
            self._do_re_enable()

    def _do_re_enable(self):
        """Actually re-enable the button"""
        self.Enable(True)
        debug.uilog("SINGLE_CLICK_DISABLE", "Button re-enabled")

    def manual_re_enable(self):
        """Manually re-enable the button"""
        self._do_re_enable()


class DoubleClickOnly:
    """
    # Button generic that only responds to double-clicks
    ### Usage
    ```python
    button = WrappedButton[DoubleClickOnly](
    panel,
    size=(120, 40),
    pos=(20, 20),
    label="Double Click Me",
    double_click_timeout=0.5 # Maximum time between clicks
    )

    # Connect event handler (will only trigger on double-click)
    def on_double_click(event):
    print("Button was double-clicked!")
    button.slots_on_click += on_double_click
    ```
    """

    @property
    def default_double_click_timeout(self) -> float:
        """Default timeout for detecting double-click (in seconds)"""
        return 0.4

    @property
    def double_click_timeout(self) -> float:
        """Maximum time between clicks to count as double-click"""
        return self._double_click_timeout

    @double_click_timeout.setter
    def double_click_timeout(self, value: float | None):
        if value is None:
            value = self.default_double_click_timeout

        self._double_click_timeout = max(0.1, float(value))

    @property
    def show_single_click_feedback(self) -> bool:
        """Whether to show visual feedback for single clicks"""
        return self._show_feedback

    @show_single_click_feedback.setter
    def show_single_click_feedback(self, value: bool):
        self._show_feedback = bool(value)

    def __init__(
        self,
        *args,
        double_click_timeout: float | None = None,
        show_single_click_feedback: bool = True,
        **kwds
        ):
        # super class init was called from WrappedButton.__init__
        # so do nothing here
        ...

        # below code was called after super class init

        # set double click timeout
        self.double_click_timeout = double_click_timeout

        # set feedback flag
        self.show_single_click_feedback = show_single_click_feedback

        # track click state
        self._last_click_time = 0
        self._click_count = 0
        self._pending_timer = None

        # store original click slots
        self._stored_click_slots = None

        # replace click handler
        self._intercept_click_events()

        debug.uilog("DOUBLE_CLICK_ONLY", f"Initialized with timeout: {self.double_click_timeout}s, feedback: {self.show_single_click_feedback}")

    def _intercept_click_events(self):
        """Intercept and replace click event handling"""
        # Store original click slots
        self._stored_click_slots = list(self.slots_on_click)

        # Clear original slots
        self.slots_on_click.clear()

        # Add our double-click handler
        self.slots_on_click += self._handle_click_for_double_click

    def _handle_click_for_double_click(self, event):
        """Handle clicks and detect double-clicks"""
        current_time = time.time()

        # Check if this is within double-click timeout
        if (current_time - self._last_click_time) <= self.double_click_timeout:
            self._click_count += 1

        else:
            self._click_count = 1

        self._last_click_time = current_time

        debug.uilog("DOUBLE_CLICK_ONLY", f"Click #{self._click_count} at {current_time}")

        # Cancel any pending single-click timer
        if self._pending_timer:
            self._pending_timer.cancel()
            self._pending_timer = None

        if self._click_count >= 2:
            # Double-click detected!
            debug.uilog("DOUBLE_CLICK_ONLY", "Double-click confirmed - executing handlers")
            self._execute_stored_handlers(event)
            self._click_count = 0
        else:
            # Single click - wait for potential second click
            if self.show_single_click_feedback:
                debug.uilog("DOUBLE_CLICK_ONLY", "Single click - waiting for double-click")
                self._show_single_click_feedback()

                # Start timer for single-click timeout
                self._pending_timer = threading.Timer(
                    self.double_click_timeout,
                    self._single_click_timeout
                )

                self._pending_timer.daemon = True
                self._pending_timer.start()

    def _execute_stored_handlers(self, event):
        """Execute the original click handlers"""
        if self._stored_click_slots:
            for handler in self._stored_click_slots:
                try:
                    handler(event)

                except Exception as e:
                    debug.uilog("DOUBLE_CLICK_ONLY", f"Error in click handler: {e}")

    def _single_click_timeout(self):
        """Called when single-click timeout expires"""
        self._click_count = 0
        debug.uilog("DOUBLE_CLICK_ONLY", "Single-click timeout - reset")

    def _show_single_click_feedback(self):
        """Show visual feedback for single click"""
        try:
            # Temporarily change button appearance
            original_label = self.label
            self.label = f"({original_label})"

            # Reset label after short delay
            def reset_label():
                try:
                    import wx
                    wx.CallAfter(lambda: setattr(self, 'label', original_label))

                except:
                    self.label = original_label

            timer = threading.Timer(0.2, reset_label)
            timer.daemon = True
            timer.start()

        except Exception as e:
            debug.uilog("DOUBLE_CLICK_ONLY", f"Feedback error: {e}")

    def add_double_click_handler(self, handler):
        """Add a handler that will only be called on double-click"""
        if self._stored_click_slots is None:
            self._stored_click_slots = []
            self._stored_click_slots.append(handler)

    def remove_double_click_handler(self, handler):
        """Remove a double-click handler"""
        if self._stored_click_slots and handler in self._stored_click_slots:
            self._stored_click_slots.remove(handler)


class ClickGuard:
    """
    # Button generic that combines single-click disable with optional double-click requirement
    ### Usage
    ```python
    button = WrappedButton[ClickGuard](
    panel,
    size=(120, 40),
    pos=(20, 20),
    label="Guarded Button",
    require_double_click=True,
    disable_duration=3.0,
    guard_message="Click again to confirm"
    )
    ```
    """

    @property
    def default_guard_message(self) -> str:
        """Default message to show during guard period"""
        return "Click again to confirm"

    @property
    def guard_message(self) -> str:
        """Message to show during guard period"""
        return self._guard_message

    @guard_message.setter
    def guard_message(self, value: str | None):
        if value is None:
            value = self.default_guard_message
            self._guard_message = str(value)

    def __init__(
        self,
        *args,
        require_double_click: bool = False,
        disable_duration: float = 2.0,
        guard_message: str | None = None,
        **kwds
    ):
    # super class init was called from WrappedButton.__init__
    # so do nothing here
        ...

        # below code was called after super class init

        self.require_double_click = require_double_click
        self.disable_duration = disable_duration
        self.guard_message = guard_message

        # State tracking
        self._original_label = None
        self._is_in_guard_state = False
        self._guard_timer = None

        # Store original handlers
        self._original_handlers = list(self.slots_on_click)

        # Replace with our guarded handler
        self.slots_on_click.clear()
        self.slots_on_click += self._handle_guarded_click

        debug.uilog("CLICK_GUARD", f"Initialized: double_click={require_double_click}, duration={disable_duration}s")

    def _handle_guarded_click(self, event):
        """Handle guarded click logic"""
        if self._is_in_guard_state:
            # Second click during guard period - execute handlers
            debug.uilog("CLICK_GUARD", "Guard confirmed - executing handlers")
            self._execute_original_handlers(event)
            self._exit_guard_state()
        else:
            # First click or after guard period
            if self.require_double_click:
                debug.uilog("CLICK_GUARD", "Entering guard state")
                self._enter_guard_state()
            else:
                # Single click mode - just execute with disable
                debug.uilog("CLICK_GUARD", "Single click mode - executing with disable")
                self._execute_original_handlers(event)
                self._temporary_disable()

    def _enter_guard_state(self):
        """Enter guard state waiting for confirmation click"""
        self._is_in_guard_state = True

        # Save original label and show guard message
        if self._original_label is None:
            self._original_label = self.label
            self.label = self.guard_message

        # Start guard timeout
        self._guard_timer = threading.Timer(
            self.disable_duration,
            self._guard_timeout
        )

        self._guard_timer.daemon = True
        self._guard_timer.start()

    def _exit_guard_state(self):
        """Exit guard state and restore normal operation"""
        self._is_in_guard_state = False

        # Cancel guard timer
        if self._guard_timer:
            self._guard_timer.cancel()
            self._guard_timer = None

        # Restore original label
        if self._original_label:
            self.label = self._original_label

        # Temporarily disable button
        self._temporary_disable()

    def _guard_timeout(self):
        """Called when guard period times out"""
        debug.uilog("CLICK_GUARD", "Guard timeout - resetting")

        try:
            import wx
            wx.CallAfter(self._reset_from_guard)

        except:
            self._reset_from_guard()

    def _reset_from_guard(self):
        """Reset button from guard state"""
        self._is_in_guard_state = False

        if self._original_label:
            self.label = self._original_label

    def _temporary_disable(self):
        """Temporarily disable the button"""
        self.Enable(False)

        # Re-enable after duration
        re_enable_timer = threading.Timer(
            self.disable_duration * 0.5, # Shorter disable after successful action
            self._re_enable
        )

        re_enable_timer.daemon = True
        re_enable_timer.start()

    def _re_enable(self):
        """Re-enable the button"""
        try:
            import wx
            wx.CallAfter(lambda: self.Enable(True))

        except:
            self.Enable(True)
            debug.uilog("CLICK_GUARD", "Button re-enabled")

    def _execute_original_handlers(self, event):
        """Execute the original click handlers"""
        for handler in self._original_handlers:
            try:
                handler(event)
                
            except Exception as e:
                debug.uilog("CLICK_GUARD", f"Handler error: {e}")


""" ### A type variable for auto detect button class. """