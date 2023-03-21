const conf = require('../conf');
const util = require('../util');
const rpc = require('../rpc');
const fs = require('fs');
const getCrc32 = require('crc32');
const path = require('path');
const mime = require('mime');
const Readable = require('stream').Readable;
const formstream = require('formstream');

exports.FormUploader = FormUploader;
exports.PutExtra = PutExtra;

function FormUploader (config) {
    this.config = config || new conf.Config();
}

// 上传可选参数
// @params fname   请求体中的文件的名称
// @params params  额外参数设置，参数名称必须以x:开头
// @param mimeType 指定文件的mimeType
// @param crc32    指定文件的crc32值
// @param checkCrc 指定是否检测文件的crc32值
function PutExtra (fname, params, mimeType, crc32, checkCrc) {
    this.fname = fname || '';
    this.params = params || {};
    this.mimeType = mimeType || null;
    this.crc32 = crc32 || null;
    this.checkCrc = checkCrc || 1;
}

FormUploader.prototype.putStream = function (uploadToken, key, fsStream,
    putExtra, callbackFunc) {
    putExtra = putExtra || new PutExtra();
    if (!putExtra.mimeType) {
        putExtra.mimeType = 'application/octet-stream';
    }

    if (!putExtra.fname) {
        putExtra.fname = key || 'fname';
    }

    fsStream.on('error', function (err) {
    // callbackFunc
        callbackFunc(err, null, null);
    });

    var accessKey = util.getAKFromUptoken(uploadToken);
    var bucket = util.getBucketFromUptoken(uploadToken);

    util.prepareZone(this, accessKey, bucket, function (err, ctx) {
        if (err) {
            callbackFunc(err, null, null);
            return;
        }
        createMultipartForm(uploadToken, key, fsStream, putExtra, function (postForm) {
            putReq(ctx.config, postForm, callbackFunc);
        });
    });
};

function putReq (config, postForm, callbackFunc) {
    // set up hosts order
    var upHosts = [];

    if (config.useCdnDomain) {
        if (config.zone.cdnUpHosts) {
            config.zone.cdnUpHosts.forEach(function (host) {
                upHosts.push(host);
            });
        }
        config.zone.srcUpHosts.forEach(function (host) {
            upHosts.push(host);
        });
    } else {
        config.zone.srcUpHosts.forEach(function (host) {
            upHosts.push(host);
        });
        config.zone.cdnUpHosts.forEach(function (host) {
            upHosts.push(host);
        });
    }

    var scheme = config.useHttpsDomain ? 'https://' : 'http://';
    var upDomain = scheme + upHosts[0];
    rpc.postMultipart(upDomain, postForm, callbackFunc);
}

// 上传字节
//
FormUploader.prototype.put = function (uploadToken, key, body, putExtra,
    callbackFunc) {
    var fsStream = new Readable();
    fsStream.push(body);
    fsStream.push(null);

    putExtra = putExtra || new PutExtra();
    return this.putStream(uploadToken, key, fsStream, putExtra, callbackFunc);
};

FormUploader.prototype.putWithoutKey = function (uploadToken, body, putExtra,
    callbackFunc) {
    return this.put(uploadToken, null, body, putExtra, callbackFunc);
};

function createMultipartForm (uploadToken, key, fsStream, putExtra, callbackFunc) {
    var postForm = formstream();
    postForm.field('token', uploadToken);
    if (key != null) {
        postForm.field('key', key);
    }
    postForm.stream('file', fsStream, putExtra.fname, putExtra.mimeType);

    // putExtra params
    for (var k in putExtra.params) {
        if (k.startsWith('x:')) {
            postForm.field(k, putExtra.params[k].toString());
        }
    }
    var fileBody = [];
    fsStream.on('data', function (data) {
        fileBody.push(data);
    });

    fsStream.on('end', function () {
        fileBody = Buffer.concat(fileBody);
        var bodyCrc32 = parseInt('0x' + getCrc32(fileBody));
        postForm.field('crc32', bodyCrc32);
    });
    callbackFunc(postForm);
}

// 上传本地文件
// @params uploadToken 上传凭证
// @param key 目标文件名
// @param localFile 本地文件路径
// @param putExtra 额外选项
// @param callbackFunc 回调函数
FormUploader.prototype.putFile = function (uploadToken, key, localFile, putExtra,
    callbackFunc) {
    putExtra = putExtra || new PutExtra();
    var fsStream = fs.createReadStream(localFile);

    if (!putExtra.mimeType) {
        putExtra.mimeType = mime.getType(localFile);
    }

    if (!putExtra.fname) {
        putExtra.fname = path.basename(localFile);
    }

    return this.putStream(uploadToken, key, fsStream, putExtra, callbackFunc);
};

FormUploader.prototype.putFileWithoutKey = function (uploadToken, localFile,
    putExtra, callbackFunc) {
    return this.putFile(uploadToken, null, localFile, putExtra, callbackFunc);
};
