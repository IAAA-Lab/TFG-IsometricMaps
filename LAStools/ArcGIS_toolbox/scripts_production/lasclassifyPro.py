#
# lasclassifyPro.py
#
# (c) 2013, martin isenburg - http://rapidlasso.com
#     rapidlasso GmbH - fast tools to catch reality
#
# uses lasclassify.exe to classify the LiDAR points
# for a folder of files in building points (class 6)
# and high vegetation (class 5) points
#
# requires that height above ground is stored in the
# user data field of each input point which can be
# done with lasheight or (licensed) lasground 
#
# LiDAR input:   LAS/LAZ/BIN/TXT/SHP/BIL/ASC/DTM
# LiDAR output:  LAS/LAZ/BIN/TXT
#
# for licensing see http://lastools.org/LICENSE.txt
#

import sys, os, arcgisscripting, subprocess

def check_output(command,console):
    if console == True:
        process = subprocess.Popen(command)
    else:
        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, universal_newlines=True)
    output,error = process.communicate()
    returncode = process.poll()
    return returncode,output 

### create the geoprocessor object
gp = arcgisscripting.create(9.3)

### report that something is happening
gp.AddMessage("Starting lasclassify production ...")

### get number of arguments
argc = len(sys.argv)

### report arguments (for debug)
#gp.AddMessage("Arguments:")
#for i in range(0, argc):
#    gp.AddMessage("[" + str(i) + "]" + sys.argv[i])

### get the path to LAStools
lastools_path = os.path.dirname(os.path.dirname(os.path.dirname(sys.argv[0])))

### make sure the path does not contain spaces
if lastools_path.count(" ") > 0:
    gp.AddMessage("Error. Path to .\\lastools installation contains spaces.")
    gp.AddMessage("This does not work: " + lastools_path)
    gp.AddMessage("This would work:    C:\\software\\lastools")
    sys.exit(1)    

### complete the path to where the LAStools executables are
lastools_path = lastools_path + "\\bin"

### check if path exists
if os.path.exists(lastools_path) == False:
    gp.AddMessage("Cannot find .\\lastools\\bin at " + lastools_path)
    sys.exit(1)
else:
    gp.AddMessage("Found " + lastools_path + " ...")

### create the full path to the lasclassify executable
lasclassify_path = lastools_path+"\\lasclassify.exe"

### check if executable exists
if os.path.exists(lastools_path) == False:
    gp.AddMessage("Cannot find lasclassify.exe at " + lasclassify_path)
    sys.exit(1)
else:
    gp.AddMessage("Found " + lasclassify_path + " ...")

### create the command string for lasclassify.exe
command = ['"'+lasclassify_path+'"']

### maybe use '-verbose' option
if sys.argv[argc-1] == "true":
    command.append("-v")

### counting up the arguments
c = 1

### add input LiDAR
wildcards = sys.argv[c+1].split()
for wildcard in wildcards:
    command.append("-i")
    command.append('"' + sys.argv[c] + "\\" + wildcard + '"')
c = c + 2

### maybe the units are in feet
if sys.argv[c] == "true":
    command.append("-feet")
c = c + 1
        
### maybe the elevation is in feet
if sys.argv[c] == "true":
    command.append("-elevation_feet")
c = c + 1
        
### maybe user-defined planarity
if sys.argv[c].replace(",",".") != "0.1":
    command.append("-planar")
    command.append(sys.argv[c].replace(",","."))
c = c + 1

### maybe user-defined planarity
if sys.argv[c].replace(",",".") != "0.4":
    command.append("-rugged")
    command.append(sys.argv[c].replace(",","."))
c = c + 1

### maybe user-defined planarity
if sys.argv[c] != "2":
    command.append("-ground_offset")
    command.append(sys.argv[c].replace(",","."))
c = c + 1

### maybe no gutters
if sys.argv[c] == "false":
    command.append("-no_gutters")

### else maybe wide gutters
elif sys.argv[c+1] == "true":
    command.append("-wide_gutters")
c = c + 2

### maybe also tiny buildings
if sys.argv[c] == "false":
    command.append("-small_buildings")
c = c + 1

### maybe keep tree overhang
if sys.argv[c] == "false":
    command.append("-keep_overhang")
c = c + 1

### maybe an output format was selected
if sys.argv[c] != "#":
    if sys.argv[c] == "las":
        command.append("-olas")
    elif sys.argv[c] == "laz":
        command.append("-olaz")
    elif sys.argv[c] == "bin":
        command.append("-obin")
    elif sys.argv[c] == "xyz":
        command.append("-otxt")
    elif sys.argv[c] == "xyzi":
        command.append("-otxt")
        command.append("-oparse")
        command.append("xyzi")
    elif sys.argv[c] == "txyzi":
        command.append("-otxt")
        command.append("-oparse")
        command.append("txyzi")
c = c + 1

### maybe an output directory was selected
if sys.argv[c] != "#":
    command.append("-odir")
    command.append('"' + sys.argv[c] + '"')
c = c + 1

### maybe an output appendix was selected
if sys.argv[c] != "#":
    command.append("-odix")
    command.append('"' + sys.argv[c] + '"')
c = c + 1

### maybe we should run on multiple cores
if sys.argv[c] != "1":
    command.append("-cores")
    command.append(sys.argv[c])
c = c + 1

### maybe there are additional input options
if sys.argv[c] != "#":
    additional_options = sys.argv[c].split()
    for option in additional_options:
        command.append(option)

### report command string
gp.AddMessage("LAStools command line:")
command_length = len(command)
command_string = str(command[0])
command[0] = command[0].strip('"')
for i in range(1, command_length):
    command_string = command_string + " " + str(command[i])
    command[i] = command[i].strip('"')
gp.AddMessage(command_string)

### run command
returncode,output = check_output(command, False)

### report output of lasclassify
gp.AddMessage(str(output))

### check return code
if returncode != 0:
    gp.AddMessage("Error. lasclassify failed.")
    sys.exit(1)

### report happy end
gp.AddMessage("Success. lasclassify done.")
