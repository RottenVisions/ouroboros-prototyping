# -*- coding: utf-8 -*-

from auras.base.ActiveAura import ActiveAura

class HarmfulAura(ActiveAura):
	def __init__(self):
		ActiveAura.__init__(self)
		
	def onTimer(self, tid, userArg):
		"""
		Ouroboros method.
		Engine callback timer trigger
		"""
		ActiveAura.onTimerTick(self, tid, userArg, self)

	def canAttach(self, caster, scObject):
		"""
		virtual method.
		Can use
		@param caster: Entity that gives Aura
		@param receiver: Entity
		"""
		#GlobalConst.GC_OK
		return ActiveAura.canAttach(self, caster, scObject)

	def attach(self, caster, scObject):
		"""
		virtual method.
		Attach an aura
		@param caster: Entity that casts Aura
		@param receiver: Entity
		"""
		self.onAttached(caster, scObject)
		return ActiveAura.attachTo(self, caster, scObject)
	
	def refresh(self, caster, scObject):
		"""
		virtual method.
		Attach an aura
		@param caster: Entity that casts Aura
		@param receiver: Entity
		"""
		self.onAttached(caster, scObject)
		return ActiveAura.refresh(self, caster, scObject, self)

	def detach(self, scObject):
		self.onDetached(scObject)

	def onAuraCycleTick(self, tid, userArg, auraCastObject):
		#DEBUG_MSG('Take your damage %i' % auraCastObject.getAmount(self))
		pass

	def onAttached(self, attacher, auraCastObject):
		pass

	def onDetached(self, scObject):
		pass
	
	def onRefreshed(self):
		pass

	def addStack(self):
		ActiveAura.addStack(self)