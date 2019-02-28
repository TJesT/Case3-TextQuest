from random import randint

from EnemyState import *
from PlayerState import *
from Event import *

class Game:
	def start(self):
		self.seeded = False
		self.seed_count = 0
		state = PlayerState()
		enemies = [EnemyState(1), EnemyState(1), EnemyState(1)] 
		
		while (True):
			state.printInfo()
			if state.hp <= 0 or state.territory + state.seeded <= 0 or state.smute >= 100 :
				print("u_lost")
			if not self.seeded:
				if input("\nСеем урожай? (+/-)") == '+':
					self.seeded = True
					state.seed(state.harvest + int(input("Skolko seyat? > ")))
			else:
				self.seed_count += 1
			state.giveOut(int(input("Skolko kushac? > ")))
			#state.setHarvest(state.harvest - int(input()))
			if input("Нанимает бойцов? (+/-)") == '+':
				state.recruit(int(input("Сколько?")))
			if self.seed_count > 10:
				if input("Собираем урожай?") == '+':
					state.collect()
					self.seed_count = 0
					self.seeded = False
			if state.ruler_is_sick:
				state.hp -= 1000
			if randint(0, 10) == 0:
				Event().relief(state)
			elif randint(0, 30) == 0:
				Event().get_sick(state)
			
			Event().meteor(state)
			Event().rats(state)
			Event().disorder(state)
			Event().prosper(state)

			state.hp -= 1000
			input("\nПрошёл один месяц. Для продолжения нажмите любую клавишу\n")
			
