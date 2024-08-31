import tkinter
from tkinter import ttk

class Window(tkinter.Frame, tkinter.Tk):
	def __init__(self, master=None, cnf={}, **args):
		super().__init__(master, cnf, **args)

		try:
			self.title('Map')
			self.geometry('500x500')
		except Exception:
			pass



		self.canvas = tkinter.Canvas(self, bg = '#eee')
		self.canvasLeft = tkinter.Canvas(self, bg = '#eee')
		self.canvasFront = tkinter.Canvas(self, bg = '#eee')
		scrollbar = ttk.Scrollbar(self, orient="vertical", command=self.canvas.yview)



		self.columnconfigure(index = 0, weight = 1)
		self.columnconfigure(index = 1, weight = 1)

		self.rowconfigure(index = 0, weight = 1)
		self.rowconfigure(index = 1, weight = 1)

		self.canvas.grid(row = 0, column = 0, sticky='nsew')
		self.canvasLeft.grid(row = 1, column = 0, sticky='nsew')
		self.canvasFront.grid(row = 1, column = 1, sticky='nsew')

		self.canvas.create_line(250, 0, 250, 500, fill='red')
		self.canvas.create_line(0, 250, 500, 250, fill='blue')

		self.canvasLeft.create_line(250, 0, 250, 500, fill='green')
		self.canvasLeft.create_line(0, 250, 500, 250, fill='red')

		self.canvasFront.create_line(250, 0, 250, 500, fill='green')
		self.canvasFront.create_line(0, 250, 500, 250, fill='blue')

		self.canvas["yscrollcommand"] = scrollbar.set
