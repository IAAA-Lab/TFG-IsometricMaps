import argparse, os

laszip_ex = "/home/pablo/Documentos/LAStools/bin/laszip" # Directory of laszip program

# Arguments

parser = argparse.ArgumentParser(description="Program to transform .LAZ files to .LAS files using laszip (LAStools)")

parser.add_argument("laz_directory", help="Directory of the .LAZ files to transform.")
parser.add_argument("las_directory", help=".LAS files transformed destination directory.")

args = parser.parse_args()

for base, dirs, files in os.walk(args.laz_directory):
	for f in files:
		os.system(laszip_ex + " -i " + args.laz_directory + f + " -o " + args.las_directory + f[:-3] + "LAS")
