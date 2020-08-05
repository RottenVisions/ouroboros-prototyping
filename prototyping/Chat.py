import json
import time
import datetime
import os.path

import GlobalConstants
import GlobalEnums
import Tools

from os import path

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
			index = len(self.chatChannelGlobal) + 1 # so it is not a zwro index
			self.chatChannelGlobal[index] = createdMessageObj
		# Each message added, make sure we aren't over our chat limit.
		self.channelGarbageCollector()

	def updateMessage(self, channelType, sender, message):
		createdMessageObj = {
			'sender': sender,
			'message': message,
			'date': Tools.getDate(),
			'time': Tools.getTime()
		}
		if channelType == GlobalEnums.ChatChannel.CHAT_CHANNEL_GLOBAL:
			self.chatChannelGlobal.update(createdMessageObj)  # use this only for existing values

	def channelGarbageCollector(self):
		if len(self.chatChannelGlobal) >= GlobalConstants.CHAT_CHANNEL_GLOBAL_CAPACITY:
			self.writeAndClear(GlobalEnums.ChatChannel.CHAT_CHANNEL_GLOBAL)

	def writeAndClear(self, channelType):
		self.writeChannelTypeToFile(channelType)
		if channelType == GlobalEnums.ChatChannel.CHAT_CHANNEL_GLOBAL:
			self.chatChannelGlobal.clear()

	def writeChannelTypeToFile(self, channelType):
		dictToWrite = None
		if channelType == GlobalEnums.ChatChannel.CHAT_CHANNEL_GLOBAL:
			dictToWrite = self.chatChannelGlobal
		self.writeChannelToFile(dictToWrite, channelType)

	def writeChannelToFile(self, dict, channelType):
		print(	os.path.abspath(os.getcwd()))
		fileName = "%s.%s.%s" % (str(channelType.name), Tools.getDateDots(), Tools.getTimeDots())
		# This is a testing check and should not happen in the real world, basically this will 
		# track many messages coming in at once and overwriting the last wrote file
		dupeIndex = 0
		while path.exists('ChatLogs/%s.txt' % fileName):
			dupeIndex += 1
			fileName = "%s.%s.%s.%s" % (str(channelType.name), Tools.getDateDots(), Tools.getTimeDots(), dupeIndex)
		with open('ChatLogs/%s.txt' % fileName, 'w') as file:
			file.write(json.dumps(dict, indent=2))  # use `json.loads` to do the reverse, indent adds to new line