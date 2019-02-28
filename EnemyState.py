from State import *
import random

RELIGIONS = ["Сатанизм", "Христианство", "Коммунизм", "Атеизм", "Киберспорт"]
NAMES = ["Адольф", "Омарон", "Игилий", "Авкадий", "Дима", "Тимур"]

class EnemyState(State):
	def __init__(self, difficulty):
		State.count_of_states += 1

		self.hp = 10000*difficulty
		self.inWar = False
		self.ruler_is_sick = False

		self.territory = random.randint(25*difficulty, 100 * difficulty)

		self.lieges = 40 * (200/self.territory)
		self.army = 16 * (200/self.territory)
		self.smute = 0
		self.tax = 50
		self.harvest = 8000

		self.RELIGION = RELIGIONS[random.randint(0, len(RELIGIONS) - 1)]
		self.NAME = NAMES[random.randint(0, len(NAMES) - 1)]

	def weLost(self, state):
		state.lieges += self.lieges
		state.harvest += self.harvest
		this.defeated = True

	def toString(self):
		return (" ".join((self.hp, self.inWar, self.ruler_is_sick, self.territory, \
		self.lieges, self.army,	self.smute,	self.tax, self.harvest,	self.RELIGION, \
		self.NAME)))
