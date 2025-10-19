""" Event Control Signals Module
    This module defines various classes that encapsulate wxPython event constants
    related to different categories of events such as geometry changes, lifecycle events,
    painting, keyboard input, menu operations, focus changes, activation, system events,
    mouse operations, scroll events, control events, and toolbar events.
    
    Each class contains class variables that map to specific wxPython event constants,
    providing a structured way to access these events in an organized manner.

    Classes:
    - GeometryEventSignal: Events related to window geometry changes.
    - LifecycleEventSignal: Events related to window and application lifecycle.
    - PaintEventSignal: Events related to painting and drawing.
    - KeyboardEventSignal: Events related to keyboard input.
    - MenuEventSignal: Events related to menu operations.
    - FocusEventSignal: Events related to focus changes.
    - ActivationEventSignal: Events related to window and application activation.
    - SystemEventSignal: Events related to system power state changes.
    - MouseEventSignal: Events related to mouse operations.
    - ScrollEventSignal: Events related to scroll operations.
    - ControlEventSignal: Events related to control operations.
    - ToolbarEventSignal: Events related to toolbar operations.
    - MiscEventSignal: Miscellaneous events not covered by other categories.
"""

from typing import (
    Dict, Union, Literal, Callable
)

import wx as _wx


class GeometryEventSignal:
    """Contains wxPython event constants related to window geometry changes.
       Each variable maps to a wxPython event for resizing or moving windows.
       
       Members:
        ``EVT_SIZE`` ... Triggered when the window size changes.
        ``EVT_SIZING`` ... Triggered while the window is being resized (during drag).
        ``EVT_MOVE`` ... Triggered when the window position changes.
        ``EVT_MOVING`` ... Triggered while the window is being moved (during drag).
        ``EVT_MOVE_START`` ... Triggered when window movement starts.
        ``EVT_MOVE_END`` ... Triggered when window movement ends.
    """
    
    EVT_SIZE = _wx.EVT_SIZE
    EVT_SIZING = _wx.EVT_SIZING
    EVT_MOVE = _wx.EVT_MOVE
    EVT_MOVING = _wx.EVT_MOVING
    EVT_MOVE_START = _wx.EVT_MOVE_START
    EVT_MOVE_END = _wx.EVT_MOVE_END


class LifecycleEventSignal:
    """Contains wxPython event constants related to window and application lifecycle.
       Each variable maps to a wxPython event for creation, closing, showing, or session changes.
       
       Members:
        ``EVT_CLOSE`` ... Triggered just before a window is closed.
        ``EVT_END_SESSION`` ... Triggered when the user session is ending (e.g., OS shutdown).
        ``EVT_QUERY_END_SESSION`` ... Triggered to query before session ends.
        ``EVT_INIT_DIALOG`` ... Triggered when a dialog is initialized.
        ``EVT_SHOW`` ... Triggered when a window is shown or hidden.
        ``EVT_MAXIMIZE`` ... Triggered when a window is maximized.
        ``EVT_ICONIZE`` ... Triggered when a window is minimized.
        ``EVT_IDLE`` ... Triggered when the application is idle.
        ``EVT_UPDATE_UI`` ... Triggered when UI elements need to be updated.
        ``EVT_UPDATE_UI_RANGE`` ... Triggered when a range of UI elements need to be updated.
        ``EVT_CONTEXT_MENU`` ... Triggered when a context menu is requested.
        ``EVT_THREAD`` ... Triggered for thread-related events.
        ``EVT_WINDOW_MODAL_DIALOG_CLOSED`` ... Triggered when a modal dialog is closed.
    """

    EVT_CLOSE = _wx.EVT_CLOSE
    EVT_END_SESSION = _wx.EVT_END_SESSION
    EVT_QUERY_END_SESSION = _wx.EVT_QUERY_END_SESSION
    EVT_INIT_DIALOG = _wx.EVT_INIT_DIALOG
    EVT_SHOW = _wx.EVT_SHOW
    EVT_MAXIMIZE = _wx.EVT_MAXIMIZE
    EVT_ICONIZE = _wx.EVT_ICONIZE

    # Application events
    EVT_IDLE = _wx.EVT_IDLE
    EVT_UPDATE_UI = _wx.EVT_UPDATE_UI
    EVT_UPDATE_UI_RANGE = _wx.EVT_UPDATE_UI_RANGE
    EVT_CONTEXT_MENU = _wx.EVT_CONTEXT_MENU
    EVT_THREAD = _wx.EVT_THREAD
    EVT_WINDOW_MODAL_DIALOG_CLOSED = _wx.EVT_WINDOW_MODAL_DIALOG_CLOSED


