# Using https://github.com/kootenpv/access_points without having to pip install access_points.

def scanAccessPoints():
    # Get all access points for any wifi adapter. 

    import access_pointsPackage as access

    wifi_scanner = access.get_scanner()
    points = wifi_scanner.get_access_points()

    for p in points:
        print(p)

    return points

def main():
    return scanAccessPoints()

if __name__ == '__main__':
    main()