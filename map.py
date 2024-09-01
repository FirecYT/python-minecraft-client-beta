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



		self.canvas.pack(fill='both', expand=True)

		self.canvas.create_line(250, 0, 250, 500, fill='red')
		self.canvas.create_line(0, 250, 500, 250, fill='blue')
