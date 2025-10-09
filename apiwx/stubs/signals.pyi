"""Type stubs for apiwx.signals module.

This module provides type information for wxPython event signal constants,
enabling proper type checking and IDE support for event handling.
"""

import wx

# Window sizing and positioning events
EVT_SIZE: wx.PyEventBinder
EVT_SIZING: wx.PyEventBinder
EVT_MOVE: wx.PyEventBinder
EVT_MOVING: wx.PyEventBinder
EVT_MOVE_START: wx.PyEventBinder
EVT_MOVE_END: wx.PyEventBinder

# Window lifecycle events
EVT_CLOSE: wx.PyEventBinder
EVT_END_SESSION: wx.PyEventBinder
EVT_QUERY_END_SESSION: wx.PyEventBinder
EVT_INIT_DIALOG: wx.PyEventBinder
EVT_SHOW: wx.PyEventBinder
EVT_MAXIMIZE: wx.PyEventBinder
EVT_ICONIZE: wx.PyEventBinder

# Paint and drawing events
EVT_PAINT: wx.PyEventBinder
EVT_NC_PAINT: wx.PyEventBinder
EVT_ERASE_BACKGROUND: wx.PyEventBinder

# Keyboard events
EVT_CHAR: wx.PyEventBinder
EVT_KEY_DOWN: wx.PyEventBinder
EVT_KEY_UP: wx.PyEventBinder
EVT_HOTKEY: wx.PyEventBinder
EVT_CHAR_HOOK: wx.PyEventBinder

# Menu events
EVT_MENU_OPEN: wx.PyEventBinder
EVT_MENU_CLOSE: wx.PyEventBinder
EVT_MENU_HIGHLIGHT: wx.PyEventBinder
EVT_MENU_HIGHLIGHT_ALL: wx.PyEventBinder

# Focus events
EVT_SET_FOCUS: wx.PyEventBinder
EVT_KILL_FOCUS: wx.PyEventBinder
EVT_CHILD_FOCUS: wx.PyEventBinder

# Window activation and app events
EVT_ACTIVATE: wx.PyEventBinder
EVT_ACTIVATE_APP: wx.PyEventBinder
EVT_HIBERNATE: wx.PyEventBinder

# System and display events
EVT_DROP_FILES: wx.PyEventBinder
EVT_SYS_COLOUR_CHANGED: wx.PyEventBinder
EVT_DISPLAY_CHANGED: wx.PyEventBinder
EVT_DPI_CHANGED: wx.PyEventBinder
EVT_NAVIGATION_KEY: wx.PyEventBinder
EVT_PALETTE_CHANGED: wx.PyEventBinder
EVT_QUERY_NEW_PALETTE: wx.PyEventBinder

# Window creation and destruction
EVT_WINDOW_CREATE: wx.PyEventBinder
EVT_WINDOW_DESTROY: wx.PyEventBinder

# Mouse cursor and capture events
EVT_SET_CURSOR: wx.PyEventBinder
EVT_MOUSE_CAPTURE_CHANGED: wx.PyEventBinder
EVT_MOUSE_CAPTURE_LOST: wx.PyEventBinder

# Mouse button events
EVT_LEFT_DOWN: wx.PyEventBinder
EVT_LEFT_UP: wx.PyEventBinder
EVT_MIDDLE_DOWN: wx.PyEventBinder
EVT_MIDDLE_UP: wx.PyEventBinder
EVT_RIGHT_DOWN: wx.PyEventBinder
EVT_RIGHT_UP: wx.PyEventBinder
EVT_MOTION: wx.PyEventBinder
EVT_LEFT_DCLICK: wx.PyEventBinder
EVT_MIDDLE_DCLICK: wx.PyEventBinder
EVT_RIGHT_DCLICK: wx.PyEventBinder
EVT_LEAVE_WINDOW: wx.PyEventBinder
EVT_ENTER_WINDOW: wx.PyEventBinder
EVT_MOUSEWHEEL: wx.PyEventBinder

# Auxiliary mouse button events
EVT_MOUSE_AUX1_DOWN: wx.PyEventBinder
EVT_MOUSE_AUX1_UP: wx.PyEventBinder
EVT_MOUSE_AUX1_DCLICK: wx.PyEventBinder
EVT_MOUSE_AUX2_DOWN: wx.PyEventBinder
EVT_MOUSE_AUX2_UP: wx.PyEventBinder
EVT_MOUSE_AUX2_DCLICK: wx.PyEventBinder
EVT_MOUSE_EVENTS: wx.PyEventBinder
EVT_MAGNIFY: wx.PyEventBinder

# Scrolling events from wxWindow (sent to wxScrolledWindow)
EVT_SCROLLWIN: wx.PyEventBinder
EVT_SCROLLWIN_TOP: wx.PyEventBinder
EVT_SCROLLWIN_BOTTOM: wx.PyEventBinder
EVT_SCROLLWIN_LINEUP: wx.PyEventBinder
EVT_SCROLLWIN_LINEDOWN: wx.PyEventBinder
EVT_SCROLLWIN_PAGEUP: wx.PyEventBinder
EVT_SCROLLWIN_PAGEDOWN: wx.PyEventBinder
EVT_SCROLLWIN_THUMBTRACK: wx.PyEventBinder
EVT_SCROLLWIN_THUMBRELEASE: wx.PyEventBinder

