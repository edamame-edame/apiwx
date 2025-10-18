"""Type stubs for apiwx.paneltransmodel module.

This module provides type information for panel transition management
functionality, enabling smooth panel switching and visibility management
within window containers in wxPython applications.
"""

from typing import Optional
from . import core
from .generics_core import GenericsType
from . import generics_window

class NotTransition:
    """Marker class to exclude panels from transition management.
    
    This class serves as a generic marker to identify panels that should
    not participate in the automatic panel transition system.
    """
    ...

class SupportTransit(generics_window.DetectPanel):
    """Mixin class to add transition support to panels.
    
    This class provides panel transition functionality by automatically
    detecting child panels and managing them through a PanelTransModel
    instance.
    """
    
    _panel_trans: 'PanelTransModel'
    
    @property
    def panel_trans(self) -> 'PanelTransModel':
        """Get the panel transition model.
        
        Returns:
            The transition model managing child panels.
        """
        ...
    
    def __new__(cls, instance, *args, **kwds): ...
    
    def __init__(self, *args, **kwds) -> None:
        """Initialize the transition support."""
        ...

class TransitPanelContainer:
    """Container class for managing panel transitions.
    
    This mixin class provides panel transition management for Window
    or Panel instances by automatically detecting child panels and
    setting up a transition model.
    """
    
    panel_trans: 'PanelTransModel'
    children: dict[core.UIIndexor, core.Panel]
    
    def __init__(self, *args, **kwds) -> None:
        """Initialize the panel container with transition support."""
        ...

class PanelTransModel(dict[core.UIIndexor, core.Panel]):
    """Panel transition model for managing panel visibility.
    
    This class extends dict to provide a mapping between UI indexors and
    wrapped panels, with automatic visibility management. Only one panel
    can be visible at a time.
    """
    
    _now: Optional[core.UIIndexor]
    
    @property
    def now(self) -> Optional[core.UIIndexor]:
        """Get the current panel indexor.
        
        Returns:
            The currently active panel indexor, or None if no panel is active.
        """
        ...
    
    @now.setter
    def now(self, indexor: Optional[core.UIIndexor]) -> None:
        """Set the current panel indexor.
        
        Args:
            indexor: The indexor to set as current, or None to hide all panels.
            
        Raises:
            TypeError: If indexor is not UIIndexor or None.
        """
        ...
    
    @property
    def is_show_any(self) -> bool:
        """Check if any panel is currently shown.
        
        Returns:
            True if a panel is currently visible, False otherwise.
        """
        ...
    
    def __init__(self) -> None:
        """Initialize the panel transition model."""
        ...
    
    def add(self, indexor: core.UIIndexor, panel: core.Panel) -> None:
        """Add a panel with the given indexor.
        
        Args:
            indexor: The unique identifier for the panel.
            panel: The panel to add to the model.
            
        Raises:
            TypeError: If indexor or panel are not of correct type.
            KeyError: If indexor already exists in the model.
        """
        ...
    
    def __setitem__(self, indexor: core.UIIndexor, panel: core.Panel) -> None:
        """Add a panel using dictionary syntax."""
        ...
    
    def remove(self, indexor: core.UIIndexor) -> None:
        """Remove the panel with the given indexor.
        
        Args:
            indexor: The indexor of the panel to remove.
        """
        ...
    
    def trans(self, indexor: core.UIIndexor) -> bool:
        """Transition to the panel with the given indexor.
        
        Args:
            indexor: The indexor of the panel to show.
            
        Returns:
            True if any panel is now visible, False otherwise.
        """
        ...

__all__: list[str]