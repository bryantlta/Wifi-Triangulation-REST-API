# Wifi-Triangulation-REST-API
Built a Node.js and a Python (2.7, 3.6) REST Api request script for determining current location based on nearby access points (w/ all dependencies having been removed.) 

## Getting Started
1) This program runs without any dependencies for Python. Dependencies have no been removed for Node.js, so you will 
  need to npm install request, elementtree, xml2js. 
2) Obtain a Skyhook API key by setting up a project: https://resources.skyhookwireless.com/wiki/type/documentation/precision-location/
3) To run these files, go to the directory where the program is and either run:
    py wifiTriangulationComplete.py {skyhook API Key}
    
    node wifiTriangulation.js {skyhook API Key}
