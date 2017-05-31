import sys, png

if (len(sys.argv) > 1):
	print("Opening " + sys.argv[1])

	everestHeight = 8848
	maxNum = 65535

	# Opening files
	asc = open(sys.argv[1])
	hf = open("salida.png", "wb")

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
	completeBar = nrows/40
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
		newpoints = [x*maxNum/everestHeight for x in newpoints]
		newpoints = [int(x) for x in newpoints]		 
		pointsList.append(newpoints)																				

		count +=1
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
else:
	print("Error: Introduce MDT file.")
