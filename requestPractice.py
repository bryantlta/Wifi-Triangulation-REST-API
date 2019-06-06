import urllib.request
import json
import argparse
from tools import openWeatherAPIQuery
from tools import skyHookApiIpQuery

def main():
    parser = argparse.ArgumentParser(description="Determine weather based on zip code.") 
    parser.add_argument('--z', dest='zipcode', required=True) 
    parser.add_argument('--apiKey', dest='apiKey', required=True)

    args = parser.parse_args()
    zipCode = str(args.zipcode)
    apiKey = str(args.apiKey)

    return openWeatherAPIQuery.getWeatherObject(zipCode, apiKey)

if __name__ == '__main__': 
    main() 
        


