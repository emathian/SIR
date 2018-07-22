import random
class Agent:
	

	#Attribu de la classe
	rng=random.Random()
	def __init__(self, statut="I", x=0 , y=0 , pi=0.2, pr= 0.4, pd=0.4): #####" On suppose que l'initiation est au depart
############################ Deplacement 
		self.x= x
		self.y = y
#################################### Probabilite
		self.statut = statut 		
		self.pi = pi
		self.pr = pr
		self.pd = pd
	

	def __str__(self):
		return "({0} , {1} , {2} , {3}, {4} , {5})".format(self.statut, self.x, self.y, self.pi, self.pr, self.pd)   	
	def move(self, w, h):
		rng = random.Random()
		direction = rng.randrange(1,5)
####### Deplacement horizontale vers la droite direction == 1
####### Deplacement horizontale vers la gauche direction == 2
###### Deplacement horizontale vers haut direction == 3
###### Deplacement horizontale vers bas direction == 4
		new_pos_x = self.x
		new_pos_y = self.y
		if direction == 1:
			if new_pos_x < w :
				new_pos_x= self.x +1
				self.x = new_pos_x
			else:
				new_pos_x = 0
				self.x = 0

		if direction == 2:
			if new_pos_x > 0 :
				new_pos_x= self.x - 1
				self.x = new_pos_x
			else:
				new_pos_x = w-1
				self.x = w-1

		if direction == 3:
			if new_pos_y > 0 :
				new_pos_y= self.y - 1
				self.y = new_pos_y
			else:
				new_pos_y = h-1
				self.y = h-1
		if direction == 4:
			if new_pos_y <h :
				new_pos_y= self.y + 1
				self.y = new_pos_y
			else:
				new_pos_y = 0
				self.y = 0
		

	def recovered_or_die (self):
		if self.statut == "I":
			#rng = random.Random()
			#statut = rng.random()
			if Agent.rng.random() <= self.pr:
				self.statut = "R"
			else:
				if Agent.rng.random() <= self.pd:
					self.statut = "D"
	
	

				
  
	
if __name__=="__main__":
	individu1 = Agent("I",1,1 ,0.3 , 0.6 , 0.4)
	print(individu1.x, individu1.y, individu1.pi)
	individu1.move(10 , 10)
	print (individu1.x, individu1.y)
	individu1.recovered_or_die()
	print('recovered_or_die', individu1.statut)
	individu2 = Agent()
	print (individu2.x)
	
