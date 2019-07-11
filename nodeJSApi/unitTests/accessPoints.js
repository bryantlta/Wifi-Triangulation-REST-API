var checkConnection = function(){
    console.log(1)
    var request = require('request');
    var result = request('http://www.google.com', function (error, response, body) {
        console.log(2)
        if (error) {
            return false;
        } else {
            return getAccessPoints();
        }
    });
    return result;
};

var getAccessPoints = function(){
    console.log(3)
        var wifi = require('node-wifi');

        // initialize the wifi object
        wifi.init({
            iface: null,
        });

        //access points PROMISE
        wifi.scan(function(err, networks) {
            if (err) {
                console.log(err);
            } else {
                console.log(4)
                //console.log(networks);
                return networks;
            }
        });
};

/* Unit Tests */
checkConnection();

module.exports = {
    checkConnection: checkConnection,
    getAccessPoints: getAccessPoints,
}