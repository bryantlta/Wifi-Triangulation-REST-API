import urllib

def infoFromIp(version, ip, key, user, prettyPrint = False):
    # Get info from IP address.

    versionString = "version=" + str(version)
    ipString = "&ip=" + str(ip)
    prettyPrintString = "&prettyPrint=" + str(prettyPrint)
    keyString = "&key=" + str(key)
    userString = "&user=" + str(user)

    hyperLocalURL = "https://context.skyhookwireless.com/accelerator/ip?" + versionString \
        + ipString + prettyPrintString + keyString + userString

    resp = urllib.request.urlopen(hyperLocalURL)
    jsonResponse = json.loads(resp.read())
    print(jsonResponse)
    return jsonResponse