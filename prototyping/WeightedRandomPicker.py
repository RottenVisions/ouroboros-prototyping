import random

from os import path


class WeightedRandomPicker:
    """
	Random Picker
	"""

    def __init__(self):
        self.entries = []
        self.accumulatedWeight = 0.0

    def addEntry(self, entry, weight):
        self.accumulatedWeight += weight
        self.entries.append(Entry(entry, self.accumulatedWeight))

    def getRandom(self):
        r = random.random() * self.accumulatedWeight
        for entry in self.entries:
            if entry.weight >= r:
                return entry
        # Should only happen when there are no entries
        return None

class Entry:
    def __init__(self, id, weight):
        self.id = id
        self.weight = weight
