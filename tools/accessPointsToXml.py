# Grab all access points and turn them into an xml file for SkyHook. 

# https://stackabuse.com/reading-and-writing-xml-files-in-python/
# https://bugs.python.org/issue10942 (issue with why ElementTree.tostring returns byte instead of string)

def accessPointsToXmlForSkyHook(accessPoints, apiKey, deviceId, xmlFile):
    import xml.etree.ElementTree as ElementTree

    # Location RQ values:
    LocationRQ = ElementTree.Element('LocationRQ')

    LocationRQ.set('xlms', "http://skyhookwireless.com/wps/2005")
    LocationRQ.set('version', "2.25")
    LocationRQ.set('street-address-lookup', "full")
    LocationRQ.set('timezone-lookup', "true")

    authentication = ElementTree.SubElement(LocationRQ, 'authentication')
    authentication.set('key', apiKey)
    authentication.set('username', deviceId)

    for point in accessPoints:
        accessPoint = ElementTree.SubElement(LocationRQ, 'access-point')
        
        bssid = point.bssid.replace(':','')
        quality = point.quality

        accessPoint.set('mac', bssid)
        accessPoint.set('signal-strength', quality)
    
    mydata = ElementTree.tostring(data, encoding="unicode") 
    myfile = open(xmlFile, "w")
    myfile.write(mydata)





    

    