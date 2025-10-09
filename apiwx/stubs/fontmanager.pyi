"""Type stubs for apiwx.fontmanager module.

This module provides type information for the singleton font management system
for wxPython applications, including centralized font creation, storage, and
retrieval with automatic key generation and multiple access patterns.
"""

from typing import overload, Type
import wx

class FontManager(dict[str, wx.Font]):
    """Singleton font manager for wxPython applications.
    
    Provides centralized font creation and management using a dictionary-based
    storage system with singleton pattern. Fonts are stored with automatically
    generated key names based on their properties.
    """
    
    instance: Type['FontManager'] | None
    font_family: str
    
    def __new__(cls, *args, **kwargs) -> 'FontManager': ...
    
    def __init__(self, font_family: str = ...) -> None: ...
    
    def create_by_parameter(
        self,
        size: int,
        weight: int = ...,
        style: int = ...,
        underline: bool = ...,
        strikethrough: bool = ...
    ) -> str:
        """Create a font with specified parameters and add it to the manager.
        
        Args:
            size: Font size in points.
            weight: Font weight (default: FONTWEIGHT_NORMAL).
            style: Font style (default: FONTSTYLE_NORMAL).
            underline: Whether the font should be underlined (default: False).
            strikethrough: Whether the font should have strikethrough (default: False).
            
        Returns:
            The key name of the created font.
        """
        ...
    
    def create_by_keyname(self, keyname: str) -> str:
        """Create a font by parsing a key name string and add it to the manager.
        
        Args:
            keyname: Key name string in the format 
                {size}_{weight}_{style}_{underline}_{strikethrough}.
                
        Returns:
            The key name of the created font (same as input keyname).
            
        Raises:
            ValueError: If the key name format is invalid.
        """
        ...
    
    def create(self, *args) -> str:
        """Create a font using flexible argument patterns.
        
        Args:
            *args: Variable arguments for either key name or parameters.
            
        Returns:
            The key name of the created font.
            
        Raises:
            ValueError: If arguments are invalid.
        """
        ...
    
    def __getitem__(self, arg: str | tuple[int, ...]) -> wx.Font:
        """Retrieve or create a font using flexible key patterns.
        
        Args:
            arg: Either a string key name or tuple of parameters.
            
        Returns:
            The wx.Font object corresponding to the specified key or parameters.
            
        Raises:
            ValueError: If the argument format is invalid.
        """
        ...
    
    @classmethod
    def parameter_to_keyname(
        cls,
        size: int,
        weight: int = ...,
        style: int = ...,
        underline: bool = ...,
        strikethrough: bool = ...
    ) -> str:
        """Convert font parameters to a standardized key name string.
        
        Args:
            size: Font size in points.
            weight: Font weight (default: FONTWEIGHT_NORMAL).
            style: Font style (default: FONTSTYLE_NORMAL).
            underline: Whether the font should be underlined (default: False).
            strikethrough: Whether the font should have strikethrough (default: False).
            
        Returns:
            A key name string in the format
            {size}_{weight}_{style}_{underline}_{strikethrough}.
        """
        ...
    
    @staticmethod
    @overload
    def create_font(
        size: int,
        weight: int = ...,
        style: int = ...,
        underline: bool = ...,
        strikethrough: bool = ...
    ) -> str: ...
    
    @staticmethod
    @overload
    def create_font(keyname: str) -> str: ...
    
    @staticmethod
    def create_font(*args) -> str:
        """Create a font using the singleton FontManager instance.
        
        Args:
            *args: Variable arguments for either key name or parameters.
            
        Returns:
            The key name of the created font.
            
        Raises:
            ValueError: If arguments are invalid.
        """
        ...
    
    @staticmethod
    @overload
    def get_font(
        size: int,
        weight: int = ...,
        style: int = ...,
        underline: bool = ...,
        strikethrough: bool = ...
    ) -> wx.Font: ...
    
    @staticmethod
    @overload
    def get_font(keyname: str) -> wx.Font: ...
    
    @staticmethod
    def get_font(*args) -> wx.Font:
        """Retrieve a font from the singleton FontManager instance.
        
        Args:
            *args: Variable arguments for either key name or parameters.
            
        Returns:
            The wx.Font object corresponding to the specified parameters or key name.
            
        Raises:
            ValueError: If arguments are invalid.
        """
        ...
    
    @classmethod
    def getkey_from_font(cls, font: wx.Font) -> str:
        """Extract or generate a key name from a wx.Font object.
        
        Args:
            font: The wx.Font object to get the key name from.
            
        Returns:
            The key name string corresponding to the font properties.
        """
        ...

__all__: list[str]