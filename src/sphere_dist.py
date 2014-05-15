import scipy.constants as const
import numpy.random as Random


from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np

# consider making this part of the constructor of Point
def random():
	return 2 * (Random.random() - 0.5)

class Point:
	"""A simple Point class with x,y and z coordinates and some useful methods"""
	def __init__(self, x, y, z):
		self.x = x
		self.y = y
		self.z = z

	def module(self):
		return ( self.x**2 + self.y**2 + self.z**2 )**(0.5)

	def standarize(self):	
		module = float(self.module())
		self.x /= module
		self.y /= module
		self.z /= module
		return self

	def show(self):
		print self.x
		print self.y
		print self.z


# Consider doing numpy arrays instead of python native list
# It could be more performant with numpy
Sphere = []
X = []
Y = []
Z = []

# Create random points
for i in range(270):
	p = Point(random(), random(), random())
	Sphere.append(  p.standarize()  )
	X.append(p.x)
	Y.append(p.y)
	Z.append(p.z)


# Show the distribution

# Doc
# http://matplotlib.org/1.3.1/mpl_toolkits/mplot3d/tutorial.html#mpl_toolkits.mplot3d.Axes3D.scatter
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(X, Y, Z, c='b', marker='o')

ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

plt.show()
