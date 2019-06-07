# Why we import http.client instead of httplib:
    # https://stackoverflow.com/questions/13778252/import-httplib-importerror-no-module-named-httplib.

#https://www.forceflow.be/2011/05/12/http-xml-post-using-python/

import sys
import http.client as httplib 

HOST = 'http://skyhookwireless.com'
API_URL = '/wps/2005'

def do_request(xml_location):
	"""HTTP XML Post request, by www.forceflow.be"""
	request = open(xml_location,"r").read()
	webservice = httplib.HTTP(HOST)
	webservice.putrequest("POST", API_URL)
	webservice.putheader("Host", HOST)
	webservice.putheader("User-Agent","Python post")
	webservice.putheader("Content-type", "text/xml; charset=\"UTF-8\"")
	webservice.putheader("Content-length", "%d" % len(request))
	webservice.endheaders()
	webservice.send(request)
	statuscode, statusmessage, header = webservice.getreply()
	result = webservice.getfile().read()
        print(statuscode, statusmessage, header)
        print(result)

do_request("precisionlocation.xml")