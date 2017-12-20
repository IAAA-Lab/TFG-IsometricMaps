from pyproj import Proj, transform
import math

origin = [399809, 4881610]
end = [989876, 4291543] # 590067x590067m intermediate point -> 4586576,5

coordinates1 = ["711500", "4670000"]
coordinates2 = ["715000", "4667000"]

def calculate_tile(x, y, z):
	if x == end[0]:
		x -= 1
	if y == end[1]:
		y += 1	

	n = 2 ** z
	xtile = int(n * (x - origin[0]) / (end[0] - origin[0]))
	ytile = int(n * (origin[1] - y) / (origin[1] - end[1]))

	return (xtile, ytile)

def calculate_coordinates(xtile, ytile, z):
	n = 2 ** z
	x = origin[0] + (xtile * (end[0] - origin[0]) / n)
	y = origin[1] - (ytile * (origin[1] - end[1]) / n) 	 

	return (x, y)

"""
def deg_to_num(lat_deg, lon_deg, zoom):
	lat_rad = math.radians(lat_deg)
	n = 2.0 ** float(zoom)
	xtile = int((lon_deg + 180.0) / 360.0 * n)
	ytile = int((1.0 - math.log(math.tan(lat_rad) + (1 / math.cos(lat_rad))) / math.pi) / 2.0 * n)

	return (xtile, ytile)

def num_to_deg(xtile, ytile, zoom):
	n = 2.0 ** zoom
	lon_deg = xtile / n * 360.0 - 180.0
	lat_rad = math.atan(math.sinh(math.pi * (1 - 2 * ytile / n)))
	lat_deg = math.degrees(lat_rad)
	
	return (lon_deg, lat_deg)	
	
def transform_to_deg(x, y):
	WGS84 = Proj(init='EPSG:4326')
	inp = Proj(init='EPSG:25830')
	
	return transform(inp, WGS84, x, y)

def transform_to_utm(x, y):
	WGS84 = Proj(init='EPSG:4326')
	inp = Proj(init='EPSG:25830')

	return transform(WGS84, inp, x, y)

def calculate_tile(x, y, zoom):
	x_trans, y_trans = transform_to_deg(x,y)
	return deg_to_num(y_trans, x_trans, zoom)

def calculate_coordinate(xtile, ytile, zoom):
	x_trans, y_trans = num_to_deg(xtile, ytile, zoom)
	return transform_to_utm(x_trans, y_trans)	
"""