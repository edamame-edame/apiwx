'''
# Api wxPython font creator class difinition
'''
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
    '''
    # Font manager class

    ### Usage:
    ```python

    FontManager('MS UI Gothic') # init instance (and set default font family)

    FontManager.instance.create()

    label = wx.StaticText(parent, label="Sample Text")

    label.SetFont(fontmgr["default"])

    '''
    instance: typing.Type['FontManager'] | None = None

    def __new__(cls, *args, **kwargs):
        if FontManager.instance is None:
            FontManager.instance = super().__new__(cls)

        return FontManager.instance


    def __init__(self, font_family: str = "MS UI Gothic"):
        # init base dict class
        super().__init__()
        # set font family
        self.font_family = font_family


    def create_by_parameter(
        self,
        size: int,
        weight: int = FONTWEIGHT_NORMAL,
        style: int = FONTSTYLE_NORMAL,
        underline: bool = False,
        strikethrough: bool = False) -> str:
        '''
        # Create font and add to manager

        ### Args:

        size (int): Font size

        weight (int, optional): Font weight. Defaults to FONTWEIGHT_NORMAL.

        style (int, optional): Font style. Defaults to FONTSTYLE_NORMAL.

        underline (bool, optional): Underline flag. Defaults to False.

        strikethrough (bool, optional): Strikethrough flag. Defaults to False.

        ### Returns:

        str: Key name of created font

        ### Usage:

        ```python
        FontManager.instance.create(12) # create normal font
        FontManager.instance.create(12, weight=FONTWEIGHT_BOLD) # create bold font
        FontManager.instance.create(12, style=FONTSTYLE_ITALIC) # create italic font
        ```

        '''

        # create font info
        fontinfo = _FontInfo(size)
        fontinfo.FaceName(self.font_family)
        fontinfo.Weight(weight)
        fontinfo.Style(style)
        fontinfo.Underlined(underline)
        fontinfo.Strikethrough(strikethrough)

        # create font
        font = _Font(fontinfo)

        # create key name
        keyname = f"{size}_{weight}_{style}_{int(underline)}_{int(strikethrough)}"

        # add to manager
        self[keyname] = font

        # return key name
        return keyname


    def create_by_keyname(self, keyname: str) -> str:
        '''
        # Create font by key name and add to manager

        ### Args:

        keyname (str): Key name of font to create. Format is "{size}_{weight}_{style}_{underline}_{strikethrough}"

        ### Returns:

        str: Key name of created font

        ### Usage:

        ```python
        FontManager.instance.create("12_400_0_0_0") # create normal font
        FontManager.instance.create("12_700_0_0_0") # create bold font
        FontManager.instance.create("12_400_1_0_0") # create italic font
        ```

        '''

        # split key name
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

        return self.create_by_parameter(size, weight, style, underline, strikethrough)


    def create(self, *args):
        if len(args) == 1 and isinstance(args[0], str):
            return self.create_by_keyname(args[0])

        elif len(args) >= 1 and isinstance(args[0], int):
            key = self.parameter_to_keyname(*args)

        else:
            raise ValueError("Invalid arguments")


    @typing.overload
    def __getitem__(self, key: str) -> _Font: ...

    @typing.overload
    def __getitem__(
        self,
        size: int,
        weight: int = FONTWEIGHT_NORMAL,
        style: int = FONTSTYLE_NORMAL,
        underline: bool = False,
        strikethrough: bool = False) -> _Font: ...


    def __getitem__(self, arg) -> _Font:

        if len(arg) == 1 and isinstance(arg[0], str):
            key = arg[0]

        elif len(arg) >= 1 and isinstance(arg[0], int):
            key = self.parameter_to_keyname(*arg)

        else:
            raise ValueError("Invalid arguments")

        # if font not exist
        if not key in self:
            # create font if not exist
            self.create_by_keyname(key)

        # return font
        return super().__getitem__(key)
    

    @classmethod
    def parameter_to_keyname(
        cls,
        size: int,
        weight: int = FONTWEIGHT_NORMAL,
        style: int = FONTSTYLE_NORMAL,
        underline: bool = False,
        strikethrough: bool = False) -> str:
        '''
        # Convert font parameters to key name

        ### Args:

        size (int): Font size

        weight (int, optional): Font weight. Defaults to FONTWEIGHT_NORMAL.

        style (int, optional): Font style. Defaults to FONTSTYLE_NORMAL.

        underline (bool, optional): Underline flag. Defaults to False.

        strikethrough (bool, optional): Strikethrough flag. Defaults to False.

        ### Returns:

        str: Key name of font

        ### Usage:

        ```python
        keyname = FontManager.parameter_to_keyname(12) # get key name of normal font
        keyname = FontManager.parameter_to_keyname(12, weight=FONTWEIGHT_BOLD) # get key name of bold font
        keyname = FontManager.parameter_to_keyname(12, style=FONTSTYLE_ITALIC) # get key name of italic font
        ```

        '''

        return f"{size}_{weight}_{style}_{int(underline)}_{int(strikethrough)}"


    @typing.overload
    def create_font(
        size: int,
        weight: int = FONTWEIGHT_NORMAL,
        style: int = FONTSTYLE_NORMAL,
        underline: bool = False,
        strikethrough: bool = False) -> str: ...


    @typing.overload
    def create_font(keyname: str) -> str: ...


    @staticmethod
    def create_font(*args) -> str:
        '''
        # Create default font and add to manager

        ### Returns:

        str: Key name of created font

        ### Usage:

        ```python
        FontManager.create_font() # create default font (12, normal, normal, False, False)
        ```

        '''

        return FontManager().create(*args)


    @typing.overload
    def get_font(
        size: int,
        weight: int = FONTWEIGHT_NORMAL,
        style: int = FONTSTYLE_NORMAL,
        underline: bool = False,
        strikethrough: bool = False) -> _Font: ...


    @typing.overload
    def get_font(keyname: str) -> _Font: ...


    @staticmethod
    def get_font(*args) -> _Font:
        '''
        # Get font from manager

        ### Args:

        key (str): Key name of font to get

        ### Returns:

        wx.Font: Font object

        ### Usage:

        ```python
        font = FontManager.get_font("12_400_0_0_0") # get normal font
        font = FontManager.get_font("12_700_0_0_0") # get bold font
        font = FontManager.get_font("12_400_1_0_0") # get italic font
        ```

        '''

        return FontManager()[*args]


    @classmethod
    def getkey_from_font(cls, font: _Font) -> str | None:
        '''
        # Get key name from font object
    
        ### Args:
    
        font (wx.Font): Font object to get key name from
    
        ### Returns:
    
        str | None: Key name of font if found, else None
    
        ### Usage:
    
        ```python
        keyname = FontManager.getkey_from_font(font) # get key name from font object
        ```
    
        '''

        for key, value in cls().items():
            if value == font:
                return key

        key = f"{
            font.GetPointSize()
        }_{
            font.GetWeight()
        }_{
            font.GetStyle()
        }_{
            int(font.GetUnderlined())
        }_{
            int(font.GetStrikethrough())
        }"

        return key