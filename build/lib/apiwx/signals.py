"""Event signal constants for wxPython applications.

This module provides convenient imports for all commonly used wxPython
event constants. It centralizes event signal definitions to simplify
event handling code and reduce boilerplate imports in wxPython
applications built with the apiwx framework.

The module includes event constants for:
    - Window events (size, move, close, focus, etc.)
    - Paint and drawing events
    - Keyboard and mouse events
    - Menu and dialog events
    - Scrolling events
    - Control-specific events (button, checkbox, listbox, etc.)
    - System events (DPI changes, display changes, etc.)
    - Touch and gesture events
    - Joystick events

Usage:
    >>> from apiwx.signals import EVT_BUTTON, EVT_CLOSE, EVT_PAINT
    >>> # Use events in window class definitions
    >>> self.Bind(EVT_BUTTON, self.on_button_click, button)
    >>> self.Bind(EVT_CLOSE, self.on_close)
"""

from wx import (
    # Window sizing and positioning events
    EVT_SIZE,
    EVT_SIZING,
    EVT_MOVE,
    EVT_MOVING,
    EVT_MOVE_START,
    EVT_MOVE_END,
    
    # Window lifecycle events
    EVT_CLOSE,
    EVT_END_SESSION,
    EVT_QUERY_END_SESSION,
    EVT_INIT_DIALOG,
    EVT_SHOW,
    EVT_MAXIMIZE,
    EVT_ICONIZE,
    
    # Paint and drawing events
    EVT_PAINT,
    EVT_NC_PAINT,
    EVT_ERASE_BACKGROUND,
    
    # Keyboard events
    EVT_CHAR,
    EVT_KEY_DOWN,
    EVT_KEY_UP,
    EVT_HOTKEY,
    EVT_CHAR_HOOK,
    
    # Menu events
    EVT_MENU_OPEN,
    EVT_MENU_CLOSE,
    EVT_MENU_HIGHLIGHT,
    EVT_MENU_HIGHLIGHT_ALL,
    
    # Focus events
    EVT_SET_FOCUS,
    EVT_KILL_FOCUS,
    EVT_CHILD_FOCUS,
    
    # Window activation and app events
    EVT_ACTIVATE,
    EVT_ACTIVATE_APP,
    EVT_HIBERNATE,
    
    # System and display events
    EVT_DROP_FILES,
    EVT_SYS_COLOUR_CHANGED,
    EVT_DISPLAY_CHANGED,
    EVT_DPI_CHANGED,
    EVT_NAVIGATION_KEY,
    EVT_PALETTE_CHANGED,
    EVT_QUERY_NEW_PALETTE,
    
    # Window creation and destruction
    EVT_WINDOW_CREATE,
    EVT_WINDOW_DESTROY,
    
    # Mouse cursor and capture events
    EVT_SET_CURSOR,
    EVT_MOUSE_CAPTURE_CHANGED,
    EVT_MOUSE_CAPTURE_LOST,
    
    # Mouse button events
    EVT_LEFT_DOWN,
    EVT_LEFT_UP,
    EVT_MIDDLE_DOWN,
    EVT_MIDDLE_UP,
    EVT_RIGHT_DOWN,
    EVT_RIGHT_UP,
    EVT_MOTION,
    EVT_LEFT_DCLICK,
    EVT_MIDDLE_DCLICK,
    EVT_RIGHT_DCLICK,
    EVT_LEAVE_WINDOW,
    EVT_ENTER_WINDOW,
    EVT_MOUSEWHEEL,
    
    # Auxiliary mouse button events
    EVT_MOUSE_AUX1_DOWN,
    EVT_MOUSE_AUX1_UP,
    EVT_MOUSE_AUX1_DCLICK,
    EVT_MOUSE_AUX2_DOWN,
    EVT_MOUSE_AUX2_UP,
    EVT_MOUSE_AUX2_DCLICK,
    EVT_MOUSE_EVENTS,
    EVT_MAGNIFY,
    EVT_MAGNIFY,
    
    # Scrolling events from wxWindow (sent to wxScrolledWindow)
    EVT_SCROLLWIN,
    EVT_SCROLLWIN_TOP,
    EVT_SCROLLWIN_BOTTOM,
    EVT_SCROLLWIN_LINEUP,
    EVT_SCROLLWIN_LINEDOWN,
    EVT_SCROLLWIN_PAGEUP,
    EVT_SCROLLWIN_PAGEDOWN,
    EVT_SCROLLWIN_THUMBTRACK,
    EVT_SCROLLWIN_THUMBRELEASE,
    
    # Scrolling events from wx.Slider and wx.ScrollBar
    EVT_SCROLL,
    EVT_SCROLL_TOP,
    EVT_SCROLL_BOTTOM,
    EVT_SCROLL_LINEUP,
    EVT_SCROLL_LINEDOWN,
    EVT_SCROLL_PAGEUP,
    EVT_SCROLL_PAGEDOWN,
    EVT_SCROLL_THUMBTRACK,
    EVT_SCROLL_THUMBRELEASE,
    EVT_SCROLL_CHANGED,
    EVT_SCROLL_ENDSCROLL,
    
    # Command scrolling events with ID
    EVT_COMMAND_SCROLL,
    EVT_COMMAND_SCROLL_TOP,
    EVT_COMMAND_SCROLL_BOTTOM,
    EVT_COMMAND_SCROLL_LINEUP,
    EVT_COMMAND_SCROLL_LINEDOWN,
    EVT_COMMAND_SCROLL_PAGEUP,
    EVT_COMMAND_SCROLL_PAGEDOWN,
    EVT_COMMAND_SCROLL_THUMBTRACK,
    EVT_COMMAND_SCROLL_THUMBRELEASE,
    EVT_COMMAND_SCROLL_CHANGED,
    EVT_COMMAND_SCROLL_ENDSCROLL,
    
    # Control events
    EVT_BUTTON,
    EVT_CHECKBOX,
    EVT_CHOICE,
    EVT_LISTBOX,
    EVT_LISTBOX_DCLICK,
    EVT_MENU,
    EVT_MENU_RANGE,
    EVT_SLIDER,
    EVT_RADIOBOX,
    EVT_RADIOBUTTON,
    EVT_SCROLLBAR,
    EVT_VLBOX,
    EVT_COMBOBOX,
    EVT_CHECKLISTBOX,
    EVT_COMBOBOX_DROPDOWN,
    EVT_COMBOBOX_CLOSEUP,
    
    # Tool and toolbar events
    EVT_TOOL,
    EVT_TOOL_RANGE,
    EVT_TOOL_RCLICKED,
    EVT_TOOL_RCLICKED_RANGE,
    EVT_TOOL_ENTER,
    EVT_TOOL_DROPDOWN,
    
    # Command events
    EVT_COMMAND_LEFT_CLICK,
    EVT_COMMAND_LEFT_DCLICK,
    EVT_COMMAND_RIGHT_CLICK,
    EVT_COMMAND_RIGHT_DCLICK,
    EVT_COMMAND_SET_FOCUS,
    EVT_COMMAND_KILL_FOCUS,
    EVT_COMMAND_ENTER,
    
    # Help events
    EVT_HELP,
    EVT_HELP_RANGE,
    EVT_DETAILED_HELP,
    EVT_DETAILED_HELP_RANGE,
    
    # Application events
    EVT_IDLE,
    EVT_UPDATE_UI,
    EVT_UPDATE_UI_RANGE,
    EVT_CONTEXT_MENU,
    EVT_THREAD,
    EVT_WINDOW_MODAL_DIALOG_CLOSED,
    
    # Joystick events
    EVT_JOY_BUTTON_DOWN,
    EVT_JOY_BUTTON_UP,
    EVT_JOY_MOVE,
    EVT_JOY_ZMOVE,
    EVT_JOYSTICK_EVENTS,
    
    # Gesture and touch events
    EVT_GESTURE_PAN,
    EVT_GESTURE_ZOOM,
    EVT_GESTURE_ROTATE,
    EVT_TWO_FINGER_TAP,
    EVT_LONG_PRESS,
    EVT_PRESS_AND_TAP,
    
    # Clipboard and other events
    EVT_CLIPBOARD_CHANGED,
    EVT_FULLSCREEN,
)


