var crypto = require('crypto');

exports.base64ToUrlSafe = function (v) {
    return v.replace(/\//g, '_').replace(/\+/g, '-');
};

exports.urlsafeBase64Encode = function (jsonFlags) {
    var encoded = Buffer.from(jsonFlags).toString('base64');
    return exports.base64ToUrlSafe(encoded);
};

exports.hmacSha1 = function (encodedFlags, secretKey) {
    var hmac = crypto.createHmac('sha1', secretKey);
    hmac.update(encodedFlags);
    return hmac.digest('base64');
};
