# Request with Header Data to send User-Agent header
import urllib.request
import json
import argparse

url = 'https://icanhazdadjoke.com/'

headers = {
   'User-Agent': '',
   'Accept': 'application/json'
}

body = {
    'id': "R7UfaahVfFd",
}

if 'id' in body:
    url = url + 'j/' + body['id']

#Create Request Object
request = urllib.request.Request(url, headers=headers)

#Opens the URL and get Response
resp = urllib.request.urlopen(request)

#Reads the URL Reponse.
joke = json.loads(resp.read())

# Get value from 'joke' key. 
print(resp.read()) 

