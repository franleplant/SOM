import scipy.constants as const
import numpy.random as Random
from numpy import linalg as LA


from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np


MAX_POINT_NUMBER = 10


# Use this instead of Point classs
# http://docs.scipy.org/doc/numpy/reference/generated/numpy.recarray.html

# TODO: Replace the Point class to just plain multidimensional arrrays

# consider making this part of the constructor of Point
def random():
	return 2 * (Random.random() - 0.5)

class Point:
	"""A Point class with x,y and z coordinates and some useful methods"""
	def __init__(self, x=0, y=0, z=0):
		self.vector = np.array([x, y, z])

	@property
	def x(self):
	    return self.vector[0]
	@x.setter
	def x(self, value):
	    self.vector[0] = value

	@property
	def y(self):
	    return self.vector[1]
	@y.setter
	def y(self, value):
	    self.vector[1] = value

	@property
	def z(self):
	    return self.vector[2]
	@z.setter
	def z(self, value):
	    self.vector[2] = value
	
	@property
	def vector(self):
	    return self.vector
	@vector.setter
	def vector(self, value):
	    self.vector = value


	def module(self):
		return LA.norm([self.x,self.y,self.z])

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

# Create random points
for i in range( MAX_POINT_NUMBER ):
	p = Point(random(), random(), random())
	Sphere.append(  p.standarize()  )



MAX_ITERATION = 10

#Time step (delta t)
dltt = 0.1                  
for iteration in range(MAX_ITERATION):

	for neuron_i_point in np.nditer(Sphere, op_flags=['readwrite']):

	#for i in range( MAX_POINT_NUMBER ):
		# Electrostatic Force Repulsion
		# This will hold the total net Force vector
		# pointing towards the direction
		# on which the neuron_i will be moving
		Fer_i = Point()

		#Diagnosis
		cos_ij_max = -1


		neuron_i = neuron_i_point.vector


		for neuron_j_point in np.nditer(Sphere):

		#for j in range( MAX_POINT_NUMBER ):

			neuron_j = neuron_j_point.vector

			distance = Point()
			distance.vector = neuron_i - neuron_j
			distance_mod = distance.module()

			#Diagnosis
			cos_ij = 0

			if distance_mod > 0:
				Fer_i.vector += (distance.vector / distance_mod)

			#Diagnosis
			# Calculate the cos(angle) between neurons i and j
			cos_ij = np.dot(  neuron_i, neuron_j  )

			#Diagnosis
			#Calculate the cos_ij max
			if cos_ij > cos_ij_max:
				cos_ij_max = cos_ij


		#Diagnosis
		# Calculate cos(angle) betwen Fer_i and Neuron j
		cos_Fer_i_j = np.dot(  Fer_i.vector,  neuron_j )

		# Calculate the position change due to the Electrostatic Repulsion Force aceleration
		neuron_i_point[...].vector += Fer_i.vector * dltt**2


		Sphere[i].standarize()






# Prepare to graphicate
X = []
Y = []
Z = []

for point_i in np.nditer(Sphere):
	X.append(point_i.x)
	Y.append(point_i.y)
	Z.append(point_i.z)



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



#Consider speeding the iteration process with
# http://docs.scipy.org/doc/numpy/reference/arrays.nditer.html#arrays-nditer



# Nice thinking about iterating efficently
# http://codereview.stackexchange.com/questions/38580/fastest-way-to-iterate-over-numpy-array