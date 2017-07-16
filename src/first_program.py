import sys, argparse, heightfield, os, povray_writer

def main():
	# Arguments

	parser = argparse.ArgumentParser(description="First version of Pablo's TFG.")

	parser.add_argument("mdt_directory", help="Directory of the MDT files to transform.")
	parser.add_argument("png_directory", help="PNG files transformed destination directory.")
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

			#for base, dirs, files in os.walk(args.mdt_directory):
			#	for asc_file in files:
			#		heightfield.transform_file_to_heightfield(args.mdt_directory + asc_file, args.png_directory 
			#			+ asc_file[:-4] + ".png", args.max_height)

			# Divide

			#if args.divide:
			#	for base, dirs, files in os.walk(args.png_directory):
			#		for asc_file in files:	
			#			print("Dividing " + args.png_directory + asc_file + " in 16 images.")
			#			os.system('mkdir ' + args.png_directory + asc_file[:-4] + '-D')
			#			os.system('convert ' + args.png_directory + asc_file + ' -crop 4x4@ +repage ' + 
			#				args.png_directory + asc_file[:-4] + '-D/' + asc_file[:-4] + '_%d.png')
			#		break

			# Generate povray file

			aspectRatio = povray_writer.write_povray_file("../PNG/MDT05-0286-H30-LIDAR.png", "../PNOA/pnoa_2012_286_3_1.jpg", args.dir_from, args.angle)
			h = 1000
			w = int(h * aspectRatio)

			# Rendering using new povray file

			os.system('povray +Irender.pov +W' + str(w) + ' +H' + str(h))
			#os.system('rm render.pov')

		else:	
			print("ERROR: dir_from must be N, S, W or E.")
	else:
		print("ERROR: angle must be 45 or 30.")	

if __name__ == "__main__":
    main()