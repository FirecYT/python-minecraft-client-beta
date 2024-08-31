import tkinter

class Window(tkinter.Frame, tkinter.Tk):
	def __init__(self, master=None, cnf={}, **args):
		super().__init__(master, cnf, **args)

		try:
			self.title('Map')
			self.geometry('500x500')
		except Exception:
			pass

		self.label_x = tkinter.Label(self, text='x', justify = 'left')
		self.label_y = tkinter.Label(self, text='y', justify = 'left')
		self.label_z = tkinter.Label(self, text='z', justify = 'left')
		self.label_yaw = tkinter.Label(self, text='yaw', justify = 'left')
		self.label_pitch = tkinter.Label(self, text='pitch', justify = 'left')
		self.label_flags = tkinter.Label(self, text='flags', justify = 'left')
		self.label_teleport_id = tkinter.Label(self, text='teleport_id', justify = 'left')
		self.label_dismount_vehicle = tkinter.Label(self, text='dismount_vehicle', justify = 'left')

		self.label_x.pack(fill = 'both')
		self.label_y.pack(fill = 'both')
		self.label_z.pack(fill = 'both')
		self.label_yaw.pack(fill = 'both')
		self.label_pitch.pack(fill = 'both')
		self.label_flags.pack(fill = 'both')
		self.label_teleport_id.pack(fill = 'both')
		self.label_dismount_vehicle.pack(fill = 'both')
