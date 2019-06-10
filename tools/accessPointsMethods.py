# Using https://github.com/kootenpv/access_points without having to pip install access_points.

def scanAccessPoints():
    # Get all access points for any wifi adapter. 

    from tools import access_pointsPackage as access

    wifi_scanner = access.get_scanner()
    points = wifi_scanner.get_access_points()

    return points

def parseFromPoints(accessPoints):
    values = [(point.ssid, point.bssid, point.quality) for point in accessPoints]
    return values

def main():
    points = scanAccessPoints()
    return parseFromPoints(points)

if __name__ == '__main__':
    main()