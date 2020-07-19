import sys
from Inventory import InventoryManager
from Inventory import ItemManager
from ItemManagement import ItemManagement

from Guild import GuildManager

from Chat import ChatManager
from Selector import Selector
from DataPuller import DataPuller
from DataProcessor import DataProcessor
from GameMaster import GameMaster
from Loot import Loot

import InitFix
import items

import GlobalConstants
import GlobalEnums

import data_entities_old

def InventoryTest1():
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

def InventoryTest2():
	inv = InventoryManager()
	inv.initialize()
	inv.addItemById(2)
	inv.items[0].getID()
	inv.addItemAtIndex(2, 7)
	print(inv.items)
	inv.moveItem(0, 7)
	print(inv.items)

def InventoryTest3():
	iman = ItemManager()
	item = iman.getItemByID(3)
	print(item.toString())

def InventoryTest4():
	inv = ItemManagement()
	inv.initialize(12)
	#print(inv.getInventoryAsString())
	result1 = inv.addItemToIndex(2, 0, 1)
	result1 = inv.addItemToIndex(1, 2, 4)
	#print(result1)

	#result2 = inv.addItem(2, 12)
	#print(inv.getInventoryAsString())
	#result3 = inv.removeItem(2, 7)
	#print(result2)
	print(inv.getInventoryAsString())
	result4 = inv.moveItemTo(2, 0)
	print(inv.getInventoryAsString())
	#result4 = inv.swapItems(0, 2)
	print(result4)
	#print(inv.getInventoryAsString())

def InventoryTest5():
	inv = ItemManagement()
	inv.Test1(2)

def InventoryTest6():
	inv = ItemManagement()
	item = items.getItemByID(2)
	item.use(1)

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
	pass

def GameMaster1():
	gameMaster = GameMaster()
	gameMaster.parseCommand(1, '.fly 100 50')

def LootTest1():
	loot = Loot()
	result = loot.getDropList(['gold ring', 'silver pendant', 'deathchargers reins'], [0.6, 0.3909, 0.001], 100)
	#print(result)
	if 'deathchargers reins' in result:
		print('got death charger!')
	else:
		print('nothing')
#GuildTest1()
#DataPullTest1()
#ChatTest1()
#Selector1()
#DataPuller1()
#Selector2()
#SelectByID2()
#Testing123()
#message ='.fly'
#if (message.startswith('.',0, 1)):
	#print('yes')
#print(message.startswith('.'))
#GameMaster1()
#InventoryTest2()
#InventoryTest3()
#InventoryTest4()
#InventoryTest5()
InventoryTest6()

#LootTest1()