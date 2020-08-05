import data_abilities
import data_auras

class Selector:
	"""
	Selector
	"""
	def __init__(self):
		self.HP = 100
		self.EG = 100
		self.abilities = []

		self.lowHPThreshold = .15
		self.lowEGThreshold = .25
		pass
	
	def setCharacterStats(self, hp, eg):
		self.HP = hp
		self.EG = eg
	
	def runSelector(self):
		passed = self.hpThresholdCheck()
		if not passed:
			healAbil = self.getBestHealingAbility()
			self.applyAbility(healAbil)
			print("chose " + healAbil['name'])
		passed = self.egThresholdCheck()
		return passed

	def hpThresholdCheck(self):
		return self.HP > (self.lowHPThreshold * 100)

	def egThresholdCheck(self):
		return self.EG > (self.lowEGThreshold * 100)

	def applyAbility(self, ability):
		if ability['type'] == 'Healing':
			self.HP += (ability['amount'] * 100)
	
	def getFirstHealingAbility(self):
		for i, itemIndex in enumerate(data_abilities.data):
			if data_abilities.data[itemIndex]['type'] == 'PeriodicHealing' or data_abilities.data[itemIndex]['type'] == 'Healing':
				return data_abilities.data[itemIndex]

	def getBestHealingAbility(self):
		healingAbilities = []
		for i, itemIndex in enumerate(data_abilities.data):
			if data_abilities.data[itemIndex]['type'] == 'PeriodicHealing' or data_abilities.data[itemIndex]['type'] == 'Healing':
				healingAbilities.append(data_abilities.data[itemIndex])
		lastAmount = 0
		for i in range(len(healingAbilities)):
			if healingAbilities[i]['amount'] > lastAmount:
				lastAmount = healingAbilities[i]['amount']
				bestAbility = healingAbilities[i]
		return bestAbility

	def auraTick(self, aura):
		pass