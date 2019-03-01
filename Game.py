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
			if state.lieges <= 0:
				print("sasat")
				break
			if state.hp <= 0:
				print("Победа! Ты прошёл игру")
				break
			if state.territory + state.seeded <= 0:
				print("Проигрыш! Ты никчёмный правитель")
				break
			if state.smute >= 100 :
				print("Поражение!!! Тебя свергли!")
				break

			state.printInfo()

			if not self.seeded:
				if input("\nСеем урожай? (+/-)") == '+':
					while True:
						d = input("Сколько сеять >")
						try:
							d = int(d)
						except ValueError:
							print("Wrong format")
							continue
						if d > 0:
							self.seeded = True
							state.seed(state.harvest + d)
							break
					
			else:
				self.seed_count += 1
			if input("Раздаём подданным? (+/-)") == '+':
				while True:
					d = input("Skolko kushac? > ")
					try:
						d = int(d)
					except ValueError:
						print("Wrong format")
						continue
					if d > 0:
						state.giveOut(вd)
						break
				
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
			input("\nПрошёл один месяц. Для продолжения нажмите клавишу ввода\n")
			