# Export all event constants for convenient access
__all__ = [
    # Window sizing and positioning events
    'EVT_SIZE', 'EVT_SIZING', 'EVT_MOVE', 'EVT_MOVING', 'EVT_MOVE_START',
    'EVT_MOVE_END',
    
    # Window lifecycle events
    'EVT_CLOSE', 'EVT_END_SESSION', 'EVT_QUERY_END_SESSION',
    'EVT_INIT_DIALOG', 'EVT_SHOW', 'EVT_MAXIMIZE', 'EVT_ICONIZE',
    
    # Paint and drawing events
    'EVT_PAINT', 'EVT_NC_PAINT', 'EVT_ERASE_BACKGROUND',
    
    # Keyboard events
    'EVT_CHAR', 'EVT_KEY_DOWN', 'EVT_KEY_UP', 'EVT_HOTKEY', 'EVT_CHAR_HOOK',
    
    # Menu events
    'EVT_MENU_OPEN', 'EVT_MENU_CLOSE', 'EVT_MENU_HIGHLIGHT',
    'EVT_MENU_HIGHLIGHT_ALL',
    
    # Focus events
    'EVT_SET_FOCUS', 'EVT_KILL_FOCUS', 'EVT_CHILD_FOCUS',
    
    # Window activation and app events
    'EVT_ACTIVATE', 'EVT_ACTIVATE_APP', 'EVT_HIBERNATE',
    
    # System and display events
    'EVT_DROP_FILES', 'EVT_SYS_COLOUR_CHANGED', 'EVT_DISPLAY_CHANGED',
    'EVT_DPI_CHANGED', 'EVT_NAVIGATION_KEY', 'EVT_PALETTE_CHANGED',
    'EVT_QUERY_NEW_PALETTE',
    
    # Window creation and destruction
    'EVT_WINDOW_CREATE', 'EVT_WINDOW_DESTROY',
    
    # Mouse cursor and capture events
    'EVT_SET_CURSOR', 'EVT_MOUSE_CAPTURE_CHANGED', 'EVT_MOUSE_CAPTURE_LOST',
    
    # Mouse button events
    'EVT_LEFT_DOWN', 'EVT_LEFT_UP', 'EVT_MIDDLE_DOWN', 'EVT_MIDDLE_UP',
    'EVT_RIGHT_DOWN', 'EVT_RIGHT_UP', 'EVT_MOTION', 'EVT_LEFT_DCLICK',
    'EVT_MIDDLE_DCLICK', 'EVT_RIGHT_DCLICK', 'EVT_LEAVE_WINDOW',
    'EVT_ENTER_WINDOW', 'EVT_MOUSEWHEEL',
    
    # Auxiliary mouse button events
    'EVT_MOUSE_AUX1_DOWN', 'EVT_MOUSE_AUX1_UP', 'EVT_MOUSE_AUX1_DCLICK',
    'EVT_MOUSE_AUX2_DOWN', 'EVT_MOUSE_AUX2_UP', 'EVT_MOUSE_AUX2_DCLICK',
    'EVT_MOUSE_EVENTS', 'EVT_MAGNIFY',
    
    # Scrolling events
    'EVT_SCROLLWIN', 'EVT_SCROLLWIN_TOP', 'EVT_SCROLLWIN_BOTTOM',
    'EVT_SCROLLWIN_LINEUP', 'EVT_SCROLLWIN_LINEDOWN', 'EVT_SCROLLWIN_PAGEUP',
    'EVT_SCROLLWIN_PAGEDOWN', 'EVT_SCROLLWIN_THUMBTRACK',
    'EVT_SCROLLWIN_THUMBRELEASE', 'EVT_SCROLL', 'EVT_SCROLL_TOP',
    'EVT_SCROLL_BOTTOM', 'EVT_SCROLL_LINEUP', 'EVT_SCROLL_LINEDOWN',
    'EVT_SCROLL_PAGEUP', 'EVT_SCROLL_PAGEDOWN', 'EVT_SCROLL_THUMBTRACK',
    'EVT_SCROLL_THUMBRELEASE', 'EVT_SCROLL_CHANGED', 'EVT_SCROLL_ENDSCROLL',
    
    # Command scrolling events
    'EVT_COMMAND_SCROLL', 'EVT_COMMAND_SCROLL_TOP',
    'EVT_COMMAND_SCROLL_BOTTOM', 'EVT_COMMAND_SCROLL_LINEUP',
    'EVT_COMMAND_SCROLL_LINEDOWN', 'EVT_COMMAND_SCROLL_PAGEUP',
    'EVT_COMMAND_SCROLL_PAGEDOWN', 'EVT_COMMAND_SCROLL_THUMBTRACK',
    'EVT_COMMAND_SCROLL_THUMBRELEASE', 'EVT_COMMAND_SCROLL_CHANGED',
    'EVT_COMMAND_SCROLL_ENDSCROLL',
    
    # Control events
    'EVT_BUTTON', 'EVT_CHECKBOX', 'EVT_CHOICE', 'EVT_LISTBOX',
    'EVT_LISTBOX_DCLICK', 'EVT_MENU', 'EVT_MENU_RANGE', 'EVT_SLIDER',
    'EVT_RADIOBOX', 'EVT_RADIOBUTTON', 'EVT_SCROLLBAR', 'EVT_VLBOX',
    'EVT_COMBOBOX', 'EVT_CHECKLISTBOX', 'EVT_COMBOBOX_DROPDOWN',
    'EVT_COMBOBOX_CLOSEUP',
    
    # Tool and toolbar events
    'EVT_TOOL', 'EVT_TOOL_RANGE', 'EVT_TOOL_RCLICKED',
    'EVT_TOOL_RCLICKED_RANGE', 'EVT_TOOL_ENTER', 'EVT_TOOL_DROPDOWN',
    
    # Command events
    'EVT_COMMAND_LEFT_CLICK', 'EVT_COMMAND_LEFT_DCLICK',
    'EVT_COMMAND_RIGHT_CLICK', 'EVT_COMMAND_RIGHT_DCLICK',
    'EVT_COMMAND_SET_FOCUS', 'EVT_COMMAND_KILL_FOCUS', 'EVT_COMMAND_ENTER',
    
    # Help events
    'EVT_HELP', 'EVT_HELP_RANGE', 'EVT_DETAILED_HELP',
    'EVT_DETAILED_HELP_RANGE',
    
    # Application events
    'EVT_IDLE', 'EVT_UPDATE_UI', 'EVT_UPDATE_UI_RANGE', 'EVT_CONTEXT_MENU',
    'EVT_THREAD', 'EVT_WINDOW_MODAL_DIALOG_CLOSED',
    
    # Joystick events
    'EVT_JOY_BUTTON_DOWN', 'EVT_JOY_BUTTON_UP', 'EVT_JOY_MOVE',
    'EVT_JOY_ZMOVE', 'EVT_JOYSTICK_EVENTS',
    
    # Gesture and touch events
    'EVT_GESTURE_PAN', 'EVT_GESTURE_ZOOM', 'EVT_GESTURE_ROTATE',
    'EVT_TWO_FINGER_TAP', 'EVT_LONG_PRESS', 'EVT_PRESS_AND_TAP',
    
    # Clipboard and other events
    'EVT_CLIPBOARD_CHANGED', 'EVT_FULLSCREEN',
]


# Example usage and common patterns
if __name__ == "__main__":
    print("apiwx.signals - Event signal constants for wxPython")
    print("This module provides convenient imports for wxPython events")
    print("\nExample usage:")
    print("  from apiwx.signals import EVT_BUTTON, EVT_CLOSE, EVT_PAINT")
    print("  # In your window class:")
    print("  self.Bind(EVT_BUTTON, self.on_button_click, button)")
    print("  self.Bind(EVT_CLOSE, self.on_close)")
    print("  self.Bind(EVT_PAINT, self.on_paint)")
    print(f"\nTotal events available: {len(__all__)}")
