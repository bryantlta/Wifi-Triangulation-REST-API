# Sends a post request using either xml or json. 

def postRequestXML(location_api_endPoint, xml_string):
    import requests

    header = {'Content-Type': 'text/xml'}

    postRequest = requests.post(location_api_endPoint, data = xml_string, headers = header)