class PaintEventSignal:
    """Contains wxPython event constants related to painting and drawing.
       Each variable maps to a wxPython event for repainting windows or controls.
       
       Members:
        ``EVT_PAINT`` ... Triggered when a window or control needs to be repainted.
        ``EVT_NC_PAINT`` ... Triggered when the non-client area (window frame, etc.) needs repainting.
        ``EVT_ERASE_BACKGROUND`` ... Triggered when the background needs to be erased before painting.
    """
    EVT_PAINT = _wx.EVT_PAINT
    EVT_NC_PAINT = _wx.EVT_NC_PAINT
    EVT_ERASE_BACKGROUND = _wx.EVT_ERASE_BACKGROUND


class KeyboardEventSignal:
    """Contains wxPython event constants related to keyboard input.
       Each variable maps to a wxPython event for key presses and character input.
       
       Members:
        ``EVT_CHAR`` ... Triggered when a character key is pressed.
        ``EVT_KEY_DOWN`` ... Triggered when any key is pressed down.
        ``EVT_KEY_UP`` ... Triggered when any key is released.
        ``EVT_HOTKEY`` ... Triggered when a registered hotkey is pressed.
        ``EVT_CHAR_HOOK`` ... Triggered for character input hooks (special key handling).
    """
    
    EVT_CHAR = _wx.EVT_CHAR
    EVT_KEY_DOWN = _wx.EVT_KEY_DOWN
    EVT_KEY_UP = _wx.EVT_KEY_UP
    EVT_HOTKEY = _wx.EVT_HOTKEY
    EVT_CHAR_HOOK = _wx.EVT_CHAR_HOOK


class MenuEventSignal:
    """Contains wxPython event constants related to menu operations.
       Each variable maps to a wxPython event for menu opening, closing, or highlighting.
       
       Members:
        ``EVT_MENU_OPEN`` ... Triggered when a menu is opened.
        ``EVT_MENU_CLOSE`` ... Triggered when a menu is closed.
        ``EVT_MENU_HIGHLIGHT`` ... Triggered when a menu item is highlighted.
        ``EVT_MENU_HIGHLIGHT_ALL`` ... Triggered when all menu items are highlighted.
    """
    
    EVT_MENU_OPEN = _wx.EVT_MENU_OPEN
    EVT_MENU_CLOSE = _wx.EVT_MENU_CLOSE
    EVT_MENU_HIGHLIGHT = _wx.EVT_MENU_HIGHLIGHT
    EVT_MENU_HIGHLIGHT_ALL = _wx.EVT_MENU_HIGHLIGHT_ALL


class FocusEventSignal:
    """Contains wxPython event constants related to focus changes.
       Each variable maps to a wxPython event for gaining or losing focus.
       
       Members:
        ``EVT_SET_FOCUS`` ... Triggered when a control receives focus.
        ``EVT_KILL_FOCUS`` ... Triggered when a control loses focus.
        ``EVT_CHILD_FOCUS`` ... Triggered when a child control receives focus.
    """
    
    EVT_SET_FOCUS = _wx.EVT_SET_FOCUS
    EVT_KILL_FOCUS = _wx.EVT_KILL_FOCUS
    EVT_CHILD_FOCUS = _wx.EVT_CHILD_FOCUS


class ActivationEventSignal:
    """Contains wxPython event constants related to window and application activation.
       Each variable maps to a wxPython event for activation or hibernation.
       
       Members:
        ``EVT_ACTIVATE`` ... Triggered when a window becomes active or inactive.
        ``EVT_ACTIVATE_APP`` ... Triggered when the application becomes active or inactive.
        ``EVT_HIBERNATE`` ... Triggered when the application enters hibernation.
    """
    
    EVT_ACTIVATE = _wx.EVT_ACTIVATE
    EVT_ACTIVATE_APP = _wx.EVT_ACTIVATE_APP
    EVT_HIBERNATE = _wx.EVT_HIBERNATE


class SystemEventSignal:
    """Contains wxPython event constants related to system power state changes.
       Each variable maps to a wxPython event for suspend or resume actions.
       
       Members:
        ``EVT_POWER_SUSPENDING`` ... Triggered when the system is about to suspend.
        ``EVT_POWER_SUSPENDED`` ... Triggered when the system has entered suspended state.
    """
     
    EVT_POWER_SUSPENDING = _wx.EVT_POWER_SUSPENDING
    EVT_POWER_SUSPENDED = _wx.EVT_POWER_SUSPENDED


