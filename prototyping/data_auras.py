# -*- coding: utf-8 -*-

data = {
	0: {
		'name': 'Corruption',
		'id': 1,
		'description': 'Corrupts the target, causing %a Shadow damage over %s sec.',
		'school': 'Shadow',
		'icon': 'Aura_30',
		'type': 'Harmful',
		'script': 'HarmfulAura',
		'stackable': 'True',
		'maxStacks': 5,
		'amount': 1,
		'duration': 12,
		'period': 2,
		'amountBased': 'AbilityPower',
		},
	1: {
		'name': 'Devouring Plague',
		'id': 2,
		'description': 'Plagues the target, causing %a Shadow damage over %s sec.',
		'school': 'Shadow',
		'icon': 'Aura_31',
		'type': 'Harmful',
		'script': 'HarmfulAura',
		'stackable': 'False',
		'maxStacks': 0,
		'amount': 2,
		'duration': 33,
		'period': 11,
		'amountBased': 'AbilityPower',
		},
	2: {
		'name': 'Kil\'Jaeden\'s Curse',
		'id': 3,
		'description': 'Curses the target, causing %a Shadow damage over %s sec.',
		'school': 'Dark',
		'icon': 'Aura_20',
		'type': 'Harmful',
		'script': 'HarmfulAura',
		'stackable': 'False',
		'maxStacks': 0,
		'amount': 2,
		'duration': 60,
		'period': 6,
		'amountBased': 'AbilityPower',
		},
	3: {
		'name': 'Smite\'s Blight',
		'id': 4,
		'description': 'Smites the target, causing %a Holy healing over %s sec.',
		'school': 'Holy',
		'icon': 'Aura_28',
		'type': 'Helpful',
		'script': 'HelpfulAura',
		'stackable': 'False',
		'maxStacks': 0,
		'amount': 10,
		'duration': 30,
		'period': 5,
		'amountBased': 'AbilityPower',
		}
}

allData = {
	'AuraInitialization': data
}