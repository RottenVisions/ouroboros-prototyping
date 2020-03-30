import datetime
import random as r
import GlobalConstants

import re

class GuildManager:
	"""
	Guild Manager
	"""
	def __init__(self):
		pass

	def isValidGuildName(self, name):
		return self.isValidLength(name) and self.isValidName(name)

	def isValidGuildNotice(self, notice):
		return True

	def createGuild(self, guildName, creator):
		return True

	def deleteGuild(self):
		return True

	def setGuildNotice(self):
		return True

	def addMember(self):
		return True

	def removeMember(self):
		return True

	def promoteMember(self):
		return True

	def demoteMember(self):
		return True

	def setMemberOnline(self):
		return True

	def setMemberOffline(self):
		return True
	
	def isValidName(self, name):
		if re.match("^[A-Za-z0-9_-]+$", name):
			return True
		return False

	def isValidLength(self, name):
		if len(name) <= GlobalConstants.GUILD_NAME_LIMIT:
			return True
		return False