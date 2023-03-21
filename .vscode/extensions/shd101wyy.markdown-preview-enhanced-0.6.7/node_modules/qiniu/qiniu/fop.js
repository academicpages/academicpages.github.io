const util = require('./util');
const rpc = require('./rpc');
const conf = require('./conf');
const digest = require('./auth/digest');
const querystring = require('querystring');

exports.OperationManager = OperationManager;

function OperationManager (mac, config) {
    this.mac = mac || new digest.Mac();
    this.config = config || new conf.Config();
}

// 发送持久化数据处理请求
// @param bucket - 空间名称
// @param key  - 文件名称
// @param fops - 处理指令集合
// @param pipeline - 处理队列名称
// @param options - 可选参数
//                  notifyURL 回调业务服务器，通知处理结果
//                  force     结果是否强制覆盖已有的同名文件
// @param callbackFunc(err, respBody, respInfo) - 回调函数
OperationManager.prototype.pfop = function (bucket, key, fops, pipeline,
    options, callbackFunc) {
    options = options || {};
    // 必须参数
    var reqParams = {
        bucket: bucket,
        key: key,
        pipeline: pipeline,
        fops: fops.join(';')
    };

    // notifyURL
    if (options.notifyURL) {
        reqParams.notifyURL = options.notifyURL;
    }

    // force
    if (options.force) {
        reqParams.force = 1;
    }

    util.prepareZone(this, this.mac.accessKey, bucket, function (err, ctx) {
        if (err) {
            callbackFunc(err, null, null);
            return;
        }
        pfopReq(ctx.mac, ctx.config, reqParams, callbackFunc);
    });
};

function pfopReq (mac, config, reqParams, callbackFunc) {
    var scheme = config.useHttpsDomain ? 'https://' : 'http://';
    var requestURI = scheme + config.zone.apiHost + '/pfop/';
    var reqBody = querystring.stringify(reqParams);
    var auth = util.generateAccessToken(mac, requestURI, reqBody);
    rpc.postWithForm(requestURI, reqBody, auth, callbackFunc);
}

// 查询持久化数据处理进度
// @param persistentId
// @callbackFunc(err, respBody, respInfo) - 回调函数
OperationManager.prototype.prefop = function (persistentId, callbackFunc) {
    var apiHost = 'api.qiniu.com';
    if (this.config.zone) {
        apiHost = this.config.zone.apiHost;
    }

    var scheme = this.config.useHttpsDomain ? 'https://' : 'http://';
    var requestURI = scheme + apiHost + '/status/get/prefop';
    var reqParams = {
        id: persistentId
    };
    var reqBody = querystring.stringify(reqParams);
    rpc.postWithForm(requestURI, reqBody, null, callbackFunc);
};
