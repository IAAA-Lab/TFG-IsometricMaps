#!/usr/bin/env python3

import math
from camera import Camera
from vector_XYZ import VectorXYZ

def camera_for_bounds(xMin, zMin, xSize, zSize, angleDeg, direction):
	cam = Camera()

	lookAt = VectorXYZ(xMin + xSize * 0.5, 0, zMin + zSize * 0.5)

	maxSize = max(xSize, zSize)
	if (maxSize == xSize):
		cameraDistance = xMin + xSize
	else:
		cameraDistance = zMin + zSize	

	rads = math.radians(angleDeg)
	sin = math.sin(rads)

	cameraOffsetX = 0
	cameraOffsetZ = - maxSize * math.cos(rads)

	if (direction == 'W') or (direction == 'E'):
		aux = cameraOffsetX
		cameraOffsetX = cameraOffsetZ
		cameraOffsetZ = aux

		aux = xSize
		xSize = zSize
		zSize = aux

	if (direction == 'N') or (direction == 'E'):
		cameraOffsetX = - cameraOffsetX
		cameraOffsetZ = - cameraOffsetZ	

	#setCamera(posX, posY, posZ, upX, upY, upZ, lookAtX, lookAtY, lookAtZ, aspectRatio, volumeHeight)	
	cam.setCamera(lookAt.get_x() + cameraOffsetX, cameraDistance * sin,
		lookAt.get_z() + cameraOffsetZ, 0, 1, math.tan(rads), lookAt.get_x(),
		lookAt.get_y(), lookAt.get_z(),	xSize / (zSize * sin), zSize * sin)

	return cam	