var http = require('http');

const host = 'rtc.qiniuapi.com';
const headers = {
    'Content-Type': 'application/json'
};

function get (credentials, options, fn) {
    options.headers.Authorization = credentials.generateAccessToken(options, null);

    var req = http.request(options, function (res) {
        res.setEncoding('utf-8');

        var responseString = '';

        res.on('data', function (data) {
            responseString += data;
        });

        res.on('end', function () {
            var resultObject = JSON.parse(responseString);

            if (res.statusCode != 200) {
                var result = {
                    code: res.statusCode,
                    message: res.statusMessage
                };
                fn(result, null);
            } else {
                fn(null, resultObject);
            }
        });
    });

    req.on('error', function (e) {
        fn(e, null);
    });

    req.end();
}

function post (credentials, options, data, fn) {
    var dataString = JSON.stringify(data);

    options.headers.Authorization = credentials.generateAccessToken(options, dataString);

    var req = http.request(options, function (res) {
        res.setEncoding('utf-8');

        var responseString = '';

        res.on('data', function (data) {
            responseString += data;
        });

        res.on('end', function () {
            var resultObject = JSON.parse(responseString);

            if (res.statusCode != 200) {
                var result = {
                    code: res.statusCode,
                    message: res.statusMessage
                };
                fn(result, null);
            } else {
                fn(null, resultObject);
            }
        });
    });
    req.on('error', function (e) {
        fn(e, null);
    });

    req.write(dataString);

    req.end();
}

exports.createApp = function (app, credentials, fn) {
    var options = {
        host: host,
        port: 80,
        path: '/v3/apps',
        method: 'POST',
        headers: headers
    };
    post(credentials, options, app, fn);
};

exports.getApp = function (appId, credentials, fn) {
    var options = {
        host: host,
        port: 80,
        path: '/v3/apps/' + appId,
        method: 'GET',
        headers: headers
    };
    get(credentials, options, fn);
};

exports.deleteApp = function (appId, credentials, fn) {
    var options = {
        host: host,
        port: 80,
        path: '/v3/apps/' + appId,
        method: 'DELETE',
        headers: headers
    };
    get(credentials, options, fn);
};

exports.updateApp = function (appId, app, credentials, fn) {
    var options = {
        host: host,
        port: 80,
        path: '/v3/apps/' + appId,
        method: 'POST',
        headers: headers
    };
    post(credentials, options, app, fn);
};