class MouseEventSignal:
    """Contains wxPython event constants related to mouse operations.
       Each variable maps to a wxPython event for mouse clicks, movement, wheel, and auxiliary buttons.
       
       Members:
        ``EVT_LEFT_DCLICK`` ... Triggered on left mouse button double-click.
        ``EVT_MIDDLE_DCLICK`` ... Triggered on middle mouse button double-click.
        ``EVT_RIGHT_DCLICK`` ... Triggered on right mouse button double-click.
        ``EVT_LEAVE_WINDOW`` ... Triggered when the mouse leaves the window area.
        ``EVT_ENTER_WINDOW`` ... Triggered when the mouse enters the window area.
        ``EVT_MOUSEWHEEL`` ... Triggered when the mouse wheel is rotated.
        ``EVT_MOUSE_AUX1_DOWN`` ... Triggered when auxiliary mouse button 1 is pressed.
        ``EVT_MOUSE_AUX1_UP`` ... Triggered when auxiliary mouse button 1 is released.
        ``EVT_MOUSE_AUX1_DCLICK`` ... Triggered on auxiliary mouse button 1 double-click.
        ``EVT_MOUSE_AUX2_DOWN`` ... Triggered when auxiliary mouse button 2 is pressed.
        ``EVT_MOUSE_AUX2_UP`` ... Triggered when auxiliary mouse button 2 is released.
        ``EVT_MOUSE_AUX2_DCLICK`` ... Triggered on auxiliary mouse button 2 double-click.
        ``EVT_MOUSE_EVENTS`` ... Triggered for all mouse events.
        ``EVT_MAGNIFY`` ... Triggered for magnification gestures.
        ``EVT_COMMAND_LEFT_CLICK`` ... Triggered on command left click.
        ``EVT_COMMAND_LEFT_DCLICK`` ... Triggered on command left double-click.
        ``EVT_COMMAND_RIGHT_CLICK`` ... Triggered on command right click.
        ``EVT_COMMAND_RIGHT_DCLICK`` ... Triggered on command right double-click.
        ``EVT_COMMAND_SET_FOCUS`` ... Triggered when command sets focus.
        ``EVT_COMMAND_KILL_FOCUS`` ... Triggered when command kills focus.
        ``EVT_COMMAND_ENTER`` ... Triggered when command enter is pressed.
        ``EVT_SET_CURSOR`` ... Triggered when the mouse cursor changes.
        ``EVT_MOUSE_CAPTURE_CHANGED`` ... Triggered when mouse capture changes.
        ``EVT_MOUSE_CAPTURE_LOST`` ... Triggered when mouse capture is lost.
    """
    
    # Mouse button events
    EVT_LEFT_DOWN = _wx.EVT_LEFT_DOWN
    EVT_LEFT_UP = _wx.EVT_LEFT_UP
    EVT_MIDDLE_DOWN = _wx.EVT_MIDDLE_DOWN
    EVT_MIDDLE_UP = _wx.EVT_MIDDLE_UP
    EVT_RIGHT_DOWN = _wx.EVT_RIGHT_DOWN
    EVT_RIGHT_UP = _wx.EVT_RIGHT_UP
    EVT_MOTION = _wx.EVT_MOTION
    EVT_LEFT_DCLICK = _wx.EVT_LEFT_DCLICK
    EVT_MIDDLE_DCLICK = _wx.EVT_MIDDLE_DCLICK
    EVT_RIGHT_DCLICK = _wx.EVT_RIGHT_DCLICK
    EVT_LEAVE_WINDOW = _wx.EVT_LEAVE_WINDOW
    EVT_ENTER_WINDOW = _wx.EVT_ENTER_WINDOW
    EVT_MOUSEWHEEL = _wx.EVT_MOUSEWHEEL

    # Auxiliary mouse button events
    EVT_MOUSE_AUX1_DOWN = _wx.EVT_MOUSE_AUX1_DOWN
    EVT_MOUSE_AUX1_UP = _wx.EVT_MOUSE_AUX1_UP
    EVT_MOUSE_AUX1_DCLICK = _wx.EVT_MOUSE_AUX1_DCLICK
    EVT_MOUSE_AUX2_DOWN = _wx.EVT_MOUSE_AUX2_DOWN
    EVT_MOUSE_AUX2_UP = _wx.EVT_MOUSE_AUX2_UP
    EVT_MOUSE_AUX2_DCLICK = _wx.EVT_MOUSE_AUX2_DCLICK
    EVT_MOUSE_EVENTS = _wx.EVT_MOUSE_EVENTS
    EVT_MAGNIFY = _wx.EVT_MAGNIFY

    # Command events
    EVT_COMMAND_LEFT_CLICK = _wx.EVT_COMMAND_LEFT_CLICK,
    EVT_COMMAND_LEFT_DCLICK = _wx.EVT_COMMAND_LEFT_DCLICK,
    EVT_COMMAND_RIGHT_CLICK = _wx.EVT_COMMAND_RIGHT_CLICK,
    EVT_COMMAND_RIGHT_DCLICK = _wx.EVT_COMMAND_RIGHT_DCLICK,
    EVT_COMMAND_SET_FOCUS = _wx.EVT_COMMAND_SET_FOCUS,
    EVT_COMMAND_KILL_FOCUS = _wx.EVT_COMMAND_KILL_FOCUS,
    EVT_COMMAND_ENTER = _wx.EVT_COMMAND_ENTER,

    # Mouse cursor and capture events
    EVT_SET_CURSOR = _wx.EVT_SET_CURSOR,
    EVT_MOUSE_CAPTURE_CHANGED = _wx.EVT_MOUSE_CAPTURE_CHANGED,
    EVT_MOUSE_CAPTURE_LOST = _wx.EVT_MOUSE_CAPTURE_LOST,


