import os, sys

minx = 13
maxx = 14
miny = 15
maxy = 16

#minx = 36
#maxx = 104
#miny = 32
#maxy = 100
#minx = 18
#maxx = 52
#miny = 16
#maxy = 50
#minx = 9
#maxx = 26
#miny = 8
#maxy = 25

# Progress bar
toolbar_width = maxx - minx + 1

# setup toolbar
sys.stdout.write("[%s]" % (" " * toolbar_width))
sys.stdout.flush()
sys.stdout.write("\b" * (toolbar_width+1)) # return to start of line, after '[' 

x = minx
while x <= maxx:
	sys.stdout.write("=")
	sys.stdout.flush()
	y = miny
	while y <= maxy:		
		actualx = x * 2
		actualy = y * 2

		if os.path.isfile('/media/pablo/280F8D1D0A5B8545/TFG_files/cliente_local/45/N/6/map_' + str(actualx) + '_' + str(actualy) + '.png'):
			file1 = '/media/pablo/280F8D1D0A5B8545/TFG_files/cliente_local/45/N/6/map_' + str(actualx) + '_' + str(actualy) + '.png'
		else:
			file1 = 'negro.png'
		if os.path.isfile('/media/pablo/280F8D1D0A5B8545/TFG_files/cliente_local/45/N/6/map_' + str(actualx) + '_' + str(actualy + 1) + '.png'):
			file2 = '/media/pablo/280F8D1D0A5B8545/TFG_files/cliente_local/45/N/6/map_' + str(actualx) + '_' + str(actualy + 1) + '.png'
		else:
			file2 = 'negro.png'
		if os.path.isfile('/media/pablo/280F8D1D0A5B8545/TFG_files/cliente_local/45/N/6/map_' + str(actualx + 1) + '_' + str(actualy) + '.png'):
			file3 = '/media/pablo/280F8D1D0A5B8545/TFG_files/cliente_local/45/N/6/map_' + str(actualx + 1) + '_' + str(actualy) + '.png'
		else:
			file3 = 'negro.png'
		if os.path.isfile('/media/pablo/280F8D1D0A5B8545/TFG_files/cliente_local/45/N/6/map_' + str(actualx + 1) + '_' + str(actualy + 1) + '.png'):
			file4 = '/media/pablo/280F8D1D0A5B8545/TFG_files/cliente_local/45/N/6/map_' + str(actualx + 1) + '_' + str(actualy + 1) + '.png'
		else:
			file4 = 'negro.png'			

		os.system('convert -append ' + file1 + ' ' + file2 + ' out1.png')
		os.system('convert -append ' + file3 + ' ' + file4 + ' out2.png')
		os.system('convert +append out1.png out2.png out.png')
		os.system('convert out.png -resize 256x181\! /media/pablo/280F8D1D0A5B8545/TFG_files/cliente_local/45/N/5/map_' + str(int(actualx / 2)) + '_' + str(int(actualy / 2)) + '.png')

		y += 1
	x += 1

os.system('rm out1.png out2.png out.png')
sys.stdout.write("\n")
print('DONE')			