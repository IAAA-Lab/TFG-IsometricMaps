import heightfield, os

mdt_directory = "./MDT"
png_directory = "./PNG"

for base, dirs, files in os.walk(mdt_directory):
	for asc_file in files:
		heightfield.transform_file_to_heightfield(mdt_directory + "/" + asc_file, 
			png_directory + "/" + asc_file[:-4] + ".png")