class ScrollEventSignal:
    """Contains wxPython event constants related to scroll operations.
       Each variable maps to a wxPython event for scrolling windows or controls.
       
       Members:
        ``EVT_SCROLLWIN`` ... Triggered when the window is scrolled.
        ``EVT_SCROLL`` ... Triggered when a scrollbar is operated.
        ``EVT_COMMAND_SCROLL`` ... Triggered for command scroll events with control ID.
        Other variables represent events for specific scroll positions or actions.
    """

    # Scrolling events from wxWindow (sent to wxScrolledWindow
    EVT_SCROLLWIN = _wx.EVT_SCROLLWIN
    EVT_SCROLLWIN_TOP = _wx.EVT_SCROLLWIN_TOP
    EVT_SCROLLWIN_BOTTOM = _wx.EVT_SCROLLWIN_BOTTOM
    EVT_SCROLLWIN_LINEUP = _wx.EVT_SCROLLWIN_LINEUP
    EVT_SCROLLWIN_LINEDOWN = _wx.EVT_SCROLLWIN_LINEDOWN
    EVT_SCROLLWIN_PAGEUP = _wx.EVT_SCROLLWIN_PAGEUP
    EVT_SCROLLWIN_PAGEDOWN = _wx.EVT_SCROLLWIN_PAGEDOWN
    EVT_SCROLLWIN_THUMBTRACK = _wx.EVT_SCROLLWIN_THUMBTRACK
    EVT_SCROLLWIN_THUMBRELEASE = _wx.EVT_SCROLLWIN_THUMBRELEASE

    EVT_SCROLL = _wx.EVT_SCROLL
    EVT_SCROLL_TOP = _wx.EVT_SCROLL_TOP
    EVT_SCROLL_BOTTOM = _wx.EVT_SCROLL_BOTTOM
    EVT_SCROLL_LINEUP = _wx.EVT_SCROLL_LINEUP
    EVT_SCROLL_LINEDOWN = _wx.EVT_SCROLL_LINEDOWN
    EVT_SCROLL_PAGEUP = _wx.EVT_SCROLL_PAGEUP
    EVT_SCROLL_PAGEDOWN = _wx.EVT_SCROLL_PAGEDOWN
    EVT_SCROLL_THUMBTRACK = _wx.EVT_SCROLL_THUMBTRACK
    EVT_SCROLL_THUMBRELEASE = _wx.EVT_SCROLL_THUMBRELEASE
    EVT_SCROLL_CHANGED = _wx.EVT_SCROLL_CHANGED
    EVT_SCROLL_ENDSCROLL = _wx.EVT_SCROLL_ENDSCROLL

    # Command scrolling events with ID
    EVT_COMMAND_SCROLL = _wx.EVT_COMMAND_SCROLL
    EVT_COMMAND_SCROLL_TOP = _wx.EVT_COMMAND_SCROLL_TOP
    EVT_COMMAND_SCROLL_BOTTOM = _wx.EVT_COMMAND_SCROLL_BOTTOM
    EVT_COMMAND_SCROLL_LINEUP = _wx.EVT_COMMAND_SCROLL_LINEUP
    EVT_COMMAND_SCROLL_LINEDOWN = _wx.EVT_COMMAND_SCROLL_LINEDOWN
    EVT_COMMAND_SCROLL_PAGEUP = _wx.EVT_COMMAND_SCROLL_PAGEUP
    EVT_COMMAND_SCROLL_PAGEDOWN = _wx.EVT_COMMAND_SCROLL_PAGEDOWN
    EVT_COMMAND_SCROLL_THUMBTRACK = _wx.EVT_COMMAND_SCROLL_THUMBTRACK
    EVT_COMMAND_SCROLL_THUMBRELEASE = _wx.EVT_COMMAND_SCROLL_THUMBRELEASE
    EVT_COMMAND_SCROLL_CHANGED = _wx.EVT_COMMAND_SCROLL_CHANGED
    EVT_COMMAND_SCROLL_ENDSCROLL = _wx.EVT_COMMAND_SCROLL_ENDSCROLL


