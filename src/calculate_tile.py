import math

origin = [399809, 4881610]
end = [989876, 4291543] # 590067x590067m intermediate point -> 4586576,5

def calculate_tile(x, y, z):
	"""
	Calculate tile number from the coordinates passed as parameter.

	Normal test
	>>> calculate_tile(650000, 4400000, 9)
	(217, 417)

	Limit test
	>>> calculate_tile(989876, 4291543, 9)
	(511, 511)

	Over limit test
	>>> calculate_tile(990000, 4400000, 9)
	('null', 'null')
	"""

	if x < origin[0] or x > end[0] or y < end[1] or y > origin[1]:
		return ('null', 'null')

	if x == end[0]:
		x -= 1
	if y == end[1]:
		y += 1	

	n = 2 ** z
	xtile = int(n * (x - origin[0]) / (end[0] - origin[0]))
	ytile = int(n * (origin[1] - y) / (origin[1] - end[1]))

	return (xtile, ytile)

def calculate_coordinates(xtile, ytile, z):
	"""
	Calculate the coordinates of the upper left corner of the tile passed as parameter.

	Normal test
	>>> calculate_coordinates(1314, 1413, 11)
	(778396.9091796875, 4474498.344238281)

	Over limit test
	>>> calculate_coordinates(1314, 1413, 8)
	'null'
	"""

	n = 2 ** z

	if xtile >= n or ytile >= n or xtile < 0 or ytile < 0:
		return ('null') 

	x = origin[0] + (xtile * (end[0] - origin[0]) / n)
	y = origin[1] - (ytile * (origin[1] - end[1]) / n) 	 

	return (x, y)

def tile_to_south(tile, z):
	"""
	Transform tile number to number for south point of view.

	Normal test
	>>> tile_to_south((325, 785), 10)
	(698, 238)

	Over limit test
	>>> tile_to_south((600, 300), 9)
	'null'
	"""

	max_tile = 2 ** z - 1

	if tile[0] > max_tile or tile[1] > max_tile or tile[0] < 0 or tile[1] < 0:
		return ('null') 

	return (max_tile - tile[0], max_tile - tile[1])

def tile_to_east(tile, z):
	"""
	Transform tile number to number for east point of view.

	Normal test
	>>> tile_to_east((325, 785), 10)
	(785, 698)

	Over limit test
	>>> tile_to_east((600, 300), 9)
	'null'
	"""

	max_tile = 2 ** z - 1

	if tile[0] > max_tile or tile[1] > max_tile or tile[0] < 0 or tile[1] < 0:
		return ('null')

	return (tile[1], max_tile - tile[0])

def tile_to_west(tile, z):
	"""
	Transform tile number to number for west point of view.

	Normal test
	>>> tile_to_west((325, 785), 10)
	(238, 325)

	Over limit test
	>>> tile_to_west((600, 300), 9)
	'null'
	"""

	max_tile = 2 ** z - 1

	if tile[0] > max_tile or tile[1] > max_tile or tile[0] < 0 or tile[1] < 0:
		return ('null')

	return (max_tile - tile[1], tile[0])

def tile_from_south(tile, z):
	"""
	Transform tile number to to number for north point of view from south.

	Normal test
	>>> tile_from_south((133, 42),8)
	(122, 213)

	Over limit test
	>>> tile_from_south((600, 300), 9)
	'null'
	"""

	max_tile = 2 ** z - 1

	if tile[0] > max_tile or tile[1] > max_tile or tile[0] < 0 or tile[1] < 0:
		return ('null')

	return (max_tile - tile[0], max_tile - tile[1])

def tile_from_east(tile, z):
	"""
	Transform tile number to to number for north point of view from east.

	Normal test
	>>> tile_from_east((133, 42),8)
	(213, 133)

	Over limit test
	>>> tile_from_east((600, 300), 9)
	'null'
	"""

	max_tile = 2 ** z - 1

	if tile[0] > max_tile or tile[1] > max_tile or tile[0] < 0 or tile[1] < 0:
		return ('null')

	return (max_tile - tile[1], tile[0])

def tile_from_west(tile, z):
	"""
	Transform tile number to to number for north point of view from west.

	Normal test
	>>> tile_from_west((133, 42),8)
	(42, 122)

	Over limit test
	>>> tile_from_west((600, 300), 9)
	'null'
	"""

	max_tile = 2 ** z - 1

	if tile[0] > max_tile or tile[1] > max_tile or tile[0] < 0 or tile[1] < 0:
		return ('null')

	return (tile[1], max_tile - tile[0])	
