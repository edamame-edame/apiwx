'''
# panaeltransmodel for apiwx
'''


try:
    from . import core
    from . import debug
    from . import generics_window

except ImportError:
    import core
    import debug
    import generics_window

class NotTransition:
	'''
	# NotTransition generics class for apiwx
	### (Not additional codes needed)
	'''
	pass


class SupportTransit(generics_window.DetectPanel):
	@property
	def panel_trans(self) -> 'PanelTransModel':
		return self._panel_trans

	def __init__(self, *args, **kwds):
		super().__init__(*args, **kwds)

		self._panel_trans = PanelTransModel()

		for child_id in self.children:
			child: core.WrappedPanel = self.children[child_id]

			if not child.hasgeneric(NotTransition):
				self.panel_trans.add(child_id, child)

		debug.internaldebug_log("TRANSIT", "Panels: {}".format(self.panel_trans))


class TransitPanelContainer:
	'''
	# TransitPanelContainer generics class
	### (for apiwx.WrappedWindow or apiwx.WrappedPanel)
	### Usage
	```python
		class MyWindow(
			WrappedWindow[
				# 01 auto detect panel class
				DetectPanel,
				# 02 panel transition model
				TransitPanelContainer]):
			...
	```
	'''

	panel_trans: 'PanelTransModel'

	def __init__(self, *args, **kwds):
		self.panel_trans = PanelTransModel()

		debug.internaldebug_log("TRANSIT", "Panels: {}".format(self.panel_trans))

		for child_id in self.children:
			child: core.WrappedPanel = self.children[child_id]

			if not child.hasgeneric(NotTransition):
				self.panel_trans.add(child_id, child)


class PanelTransModel(dict[core.UIIndexor, core.WrappedPanel]):
	'''
	# PanelTransModel class for apiwx
	'''
	_now: core.UIIndexor | None


	@property
	def now(self) -> core.UIIndexor | None:
		'''
		# get the current panel indexor
		'''
		return self._now
	
	@now.setter
	def now(self, indexor: core.UIIndexor | None) -> None:
		'''
		# set the current panel indexor
		'''
		if indexor is not None and not isinstance(indexor, core.UIIndexor):
			raise TypeError('indexor must be an instance of new_core.UIIndexor or None')

		self.trans(indexor)


	@property
	def is_show_any(self) -> bool:
		'''
		# check if any panel is currently shown
		'''
		return self.now is not None


	def __init__(self):
		super(PanelTransModel, self).__init__()

		self._now = None


	def add(self, indexor: core.UIIndexor, panel: core.WrappedPanel) -> None:
		'''
		# set the panel with the given indexor
		'''
		if not isinstance(indexor, core.UIIndexor):
			raise TypeError('indexor must be an instance of new_core.UIIndexor')

		if not isinstance(panel, core.WrappedPanel):
			raise TypeError('panel must be an instance of new_core.WrappedPanel')

		if indexor in self:
			raise KeyError('indexor already exists')

		if panel.__class__.hasgeneric(NotTransition):
			return # do nothing for NotTransition panels
		
		if len(self) == 0:
			# make sure the panel is shown first
			panel.Show()
		
		else:
			# hide the panel
			panel.Hide()

		super(PanelTransModel, self).__setitem__(indexor, panel)


	def __setitem__(self, indexor: core.UIIndexor, panel: core.WrappedPanel) -> None:
		'''
		# add the panel with the given indexor
		'''
		self.add(indexor, panel)


	def remove(self, indexor: core.UIIndexor) -> None:
		'''
		# remove the panel with the given indexor
		'''
		if indexor in self:
			if self.now == indexor:
				self.now = None

			super(PanelTransModel, self).__delitem__(indexor)


	def trans(self, indexor: core.UIIndexor) -> bool:
		'''
		# transition to the panel with the given indexor
		'''
		if self.now is not None:
			self._now.hide()
			self._now = None

		if indexor in self:
			if indexor.show():
				self._now = indexor

		return self.is_show_any

