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
            // var resultObject = JSON.parse(responseString);
            // console.log(JSON.parse(responseString))

            if (res.statusCode != 200) {
                var result = {
                    code: res.statusCode,
                    message: res.statusMessage
                };
                fn(result, null);
            } else {
                fn(null, JSON.parse(responseString));
            }
        });
    });

    req.on('error', function (e) {
        fn(e, null);
    });

    req.end();
}

// function post(credentials, options, data, fn) {
//     var dataString = JSON.stringify(data);

//     options.headers['Authorization'] = credentials.generateAccessToken(options, dataString);

//     var req = http.request(options, function(res) {
//         res.setEncoding('utf-8');

//         var responseString = '';

//         res.on('data', function(data) {
//             responseString += data;
//         });

//         res.on('end', function() {
//             var resultObject = JSON.parse(responseString);

//             if (res.statusCode != 200) {
//                 var result = {
//                     code: res.statusCode,
//                     message: res.statusMessage
//                 };
//                 fn(result, null);
//             } else {
//                 fn(null, resultObject);
//             }
//         });
//     });
//     req.on('error', function(e) {
//         fn(e, null);
//     });

//     req.write(dataString);

//     req.end();
// }

exports.listUser = function (appId, roomName, credentials, fn) {
    var options = {
        host: host,
        port: 80,
        path: '/v3/apps/' + appId + '/rooms/' + roomName + '/users',
        method: 'GET',
        headers: headers
    };
    get(credentials, options, fn);
};

exports.kickUser = function (appId, roomName, userId, credentials, fn) {
    var options = {
        host: host,
        port: 80,
        path: '/v3/apps/' + appId + '/rooms/' + roomName + '/users/' + userId,
        method: 'DELETE',
        headers: headers
    };
    get(credentials, options, fn);
};

exports.listActiveRooms = function (appId, roomNamePrefix, offset, limit, credentials, fn) {
    var options = {
        host: host,
        port: 80,
        path: '/v3/apps/' + appId + '/rooms?prefix=' + roomNamePrefix + '&offset=' + offset + '&limit=' + limit,
        method: 'GET',
        headers: headers
    };
    get(credentials, options, fn);
};

exports.getRoomToken = function (roomAccess, credentials) {
    if (!roomAccess.expireAt) {
        roomAccess.expireAt = Math.floor(Date.now() / 1000) + 3600;
    }
    return credentials.signJson(roomAccess);
};
