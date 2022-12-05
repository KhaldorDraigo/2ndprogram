from spells import *

class Reaper():
	def __init__(self, name):
		self.HP = 2000
		self.AD = 100
		self.turn = 1
		self.name = name
		self.spells = [combo, legend, temper]

	def attack(self, target):
		(target).HP -= self.AD

	def use_spell(self, target, spell_number):
		(self.spells[spell_number - 1]).cast(target)




class Priest():
	def __init__(self, name):
		self.HP = 1800
		self.AD = 10
		self.turn = 1
		self.name = name
		self.spells = [remedy, revitalize, judgement]

	def attack(self, target):
		(target).HP -= self.AD

	def use_spell(self, target, spell_number):
		(self.spells[spell_number - 1]).cast(target)

class Alien():
	def __init__(self, name):
		self.HP = 1800
		self.AD = 40
		self.turn = 1
		self.name = name
		self.spells = [mindbreak, terrify, mend]

	def attack(self, target):
		(target).HP -= self.AD

	def use_spell(self, target, spell_number):
		(self.spells[spell_number - 1]).cast(target)

reaper = Reaper("Reaper")
aelita = Priest("Aelita")
nerfer = Alien("nerfer")