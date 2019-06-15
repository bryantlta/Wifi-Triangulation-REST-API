var express = require('express.js')
var app = express()

app.set('view engine', 'ejs')

var bodyParser = require('body-parser')
var urlencodedParser = bodyParser.urlencoded{enabled: false}

var getAccessPoints = function(){
  //Import NPM node-wifi.
  var wifi = require('node-wifi')

  // Initialize the wifi object.
  wifi.init({
    iface: null
  })

  // Access Points PROMISE.
  wifi.scan().then(function (networks) {
    return networks
  }).catch(function (error) {
    console.log(error)
  })
}

var findComputerName = function() {
  var os = require('os')
  var hostaddress = os.hostname()
  console.log("Hostname: " + hostaddress)
  return hostaddress
}

var getHash = function(name) {
  var cryto = require('crypto');
  var hash = crypto.createHmac('sha256', name)
                  .digest('hex');
  console.log("Hash " + hash);
  return hash 
}

var xml2js = require('xml2js')

var getJson = function(xmlString){
  var parser = new xml2js.Parse();

    parser.parseString(xmlString, function (err, result) {
      console.dir(result);
      console.log('Done');
      return JSON.stringify(result)
    })
  })
}

var json = getJson('index.html')

var parsePoints = function() {
  var locationRQ = element('LocationRQ')
  locationRQ.set('xmlns', "http://skyhookwireless.com/wps/2005")
  locationRQ.set('version', "2.26")
  locationRQ.set('street-address-lookup', "full")

  var authentication = subElement(locationRQ, 'authentication')
  authentication.set('version', '2.2')

  key = subElement(authentication, 'key')
  key.set('key', apiKey)
  key.set('username', deviceId)

  var point;
  for (point in accessPoints) {
    var accessPoint = subElement(locationRQ, 'access-point')

    var bssid = subElement(accessPoint, 'mac')
    bssid.text = str(point.bssid).replace(':', '') //Check syntax

    var quality = ubElement(accessPoint, 'signal-strength')
    quality.text = str(point.quality)
  }

  etree = new ElementTree(locationRQ)
  xml = etree.write({'xml_declaration': false});
  console.log(xml);
}

// PROJECT IDEA. We can try connecting to networks programmatically
// Brute force guess passwords. Outputs the password that works!

app.get('/', function(req, res){
  res.sendFile(__dirname + 'index.html')
}

app.post('/key',  urlencodedParser, function(req, res){
  // Get access points.
  //  all of the access point names and qualities.
  // Grab computer name and encode it.
  // Turn access points to XML string.
  // POST request to Skyhook
  // XML response to JSON
  // POST RESPONSE the JSON and display important information.
  points = getAccessPoints();


  req.body.key
  res.render(...esj, {body: req.body}
})
