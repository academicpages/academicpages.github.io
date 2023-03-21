var urllib = require('urllib');
var conf = require('./conf');

exports.post = post;
exports.postMultipart = postMultipart;
exports.postWithForm = postWithForm;
exports.postWithoutForm = postWithoutForm;

function postMultipart (requestURI, requestForm, callbackFunc) {
    return post(requestURI, requestForm, requestForm.headers(), callbackFunc);
}

function postWithForm (requestURI, requestForm, token, callbackFunc) {
    var headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    };
    if (token) {
        headers.Authorization = token;
    }
    return post(requestURI, requestForm, headers, callbackFunc);
}

function postWithoutForm (requestURI, token, callbackFunc) {
    var headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    };
    if (token) {
        headers.Authorization = token;
    }
    return post(requestURI, null, headers, callbackFunc);
}

function post (requestURI, requestForm, headers, callbackFunc) {
    // var start = parseInt(Date.now() / 1000);
    headers = headers || {};
    headers['User-Agent'] = headers['User-Agent'] || conf.USER_AGENT;
    headers.Connection = 'keep-alive';

    var data = {
        headers: headers,
        method: 'POST',
        dataType: 'json',
        timeout: conf.RPC_TIMEOUT,
        gzip: true
    //  timing: true,
    };

    if (conf.RPC_HTTP_AGENT) {
        data.agent = conf.RPC_HTTP_AGENT;
    }

    if (conf.RPC_HTTPS_AGENT) {
        data.httpsAgent = conf.RPC_HTTPS_AGENT;
    }

    if (Buffer.isBuffer(requestForm) || typeof requestForm === 'string') {
        data.content = requestForm;
    } else if (requestForm) {
        data.stream = requestForm;
    } else {
        data.headers['Content-Length'] = 0;
    }

    var req = urllib.request(requestURI, data, function (respErr, respBody,
        respInfo) {
    // var end = parseInt(Date.now() / 1000);
    // console.log((end - start) + " seconds");
    // console.log("queuing:\t" + respInfo.timing.queuing);
    // console.log("dnslookup:\t" + respInfo.timing.dnslookup);
    // console.log("connected:\t" + respInfo.timing.connected);
    // console.log("requestSent:\t" + respInfo.timing.requestSent);
    // console.log("waiting:\t" + respInfo.timing.waiting);
    // console.log("contentDownload:\t" + respInfo.timing.contentDownload);

        callbackFunc(respErr, respBody, respInfo);
    });

    return req;
}
