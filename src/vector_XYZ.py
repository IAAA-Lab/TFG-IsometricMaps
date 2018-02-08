#!/usr/bin/env python3

import math

class VectorXYZ(object):
	
	def __init__(self, x2, y2, z2):
		self.__x = x2
		self.__y = y2
		self.__z = z2

	def get_x(self):
		return self.__x

	def get_y(self):
		return self.__y
		
	def get_z(self):
		return self.__z			

	def length(self):
		"""
		Return the length of the vector.

		>>> vector = VectorXYZ(1, 2, 3)
		>>> vector.length()
		3.7416573867739413
		"""

		return (self.__x ** 2 + self.__y ** 2 + self.__z ** 2) ** 0.5

	def length_squared(self):
		"""
		Return the length squared of the vector.

		>>> vector = VectorXYZ(1, 2, 3)
		>>> vector.length_squared()
		14
		"""

		return self.__x ** 2 + self.__y ** 2 + self.__z ** 2

	def normalize(self):
		"""
		Return the vector normalized.

		>>> vector = VectorXYZ(1, 2, 3)
		>>> vector.normalize().toString()
		'<0.2672612419124244, 0.5345224838248488, 0.8017837257372732>'
		"""

		length = self.length()
		return VectorXYZ(self.__x / length, self.__y / length, self.__z / length)	

	def add(self, other):
		"""
		Return the sum of two vectors.

		>>> vector1 = VectorXYZ(1, 2, 3)
		>>> vector2 = VectorXYZ(3, 2, 1)
		>>> vector1.add(vector2).toString()
		'<4, 4, 4>'
		"""

		return VectorXYZ(self.__x + other.__x, self.__y + other.__y, self.__z + other.__z)

	def subtract(self, other):
		"""
		Return the substraction of two vectors.

		>>> vector1 = VectorXYZ(1, 2, 3)
		>>> vector2 = VectorXYZ(3, 2, 1)
		>>> vector1.subtract(vector2).toString()
		'<-2, 0, 2>'
		"""

		return VectorXYZ(self.__x - other.__x, self.__y - other.__y, self.__z - other.__z)

	def cross(self, other):
		"""
		Return the vectorial product of two vectors.

		>>> vector1 = VectorXYZ(1, 2, 3)
		>>> vector2 = VectorXYZ(3, 2, 1)
		>>> vector1.cross(vector2).toString()
		'<-4, 8, -4>'
		"""

		return VectorXYZ(self.__y * other.__z - self.__z * other.__y, 
			self.__z * other.__x - self.__x * other.__z, self.__x * other.__y - self.__y * other.__x)			

	def mult(self, scalar):
		"""
		Return the multiplication of the vector and a number.

		>>> vector = VectorXYZ(1, 2, 3)
		>>> vector.mult(2).toString()
		'<2, 4, 6>'
		"""

		return VectorXYZ(self.__x * scalar, self.__y * scalar, self.__z * scalar)
	
	def invert(self):
		"""
		Return the vector inverted.

		>>> vector = VectorXYZ(1, 2, 3)
		>>> vector.invert().toString()
		'<-1, -2, -3>'
		"""

		return VectorXYZ(- self.__x, - self.__y, - self.__z)
			
	def toString(self):
		return "<" + str(self.__x) + ", " + str(self.__y) + ", " + str(self.__z) + ">"
							