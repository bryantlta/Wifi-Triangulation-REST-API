import xmlToDict
import pprint
import json

my_xml = """
    <audience>
      <id what="attribute">123</id>
      <name>Shubham</name>
    </audience>
"""

o = xmlToDict.parse(my_xml)
x = json.dumps(o)
print(x)
