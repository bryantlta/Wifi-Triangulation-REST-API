import urllib.request
import json

positionalRequests = {
    'latitude': 40.714728,
    'longitude': -73.998672
}
locationUrl = 'locations=' + str(positionalRequests['latitude']) + ',' + str(positionalRequests['longitude'])

key = 'AIzaSyAE2pV0X5HZfrdz8HciK6kQN-SiDP3eHoE'
keyUrl = '&key=' + key

url = 'https://maps.googleapis.com/maps/api/elevation/json?' + locationUrl + keyUrl

resp = urllib.request.urlopen(url)

print(resp.read())



