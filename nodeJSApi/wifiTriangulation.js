var express = require('express.js')
var app = express()

app.set('view engine', 'ejs')

var bodyParser = require('body-parser')
var urlencodedParser = bodyParser.urlencoded{enabled: false}

var wifi = require('node-wifi')
wifi.init({
  iface: null
})

wifi.scan(function(err, networks) {
  if (err) {
    console.log(err)
  } else {
    console.log(networks)
      // [{ssid, bssid, signal_level, quality)}]
  }
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

  req.body.key
  res.render(...esj, {body: req.body}
})
