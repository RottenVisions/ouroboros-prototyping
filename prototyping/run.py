import sys
from Inventory import InventoryManager
from Inventory import ItemManager

from Guild import GuildManager

from Chat import ChatManager
from Selector import Selector
from DataPuller import DataPuller
from DataProcessor import DataProcessor

import InitFix

import GlobalConstants
import GlobalEnums

import data_entities_old

def InventoryTest1(self):
	inv = InventoryManager()
	inv.initialize()

	for i in range(0, 12):
		result = inv.addItemById(0, 1)

	#print(inv.items)
	#print(len(inv.items))

	#print(inv.testOne())

	#print(inv.getItemInInventoryByName('boob'))

	iman = ItemManager()
	#item = iman.getItemWithIndex(1)
	#print(item)
	#print(iman.getItemWithId(0))

	print(inv.items)
	inv.removeItemById(0, 8)
	print(result)
	print(inv.items)
	#print(inv.itemsUuid)
	pass

def GuildTest1():
	gld = GuildManager()
	valid = gld.isValidGuildName('Make Azeroth Great Again')
	print(valid)
	#print(gld.isValidLength('MakeAzeroth'))
	print(gld.isValidName('MakeAzeroth'))
	#print(gld.isValidLength('Make Azeroth'))
	print(gld.isValidName('Make Azeroth'))
	pass

def DataPullTest1():
	testData = data_entities_old.data.get(80008001)
	#testData = data_entities.allData.get('80008001')
	print("%f" % testData['moveSpeed'])
	#print(testData)
	#print(data_entities.data)

def ChatTest1():
	chat = ChatManager()
	for _ in range(20):
		chat.appendMessage(GlobalEnums.ChatChannel.CHAT_CHANNEL_GLOBAL, 'Alfred', 'We need to overcome')
		print(_)
	#chat.writeChannelTypeToFile(GlobalEnums.ChatChannel.CHAT_CHANNEL_GLOBAL)
	print(chat.chatChannelGlobal)

def Selector1():
	selector = Selector()
	dataProcessor = DataProcessor()
	#abil = selector.getAbilityWithId(3)
	passed = selector.runSelector()
	print(passed)
	selector.setCharacterStats(15, 15)
	passed = selector.runSelector()
	print(passed)
	print(selector.HP)
	print(selector.getAuraWithId(selector.getAbilityWithId(2)['auraOne']))
	#abil = selector.getFirstHealingAbility()
	#print (abil['name'])

def Selector2():
	selector = Selector()
	dataProcessor = DataProcessor()
	selector.auraTick(dataProcessor.getAuraWithId(2))

def DataPuller1():
	dataPull = DataPuller()
	dataPull.createSpawnPointDatas()

def SelectByID():
	dataProcessor = DataProcessor()
	aura = dataProcessor.getAuraWithIdLine(2)
	print(aura)

def SelectByID2():
	InitFix.onInit()
	InitFix.getAuraByID(3)

def Testing123():
	#print(60 % 10.0)
	#print(60 % 10.0 is 0)

#GuildTest1()
#DataPullTest1()
#ChatTest1()
#Selector1()
#DataPuller1()
#Selector2()
#SelectByID2()
Testing123()