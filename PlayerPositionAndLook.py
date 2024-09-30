import tkinter

class Window(tkinter.Frame, tkinter.Tk):
	def __init__(self, master=None, cnf={}, **args):
		super().__init__(master, cnf, **args)

		try:
			self.title('Map')
			self.geometry('500x500')
		except Exception:
			pass

		self.x_frame = tkinter.Frame(self, borderwidth=1, relief='solid')
		self.y_frame = tkinter.Frame(self, borderwidth=1, relief='solid')
		self.z_frame = tkinter.Frame(self, borderwidth=1, relief='solid')

		self.x_scale = tkinter.Scale(self.x_frame, orient = 'horizontal', from_ = 0, to = 100)
		self.x_add = tkinter.Button(self.x_frame, text = '+', width=4)
		self.x_dda = tkinter.Button(self.x_frame, text = '-', width=4)

		self.y_scale = tkinter.Scale(self.y_frame, orient = 'horizontal', from_ = 0, to = 100)
		self.y_add = tkinter.Button(self.y_frame, text = '+', width=4)
		self.y_dda = tkinter.Button(self.y_frame, text = '-', width=4)

		self.z_scale = tkinter.Scale(self.z_frame, orient = 'horizontal', from_ = 0, to = 100)
		self.z_add = tkinter.Button(self.z_frame, text = '+', width=4)
		self.z_dda = tkinter.Button(self.z_frame, text = '-', width=4)

		self.label_x = tkinter.Label(self.x_frame, text='x', justify = 'left')
		self.label_y = tkinter.Label(self.y_frame, text='y', justify = 'left')
		self.label_z = tkinter.Label(self.z_frame, text='z', justify = 'left')

		self.label_yaw = tkinter.Label(self, text='yaw', justify = 'left')
		self.label_pitch = tkinter.Label(self, text='pitch', justify = 'left')
		self.label_flags = tkinter.Label(self, text='flags', justify = 'left')
		self.label_teleport_id = tkinter.Label(self, text='teleport_id', justify = 'left')
		self.label_dismount_vehicle = tkinter.Label(self, text='dismount_vehicle', justify = 'left')



		self.x_frame.pack(fill = 'both')
		self.y_frame.pack(fill = 'both')
		self.z_frame.pack(fill = 'both')

		self.x_frame.columnconfigure(index = 0, weight = 0)
		self.x_frame.columnconfigure(index = 1, weight = 1)
		self.x_frame.columnconfigure(index = 2, weight = 0)
		self.x_frame.columnconfigure(index = 3, weight = 0)

		self.y_frame.columnconfigure(index = 0, weight = 0)
		self.y_frame.columnconfigure(index = 1, weight = 1)
		self.y_frame.columnconfigure(index = 2, weight = 0)
		self.y_frame.columnconfigure(index = 3, weight = 0)

		self.z_frame.columnconfigure(index = 0, weight = 0)
		self.z_frame.columnconfigure(index = 1, weight = 1)
		self.z_frame.columnconfigure(index = 2, weight = 0)
		self.z_frame.columnconfigure(index = 3, weight = 0)

		self.label_x.grid(row = 0, column = 0, sticky = 'nsew')
		self.label_y.grid(row = 0, column = 0, sticky = 'nsew')
		self.label_z.grid(row = 0, column = 0, sticky = 'nsew')

		self.x_scale.grid(row = 0, column = 1, sticky = 'nsew')
		self.y_scale.grid(row = 0, column = 1, sticky = 'nsew')
		self.z_scale.grid(row = 0, column = 1, sticky = 'nsew')

		self.x_add.grid(row = 0, column = 2, sticky = 'nsew')
		self.y_add.grid(row = 0, column = 2, sticky = 'nsew')
		self.z_add.grid(row = 0, column = 2, sticky = 'nsew')

		self.x_dda.grid(row = 0, column = 3, sticky = 'nsew')
		self.y_dda.grid(row = 0, column = 3, sticky = 'nsew')
		self.z_dda.grid(row = 0, column = 3, sticky = 'nsew')

		self.label_yaw.pack(fill = 'both')
		self.label_pitch.pack(fill = 'both')
		self.label_flags.pack(fill = 'both')
		self.label_teleport_id.pack(fill = 'both')
		self.label_dismount_vehicle.pack(fill = 'both')
