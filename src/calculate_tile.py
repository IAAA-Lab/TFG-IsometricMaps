import math

origin = [399809, 4881610]
end = [989876, 4291543] # 590067x590067m intermediate point -> 4586576,5

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

def tile_to_south(tile, z):
	max_tile = 2 ** z - 1

	return (max_tile - tile[0], max_tile - tile[1])

def tile_to_east(tile, z):
	max_tile = 2 ** z - 1

	return (tile[1], max_tile - tile[0])

def tile_to_west(tile, z):
	max_tile = 2 ** z - 1

	return (max_tile - tile[1], tile[0])

def tile_from_south(tile, z):
	max_tile = 2 ** z - 1

	return (max_tile - tile[0], max_tile - tile[1])

def tile_from_east(tile, z):
	max_tile = 2 ** z - 1

	return (max_tile - tile[1], tile[0])

def tile_from_west(tile, z):
	max_tile = 2 ** z - 1

	return (tile[1], max_tile - tile[0])	
