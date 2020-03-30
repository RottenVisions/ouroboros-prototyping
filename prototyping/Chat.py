import json
import time
import datetime

import GlobalConstants
import GlobalEnums
import Tools

class ChatManager:
	"""
	Chat Manager
	"""
	def __init__(self):
		#self.chatChannelGlobal = {}
		self.createChannel(GlobalEnums.ChatChannel.CHAT_CHANNEL_GLOBAL)

	def createChannel(self, channelType):
		if channelType == GlobalEnums.ChatChannel.CHAT_CHANNEL_GLOBAL:
			self.chatChannelGlobal = {}

	def appendMessage(self, channelType, sender, message):
		createdMessageObj = {
			'sender': sender,
			'message': message,
			'date': Tools.getDate(),
			'time': Tools.getTime()
		}
		if channelType == GlobalEnums.ChatChannel.CHAT_CHANNEL_GLOBAL:
			index = len(self.chatChannelGlobal) + 1 #so it is not a zwro index
			self.chatChannelGlobal[index] = createdMessageObj

	def updateMessage(self, channelType, sender, message):
		createdMessageObj = {
			'sender': sender,
			'message': message,
			'date': Tools.getDate(),
			'time': Tools.getTime()
		}
		if channelType == GlobalEnums.ChatChannel.CHAT_CHANNEL_GLOBAL:
			self.chatChannelGlobal.update(createdMessageObj)  # use this only for existing values

	def writeChannelTypeToFile(self, channelType):
		dictToWrite = None
		if channelType == GlobalEnums.ChatChannel.CHAT_CHANNEL_GLOBAL:
			dictToWrite = self.chatChannelGlobal
		self.writeChannelToFile(dictToWrite, channelType)

	def writeChannelToFile(self, dict, channelType):
		fileName = "%s.%s.%s" % (str(channelType.name), Tools.getDateDots(), Tools.getTimeDots())
		with open('ChatLogs/%s.txt' % fileName, 'w') as file:
			file.write(json.dumps(dict, indent=2))  # use `json.loads` to do the reverse, indent adds to new line