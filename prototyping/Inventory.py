import uuid
import base64
import datetime
import random as r
import GlobalConstants

import d_items

class InventoryManager:
	"""
	Inventory Manager
	"""
	def __init__(self):
		self.size = 12
		self.items = [0]
		self.itemsUuid = [0]
		self.playerInvSize = 12
		pass

	def initialize(self):
		self.items *= self.playerInvSize
		self.itemsUuid *= self.playerInvSize
		self.clear()

	def clear(self):
		for i in range(len(self.items)):
			self.items[i] = -1
		for i in range(len(self.itemsUuid)):
			self.itemsUuid[i] = -1

	def addItemById(self, itemId, itemCount = 1):
		foundItem = self.getItemInInventoryById(itemId)

		if foundItem == -1 or self.isInventoryFull():
			return GlobalConstants.INVENTORY_OPERATION_ERROR

		index = self.getFirstFreeSpace()
		return self.addItemAtIndex(itemId, index, itemCount)

	def addItemAtIndex(self, itemId, index = -1, itemCount = 1):
		result = -1

		if index != -1:
			emptyIndex = index
		else:
			emptyIndex = self.getFirstFreeSpace()

		print('%i emp ind' % (emptyIndex))
		if self.isInventoryFull():
			return result

		itemMan = ItemManager()

		# Get item prototype
		dataItem = itemMan.getItemWithId(itemId)
		# Place items
		itemMaxStack = dataItem['maxStack']

		# Non-stackable item
		if itemMaxStack == 1:
			itemUUID = itemMan.generate_uuid()
			itemInfo = {
				'uuid': itemUUID,
				'id': itemId,
				'count': itemCount,
				'index': emptyIndex
			}
			self.items[emptyIndex] = itemInfo
			result = itemUUID
		# Stackable Item
		else:
			for info in self.items:
				# Skip over blank slots
				if info == -1:
					continue
				if(info['id'] == itemId) and (info['count'] < itemMaxStack):
					info['count'] += itemCount
					result = info['uuid']
					if info['count'] > itemMaxStack:
						itemCount = info['count'] - itemMaxStack
						info['count'] = itemMaxStack
					else:
						itemCount = 0
						break

			if itemCount > 0:
				itemUUID = itemMan.generate_uuid()
				itemInfo = {
					'uuid': itemUUID,
					'id': itemId,
					'count': itemCount,
					'index': emptyIndex
				}
				self.items[emptyIndex] = itemInfo
				#self.itemsUuid[itemUUID] = itemInfo
				result = itemUUID

		return result

	def addItemByIndex(self, dataIndex, itemCount = 1):
		self.addItemById(d_items.data[dataIndex]['id'], itemCount)

	def removeItem(self, uuid, itemCount = 1):
		foundIndex = -1
		for i in range(0, len(self.items)):
			if self.items[i] == -1:
				continue
			if self.items[i]['uuid'] == uuid:
				foundIndex = i;
				break
		if foundIndex == -1:
			return GlobalConstants.INVENTORY_OPERATION_ERROR
		foundItem = self.items[foundIndex]
		print(foundItem)
		if itemCount < foundItem['count']:
			self.items[foundIndex]['count'] = foundItem['count'] - itemCount
			return -1
		else:
			self.items[foundIndex] = -1
			del self.items[foundIndex]
		return foundItem['id']

	def removeItemById(self, itemId, itemCount = 1):
		foundIndex = -1
		result = []
		removalsLeft = itemCount;
		for i in range(0, len(self.items)):
			if self.items[i] == -1:
				continue
			if self.items[i]['id'] == itemId:
				foundIndex = i
				result.append(i)

		iman = ItemManager()
		itemData = iman.getItemWithId(itemId)
		itemMaxStack = itemData['maxStack']

		if itemCount > itemMaxStack:
			removalsLeft = itemCount

		print(result)
		for i in range(0, len(result)):
			if removalsLeft == 0:
				break
			self.removeItemAtIndex(result[i], removalsLeft)
			print('%i %i' % (removalsLeft, i))
			removalsLeft -= itemMaxStack
			if removalsLeft < 0:
				removalsLeft == 0
		return result

	def removeItemAtIndex(self, index, itemCount = 1):
		if self.items[index] != GlobalConstants.EMPTY_SLOT:
			self.removeItem(self.items[index]['uuid'], itemCount)
			return index
		else:
			return GlobalConstants.INVENTORY_OPERATION_ERROR

	def getFirstFreeSpace(self):
		for i in range(0, len(self.items)):
			if self.items[i] == -1:
				return i

	def isInventoryFull(self):
		emptyIndex = -1
		# Find the first empty index in the inventory
		for i in range(0, len(self.items)):
			if self.items[i] == -1:
				emptyIndex = i
				break

		# Inventory is full
		if emptyIndex == -1:
			return True
		return False

	def getItemInInventoryById(self, id):
		for i, item in enumerate(self.items):
			if self.items[i] == -1:
				continue
			if item['id'] == id:
				# https://stackoverflow.com/questions/28997563/find-object-from-list-that-has-attribute-equal-to-some-value-and-also-get-the-ne
				# To handle the last element, you can use modulo: index % len(users)
				return self.items[(i + 1) % len(self.items)]

	def getItemInInventoryByName(self, name):
		for i, item in enumerate(self.items):
			if item['name'] == name:
				# To handle the last element, you can use modulo: index % len(users)
				return self.items[(i + 1) % len(self.items)]

class ItemManager:

	def __init__(self):
		pass

	def getItemWithIndex(self, index):
		for i, itemIndex in enumerate(d_items.data):
			if itemIndex == index:
				return d_items.data[(i + 1) % len(d_items.data)]

	def getItemWithId(self, id):
		for i, itemIndex in enumerate(d_items.data):
			if d_items.data[itemIndex]['id'] == id:
				return d_items.data[(i + 1) % len(d_items.data)]

	def getItemWithName(self, name):
		for i, itemIndex in enumerate(d_items.data):
			if d_items.data[itemIndex]['name'] == name:
				return d_items.data[(i + 1) % len(d_items.data)]

	def generate_uuid(self):
		random_string = ''
		random_str_seq = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
		uuid_format = [8, 4, 4, 4, 12]
		for n in uuid_format:
			for i in range(0, n):
				random_string += str(random_str_seq[r.randint(0, len(random_str_seq) - 1)])
			if n != 12:
				random_string += '-'
		return random_string

	# get a UUID - URL safe, Base64
	def get_a_uuid(self):
		r_uuid = base64.urlsafe_b64encode(uuid.uuid4().bytes)
		return r_uuid.replace('=', '')

	def getTimestamp(self):
		return datetime.datetime.now().strftime('%Y%m%d%H%M%S')

	def getTimestampWithMs(self):
		return datetime.datetime.now().strftime('%Y%m%d%H%M%S%f')

#print('%i %s' % (i, itemIndex))