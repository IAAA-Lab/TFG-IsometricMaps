#!/usr/bin/env python3

from vector_XYZ import VectorXYZ
from camera import Camera
import cameraUtils

xSize = 14480 * 0.5
zSize = 10100 * 0.5
xMin = 718450.25
zMin = 4671989.75 - zSize
 
result = cameraUtils.camera_for_bounds(xMin, zMin, xSize, zSize, 45, 'S')
width = result.get_volumeHeight() * result.get_aspectRatio()
print("Location -> " + result.get_pos().toString())
print("Right -> " + result.getRight().mult(width).invert().toString())
print("Up -> " + result.get_up().mult(result.get_volumeHeight()).toString())
print("LookAt -> " + result.get_lookAt().toString())