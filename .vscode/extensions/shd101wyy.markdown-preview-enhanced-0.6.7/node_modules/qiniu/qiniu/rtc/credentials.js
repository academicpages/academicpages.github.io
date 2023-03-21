var util = require('./util');

function Credentials (accessKey, secretKey) {
    this.accessKey = accessKey;
    this.secretKey = secretKey;
}

Credentials.prototype.generateAccessToken = function (options, data) {
    var sign = this._signRequest(options, data);
    var token = 'Qiniu' + ' ' + this.accessKey + ':' + sign;

    return token;
};

Credentials.prototype._signRequest = function (options, body) {
    var contentType = options.headers['Content-Type'];

    var host = options.host;
    if (options.port && options.port != 80) {
        host = host + ':' + options.port;
    }

    var data = options.method + ' ' + options.path;
    data += '\nHost: ' + host;
    if (contentType) {
        data += '\nContent-Type: ' + contentType;
    }
    data += '\n\n';

    if (body && contentType && contentType != 'application/octet-stream') {
        data += body;
    }

    var digest = util.hmacSha1(data, this.secretKey);

    var sageDigest = util.base64ToUrlSafe(digest);

    return sageDigest;
};

Credentials.prototype.sign = function (data) {
    var digest = util.hmacSha1(data, this.secretKey);
    var sageDigest = util.base64ToUrlSafe(digest);
    return this.accessKey + ':' + sageDigest;
};

Credentials.prototype.signJson = function (opt) {
    var str = JSON.stringify(opt);
    var encodedStr = util.urlsafeBase64Encode(str);
    var sign = util.hmacSha1(encodedStr, this.secretKey);
    var encodedSign = util.base64ToUrlSafe(sign);

    var token = this.accessKey + ':' + encodedSign + ':' + encodedStr;
    return token;
};

module.exports = exports = Credentials;
