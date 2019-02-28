class State:
	count_of_states = 0
	defeated = False
	
	def printInfo(self):
		print("Религия:", self.RELIGION)
		print("Имя:", self.NAME)
		print("Урожай:", self.harvest)
		print("Подданые:", self.lieges)
		print("Армия:", self.army)
		print("Территории:", self.territory)
