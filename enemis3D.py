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
					verticies[vertex][0] * size - 0.5,
					verticies[vertex][1] * size - 0.5,
					verticies[vertex][2] * size - 0.5,
				)
			)
	GL.glEnd()
	GL.glTranslatef(-x, -y, -z)

class Window(pyopengltk.OpenGLFrame):
	def __init__(self, master=None, cnf={}, **args):
		super().__init__(master, cnf, **args)

		self.cubes = [
			(0, 0, 0, 1, (1, 0, 0))
		]
		self.timer = 0

	def initgl(self):
		GL.glLoadIdentity()
		GLU.gluPerspective(45, (self.width/self.height), 0.1, 1000.0)

	def redraw(self):
		GL.glClear(GL.GL_COLOR_BUFFER_BIT|GL.GL_DEPTH_BUFFER_BIT)

		GL.glPushMatrix()
		GLU.gluLookAt(
			math.cos(math.pi * self.timer / 180) * 50,
			0,
			math.sin(math.pi * self.timer / 180) * 50,
			0, 0, 0,
			0, 1, 0
		)

		GL.glRotate(1, 0, 1, 0)

		GL.glColor3f(1, 1, 1)
		for cube in self.cubes:
			GL.glColor3f(*cube[4])
			Cube(*cube[:4])

		GL.glPopMatrix()
		self.timer += 1
