var parsePoints = function(accessPoints, apiKey, deviceId) {
    var elementTree = require('elementtree');

    var XML = elementTree.XML;
    var ElementTree = elementTree.ElementTree;
    var element = elementTree.Element;
    var subElement = elementTree.SubElement;

    var locationRQ = element('LocationRQ');
    locationRQ.set('xmlns', "http://skyhookwireless.com/wps/2005");
    locationRQ.set('version', '2.26');
    locationRQ.set('street-address-lookup', 'full');

    var authentication = subElement(locationRQ, 'authentication');
    authentication.set('version', '2.2');

    key = subElement(authentication, 'key');
    key.set('key', apiKey);
    key.set('username', deviceId.toUpperCase());

    var point;
    for (point in accessPoints) {
        var accessPoint = subElement(locationRQ, 'access-point');

        var bssid = subElement(accessPoint, 'mac');
        var fixBssid = accessPoints[point].bssid.replace(/:/g,'');
        bssid.text = fixBssid;

        var quality = subElement(accessPoint, 'signal-strength');
        quality.text = accessPoints[point].quality.toString();
    };

    etree = new ElementTree(locationRQ);
    xml = etree.write({'xml_declaration': false});
    //console.log("XML String: " + xml)
    console.log(5)
    console.log(xml)
    return xml;
};

module.exports = {
    parsePoints: parsePoints,
};