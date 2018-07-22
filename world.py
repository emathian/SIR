import agent as a
import random
class World:
	def __init__(self, w=10 , h =10 , nb=10, prop_inf = 0.2 , pi=0.2 , pr=0.5 , pd=0.5):
		self.w= w
		self.h = h
		self.nb = nb
		self.prop_inf = prop_inf
		self.pop = self.list_agent(pi, pr, pd)
		
		self.pi = pi
		self.rng = random.Random()
		#self.pr = pr
		#self.pd = pd
	def __str__(self):
		

		str_pop = []
		for agent in self.pop:
			str_pop.append(str(agent))
		return str(str_pop)	


	def list_agent(self, pi, pr, pd):
		my_list = []
		for i in range (1, self.nb +1):
			rng = random.Random()	
			proba_x= rng.randrange(1, self.w)
			proba_y = rng.randrange(1, self.h)

			rng2 = random.Random()	
			proba_statut = rng2.random()		
			if proba_statut < self.prop_inf: 
				proba_statut = "I"
			else:
				proba_statut = "S"

				

			my_list.append(a.Agent(proba_statut, proba_x, proba_y, pi, pr, pd))
		return my_list
			
	def move_everybody(self):
		for a in self.pop:
			a.move(self.w, self.h)
			
			

	def infect(self, obs_x, obs_y):
		self.obs_x = obs_x
		self.obs_y = obs_y
		same_pos_list = []
		for a in self.pop:
		
			if a.x == self.obs_x  and a.y== self.obs_y:
				#print(a)
				same_pos_list.append(a)
			
		
		count_infect = 0
		if len(same_pos_list) >=2:
			for a in same_pos_list:
				if a.statut == "I":

					count_infect += 1
				#else:
					#break
			#return count_infect 		
		if count_infect>0:
			for a in same_pos_list:
				if a.statut == "S":
					rng_infect = random.Random()
					if rng_infect < self.pi:
						a.staut = "I"
					else:
						a.staut = "S"
#				else:
#					break	
		#print(type(same_pos_list))
		same_pos_list_human=[]
		for a in same_pos_list:
			same_pos_list_human.append(str(a))
		
		return same_pos_list_human	
			
	def contact(self):
		contact_list = []
		for i in range(self.w):
			contact_list.append([])
			for j in range(self.h):
				contact_list[i].append([])
	

		for i in range(self.w):
			for j in range(self.h):
				for a in self.pop:
					if a.x==i and a.y== j:
						contact_list[i][j].append(str(a))
						#print("indentation")		
		return contact_list

	def recovery_or_die(self):
		for a in self.pop:
			a.recovered_or_die()



	def run (self):
		self.move_everybody()
		contact_list = self.contact()
		for i in range(self.w):
			for j in range(self.h):		
				if len(contact_list[i][j])>=2:
					self.infect(i ,j)
		self.recovery_or_die()
					
if __name__ == "__main__":
	
	my_world= World (100 ,100 , 500 , 0.6 , 0.2 , 0.1 , 0.5)
	#print(my_world )
	#print(type(my_world.pop))
	#print((my_world.pop[0]))
	my_world.move_everybody()
	#print ("		")
	print(my_world)
	#for a in my_world.pop:
	#	print(a.x)
	#print ("		")
	#print ("		")
	#print(type(my_world.pop[0].x))
	#print(type(my_world.pop[0]))
	#print(str(my_world))
	#print (my_world)
	#print ("		")
	#print ("		")
	#print(my_world.infect(6,1))
	#print(my_world.contact())

	#print(type(my_world.w))
	my_world.recovery_or_die()
	print(my_world)

	my_world.run()

	print("	")
	print(my_world)
	#print ("		")
	#print(my_world)
