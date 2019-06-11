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

#import requests

def main():
    # [skyHook API Key, optional deviceId, optional boolean for accesspoints, optional xmlFile]
    if internet_on():
        args = sys.argv
        points = scanAccessPoints()
        # numPoints = len(points)
        xmlFile = accessPointsToXmlForSkyHook(points, str(args[1]), 'JFSLIFJE87')
        xmlString = readIn(xmlFile)
        api_location_endPoint = 'https://global.skyhookwireless.com/wps2/location'
        request = postRequestXML(api_location_endPoint, xmlString)
        print(request.text)
        return request

# https://stackoverflow.com/questions/3764291/checking-network-connection
def internet_on():
    try:
        urllib2.urlopen('http://google.com', timeout=1)
        return True
    except urllib2.URLError: 
        return False

def scanAccessPoints():
    # Get all access points for any wifi adapter. 

    wifi_scanner = access.get_scanner()
    points = wifi_scanner.get_access_points()
    print('AccessPoints: ' + str(len(points)))
    return points

def accessPointsToXmlForSkyHook(accessPoints, apiKey, deviceId, xmlFile = 'xmlRequest.xml'):
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
	in_file = open(fileName, 'r')
	string = in_file.read()
	return string 

def postRequestXML(location_api_endPoint, xml_string):
    import requests
    header = {'Content-Type': 'text/xml'}

    response = requests.post(location_api_endPoint, data = xml_string, headers = header)
    return response
    """req = urllib2.Request(location_api_endPoint, data=xml_string)
    openObj = urllib2.urlopen(req)
    response = openObj.read()
    print(response)
    return response"""

def xmlToJson(xml_string):
    orderedDict = xmlToDict.parse(xml_string)
    jsonObj = json.dumps(orderedDict)
    return jsonObj

if __name__ == '__main__':
    main()