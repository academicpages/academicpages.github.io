const querystring = require('querystring');
const encodeUrl = require('encodeurl');
const rpc = require('../rpc');
const conf = require('../conf');
const digest = require('../auth/digest');
const util = require('../util');

exports.BucketManager = BucketManager;
exports.PutPolicy = PutPolicy;

function BucketManager (mac, config) {
    this.mac = mac || new digest.Mac();
    this.config = config || new conf.Config();
}

// 获取资源信息
// @link https://developer.qiniu.com/kodo/api/1308/stat
// @param bucket 空间名称
// @param key    文件名称
// @param callbackFunc(err, respBody, respInfo) 回调函数
BucketManager.prototype.stat = function (bucket, key, callbackFunc) {
    util.prepareZone(this, this.mac.accessKey, bucket, function (err, ctx) {
        if (err) {
            callbackFunc(err, null, null);
            return;
        }
        statReq(ctx.mac, ctx.config, bucket, key, callbackFunc);
    });
};

function statReq (mac, config, bucket, key, callbackFunc) {
    var scheme = config.useHttpsDomain ? 'https://' : 'http://';
    var statOp = exports.statOp(bucket, key);
    var requestURI = scheme + config.zone.rsHost + statOp;
    var digest = util.generateAccessToken(mac, requestURI, null);
    rpc.postWithoutForm(requestURI, digest, callbackFunc);
}

//  修改文件的类型
// @link https://developer.qiniu.com/kodo/api/1252/chgm
// @param bucket  空间名称
// @param key     文件名称
// @param newMime 新文件类型
// @param callbackFunc(err, respBody, respInfo) 回调函数
BucketManager.prototype.changeMime = function (bucket, key, newMime,
    callbackFunc) {
    util.prepareZone(this, this.mac.accessKey, bucket, function (err, ctx) {
        if (err) {
            callbackFunc(err, null, null);
            return;
        }
        changeMimeReq(ctx.mac, ctx.config, bucket, key, newMime, callbackFunc);
    });
};

function changeMimeReq (mac, config, bucket, key, newMime, callbackFunc) {
    var scheme = config.useHttpsDomain ? 'https://' : 'http://';
    var changeMimeOp = exports.changeMimeOp(bucket, key, newMime);
    var requestURI = scheme + config.zone.rsHost + changeMimeOp;
    var digest = util.generateAccessToken(mac, requestURI, null);
    rpc.postWithoutForm(requestURI, digest, callbackFunc);
}

// 修改文件返回的Headers内容
// @link TODO
// @param bucket  空间名称
// @param key     文件名称
// @param headers 需要修改的headers
// @param callbackFunc(err, respBody, respInfo) 回调函数
BucketManager.prototype.changeHeaders = function (bucket, key, headers,
    callbackFunc) {
    util.prepareZone(this, this.mac.accessKey, bucket, function (err, ctx) {
        if (err) {
            callbackFunc(err, null, null);
            return;
        }
        changeHeadersReq(ctx.mac, ctx.config, bucket, key, headers, callbackFunc);
    });
};

function changeHeadersReq (mac, config, bucket, key, headers, callbackFunc) {
    var scheme = config.useHttpsDomain ? 'https://' : 'http://';
    var changeHeadersOp = exports.changeHeadersOp(bucket, key, headers);
    var requestURI = scheme + config.zone.rsHost + changeHeadersOp;
    var digest = util.generateAccessToken(mac, requestURI, null);
    rpc.postWithoutForm(requestURI, digest, callbackFunc);
}

// 移动或重命名文件，当bucketSrc==bucketDest相同的时候，就是重命名文件操作
// @link https://developer.qiniu.com/kodo/api/1257/delete
// @param srcBucket  源空间名称
// @param srcKey     源文件名称
// @param destBucket 目标空间名称
// @param destKey    目标文件名称
// @param options    可选参数
//                   force 强制覆盖
// @param callbackFunc(err, respBody, respInfo) 回调函数
BucketManager.prototype.move = function (srcBucket, srcKey, destBucket, destKey,
    options, callbackFunc) {
    util.prepareZone(this, this.mac.accessKey, srcBucket, function (err, ctx) {
        if (err) {
            callbackFunc(err, null, null);
            return;
        }
        moveReq(ctx.mac, ctx.config, srcBucket, srcKey, destBucket, destKey,
            options, callbackFunc);
    });
};

function moveReq (mac, config, srcBucket, srcKey, destBucket, destKey,
    options, callbackFunc) {
    var scheme = config.useHttpsDomain ? 'https://' : 'http://';
    var moveOp = exports.moveOp(srcBucket, srcKey, destBucket, destKey, options);
    var requestURI = scheme + config.zone.rsHost + moveOp;
    var digest = util.generateAccessToken(mac, requestURI, null);
    rpc.postWithoutForm(requestURI, digest, callbackFunc);
}

// 复制一个文件
// @link https://developer.qiniu.com/kodo/api/1254/copy
// @param srcBucket  源空间名称
// @param srcKey     源文件名称
// @param destBucket 目标空间名称
// @param destKey    目标文件名称
// @param options    可选参数
//                   force 强制覆盖
// @param callbackFunc(err, respBody, respInfo) 回调函数
BucketManager.prototype.copy = function (srcBucket, srcKey, destBucket, destKey,
    options, callbackFunc) {
    util.prepareZone(this, this.mac.accessKey, srcBucket, function (err, ctx) {
        if (err) {
            callbackFunc(err, null, null);
            return;
        }
        copyReq(ctx.mac, ctx.config, srcBucket, srcKey, destBucket, destKey,
            options, callbackFunc);
    });
};

