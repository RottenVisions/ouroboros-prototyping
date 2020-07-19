# -*- coding: utf-8 -*-
import GlobalConstants

from items.base.BaseItem import BaseItem

class NormalItem(BaseItem):

	def __init__(self):
		BaseItem.__init__(self)

	def copy(self):
		return NormalItem()

	def canUse(self, user):
		return GlobalConstants.GC_OK

	def use(self, user):
		#self.getID()
		return GlobalConstants.GC_OK