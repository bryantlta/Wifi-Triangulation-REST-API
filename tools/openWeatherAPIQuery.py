def getWeatherObject(zipCode, apiKey):
    # Gets weather from zip code and uses the open weather api. 

    import json
    import urllib

    zipString = "zip=" + zipCode + ',us'

    keyString = "&appid=" + apiKey

    url = 'http://api.openweathermap.org/data/2.5/weather?' + zipString + keyString

    resp = urllib.request.urlopen(url)
    jsonResponse = json.loads(resp.read())
    print(jsonResponse)
    return jsonResponse

def main():
    parser = argparse.ArgumentParser(description="Determine weather based on zip code.") 
    parser.add_argument('--z', dest='zipcode', required=True) 
    parser.add_argument('--apiKey', dest='apiKey', required=True)

    args = parser.parse_args()
    zipCode = str(args.zipcode)
    apiKey = str(args.apiKey)

    return getWeatherObject(zipCode, apiKey)


if __name__ == '__main__':
    main()