function copyReq (mac, config, srcBucket, srcKey, destBucket, destKey,
    options, callbackFunc) {
    options = options || {};
    var scheme = config.useHttpsDomain ? 'https://' : 'http://';
    var copyOp = exports.copyOp(srcBucket, srcKey, destBucket, destKey, options);
    var requestURI = scheme + config.zone.rsHost + copyOp;
    var digest = util.generateAccessToken(mac, requestURI, null);
    rpc.postWithoutForm(requestURI, digest, callbackFunc);
}

// 删除资源
// @link https://developer.qiniu.com/kodo/api/1257/delete
// @param bucket 空间名称
// @param key    文件名称
// @param callbackFunc(err, respBody, respInfo) 回调函数
BucketManager.prototype.delete = function (bucket, key, callbackFunc) {
    util.prepareZone(this, this.mac.accessKey, bucket, function (err, ctx) {
        if (err) {
            callbackFunc(err, null, null);
            return;
        }
        deleteReq(ctx.mac, ctx.config, bucket, key, callbackFunc);
    });
};

function deleteReq (mac, config, bucket, key, callbackFunc) {
    var scheme = config.useHttpsDomain ? 'https://' : 'http://';
    var deleteOp = exports.deleteOp(bucket, key);
    var requestURI = scheme + config.zone.rsHost + deleteOp;
    var digest = util.generateAccessToken(mac, requestURI, null);
    rpc.postWithoutForm(requestURI, digest, callbackFunc);
}

// 更新文件的生命周期
// @link https://developer.qiniu.com/kodo/api/1732/update-file-lifecycle
// @param bucket 空间名称
// @param key    文件名称
// @param days   有效期天数
// @param callbackFunc(err, respBody, respInfo) 回调函数
BucketManager.prototype.deleteAfterDays = function (bucket, key, days,
    callbackFunc) {
    util.prepareZone(this, this.mac.accessKey, bucket, function (err, ctx) {
        if (err) {
            callbackFunc(err, null, null);
            return;
        }
        deleteAfterDaysReq(ctx.mac, ctx.config, bucket, key, days, callbackFunc);
    });
};

function deleteAfterDaysReq (mac, config, bucket, key, days, callbackFunc) {
    var scheme = config.useHttpsDomain ? 'https://' : 'http://';
    var deleteAfterDaysOp = exports.deleteAfterDaysOp(bucket, key, days);
    var requestURI = scheme + config.zone.rsHost + deleteAfterDaysOp;
    var digest = util.generateAccessToken(mac, requestURI, null);
    rpc.postWithoutForm(requestURI, digest, callbackFunc);
}

// 抓取资源
// @link https://developer.qiniu.com/kodo/api/1263/fetch
// @param resUrl 资源链接
// @param bucket 空间名称
// @param key    文件名称
// @param callbackFunc(err, respBody, respInfo) 回调函数
BucketManager.prototype.fetch = function (resUrl, bucket, key, callbackFunc) {
    util.prepareZone(this, this.mac.accessKey, bucket, function (err, ctx) {
        if (err) {
            callbackFunc(err, null, null);
            return;
        }
        fetchReq(ctx.mac, ctx.config, resUrl, bucket, key, callbackFunc);
    });
};

function fetchReq (mac, config, resUrl, bucket, key, callbackFunc) {
    var scheme = config.useHttpsDomain ? 'https://' : 'http://';
    var encodedEntryURI = util.encodedEntry(bucket, key);
    var encodedResURL = util.urlsafeBase64Encode(resUrl);
    var requestURI = scheme + config.zone.ioHost + '/fetch/' + encodedResURL +
        '/to/' + encodedEntryURI;
    var digest = util.generateAccessToken(mac, requestURI, null);
    rpc.postWithoutForm(requestURI, digest, callbackFunc);
}

// 更新镜像副本
// @link https://developer.qiniu.com/kodo/api/1293/prefetch
// @param bucket 空间名称
// @param key    文件名称
// @param callbackFunc(err, respBody, respInfo) 回调函数
BucketManager.prototype.prefetch = function (bucket, key, callbackFunc) {
    util.prepareZone(this, this.mac.accessKey, bucket, function (err, ctx) {
        if (err) {
            callbackFunc(err, null, null);
            return;
        }
        prefetchReq(ctx.mac, ctx.config, bucket, key, callbackFunc);
    });
};

function prefetchReq (mac, config, bucket, key, callbackFunc) {
    var scheme = config.useHttpsDomain ? 'https://' : 'http://';
    var encodedEntryURI = util.encodedEntry(bucket, key);
    var requestURI = scheme + config.zone.ioHost + '/prefetch/' + encodedEntryURI;
    var digest = util.generateAccessToken(mac, requestURI, null);
    rpc.postWithoutForm(requestURI, digest, callbackFunc);
}

