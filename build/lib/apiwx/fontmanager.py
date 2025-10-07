"""wxPython font management system with singleton pattern.

This module provides the FontManager class, a centralized font creation and
management system for wxPython applications. The FontManager implements a
singleton pattern to ensure consistent font management across the entire
application lifecycle.

Key features:
- Singleton pattern for application-wide font management
- Dictionary-based font storage with automatic key generation
- Multiple font creation methods (parameters, key names)
- Static methods for convenient access without instance management
- Automatic font creation when accessing non-existent fonts

The module is designed to simplify font handling in wxPython applications
by providing a consistent interface for font creation, storage, and retrieval.
"""
import typing

from wx import (
    Font as _Font,
    FontInfo as _FontInfo,
    FONTWEIGHT_NORMAL,
    FONTWEIGHT_BOLD,
    FONTWEIGHT_LIGHT,
    FONTSTYLE_NORMAL,
    FONTSTYLE_ITALIC,
    FONTSTYLE_SLANT,
)


class FontManager(dict[str, _Font]):
    """Singleton font manager for wxPython applications.

    FontManager provides centralized font creation and management using a
    dictionary-based storage system. It implements the singleton pattern to
    ensure a single instance manages all fonts throughout the application.
    Fonts are stored with automatically generated key names based on their
    properties, enabling efficient reuse and management.

    The class extends dict[str, wx.Font] and provides multiple creation 
    methods:
    - Parameter-based creation with automatic key generation
    - Key name-based creation for explicit font specification
    - Static methods for convenient access without instance management

    Key name format: ``{size}_{weight}_{style}_{underline}_{strikethrough}``

    Attributes:
        instance: Class variable holding the singleton instance.
        font_family: Default font family name for all created fonts.

    Example:
        >>> # Initialize with default font family
        >>> mgr = FontManager('MS UI Gothic')
        >>> 
        >>> # Create fonts using different methods
        >>> key1 = mgr.create_by_parameter(12, weight=FONTWEIGHT_BOLD)
        >>> key2 = mgr.create_by_keyname("14_400_1_0_0")  # Italic font
        >>> 
        >>> # Access fonts
        >>> font = mgr[key1]
        >>> label = wx.StaticText(parent, label="Sample Text")
        >>> label.SetFont(font)
        >>> 
        >>> # Use static methods for convenience
        >>> font = FontManager.get_font(16, style=FONTSTYLE_ITALIC)
        >>> button.SetFont(font)
    """
    instance: typing.Type['FontManager'] | None = None


    def __new__(cls, *args, **kwargs):
        if FontManager.instance is None:
            FontManager.instance = super().__new__(cls)

        return FontManager.instance


    def __init__(self, font_family: str = "MS UI Gothic"):
        # Init base dict class
        super().__init__()
        # Set font family
        self.font_family = font_family


    def create_by_parameter(
        self,
        size: int,
        weight: int = FONTWEIGHT_NORMAL,
        style: int = FONTSTYLE_NORMAL,
        underline: bool = False,
        strikethrough: bool = False) -> str:
        """Create a font with specified parameters and add it to the manager.

        This method creates a new font using the provided parameters and stores
        it in the manager with an automatically generated key name. If a font
        with the same parameters already exists, it will be overwritten.

        Args:
            size: Font size in points.
            weight: Font weight (default: FONTWEIGHT_NORMAL).
            style: Font style (default: FONTSTYLE_NORMAL).
            underline: Whether the font should be underlined (default: False).
            strikethrough: Whether the font should have strikethrough 
                (default: False).

        Returns:
            The key name of the created font in the format
            ``{size}_{weight}_{style}_{underline}_{strikethrough}``.

        Example:
            >>> mgr = FontManager()
            >>> key = mgr.create_by_parameter(12)  # Normal font
            >>> key = mgr.create_by_parameter(
            ...     12, weight=FONTWEIGHT_BOLD)  # Bold font
            >>> key = mgr.create_by_parameter(
            ...     12, style=FONTSTYLE_ITALIC)  # Italic font
        """

        # Create font info
        fontinfo = _FontInfo(size)
        fontinfo.FaceName(self.font_family)
        fontinfo.Weight(weight)
        fontinfo.Style(style)
        fontinfo.Underlined(underline)
        fontinfo.Strikethrough(strikethrough)

        # Create font
        font = _Font(fontinfo)

        # Create key name
        keyname = (
            f"{size}_{weight}_{style}_{int(underline)}_{int(strikethrough)}"
        )

        # Add to manager
        self[keyname] = font

        # Return key name
        return keyname


    def create_by_keyname(self, keyname: str) -> str:
        """Create a font by parsing a key name string and add it to the 
        manager.

        This method parses a key name in the format 
        ``{size}_{weight}_{style}_{underline}_{strikethrough}`` and creates
        a corresponding font. The created font is stored in the manager.

        Args:
            keyname: Key name string in the format 
                ``{size}_{weight}_{style}_{underline}_{strikethrough}``.
                All components must be valid integers, with underline and
                strikethrough as 0 or 1.

        Returns:
            The key name of the created font (same as input keyname).

        Raises:
            ValueError: If the key name format is invalid or contains
                non-integer values.

        Example:
            >>> mgr = FontManager()
            >>> key = mgr.create_by_keyname("12_400_0_0_0")  # Normal font
            >>> key = mgr.create_by_keyname("12_700_0_0_0")  # Bold font
            >>> key = mgr.create_by_keyname("12_400_1_0_0")  # Italic font
        """

        # Split key name
        params = keyname.split("_")

        if len(params) != 5:
            raise ValueError("Invalid key name format")

        try:
            size = int(params[0])
            weight = int(params[1])
            style = int(params[2])
            underline = bool(int(params[3]))
            strikethrough = bool(int(params[4]))

        except Exception as e:
            raise ValueError("Invalid key name format") from e

        return self.create_by_parameter(
            size, weight, style, underline, strikethrough
        )


    def create(self, *args):
        """Create a font using flexible argument patterns.

        This method provides a unified interface for font creation that 
        supports both parameter-based and key name-based creation patterns. 
        It delegates to the appropriate specific creation method based on the 
        argument types.

        Args:
            *args: Variable arguments that can be either
                - A single string: key name in format 
                  ``{size}_{weight}_{style}_{underline}_{strikethrough}``
                - Multiple parameters: size (int), weight (int, optional), 
                  style (int, optional), underline (bool, optional), 
                  strikethrough (bool, optional)

        Returns:
            The key name of the created font.

        Raises:
            ValueError: If arguments are invalid or do not match expected 
                patterns.

        Example:
            >>> mgr = FontManager()
            >>> # Create by parameters
            >>> key1 = mgr.create(12, FONTWEIGHT_BOLD)
            >>> # Create by key name
            >>> key2 = mgr.create("14_400_1_0_0")
        """
        if len(args) == 1 and isinstance(args[0], str):
            return self.create_by_keyname(args[0])

        elif len(args) >= 1 and isinstance(args[0], int):
            return self.create_by_parameter(*args)

        else:
            raise ValueError("Invalid arguments")


    def __getitem__(self, arg: str | tuple[int, ...]) -> _Font:
        """Retrieve or create a font using flexible key patterns.

        This method overrides the dictionary's __getitem__ to support both
        string keys and parameter-based access. If the requested font does not
        exist, it will be automatically created and added to the manager.

        Args:
            arg: Can be either
                - A string: key name in format 
                  ``{size}_{weight}_{style}_{underline}_{strikethrough}``
                - A tuple of parameters: 
                  (size, weight, style, underline, strikethrough)

        Returns:
            The wx.Font object corresponding to the specified key or 
            parameters.

        Raises:
            ValueError: If the argument format is invalid.

        Example:
            >>> mgr = FontManager()
            >>> # Access by key name
            >>> font1 = mgr["12_400_0_0_0"]
            >>> # Access by parameters (if implemented)
            >>> # font2 = mgr[(12, FONTWEIGHT_BOLD, FONTSTYLE_NORMAL, 
            >>> #               False, False)]
        """

        if isinstance(arg, str):
            key = arg

        elif isinstance(arg, tuple):
            key = self.parameter_to_keyname(*arg)

        else:
            raise ValueError("Invalid arguments")

        # If font not exist
        if key not in self:
            # Create font if not exist
            self.create_by_keyname(key)

        # Return font
        return super().__getitem__(key)
    

    @classmethod
    def parameter_to_keyname(
        cls,
        size: int,
        weight: int = FONTWEIGHT_NORMAL,
        style: int = FONTSTYLE_NORMAL,
        underline: bool = False,
        strikethrough: bool = False) -> str:
        """Convert font parameters to a standardized key name string.

        This class method generates a standardized key name string from font
        parameters without creating an actual font object. The generated key
        can be used for font identification and storage.

        Args:
            size: Font size in points.
            weight: Font weight (default: FONTWEIGHT_NORMAL).
            style: Font style (default: FONTSTYLE_NORMAL).
            underline: Whether the font should be underlined (default: False).
            strikethrough: Whether the font should have strikethrough 
                (default: False).

        Returns:
            A key name string in the format
            ``{size}_{weight}_{style}_{underline}_{strikethrough}``,
            where underline and strikethrough are converted to integers 
            (0 or 1).

        Example:
            >>> key = FontManager.parameter_to_keyname(12)
            >>> print(key)  # "12_400_0_0_0"
            >>> key = FontManager.parameter_to_keyname(
            ...     12, weight=FONTWEIGHT_BOLD)
            >>> print(key)  # "12_700_0_0_0"
            >>> key = FontManager.parameter_to_keyname(
            ...     12, style=FONTSTYLE_ITALIC)
            >>> print(key)  # "12_400_1_0_0"
        """

        return f"{size}_{weight}_{style}_{int(underline)}_{int(strikethrough)}"


    @staticmethod
    @typing.overload
    def create_font(
        size: int,
        weight: int = FONTWEIGHT_NORMAL,
        style: int = FONTSTYLE_NORMAL,
        underline: bool = False,
        strikethrough: bool = False) -> str: ...


    @staticmethod
    @typing.overload
    def create_font(keyname: str) -> str: ...


    @staticmethod
    def create_font(*args) -> str:
        """Create a font using the singleton FontManager instance and add it 
        to the manager.

        This static method provides a convenient way to create fonts without
        explicitly managing the FontManager instance. It supports two calling
        patterns: by parameters or by key name string.

        Args:
            *args: Variable arguments that can be either
                - A single string: key name in format 
                  ``{size}_{weight}_{style}_{underline}_{strikethrough}``
                - Multiple parameters: size (int), weight (int, optional), 
                  style (int, optional), underline (bool, optional), 
                  strikethrough (bool, optional)

        Returns:
            The key name of the created font.

        Raises:
            ValueError: If arguments are invalid or key name format is 
                incorrect.

        Example:
            >>> # Create by parameters
            >>> key = FontManager.create_font(12, FONTWEIGHT_BOLD)
            >>> # Create by key name
            >>> key = FontManager.create_font("12_400_0_0_0")
        """

        return FontManager().create(*args)


    @staticmethod
    @typing.overload
    def get_font(
        size: int,
        weight: int = FONTWEIGHT_NORMAL,
        style: int = FONTSTYLE_NORMAL,
        underline: bool = False,
        strikethrough: bool = False) -> _Font: ...


    @staticmethod
    @typing.overload
    def get_font(keyname: str) -> _Font: ...


    @staticmethod
    def get_font(*args) -> _Font:
        """Retrieve a font from the singleton FontManager instance.

        This static method provides a convenient way to access fonts without
        explicitly managing the FontManager instance. It supports two calling
        patterns: by parameters or by key name string. If the requested font
        does not exist, it will be automatically created and added to the 
        manager.

        Args:
            *args: Variable arguments that can be either
                - A single string: key name in format 
                  ``{size}_{weight}_{style}_{underline}_{strikethrough}``
                - Multiple parameters: size (int), weight (int, optional), 
                  style (int, optional), underline (bool, optional), 
                  strikethrough (bool, optional)

        Returns:
            The wx.Font object corresponding to the specified parameters or 
            key name.

        Raises:
            ValueError: If arguments are invalid or key name format is 
                incorrect.

        Example:
            >>> # Get by parameters
            >>> font = FontManager.get_font(12, FONTWEIGHT_BOLD)
            >>> # Get by key name
            >>> font = FontManager.get_font("12_400_0_0_0")
            >>> # Use in wxPython widget
            >>> label.SetFont(font)
        """

        return FontManager()[*args]


    @classmethod
    def getkey_from_font(cls, font: _Font) -> str:
        """Extract or generate a key name from a wx.Font object.

        This class method searches the FontManager for an existing font that
        matches the provided font object. If found, it returns the 
        corresponding key name. If not found, it generates a key name based on 
        the font's properties without adding the font to the manager.

        Args:
            font: The wx.Font object to get the key name from.

        Returns:
            The key name string in the format
            ``{size}_{weight}_{style}_{underline}_{strikethrough}``.
            Returns the existing key if the font is found in the manager,
            or a generated key based on font properties if not found.

        Example:
            >>> font = wx.Font(12, wx.FONTFAMILY_DEFAULT, 
            ...                 wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD)
            >>> key = FontManager.getkey_from_font(font)
            >>> print(key)  # "12_700_0_0_0"
            >>> # Use with existing managed font
            >>> managed_font = FontManager.get_font("12_400_0_0_0")
            >>> key = FontManager.getkey_from_font(managed_font)
            >>> print(key)  # "12_400_0_0_0"
        """

        for key, value in cls().items():
            if value == font:
                return key

        key = (
            f"{font.GetPointSize()}_{font.GetWeight()}_{font.GetStyle()}_"
            f"{int(font.GetUnderlined())}_{int(font.GetStrikethrough())}"
        )

        return key


__all__ = [
    'FontManager',
]