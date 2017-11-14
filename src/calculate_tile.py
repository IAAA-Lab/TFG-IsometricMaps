from pyproj import Proj, transform
import math

def deg_to_num(lat_deg, lon_deg, zoom):
	lat_rad = math.radians(lat_deg)
	n = 2.0 ** float(zoom)
	xtile = int((lon_deg + 180.0) / 360.0 * n)
	ytile = int((1.0 - math.log(math.tan(lat_rad) + (1 / math.cos(lat_rad))) / math.pi) / 2.0 * n)

	return (xtile, ytile)
	
def transform_to_deg(x, y):
	WGS84 = Proj(init='EPSG:4326')
	inp = Proj(init='EPSG:25830')
	
	return transform(inp, WGS84, x, y)

def calculate_tile(x, y, zoom):
	x_trans, y_trans = transform_to_deg(x,y)
	return deg_to_num(y_trans, x_trans, zoom)