// 修改文件的存储类型
// @link https://developer.qiniu.com/kodo/api/3710/modify-the-file-type
// @param bucket  空间名称
// @param key     文件名称
// @param newType 新文件存储类型
// @param callbackFunc(err, respBody, respInfo) 回调函数
BucketManager.prototype.changeType = function (bucket, key, newType,
    callbackFunc) {
    util.prepareZone(this, this.mac.accessKey, bucket, function (err, ctx) {
        if (err) {
            callbackFunc(err, null, null);
            return;
        }
        changeTypeReq(ctx.mac, ctx.config, bucket, key, newType, callbackFunc);
    });
};

function changeTypeReq (mac, config, bucket, key, newType, callbackFunc) {
    var scheme = config.useHttpsDomain ? 'https://' : 'http://';
    var changeTypeOp = exports.changeTypeOp(bucket, key, newType);
    var requestURI = scheme + config.zone.rsHost + changeTypeOp;
    var digest = util.generateAccessToken(mac, requestURI, null);
    rpc.postWithoutForm(requestURI, digest, callbackFunc);
}

// 设置空间镜像源
// @link https://developer.qiniu.com/kodo/api/1370/mirror
// @param bucket 空间名称
// @param srcSiteUrl 镜像源地址
// @param srcHost 镜像Host
// @param callbackFunc(err, respBody, respInfo) 回调函数
const PU_HOST = 'http://pu.qbox.me:10200';
BucketManager.prototype.image = function (bucket, srcSiteUrl, srcHost,
    callbackFunc) {
    var encodedSrcSite = util.urlsafeBase64Encode(srcSiteUrl);
    var requestURI = PU_HOST + '/image/' + bucket + '/from/' + encodedSrcSite;
    if (srcHost) {
        var encodedHost = util.urlsafeBase64Encode(srcHost);
        requestURI += '/host/' + encodedHost;
    }
    var digest = util.generateAccessToken(this.mac, requestURI, null);
    rpc.postWithoutForm(requestURI, digest, callbackFunc);
};

// 取消设置空间镜像源
// @link https://developer.qiniu.com/kodo/api/1370/mirror
// @param bucket 空间名称
// @param callbackFunc(err, respBody, respInfo) 回调函数
BucketManager.prototype.unimage = function (bucket, callbackFunc) {
    var requestURI = PU_HOST + '/unimage/' + bucket;
    var digest = util.generateAccessToken(this.mac, requestURI, null);
    rpc.postWithoutForm(requestURI, digest, callbackFunc);
};

// 获取指定前缀的文件列表
// @link https://developer.qiniu.com/kodo/api/1284/list
//
// @param bucket 空间名称
// @param options 列举操作的可选参数
//                prefix    列举的文件前缀
//                marker    上一次列举返回的位置标记，作为本次列举的起点信息
//                limit     每次返回的最大列举文件数量
//                delimiter 指定目录分隔符
// @param callbackFunc(err, respBody, respInfo) - 回调函数
BucketManager.prototype.listPrefix = function (bucket, options, callbackFunc) {
    util.prepareZone(this, this.mac.accessKey, bucket, function (err, ctx) {
        if (err) {
            callbackFunc(err, null, null);
            return;
        }
        listPrefixReq(ctx.mac, ctx.config, bucket, options, callbackFunc);
    });
};

function listPrefixReq (mac, config, bucket, options, callbackFunc) {
    options = options || {};
    // 必须参数
    var reqParams = {
        bucket: bucket
    };

    if (options.prefix) {
        reqParams.prefix = options.prefix;
    } else {
        reqParams.prefix = '';
    }

    if (options.limit >= 1 && options.limit <= 1000) {
        reqParams.limit = options.limit;
    } else {
        reqParams.limit = 1000;
    }

    if (options.marker) {
        reqParams.marker = options.marker;
    } else {
        reqParams.marker = '';
    }

    if (options.delimiter) {
        reqParams.delimiter = options.delimiter;
    } else {
        reqParams.delimiter = '';
    }

    var scheme = config.useHttpsDomain ? 'https://' : 'http://';
    var reqSpec = querystring.stringify(reqParams);
    var requestURI = scheme + config.zone.rsfHost + '/list?' + reqSpec;

    var auth = util.generateAccessToken(mac, requestURI, null);
    rpc.postWithForm(requestURI, null, auth, callbackFunc);
}

// 获取指定前缀的文件列表
//
// @param bucket 空间名称
// @param options 列举操作的可选参数
//                prefix    列举的文件前缀
//                marker    上一次列举返回的位置标记，作为本次列举的起点信息
//                limit     每次返回的最大列举文件数量
//                delimiter 指定目录分隔符
// @param callbackFunc(err, respBody, respInfo) - 回调函数
BucketManager.prototype.listPrefixV2 = function (bucket, options, callbackFunc) {
    util.prepareZone(this, this.mac.accessKey, bucket, function (err, ctx) {
        if (err) {
            callbackFunc(err, null, null);
            return;
        }
        listPrefixReqV2(ctx.mac, ctx.config, bucket, options, callbackFunc);
    });
};

