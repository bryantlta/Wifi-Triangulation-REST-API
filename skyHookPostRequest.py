# Precision location POST request from skyhook REST api. 
        
def skyHookRequest():
    from tools import readArgs
    from tools import postRequests
    
    api_location_endPoint = 'https://global.skyhookwireless.com/wps2/location'
    xml_string = readArgs.readArgs()

    postRequest = postRequests.postRequestXML(api_location_endPoint, xml_string)
    return postRequest 