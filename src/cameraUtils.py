#!/usr/bin/env python3

import math
from camera import Camera
from vector_XYZ import VectorXYZ

def calculate_camera(xz1, xz2, angleDeg, direction):
	cam = Camera()

	heightCam = 10000
	lookAtHeight = 1200
	xSize = xz2[0] - xz1[0]
	zSize = xz1[1] - xz2[1]
	lonM = xz1[0] + xSize * 0.5
	latM = xz2[1] + zSize * 0.5

	rads = math.radians(int(angleDeg))
	sin = math.sin(rads)
	cos = math.cos(rads)
	tan = math.tan(rads)

	cameraOffsetX = 0
	cameraOffsetZ = heightCam / tan

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

	initialUp = VectorXYZ(0, tan, 1)
	initialUp = initialUp.normalize().mult(zSize).mult(sin)
	upLength = initialUp.length()		

	# setCamera(posX, posY, posZ, upX, upY, upZ, lookAtX, lookAtY, lookAtZ, rightX, aspectRatio)	
	cam.setCamera(lonM - cameraOffsetX, heightCam + lookAtHeight, latM - cameraOffsetZ,
		initialUp.get_x(), initialUp.get_y(), initialUp.get_z(), lonM, lookAtHeight,
		latM, xSize, xSize / upLength)

	return cam