function listPrefixReqV2 (mac, config, bucket, options, callbackFunc) {
    options = options || {};
    // 必须参数
    var reqParams = {
        bucket: bucket
    };

    if (options.prefix) {
        reqParams.prefix = options.prefix;
    } else {
        reqParams.prefix = '';
    }

    if (options.limit) {
        reqParams.limit = Math.min(1000, Math.max(0, options.limit));
    } else {
        reqParams.limit = 0;
    }

    if (options.marker) {
        reqParams.marker = options.marker;
    } else {
        reqParams.marker = '';
    }

    if (options.delimiter) {
        reqParams.delimiter = options.delimiter;
    } else {
        reqParams.delimiter = '';
    }

    var scheme = config.useHttpsDomain ? 'https://' : 'http://';
    var reqSpec = querystring.stringify(reqParams);
    var requestURI = scheme + config.zone.rsfHost + '/v2/list?' + reqSpec;

    var auth = util.generateAccessToken(mac, requestURI, null);
    rpc.postWithForm(requestURI, null, auth, callbackFunc);
}

// 批量文件管理请求，支持stat，chgm，chtype，delete，copy，move
BucketManager.prototype.batch = function (operations, callbackFunc) {
    var requestURI = conf.RS_HOST + '/batch';
    var reqParams = {
        op: operations
    };
    var reqBody = querystring.stringify(reqParams);
    var digest = util.generateAccessToken(this.mac, requestURI, reqBody);
    rpc.postWithForm(requestURI, reqBody, digest, callbackFunc);
};

// 批量操作支持的指令构造器
exports.statOp = function (bucket, key) {
    return '/stat/' + util.encodedEntry(bucket, key);
};

exports.deleteOp = function (bucket, key) {
    return '/delete/' + util.encodedEntry(bucket, key);
};

exports.deleteAfterDaysOp = function (bucket, key, days) {
    var encodedEntryURI = util.encodedEntry(bucket, key);
    return '/deleteAfterDays/' + encodedEntryURI + '/' + days;
};

exports.changeMimeOp = function (bucket, key, newMime) {
    var encodedEntryURI = util.encodedEntry(bucket, key);
    var encodedMime = util.urlsafeBase64Encode(newMime);
    return '/chgm/' + encodedEntryURI + '/mime/' + encodedMime;
};

exports.changeHeadersOp = function (bucket, key, headers) {
    var encodedEntryURI = util.encodedEntry(bucket, key);
    var prefix = 'x-qn-meta-!';
    var path = '/chgm/' + encodedEntryURI;
    for (var headerKey in headers) {
        var encodedValue = util.urlsafeBase64Encode(headers[headerKey]);
        var prefixedHeaderKey = prefix + headerKey;
        path += '/' + prefixedHeaderKey + '/' + encodedValue;
    }

    return path;
};

exports.changeTypeOp = function (bucket, key, newType) {
    var encodedEntryURI = util.encodedEntry(bucket, key);
    return '/chtype/' + encodedEntryURI + '/type/' + newType;
};

exports.changeStatusOp = function (bucket, key, newStatus) {
    var encodedEntryURI = util.encodedEntry(bucket, key);
    return '/chstatus/' + encodedEntryURI + '/status/' + newStatus;
};

exports.moveOp = function (srcBucket, srcKey, destBucket, destKey, options) {
    options = options || {};
    var encodedEntryURISrc = util.encodedEntry(srcBucket, srcKey);
    var encodedEntryURIDest = util.encodedEntry(destBucket, destKey);
    var op = '/move/' + encodedEntryURISrc + '/' + encodedEntryURIDest;
    if (options.force) {
        op += '/force/true';
    }
    return op;
};

exports.copyOp = function (srcBucket, srcKey, destBucket, destKey, options) {
    options = options || {};
    var encodedEntryURISrc = util.encodedEntry(srcBucket, srcKey);
    var encodedEntryURIDest = util.encodedEntry(destBucket, destKey);
    var op = '/copy/' + encodedEntryURISrc + '/' + encodedEntryURIDest;
    if (options.force) {
        op += '/force/true';
    }
    return op;
};

// 空间资源下载

// 获取私有空间的下载链接
// @param domain 空间绑定的域名，比如以http或https开头
// @param fileName 原始文件名
// @param deadline 文件有效期时间戳（单位秒）
// @return 私有下载链接
BucketManager.prototype.privateDownloadUrl = function (domain, fileName,
    deadline) {
    var baseUrl = this.publicDownloadUrl(domain, fileName);
    if (baseUrl.indexOf('?') >= 0) {
        baseUrl += '&e=';
    } else {
        baseUrl += '?e=';
    }
    baseUrl += deadline;

    var signature = util.hmacSha1(baseUrl, this.mac.secretKey);
    var encodedSign = util.base64ToUrlSafe(signature);
    var downloadToken = this.mac.accessKey + ':' + encodedSign;
    return baseUrl + '&token=' + downloadToken;
};

// 获取公开空间的下载链接
// @param domain 空间绑定的域名，比如以http或https开头
// @param fileName 原始文件名
// @return 公开下载链接
BucketManager.prototype.publicDownloadUrl = function (domain, fileName) {
    return domain + '/' + encodeUrl(fileName);
};

