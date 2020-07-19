# -*- coding: utf-8 -*-

data = {
	0: {
		'name': 'Book',
		'id': 1,
		'description': 'This is a book.',
		'icon': 'Item_Book_004',
		'stackable': True,
		'maxStack': 5,
		'scriptName': 'NormalItem',
		},
	1: {
		'name': 'Shield',
		'id': 2,
		'description': 'This is a shield.',
		'icon': 'Item_Shield_2',
		'stackable': False,
		'maxStack': 0,
		'scriptName': 'EquipItem',
		},
	2: {
		'name': 'Alcohol, the Other Drink',
		'id': 3,
		'description': '100% Proof Alcohol.',
		'icon': 'Item_Alchemy_Potion_Type_2',
		'stackable': True,
		'maxStack': 15,
		'scriptName': 'ConsumeItem',
		},
	3: {
		'name': 'Borite',
		'id': 4,
		'description': 'A simple resource.',
		'icon': 'Item_Mineral_1',
		'stackable': True,
		'maxStack': 30,
		'scriptName': 'NormalItem',
		},
	4: {
		'name': 'Gunite',
		'id': 5,
		'description': 'This is a really rare resource.',
		'icon': 'Item_Mineral_2',
		'stackable': True,
		'maxStack': 75,
		'scriptName': 'NormalItem',
		},
	5: {
		'name': 'Trash',
		'id': 6,
		'description': 'This is useless trash.',
		'icon': 'Item_Alchemy_Potion_Type_10',
		'stackable': True,
		'maxStack': 200,
		'scriptName': 'NormalItem',
		}
	}

allData = {
	'ItemInitialization': data
}