class ControlEventSignal:
    """Contains wxPython event constants related to control operations.
       Each variable maps to a wxPython event for button, checkbox, listbox, menu, slider, radio, and combobox actions.
       
       Members:
        ``EVT_BUTTON`` ... Triggered when a button is clicked.
        ``EVT_CHECKBOX`` ... Triggered when a checkbox state changes.
        ``EVT_CHOICE`` ... Triggered when a choice selection changes.
        ``EVT_LISTBOX`` ... Triggered when a listbox selection changes.
        ``EVT_LISTBOX_DCLICK`` ... Triggered on listbox item double-click.
        ``EVT_MENU`` ... Triggered when a menu item is selected.
        ``EVT_MENU_RANGE`` ... Triggered when a range of menu items is selected.
        ``EVT_SLIDER`` ... Triggered when a slider value changes.
        ``EVT_RADIOBOX`` ... Triggered when a radiobox selection changes.
        ``EVT_RADIOBUTTON`` ... Triggered when a radiobutton selection changes.
        ``EVT_SCROLLBAR`` ... Triggered when a scrollbar is operated.
        ``EVT_VLBOX`` ... Triggered for virtual listbox events.
        ``EVT_COMBOBOX`` ... Triggered when a combobox selection changes.
        ``EVT_CHECKLISTBOX`` ... Triggered when a checklistbox state changes.
        ``EVT_COMBOBOX_DROPDOWN`` ... Triggered when a combobox dropdown is shown.
        ``EVT_COMBOBOX_CLOSEUP`` ... Triggered when a combobox dropdown is closed.
    """

    EVT_BUTTON = _wx.EVT_BUTTON
    EVT_CHECKBOX = _wx.EVT_CHECKBOX
    EVT_CHOICE = _wx.EVT_CHOICE
    EVT_LISTBOX = _wx.EVT_LISTBOX
    EVT_LISTBOX_DCLICK = _wx.EVT_LISTBOX_DCLICK
    EVT_MENU = _wx.EVT_MENU
    EVT_MENU_RANGE = _wx.EVT_MENU_RANGE
    EVT_SLIDER = _wx.EVT_SLIDER
    EVT_RADIOBOX = _wx.EVT_RADIOBOX
    EVT_RADIOBUTTON = _wx.EVT_RADIOBUTTON
    EVT_SCROLLBAR = _wx.EVT_SCROLLBAR
    EVT_VLBOX = _wx.EVT_VLBOX
    EVT_COMBOBOX = _wx.EVT_COMBOBOX
    EVT_CHECKLISTBOX = _wx.EVT_CHECKLISTBOX
    EVT_COMBOBOX_DROPDOWN = _wx.EVT_COMBOBOX_DROPDOWN
    EVT_COMBOBOX_CLOSEUP = _wx.EVT_COMBOBOX_CLOSEUP


