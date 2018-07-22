import tkinter as tk
import world
import agent

class WorldView(tk.Canvas):
	def __init__(self, parent):
		tk.Canvas.__init__(self, parent, width = 400, height = 400, highlightthickness=0, bg = "black")
		self.size_in_pixels = 400

	def draw_grid (self, grid_size):
		self.w = grid_size
		self.h = grid_size
		self.intervalle = int(self.size_in_pixels)/self.w
		for i in range(self.h+1):
			self.create_line(0,i*self.intervalle, self.w*self.intervalle , i*self.intervalle, fill="#3c3c3c")

		for j in range(self.w+1):
			self.create_line(j*self.intervalle, 0, j*self.intervalle, self.h*self.intervalle, fill="#3c3c3c", width=0)





mafenetre = tk.Tk()
mafenetre.title("SIR simulation")

my_world_view = WorldView(mafenetre)
my_world_view .pack()

myworld= world.World(20, 20, 50 , 0.2 , 1 , 0.001 , 0.001)
my_world_view.draw_grid(20)

monbouton2 = tk.Button(mafenetre, text='Quitter', command = mafenetre.destroy) 
monbouton2.pack()
mafenetre.mainloop()

