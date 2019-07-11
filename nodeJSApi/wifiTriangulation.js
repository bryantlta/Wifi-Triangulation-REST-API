var main = function() {
    return checkConnection();
};

var checkConnection = function(){
    var request = require('request');
    return request('http://www.google.com', function (error, response, body) {
        if (error) {
            return false;
        } else {
            return getAccessPoints();
        };
    });
};

var getAccessPoints = function(){
        var wifi = require('node_modules/node-wifi');

        wifi.init({
            iface: null,
        });

        return wifi.scan(function(err, networks) {
            if (err) {
                console.log(err);
            } else {
                return findComputerName(networks);
            }
        });
};

var findComputerName = function(networks) {
    // https://stackoverflow.com/questions/42151493/how-to-get-client-computer-name-in-node-js
    var os = require("os");
    var hostaddress = os.hostname();
    return getHash(networks, hostaddress);
};

var getHash = function(networks, name) {
    //https://nodejs.org/api/crypto.html#crypto_crypto
    if (name === undefined){
        var name = "";
    } else {
        const crypto = require('crypto');
        const hash = crypto.createHmac('sha256', name)
                        .digest('hex');
        return getKey(networks, hash);
    }
};

var getKey = function(networks, hash) {
    if (process.argv.length < 3) {
        return null;
    } else {
        return parsePoints(networks, process.argv[2], hash);
    };
};

// npm elementtree
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
    return skyHookRequest('https://global.skyhookwireless.com/wps2/location', xml.toString());
};

var skyHookRequest = function(location_api_endPoint, xmlString){
    var request = require('request');

    //https://stackoverflow.com/questions/19059997/node-js-request-library-post-text-xml-to-body
    return request.post(
        {url: location_api_endPoint,
        body : xmlString,
        headers: {'Content-Type': 'text/xml'}
        },
        function (error, response, body) {        
            if (!error && response.statusCode == 200) {
                return xmlToJson(body);
            } else {
                console.log('error:', error); // Print the error if one occurred
                console.log('statusCode:', response && response.statusCode); // Print the response status code if a response was received
                console.log('body:', body); // Print the HTML for the Google homepage.
            }
        }
    );
};

var xmlToJson = function(xmlString) {
    var xml2js = require('xml2js');

    var parser = new xml2js.Parser();

    return parser.parseString(xmlString, function(error, result){
        var final = JSON.stringify(result);
        console.log(final)
        return final
    });
};

main();