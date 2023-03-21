const urllib = require('urllib');
const util = require('util');
const conf = require('./conf');

// huadong
exports.Zone_z0 = new conf.Zone([
    'up.qiniup.com',
    'up-nb.qiniup.com',
    'up-xs.qiniup.com'
], [
    'upload.qiniup.com',
    'upload-nb.qiniup.com',
    'upload-xs.qiniup.com'
], 'iovip.qbox.me',
'rs.qbox.me',
'rsf.qbox.me',
'api.qiniu.com');

// huabei
exports.Zone_z1 = new conf.Zone([
    'up-z1.qiniup.com'
], [
    'upload-z1.qiniup.com'
], 'iovip-z1.qbox.me',
'rs-z1.qbox.me',
'rsf-z1.qbox.me',
'api-z1.qiniu.com');

// huanan
exports.Zone_z2 = new conf.Zone([
    'up-z2.qiniup.com',
    'up-gz.qiniup.com',
    'up-fs.qiniup.com'
], [
    'upload-z2.qiniup.com',
    'upload-gz.qiniup.com',
    'upload-fs.qiniup.com'
], 'iovip-z2.qbox.me',
'rs-z2.qbox.me',
'rsf-z2.qbox.me',
'api-z2.qiniu.com');

// beimei
exports.Zone_na0 = new conf.Zone([
    'up-na0.qiniup.com'
], [
    'upload-na0.qiniup.com'
], 'iovip-na0.qbox.me',
'rs-na0.qbox.me',
'rsf-na0.qbox.me',
'api-na0.qiniu.com');

exports.Zone_as0 = new conf.Zone([
    'up-as0.qiniup.com'
], [
    'upload-as0.qiniup.com'
], 'iovip-as0.qbox.me',
'rs-as0.qbox.me',
'rsf-as0.qbox.me',
'api-as0.qiniu.com');

exports.getZoneInfo = function (accessKey, bucket, callbackFunc) {
    var apiAddr = util.format('https://uc.qbox.me/v2/query?ak=%s&bucket=%s',
        accessKey, bucket);
    urllib.request(apiAddr, function (respErr, respData, respInfo) {
        if (respErr) {
            callbackFunc(respErr, null, null);
            return;
        }

        if (respInfo.statusCode != 200) {
            // not ok
            respErr = new Error(respInfo.statusCode + '\n' + respData);
            callbackFunc(respErr, null, null);
            return;
        }

        var zoneData = JSON.parse(respData);
        var srcUpHosts = [];
        var cdnUpHosts = [];
        var zoneExpire = 0;

        try {
            zoneExpire = zoneData.ttl;
            // read src hosts
            zoneData.up.src.main.forEach(function (host) {
                srcUpHosts.push(host);
            });
            if (zoneData.up.src.backup) {
                zoneData.up.src.backup.forEach(function (host) {
                    srcUpHosts.push(host);
                });
            }

            // read acc hosts
            zoneData.up.acc.main.forEach(function (host) {
                cdnUpHosts.push(host);
            });
            if (zoneData.up.acc.backup) {
                zoneData.up.acc.backup.forEach(function (host) {
                    cdnUpHosts.push(host);
                });
            }

            var ioHost = zoneData.io.src.main[0];
            var zoneInfo = new conf.Zone(srcUpHosts, cdnUpHosts, ioHost);
            callbackFunc(null, zoneInfo, zoneExpire);
        } catch (e) {
            callbackFunc(e, null, null);
        }
    });
};
