from Ruler import *
from State import *

class PlayerState(State):
	def __init__(self):
		ruler = Ruler()
		
		State.count_of_states += 1

		self.inWar = False
		self.ruler_is_sick = False
		self.hp = ruler.hp
		self.gold = ruler.gold
		self.faith = ruler.faith
		self.humidity = ruler.humidity
		self.territory = ruler.territory

		self.seeded = 0

		self.lieges = 40
		self.army = 0
		self.smute = 0
		self.tax = 50
		self.harvest = 8000

		self.RELIGION = input("Какой религии придерживаетесь?: ")
		self.NAME = input("Имя вашего правителя?: ")

	def getReligion(self):
		return self.RELIGION

	def getName(self):
		return self.Name
    
	def endWar(self, state):
		if self.inWar:
			print("Уже воюем")
			return

		state.inWar = False
		self.inWar = False

	def declareWar(self, state):
		state.inWar = True
		self.inWar = True
    
	def giveOut(self, count):
		self.harvest -= count
		self.faith += 20 * (1 - self.faith/100)

	def recruit(self, count):
		self.lieges -= count
		self.army += count

	def setTax(self, tax):
		self.tax = tax
            
	def setHarvest(self,harvest):
		self.harvest = harvest

	def seed(self, count):
		self.seeded += count
		self.territory -= count
