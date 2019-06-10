from tools import access_pointsPackage
from tools import accessPointsMethods
from tools import postRequests
from tools import readArgs
from tools import accessPointsToXmlForSkyhook

def main():
    points = accessPointsMethods.scanAccessPoints()
    
    accessPointsToXmlForSkyhook.accessPointsToXmlForSkyHook()


if __name__ == "__main__":
    main()