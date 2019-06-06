def infoFromIp(version, ip, key, user, prettyPrint = False):
    # Get info from IP address using the skyHook ip location api. 
    import urllib
    import json
    import argparse

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

def main():
    import argparse

    parser = argparse.ArgumentParser(description="Get info about IP.") 
    parser.add_argument('--ip', dest='ip', required=True) 
    parser.add_argument('--version', dest='version', required=True)
    parser.add_argument('--prettyPrint', dest='print', required=False) 
    parser.add_argument('--key', dest='key', required=True)
    parser.add_argument('--user', dest='user', required=True)


    args = parser.parse_args()
    ip = str(args.ip)
    version = str(args.version)
    prettyPrint = str(args.print)
    key = str(args.key)
    user = str(args.user)

    return infoFromIp(version, ip, key, user, prettyPrint)

if __name__ == '__main__':
    main()