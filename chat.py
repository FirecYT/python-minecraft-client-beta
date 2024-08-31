import tkinter

class Window(tkinter.Frame, tkinter.Tk):
	def __init__(self, master=None, cnf={}, **args):
		super().__init__(master, cnf, **args)

		try:
			self.title('Map')
			self.geometry('500x500')
		except Exception:
			pass



		self.text = tkinter.Text(self, bg = '#333', fg='white', font="Arial 12 bold roman")
		self.input = tkinter.Entry(self, bg = '#eee')
		self.button = tkinter.Button(self, text='Отправить')



		self.columnconfigure(index = 0, weight = 1)
		self.columnconfigure(index = 1, weight = 0)

		self.rowconfigure(index = 0, weight = 1)
		self.rowconfigure(index = 1, weight = 0)

		self.text.grid(row = 0, column = 0, columnspan = 2, sticky = 'nsew', padx=8, pady=8)
		self.input.grid(row = 1, column = 0, sticky = 'nsew', padx=8, pady=8)
		self.button.grid(row = 1, column = 1, sticky = 'nsew', padx=8, pady=8)

		self.text.tag_config('bold', font="Impact 12 bold roman")
		self.text.tag_config('underlined', underline=True)
		self.text.tag_config('strikethrough', overstrike=True)
		self.text.tag_config('obfuscated', background="#666")

		self.text.tag_config('color_blue', foreground="#55f")
		self.text.tag_config('color_green', foreground="#5f5")
		self.text.tag_config('color_cyan', foreground="#5ff")
		self.text.tag_config('color_red', foreground="#f55")
		self.text.tag_config('color_pink', foreground="#f5f")
		self.text.tag_config('color_yellow', foreground="#ff5")
		self.text.tag_config('color_white', foreground="#fff")
