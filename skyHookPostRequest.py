# Precision location POST request from skyhook REST api. 

# Skyhook request requies that bssids do NOT have colons. 
# Signal strength and quality mean the same thing and negative signs do not matter. 
        
def skyHookRequest():
    from tools import readArgs
    from tools import postRequests
    
    api_location_endPoint = 'https://global.skyhookwireless.com/wps2/location'
    xml_string = readArgs.readArgs(1)

    postRequest = postRequests.postRequestXML(api_location_endPoint, xml_string)
    print(postRequest.text)
    return postRequest

def main():
    return skyHookRequest()

if __name__ == '__main__':
    main()   