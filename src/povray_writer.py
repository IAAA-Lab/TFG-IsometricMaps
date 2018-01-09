from PIL import Image
import os, load_info

def write_heightfields(mdt_list, orto_list):
	Image.MAX_IMAGE_PIXELS = 1000000000 # To hide PIL warning
	heightfields_to_pov = ""
	l_length = len(mdt_list)
	count = 0

	for mdt_file in mdt_list:
		count += 1
		if count == len(mdt_list):
			last_mdt = True
		else:
			last_mdt = False	

		height_field = ("height_field {\npng \"" + mdt_file[0] + "\"\nsmooth\nscale <" + mdt_file[1] 
			+ "*" + mdt_file[5] + ", 4000, " + mdt_file[2] + "*" + mdt_file[5] + ">\ntranslate <" 
			+ mdt_file[3] + ", 0, " + mdt_file[4] + "> + <-2.5, 0, -2.5>\n")

		# Add all ortophotos of specified mdt

		for orto_file in orto_list:
			if last_mdt == True:
				if (load_info.is_collision(float(mdt_file[3]), float(mdt_file[4]) + float(mdt_file[2]) * float(mdt_file[5]), float(mdt_file[3])
					+ float(mdt_file[1]) * float(mdt_file[5]), float(mdt_file[4]), float(orto_file[4]), float(orto_file[5]), float(orto_file[4])
					+ float(orto_file[2]) * float(orto_file[6]), float(orto_file[5]) + float(orto_file[3]) * float(orto_file[7])) == True):
					accept = True
				else:
					accept = False
			else:
				if mdt_file[0][mdt_file[0].rfind("/") + 1:-4] == orto_file[0]:
					accept = True
				else:
					accept = False
									
			if accept == True:
				for base, dirs, files in os.walk(orto_file[1]):
					image_format = ""
					for f in files:
						if f[-4:] == ".jpg" or f[-4:] == ".tif":
							image = orto_file[1] + "/" + f
							if f[-4:] == ".jpg":
								image_format = "jpeg"
							else:
								image_format = "tiff"	

				xSize = float(orto_file[2]) * float(orto_file[6])
				zSize = float(orto_file[3]) * -float(orto_file[7])
				xMin = float(orto_file[4]) - float(orto_file[2]) / 2
				zMin = float(orto_file[5]) + float(orto_file[3]) / 2 - zSize

				height_field += ("texture {\npigment {\nimage_map {\n" + image_format + " \"" + image + "\"\nonce}}" 
					+ "\nscale <" + str(xSize) + ", " + str(zSize) +", 1>\nrotate x*90\ntranslate " 
					+ "<" + str(xMin) + ", 0, " + str(zMin) + ">\n")

				height_field += write_texture_finish()

		height_field += ("}\n")		
		heightfields_to_pov += height_field	

	return heightfields_to_pov			

def write_povray_file(cam, heightfields, spheres):
	print("Generating pov-ray file...")
	pov = open("render.pov", "w")

	write_headers_and_camera(pov, cam)

	"""
	xCenter = xz1[0] + (xz2[0] - xz1[0]) / 2
	zCenter = xz2[1] + (xz1[1] - xz2[1]) / 2
	pov.write("light_source {<" + str(xCenter) + ", 0, " + str(zCenter) + "> + <5000, 8000, 0> color White }\n\n")
	"""

	pov.write("light_source {<800000, 8000000, 4900000> color White parallel}\n\n") # NE of Spain
	pov.write(heightfields)
	pov.write(spheres)

	pov.close()

def write_headers_and_camera(pov, cam):
	pov.write("#include \"colors.inc\"\n\n")

	pov.write("camera {\northographic\nlocation " + cam.get_pos().toString() + 
		"\nright " + cam.get_right().toString() + "\nup " + cam.get_up().toString() + 
		"\nlook_at " + cam.get_lookAt().toString() + "}\n\n")

def write_texture_finish(): 
	return "finish {\nambient 0.2\ndiffuse 0.8\nroughness 0.05\n}\n}\n"
