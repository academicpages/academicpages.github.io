const conf = require('../conf');
const util = require('../util');
const rpc = require('../rpc');
const path = require('path');
const mime = require('mime');
const fs = require('fs');
const getCrc32 = require('crc32');
const destroy = require('destroy');
const BlockStream = require('block-stream2');

exports.ResumeUploader = ResumeUploader;
exports.PutExtra = PutExtra;

function ResumeUploader (config) {
    this.config = config || new conf.Config();
}

// 上传可选参数
// @params fname                      请求体中的文件的名称
// @params params                     额外参数设置，参数名称必须以x:开头
// @param mimeType                    指定文件的mimeType
// @param resumeRecordFile            断点续传的已上传的部分信息记录文件
// @param progressCallback(uploadBytes, totalBytes) 上传进度回调
function PutExtra (fname, params, mimeType, resumeRecordFile, progressCallback) {
    this.fname = fname || '';
    this.params = params || {};
    this.mimeType = mimeType || null;
    this.resumeRecordFile = resumeRecordFile || null;
    this.progressCallback = progressCallback || null;
}

ResumeUploader.prototype.putStream = function (uploadToken, key, rsStream,
    rsStreamLen, putExtra, callbackFunc) {
    putExtra = putExtra || new PutExtra();
    if (!putExtra.mimeType) {
        putExtra.mimeType = 'application/octet-stream';
    }

    if (!putExtra.fname) {
        putExtra.fname = key || '?';
    }

    rsStream.on('error', function (err) {
    // callbackFunc
        callbackFunc(err, null, null);
        destroy(rsStream);
    });

    var accessKey = util.getAKFromUptoken(uploadToken);
    var bucket = util.getBucketFromUptoken(uploadToken);

    util.prepareZone(this, accessKey, bucket, function (err, ctx) {
        if (err) {
            callbackFunc(err, null, null);
            destroy(rsStream);
            return;
        }
        putReq(ctx.config, uploadToken, key, rsStream, rsStreamLen, putExtra,
            callbackFunc);
    });
};

function putReq (config, uploadToken, key, rsStream, rsStreamLen, putExtra,
    callbackFunc) {
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
    // block upload

    var blkStream = rsStream.pipe(new BlockStream({
        size: conf.BLOCK_SIZE,
        zeroPadding: false
    }));

    var readLen = 0;
    var curBlock = 0;
    var finishedBlock = 0;
    var finishedCtxList = [];
    var finishedBlkPutRets = [];
    var isSent = false;
    var totalBlockNum = Math.ceil(rsStreamLen / conf.BLOCK_SIZE);
    // read resumeRecordFile
    if (putExtra.resumeRecordFile) {
        try {
            var resumeRecords = fs.readFileSync(putExtra.resumeRecordFile).toString();
            var blkputRets = JSON.parse(resumeRecords);

            for (var index = 0; index < blkputRets.length; index++) {
                // check ctx expired or not
                var blkputRet = blkputRets[index];
                var expiredAt = blkputRet.expired_at;
                // make sure the ctx at least has one day expiration
                expiredAt += 3600 * 24;
                if (util.isTimestampExpired(expiredAt)) {
                    // discard these ctxs
                    break;
                }

                finishedBlock += 1;
                finishedCtxList.push(blkputRet.ctx);
                finishedBlkPutRets.push(blkputRet);
            }
        } catch (e) {
            // log(e);
        }
    }

    // check when to mkblk
    blkStream.on('data', function (chunk) {
        readLen += chunk.length;
        curBlock += 1; // set current block
        if (curBlock > finishedBlock) {
            blkStream.pause();
            mkblkReq(upDomain, uploadToken, chunk, function (respErr,
                respBody,
                respInfo) {
                var bodyCrc32 = parseInt('0x' + getCrc32(chunk));
                if (respInfo.statusCode != 200 || respBody.crc32 != bodyCrc32) {
                    callbackFunc(respErr, respBody, respInfo);
                    destroy(rsStream);
                } else {
                    finishedBlock += 1;
                    var blkputRet = respBody;
                    finishedCtxList.push(blkputRet.ctx);
                    finishedBlkPutRets.push(blkputRet);
                    if (putExtra.progressCallback) {
                        putExtra.progressCallback(readLen, rsStreamLen);
                    }
                    if (putExtra.resumeRecordFile) {
                        var contents = JSON.stringify(finishedBlkPutRets);
                        // console.log('write resume record ' + putExtra.resumeRecordFile);
                        fs.writeFileSync(putExtra.resumeRecordFile, contents, {
                            encoding: 'utf-8'
                        });
                    }
                    blkStream.resume();
                    if (finishedCtxList.length === totalBlockNum) {
                        mkfileReq(upDomain, uploadToken, rsStreamLen, finishedCtxList, key, putExtra, callbackFunc);
                        isSent = true;
                    }
                }
            });
        }
    });

    blkStream.on('end', function () {
        if (!isSent && rsStreamLen === 0) {
            mkfileReq(upDomain, uploadToken, rsStreamLen, finishedCtxList, key, putExtra, callbackFunc);
        }
        destroy(rsStream);
    });
}

