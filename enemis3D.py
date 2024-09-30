from OpenGL import GL
from OpenGL import GLU
from OpenGL import GLUT
import pyopengltk, math

verticies = (    (1, 0, 0),    (1, 1, 0),    (0, 1, 0),    (0, 0, 0),
                 (1, 0, 1),    (1, 1, 1),    (0, 0, 1),    (0, 1, 1)    )

edges = ((0,1), (0,3), (0,4), (2,1), (2,3), (2,7), (6,3), (6,4), (6,7), (5,1), (5,4), (5,7))

def Cube(x, y, z, size):
	GL.glTranslatef(x, y, z)
	GL.glBegin(GL.GL_LINES)
	for edge in edges:
		for vertex in edge:
			GL.glVertex3fv(
				(
					(verticies[vertex][0] - 0.5) * size,
					(verticies[vertex][1] - 0.5) * size,
					(verticies[vertex][2] - 0.5) * size,
				)
			)
	GL.glEnd()
	GL.glTranslatef(-x, -y, -z)

class Window(pyopengltk.OpenGLFrame):
	def __init__(self, master=None, cnf={}, entities={}, **args):
		super().__init__(master, cnf, **args)

		self.entities = entities
		self.angle = 0
		self.distance = 50

		self.center = (0, 0, 0)

	def angleMinus(self, event):
		if event.keycode == 68:
			self.angle -= 1
		elif event.keycode == 65:
			self.angle += 1
		elif event.keycode == 83:
			self.distance += 1
		elif event.keycode == 87:
			self.distance -= 1
		else:
			print(event.keycode)

	def initgl(self):
		GL.glLoadIdentity()
		GLU.gluPerspective(45, (self.width/self.height), 0.1, 1000.0)

	def redraw(self):
		GL.glClear(GL.GL_COLOR_BUFFER_BIT|GL.GL_DEPTH_BUFFER_BIT)

		GL.glPushMatrix()
		GLU.gluLookAt(
			math.cos(math.pi * self.angle / 180) * self.distance + self.center[0],
			20 + self.center[1],
			math.sin(math.pi * self.angle / 180) * self.distance + self.center[2],
			0 + self.center[0], 0 + self.center[1], 0 + self.center[2],
			0, 1, 0
		)

		GL.glRotate(1, 0, 1, 0)

		for index in self.entities:
			entity = self.entities[index]

			GL.glColor3f(*entity['color'])
			Cube(*entity['position'])

			# GL.glColor3f(0, 1, 1)
			# GL.glBegin(GL.GL_LINES)
			# for pose in cube['poses']:
			# 	GL.glVertex3fv(
			# 		pose[:3]
			# 	)
			# GL.glEnd()

		GL.glPopMatrix()
