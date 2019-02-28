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

	def __str__(self):
		return (" ".join(map(str, (self.hp, self.inWar, self.ruler_is_sick, self.territory, \
		self.lieges, self.army,	self.smute,	self.tax, self.harvest,	self.RELIGION, \
		self.NAME))))
