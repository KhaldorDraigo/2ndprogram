
#importing modules from files
import random
from typing import Type
from spells import *
from heroes import *
from monsters import *

#creating tables for iterations
hero_table = [reaper, aelita, nerfer]
heroes_with_move = [reaper, aelita, nerfer]

#creating instances of monsters
jaini = Goblin("Jaini")
zaini = Goblin("Zaini")
nula = Goblin_Warrior("Nula")

#creating tables for monsters
monster_table = [jaini, zaini, nula]
monsters_with_hp = [jaini, zaini, nula]

#creating function to select hero to move
def select_hero():

	#making loop that will continue to ask user until the proper input is used
	while True:
			movable = {"None": "None"}
			i = 0
			for hero in heroes_with_move:
				print("use %d to move with %s" % ( (i + 1)  , (hero).name ) )
				movable[i] = hero
				i += 1

			#asking user who he wants to move with
			number = input("please select hero you want to move: " )

			#we try to assign proper hero to move with
			try:
				hero_to_move = movable[ int(number) - 1 ]

			#we tell if user input is incorrect and tell him to use numbers given and continue to ask if he did so
			except(TypeError, IndexError):
				print("please use numbers given")
				continue

			#if everything is fine we return the hero that will move
			finally:
				return hero_to_move

#we create function that will make user select monster that he wants to attack
def select_monster_to_attack():

	#we make loop making sure input user made is proper and until its not we continue to ask him
	while True:

		#we make handy loop to print to user all the monsters that are on battlefield
		for monster in monsters_with_hp:
			print("%d: %s" % (monsters_with_hp.index(monster) + 1, (monster).name ) )

		try:

			#we ask user to type number that will corespond to selected monster
			number = input("select target: ")
			attacked_monster = monsters_with_hp[ int(number) - 1 ]

		#in case user did not use correct number we tell him to do so
		except(IndexError, TypeError):
			print("use given numbers")
			continue

		#we end function returning monster that he will attack
		finally:
			return attacked_monster


#we create funtion to make user select hero to assist
def select_hero_to_assist():

	#we create loop making sure user will use correct number otherwise returning to asking to do so
	while True:
		#we make handy loop that will print the heroes that can be selected to assist
		for hero in hero_table:
			print("%d to assist %s" % (hero_table.index(hero) + 1, (hero).name )  )

		number = input("select number: ")

		try:
			assisted = hero_table[int(number) - 1]

		except(TypeError, IndexError):
			print("please use numbers given")

		finally:
			return assisted

#we create function that will execute one hero move
def hero_move():
	#we choose hero that will be taking turn
	selected_hero = select_hero()

	#we create loop that will ask what action to perform until the input is correct
	while True:
			
			#we assign variables to the spells
			spell1 = (selected_hero).spells[0]
			spell2 = (selected_hero).spells[1]
			spell3 = (selected_hero).spells[2]
			spells = [spell1, spell2, spell3]

			#we ask what action person wants to do
			action = input("type A: attack, 1: %s  2: %s  3: %s: " % ( (spell1).name , (spell2).name, (spell3).name ) )

			#if user chose to attack they'll do
			if (action == "A") or (action == "a"):
				target = select_monster_to_attack()
				move = "hero used attack"
				(selected_hero).attack(target)
				heroes_with_move.remove(selected_hero)
				break

			try:
				action = int(action)

			# if user didnt choose A and after convertion into number we get errors we print this
			except(ValueError):
				print("if not selecting attack please use numbers")
				continue


			#when input is ok we start to check what action was taken
			finally:
				if (action == 1) or (action == 2) or (action == 3):

					#for user convinience we use numbers from 1 to 3 and assign variable for later
					spell = spells[action - 1]


					#if spell is assistance type we make user select hero to assist
					if ( isinstance( spell, Heal ) ) or ( isinstance( spell, Buff ) ):
						target = select_hero_to_assist()
						(selected_hero).use_spell(target, action)
						heroes_with_move.remove(selected_hero)
						print("hero cast spell: %s" % (spell.name) )
						return True

					#if spell is dmg type we make user select monster to attack
					if ( isinstance( spell, Dmg ) ) or ( isinstance( spell, CC ) ):
						target = select_monster_to_attack()
						(selected_hero).use_spell(target, action)
						heroes_with_move.remove(selected_hero)
						print("hero cast spell: %s" % (spell.name) )
						return True


					#if spell attacks all we dont need all the inputs
					if ( isinstance( spell, AOE ) ):
						table = monster_table
						(selected_hero).use_spell(table, action)
						heroes_with_move.remove(selected_hero)
						print("hero cast spell: %s" % (spell.name) )
						return True


					#if spell heals all we dont need the all inputs
					if ( isinstance( spell, HealAll) ):
						table = hero_table
						(selected_hero).use_spell(table, action)
						heroes_with_move.remove(selected_hero)
						print("hero cast spell: %s" % (spell.name) )
						return True

				#reminding that heroes only have 3 spells
				else:
					print("please use numbers from 1 to 3")


#we check and delete the monsters without hp
def remove_dead_monsters():
	for monster in monsters_with_hp:
		if monster.HP <= 0:
			monsters_with_hp.remove(monster)

#we remove heroes without hp
def remove_dead_heroes():
	for hero in hero_table:
		if hero.HP <= 0:
			hero_table.remove(hero) 

#defining heroes turn function
def heroes_turn():
	while len(heroes_with_move) >= 1:
		hero_move()
		remove_dead_monsters()

#defining monsters turn function
def monsters_turn():
	for monster in (monsters_with_hp):
		if ( isinstance( monster, Goblin ) ):
			target = (random.sample(hero_table, 1))[0]
			monster.attack(target)
			print("monster attacked for %d" % monster.AD)

		elif ( isinstance( monster, Goblin_Warrior ) ):
			if random.randint(1,3) == 3:
				spell = monster.spells[0]
				target = (random.sample(hero_table, 1))[0]
				monster.use_spell(target, 1)
				print("hero cast spell: %s" % (spell.name) )
			else:
				target = (random.sample(hero_table, 1))[0]
				monster.attack(target)
				print("monster attacked for %d" % monster.AD)

	check_dead_heroes
	return True

while len(monsters_with_hp) > 0:
	heroes_turn()
	monsters_turn()
	heroes_with_move = hero_table
