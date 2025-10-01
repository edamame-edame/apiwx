"""
# apiwx - A generic definitions for wxPython wx.Frame.
"""
try:
    from . import core
    from . import generics_common
except ImportError:
    import core
    import generics_common


class ByPanelSize:
	'''
	# Generics for WrappedWindow
	### Usage
	```python
	window = WrappedWindow[ByPanelSize](
		app,
		panel_size = (800, 600),
		...
	)

	window.show()

	app.mainloop()

	```
	'''


	@property
	def size(self: core.WrappedWindow) -> tuple[int, int]:
		return self.clientsize
	
	@size.setter
	def size(self: core.WrappedWindow, value: tuple[int, int]):
		self.clientsize = value


	def __init__(self: core.WrappedWindow, *args, **kwds):
		# super class init was called from WrappedWindow.__init__
		# so do nothing here
		...

		# below code was called after super class init
		# set size (panel size is client size)
		self.clientsize = self.GetSize()

		# end of __init__
		return
	

DetectPanel = generics_common.AutoDetect[
    core.WrappedPanel
]
''' ### A type variable for auto detect panel class. '''

