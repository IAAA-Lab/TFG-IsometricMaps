from time import time
import sys, argparse, heightfield, os, povray_writer, load_info, read_lidar, cameraUtils, calculate_tile

#/media/pablo/280F8D1D0A5B8545/TFG_files/strummerTFIU.github.io/

def tiles_to_render(c1, c2, zoom):
	# Calculate tiles

	tile1_x, tile1_y = calculate_tile.calculate_tile(c1[0], c1[1], zoom)
	tile2_x, tile2_y = calculate_tile.calculate_tile(c2[0], c2[1], zoom)

	w_tiles = tile2_x - tile1_x + 1
	h_tiles = tile2_y - tile1_y + 1

	if w_tiles != h_tiles:
		tile_max = max(w_tiles, h_tiles)
		w_tiles = tile_max
		h_tiles = tile_max

		tile2_x = tile1_x + w_tiles - 1
		tile2_y = tile1_y + h_tiles - 1

	# Calculate new coordinates

	c_nw = calculate_tile.calculate_coordinates(tile1_x, tile1_y, zoom)
	c_se = calculate_tile.calculate_coordinates(tile2_x + 1, tile2_y + 1, zoom)
	
	return ((tile1_x, tile1_y), (tile2_x, tile2_y), c_nw, c_se)

def dir_view_tile(tile, dir_view, zoom):
	if dir_view == 'S':
		return calculate_tile.tile_to_south(tile, zoom)
	elif dir_view == 'E':
		return calculate_tile.tile_to_east(tile, zoom)
	elif dir_view == 'W':
		return calculate_tile.tile_to_west(tile, zoom)		
	else:
		return tile	

def render(tile1, tile2, c1, c2, dir_view, angle, result, lidar):
	# Apply a offset

	off_c1_0 = 0
	off_c1_1 = 0
	off_c2_0 = 0
	off_c2_1 = 0
	if dir_view == 'N':
		off_c1_1 = 500
		off_c2_1 = -2500
	elif dir_view == 'S':
		off_c1_1 = 2500
		off_c2_1 = -500
	elif dir_view == 'E':
		off_c1_0 = -2500
		off_c2_0 = 500
	else:
		off_c1_0 = -500
		off_c2_0 = 2500			

	# Find mdts and ortophotos and write heighfields info 

	mdt_list = load_info.find_mdt(c1[0] + off_c1_0, c1[1] + off_c1_1, c2[0] + off_c2_0, c2[1] + off_c2_1)
	if len(mdt_list) == 0:
		return ("null", "null")

	orto_list = load_info.find_orto(c1[0] + off_c1_0, c1[1] + off_c1_1, c2[0] + off_c2_0, c2[1] + off_c2_1, mdt_list)
	areas_list = load_info.find_a_interest(c1[0] + off_c1_0, c1[1] + off_c1_1, c2[0] + off_c2_0, c2[1] + off_c2_1)
	lidar_list = load_info.find_lidar(areas_list)
		
	if len(orto_list) <= 10:
		if lidar == True:
			spheres = read_lidar.generate_spheres(lidar_list, areas_list)
		else:
			spheres = ""	

		# Create camera, heighfields and spheres

		cam = cameraUtils.calculate_camera(c1, c2, angle, dir_view)
		heightfields = povray_writer.write_heightfields(mdt_list, orto_list) # Generate a string which contain the heightfields to pov file.

		# Generate povray file

		tile_size_x = 256
		tile_size_y = int(256 / cam.get_aspectRatio() + 0.5)

		povray_writer.write_povray_file(cam, heightfields, spheres)

		w_tiles = tile2[0] - tile1[0] + 1
		h_tiles = tile2[1] - tile1[1] + 1

		w = tile_size_x * w_tiles
		h = tile_size_y * h_tiles

		# Rendering using new povray file

		print("Rendering " + result)
		os.system('povray +Irender.pov +O' + result + ' -D +A -GA +W' + str(w) + ' +H' + str(h) + '> /dev/null 2>&1')

		return (tile_size_x, tile_size_y)
	else:
		print("Error: The zone to render must be smaller (orto_list > 10). Try with other coordinates.")