class ToolbarEventSignal:
    """Contains wxPython event constants related to toolbar operations.
       Each variable maps to a wxPython event for toolbar tool clicks, dropdowns, and mouse actions.
       
       Members:
        ``EVT_TOOL`` ... Triggered when a toolbar tool is clicked.
        ``EVT_TOOL_RANGE`` ... Triggered when a range of toolbar tools is clicked.
        ``EVT_TOOL_RCLICKED`` ... Triggered when a toolbar tool is right-clicked.
        ``EVT_TOOL_RCLICKED_RANGE`` ... Triggered when a range of toolbar tools is right-clicked.
        ``EVT_TOOL_ENTER`` ... Triggered when the mouse enters a toolbar tool.
        ``EVT_TOOL_DROPDOWN`` ... Triggered when a toolbar dropdown is shown.
    """
    
    # Tool and toolbar events
    EVT_TOOL = _wx.EVT_TOOL
    EVT_TOOL_RANGE = _wx.EVT_TOOL_RANGE
    EVT_TOOL_RCLICKED = _wx.EVT_TOOL_RCLICKED
    EVT_TOOL_RCLICKED_RANGE = _wx.EVT_TOOL_RCLICKED_RANGE
    EVT_TOOL_ENTER = _wx.EVT_TOOL_ENTER
    EVT_TOOL_DROPDOWN = _wx.EVT_TOOL_DROPDOWN


class JoystickEventSignal:
    """Contains wxPython event constants related to joystick operations.
       Each variable maps to a wxPython event for joystick button and movement actions.
       
       Members:
        ``EVT_JOY_BUTTON_DOWN`` ... Triggered when a joystick button is pressed.
        ``EVT_JOY_BUTTON_UP`` ... Triggered when a joystick button is released.
        ``EVT_JOY_MOVE`` ... Triggered when the joystick is moved.
        ``EVT_JOY_ZMOVE`` ... Triggered when the joystick Z-axis is moved.
        ``EVT_JOYSTICK_EVENTS`` ... Triggered for all joystick events.
    """
    
    EVT_JOY_BUTTON_DOWN = _wx.EVT_JOY_BUTTON_DOWN
    EVT_JOY_BUTTON_UP = _wx.EVT_JOY_BUTTON_UP
    EVT_JOY_MOVE = _wx.EVT_JOY_MOVE
    EVT_JOY_ZMOVE = _wx.EVT_JOY_ZMOVE
    EVT_JOYSTICK_EVENTS = _wx.EVT_JOYSTICK_EVENTS


class MiscEventSignal:
    """Contains wxPython event constants for miscellaneous operations.
       Each variable maps to a wxPython event for file drops, system changes, help requests, gestures, and clipboard actions.
       
       Members:
        ``EVT_DROP_FILES`` ... Triggered when files are dropped onto a window.
        ``EVT_SYS_COLOUR_CHANGED`` ... Triggered when system colors change.
        ``EVT_DISPLAY_CHANGED`` ... Triggered when display configuration changes.
        ``EVT_DPI_CHANGED`` ... Triggered when DPI settings change.
        ``EVT_NAVIGATION_KEY`` ... Triggered when navigation keys (e.g., Tab) are used.
        ``EVT_PALETTE_CHANGED`` ... Triggered when the palette changes.
        ``EVT_QUERY_NEW_PALETTE`` ... Triggered when querying for a new palette.
        ``EVT_WINDOW_CREATE`` ... Triggered when a window is created.
        ``EVT_WINDOW_DESTROY`` ... Triggered when a window is destroyed.
        ``EVT_HELP`` ... Triggered when help is requested.
        ``EVT_HELP_RANGE`` ... Triggered when help is requested for a range of controls.
        ``EVT_DETAILED_HELP`` ... Triggered when detailed help is requested.
        ``EVT_DETAILED_HELP_RANGE`` ... Triggered when detailed help is requested for a range.
        ``EVT_GESTURE_PAN`` ... Triggered for pan gesture events.
        ``EVT_GESTURE_ZOOM`` ... Triggered for zoom gesture events.
        ``EVT_GESTURE_ROTATE`` ... Triggered for rotate gesture events.
        ``EVT_TWO_FINGER_TAP`` ... Triggered for two-finger tap gesture events.
        ``EVT_LONG_PRESS`` ... Triggered for long press gesture events.
        ``EVT_PRESS_AND_TAP`` ... Triggered for press-and-tap gesture events.
        ``EVT_CLIPBOARD_CHANGED`` ... Triggered when the clipboard content changes.
        ``EVT_FULLSCREEN`` ... Triggered when a window enters fullscreen mode.
    """
    
    # System and display events
    EVT_DROP_FILES = _wx.EVT_DROP_FILES
    EVT_SYS_COLOUR_CHANGED = _wx.EVT_SYS_COLOUR_CHANGED
    EVT_DISPLAY_CHANGED = _wx.EVT_DISPLAY_CHANGED
    EVT_DPI_CHANGED = _wx.EVT_DPI_CHANGED
    EVT_NAVIGATION_KEY = _wx.EVT_NAVIGATION_KEY
    EVT_PALETTE_CHANGED = _wx.EVT_PALETTE_CHANGED
    EVT_QUERY_NEW_PALETTE = _wx.EVT_QUERY_NEW_PALETTE

    # Window creation and destruction
    EVT_WINDOW_CREATE = _wx.EVT_WINDOW_CREATE
    EVT_WINDOW_DESTROY = _wx.EVT_WINDOW_DESTROY

    # Help events
    EVT_HELP = _wx.EVT_HELP
    EVT_HELP_RANGE = _wx.EVT_HELP_RANGE
    EVT_DETAILED_HELP = _wx.EVT_DETAILED_HELP
    EVT_DETAILED_HELP_RANGE = _wx.EVT_DETAILED_HELP_RANGE
    
    # Gesture and touch events
    EVT_GESTURE_PAN = _wx.EVT_GESTURE_PAN
    EVT_GESTURE_ZOOM = _wx.EVT_GESTURE_ZOOM
    EVT_GESTURE_ROTATE = _wx.EVT_GESTURE_ROTATE
    EVT_TWO_FINGER_TAP = _wx.EVT_TWO_FINGER_TAP
    EVT_LONG_PRESS = _wx.EVT_LONG_PRESS
    EVT_PRESS_AND_TAP = _wx.EVT_PRESS_AND_TAP

    # Clipboard and other events
    EVT_CLIPBOARD_CHANGED = _wx.EVT_CLIPBOARD_CHANGED
    EVT_FULLSCREEN = _wx.EVT_FULLSCREEN


