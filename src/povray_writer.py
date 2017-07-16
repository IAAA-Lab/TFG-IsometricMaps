from PIL import Image
import os, cameraUtils

def write_povray_file(mdt_file, ortophoto_directory, dirFrom, angle):
	Image.MAX_IMAGE_PIXELS = 1000000000 # To hide PIL warning
	print("Generating pov-ray file...")
	
	mdt = open(mdt_file[:-4] + ".txt")
	mdt_width = mdt.readline()[:-1]
	mdt_height = mdt.readline()[:-1]
	mdt_x_center = mdt.readline()[:-1]
	mdt_z_center = mdt.readline()[:-1]

	pov = open("render.pov", "w")

	for base, dirs, files in os.walk(ortophoto_directory):
		for f in files:
			if f[-4:] == ".jpg":
				image = ortophoto_directory + "/" + f
				width, height = Image.open(image).size	
			if f[-4:] == ".jgw":
				jgw = open(ortophoto_directory + "/" + f)

				pixelX_size = jgw.readline()
				jgw.readline() 
				jgw.readline()
				pixelZ_size = -float(jgw.readline())
				x_coord = jgw.readline()
				z_coord = jgw.readline()
		break		
	
	xSize = int(float(pixelX_size) * width)
	zSize = int(float(pixelZ_size) * height)
	xMin = float(x_coord) - float(pixelX_size) / 2
	zMin = float(z_coord) + float(pixelZ_size) / 2 - zSize

	cam = cameraUtils.calculate_camera(xMin, zMin, xSize, zSize, angle, dirFrom)

	write_headers_and_camera(pov, cam)

	xCenter = xMin + xSize / 2
	zCenter = zMin + zSize / 2

	pov.write("light_source {<" + str(xCenter) + ", 0, " + str(zCenter) + "> + <5000, 8000, 0> color White }\n")

	pov.write("height_field {png \"" + mdt_file + "\" smooth scale <" + mdt_width + 
		"*5, 4000, " + mdt_height + "*5> translate <" + mdt_x_center + ", 0, " + 
		mdt_z_center + "> + <-2.5, 0, -2.5>\n")

	pov.write("texture{pigment{image_map{jpeg \"" + image + "\" once}} " +
		"scale <" + str(xSize) + ", " + str(zSize) +", 1> rotate x*90 translate " +
		"<" + str(xMin) + ", 0, " + str(zMin) + "> + <-0.25, 0, -0.25>}\n")

	write_finish(pov)

	pov.write("}")

	pov.close()

	return cam.get_aspectRatio()

def write_headers_and_camera(pov, cam):
	pov.write("#include \"colors.inc\"\n")

	pov.write("camera {orthographic location " + cam.get_pos().toString() + 
		" right " + cam.get_right().toString() + " up " + cam.get_up().toString() + 
		" look_at " + cam.get_lookAt().toString() + "}\n")

def write_finish(pov):
	pov.write("finish { ")
	pov.write("ambient 0.2 ")
	pov.write("diffuse 0.8 ")
	pov.write("roughness 0.05 ")
	pov.write("}")	