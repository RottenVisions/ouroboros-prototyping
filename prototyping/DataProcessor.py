import data_abilities
import data_auras
import data_entities

class DataProcessor:
	"""
	Selector
	"""
	def __init__(self):
		pass

	def getAbilityWithUnknown(self, id):
		for i, itemIndex in enumerate(data_abilities.data):
			if data_abilities.data[itemIndex]['id'] == id:
				return data_abilities.data[(i + 1) % len(data_abilities.data)]

	def getAbilityWithId(self, id):
		for i, itemIndex in enumerate(data_abilities.data):
			if data_abilities.data[itemIndex]['id'] == id:
				return data_abilities.data[itemIndex]

	def getAbilityWithName(self, name):
		for i, itemIndex in enumerate(data_abilities.data):
			if data_abilities.data[itemIndex]['name'] == name:
				return data_abilities.data[itemIndex]

	def getAuraWithId(self, id):
		for i, itemIndex in enumerate(data_auras.data):
			if data_auras.data[itemIndex]['id'] == id:
				return data_auras.data[itemIndex]

	def getAuraWithName(self, name):
		for i, itemIndex in enumerate(data_auras.data):
			if data_auras.data[itemIndex]['name'] == name:
				return data_auras.data[itemIndex]

	def getEntityWithId(self, id):
		for i, itemIndex in enumerate(data_entities.data):
			if data_entities.data[itemIndex]['id'] == id:
				return data_entities.data[itemIndex]

	def getEntityWithName(self, name):
		for i, itemIndex in enumerate(data_entities.data):
			if data_entities.data[itemIndex]['name'] == name:
				return data_entities.data[itemIndex]