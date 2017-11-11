from laspy.file import File
from sklearn.neighbors import NearestNeighbors
import numpy as np
import colorsys, random, math

def generate_spheres(cam):	
	inFile = File("../LIDAR/PNOA_2010_LOTE1_ARA-NORTE_712-4670_ORT-CLA-COL.LAS", mode='r')

	pos_v = cam.get_pos()
	loo_v = cam.get_lookAt()
	pos_to_loo = [loo_v.get_x() - pos_v.get_x(), loo_v.get_y() - pos_v.get_y(), loo_v.get_z() - pos_v.get_z()]

	point_records = inFile.points

	x_scale = inFile.header.scale[0]
	x_offset = inFile.header.offset[0]

	y_scale = inFile.header.scale[1]
	y_offset = inFile.header.offset[1]

	z_scale = inFile.header.scale[2]
	z_offset = inFile.header.offset[2]

	#final_points = list(set(final_points))	
	#final_points = sorted(final_points, key=lambda x: (x[0], x[1], x[2]))
	#final_points = [[2, 3, 1], [1, 1, 0], [5, 1, 3], [3, 3, 4], [1, 2, 3]]	
	
	print(len(point_records))
	final_points = []	
	count = 0
	print("Reading all points...")		
	for point in point_records:	
		# Take point coordinates
		point = point[0]

		x_coordinate = point[0] * x_scale + x_offset
		y_coordinate = point[1] * y_scale + y_offset
		z_coordinate = point[2] * z_scale + z_offset
		
		# Take neighbour point

		if count == 0:
			a = point_records[1]
			aux = 2
		elif count >= (len(point_records) - 2):
			a = point_records[count - 1]
			aux = -2	
		else:
			a = point_records[count - 1]
			aux = 1

		a = a[0]	

		point_to_a = distance(point, a)

		if point_to_a < 150 and point_to_a != 0:
		#if point_to_a != 0:			
			# Take another neighbour (must be not collinear)

			found = False
			while(found != True):
				if aux == -len(point_records):
					print("BREAK")
					break
				if count + aux > len(point_records) - 1:
					aux = - 2

				b = point_records[count + aux]
				b = b[0]

				point_to_b = distance(point, b)
				a_to_b = distance(a, b)

				if point_to_a >= point_to_b and point_to_a >= a_to_b:
					if point_to_a != point_to_b + a_to_b:
						found = True
				elif point_to_a < point_to_b and point_to_b >= a_to_b:
					if point_to_b != point_to_a + a_to_b:
						found = True
				else:
					if a_to_b != point_to_a + point_to_b:
						found = True		

				if aux > 0:
					aux += 1
				else:
					aux += -1	

			if found == True:		

				# Calculate normal vector

				x_a = a[0] * x_scale + x_offset
				y_a = a[1] * y_scale + y_offset
				z_a = a[2] * z_scale + z_offset

				x_b = b[0] * x_scale + x_offset
				y_b = b[1] * y_scale + y_offset
				z_b = b[2] * z_scale + z_offset
				
				v1 = [x_a - x_coordinate, z_a - z_coordinate, y_a - y_coordinate]
				v2 = [x_b - x_coordinate, z_b - z_coordinate, y_b - y_coordinate]
				normal = [v1[1] * v2[2] - v2[1] * v1[2], -(v1[0] * v2[2] - v2[0] * v1[2]), v1[0] * v2[1] - v2[0] * v1[1]]

				if angle_between(pos_to_loo, normal) < 65:

					# Point colors

					red = str(point[10] / 65535)
					green = str(point[11] / 65535)
					blue = str(point[12] / 65535)

					z_coordinate *= 1.85

					final_points.append([str(x_coordinate), str(z_coordinate), str(y_coordinate), str(normal[0]), str(normal[1]),
						str(normal[2]), red, green, blue]) 

					# Create shape

					#spheres += ("disc {\n<" + str(x_coordinate) + ", " + str(z_coordinate) + ", " + str(y_coordinate) + ">, <" 
					#	+ str(normal[0]) + ", " + str(normal[1]) + ", " + str(normal[2]) + ">, 2\ntexture {\npigment { color rgb <" 
					#	+ red + ", " + green + ", " + blue + "> }\n}\n}\n")

					#spheres += ("sphere {\n<" + str(x_coordinate) + ", " + str(z_coordinate) + ", " + str(y_coordinate)
					#	+ ">, 2\ntexture {\npigment { color rgb <" + red + ", " + green + ", " + blue + "> }\n}\n}\n")

					#spheres += ("sphere {\n<0, 0, 0>, 2 scale <1, 0.4, 2>\nrotate <" + angle_x +", " + angle_y + ", " + angle_z + ">\ntranslate<" 
					#	+ str(x_coordinate) + ", " + str(z_coordinate) + ", " + str(y_coordinate) 
					#	+ ">\ntexture {\npigment { color rgb <"	+ red + ", " + green + ", " + blue + "> }\n}\n}\n")

		count += 1

	inFile.close()

	number_points = len(final_points)
	print(number_points)
	max_points = int(number_points / 5)
	max_points = number_points

	spheres = ""
	count = 0
	print("Taking " + str(max_points) + " points...")
	while(count < max_points):
		rand = random.randint(0, number_points - 1)
		point = final_points[rand]

		spheres += ("disc {\n<" + point[0] + ", " + point[1] + ", " + point[2] + ">, <" 
			+ point[3] + ", " + point[4] + ", " + point[5] + ">, 3\ntexture {\npigment { color rgb <" 
			+ point[6] + ", " + point[7] + ", " + point[8] + "> }\n}\n}\n")

		#final_points.append(point_records[rand][0])
		#point_records = np.delete(point_records, (rand), axis=0) # Muy lento
		count += 1

	return spheres

def distance(p1, p2):
	return ((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2 + (p1[2] - p2[2]) ** 2) ** 0.5

def sort_points(points):
	new_list = [points[0]]
	points.remove(points[0])
	count = 0
	
	while points:
		nearest = min(points, key=lambda x: distance(new_list[-1], x))
		new_list.append(nearest)
		#points.remove(nearest)
		count += 1
		print(count)

	return new_list	

def unit_vector(vector):
    if vector == [0, 0, 0]:
    	return vector
    else:	
    	return vector / np.linalg.norm(vector)

def angle_between(v1, v2):
    v1_u = unit_vector(v1)
    v2_u = unit_vector(v2)
    return np.arccos(np.clip(np.dot(v1_u, v2_u), -1.0, 1.0)) * 180.0 / math.pi	

if __name__ == "__main__":
    generate_spheres()	