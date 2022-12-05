from spells import *

class Goblin():
	def __init__(self, name):
		self.HP = 200
		self.AD = 10
		self.turn = 1
		self.name = name

	def attack(self, target):
		(target).HP -= self.AD

class Goblin_Warrior(Goblin):
	def __init__(self, name):
		self.HP = 400
		self.AD = 20
		self.turn = 1
		self.name = name
		self.spells = [bash]

	def use_spell(self, target, spell_number):
		(self.spells[spell_number - 1]).cast(target)

class Goblin_Shaman(Goblin):
	def __init__(self, name):
		self.HP = 400
		self.AD = 10
		self.turn = 1
		self.name = name
		self.spells = [fireball]

	def use_spell(self, target, spell_number):
		(self.spells[spell_number - 1]).cast(target)


class Orc():
	def __init__(self, name):
		self.HP = 450
		self.AD = 65
		self.turn = 1
		self.name = name

	def attack(self, target):
		(target).HP -= self.AD

class Orc_Warrior(Orc):
	def __init__(self, name):
		self.HP = 750
		self.AD = 80
		self.turn = 1
		self.name = name
		self.spells = [rend]

	def use_spell(self, target, spell_number):
		(self.spells[spell_number - 1]).cast(target)

