# Grab arguments from command line 
#   (assuming that file being read is the second arg (first being this py file)), 
#   find that file, and read that file into string.

def readInArgs(k):
	import sys

	in_filename = sys.argv[k]
	in_file = open(in_filename, 'r')
	string = in_file.read()
	return string 

def readAllArgs():
	import sys
	return sys.argv

def main():
    return readInArgs(1)

if __name__ == 'main':
    main()

