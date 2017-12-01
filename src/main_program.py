from time import time
import sys, argparse, heightfield, os, povray_writer, load_info, read_lidar, cameraUtils, calculate_tile

def render(c1, c2, dir_from, angle, result, zoom):
	t_render_i = time()

	# Find mdts and ortophotos and write heighfields info 

	mdt_list = load_info.find_mdt(c1[0], c1[1], c2[0], c2[1])
	orto_list = load_info.find_orto(c1[0], c1[1], c2[0], c2[1], mdt_list)
	areas_list = load_info.find_a_interest(c1[0], c1[1], c2[0], c2[1])
	lidar_list = load_info.find_lidar(areas_list)
	#lidar_list = ["/home/pablo/Documentos/Universidad/TFG/TFG-IsometricMaps/LIDAR/PNOA_2010_LOTE1_ARA-NORTE_712-4670_ORT-CLA-COL.LAZ"]
		
	if len(orto_list) <= 10:
		# Calculate tiles

		tile1_x, tile1_y = calculate_tile.calculate_tile(c1[0], c1[1], zoom)
		tile2_x, tile2_y = calculate_tile.calculate_tile(c2[0], c2[1], zoom)
		print([tile1_x, tile1_y])
		print([tile2_x, tile2_y])

		w_tiles = tile2_x - tile1_x + 1
		h_tiles = tile2_y - tile1_y + 1
		print(w_tiles)
		print(h_tiles)

		"""
		# Calculate NW tile coordinate

		print("NW")
		c_nw_x, c_nw_y = calculate_tile.calculate_coordinate(tile1_x, tile1_y, zoom)
		print([c_nw_x, c_nw_y])

		# Calculate SW tile coordinate

		print("SW")
		c_sw_x, c_sw_y = calculate_tile.calculate_coordinate(tile1_x, tile2_y + 1, zoom)
		print([c_sw_x, c_sw_y])

		# Calculate NE tile coordinate

		print("NE")
		c_ne_x, c_ne_y = calculate_tile.calculate_coordinate(tile2_x + 1, tile2_y, zoom)
		print([c_ne_x, c_ne_y])

		# Calculate SE tile coordinate

		print("SE")
		c_se_x, c_se_y = calculate_tile.calculate_coordinate(tile2_x + 1, tile2_y + 1, zoom)
		print([c_se_x, c_se_y])
		"""

		# Create camera, heighfields and spheres

		#cam = cameraUtils.calculate_camera((c1_x, c1_y), (c2_x, c2_y), angle, dir_from)
		cam = cameraUtils.calculate_camera(c1, c2, angle, dir_from)
		heightfields = povray_writer.write_heightfields(mdt_list, orto_list) # Generate a string which contain the heightfields to pov file.
		#spheres = read_lidar.generate_spheres(lidar_list, areas_list)
		spheres = ""

		# Generate povray file

		tile_size_x = 256
		tile_size_y = int(256 / cam.get_aspectRatio() + 0.5)

		print(cam.get_aspectRatio())
		povray_writer.write_povray_file(cam, heightfields, spheres)
		w = tile_size_x * w_tiles
		h = tile_size_y * h_tiles 
		print(str(w))
		print(str(h))

		# Rendering using new povray file

		print("Rendering " + result)
		os.system('povray +Irender.pov +O' + result + ' -D +W' + str(w) + ' +H' + str(h))
		os.system('rm render.pov')
		
		t_render_f = time()
		t_render = t_render_f - t_render_i

		print("Rendering time: " + str(int(t_render / 60)) + "min " + str(int(t_render % 60)) + "s.")

		#return ((c1_x, c1_y), (c2_x, c2_y), tile_size_x, tile_size_y, cam.get_aspectRatio())
		return (tile_size_x, tile_size_y, cam.get_aspectRatio())
	else:
		print("Error: The zone to render must be smaller (orto_list > 10). Try with other coordinates.")

