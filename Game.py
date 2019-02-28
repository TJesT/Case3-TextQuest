from math import randint
from EnemyState import *
from PlayerState import *

class Game:
	def start(self):
		state = PlayerState(Ruler())
		enemies = [EnemyState(1), EnemyState(1), EnemyState(1)] 
		
		while (True):
			if state.hp <= 0 or state.territory + state.seeded <= 0 or state.smute >= 100 :
				print("u_lost")
				state.seed(state.harvest + int(input("Skolko seyat? - ")))
				state.giveOut(int(input("Skolko kushac? - ")))
				state.sellHarvest(int(input()))
				state.recruit(int(input())) 
				state.collect() 
			if state.ruler_is_sick:
				state.hp -= 100
			if randint(0, 10) == 0:
				event().relief()
			elif randint(0, 30) == 0:
				event().get_sick(state)
			event().meteor(state)
			event().rats(state)
			event().disorder(state)
			event().prosper(state)