//  修改文件状态
// @link https://developer.qiniu.com/kodo/api/4173/modify-the-file-status
// @param bucket  空间名称
// @param key     文件名称
// @param status  文件状态
// @param callbackFunc(err, respBody, respInfo) 回调函数
// updateObjectStatus(bucketName string, key string, status ObjectStatus, condition UpdateObjectInfoCondition)
BucketManager.prototype.updateObjectStatus = function (bucket, key, status,
    callbackFunc) {
    util.prepareZone(this, this.mac.accessKey, bucket, function (err, ctx) {
        if (err) {
            callbackFunc(err, null, null);
            return;
        }
        updateStatusReq(ctx.mac, ctx.config, bucket, key, status, callbackFunc);
    });
};

function updateStatusReq (mac, config, bucket, key, status, callbackFunc) {
    var scheme = config.useHttpsDomain ? 'https://' : 'http://';
    var changeStatusOp = exports.changeStatusOp(bucket, key, status);
    var requestURI = scheme + config.zone.rsHost + changeStatusOp;
    var digest = util.generateAccessToken(mac, requestURI, null);
    rpc.postWithoutForm(requestURI, digest, callbackFunc);
}

// 列举bucket
// @link https://developer.qiniu.com/kodo/api/3926/get-service
// @param callbackFunc(err, respBody, respInfo) 回调函数
BucketManager.prototype.listBucket = function (callbackFunc) {
    var requestURI = 'https://rs.qbox.me/buckets';
    var digest = util.generateAccessToken(this.mac, requestURI, null);
    rpc.postWithoutForm(requestURI, digest, callbackFunc);
};

// 获取bucket信息
// @param bucket 空间名
// @param callbackFunc(err, respBody, respInfo) 回调函数
BucketManager.prototype.getBucketInfo = function (bucket, callbackFunc) {
    var scheme = this.config.useHttpsDomain ? 'https://' : 'http://';
    var requestURI = scheme + conf.UC_HOST + '/v2/bucketInfo?bucket=' + bucket;
    var digest = util.generateAccessToken(this.mac, requestURI, null);
    rpc.postWithoutForm(requestURI, digest, callbackFunc);
};

// rules/add增加bucket规则
// @param bucket 空间名
// @param name: 规则名称 bucket 内唯一，长度小于50，不能为空，只能为字母、数字、下划线
// @param prefix: 同一个 bucket 里面前缀不能重复
// @param to_line_after_days: 指定文件上传多少天后转低频存储。指定为0表示不转低频存储，
//      小于0表示上传的文件立即变低频存储
// @param delete_after_days: 指定上传文件多少天后删除，指定为0表示不删除，大于0表示多少天后删除
// @param history_delete_after_days: 指定文件成为历史版本多少天后删除，指定为0表示不删除，
//      大于0表示多少天后删除
// @param history_to_line_after_days: 指定文件成为历史版本多少天后转低频存储。指定为0表示不转低频存储
BucketManager.prototype.putBucketLifecycleRule = function (bucket, options,
    callbackFunc) {
    PutBucketLifecycleRule(this.mac, this.config, bucket, options, callbackFunc);
};

function PutBucketLifecycleRule (mac, config, bucket, options, callbackFunc) {
    options = options || {};
    var reqParams = {
        bucket: bucket,
        name: options.name
    };

    if (options.prefix) {
        reqParams.prefix = options.prefix;
    } else {
        reqParams.prefix = '';
    }

    if (options.to_line_after_days) {
        reqParams.to_line_after_days = options.to_line_after_days;
    } else {
        reqParams.to_line_after_days = 0;
    }

    if (options.delete_after_days) {
        reqParams.delete_after_days = options.delete_after_days;
    } else {
        reqParams.delete_after_days = 0;
    }

    if (options.history_delete_after_days) {
        reqParams.history_delete_after_days = options.history_delete_after_days;
    } else {
        reqParams.history_delete_after_days = 0;
    }

    if (options.history_to_line_after_days) {
        reqParams.history_to_line_after_days = options.history_to_line_after_days;
    } else {
        reqParams.history_to_line_after_days = 0;
    }

    var scheme = config.useHttpsDomain ? 'https://' : 'http://';
    var reqSpec = querystring.stringify(reqParams);
    var requestURI = scheme + conf.UC_HOST + '/rules/add?' + reqSpec;
    var auth = util.generateAccessToken(mac, requestURI, null);
    rpc.postWithoutForm(requestURI, auth, callbackFunc);
}

// rules/delete 删除bucket规则
// @param bucket 空间名
// @param name: 规则名称 bucket 内唯一，长度小于50，不能为空，只能为字母、数字、下划线
BucketManager.prototype.deleteBucketLifecycleRule = function (bucket, name, callbackFunc) {
    var reqParams = {
        bucket: bucket,
        name: name
    };
    var scheme = this.config.useHttpsDomain ? 'https://' : 'http://';
    var reqSpec = querystring.stringify(reqParams);
    var requestURI = scheme + conf.UC_HOST + '/rules/delete?' + reqSpec;
    var digest = util.generateAccessToken(this.mac, requestURI, null);
    rpc.postWithoutForm(requestURI, digest, callbackFunc);
};

