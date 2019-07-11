var getHash = function(name) {
    //https://nodejs.org/api/crypto.html#crypto_crypto
    if (name === undefined){
        var name = "";
    } else {
        const crypto = require('crypto');
        const hash = crypto.createHmac('sha256', name)
                        .digest('hex');
        console.log("Hash  " + hash);
        return hash;
    }
};

/* Unit Tests */
getHash('alsijr32ijf90u0waejf');
getHash('1209347104710');
getHash('asfjlasjefisj');
getHash('-#%$(&#$');
getHash();

module.exports = {
    getHash: getHash
};