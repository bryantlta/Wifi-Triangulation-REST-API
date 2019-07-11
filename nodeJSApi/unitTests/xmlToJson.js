var xmlToJson = function(xmlString) {
    var xml2js = require('xml2js');

    var bodyParser = require('body-parser');
    var urlencodedParser = bodyParser.urlencoded({extended: false});
    var parser = new xml2js.Parser();

    parser.parseString(xmlString, function(error, result){
        //console.dir(result);
        //console.log('Done');
        //console.log(result)
        return JSON.stringify(result);
    });
};

module.exports = {
    xmltoJson: xmltoJson,
}