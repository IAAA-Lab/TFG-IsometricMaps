from PIL import Image
from laspy.file import File
import numpy as np
import sys, os

m_file = "mdt_data.txt"
o_file = "orto_data.txt"
l_file = "lidar_data.txt"
a_file = "areas_interest.txt"

laszip = "/home/pablo/Documentos/LAStools/bin/laszip"

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
	y2 = y2 - 1500

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
							if orto_file[-4:] == ".jpg" or orto_file[-4:] == ".tif":
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
				# TODO: Lista diferente para 25831? Concatenarla al inicio (o al final) de ortos para forzar que se incluyan antes o después (depende como pinte el povray) y se monten correctamente con las ortos en 25830. Mirar como montar entre 2 de 25831.
				ortos.append(info)				

	f.close()

	return ortos


def load_lidar_info(lidar_directory):
	print("Loading LIDARs data...")
	f = open(l_file, "w")

	for base, dirs, files in os.walk(lidar_directory):
		for lidar_file in files:
			lidar_file = lidar_directory + lidar_file
			f.write(lidar_file)

			os.system(laszip + " -i " + lidar_file + " -o " + lidar_file[:-3] + "LAS")

			inFile = File(lidar_file[:-3] + "LAS", mode='r')

			x_min = inFile.header.min[0]
			x_max = inFile.header.max[0]

			y_min = inFile.header.min[1]
			y_max = inFile.header.max[1]

			f.write(" " + str(x_min) + " " + str(y_min) + " " + str(x_max) + " " + str(y_max) + "\n")

			inFile.close()
			os.system("rm " + lidar_file[:-3] + "LAS")

	f.close()
	print("Load successful")

def find_lidar(areas):
	lidars = []
	f = open(l_file, "r")

	for line in f:
		info = line.split()

		# Calculate lidar vertex points
		
		mx1 = float(info[1])
		mx2 = float(info[3])
		my1 = float(info[4])
		my2 = float(info[2])

		for area in areas:
			if is_collision(float(area[0]), float(area[1]), float(area[2]), float(area[3]), mx1, my1, mx2, my2):
				lidars.append(info)
				break
		
	f.close()

	return lidars

def find_a_interest(x1, y1, x2, y2):
	areas = []
	f = open(a_file, "r")

	for line in f:
		info = line.split()

		mx1 = float(info[0])
		mx2 = float(info[2])
		my1 = float(info[1])
		my2 = float(info[3])

		if is_collision(x1, y1, x2, y2, mx1, my1, mx2, my2):
			areas.append(info)

	f.close()

	return areas			

def is_collision(x1, y1, x2, y2, mx1, my1, mx2, my2):
	y2 -= 1500
	# X axis
	if ((x2 < mx1) or (x1 > mx2)):
		return False
	# Y axis	
	elif ((y1 < my2) or (y2 > my1)):
		return False
	else:
		return True	

def load_info(png_directory, orto_directory, lidar_directory):
	load_mdt_info(png_directory)
	load_orto_info(orto_directory)
	load_lidar_info(lidar_directory)	
