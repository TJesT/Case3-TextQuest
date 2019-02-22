import random

RELIGIONS = ["Сатанизм", "Христианство", "Коммунизм", "Атеизм", "Киберспорт"]
NAMES = ["Адольф", "Омарон", "Игилий", "Авкадий", "Дима", "Тимур"]

class EnemyState:
	def __init__(self, difficulty):
		self.hp = 10000*difficulty
		self.inWar = False
		self.ruler_is_sick = False

		self.territory = random.randint(50, 200)

		self.lieges = 40 * (200/self.territory)
		self.army = 16 * (200/self.territory)
		self.smute = 0
		self.tax = 50
		self.harvest = 8000

		self.RELIGION = RELIGIONS[random.randint(0, len(RELIGIONS) - 1)]
		self.NAME = NAMES[random.randint(0, len(NAMES) - 1)]

  def declareWar(self, state):
    self.inWar = True
    state.inWar = True

	def weLost(self, state):
		state.lieges += self.lieges
		state.harvest += self.harvest
    state.inWar = False
