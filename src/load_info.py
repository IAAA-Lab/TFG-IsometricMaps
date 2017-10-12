from PIL import Image
import sys, os

m_file = "mdt_data.txt"
o_file = "orto_data.txt"

def load_mdt_info(png_directory):
	print("Loading MDTs data...")
	f = open(m_file, "w")

	for base, dirs, files in os.walk(png_directory):
		for mdt_file in files:
			if mdt_file[-4:] == ".txt":
				f.write(png_directory + mdt_file[:-3] + "png")

				mdt = open(png_directory + mdt_file)
				for line in mdt:
					f.write(" ")
					aux = line.split()
					f.write(aux[0])

				mdt.close()		
				f.write("\n")					

	f.close()
	print("Load successful")

def find_mdt(x1, y1, x2, y2):
	mdts = []
	f = open(m_file, "r")

	for line in f:
		info = line.split()

		# Calculate mdt vertex points
		mx1 = float(info[3])
		mx2 = float(info[3]) + float(info[1]) * float(info[5])
		my1 = float(info[4]) + float(info[2]) * float(info[5])
		my2 = float(info[4])

		if is_collision(x1, y1, x2, y2, mx1, my1, mx2, my2):
			mdts.append(info)
		
	f.close()

	return mdts

def load_orto_info(orto_directory):
	Image.MAX_IMAGE_PIXELS = 1000000000 # To hide PIL warning
	print("Loading ortophotos data...")
	f = open(o_file, "w")

	for base, dirs, files in os.walk(orto_directory):
		for d in dirs:
			for base2, dirs2, files2 in os.walk(orto_directory + d):
				for dAux in dirs2:
					for base3, dirs3, files3 in os.walk(orto_directory + d + "/" + dAux):
						for orto_file in files3:
							if orto_file[-4:] == ".jpg" and orto_file[0] == "H":
								image = orto_directory + d + "/" + dAux + "/" + orto_file
								width, height = Image.open(image).size	
							if orto_file[-4:] == ".jgw":
								jgw = open(orto_directory + d + "/" + dAux + "/" + orto_file)

								f.write(d + " " + orto_directory + d + "/" + dAux + " ")

								aux = jgw.readline().split()
								f.write(aux[0] + " ")

								jgw.readline() 
								jgw.readline()

								aux = jgw.readline().split()
								f.write(aux[0] + " ")

								aux = jgw.readline().split()
								f.write(aux[0] + " ")
								aux = jgw.readline().split()
								f.write(aux[0] + " ")

								jgw.close()

						f.write(str(width) + " ")
						f.write(str(height))
						f.write("\n")		
				break	
		break	

	f.close()
	print("Load successful")

def find_orto(x1, y1, x2, y2, mdts):
	ortos = []
	f = open(o_file, "r")

	for line in f:
		info = line.split()
		found = False
		for mdt in mdts:
			if mdt[0][mdt[0].rfind("/") + 1:-4] == info[0]:
				found = True
				break	

		if found:
			mx1 = float(info[4]) - (float(info[2]) / 2)
			my1 = float(info[5]) - (float(info[3]) / 2)
			mx2 = mx1 + float(info[2]) * float(info[6]) + float(info[2])
			my2 = my1 + float(info[3]) * float(info[7]) + float(info[3])
			
			if is_collision(x1, y1, x2, y2, mx1, my1, mx2, my2):
				ortos.append(info)				

	f.close()

	return ortos	


def is_collision(x1, y1, x2, y2, mx1, my1, mx2, my2):
	# X axis
	if ((x2 < mx1) or (x1 > mx2)):
		return False
	# Y axis	
	elif ((y1 < my2) or (y2 > my1)):
		return False
	else:
		return True	

def load_info(png_directory, orto_directory):
	load_mdt_info(png_directory)
	load_orto_info(orto_directory)	
