#https://stackoverflow.com/questions/191536/converting-xml-to-json-using-python
from xml.etree import ElementTree as ET

xml = ET.parse('FILE_NAME.xml')
parsed = parseXmlToJson(xml)

def parseXmlToJson(xml):
    response = {}

    for child in list(xml):
        if len(list(child)) > 0:
            response[child.tag] = parseXmlToJson(child)
        else:
            response[child.tag] = child.text or ''

    return response