def tessellation(result, tile1, tile_size_x, tile_size_y, zoom, dir_view, angle, dist_tile):
	if dist_tile[-1] != "/":
		dist_tile += "/"
	
	print("Creating tiles from [" + str(tile1[0]) + ", " + str(tile1[1]) + "]...")

	os.system("mkdir " + dist_tile + angle + '> /dev/null 2>&1')
	os.system("mkdir " + dist_tile + angle + "/" + dir_view + '> /dev/null 2>&1')
	os.system("mkdir " + dist_tile + angle + "/" + dir_view + "/" + str(zoom) + '> /dev/null 2>&1')
	os.system("convert " + result + " -crop " + str(tile_size_x) + "x" + str(tile_size_y) + " -set filename:tile \"%[fx:page.x/" 
		+ str(tile_size_x) + "+" + str(tile1[0]) + "]_%[fx:page.y/" + str(tile_size_y) + "+" + str(tile1[1]) + "]\" +adjoin \"" 
		+ dist_tile + angle + "/" + dir_view + "/" + str(zoom) + "/map_%[filename:tile].png\"")

	if zoom == "9":
		# -1 zoom lvl

		aux1_x = int(tile1[0] / 2)
		aux1_y = int(tile1[1] / 2)

		os.system("mkdir " + dist_tile + angle + "/" + dir_view + "/" + str(int(zoom) - 1) + '> /dev/null 2>&1')
		os.system("convert " + result + " -resize " + str(tile_size_x) + "x" + str(tile_size_y) + " " + dist_tile + angle + "/" 
			+ dir_view + "/" + str(int(zoom) - 1) + "/map_" + str(aux1_x) + "_" + str(aux1_y) + ".png")

	#os.system("rm " + result)									
	
