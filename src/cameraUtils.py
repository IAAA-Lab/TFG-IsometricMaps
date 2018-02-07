#!/usr/bin/env python3

import math
from camera import Camera
from vector_XYZ import VectorXYZ

def calculate_camera(xz1, xz2, angleDeg, direction):
	"""
	Create a Camera object with the data passed as parameters.

	Normal test
	>>> cam = calculate_camera((700000, 4140000), (702000, 4137000), '45', 'N')
	>>> cam.get_pos().toString()
	'<701000.0, 11200, 4128500.0>'
	>>> cam.get_up().toString()
	'<0.0, 1499.9999999999998, 1500.0>'
	>>> cam.get_lookAt().toString()
	'<701000.0, 1200, 4138500.0>'
	>>> cam.get_right().toString()
	'<2000, 0, 0>'
	>>> cam.get_aspectRatio()
	0.9428090415820635
	"""
	
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

	if (direction == 'S') or (direction == 'W'):
		cameraOffsetX = - cameraOffsetX
		cameraOffsetZ = - cameraOffsetZ

	initialUp = VectorXYZ(0, tan, 1)
	initialUp = initialUp.normalize().mult(zSize).mult(sin)
	upLength = initialUp.length()

	aspectRatio = xSize / upLength	

	# setCamera(posX, posY, posZ, upX, upY, upZ, lookAtX, lookAtY, lookAtZ, rightX, aspectRatio)	
	cam.setCamera(lonM - cameraOffsetX, heightCam + lookAtHeight, latM - cameraOffsetZ,
		initialUp.get_x(), initialUp.get_y(), initialUp.get_z(), lonM, lookAtHeight,
		latM, xSize, aspectRatio)

	return cam
