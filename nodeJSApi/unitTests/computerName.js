var findComputerName = function() {
    // https://stackoverflow.com/questions/42151493/how-to-get-client-computer-name-in-node-js
    var os = require("os");
    var hostaddress = os.hostname();
    console.log("Hostname: " + hostaddress);
    return hostaddress;
};

findComputerName()

module.exports = {
    findComputerName: findComputerName,
};