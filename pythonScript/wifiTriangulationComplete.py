import sys
import access_pointsPackage as access
 
# Try/Except statements for Python 2/3: https://stackoverflow.com/questions/3764291/checking-network-connection/29854274#29854274
try: 
    import urllib2 as urllib2
except:
    import urllib.request as urllib2

import urllib
import requests
import xmlToDict
import json 
import requests
import hashlib
import platform
import time 
import inspect 

key = 'eJwz5DQ0AAFLA2MLzmojMzcXIxNDR11LFxdTXQsDFwtdZ1MDY10nZ0NTU1NXR0cDY7daABFhCyk'

def checkPyVersion():
    print(platform.python_version())
    return platform.python_version()

def inspectModules():
    print(inspect.getouterframes(inspect.currentframe()))

def main():
    # [skyHook API Key, optional deviceId, optional boolean for accesspoints, optional xmlFile]
    if internet_on():
        points = scanAccessPoints() # Obtain Access Point objects.
        xmlFile = accessPointsToXmlForSkyHook(points, key, hashEncoder()) # Access Points to XML file.
        xmlString = readIn('xmlRequest.xml') # Read from the XML File. 
        response = postRequestXML('https://global.skyhookwireless.com/wps2/location', xmlString) # POST Request
        jsonString = xmlToJson(response._content) # XML string to Json String 
        jsonStringToObj(jsonString) # Write Json String to .json file.
        return jsonString

# https://stackoverflow.com/questions/3764291/checking-network-connection
def internet_on():
    # Checks whether the internet is on. 
    try:
        urllib2.urlopen('http://google.com', timeout=1)
        return True
    except urllib2.URLError: 
        return False

def scanAccessPoints():
    # Get all access points for any wifi adapter. 
    wifi_scanner = access.get_scanner()
    points = wifi_scanner.get_access_points()
    # print('AccessPoints: ' + str(len(points)))
    return points

def hashEncoder():
    # Encodes the platform's node using sha256. 
    nodeName = platform.node()

    try:
        encodedNode = hashlib.sha256(nodeName).hexdigest()
    except:
        encodedNode = hashlib.sha256(nodeName.encode('UTF-8')).hexdigest()
        
    encodedNode = encodedNode.upper()
    return encodedNode

def accessPointsToXmlForSkyHook(accessPoints, apiKey, deviceId, xmlFile = 'xmlRequest.xml'):
    # Turning access point objects to xml for the skyhook api. 
    import xml.etree.ElementTree as ElementTree

    # Location RQ values:
    LocationRQ = ElementTree.Element('LocationRQ')

    LocationRQ.set('xmlns', "http://skyhookwireless.com/wps/2005")
    LocationRQ.set('version', "2.26")
    LocationRQ.set('street-address-lookup', "full")
    
    authentication = ElementTree.SubElement(LocationRQ, 'authentication')
    authentication.set('version', '2.2')

    key = ElementTree.SubElement(authentication, 'key')
    key.set('key', apiKey)
    key.set('username', deviceId)
    

    for point in accessPoints:
        accessPoint = ElementTree.SubElement(LocationRQ, 'access-point')

        bssid = ElementTree.SubElement(accessPoint, 'mac')
        bssid.text = str(point.bssid).replace(':', '')

        quality = ElementTree.SubElement(accessPoint, 'signal-strength')
        quality.text = str(point.quality)
    
    try:
        mydata = ElementTree.tostring(LocationRQ)
        myfile = open(xmlFile, "w")
        myfile.write(mydata)
    except:
        mydata = ElementTree.tostring(LocationRQ, encoding = 'unicode') 
        myfile = open(xmlFile, "w")
        myfile.write(mydata)

    return xmlFile 

def readIn(fileName):
    # Reading in (turning into string) a file.
	in_file = open(fileName, 'r')
	string = in_file.read()
	return string 

def postRequestXML(location_api_endPoint, xml_string):
    # Sending a POST request to a URL. 
    import requests
    header = {'Content-Type': 'text/xml'}

    response = requests.post(location_api_endPoint, data = xml_string, headers = header)
    print(response._content)
    return response

def xmlToJson(xml_string):
    # Converting XML string to JSON string.
    orderedDict = xmlToDict.parse(xml_string)
    jsonObj = json.dumps(orderedDict)
    print(jsonObj)
    return jsonObj

def jsonStringToObj(jsonString):
    # Writing into a JSON file the JSON String. 
    jsonFile = open("skyhook.json", "w+")
    jsonFile.write(jsonString)
    jsonFile.close()

if __name__ == '__main__':
    #start_time = time.time()
    main()
    #print("--- %s seconds ---" % (time.time() - start_time))