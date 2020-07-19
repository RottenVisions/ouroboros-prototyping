import datetime
import random as r
import GlobalConstants


import re

class Loot:
	"""
	Loot Manager
	"""
	def __init__(self):
		pass

	def dropLoot(self, ):
		pass

	def getDropList(self, pop, distrib, pickAmount):
		return r.choices(population=pop, weights=distrib, k=pickAmount)

	def determineLoot(self):
		pass
