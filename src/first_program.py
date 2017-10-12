import sys, argparse, heightfield, os, povray_writer, load_info, povray_divider

def main():
	# Arguments

	parser = argparse.ArgumentParser(description="First version of Pablo's TFG.")

	parser.add_argument("mdt_directory", help="Directory of the MDT files to transform.")
	parser.add_argument("png_directory", help="PNG files transformed destination directory.")
	parser.add_argument("orto_directory", help="Ortophotos files directory.")
	parser.add_argument("dir_from", help="From direction of the view (only N, S, E or W).")
	parser.add_argument("angle", help="Angle of the view (only 45 or 30).")
	#parser.add_argument("result_name", help="Name of the image (jpg) result.")

	parser.add_argument("--max_height", dest="max_height", type=int, default=2200, metavar="MAX_HEIGHT",
		help="Max height transforming MDT files. Higher heights will be considered MAX_HEIGHT " + 
			"(default value = 2200)")

	parser.add_argument("--divide", help="Divide PNG files in 16 image portions.", action="store_true")

	args = parser.parse_args()

	if (args.angle == "30") or (args.angle == "45"):
		if (args.dir_from == 'S') or (args.dir_from == 'N') or (args.dir_from == 'W') or (args.dir_from == 'E'):

			# Transform to heightfield

			if args.mdt_directory[-1] != "/":
				args.mdt_directory += "/"
			if args.png_directory[-1] != "/":
				args.png_directory += "/"
			if args.orto_directory[-1] != "/":
				args.orto_directory += "/"	

			#for base, dirs, files in os.walk(args.mdt_directory):
			#	for asc_file in files:
			#		heightfield.transform_file_to_heightfield(args.mdt_directory + asc_file, args.png_directory 
			#			+ asc_file[:-4] + ".png", args.max_height)

			# Load info data to file

			#load_info.load_info(args.png_directory, args.orto_directory)

			# Divide

			#if args.divide:
			#	for base, dirs, files in os.walk(args.png_directory):
			#		for asc_file in files:	
			#			print("Dividing " + args.png_directory + asc_file + " in 16 images.")
			#			os.system('mkdir ' + args.png_directory + asc_file[:-4] + '-D')
			#			os.system('convert ' + args.png_directory + asc_file + ' -crop 4x4@ +repage ' + 
			#				args.png_directory + asc_file[:-4] + '-D/' + asc_file[:-4] + '_%d.png')
			#		break

			# Ask for coordinates

			#offset = 1000
			offset = 0
			minX = 704000 + offset # Incluído de momento a mano (coordenada central mdt - nºcolumnas/2 * tamaño celda)
			maxX = 704400 + 5760 * 5 - offset # Se comprueba en la lista que valores serían los mayores y cuales los menores
			minY = 4652400 + offset # Se suma el offset para que luego los datos concuerden al aplicarle el offset
			maxY = 4671000 + 4000 * 5 - offset
			
			#coordinates = input("Introduce UTM X and Y coordinates, separated by a blank space and respecting the values min " 
			#	+ "and max for the coordinates, for upper left vertex (" + str(minX) + " <= X1 <= " + str(maxX) + " " + str(minY) 
			#	+ " <= Y1 <= " + str(maxY) + "): ")
			#coordinates1 = coordinates.split()
			coordinates1 = ["713000", "4682000"]

			if (len(coordinates1) == 2 and float(coordinates1[0]) >= minX and float(coordinates1[0]) <= maxX and 
					float(coordinates1[1]) >= minY and float(coordinates1[1]) <= maxY):
				
				#coordinates = input("Introduce UTM X and Y coordinates, separated by a blank space and respecting the values min " 
				#	+ "and max for the coordinates, for bottom right vertex (" + coordinates1[0] + " <= X2 <= " + str(maxX) + " " + str(minY) 
				#	+ " <= Y2 <= " + coordinates1[1] + "): ")
				#coordinates2 = coordinates.split()
				coordinates2 = ["721000", "4678000"]	

				if (len(coordinates2) == 2 and float(coordinates2[0]) >= minX and float(coordinates2[0]) <= maxX and 
						float(coordinates2[1]) >= minY and float(coordinates2[1]) <= maxY and coordinates1[0] < coordinates2[0]
						and coordinates1[1] > coordinates2[1]):
					
					# Offset to adjust later during join process

					coordinates1[0] = float(coordinates1[0]) - offset
					coordinates2[0] = float(coordinates2[0]) + offset
					coordinates1[1] = float(coordinates1[1]) + offset
					coordinates2[1] = float(coordinates2[1]) - offset

					# Find mdts and ortophotos and write heighfields info 

					mdt_list = load_info.find_mdt(coordinates1[0], coordinates1[1], coordinates2[0], coordinates2[1])
					orto_list = load_info.find_orto(coordinates1[0], coordinates1[1], coordinates2[0], coordinates2[1], mdt_list)

					#pov_files = povray_divider.generate_pov_files(coordinates1, coordinates2, args.dir_from, args.angle, mdt_list, orto_list)
					
					heightfields = povray_writer.write_heightfields(mdt_list, orto_list) # Generate a string which contain the heightfields to pov file.

					# Generate povray file

					aspectRatio = povray_writer.write_povray_file(coordinates1, coordinates2, args.dir_from, args.angle, heightfields)
					#h = (coordinates1[1] - coordinates2[1]) / 4 # 1/4 of z values distance in UTM coordinates
					h = 2000
					w = int(h * aspectRatio + 0.5)

					# Rendering using new povray file

					os.system('povray +Irender.pov -D +W' + str(w) + ' +H' + str(h))
					#os.system('rm render.pov')
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