function mkblkReq (upDomain, uploadToken, blkData, callbackFunc) {
    // console.log("mkblk");
    var requestURI = upDomain + '/mkblk/' + blkData.length;
    var auth = 'UpToken ' + uploadToken;
    var headers = {
        Authorization: auth,
        'Content-Type': 'application/octet-stream'
    };
    rpc.post(requestURI, blkData, headers, callbackFunc);
}

function mkfileReq (upDomain, uploadToken, fileSize, ctxList, key, putExtra,
    callbackFunc) {
    // console.log("mkfile");
    var requestURI = upDomain + '/mkfile/' + fileSize;
    if (key) {
        requestURI += '/key/' + util.urlsafeBase64Encode(key);
    }
    if (putExtra.mimeType) {
        requestURI += '/mimeType/' + util.urlsafeBase64Encode(putExtra.mimeType);
    }
    if (putExtra.fname) {
        requestURI += '/fname/' + util.urlsafeBase64Encode(putExtra.fname);
    }
    if (putExtra.params) {
    // putExtra params
        for (var k in putExtra.params) {
            if (k.startsWith('x:') && putExtra.params[k]) {
                requestURI += '/' + k + '/' + util.urlsafeBase64Encode(putExtra.params[
                    k].toString());
            }
        }
    }
    var auth = 'UpToken ' + uploadToken;
    var headers = {
        Authorization: auth,
        'Content-Type': 'application/octet-stream'
    };
    var postBody = ctxList.join(',');
    rpc.post(requestURI, postBody, headers, function (err, ret, info) {
        if (info.statusCode == 200 || info.statusCode == 701 ||
      info.statusCode == 401) {
            if (putExtra.resumeRecordFile) {
                fs.unlinkSync(putExtra.resumeRecordFile);
            }
        }
        callbackFunc(err, ret, info);
    });
}

ResumeUploader.prototype.putFile = function (uploadToken, key, localFile,
    putExtra, callbackFunc) {
    putExtra = putExtra || new PutExtra();
    var rsStream = fs.createReadStream(localFile, {
        highWaterMark: conf.BLOCK_SIZE
    });
    var rsStreamLen = fs.statSync(localFile).size;
    if (!putExtra.mimeType) {
        putExtra.mimeType = mime.getType(localFile);
    }

    if (!putExtra.fname) {
        putExtra.fname = path.basename(localFile);
    }

    return this.putStream(uploadToken, key, rsStream, rsStreamLen, putExtra,
        callbackFunc);
};

ResumeUploader.prototype.putFileWithoutKey = function (uploadToken, localFile,
    putExtra, callbackFunc) {
    return this.putFile(uploadToken, null, localFile, putExtra, callbackFunc);
};
