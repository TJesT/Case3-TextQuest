class Game:
	def start():
		state=State(Ruler())
		enemies = []
		enemies.append()
		
		while(True):
			if state.hp<=0 or state.territory+state.seeded<=0 or state.smute>=100%:
				break
			state.seed(state.harvest+int(input("Skolko seyat?"))
			state.giveOut(int(input("Skolko kushac?"))
			state.sellHarvest(int(input()))
			state.recruit(int(input()))
			state.collect()
			if state.ruler_is_sick:
				state.hp-=100
			event().relief()
			event().get_sick()
			event().meteor()
			event().bless()
