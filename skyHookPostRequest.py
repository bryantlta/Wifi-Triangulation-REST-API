import sys
import requests

# Need file name, index of ip & newline
if len (sys.argv) < 2:
        print("USAGE: {} <xml filename>".format(sys.argv[0]))
        exit(-1)
in_filename = sys.argv[1]

# Open input and output file streams
in_file = open(in_filename, "r")              

# Begin processing IP addresses
print("Script started")   
print("Analyzing Log File")

# Read in xml file
xml_string = in_file.read()   

# HTML headers
headers = {'Content-Type': 'text/xml'}

# Make the request to the Precision location API
r = requests.post('https://global.skyhookwireless.com/wps2/location', data=xml_string, headers=headers)
print(r.text)

print("Script finished")                 

# Close input and output file streams
in_file.close()