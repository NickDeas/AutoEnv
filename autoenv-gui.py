import tkinter as tk
from tkinter import font
from envManager import EnvManager
import os

class AEApplication(tk.Frame):

	#Color Scheme Constants
	P_RED 	= '#A0031D'
	P_GREY 	= '#A4B6AF'
	S_GREY 	= '#564D4A'
	S_BLUE 	= '#001427'
	S_PURP	= '#5B2333'

	HEIGHT = 800
	HEADER_R = 0.15

	def __init__(self, parent, *args, **kwargs):
		tk.Frame.__init__(self, parent, *args, **kwargs)
		self.parent = parent


		#Header--------------------------------------------------------
		header = tk.Frame(parent, 
			bg = self.P_RED)
		header.pack(fill = tk.X, side = tk.TOP)

		title = tk.Label(header, 
			text = "AutoEnv",
			height = 2,
			font = font.Font(family = "Lucida Grande", size = 20),
			fg = 'white',
			bg = self.P_RED)
		title.pack()

		#Body----------------------------------------------------------
		body = tk.Frame(parent,
			height = (1-self.HEADER_R)*self.HEIGHT,
			bg = self.P_GREY)
		body.pack(fill = tk.BOTH, side = tk.TOP)

		envs = self.listEnvs()
		env_buttons = []
		for env in envs:
			new_button = tk.Button(body,
				text = env,
				font = font.Font(family = 'Lucida Grande', size = 10),
				bg = 'white')
			new_button.pack(side = tk.TOP, pady = 10, padx = 10)
			env_buttons.append(new_button)


	def listEnvs(self):
		envs = [env[:-5] for env in os.listdir('./saved-envs/')]
		return envs



if __name__ == "__main__":
	root = tk.Tk()
	AEApplication(root).pack(side="top", fill="both", expand=True)
	root.mainloop()