import sys, png

def transform_file_to_heightfield(file_in, file_out, maxHeight):
	print("Opening " + file_in)

	maxNum = 65535

	# Opening files
	asc = open(file_in)
	hf = open(file_out, "wb")

	# First data
	line = asc.readline()
	aux = line.split()
	ncols = int(aux[1])

	line = asc.readline()
	aux = line.split()
	nrows = int(aux[1])

	asc.readline() #xllcenter
	asc.readline() #yllcenter
	asc.readline() #cellsize
	asc.readline() #nodata_value

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
		newpoints = [x*maxNum/maxHeight for x in newpoints]
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

	print("Done!")