def tessellation(result, c1, c2, render_result, zoom):
	app_directory = "/home/pablo/Documentos/Universidad/TFG/strummerTFIU.github.io/"
	print("Creating tiles...")

	tile_size_x = str(render_result[0])
	tile_size_y = str(render_result[1])
	aspect_ratio = render_result[2]

	# Principal zoom

	tile1_x, tile1_y = calculate_tile.calculate_tile(c1[0], c1[1], zoom)

	os.system("mkdir " + app_directory + str(zoom))
	os.system("convert " + result + " -crop " + tile_size_x + "x" + tile_size_y + " -set filename:tile \"%[fx:page.x/" 
		+ tile_size_x + "+" + str(tile1_x) + "]_%[fx:page.y/" + tile_size_y + "+" + str(tile1_y) + "]\" +adjoin \"" 
		+ app_directory + str(zoom) + "/map_%[filename:tile].png\"")
	
	# -1 Zoom lvl
		
	tile1_x, tile1_y = calculate_tile.calculate_tile(c1[0], c1[1], zoom - 1)
	tile2_x, tile2_y = calculate_tile.calculate_tile(c2[0], c2[1], zoom - 1)

	w_tiles = tile2_x - tile1_x + 1
	h_tiles = tile2_y - tile1_y + 1
	print(w_tiles)
	print(h_tiles)

	w = int(tile_size_x) * w_tiles
	h = int(tile_size_y) * h_tiles
	print(w)
	print(h) 

	os.system("mkdir " + app_directory + str(zoom - 1))
	os.system("convert " + result + " -resize " + str(w) + "x" + str(h) + " " + result)
	os.system("convert " + result + " -crop " + tile_size_x + "x" + tile_size_y + " -set filename:tile \"%[fx:page.x/" 
		+ tile_size_x + "+" + str(tile1_x) + "]_%[fx:page.y/" + tile_size_y + "+" + str(tile1_y) + "]\" +adjoin \"" 
		+ app_directory + str(zoom - 1) + "/map_%[filename:tile].png\"")

	os.system("rm " + result)									
	
