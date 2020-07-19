# -*- coding: utf-8 -*-

class GameMaster:
	"""
	The base interface class of the server game master abilities
	"""

	def __init__(self):
		pass

	def setGameMaster(self, value):
		self.gameMaster = value

	def isGameMaster(self):
		print('someone checking for game master')
		return self.gameMaster

	def command(self, command, value):
		pass

	def parseCommand(self, entityID, command):
		#Remove the dot that begins the command
		command = command[1:]
		parts = command.split()
		cmd = parts[0]
		valOne = parts[1]
		if cmd == 'fly':
			print('i need to fly')
			pass
		if cmd == 'addAura':
			pass
		print(parts)
		print('parse that command')
		pass

	def parseValue(self, value):
		pass