// rules/update 更新bucket规则
// @param bucket 空间名
BucketManager.prototype.updateBucketLifecycleRule = function (bucket, options, callbackFunc) {
    options = options || {};
    var reqParams = {
        bucket: bucket,
        name: options.name
    };

    if (options.prefix) {
        reqParams.prefix = options.prefix;
    }

    if (options.to_line_after_days) {
        reqParams.to_line_after_days = options.to_line_after_days;
    }

    if (options.delete_after_days) {
        reqParams.delete_after_days = options.delete_after_days;
    }

    if (options.history_delete_after_days) {
        reqParams.history_delete_after_days = options.history_delete_after_days;
    }

    if (options.history_to_line_after_days) {
        reqParams.history_to_line_after_days = options.history_to_line_after_days;
    }

    var scheme = this.config.useHttpsDomain ? 'https://' : 'http://';
    var reqSpec = querystring.stringify(reqParams);
    var requestURI = scheme + conf.UC_HOST + '/rules/update?' + reqSpec;
    var digest = util.generateAccessToken(this.mac, requestURI, null);
    rpc.postWithoutForm(requestURI, digest, callbackFunc);
};

// rules/get 获取bucket规则
// @param bucket 空间名
BucketManager.prototype.getBucketLifecycleRule = function (bucket, callbackFunc) {
    var scheme = this.config.useHttpsDomain ? 'https://' : 'http://';
    var requestURI = scheme + conf.UC_HOST + '/rules/get?bucket=' + bucket;
    var digest = util.generateAccessToken(this.mac, requestURI, null);
    rpc.postWithoutForm(requestURI, digest, callbackFunc);
};

// events/add 增加事件通知规则
BucketManager.prototype.putBucketEvent = function (bucket, options, callbackFunc) {
    PutBucketEvent(this.mac, this.config, options, bucket, callbackFunc);
};

function PutBucketEvent (mac, config, options, bucket, callbackFunc) {
    options = options || {};
    var reqParams = { // 必填参数
        bucket: bucket,
        name: options.name,
        event: options.event,
        callbackURL: options.callbackURL
    };

    if (options.prefix) {
        reqParams.prefix = options.prefix;
    } else {
        reqParams.prefix = '';
    }

    if (options.suffix) {
        reqParams.suffix = options.suffix;
    } else {
        reqParams.suffix = '';
    }

    if (options.access_key) {
        reqParams.access_key = options.access_key;
    } else {
        reqParams.access_key = '';
    }

    if (options.host) {
        reqParams.host = options.host;
    } else {
        reqParams.host = '';
    }

    var scheme = config.useHttpsDomain ? 'https://' : 'http://';
    var reqSpec = querystring.stringify(reqParams);
    var requestURI = scheme + conf.UC_HOST + '/events/add?' + reqSpec;
    var digest = util.generateAccessToken(mac, requestURI, null);
    rpc.postWithoutForm(requestURI, digest, callbackFunc);
}

// events/get 更新事件通知规则
BucketManager.prototype.updateBucketEvent = function (bucket, options, callbackFunc) {
    UpdateBucketEvent(this.mac, this.config, options, bucket, callbackFunc);
};

function UpdateBucketEvent (mac, config, options, bucket, callbackFunc) {
    options = options || {};
    var reqParams = {
        bucket: bucket,
        name: options.name
    };

    if (options.prefix) {
        reqParams.prefix = options.prefix;
    }

    if (options.suffix) {
        reqParams.suffix = options.suffix;
    }

    if (options.event) {
        reqParams.event = options.event;
    }

    if (options.callbackURL) {
        reqParams.callbackURL = options.callbackURL;
    }

    if (options.access_key) {
        reqParams.access_key = options.access_key;
    }

    if (options.host) {
        reqParams.host = options.host;
    }

    var scheme = config.useHttpsDomain ? 'https://' : 'http://';
    var reqSpec = querystring.stringify(reqParams);
    var requestURI = scheme + conf.UC_HOST + '/events/update?' + reqSpec;
    var digest = util.generateAccessToken(mac, requestURI, null);
    rpc.postWithoutForm(requestURI, digest, callbackFunc);
}

// events/get 获取事件通知规则
BucketManager.prototype.getBucketEvent = function (bucket, callbackFunc) {
    var scheme = this.config.useHttpsDomain ? 'https://' : 'http://';
    var requestURI = scheme + conf.UC_HOST + '/events/get?bucket=' + bucket;
    var digest = util.generateAccessToken(this.mac, requestURI, null);
    rpc.postWithoutForm(requestURI, digest, callbackFunc);
};

// events/delete 删除事件通知规则
BucketManager.prototype.deleteBucketEvent = function (bucket, name, callbackFunc) {
    var reqParams = {
        bucket: bucket,
        name: name
    };
    var scheme = this.config.useHttpsDomain ? 'https://' : 'http://';
    var reqSpec = querystring.stringify(reqParams);
    var requestURI = scheme + conf.UC_HOST + '/events/delete?' + reqSpec;
    var digest = util.generateAccessToken(this.mac, requestURI, null);
    rpc.postWithoutForm(requestURI, digest, callbackFunc);
};

// 设置防盗链
// @param bucket: bucket 名
// @param mode 0: 表示关闭Referer; 1: 表示设置Referer白名单; 2: 表示设置Referer黑名单
// @param norefer 0: 表示不允许空 Refer 访问; 1: 表示允许空 Refer 访问
// @param pattern  一种为空主机头域名, 比如 foo.com; 一种是泛域名, 比如 *.bar.com;
//          一种是完全通配符, 即一个 *; 多个规则之间用;隔开
// @param source_enabled=: 源站是否支持，默认为0只给CDN配置, 设置为1表示开启源站防盗链
BucketManager.prototype.putReferAntiLeech = function (bucket, options, callbackFunc) {
    PutReferAntiLeech(this.mac, this.config, bucket, options, callbackFunc);
};

