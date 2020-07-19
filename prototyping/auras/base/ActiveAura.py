# -*- coding: utf-8 -*-

class ActiveAura():
	def __init__(self):
		self.auraTimer = -1
		self.tickCount = -1

	def loadFromDict(self, dictDatas):
		"""
		virtual method.
		Create this object from the dictionary
		Runs when all Auras are added to the from their files on init
		"""

	def onTimerTick(self, tid, userArg, superScript):
		pass

	def onAttach(self, attacher, auraCastObject):
		"""
		virtual method.
		When an aura is bound
		"""
		if self.auraTimer is not -1:
			return False

	def onDetach(self, context):
		"""
		virtual method.
		When an aura is unbound
		"""
		ActiveAura.setSource(self, None)
		self.auraTimer = -1
		self.tickCount = -1

	def onAuraTick(self, tid, userArg, superScript):
		"""
		virtual method.
		Cycle trigger
		"""
		superScript.onAuraCycleTick(tid, userArg, ActiveAura)
	
	def canAttach(self, attacher, auraCastObject):
		
		#Run any checks here then, run the super
		return 1
	
	def attachTo(self, attacher, auraCastObject):
		self.onAttach(attacher, auraCastObject)
		return self

	def detachFrom(self, superScript):
		pass
	
	def refresh(self, attacher, auraCastObject, superScript):
		if self.auraTimer is not -1:
			return False