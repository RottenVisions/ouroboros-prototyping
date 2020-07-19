# -*- coding: utf-8 -*-
#import Ouroboros
import items
import GlobalConstants
#import GlobalDefine
#import ServerConstantsDefine
#from OURODebug import

class ItemManagement:

	def __init__(self):
		self.inventory = []
		items.onInit() # remove this later

	def initialize(self, size):
		self.setSize(size)

	def addItem(self, id, count=1):
		remainingCount = count
		itemAdded = False
		for i in range(len(self.inventory)):
			item = self.inventory[i]
			# Blank space
			blankSpaceResult = self.isSpaceEmpty(i)
			# Operations are finished, No items left to add
			if remainingCount == 0:
				break
			# Blank Space
			if blankSpaceResult is GlobalConstants.INVENTORY_OPERATION_OK:
				# Create new item in blank space
				newItem = items.getItemByID(id)
				amountToAdd = remainingCount
				if remainingCount > newItem.getMaxStack():
					amountToAdd = newItem.getMaxStack()
				addItemResult, updatedBlankItem = self.addItemToIndex(id, i, amountToAdd)
				self.inventory[i] = updatedBlankItem
				remainingCount -= amountToAdd
				if addItemResult is GlobalConstants.INVENTORY_OPERATION_OK:
					itemAdded = True
			# Non-Blank Space
			elif blankSpaceResult is not GlobalConstants.INVENTORY_OPERATION_OK and item.getID() is id and remainingCount > 0:
				amountCanAdd = item.getMaxStack() - item.getCount()
				amountToAdd = remainingCount
				if remainingCount > amountCanAdd:
					amountToAdd = amountCanAdd
				finalAmountToAdd = amountToAdd + item.getCount()
				# Get updated item
				addItemResult, updatedItem = self.updateItem(item, i, finalAmountToAdd)
				# Update failed, discontinue add item procedure
				if addItemResult is not GlobalConstants.INVENTORY_OPERATION_OK:
					break
				# Set updated item
				self.inventory[i] = updatedItem
				remainingCount -= amountToAdd
				if addItemResult is GlobalConstants.INVENTORY_OPERATION_OK:
					itemAdded = True
			else:
				continue
		if itemAdded is True:
			return GlobalConstants.INVENTORY_OPERATION_OK
		return addItemResult

	def addItemToIndex(self, id, index, count=1):
		# Check parameters before initiation
		if self.countIsValid(items.getItemByID(id), count) is GlobalConstants.INVENTORY_OPERATION_INVALID_COUNT:
			return GlobalConstants.INVENTORY_OPERATION_INVALID_COUNT, None
		# Item exists in the space requested
		if not self.isSpaceEmpty(index):
			# item requested to be added is the same as the slot it is going in
			if self.inventory[index].getID() == id:
				# item is stackable (CHANGE THIS WHEN REAL ITEMS IMPLEMENTED)
				if self.inventory[index].getMaxStack() > 0:
					newCount = count
					# Do not let the count overflow
					if count > self.inventory[index].getMaxStack():
						newCount = self.inventory[index].getMaxStack()
					updateResult, updatedItem = self.updateItem(self.inventory[index], index, newCount)
					self.inventory[index] = updatedItem
					return updateResult, updatedItem

		item = items.getNewItemByID(id)

		if item is None:
			return GlobalConstants.INVENTORY_OPERATION_ITEM_NONEXISTENT, None

		if self.indexIsValid(index) is GlobalConstants.INVENTORY_OPERATION_INVALID_INDEX:
			return GlobalConstants.INVENTORY_OPERATION_INVALID_INDEX, None
		setupResult, setupItem = self.setupItem(item, index, count)
		self.inventory[index] = setupItem
		return setupResult, setupItem

	def removeItem(self, id, count=1):
		remainingCount = count
		itemRemoved = False
		removeItemResult = GlobalConstants.INVENTORY_OPERATION_ERROR
		for i in range(len(self.inventory)):
			item = self.inventory[i]
			# Blank space
			blankSpaceResult = self.isSpaceEmpty(i)
			# Operations are finished, No items left to add
			if remainingCount == 0:
				break
			# Non-Blank Space
			if blankSpaceResult is not GlobalConstants.INVENTORY_OPERATION_OK and item.getID() is id:
				amountCanRemove = item.getCount()
				amountToRemove = remainingCount
				if remainingCount > amountCanRemove:
					amountToRemove = amountCanRemove
				# Get updated item
				removeItemResult, updatedItem = self.removeItemAtIndex(i, amountToRemove)
				# Update failed, discontinue add item procedure
				if removeItemResult is not GlobalConstants.INVENTORY_OPERATION_OK:
					break
				# Set updated item
				self.inventory[i] = updatedItem
				remainingCount -= amountToRemove
				if removeItemResult is GlobalConstants.INVENTORY_OPERATION_OK:
					itemRemoved = True
			else:
				continue
		if itemRemoved is True:
			return GlobalConstants.INVENTORY_OPERATION_OK
		return removeItemResult

	def removeItemAtIndex(self, index, count=1):
		# Check parameters before initiation
		if self.indexIsValid(index) is GlobalConstants.INVENTORY_OPERATION_INVALID_INDEX:
			return GlobalConstants.INVENTORY_OPERATION_INVALID_INDEX, None
		# Declare item here before count because count is valid needs it
		item = self.inventory[index]
		if self.countIsValid(item, count) is GlobalConstants.INVENTORY_OPERATION_INVALID_COUNT:
			return GlobalConstants.INVENTORY_OPERATION_INVALID_COUNT, None

		removalAmount = count
		# Do not exceed the actual items count
		if count > item.getCount():
			removalAmount = item.getCount()
		updatedAmount = item.getCount() - removalAmount
		updateResult, updatedItem = self.updateItem(self.inventory[index], index, updatedAmount)
		self.inventory[index] = updatedItem
		return updateResult, updatedItem

	def moveItemTo(self, sourceIndex, destinationIndex):
		# Check if the source is empty
		emptySourceResult = self.isSpaceEmpty(sourceIndex)
		if emptySourceResult is GlobalConstants.INVENTORY_OPERATION_OK:
			return GlobalConstants.INVENTORY_OPERATION_EMPTY_SOURCE

		tempSourceItem = self.inventory[sourceIndex]

		emptyDestinationResult = self.isSpaceEmpty(destinationIndex)
		# Moving to an empty destination
		if emptyDestinationResult is GlobalConstants.INVENTORY_OPERATION_OK:
			updateDestinationResult, updatedDestinationItem = self.moveItem(
				tempSourceItem, destinationIndex, tempSourceItem.getCount())
			updateSourceResult, updatedSourceItem = self.updateItem(
				tempSourceItem, sourceIndex, 0)
			self.inventory[destinationIndex] = updatedDestinationItem
			self.inventory[sourceIndex] = updatedSourceItem
			return updateSourceResult, updateDestinationResult
		else:
			return self.swapItems(sourceIndex, destinationIndex)


	def swapItems(self, sourceIndex, destinationIndex):
		# Check if the source is empty
		emptySourceResult = self.isSpaceEmpty(sourceIndex)
		if emptySourceResult is GlobalConstants.INVENTORY_OPERATION_OK:
			return GlobalConstants.INVENTORY_OPERATION_EMPTY_SOURCE, None
		# Check if the destination is empty
		emptyDestinationResult = self.isSpaceEmpty(destinationIndex)
		if emptyDestinationResult is GlobalConstants.INVENTORY_OPERATION_OK:
			return GlobalConstants.INVENTORY_OPERATION_EMPTY_SOURCE, None

		# Check parameters before initiation
		if self.indexIsValid(sourceIndex) is GlobalConstants.INVENTORY_OPERATION_INVALID_INDEX:
			return GlobalConstants.INVENTORY_OPERATION_INVALID_INDEX, None
		if self.indexIsValid(destinationIndex) is GlobalConstants.INVENTORY_OPERATION_INVALID_INDEX:
			return GlobalConstants.INVENTORY_OPERATION_INVALID_INDEX, None

		tempSourceItem = self.inventory[sourceIndex]
		tempDestinationItem = self.inventory[destinationIndex]

		updateSourceResult = GlobalConstants.INVENTORY_OPERATION_ERROR
		updateDestinationResult = GlobalConstants.INVENTORY_OPERATION_ERROR

		# Same item detected for move
		if tempSourceItem.getID() == tempDestinationItem.getID():
			# Stackable item
			if tempDestinationItem.getMaxStack() > 0:
				# Find the max count we can add
				maxCountCanAdd = tempDestinationItem.getMaxStack() - tempDestinationItem.getCount()
				# Overflow will occur, so max out destination item
				if tempSourceItem.getCount() >= maxCountCanAdd:
					updateDestinationResult, updatedDestinationItem = self.updateItem(
						self.inventory[destinationIndex], destinationIndex, tempDestinationItem.getMaxStack())
					newSourceAmount = tempSourceItem.getCount() - maxCountCanAdd
					updateSourceResult, updatedSourceItem = self.updateItem(
						self.inventory[sourceIndex], sourceIndex, newSourceAmount)
				# Normal add to destination
				else:
					newDestinationAmount = tempDestinationItem.getCount() + tempSourceItem.getCount()
					updateDestinationResult, updatedDestinationItem = self.updateItem(
						tempSourceItem, destinationIndex, newDestinationAmount)
					newSourceAmount = tempSourceItem.getCount() - maxCountCanAdd
					updateSourceResult, updatedSourceItem = self.updateItem(
						tempSourceItem, sourceIndex, 0)
				self.inventory[destinationIndex] = updatedDestinationItem
				self.inventory[sourceIndex] = updatedSourceItem
			# Non stackable item
			else:
				# Simple swap
				self.inventory[destinationIndex] = tempSourceItem
				self.inventory[sourceIndex] = tempDestinationItem
				updateSourceResult = GlobalConstants.INVENTORY_OPERATION_OK
				updateDestinationResult = GlobalConstants.INVENTORY_OPERATION_OK
		# Different Items
		else:
			# Simple swap
			self.inventory[destinationIndex] = tempSourceItem
			self.inventory[sourceIndex] = tempDestinationItem
			updateSourceResult = GlobalConstants.INVENTORY_OPERATION_OK
			updateDestinationResult = GlobalConstants.INVENTORY_OPERATION_OK
		return updateSourceResult, updateDestinationResult

	# Modifiers
	def setupItem(self, item, index, count):
		if item is None or item == -1:
			return GlobalConstants.INVENTORY_OPERATION_ERROR, None
		if self.indexIsValid(index) is GlobalConstants.INVENTORY_OPERATION_INVALID_INDEX:
			return GlobalConstants.INVENTORY_OPERATION_INVALID_INDEX, None
		if self.countIsValid(item, count) is GlobalConstants.INVENTORY_OPERATION_INVALID_COUNT:
			return GlobalConstants.INVENTORY_OPERATION_INVALID_COUNT, None
		item.setCount(count)
		item.setIndex(index)
		item.setUUID(items.generate_uuid())
		return GlobalConstants.INVENTORY_OPERATION_OK, item

	def updateItem(self, item, index, count):
		if item is None or item == -1:
			return GlobalConstants.INVENTORY_OPERATION_ERROR, None
		if self.indexIsValid(index) is GlobalConstants.INVENTORY_OPERATION_INVALID_INDEX:
			return GlobalConstants.INVENTORY_OPERATION_INVALID_INDEX, None
		if self.countIsValid(item, count, True) is GlobalConstants.INVENTORY_OPERATION_INVALID_COUNT:
			return GlobalConstants.INVENTORY_OPERATION_INVALID_COUNT, None
		# Catch an item being deleted
		if count == 0:
			item = -1
		else:
			item.setCount(count)
			item.setIndex(index)
		return GlobalConstants.INVENTORY_OPERATION_OK, item

	def moveItem(self, item, index, count):
		if item is None or item == -1:
			return GlobalConstants.INVENTORY_OPERATION_ERROR, None
		if self.indexIsValid(index) is GlobalConstants.INVENTORY_OPERATION_INVALID_INDEX:
			return GlobalConstants.INVENTORY_OPERATION_INVALID_INDEX, None
		if self.countIsValid(item, count) is GlobalConstants.INVENTORY_OPERATION_INVALID_COUNT:
			return GlobalConstants.INVENTORY_OPERATION_INVALID_COUNT, None
		item.setCount(count)
		item.setIndex(index)
		return GlobalConstants.INVENTORY_OPERATION_OK, item

	def setSize(self, size):
		for n in range(len(self.inventory), size):
			self.inventory.append(-1)

	def clear(self):
		for i in range(len(self.inventory)):
			self.inventory[i] = -1

	#Utility
	def indexIsValid(self, index):
		if index < 0 or index >= len(self.inventory):
			return GlobalConstants.INVENTORY_OPERATION_INVALID_INDEX
		return GlobalConstants.INVENTORY_OPERATION_OK

	def countIsValid(self, item, count, countCanBeZero=False):
		if count < 0 or (count == 0 and countCanBeZero is False) or count > item.getMaxStack():
			return GlobalConstants.INVENTORY_OPERATION_INVALID_COUNT
		return GlobalConstants.INVENTORY_OPERATION_OK

	def isSpaceEmpty(self, index):
		if self.indexIsValid(index) is GlobalConstants.INVENTORY_OPERATION_INVALID_INDEX:
			return GlobalConstants.INVENTORY_OPERATION_INVALID_INDEX
		if self.isBlankSpace(index) or self.isNoneSpace(index):
			return GlobalConstants.INVENTORY_OPERATION_OK
		return GlobalConstants.INVENTORY_OPERATION_ERROR

	def getFirstFreeSpace(self):
		for i in range(0, len(self.inventory)):
			if self.inventory[i] == -1:
				return i

	def getFirstItemWithID(self, id):
		for item in self.inventory:
			if item is None or item == -1:
				continue
			if item.getID() == id:
				return item
		return None

	def getItemsWithID(self, id):
		foundItems = []
		for item in self.inventory:
			if item is None or item == -1:
				continue
			if item.getID() == id:
				foundItems.append(item)
		return foundItems

	def isInventoryFull(self):
		emptyIndex = -1
		# Find the first empty index in the inventory
		for i in range(0, len(self.inventory)):
			if self.inventory[i] == -1:
				emptyIndex = i
				break

		# Inventory is full
		if emptyIndex == -1:
			return GlobalConstants.INVENTORY_OPERATION_FULL
		return GlobalConstants.INVENTORY_OPERATION_OK

	def isBlankSpace(self, index):
		if self.inventory[index] == -1:
			return True
		return False

	def isNoneSpace(self, index):
		if self.inventory[index] is None:
			return True
		return False

	def getSize(self):
		return len(self.inventory)

	def oldSwapSameItemLogic(self):
		#destination has max stacks
		#updateDestinationResult, updatedDestinationItem = self.updateItem(tempDestinationItem, destinationIndex,
		#																  tempSourceItem.getCount())
		#updateSourceResult, updatedSourceItem = self.updateItem(tempSourceItem, sourceIndex,
		#														tempSourceItem.getMaxStack())
		pass

	def getInventoryAsString(self):
		invString = ''
		for i in range(len(self.inventory)):
			item = self.inventory[i]
			if item == -1:
				invString += str(item)
				if i != len(self.inventory) - 1:
					invString += ', '
			elif item is None:
				invString += 'None'
				invString += ', '
			else:
				invString += item.toString()
				if i != len(self.inventory) - 1:
					invString += ', '
		return ''.join(('[', invString, ']'))