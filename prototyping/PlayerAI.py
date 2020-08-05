import data_abilities
import data_auras
import GlobalDefine
import GlobalConstants
import Selector
import Sequencer

class PlayerAI:
    """
    Player AI
    """

    def __init__(self):
        self.sequencer = Sequencer()
        self.selector = Selector()
        self.aiType = GlobalConstants.AI_PLAYER_TYPE_SEQUENCER
        self.selector.abilities = [0, 1, 2]