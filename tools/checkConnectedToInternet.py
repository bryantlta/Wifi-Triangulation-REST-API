# https://stackoverflow.com/questions/3764291/checking-network-connection
def internet_on():
    # Try/Except statements for Python 2/3: https://stackoverflow.com/questions/3764291/checking-network-connection/29854274#29854274
    try: 
        import urllib2 as urllib
    except:
        import urllib.request as urllib

    try:
        urllib.urlopen('http://google.com', timeout=1)
        return True
    except: 
        return False