# Scrolling events from wx.Slider and wx.ScrollBar
EVT_SCROLL: wx.PyEventBinder
EVT_SCROLL_TOP: wx.PyEventBinder
EVT_SCROLL_BOTTOM: wx.PyEventBinder
EVT_SCROLL_LINEUP: wx.PyEventBinder
EVT_SCROLL_LINEDOWN: wx.PyEventBinder
EVT_SCROLL_PAGEUP: wx.PyEventBinder
EVT_SCROLL_PAGEDOWN: wx.PyEventBinder
EVT_SCROLL_THUMBTRACK: wx.PyEventBinder
EVT_SCROLL_THUMBRELEASE: wx.PyEventBinder
EVT_SCROLL_CHANGED: wx.PyEventBinder
EVT_SCROLL_ENDSCROLL: wx.PyEventBinder

# Command scrolling events with ID
EVT_COMMAND_SCROLL: wx.PyEventBinder
EVT_COMMAND_SCROLL_TOP: wx.PyEventBinder
EVT_COMMAND_SCROLL_BOTTOM: wx.PyEventBinder
EVT_COMMAND_SCROLL_LINEUP: wx.PyEventBinder
EVT_COMMAND_SCROLL_LINEDOWN: wx.PyEventBinder
EVT_COMMAND_SCROLL_PAGEUP: wx.PyEventBinder
EVT_COMMAND_SCROLL_PAGEDOWN: wx.PyEventBinder
EVT_COMMAND_SCROLL_THUMBTRACK: wx.PyEventBinder
EVT_COMMAND_SCROLL_THUMBRELEASE: wx.PyEventBinder
EVT_COMMAND_SCROLL_CHANGED: wx.PyEventBinder
EVT_COMMAND_SCROLL_ENDSCROLL: wx.PyEventBinder

# Control events
EVT_BUTTON: wx.PyEventBinder
EVT_CHECKBOX: wx.PyEventBinder
EVT_CHOICE: wx.PyEventBinder
EVT_LISTBOX: wx.PyEventBinder
EVT_LISTBOX_DCLICK: wx.PyEventBinder
EVT_MENU: wx.PyEventBinder
EVT_MENU_RANGE: wx.PyEventBinder
EVT_SLIDER: wx.PyEventBinder
EVT_RADIOBOX: wx.PyEventBinder
EVT_RADIOBUTTON: wx.PyEventBinder
EVT_SCROLLBAR: wx.PyEventBinder
EVT_VLBOX: wx.PyEventBinder
EVT_COMBOBOX: wx.PyEventBinder
EVT_CHECKLISTBOX: wx.PyEventBinder
EVT_COMBOBOX_DROPDOWN: wx.PyEventBinder
EVT_COMBOBOX_CLOSEUP: wx.PyEventBinder

# Tool and toolbar events
EVT_TOOL: wx.PyEventBinder
EVT_TOOL_RANGE: wx.PyEventBinder
EVT_TOOL_RCLICKED: wx.PyEventBinder
EVT_TOOL_RCLICKED_RANGE: wx.PyEventBinder
EVT_TOOL_ENTER: wx.PyEventBinder
EVT_TOOL_DROPDOWN: wx.PyEventBinder

# Command events
EVT_COMMAND_LEFT_CLICK: wx.PyEventBinder
EVT_COMMAND_LEFT_DCLICK: wx.PyEventBinder
EVT_COMMAND_RIGHT_CLICK: wx.PyEventBinder
EVT_COMMAND_RIGHT_DCLICK: wx.PyEventBinder
EVT_COMMAND_SET_FOCUS: wx.PyEventBinder
EVT_COMMAND_KILL_FOCUS: wx.PyEventBinder
EVT_COMMAND_ENTER: wx.PyEventBinder

# Help events
EVT_HELP: wx.PyEventBinder
EVT_HELP_RANGE: wx.PyEventBinder
EVT_DETAILED_HELP: wx.PyEventBinder
EVT_DETAILED_HELP_RANGE: wx.PyEventBinder

# Application events
EVT_IDLE: wx.PyEventBinder
EVT_UPDATE_UI: wx.PyEventBinder
EVT_UPDATE_UI_RANGE: wx.PyEventBinder
EVT_CONTEXT_MENU: wx.PyEventBinder
EVT_THREAD: wx.PyEventBinder
EVT_WINDOW_MODAL_DIALOG_CLOSED: wx.PyEventBinder

# Joystick events
EVT_JOY_BUTTON_DOWN: wx.PyEventBinder
EVT_JOY_BUTTON_UP: wx.PyEventBinder
EVT_JOY_MOVE: wx.PyEventBinder
EVT_JOY_ZMOVE: wx.PyEventBinder
EVT_JOYSTICK_EVENTS: wx.PyEventBinder

# Gesture and touch events
EVT_GESTURE_PAN: wx.PyEventBinder
EVT_GESTURE_ZOOM: wx.PyEventBinder
EVT_GESTURE_ROTATE: wx.PyEventBinder
EVT_TWO_FINGER_TAP: wx.PyEventBinder
EVT_LONG_PRESS: wx.PyEventBinder
EVT_PRESS_AND_TAP: wx.PyEventBinder

# Clipboard and other events
EVT_CLIPBOARD_CHANGED: wx.PyEventBinder
EVT_FULLSCREEN: wx.PyEventBinder

__all__: list[str]