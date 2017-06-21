import sys, argparse, heightfield, os

def main():
	# Arguments

	parser = argparse.ArgumentParser(description="First version of Pablo's TFG.")

	parser.add_argument("mdt_directory", help="Directory of the MDT files to transform.")
	parser.add_argument("png_directory", help="PNG files transformed destination directory.")
	parser.add_argument("result_name", help="Name of the image (jpg) result.")

	parser.add_argument("--max_height", dest="max_height", type=int, default=2200, metavar="MAX_HEIGHT",
		help="Max height transforming MDT files. Higher heights will be considered MAX_HEIGHT " + 
			"(default value = 2200)")

	parser.add_argument("--divide", help="Divide PNG files in 16 image portions.", action="store_true")

	args = parser.parse_args()

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

	if args.divide:
		for base, dirs, files in os.walk(args.png_directory):
			for asc_file in files:	
				print("Dividing " + args.png_directory + asc_file + " in 16 images.")
				os.system('mkdir ' + args.png_directory + asc_file[:-4] + '-D')
				os.system('convert ' + args.png_directory + asc_file + ' -crop 4x4@ +repage ' + 
					args.png_directory + asc_file[:-4] + '-D/' + asc_file[:-4] + '_%d.png')
			break

	# Generate povray file

	print("Generating pov-ray file...")
	pov = open(args.result_name + ".pov", "w")

	pov.write("#include \"colors.inc\"\n")
	pov.write("camera {orthographic angle 50 location <15, 15, -15> look_at  <0, 0, 0> right x * " + 
		"image_width / image_height translate <0, 2.00, 0>}\n")
	pov.write("global_settings {ambient_light rgb <1.00000, 1.0000, 1.0000> }\n")
	pov.write("light_source { <2000, 2000, 0> White parallel point_at <0,0,0> fade_power 0 }\n")
	pov.write("object { height_field { png \"../PNG/MDT05-0286-H30-LIDAR-D/MDT05-0286-H30-LIDAR_2.png\""
		+ "hierarchy on texture { pigment { image_map { jpeg \"../PNOA/pnoa_2012_286_3_1.jpg\"}" +
		" scale 0.5}}} scale <20,10,20>	translate <-1, 2,-20>}")
	
	pov.close()			

	# Rendering using new povray file

	os.system('povray ' + args.result_name + '.pov')
	os.system('rm ' + args.result_name + '.pov')

if __name__ == "__main__":
    main()