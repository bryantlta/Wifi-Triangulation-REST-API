# Grab arguments from command line 
#   (assuming that file being read is the second arg (first being this py file)), 
#   find that file, and read that file into string.

def readArgs():
	import sys

	in_filename = sys.argv[1]
	in_file = open(in_filename, 'r')
	string = in_file.read()
	return string 

def main():
    return readArgs()

if __name__ == 'main':
    main()

