import os, argparse

def main():
	parser = argparse.ArgumentParser(description="Histmatch program")
	parser.add_argument("orto_directory", help="Directory of the ORTO files (or directories) to transform.")
	args = parser.parse_args()

	print("Starting histmatch program...")

	if args.orto_directory[-1] != "/":
		args.orto_directory += "/"

	for base, dirs, files in os.walk(args.orto_directory):
		for d in dirs:
			baseImage = args.orto_directory + dirs[0] + "/" + dirs[0]
			for base2, dirs2, files2 in os.walk(args.orto_directory + d):
				for f in files2:
					if f[-4:] == ".jpg":
						image = args.orto_directory + d + "/" + f
						result = args.orto_directory + d + "/H_" + f
						
						print("Modifying " + image)	
						os.system('./histmatch ' + baseImage + ' ' + image + ' ' + result)

if __name__ == "__main__":
    main()	