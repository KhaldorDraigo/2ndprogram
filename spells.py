
class Heal():
	def __init__(self, power, name):
		self.power = power
		self.name = name

	def cast(self, target):
		(target).HP += self.power

class HealAll():
	def __init__(self, power, name):
		self.power = power
		self.name = name

	def cast(self, table):
		for hero in table:
			(hero).HP += self.power

class Dmg():
	def __init__(self, power, name):
		self.power = power
		self.name = name

	def cast(self, target):
		(target).HP -= self.power

class AOE():
	def __init__(self, power, name):
		self.power = power
		self.name = name

	def cast(self, table):
		for unit in table:
			(unit).HP -= self.power

class Buff():
	def __init__(self, power, name):
		self.power = power
		self.name = name

	def cast(self, target):
		(target).AD += self.power

class CC():
	def __init__(self, power, name):
		self.power = power
		self.name = name

	def cast(self, target):
		(target).turn -= self.power
		



combo = Dmg(120, "combo")
legend = Dmg(250, "legend")
remedy = Heal(200, "remedy")
revitalize = HealAll(130, "revitalize")
judgement = Dmg(100, "judgement")
temper = Buff(30, "temper")
mindbreak = Dmg(300, "mindbreak")
terrify = CC(2, "terrify")
mend = Heal(150, "mend")
bash = CC(1, "bash")
fireball = Dmg(80, "fireball")
rend = Dmg(120, "rend")