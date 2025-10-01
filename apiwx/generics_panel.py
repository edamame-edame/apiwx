"""
# apiwx - A generic definitions for wxPython wx.Panel.
"""
try:
    from . import core
    from . import generics_common
    from . import painttool
    from . import debug
except ImportError:
    import core
    import generics_common
    import painttool
    import debug


class WithBoarder():
    @property
    def default_boarder_color(self) -> str:
        return "#000000"

    @property
    def boarder_color(self) -> str:
        if not hasattr(self, '_boarder_color'):
            return self.default_boarder_color

        return self._boarder_color

    @boarder_color.setter
    def boarder_color(self, value: str | None):
        if(value is None):
            value = self.default_boarder_color

        self._boarder_color = value


    @property
    def default_boarder_thickness(self) -> int:
        return 3

    @property
    def boarder_thickness(self) -> int:
        if not hasattr(self, '_boarder_thickness'):
            return self.default_boarder_thickness

        return self._boarder_thickness

    @boarder_thickness.setter
    def boarder_thickness(self, value: int | None):
        if(value is None):
            value = self.default_boarder_thickness

        self._boarder_thickness = value


    @property
    def default_boarder_offset(self) -> int:
        return 0

    @property
    def boarder_offset(self) -> int:
        if not hasattr(self, '_boarder_offset'):
            return self.default_boarder_offset

        return self._boarder_offset

    @boarder_offset.setter
    def boarder_offset(self, value: int | None):
        if(value is None):
            value = self.default_boarder_offset

        self._boarder_offset = value


    def __init__(
        self,
        *args,
        boarder_color: str | None = None,
        boarder_thickness: int | None = None,
        boarder_offset: int | None = None,
        **kwds):
        # super class init was called from WrappedWindow.__init__
        # so do nothing here
        ...

        # below code was called after super class init

        # set boarder color
        self.boarder_color = boarder_color

        # set boarder thickness
        self.boarder_thickness = boarder_thickness

        # set boarder offset from panel frame
        self.boarder_offset = boarder_offset

        # connect slots for paint boarder
        self.slots_on_paint += (
            self.draw_boarder
        )


    def draw_boarder(self, *args, **kwds):
        debug.uilog("BOARDER", f"Draw boarder: {self.boarder_color}, {self.boarder_thickness}, {self.boarder_offset}")

        # get panel size
        width, height = self.size

        # create draw context
        device_context = painttool.PaintDC(
            self
        )

        # pen -> boarder_color
        device_context.SetPen(
            painttool.Pen(
                self.boarder_color,
                self.boarder_thickness
            )
        )

        # fill color -> transparent
        device_context.SetBrush(
            painttool.TRANSPARENT_BRUSH
        )

        x0 = self.boarder_offset + self.boarder_thickness // 2
        y0 = self.boarder_offset + self.boarder_thickness // 2
        x = width - int(self.boarder_offset + self.boarder_thickness // 2)
        y = height - int(self.boarder_offset + self.boarder_thickness // 2)

        # draw rectangle
        device_context.DrawRectangle(
            x0, y0, x, y
        )

        debug.uilog("DRAWRECT", f"Rect(x0, x, y0, y) = ({x0}, {x}, {y0}, {y})")

        # remove draw slot
        self.slots_on_paint -= (
            self.draw_boarder
        )


DetectChildren = generics_common.AutoDetect[
    core.WrappedPanel,
    core.WrappedTextBox,
    core.WrappedButton,
    core.WrappedCheckBox,
    core.WrappedComboBox,
    core.WrappedChoice,
    core.WrappedStaticText,
    core.WrappedImage,
    core.WrappedListBox,
    core.WrappedListCtrl,
    core.WrappedRadioBox,
    core.WrappedScrolledWindow,
    core.WrappedSlider,
]
''' ### A type variable for auto detect panel class. '''