class CustomEvent(_wx.PyEventBinder):
    """ A custom event binder that creates a new event type upon instantiation.
    Attributes
    ----------
    event_type : wx.EventType
        The event type associated with this binder.
    expected_ids : Literal[0, 1, 2]
        The expected IDs (of control objects) for this event binder.
    """
    @property
    def event_type(self):
        """  The event type associated with this binder."""
        return self._event_type
    
    @property
    def expected_ids(self):
        """ The expected IDs (of control objects) for this event binder. """
        return self._expected_ids
    

    def __init__(self, expected_ids: Literal[0, 1, 2]=0):
        self._event_type = _wx.NewEventType()
        self._expected_ids = expected_ids

        super().__init__(
            self._event_type,
            self._expected_ids
        )

        self.binded_controls: list[_wx.EvtHandler] = []


    def __del__(self):
        for control in self.binded_controls:
            self.unbind_control(control)
        
        self.binded_controls.clear()

    
    def bind_control(
            self,
            control: _wx.EvtHandler,
            handler: Callable[[_wx.Event], None]=lambda e: None,
            id1: Union[int, None]=None,
            id2: Union[int, None]=None):
        """ Bind this event binder to a control.
        Parameters
        ----------
        control : wx.EvtHandler
            The control to bind this event binder to.
        handler : Callable[[wx.Event], None], optional
            The event handler function to be called when the event is triggered.
            Default is a no-op lambda function.
        """
        ids = ()

        if self.expected_ids >= 1:
            ids += (id1 if id1 is not None else _wx.ID_ANY, )

        if self.expected_ids == 2:
            ids += (id2 if id2 is not None else _wx.ID_ANY, )
        
        if control not in self.binded_controls:
            control.Bind(self, handler, None, *ids)
            self.binded_controls.append(control)


    def unbind_control(self, control: _wx.EvtHandler):
        """ Unbind this event binder from a control.
        Parameters
        ----------
        control : wx.EvtHandler
            The control to unbind this event binder from.
        """
        if control in self.binded_controls:
            control.Unbind(self)
            self.binded_controls.remove(control)


