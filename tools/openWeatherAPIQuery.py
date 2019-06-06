import json
import urllib

def getWeatherObject(zipCode, apiKey):
    zipString = "zip=" + zipCode + ',us'

    keyString = "&appid=" + apiKey

    url = 'http://api.openweathermap.org/data/2.5/weather?' + zipString + keyString

    resp = urllib.request.urlopen(url)
    jsonResponse = json.loads(resp.read())
    print(jsonResponse)
    return jsonResponse