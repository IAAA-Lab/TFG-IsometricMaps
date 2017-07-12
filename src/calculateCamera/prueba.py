#!/usr/bin/env python3

from vector_XYZ import VectorXYZ
from camera import Camera
import cameraUtils

xSize = 14480 * 0.5
zSize = 10100 * 0.5
xMin = 718450
zMin = 4671990 - zSize
 
result = cameraUtils.camera_for_bounds(xMin, zMin, xSize, zSize, 45, 'E')
print("Location -> " + result.get_pos().toString())
print("Right -> " + result.get_right().toString())
print("Up -> " + result.get_up().toString())
print("LookAt -> " + result.get_lookAt().toString())
print("AspectRatio -> " + str(result.get_aspectRatio()))