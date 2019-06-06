# Using https://github.com/kootenpv/access_points without having to pip install access_points.

def scanAccessPoints():
    # Get all access points. 
    
    import access_pointsPackage as access


    wifi_scanner = access.get_scanner("wlp2s0")
    points = wifi_scanner.get_access_points()

    for p in points:
        print(p)

    return points