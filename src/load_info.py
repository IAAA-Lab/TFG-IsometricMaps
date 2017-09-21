import sys, os

def load_mdt_info(png_directory):
	print("Loading MDTs data...")
	f = open("mdt_data.txt", "w")

	for base, dirs, files in os.walk(png_directory):
		for mdt_file in files:
			if mdt_file[-4:] == ".txt":
				f.write(mdt_file[:-4])

				mdt = open(png_directory + mdt_file)
				for line in mdt:
					f.write(" ")
					aux = line.split()
					f.write(aux[0])

				mdt.close()		
				f.write("\n")					

	f.close()
	print("Load successful")

def load_orto_info(orto_directory):
	print("Loading ortophotos data...")
	f = open("orto_data.txt", "w")

	for base, dirs, files in os.walk(orto_directory):
		for d in dirs:
			for base2, dirs2, files2 in os.walk(orto_directory + d):
				for dAux in dirs2:
					for base3, dirs3, files3 in os.walk(orto_directory + d + "/" + dAux):
						for orto_file in files3:
							if orto_file[-4:] == ".jgw":
								jgw = open(orto_directory + d + "/" + dAux + "/" + orto_file)

								f.write(d + " " + dAux + " ")

								jgw.readline()
								jgw.readline() 
								jgw.readline()
								jgw.readline()

								aux = jgw.readline().split()
								f.write(aux[0] + " ")
								aux = jgw.readline().split()
								f.write(aux[0])

								jgw.close()
								f.write("\n")
				break	
		break	

	f.close()
	print("Load successful")

def load_info(png_directory, orto_directory):
	load_mdt_info(png_directory)
	load_orto_info(orto_directory)	