function PutReferAntiLeech (mac, config, bucket, options, callbackFunc) {
    options = options || {};
    var reqParams = {
        bucket: bucket
    };

    if (options.mode) {
        reqParams.mode = options.mode;
    } else {
        reqParams.mode = 0;
    }

    if (options.norefer) {
        reqParams.norefer = options.norefer;
    } else {
        reqParams.norefer = 0;
    }

    if (options.pattern) {
        reqParams.pattern = options.pattern;
    } else {
        reqParams.pattern = '*';
    }

    if (options.source_enabled) {
        reqParams.source_enabled = options.source_enabled;
    } else {
        reqParams.source_enabled = 0;
    }

    var scheme = config.useHttpsDomain ? 'https://' : 'http://';
    var reqSpec = querystring.stringify(reqParams);
    var requestURI = scheme + conf.UC_HOST + '/referAntiLeech?' + reqSpec;
    var digest = util.generateAccessToken(mac, requestURI, null);
    rpc.postWithoutForm(requestURI, digest, callbackFunc);
}

/// corsRules/set 设置bucket的cors（跨域）规则
BucketManager.prototype.putCorsRules = function (bucket, body, callbackFunc) {
    PutCorsRules(this.mac, this.config, bucket, body, callbackFunc);
};

function PutCorsRules (mac, config, bucket, body, callbackFunc) {
    var reqBody = JSON.stringify(body);
    var scheme = config.useHttpsDomain ? 'https://' : 'http://';
    var requestURI = scheme + conf.UC_HOST + '/corsRules/set/' + bucket;
    var auth = util.generateAccessToken(mac, requestURI, reqBody);
    rpc.postWithForm(requestURI, reqBody, auth, callbackFunc);
}

/// corsRules/get 获取bucket跨域
BucketManager.prototype.getCorsRules = function (bucket, callbackFunc) {
    GetCorsRules(this.mac, this.config, bucket, callbackFunc);
};

function GetCorsRules (mac, config, bucket, callbackFunc) {
    var scheme = config.useHttpsDomain ? 'https://' : 'http://';
    var requestURI = scheme + conf.UC_HOST + '/corsRules/get/' + bucket;
    var digest = util.generateAccessToken(mac, requestURI, null);
    rpc.postWithoutForm(requestURI, digest, callbackFunc);
}

// BucketManager.prototype.getBucketSourceConfig = function(body, callbackFunc) {
//     var reqBody = JSON.stringify(body);
//     console.log(reqBody);
//     var scheme = this.config.useHttpsDomain ? 'https://' : 'http://';
//     var requestURI = scheme + conf.UC_HOST + '/mirrorConfig/get';
//     var digest = util.generateAccessTokenV2(this.mac, requestURI, 'POST', conf.FormMimeJson, reqBody);
//     rpc.postWithForm(requestURI, reqBody,digest, callbackFunc);
// }

// 原图保护
// @param bucket 空间名称
// @param mode 为1表示开启原图保护，0表示关闭
BucketManager.prototype.putBucketAccessStyleMode = function (bucket, mode, callbackFunc) {
    var scheme = this.config.useHttpsDomain ? 'https://' : 'http://';
    var requestURI = scheme + conf.UC_HOST + '/accessMode/' + bucket + '/mode/' + mode;
    var digest = util.generateAccessToken(this.mac, requestURI, null);
    rpc.postWithoutForm(requestURI, digest, callbackFunc);
};

// 设置Bucket的cache-control: max-age属性
// @param maxAge:为0或者负数表示为默认值（31536000）
BucketManager.prototype.putBucketMaxAge = function (bucket, options, callbackFunc) {
    var maxAge = options.maxAge;
    if (maxAge <= 0) {
        maxAge = 31536000;
    }
    var reqParams = {
        bucket: bucket,
        maxAge: maxAge
    };
    var scheme = this.config.useHttpsDomain ? 'https://' : 'http://';
    var reqSpec = querystring.stringify(reqParams);
    var requestURI = scheme + conf.UC_HOST + '/maxAge?' + reqSpec;
    var digest = util.generateAccessToken(this.mac, requestURI, null);
    rpc.postWithoutForm(requestURI, digest, callbackFunc);
};

// 设置Bucket私有属性
// @param private为0表示公开，为1表示私有
BucketManager.prototype.putBucketAccessMode = function (bucket, options, callbackFunc) {
    options = options || {};
    var reqParams = {
        bucket: bucket
    };

    if (options.private) {
        reqParams.private = options.private;
    } else {
        reqParams.private = 0;
    }

    var scheme = this.config.useHttpsDomain ? 'https://' : 'http://';
    var reqSpec = querystring.stringify(reqParams);
    var requestURI = scheme + conf.UC_HOST + '/private?' + reqSpec;
    var digest = util.generateAccessToken(this.mac, requestURI, null);
    rpc.postWithoutForm(requestURI, digest, callbackFunc);
};

