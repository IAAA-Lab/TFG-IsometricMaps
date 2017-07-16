#!/usr/bin/env python3

from vector_XYZ import VectorXYZ

class Camera(object):

	def __init__(self):
		self.__pos = None
		self.__up = None
		self.__right = None
		self.__lookAt = None
		self.__aspectRatio = None
		self.__volumeHeight = None

	def get_pos(self):
		return self.__pos
		
	def get_up(self):
		return self.__up

	def get_right(self):
		return self.__right	
		
	def get_lookAt(self):
		return self.__lookAt

	def get_aspectRatio(self):
		return self.__aspectRatio

	def get_volumeHeight(self):
		return self.__volumeHeight

	def set_aspectRatio(self, new):
		self.__aspectRatio = new

	def set_volumeHeigth(self, new):
		self.__volumeHeight = new

	def getViewDirection(self):
		return self.__lookAt.subtract(self.__pos).normalize()

	def setCamera(self, posX, posY, posZ, upX, upY, upZ, lookAtX, lookAtY, 
		lookAtZ, rightX, aspectRatio):
		self.__pos = VectorXYZ(posX, posY, posZ)
		self.__up = VectorXYZ(upX, upY, upZ)
		self.__right = VectorXYZ(rightX, 0, 0)
		self.__lookAt = VectorXYZ(lookAtX, lookAtY, lookAtZ)
		self.__aspectRatio = aspectRatio
