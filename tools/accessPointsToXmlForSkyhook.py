# Grab all access points and turn them into an xml file for SkyHook. 

# https://stackabuse.com/reading-and-writing-xml-files-in-python/
# https://bugs.python.org/issue10942 (issue with why ElementTree.tostring returns byte instead of string)

def accessPointsToXmlForSkyHook(accessPoints, apiKey, deviceId, xmlFile = 'xmlFile.xml'):
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
    
    mydata = ElementTree.tostring(LocationRQ, encoding="unicode") 
    myfile = open(xmlFile, "w")
    myfile.write(mydata)
    return xmlFile 





    

    