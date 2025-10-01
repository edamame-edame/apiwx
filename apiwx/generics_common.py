"""
# apiwx - A generic definitions for wxPython class common.
"""
import typing
import types


try:
    from . import core
    from . import debug
    from . import generics_core

except ImportError:
    import core
    import debug
    import generics_core


class FixSize:
	"""
	# Mixin class to fix the size of a window or panel.
	"""
	def __init__(self: core.UIAttributes, *args, **kwds):
		# fix the size of the window/panel
		self.size_max = self.size
		self.size_min = self.size


class AutoDetect:
	detect_target: tuple[core.UIAttributes, ...] = ()


	_children_namelist: list[str]


	def __new__(cls: typing.Type['AutoDetect'], instance: 'AutoDetect', *args, **kwds):
		# create object
		# super class init was called from WrappedApp.__new__
		# so do nothing here
		...

		# below code was called after super class init

		# init children namelist
		instance._children_namelist = []

		members = cls.get_all_members()

		debug.internaldebug_log("CHILDREN", f"__dict__ = {members}")

		# scan attributes
		for attr_name in members:
			# is wx.Frame instance ?
			if (cls.is_target_class(members[attr_name])
			 or cls.is_target_instance(members[attr_name])):
				# add to children namelist
				instance._children_namelist.append(attr_name)

		debug.internaldebug_log("CHILDREN", f"__children_namelist__ = {instance._children_namelist}")

		# end of __new__
		return instance


	def __class_getitem__(cls, detect_target: tuple[core.UIAttributes, ...] | core.UIAttributes) -> type:
		if not isinstance(detect_target, tuple):
			detect_target = (detect_target,)

		for target in detect_target:
			if not issubclass(target, core.UIAttributes):
				raise TypeError('detect_target must be an instance of core.UIAttributes or a tuple of core.UIAttributes')

		# create new class namespace
		new_cls_namespace = dict(cls.get_all_members_for_autodetect())

		# add detect target
		new_cls_namespace["detect_target"] = detect_target

		# create new class
		new_cls = types.new_class(
			f"{cls.__name__}<{', '.join([t.__name__ for t in detect_target])}>",
			cls.__mro__,
			{},
			lambda ns: ns.update(new_cls_namespace)
		)

		return new_cls
	

	@classmethod
	def is_target_class(cls, classobj: typing.Type) -> bool:
		return (
			# is class type ?
			(isinstance(classobj, type))
			# is subclass of wx.Frame ?
			and (issubclass(classobj, cls.detect_target))
		)
	

	@classmethod
	def is_target_instance(cls, instance: object) -> bool:
		return (
			# is instance ?
			(isinstance(instance, object))
			# is instance of wx.Frame ?
			and (isinstance(instance, cls.detect_target))
		)
	

	@classmethod
	def get_all_members_for_autodetect(cls) -> dict[str, typing.Type]:
		members = {}

		# scan mro
		for mro_cls in cls.__mro__:
			# skip built-in classes
			if mro_cls.__name__ in ('object', 'sip.wrapper'):
				continue

			members.update(mro_cls.__dict__)

		return members


	@property
	def children(self) -> dict[core.UIIndexor, typing.Type]:
		# lazy init
		if not hasattr(self, '_children'):
			self._children = {}

		return self._children
	

	def __init__(self, *args, **kwds):
		# create object
		# super class init was called from WrappedApp.__new__
		# so do nothing here
		...

		# below code was called after super class init

		# init children counter
		self._children_counter = 0

		# scan children namelist
		for child_name in self._children_namelist:
			# get child window
			child = getattr(self, child_name)

			# is wx.Frame class or instance ?
			if self.is_target_class(child):
				# create instance
				child = child(self)

			if self.is_target_instance(child):
				# increase counter
				index = self._children_counter
				self._children_counter += 1

				# set index attribute
				setattr(
					self, f"child_{index}", core.UIIndexor(index, self.children)
				)

				debug.uilog("CHILDREN", f"Created, child_{index} = {child_name}	({child})")

				# add to children dict
				self.children[index] = child

