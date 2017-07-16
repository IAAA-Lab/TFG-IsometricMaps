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
		return (self.__x ** 2 + self.__y ** 2 + self.__z ** 2) ** 0.5

	def length_squared(self):
		return self.__x ** 2 + self.__y ** 2 + self.__z ** 2

	def normalize(self):
		length = self.length()
		return VectorXYZ(self.__x / length, self.__y / length, self.__z / length)	

	def add(self, other):
		return VectorXYZ(self.__x + other.__x, self.__y + other.__y, self.__z + other.__z)

	def subtract(self, other):
		return VectorXYZ(self.__x - other.__x, self.__y - other.__y, self.__z - other.__z)

	def cross(self, other):
		return VectorXYZ(self.__y * other.__z - self.__z * other.__y, 
			self.__z * other.__x - self.__x * other.__z, self.__x * other.__y - self.__y * other.__x)			

	def dot(self, other):
		return self.__x * other.__x + self.__y * other.__y + self.__z * other.__z

	def mult(self, scalar):
		return VectorXYZ(self.__x * scalar, self.__y * scalar, self.__z * scalar)
	
	def toString(self):
		return "<" + str(self.__x) + ", " + str(self.__y) + ", " + str(self.__z) + ">"

	def rotateX(self, angleRad):
		sin = math.sin(angleRad)
		cos = math.cos(angleRad)
		return VectorXYZ(self.__x, self.__y * cos - self.__z * sin, 
			self.__y * sin + self.__z * cos)

	def rotateY(self, angleRad):
		sin = math.sin(angleRad)
		cos = math.cos(angleRad)
		return VectorXYZ(self.__z * sin + self.__x * cos, self.__y, 
			self.__z * cos - self.__x * sin)
			
	def rotateZ(self, angleRad):
		sin = math.sin(angleRad)
		cos = math.cos(angleRad)
		return VectorXYZ(self.__x * cos - self.__y * sin, self.__x * sin + self.__y * cos, 
			self.__z)

	def invert(self):
		return VectorXYZ(- self.__x, - self.__y, - self.__z)							