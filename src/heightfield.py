import sys, png

def transform_file_to_heightfield(file_in, file_out, maxHeight):
	"""
	Create PNG and TXT file from ASC file passed as parameter.
	"""
	
	print("Opening " + file_in)

	maxNum = 65535

	# Opening files
	asc = open(file_in)
	hf = open(file_out, "wb")
	info = open(file_out[:-4] + ".txt", "w")

	# First data
	line = asc.readline()
	aux = line.split()
	ncols = int(aux[1])
	info.write(aux[1] + "\n")

	line = asc.readline()
	aux = line.split()
	nrows = int(aux[1])
	info.write(aux[1] + "\n")

	line = asc.readline() # xllcenter
	aux = line.split()
	info.write(aux[1] + "\n")

	line = asc.readline() # zllcenter
	aux = line.split()
	info.write(aux[1] + "\n")

	line = asc.readline() #cellsize
	aux = line.split()
	info.write(aux[1] + "\n")
	
	line = asc.readline() #nodata_value
	aux = line.split()
	nodata = int(aux[1])

	print("Reading points...")

	# Progress bar
	toolbar_width = 40
	completeBar = nrows//toolbar_width
	count = 0

	# setup toolbar
	sys.stdout.write("[%s]" % (" " * toolbar_width))
	sys.stdout.flush()
	sys.stdout.write("\b" * (toolbar_width+1)) # return to start of line, after '[' 

	# Read rows
	pointsList = []
	lines = asc.readlines()
	lines = lines[:-1]
	for line in lines:
		points = line.split()
		newpoints = [float(x) for x in points]
		newpoints = [0 if x == nodata else x for x in newpoints]
		newpoints = [x*maxNum/maxHeight for x in newpoints]
		newpoints = [maxNum if x > maxNum else x for x in newpoints]
		newpoints = [int(x) for x in newpoints]
		pointsList.append(newpoints)

		count += 1
		#print("count = " + str(count) + " - completeBar = " + str(completeBar))
		if (count == completeBar):
			count = 0
			sys.stdout.write("=")
			sys.stdout.flush()

	sys.stdout.write("\n")

	print("Generating png...")
	w = png.Writer(width=ncols, height=nrows, greyscale=True, bitdepth=16)
	w.write(hf, pointsList)

	asc.close()
	hf.close()
	info.close()

	print("Done!")
