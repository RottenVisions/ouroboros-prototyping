import data_abilities
import data_auras


class Sequencer:
    """
    Selector
    """

    def __init__(self):
        self.HP = 100
        self.EG = 100

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