// 设置配额
// @param bucket: 空间名称，不支持授权空间
// @param size: 空间存储量配额,参数传入0或不传表示不更改当前配置，传入-1表示取消限额，新创建的空间默认没有限额。
// @param count: 空间文件数配额，参数含义同<size>
BucketManager.prototype.putBucketQuota = function (bucket, options, callbackFunc) {
    options = options || {};
    var reqParams = {
        bucket: bucket
    };

    if (options.size) {
        reqParams.size = options.size;
    } else {
        reqParams.size = 0;
    }

    if (options.count) {
        reqParams.count = options.count;
    } else {
        reqParams.count = 0;
    }

    var scheme = this.config.useHttpsDomain ? 'https://' : 'http://';
    var reqSpec = `${reqParams.bucket}/size/${reqParams.size}/count/${reqParams.count}`;
    var requestURI = scheme + conf.UC_HOST + '/setbucketquota/' + reqSpec;
    var digest = util.generateAccessToken(this.mac, requestURI, null);
    rpc.postWithoutForm(requestURI, digest, callbackFunc);
};

// 获取配额
// @param bucket: 空间名称，不支持授权空间
BucketManager.prototype.getBucketQuota = function (bucket, callbackFunc) {
    var scheme = this.config.useHttpsDomain ? 'https://' : 'http://';
    var requestURI = scheme + conf.UC_HOST + '/getbucketquota/' + bucket;
    var digest = util.generateAccessToken(this.mac, requestURI, null);
    rpc.postWithoutForm(requestURI, digest, callbackFunc);
};

// 获得Bucket的所有域名
// @param bucket:bucketName
BucketManager.prototype.listBucketDomains = function (bucket, callbackFunc) {
    var scheme = this.config.useHttpsDomain ? 'https://' : 'http://';
    var requestURI = scheme + conf.UC_HOST + '/v3/domains?tbl=' + bucket;
    var digest = util.generateAccessToken(this.mac, requestURI, null);
    rpc.postWithoutForm(requestURI, digest, callbackFunc);
};

//解冻归档存储文件
BucketManager.prototype.restoreAr = function (entry, freezeAfterDays, callbackFunc) {
    var scheme = this.config.useHttpsDomain ? 'https://' : 'http://';
    var requestURI = scheme + conf.RS_QBOX + "/restoreAr/"+util.urlsafeBase64Encode(entry)+"/freezeAfterDays/"+freezeAfterDays;
    var digest = util.generateAccessToken(this.mac, requestURI, null);
    rpc.postWithoutForm(requestURI, digest, callbackFunc);
};

// 上传策略
// @link https://developer.qiniu.com/kodo/manual/1206/put-policy
function PutPolicy (options) {
    if (typeof options !== 'object') {
        throw new Error('invalid putpolicy options');
    }

    this.scope = options.scope || null;
    this.isPrefixalScope = options.isPrefixalScope || null;
    this.expires = options.expires || 3600;
    this.insertOnly = options.insertOnly || null;

    this.saveKey = options.saveKey || null;
    this.endUser = options.endUser || null;

    this.returnUrl = options.returnUrl || null;
    this.returnBody = options.returnBody || null;

    this.callbackUrl = options.callbackUrl || null;
    this.callbackHost = options.callbackHost || null;
    this.callbackBody = options.callbackBody || null;
    this.callbackBodyType = options.callbackBodyType || null;
    this.callbackFetchKey = options.callbackFetchKey || null;

    this.persistentOps = options.persistentOps || null;
    this.persistentNotifyUrl = options.persistentNotifyUrl || null;
    this.persistentPipeline = options.persistentPipeline || null;

    this.fsizeLimit = options.fsizeLimit || null;
    this.fsizeMin = options.fsizeMin || null;
    this.mimeLimit = options.mimeLimit || null;

    this.detectMime = options.detectMime || null;
    this.deleteAfterDays = options.deleteAfterDays || null;
    this.fileType = options.fileType || null;
}

PutPolicy.prototype.getFlags = function () {
    var flags = {};
    var attrs = ['scope', 'isPrefixalScope', 'insertOnly', 'saveKey', 'endUser',
        'returnUrl', 'returnBody', 'callbackUrl', 'callbackHost',
        'callbackBody', 'callbackBodyType', 'callbackFetchKey', 'persistentOps',
        'persistentNotifyUrl', 'persistentPipeline', 'fsizeLimit', 'fsizeMin',
        'detectMime', 'mimeLimit', 'deleteAfterDays', 'fileType'
    ];

    for (var i = attrs.length - 1; i >= 0; i--) {
        if (this[attrs[i]] !== null) {
            flags[attrs[i]] = this[attrs[i]];
        }
    }

    flags.deadline = this.expires + Math.floor(Date.now() / 1000);

    return flags;
};

PutPolicy.prototype.uploadToken = function (mac) {
    mac = mac || new digest.Mac();
    var flags = this.getFlags();
    var encodedFlags = util.urlsafeBase64Encode(JSON.stringify(flags));
    var encoded = util.hmacSha1(encodedFlags, mac.secretKey);
    var encodedSign = util.base64ToUrlSafe(encoded);
    var uploadToken = mac.accessKey + ':' + encodedSign + ':' + encodedFlags;
    return uploadToken;
};
