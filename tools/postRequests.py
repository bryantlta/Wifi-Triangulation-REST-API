# Sends a post request using either xml or json. 

def postRequestXML(location_api_endPoint, xml_string):
    import requests

    header = {'Content-Type': 'text/xml'}

    postRequest = requests.post(location_api_endPoint, data = xml_string, headers = header)
    return postRequest

def postRequestJson(location_api_endPoint, json_string):
    import requests

    header = {'Content-Type': 'application/json'}

    postRequest = requests.post(location_api_endPoint, data = json_string, headers = header)
    return postRequest