class EventCreatorModel(dict[int, CustomEvent]):
    def __new__(cls):
        if not hasattr(EventCreatorModel, 'instance'):
            EventCreatorModel.instance = super().__new__(cls)

        return EventCreatorModel.instance
    

    def create(self, event_id: int, expected_ids: Literal[0, 1, 2]=0) -> CustomEvent:
        """ Create or retrieve a CustomEvent binder for the given event_id.
        Parameters
        ----------
        event_id : int
            The unique identifier for the custom event.
        expected_ids : Literal[0, 1, 2], optional
            The expected IDs (of control objects) for this event binder. Default is 0.
        Returns
        -------
        CustomEvent
            The CustomEvent binder associated with the given event_id.
        """
        if event_id in self:
            raise ValueError(f"Event ID {event_id} is already registered.")
        
        self[event_id] = CustomEvent(expected_ids)
        
        return self[event_id]
    

    def remove(self, event_id: int):
        """ Remove the CustomEvent binder associated with the given event_id.
        Parameters
        ----------
        event_id : int
            The unique identifier for the custom event to be removed.
        """
        if event_id in self:
            del self[event_id]


    def bind_control(
            self,
            event_id: int,
            control: _wx.EvtHandler,
            handler: Callable[[_wx.Event], None]=lambda e: None,
            id1: Union[int, None]=None,
            id2: Union[int, None]=None):
        """ Bind the CustomEvent binder associated with the given event_id to a control.
        Parameters
        ----------
        event_id : int
            The unique identifier for the custom event.
        control : wx.EvtHandler
            The control to bind the event binder to.
        handler : Callable[[wx.Event], None], optional
            The event handler function to be called when the event is triggered.
            Default is a no-op lambda function.
        """
        if event_id not in self:
            raise ValueError(f"Event ID {event_id} is not registered.")
        
        self[event_id].bind_control(control, handler, id1, id2)

    def unbind_control(
            self,
            event_id: int,
            control: _wx.EvtHandler):
        """ Unbind the CustomEvent binder associated with the given event_id from a control.
        Parameters
        ----------
        event_id : int
            The unique identifier for the custom event.
        control : wx.EvtHandler
            The control to unbind the event binder from.
        """
        if event_id not in self:
            raise ValueError(f"Event ID {event_id} is not registered.")

        self[event_id].unbind_control(control)


class EventControl:
    """ A controller for managing custom events.
    Attributes
    ----------
    event_creators : EventCreatorModel
        The model that manages custom event binders.
    """
    def __init__(self):
        self.event_creators = EventCreatorModel()
    

    def create_event(
            self,
            event_id: int,
            expected_ids: Literal[0, 1, 2]=0) -> CustomEvent:
        """ Create or retrieve a CustomEvent binder for the given event_id.
        Parameters
        ----------
        event_id : int
            The unique identifier for the custom event.
        expected_ids : Literal[0, 1, 2], optional
            The expected IDs (of control objects) for this event binder. Default is 0.
        Returns
        -------
        CustomEvent
            The CustomEvent binder associated with the given event_id.
        """
        return self.event_creators.create(event_id, expected_ids)
    

    def remove_event(self, event_id: int):
        """ Remove the CustomEvent binder associated with the given event_id.
        Parameters
        ----------
        event_id : int
            The unique identifier for the custom event to be removed.
        """
        self.event_creators.remove(event_id)

    
    def bind_event_to_control(
            self,
            event_id: int,
            control: _wx.EvtHandler,
            handler: Callable[[_wx.Event], None]=lambda e: None,
            id1: Union[int, None]=None,
            id2: Union[int, None]=None):
        """ Bind the CustomEvent binder associated with the given event_id to a control.
        Parameters
        ----------
        event_id : int
            The unique identifier for the custom event.
        control : wx.EvtHandler
            The control to bind the event binder to.
        handler : Callable[[wx.Event], None], optional
            The event handler function to be called when the event is triggered.
            Default is a no-op lambda function.
        """
        self.event_creators.bind_control(event_id, control, handler, id1, id2)


    def unbind_event_from_control(
            self,
            event_id: int,
            control: _wx.EvtHandler):
        """ Unbind the CustomEvent binder associated with the given event_id from a control.
        Parameters
        ----------
        event_id : int
            The unique identifier for the custom event.
        control : wx.EvtHandler
            The control to unbind the event binder from.
        """
        self.event_creators.unbind_control(event_id, control)


__all__ = [
    "EventControl",
    "CustomEvent",
    "GeometryEventSignal",
    "LifecycleEventSignal",
    "PaintEventSignal",
    "KeyboardEventSignal",
    "MenuEventSignal",
    "FocusEventSignal",
    "ActivationEventSignal",
    "SystemEventSignal",
    "MouseEventSignal",
    "ScrollEventSignal",
    "ControlEventSignal",
    "ToolbarEventSignal",
    "MiscEventSignal"
]