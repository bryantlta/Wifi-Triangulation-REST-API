from tools import access_pointsPackage
from tools import accessPointsMethods
from tools import postRequests
from tools import readArgs
from tools import accessPointsToXmlForSkyhook
from tools import checkConnectedToInternet
import sys 

def main():
    # [skyHook API Key, deviceId, optional xmlFile]
    if checkConnectedToInternet.connected_to_internet():
        args = sys.argv

        points = accessPointsMethods.scanAccessPoints()

        xmlFile = accessPointsToXmlForSkyhook.accessPointsToXmlForSkyHook(points, args[1], args[2])
        in_file = open(xmlFile, 'r')
        xmlString = in_file.read()
        api_location_endPoint = 'https://global.skyhookwireless.com/wps2/location'
        pr = postRequests.postRequestXML(api_location_endPoint, xmlString)
        print(pr.text)
        return pr

if __name__ == "__main__":
    main()