def main():
	# Arguments

	parser = argparse.ArgumentParser(description="First version of Pablo's TFG.")

	parser.add_argument("mdt_directory", help="Directory of the MDT files to transform.")
	parser.add_argument("png_directory", help="PNG files transformed destination directory.")
	parser.add_argument("orto_directory", help="Ortophotos files directory.")
	parser.add_argument("lidar_directory", help="Directory of LAZ files.")
	parser.add_argument("dir_view", help="Direction of the view (only N, S, E or W).")
	parser.add_argument("angle", help="Angle of the view (only 45 or 30).")
	parser.add_argument("zoom", help="Zoom.")

	parser.add_argument("--max_height", dest="max_height", type=int, default=2200, metavar="MAX_HEIGHT",
		help="Max height transforming MDT files. Higher heights will be considered MAX_HEIGHT " + 
			"(default value = 2200)")

	parser.add_argument("--renderAll", help="Render all available zones.", action="store_true")
	parser.add_argument("--renderTiles", help="Render especified tiles.", action="store_true")
	parser.add_argument("--transform", help="Transform all mdt in mdt_directory from .asc to .png.", action="store_true")
	parser.add_argument("--load", help="Load info from mdts, pnoas and lidar files.", action="store_true")
	parser.add_argument("--tile", help="Tessellation result/s.", action="store_true")
	parser.add_argument("--deletePov", help="Delete povray file.", action="store_true")

	args = parser.parse_args()

	if (args.angle == "30") or (args.angle == "45"):
		if (args.dir_view == 'S') or (args.dir_view == 'N') or (args.dir_view == 'W') or (args.dir_view == 'E'):
			if int(args.zoom) < 10:
				lidar = False
			else:
				lidar = True

			t_exe_i = time()

			if args.mdt_directory[-1] != "/":
				args.mdt_directory += "/"
			if args.png_directory[-1] != "/":
				args.png_directory += "/"
			if args.orto_directory[-1] != "/":
				args.orto_directory += "/"
			if args.lidar_directory[-1] != "/":
				args.lidar_directory += "/"		

			# Transform to heightfield	

			if args.transform:
				os.system('mkdir ' + args.png_directory)
				for base, dirs, files in os.walk(args.mdt_directory):
					for asc_file in files:
						heightfield.transform_file_to_heightfield(args.mdt_directory + asc_file, args.png_directory 
							+ asc_file[:-4] + ".png", args.max_height)

			# Load info data to file

			if args.load:
				load_info.load_info(args.png_directory, args.orto_directory, args.lidar_directory)

			if args.tile:
				dist_tile = input("Introduce tiles destination directory: ")
			else:
				os.system("mkdir result_dir")
				dist_tile = "./result_dir/"		

			minX = 560000
			maxX = 789000
			minY = 4410000
			maxY = 4745000

			if args.renderTiles:
				tile_init = input("Introduce tile number (x y) for upper left vertex: ").split()
				tile_init = (int(tile_init[0]), int(tile_init[1]))
				if tile_init[0] >= 0 and tile_init[0] <= (2 ** int(args.zoom) - 1) and tile_init[1] >= 0 or tile_init[1] <= (2 ** int(args.zoom) - 1):
					tile_end = input("Introduce tile number (x,y) for bottom right vertex: ").split()
					tile_end = (int(tile_end[0]), int(tile_end[1]))
					if tile_end[0] >= 0 and tile_end[0] <= (2 ** int(args.zoom) - 1) and tile_end[1] >= 0 or tile_end[1] <= (2 ** int(args.zoom) - 1
						and tile_end[0] >= tile_init[0] and tile_end[1] >= tile_init[1]):
	
						result = "./result.png"

						if args.dir_view == 'S':
							tile_1 = calculate_tile.tile_from_south(tile_end, int(args.zoom))
							tile_2 = calculate_tile.tile_from_south(tile_init, int(args.zoom))
						elif args.dir_view == 'E':
							tile_1_aux = calculate_tile.tile_from_east(tile_init, int(args.zoom))
							tile_2_aux = calculate_tile.tile_from_east(tile_end, int(args.zoom))

							tile_1 = (tile_2_aux[0], tile_1_aux[1])
							tile_2 = (tile_1_aux[0], tile_2_aux[1])
						elif args.dir_view == 'W':
							tile_1_aux = calculate_tile.tile_from_west(tile_init, int(args.zoom))
							tile_2_aux = calculate_tile.tile_from_west(tile_end, int(args.zoom))

							tile_1 = (tile_1_aux[0], tile_2_aux[1])
							tile_2 = (tile_2_aux[0], tile_1_aux[1])
						else:
							tile_1 = tile_init
							tile_2 = tile_end
						
						c_nw = calculate_tile.calculate_coordinates(tile_1[0], tile_1[1], int(args.zoom))
						c_se = calculate_tile.calculate_coordinates(tile_2[0] + 1, tile_2[1] + 1, int(args.zoom))

						print("Rendering from tile [" + str(tile_1[0]) + ", " + str(tile_1[1]) + "] to [" + str(tile_2[0]) 
							+ "," + str(tile_2[1]) + "] with coordinates from [" + str(c_nw[0]) + ", " + str(c_nw[1]) 
							+ "] to [" + str(c_se[0]) + ", " + str(c_se[1]) + "].")

						tile_size_x, tile_size_y = render(tile_1, tile_2, c_nw, c_se, args.dir_view, args.angle, result, lidar)
						
						if tile_size_x == "null" and tile_size_y == "null":
							print("ERROR: Nothing to render. Continuing...")
						else:		
							tessellation(result, tile_init, tile_size_x, tile_size_y, args.zoom, args.dir_view, args.angle, dist_tile)	
					else:
						print("ERROR: Introduce tiles correctly.")
				else:
					print("ERROR: Introduce tiles correctly.")
			else:			
				if args.renderAll:
					if int(args.zoom) > 7 and int(args.zoom) < 13:
						iTile_z5_x = 9
						iTile_z5_y = 8
						fTile_z5_x = 26
						fTile_z5_y = 25

						tile1_x = iTile_z5_x * (2 ** (int(args.zoom) - 5))
						tile1_y = iTile_z5_y * (2 ** (int(args.zoom) - 5))
						tile2_x = fTile_z5_x * (2 ** (int(args.zoom) - 5))
						tile2_y = fTile_z5_y * (2 ** (int(args.zoom) - 5))
						#tile1_x = 286
						#tile2_x = 287
						#tile1_y = 130
						#tile2_y = 131 

						result = "./result.png"

						if int(args.zoom) == 9:
							n_tiles = 2
						else:
							n_tiles = 1	

						x_number = 0

						while(tile1_x + x_number <= tile2_x):
							aux1_x = tile1_x + x_number
							y_number = 0

							while(tile1_y + y_number <= tile2_y):
								aux1_y = tile1_y + y_number

								c_nw = calculate_tile.calculate_coordinates(aux1_x, aux1_y, int(args.zoom))
								c_se = calculate_tile.calculate_coordinates(aux1_x + n_tiles, aux1_y + n_tiles, int(args.zoom))

								print("Rendering from tile [" + str(aux1_x) + ", " + str(aux1_y) + "] to [" + str(aux1_x + n_tiles - 1) 
									+ "," + str(aux1_y + n_tiles -1) + "] with coordinates from [" + str(c_nw[0]) + ", " + str(c_nw[1]) 
									+ "] to [" + str(c_se[0]) + ", " + str(c_se[1]) + "].")

								tile_size_x, tile_size_y = render((aux1_x, aux1_y), (aux1_x + n_tiles - 1, aux1_y + n_tiles - 1), c_nw, c_se, args.dir_view, args.angle, result, lidar)
								
								if tile_size_x == "null" and tile_size_y == "null":
									print("ERROR: Nothing to render. Continuing...")
								else:
									#print("NOPE")
									if args.dir_view == 'S':
										tile_init = calculate_tile.tile_to_south((aux1_x + n_tiles - 1, aux1_y + n_tiles - 1), int(args.zoom))
									elif args.dir_view == 'E':
										tile1_aux = calculate_tile.tile_to_east((aux1_x, aux1_y), int(args.zoom))
										tile2_aux = calculate_tile.tile_to_east((aux1_x + n_tiles - 1, aux1_y + n_tiles - 1), int(args.zoom))

										tile_init = (tile1_aux[0], tile2_aux[1])
									elif args.dir_view == 'W':
										tile1_aux = calculate_tile.tile_to_west((aux1_x, aux1_y), int(args.zoom))
										tile2_aux = calculate_tile.tile_to_west((aux1_x + n_tiles - 1, aux1_y + n_tiles - 1), int(args.zoom))		
										
										tile_init = (tile2_aux[0], tile1_aux[1])
									else:
										tile_init = (aux1_x, aux1_y)

									tessellation(result, tile_init, tile_size_x, tile_size_y, args.zoom, args.dir_view, args.angle, dist_tile)

								y_number += n_tiles

							x_number += n_tiles
					else:
						print("ERROR: zoom for --renderAll option must be 7 < z < 13.")			
				else:
					# Ask for coordinates

					coordinates = input("Introduce UTM X and Y coordinates, separated by a blank space and respecting the values min " 
						+ "and max for the coordinates, for upper left vertex (" + str(minX) + " <= X1 <= " + str(maxX) + " " + str(minY) 
						+ " <= Y1 <= " + str(maxY) + "): ")
					coordinates1 = coordinates.split()
					#coordinates1 = ["519098", "4769065"]
					coordinates1 = ["711500", "4670000"]
					#coordinates1 = ["711500", "4667000"]
					#coordinates1 = ["715000", "4670000"]
					#coordinates1 = ["715000", "4667000"]

					if (len(coordinates1) == 2 and float(coordinates1[0]) >= minX and float(coordinates1[0]) <= maxX and 
							float(coordinates1[1]) >= minY and float(coordinates1[1]) <= maxY):
						
						coordinates = input("Introduce UTM X and Y coordinates, separated by a blank space and respecting the values min " 
							+ "and max for the coordinates, for bottom right vertex (" + coordinates1[0] + " <= X2 <= " + str(maxX) + " " + str(minY) 
							+ " <= Y2 <= " + coordinates1[1] + "): ")
						coordinates2 = coordinates.split()
						#coordinates2 = ["870586", "4417577"]
						coordinates2 = ["715000", "4667000"]
						#coordinates2 = ["715000", "4664000"]
						#coordinates2 = ["718500", "4667000"]
						#coordinates2 = ["718500", "4664000"]

						if (len(coordinates2) == 2 and float(coordinates2[0]) >= minX and float(coordinates2[0]) <= maxX and 
								float(coordinates2[1]) >= minY and float(coordinates2[1]) <= maxY and coordinates1[0] < coordinates2[0]
								and coordinates1[1] > coordinates2[1]):
							
							# Offset to adjust later during join process

							coordinates1[0] = float(coordinates1[0])
							coordinates2[0] = float(coordinates2[0])
							coordinates1[1] = float(coordinates1[1])
							coordinates2[1] = float(coordinates2[1])

							result = "./result.png"

							tile1, tile2, c_nw, c_se = tiles_to_render(coordinates1, coordinates2, int(args.zoom))

							if args.dir_view == 'S':
								tile_init = calculate_tile.tile_to_south(tile2, int(args.zoom))
							elif args.dir_view == 'E':
								tile1_aux = calculate_tile.tile_to_east(tile1, int(args.zoom))
								tile2_aux = calculate_tile.tile_to_east(tile2, int(args.zoom))

								tile_init = (tile1_aux[0], tile2_aux[1])
							elif args.dir_view == 'W':
								tile1_aux = calculate_tile.tile_to_west(tile1, int(args.zoom))
								tile2_aux = calculate_tile.tile_to_west(tile2, int(args.zoom))		
								
								tile_init = (tile2_aux[0], tile1_aux[1])
							else:
								tile_init = tile1

							tile_size_x, tile_size_y = render(tile1, tile2, c_nw, c_se, args.dir_view, args.angle, result, lidar)
							tessellation(result, tile_init, tile_size_x, tile_size_y, args.zoom, args.dir_view, args.angle, dist_tile)

							print("DONE!")	
						else:
							print("Error: Introduce UTM coordinates correctly.")
					else:
						print("Error: Introduce UTM coordinates correctly.")
			
			if args.deletePov:
				os.system('rm render.pov')

			t_exe_f = time()
			t_exe = t_exe_f - t_exe_i

			print("Execution time: " + str(int(t_exe / 60)) + "min " + str(int(t_exe % 60)) + "s.")						
		else:	
			print("ERROR: dir_view must be N, S, W or E.")
	else:
		print("ERROR: angle must be 45 or 30.")	

if __name__ == "__main__":
    main()