def main():
	# Arguments

	parser = argparse.ArgumentParser(description="First version of Pablo's TFG.")

	parser.add_argument("mdt_directory", help="Directory of the MDT files to transform.")
	parser.add_argument("png_directory", help="PNG files transformed destination directory.")
	parser.add_argument("orto_directory", help="Ortophotos files directory.")
	parser.add_argument("lidar_directory", help="Directory of LAZ files.")
	parser.add_argument("dir_from", help="From direction of the view (only N, S, E or W).")
	parser.add_argument("angle", help="Angle of the view (only 45 or 30).")
	parser.add_argument("zoom", help="Zoom.")

	parser.add_argument("--max_height", dest="max_height", type=int, default=2200, metavar="MAX_HEIGHT",
		help="Max height transforming MDT files. Higher heights will be considered MAX_HEIGHT " + 
			"(default value = 2200)")

	parser.add_argument("--all", help="Render all available zones.", action="store_true")

	args = parser.parse_args()

	if (args.angle == "30") or (args.angle == "45"):
		if (args.dir_from == 'S') or (args.dir_from == 'N') or (args.dir_from == 'W') or (args.dir_from == 'E'):

			if args.mdt_directory[-1] != "/":
				args.mdt_directory += "/"
			if args.png_directory[-1] != "/":
				args.png_directory += "/"
			if args.orto_directory[-1] != "/":
				args.orto_directory += "/"
			if args.lidar_directory[-1] != "/":
				args.lidar_directory += "/"		

			# Transform to heightfield	

			#for base, dirs, files in os.walk(args.mdt_directory):
			#	for asc_file in files:
			#		heightfield.transform_file_to_heightfield(args.mdt_directory + asc_file, args.png_directory 
			#			+ asc_file[:-4] + ".png", args.max_height)

			# Load info data to file

			#load_info.load_info(args.png_directory, args.orto_directory, args.lidar_directory)

			#offset = 1000
			offset = 0
			minX = 704000 + offset # Incluído de momento a mano (coordenada central mdt - nºcolumnas/2 * tamaño celda)
			maxX = 704400 + 5760 * 5 - offset # Se comprueba en la lista que valores serían los mayores y cuales los menores
			minY = 4652400 + offset # Se suma el offset para que luego los datos concuerden al aplicarle el offset
			maxY = 4671000 + 4000 * 5 - offset

			if args.all:
				os.system('mkdir result_dir')
				dist_x = 8000
				dist_y = 6000 
				
				x1 = minX
				x_number = 0

				while(x1 + dist_x < maxX): # Recorre las X de menor a mayor
					x_number += 1
					
					y1 = maxY
					y_number = 0
					
					while(y1 - dist_y > minY): # Recorre las Y de mayor a menor
						y_number += 1
						render([x1, y1], [x1 + dist_x, y1 - dist_y], args.dir_from, args.angle, 
							"./result_dir/result_" + str(x_number) + "_" + str(y_number) + ".png")
						y1 -= dist_y

					y_number += 1	
					render([x1, y1], [x1 + dist_x, minY], args.dir_from, args.angle, 
						"./result_dir/result_" + str(x_number) + "_" + str(y_number) + ".png") # La última con la segunda coordenada la menor Y
					x1 += dist_x	

				# Recorre para los últimos valores para las X
					
				x_number += 1

				y1 = maxY
				y_number = 0

				while(y1 - dist_y > minY):
					y_number += 1
					render([x1, y1], [maxX, y1 - dist_y], args.dir_from, args.angle, 
						"./result_dir/result_" + str(x_number) + "_" + str(y_number) + ".png")
					y1 -= dist_y

				y_number += 1	
				render([x1, y1], [maxX, minY], args.dir_from, args.angle, 
					"./result_dir/result_" + str(x_number) + "_" + str(y_number) + ".png")
			else:
				# Ask for coordinates

				coordinates = input("Introduce UTM X and Y coordinates, separated by a blank space and respecting the values min " 
					+ "and max for the coordinates, for upper left vertex (" + str(minX) + " <= X1 <= " + str(maxX) + " " + str(minY) 
					+ " <= Y1 <= " + str(maxY) + "): ")
				coordinates1 = coordinates.split()
				coordinates1 = ["711500", "4670000"]
				#coordinates1 = ["711500", "4667000"]

				if (len(coordinates1) == 2 and float(coordinates1[0]) >= minX and float(coordinates1[0]) <= maxX and 
						float(coordinates1[1]) >= minY and float(coordinates1[1]) <= maxY):
					
					coordinates = input("Introduce UTM X and Y coordinates, separated by a blank space and respecting the values min " 
						+ "and max for the coordinates, for bottom right vertex (" + coordinates1[0] + " <= X2 <= " + str(maxX) + " " + str(minY) 
						+ " <= Y2 <= " + coordinates1[1] + "): ")
					coordinates2 = coordinates.split()
					coordinates2 = ["715000", "4667000"]
					#coordinates2 = ["715000", "4664000"]

					if (len(coordinates2) == 2 and float(coordinates2[0]) >= minX and float(coordinates2[0]) <= maxX and 
							float(coordinates2[1]) >= minY and float(coordinates2[1]) <= maxY and coordinates1[0] < coordinates2[0]
							and coordinates1[1] > coordinates2[1]):
						
						# Offset to adjust later during join process

						coordinates1[0] = float(coordinates1[0]) - offset
						coordinates2[0] = float(coordinates2[0]) + offset
						coordinates1[1] = float(coordinates1[1]) + offset
						coordinates2[1] = float(coordinates2[1]) - offset

						result = "./result.png"

						render_result = render(coordinates1, coordinates2, args.dir_from, args.angle, result, int(args.zoom))
						tessellation(result, coordinates1, coordinates2, render_result, int(args.zoom))

						print("DONE!")	
					else:
						print("Error: Introduce UTM coordinates correctly.")
				else:
					print("Error: Introduce UTM coordinates correctly.")				
		else:	
			print("ERROR: dir_from must be N, S, W or E.")
	else:
		print("ERROR: angle must be 45 or 30.")	

if __name__ == "__main__":
    main()