from tiny_3d_engine import (Scene3D, Engine3D)
import tkinter

points = list()
conn = list()
index = 0

def cube(x, z, y, size):
	global index

	points.append([1 * size + x, 1 * size + y, 0 * size + z]) # 0
	points.append([0 * size + x, 1 * size + y, 0 * size + z]) # 1
	points.append([0 * size + x, 0 * size + y, 0 * size + z]) # 2
	points.append([1 * size + x, 0 * size + y, 0 * size + z]) # 3
	points.append([1 * size + x, 0 * size + y, 1 * size + z]) # 4
	points.append([0 * size + x, 0 * size + y, 1 * size + z]) # 5
	points.append([0 * size + x, 1 * size + y, 1 * size + z]) # 6
	points.append([1 * size + x, 1 * size + y, 1 * size + z]) # 7

	conn.append([0 + index, 1 + index, 2 + index, 3 + index])
	conn.append([0 + index, 1 + index, 6 + index, 7 + index])
	conn.append([0 + index, 3 + index, 4 + index, 7 + index])
	conn.append([1 + index, 2 + index, 5 + index, 6 + index])
	conn.append([2 + index, 3 + index, 4 + index, 5 + index])
	conn.append([4 + index, 5 + index, 6 + index, 7 + index])

	index += 8

if __name__ == "__main__":
	angle = 0

	root = tkinter.Tk()

	scene = Scene3D()

	cube(0, 0, 0)
	cube(1, 0, 0)
	cube(2, 0, 0)
	cube(0, 1, 0)
	cube(0, 2, 0)
	cube(0, 0, 1)
	scene.update("squares", points, conn, color="#ff0000")
	cube(0, 0, 5)
	scene.update("squares", points, conn, color="#ffff00")

	test = Engine3D(scene, root, 200, 200)
	test.rotate("y", 45)
	test.rotate("x", 30)
	test.render()

	while True:
		test.clear()
		test.rotate("y", 1)
		test.render()

		root.update()
