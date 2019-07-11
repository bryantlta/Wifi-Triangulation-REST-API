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
                console.log(body)
                return body
            }
            console.log('error:', error); // Print the error if one occurred
            console.log('statusCode:', response && response.statusCode); // Print the response status code if a response was received
            console.log('body:', body); // Print the HTML for the Google homepage.
        }
    );
};


//Unit Tests
console.log(skyHookRequest(endPoint, requestString))

module.exports = {
    skyHookRequest: skyHookRequest,
};


