var conf = require('../conf');

exports.Mac = Mac;

function Mac (accessKey, secretKey) {
    this.accessKey = accessKey || conf.ACCESS_KEY;
    this.secretKey = secretKey || conf.SECRET_KEY;
}
