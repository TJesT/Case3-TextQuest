from math import randint
class Event: #Negative
	def get_sick(self, state):
		  state.ruler_is_sick = True
		  print("get_sick (current hp)", state.ruler_hp)
		  return state.ruler_is_sick
	def declare_war(self, state, CTS): #State.declare_wa
		if randint(0, 50) == 0:
			  print("declared_war")# balance this 
		if (CTS):
			  diff = 0 * 5
		else :
			  deff = 1
		if (state.army * state.faith * (1 - state.smute) % (200 + randint(0, 50)) > 30 * diff && state.harvest > 100:
				print("win") 
				state.army = int(state.army * 0.8) 
				state.lieges = int(state.lieges * 1.05) 
				state.gold += 500 state.land += 50
		else :
				print("lose")
				state.army = int(state.army * 0.6) 
				state.lieges = int(state.lieges * 0.9) 
				state.gold -= 1000 state.land -= 100
		return state
	def rats(self, state):
		if randint(0, 50) == 0:
			state.harvest -= math.randint(500) print("rats") 
		return state.harvest
	def meteor(self, state):
	  if randint(0, 50) == 0:
			if (input("meteor_gold_or_lieges") == "1"):
				state.gold -= math.randint(500)
				return state
			else :
				state.lieges -= math.randint(500, 700)
				return state
	  def disorder(self, state):
		if randint(0, 50) == 0:
			state.smute += math.randint(15, 20) 
				print("smute", state.smute) 
			return state.smute
	# Positive
	  def bless(self, state):
		if randint(0, 50) == 0:
			state.faith += math.randint(10, 20) 
				print("bless ", state.faith) 
		return state.faith
	  def good_harvest(self, state):
		if randint(0, 50) == 0:
			state.harvest += math.randint(100, 200) 
				print("good_harvest ", state.harvest) 
		return state.harvest
	  def chanceToStrike(self, state):
		if randint(0, 50) == 0:
			if (input("strike?(0,1)") == 1):
			state = state.declare_war(state, True)
			return state
		else :
			return state
	  def relief(self,state):
		if randint(0, 50) == 0:
				state.ruler_is_sick = False 
				print("relief (current hp)", state.ruler_hp) 
				return state.ruler_sick
	  def prosper(self,state):
		if randint(0, 50) == 0:
			state.smute -= math.randint(15, 20) 
			state.gold += math.randint(150, 200) 
			state.faith += math.randint(10, 20) 
			state.faith %= 100 print("prosper(smute,faith)", state.smute, state.faith) 
		return state
class Game:
	def start():
		state = State(Ruler())
  		enemies = [] enemies.append()
  		while (True):
			if state.hp <= 0 or state.territory + state.seeded <= 0 or state.smute >= 100 %:
				print("u_lost")
				state.seed(state.harvest + int(input("Skolko seyat?")) 
				state.giveOut(int(input("Skolko kushac?")) 
				state.sellHarvest(int(input())) state.recruit(int(input())) state.collect() if state.ruler_is_sick:
			state.hp -= 100
			if randint(0, 10) == 0:
				event().relief()
			else :
				if randint(0, 30) == 0:
					event().get_sick() 
			event().meteor(state)
			event().rats(state)
			event().disorder(state)							
			event().prosper(state)
			#events...
																																						 
																																						 
