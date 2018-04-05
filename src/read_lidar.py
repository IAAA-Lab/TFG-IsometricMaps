from laspy.file import File
import numpy as np
import colorsys, random, math, os, load_info

laszip = "../LAStools/bin/laszip"

def generate_spheres(lidar_list, areas_list, c1, c2):
	"""
	Create a string with the definition of spheres which represents points of the LiDAR file
	included into de coordinates passed as parameters.
	"""

	print("Generating spheres...")
	spheres = ""

	for lidar_file in lidar_list:
		lidar_file = lidar_file[0]
		print("Generating spheres from " + lidar_file)
		os.system(laszip + " -i " + lidar_file + " -o " + lidar_file[:-3] + "LAS")

		inFile = File(lidar_file[:-3] + "LAS", mode='r')

		point_records = inFile.points

		x_scale = inFile.header.scale[0]
		x_offset = inFile.header.offset[0]

		y_scale = inFile.header.scale[1]
		y_offset = inFile.header.offset[1]

		z_scale = inFile.header.scale[2]
		z_offset = inFile.header.offset[2]

		final_points = []
		count = 0
		total = 0
		number_points = len(point_records)
		max_points = int(number_points / 3)
		if max_points > 1000000:
			max_points = 1000000	
		print("Reading all points...")

		while(count < max_points and total < number_points):
			rand = random.randint(0, number_points - 1)
			point = point_records[rand]	
			# Take point coordinates
			point = point[0]

			x_coordinate = point[0] * x_scale + x_offset
			y_coordinate = point[1] * y_scale + y_offset
			z_coordinate = point[2] * z_scale + z_offset

			total += 1

			# In interesting zone?
			
			interest = False
			for area in areas_list:
				if load_info.is_collision(float(area[0]), float(area[1]), float(area[2]), float(area[3]), 
					x_coordinate, y_coordinate, x_coordinate, y_coordinate):
					if load_info.is_collision(float(c1[0]), float(c1[1]), float(c2[0]), float(c2[1]) - 500, 
						x_coordinate, y_coordinate, x_coordinate, y_coordinate):
						interest = True
						break
						
			if interest == True:
				red = str(point[10] / 65535)
				green = str(point[11] / 65535)
				blue = str(point[12] / 65535)

				z_coordinate *= 1.85
				z_coordinate -= 18

				final_points.append([str(x_coordinate), str(z_coordinate), str(y_coordinate), red, green, blue])
				count += 1				

		inFile.close()
		os.system("rm " + lidar_file[:-3] + "LAS")

		number_points = len(final_points)
		#max_points = int(number_points / 3)
		#max_points = number_points

		if max_points > 1000000:
			max_points = 1000000

		count = 0
		print("Taking " + str(number_points) + " points...")
		for point in final_points:
			#rand = random.randint(0, number_points - 1)
			#point = final_points[rand]

			spheres += ("sphere {\n<" + point[0] + ", " + point[1] + ", " + point[2] + ">, 2\ntexture {\npigment { color rgb <" 
				+ point[3] + ", " + point[4] + ", " + point[5] + "> }\n}\nno_shadow\n}\n")

			count += 1		

	return spheres		
