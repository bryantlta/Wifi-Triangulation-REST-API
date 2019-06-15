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

var fs = require('fs')
var xml2js = require('xml2js')

var getJson = function(html){
  var parser = new xml2js.Parse();

  fs.readFile(__dirname + html, function(err, data) {
    parser.parseString(data, function (err, result) {
      console.dir(result);
      console.log('Done');
      return JSON.stringify(result)
    })
  })
}

var json = getJson('index.html')

root = element('entry')
root.set('xmlns', 'http://www.w3.org/2005/Atom...')

tenantId = subElement(root, 'TenantId');
tenantId.text = '12345';

etree = new ElementTree(root)
xml = etree.write({'xml_declaration': false});
console.log(xml);

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

  req.body.key
  res.render(...esj, {body: req.body}
})
