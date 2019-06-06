import urllib.request
import json

positionalRequests = {
    'latitude': 40.714728,
    'longitude': -73.998672
}
locationUrl = 'locations=' + str(positionalRequests['latitude']) + ',' + str(positionalRequests['longitude'])

key = '-'
keyUrl = '&key=' + key

url = 'https://maps.googleapis.com/maps/api/elevation/json?' + locationUrl + keyUrl

resp = urllib.request.urlopen(url)

print(resp.read())



