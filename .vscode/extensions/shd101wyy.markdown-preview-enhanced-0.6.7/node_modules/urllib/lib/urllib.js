'use strict';

var debug = require('debug')('urllib');
var path = require('path');
var dns = require('dns');
var http = require('http');
var https = require('https');
var urlutil = require('url');
var URL = urlutil.URL;
var util = require('util');
var qs = require('qs');
var ip = require('ip');
var querystring = require('querystring');
var zlib = require('zlib');
var ua = require('default-user-agent');
var digestAuthHeader = require('digest-header');
var ms = require('humanize-ms');
var statuses = require('statuses');
var contentTypeParser = require('content-type');
var first = require('ee-first');
var pump = require('pump');
var utility = require('utility');
var FormStream = require('formstream');
var detectProxyAgent = require('./detect_proxy_agent');

var _Promise;
var _iconv;

var pkg = require('../package.json');

var USER_AGENT = exports.USER_AGENT = ua('node-urllib', pkg.version);
var NODE_MAJOR_VERSION = parseInt(process.versions.node.split('.')[0]);

// change Agent.maxSockets to 1000
exports.agent = new http.Agent();
exports.agent.maxSockets = 1000;

exports.httpsAgent = new https.Agent();
exports.httpsAgent.maxSockets = 1000;

var LONG_STACK_DELIMITER = '\n    --------------------\n';

/**
 * The default request timeout(in milliseconds).
 * @type {Number}
 * @const
 */

exports.TIMEOUT = ms('5s');
exports.TIMEOUTS = [ms('5s'), ms('5s')];

var REQUEST_ID = 0;
var MAX_VALUE = Math.pow(2, 31) - 10;
var isNode010 = /^v0\.10\.\d+$/.test(process.version);
var isNode012 = /^v0\.12\.\d+$/.test(process.version);

/**
 * support data types
 * will auto decode response body
 * @type {Array}
 */
var TEXT_DATA_TYPES = [
  'json',
  'text'
];

var PROTO_RE = /^https?:\/\//i;

// Keep-Alive: timeout=5, max=100
var KEEP_ALIVE_RE = /^timeout=(\d+)/i;

var SOCKET_REQUEST_COUNT = '_URLLIB_SOCKET_REQUEST_COUNT';
var SOCKET_RESPONSE_COUNT = '_URLLIB_SOCKET_RESPONSE_COUNT';

/**
 * Handle all http request, both http and https support well.
 *
 * @example
 *
 * ```js
 * // GET https://nodejs.org
 * urllib.request('https://nodejs.org', function(err, data, res) {});
 * // POST https://nodejs.org
 * var args = { type: 'post', data: { foo: 'bar' } };
 * urllib.request('https://nodejs.org', args, function(err, data, res) {});
 * ```
 *
 * @param {String|Object} url: the request full URL.
 * @param {Object} [args]: optional
 *   - {Object} [data]: request data, will auto be query stringify.
 *   - {Boolean} [dataAsQueryString]: force convert `data` to query string.
 *   - {String|Buffer} [content]: optional, if set content, `data` will ignore.
 *   - {ReadStream} [stream]: read stream to sent.
 *   - {WriteStream} [writeStream]: writable stream to save response data.
 *       If you use this, callback's data should be null.
 *       We will just `pipe(ws, {end: true})`.
 *   - {consumeWriteStream} [true]: consume the writeStream, invoke the callback after writeStream close.
 *   - {Array<ReadStream|Buffer|String>|Object|ReadStream|Buffer|String} [files]: optional,
 *       The files will send with `multipart/form-data` format, base on `formstream`.
 *       If `method` not set, will use `POST` method by default.
 *   - {String} [method]: optional, could be GET | POST | DELETE | PUT, default is GET
 *   - {String} [contentType]: optional, request data type, could be `json`, default is undefined
 *   - {String} [dataType]: optional, response data type, could be `text` or `json`, default is buffer
 *   - {Boolean|Function} [fixJSONCtlChars]: optional, fix the control characters (U+0000 through U+001F)
 *       before JSON parse response. Default is `false`.
 *       `fixJSONCtlChars` can be a function, will pass data to the first argument. e.g.: `data = fixJSONCtlChars(data)`
 *   - {Object} [headers]: optional, request headers
 *   - {Number|Array} [timeout]: request timeout(in milliseconds), default is `exports.TIMEOUTS containing connect timeout and response timeout`
 *   - {Agent} [agent]: optional, http agent. Set `false` if you does not use agent.
 *   - {Agent} [httpsAgent]: optional, https agent. Set `false` if you does not use agent.
 *   - {String} [auth]: Basic authentication i.e. 'user:password' to compute an Authorization header.
 *   - {String} [digestAuth]: Digest authentication i.e. 'user:password' to compute an Authorization header.
 *   - {String|Buffer|Array} [ca]: An array of strings or Buffers of trusted certificates.
 *       If this is omitted several well known "root" CAs will be used, like VeriSign.
 *       These are used to authorize connections.
 *       Notes: This is necessary only if the server uses the self-signed certificate
 *   - {Boolean} [rejectUnauthorized]: If true, the server certificate is verified against the list of supplied CAs.
 *       An 'error' event is emitted if verification fails. Default: true.
 *   - {String|Buffer} [pfx]: A string or Buffer containing the private key,
 *       certificate and CA certs of the server in PFX or PKCS12 format.
 *   - {String|Buffer} [key]: A string or Buffer containing the private key of the client in PEM format.
 *       Notes: This is necessary only if using the client certificate authentication
 *   - {String|Buffer} [cert]: A string or Buffer containing the certificate key of the client in PEM format.
 *       Notes: This is necessary only if using the client certificate authentication
 *   - {String} [passphrase]: A string of passphrase for the private key or pfx.
 *   - {String} [ciphers]: A string describing the ciphers to use or exclude.
 *   - {String} [secureProtocol]: The SSL method to use, e.g. SSLv3_method to force SSL version 3.
 *       The possible values depend on your installation of OpenSSL and are defined in the constant SSL_METHODS.
 *   - {Boolean} [followRedirect]: Follow HTTP 3xx responses as redirects. defaults to false.
 *   - {Number} [maxRedirects]: The maximum number of redirects to follow, defaults to 10.
 *   - {Function(from, to)} [formatRedirectUrl]: Format the redirect url by your self. Default is `url.resolve(from, to)`
 *   - {Function(options)} [beforeRequest]: Before request hook, you can change every thing here.
 *   - {Boolean} [streaming]: let you get the res object when request connected, default is `false`. alias `customResponse`
 *   - {Boolean} [gzip]: Accept gzip response content and auto decode it, default is `false`.
 *   - {Boolean} [timing]: Enable timing or not, default is `false`.
 *   - {Function} [lookup]: Custom DNS lookup function, default is `dns.lookup`.
 *       Require node >= 4.0.0 and only work on `http` protocol.
 *   - {Boolean} [enableProxy]: optional, enable proxy request. Default is `false`.
 *   - {String|Object} [proxy]: optional proxy agent uri or options. Default is `null`.
 *   - {Function} checkAddress: optional, check request address to protect from SSRF and similar attacks.
 * @param {Function} [callback]: callback(error, data, res). If missing callback, will return a promise object.
 * @return {HttpRequest} req object.
 * @api public
 */
exports.request = function request(url, args, callback) {
  // request(url, callback)
  if (arguments.length === 2 && typeof args === 'function') {
    callback = args;
    args = null;
  }
  if (typeof callback === 'function') {
    return exports.requestWithCallback(url, args, callback);
  }

  // Promise
  if (!_Promise) {
    _Promise = require('any-promise');
  }
  return new _Promise(function (resolve, reject) {
    exports.requestWithCallback(url, args, makeCallback(resolve, reject));
  });
};

// alias to curl
exports.curl = exports.request;

function makeCallback(resolve, reject) {
  return function (err, data, res) {
    if (err) {
      return reject(err);
    }
    resolve({
      data: data,
      status: res.statusCode,
      headers: res.headers,
      res: res
    });
  };
}

// yield urllib.requestThunk(url, args)
exports.requestThunk = function requestThunk(url, args) {
  return function (callback) {
    exports.requestWithCallback(url, args, function (err, data, res) {
      if (err) {
        return callback(err);
      }
      callback(null, {
        data: data,
        status: res.statusCode,
        headers: res.headers,
        res: res
      });
    });
  };
};

function requestWithCallback(url, args, callback) {
  var req;
  // requestWithCallback(url, callback)
  if (!url || (typeof url !== 'string' && typeof url !== 'object')) {
    var msg = util.format('expect request url to be a string or a http request options, but got %j', url);
    throw new Error(msg);
  }

  if (arguments.length === 2 && typeof args === 'function') {
    callback = args;
    args = null;
  }

  args = args || {};
  if (REQUEST_ID >= MAX_VALUE) {
    REQUEST_ID = 0;
  }
  var reqId = ++REQUEST_ID;

  args.requestUrls = args.requestUrls || [];

  args.timeout = args.timeout || exports.TIMEOUTS;
  args.maxRedirects = args.maxRedirects || 10;
  args.streaming = args.streaming || args.customResponse;
  var requestStartTime = Date.now();
  var parsedUrl;

  if (typeof url === 'string') {
    if (!PROTO_RE.test(url)) {
      // Support `request('www.server.com')`
      url = 'http://' + url;
    }
    if (URL) {
      parsedUrl = urlutil.parse(new URL(url).href);
    } else {
      parsedUrl = urlutil.parse(url);
    }
  } else {
    parsedUrl = url;
  }

  var reqMeta = {
    requestId: reqId,
    url: parsedUrl.href,
    args: args,
    ctx: args.ctx,
  };
  if (args.emitter) {
    args.emitter.emit('request', reqMeta);
  }

  var method = (args.type || args.method || parsedUrl.method || 'GET').toUpperCase();
  var port = parsedUrl.port || 80;
  var httplib = http;
  var agent = getAgent(args.agent, exports.agent);
  var fixJSONCtlChars = args.fixJSONCtlChars;

  if (parsedUrl.protocol === 'https:') {
    httplib = https;
    agent = getAgent(args.httpsAgent, exports.httpsAgent);

    if (!parsedUrl.port) {
      port = 443;
    }
  }

  // request through proxy tunnel
  var proxyTunnelAgent = detectProxyAgent(parsedUrl, args);
  if (proxyTunnelAgent) {
    agent = proxyTunnelAgent;
  }

  var lookup = args.lookup;
  // check address to protect from SSRF and similar attacks
  if (args.checkAddress) {
    var _lookup = lookup || dns.lookup;
    lookup = function(host, dnsopts, callback) {
      _lookup(host, dnsopts, function emitLookup(err, ip, family) {
        // add check address logic in custom dns lookup
        if (!err && !args.checkAddress(ip, family)) {
          err = new Error('illegal address');
          err.name = 'IllegalAddressError';
          err.hostname = host;
          err.ip = ip;
          err.family = family;
        }
        callback(err, ip, family);
      });
    };
  }

  var requestSize = 0;
  var options = {
    host: parsedUrl.hostname || parsedUrl.host || 'localhost',
    path: parsedUrl.path || '/',
    method: method,
    port: port,
    agent: agent,
    headers: {},
    // default is dns.lookup
    // https://github.com/nodejs/node/blob/master/lib/net.js#L986
    // custom dnslookup require node >= 4.0.0 (for http), node >=8 (for https)
    // https://github.com/nodejs/node/blob/archived-io.js-v0.12/lib/net.js#L952
    lookup: lookup,
  };
  if (args.headers) {
    // only allow enumerable and ownProperty value of args.headers
    var names = utility.getOwnEnumerables(args.headers, true);
    for (var i = 0; i < names.length; i++) {
      var name = names[i];
      options.headers[name.toLowerCase()] = args.headers[name];
    }
  }

  var sslNames = [
    'pfx',
    'key',
    'passphrase',
    'cert',
    'ca',
    'ciphers',
    'rejectUnauthorized',
    'secureProtocol',
    'secureOptions',
  ];
  for (var i = 0; i < sslNames.length; i++) {
    var name = sslNames[i];
    if (args.hasOwnProperty(name)) {
      options[name] = args[name];
    }
  }

  // fix rejectUnauthorized when major version < 12
  if (NODE_MAJOR_VERSION < 12) {
    if (options.rejectUnauthorized === false && !options.hasOwnProperty('secureOptions')) {
      options.secureOptions = require('constants').SSL_OP_NO_TLSv1_2;
    }
  }

  var auth = args.auth || parsedUrl.auth;
  if (auth) {
    options.auth = auth;
  }

  var body = null;
  var dataAsQueryString = false;

  if (args.files) {
    if (!options.method || options.method === 'GET' || options.method === 'HEAD') {
      options.method = 'POST';
    }
    var files = args.files;
    var uploadFiles = [];
    if (Array.isArray(files)) {
      for (var i = 0; i < files.length; i++) {
        var field = 'file' + (i === 0 ? '' : i);
        uploadFiles.push([ field, files[i] ]);
      }
    } else {
      if (Buffer.isBuffer(files) || typeof files.pipe === 'function' || typeof files === 'string') {
        uploadFiles.push([ 'file', files ]);
      } else if (typeof files === 'object') {
        for (var field in files) {
          uploadFiles.push([ field, files[field] ]);
        }
      }
    }
    var form = new FormStream();
    // set normal fields first
    if (args.data) {
      for (var fieldName in args.data) {
        form.field(fieldName, args.data[fieldName]);
      }
    }

    for (var i = 0; i < uploadFiles.length; i++) {
      var item = uploadFiles[i];
      if (Buffer.isBuffer(item[1])) {
        form.buffer(item[0], item[1], 'bufferfile' + i);
      } else if (typeof item[1].pipe === 'function') {
        var filename = item[1].path || ('streamfile' + i);
        filename = path.basename(filename);
        form.stream(item[0], item[1], filename);
      } else {
        form.file(item[0], item[1]);
      }
    }

    var formHeaders = form.headers();
    var formHeaderNames = utility.getOwnEnumerables(formHeaders, true);
    for (var i = 0; i < formHeaderNames.length; i++) {
      var name = formHeaderNames[i];
      options.headers[name.toLowerCase()] = formHeaders[name];
    }
    debug('set multipart headers: %j, method: %s', formHeaders, options.method);
    args.stream = form;
  } else {
    body = args.content || args.data;
    dataAsQueryString = method === 'GET' || method === 'HEAD' || args.dataAsQueryString;
    if (!args.content) {
      if (body && !(typeof body === 'string' || Buffer.isBuffer(body))) {
        if (dataAsQueryString) {
          // read: GET, HEAD, use query string
          body = args.nestedQuerystring ? qs.stringify(body) : querystring.stringify(body);
        } else {
          var contentType = options.headers['content-type'];
          // auto add application/x-www-form-urlencoded when using urlencode form request
          if (!contentType) {
            if (args.contentType === 'json') {
              contentType = 'application/json';
            } else {
              contentType = 'application/x-www-form-urlencoded';
            }
            options.headers['content-type'] = contentType;
          }

          if (parseContentType(contentType).type === 'application/json') {
            body = JSON.stringify(body);
          } else {
            // 'application/x-www-form-urlencoded'
            body = args.nestedQuerystring ? qs.stringify(body) : querystring.stringify(body);
          }
        }
      }
    }
  }

  if (body) {
    // if it's a GET or HEAD request, data should be sent as query string
    if (dataAsQueryString) {
      options.path += (parsedUrl.query ? '&' : '?') + body;
      body = null;
    }

    if (body) {
      var length = body.length;
      if (!Buffer.isBuffer(body)) {
        length = Buffer.byteLength(body);
      }
      requestSize = length;

      options.headers['content-length'] = length.toString();
    }
  }

  if (args.dataType === 'json') {
    if (!options.headers.accept) {
      options.headers.accept = 'application/json';
    }
  }

  if (typeof args.beforeRequest === 'function') {
    // you can use this hook to change every thing.
    args.beforeRequest(options);
  }
  var connectTimer = null;
  var responseTimer = null;
  var __err = null;
  var connected = false; // socket connected or not
  var keepAliveSocket = false; // request with keepalive socket
  var socketHandledRequests = 0; // socket already handled request count
  var socketHandledResponses = 0; // socket already handled response count
  var responseSize = 0;
  var statusCode = -1;
  var statusMessage = null;
  var responseAborted = false;
  var remoteAddress = '';
  var remotePort = '';
  var timing = null;
  if (args.timing) {
    timing = {
      // socket assigned
      queuing: 0,
      // dns lookup time
      dnslookup: 0,
      // socket connected
      connected: 0,
      // request sent
      requestSent: 0,
      // Time to first byte (TTFB)
      waiting: 0,
      contentDownload: 0,
    };
  }

  function cancelConnectTimer() {
    if (connectTimer) {
      clearTimeout(connectTimer);
      connectTimer = null;
      debug('Request#%d connect timer canceled', reqId);
    }
  }
  function cancelResponseTimer() {
    if (responseTimer) {
      clearTimeout(responseTimer);
      responseTimer = null;
      debug('Request#%d response timer canceled', reqId);
    }
  }

  function done(err, data, res) {
    cancelConnectTimer();
    cancelResponseTimer();
    if (!callback) {
      console.warn('[urllib:warn] [%s] [%s] [worker:%s] %s %s callback twice!!!',
        Date(), reqId, process.pid, options.method, url);
      // https://github.com/node-modules/urllib/pull/30
      if (err) {
        console.warn('[urllib:warn] [%s] [%s] [worker:%s] %s: %s\nstack: %s',
          Date(), reqId, process.pid, err.name, err.message, err.stack);
      }
      return;
    }
    var cb = callback;
    callback = null;
    var headers = {};
    if (res) {
      statusCode = res.statusCode;
      statusMessage = res.statusMessage;
      headers = res.headers;
    }

    // handle digest auth
    if (statusCode === 401 && headers['www-authenticate']
        && !options.headers.authorization && args.digestAuth) {
      var authenticate = headers['www-authenticate'];
      if (authenticate.indexOf('Digest ') >= 0) {
        debug('Request#%d %s: got digest auth header WWW-Authenticate: %s', reqId, url, authenticate);
        options.headers.authorization = digestAuthHeader(options.method, options.path, authenticate, args.digestAuth);
        debug('Request#%d %s: auth with digest header: %s', reqId, url, options.headers.authorization);
        if (res.headers['set-cookie']) {
          options.headers.cookie = res.headers['set-cookie'].join(';');
        }
        args.headers = options.headers;
        return exports.requestWithCallback(url, args, cb);
      }
    }

    var requestUseTime = Date.now() - requestStartTime;
    if (timing) {
      timing.contentDownload = requestUseTime;
    }

    debug('[%sms] done, %s bytes HTTP %s %s %s %s, keepAliveSocket: %s, timing: %j, socketHandledRequests: %s, socketHandledResponses: %s',
      requestUseTime, responseSize, statusCode, options.method, options.host, options.path,
      keepAliveSocket, timing, socketHandledRequests, socketHandledResponses);

    var response = {
      status: statusCode,
      statusCode: statusCode,
      statusMessage: statusMessage,
      headers: headers,
      size: responseSize,
      aborted: responseAborted,
      rt: requestUseTime,
      keepAliveSocket: keepAliveSocket,
      data: data,
      requestUrls: args.requestUrls,
      timing: timing,
      remoteAddress: remoteAddress,
      remotePort: remotePort,
      socketHandledRequests: socketHandledRequests,
      socketHandledResponses: socketHandledResponses,
    };

    if (err) {
      var agentStatus = '';
      if (agent && typeof agent.getCurrentStatus === 'function') {
        // add current agent status to error message for logging and debug
        agentStatus = ', agent status: ' + JSON.stringify(agent.getCurrentStatus());
      }
      err.message += ', ' + options.method + ' ' + url + ' ' + statusCode
        + ' (connected: ' + connected + ', keepalive socket: ' + keepAliveSocket + agentStatus
        + ', socketHandledRequests: ' + socketHandledRequests
        + ', socketHandledResponses: ' + socketHandledResponses + ')'
        + '\nheaders: ' + JSON.stringify(headers);
      err.data = data;
      err.path = options.path;
      err.status = statusCode;
      err.headers = headers;
      err.res = response;
      addLongStackTrace(err, req);
    }

    // only support agentkeepalive module for now
    // agentkeepalive@4: agent.options.freeSocketTimeout
    // agentkeepalive@3: agent.freeSocketKeepAliveTimeout
    var freeSocketTimeout = agent && (agent.options && agent.options.freeSocketTimeout || agent.freeSocketKeepAliveTimeout);
    if (agent && agent.keepAlive && freeSocketTimeout > 0 &&
        statusCode >= 200 && headers.connection === 'keep-alive' && headers['keep-alive']) {
      // adjust freeSocketTimeout on the socket
      var m = KEEP_ALIVE_RE.exec(headers['keep-alive']);
      if (m) {
        var seconds = parseInt(m[1]);
        if (seconds > 0) {
          // network delay 500ms
          var serverSocketTimeout = seconds * 1000 - 500;
          if (serverSocketTimeout < freeSocketTimeout) {
            // https://github.com/node-modules/agentkeepalive/blob/master/lib/agent.js#L127
            // agentkeepalive@4
            var socket = res.socket || (req && req.socket);
            if (agent.options && agent.options.freeSocketTimeout) {
              socket.freeSocketTimeout = serverSocketTimeout;
            } else {
              socket.freeSocketKeepAliveTimeout = serverSocketTimeout;
            }
          }
        }
      }
    }

    cb(err, data, args.streaming ? res : response);

    if (args.emitter) {
      // keep to use the same reqMeta object on request event before
      reqMeta.url = parsedUrl.href;
      reqMeta.socket = req && req.connection;
      reqMeta.options = options;
      reqMeta.size = requestSize;

      args.emitter.emit('response', {
        requestId: reqId,
        error: err,
        ctx: args.ctx,
        req: reqMeta,
        res: response,
      });
    }
  }

  function handleRedirect(res) {
    var err = null;
    if (args.followRedirect && statuses.redirect[res.statusCode]) {  // handle redirect
      args._followRedirectCount = (args._followRedirectCount || 0) + 1;
      var location = res.headers.location;
      if (!location) {
        err = new Error('Got statusCode ' + res.statusCode + ' but cannot resolve next location from headers');
        err.name = 'FollowRedirectError';
      } else if (args._followRedirectCount > args.maxRedirects) {
        err = new Error('Exceeded maxRedirects. Probably stuck in a redirect loop ' + url);
        err.name = 'MaxRedirectError';
      } else {
        var newUrl = args.formatRedirectUrl ? args.formatRedirectUrl(url, location) : urlutil.resolve(url, location);
        debug('Request#%d %s: `redirected` from %s to %s', reqId, options.path, url, newUrl);
        // make sure timer stop
        cancelResponseTimer();
        // should clean up headers.host on `location: http://other-domain/url`
        if (options.headers.host && PROTO_RE.test(location)) {
          options.headers.host = null;
          args.headers = options.headers;
        }
        // avoid done will be execute in the future change.
        var cb = callback;
        callback = null;
        exports.requestWithCallback(newUrl, args, cb);
        return {
          redirect: true,
          error: null
        };
      }
    }
    return {
      redirect: false,
      error: err
    };
  }

  // don't set user-agent
  if (args.headers && (args.headers['User-Agent'] === null || args.headers['user-agent'] === null)) {
    if (options.headers['user-agent']) {
      delete options.headers['user-agent'];
    }
  } else {
    // need to set user-agent
    var hasAgentHeader = options.headers['user-agent'];
    if (!hasAgentHeader) {
      options.headers['user-agent'] = USER_AGENT;
    }
  }

  if (args.gzip) {
    var isAcceptEncodingNull = (args.headers && (args.headers['Accept-Encoding'] === null || args.headers['accept-encoding'] === null));
    if (!isAcceptEncodingNull) {
      var hasAcceptEncodingHeader = options.headers['accept-encoding'];
      if (!hasAcceptEncodingHeader) {
        options.headers['accept-encoding'] = 'gzip, deflate';
      }
    }
  }

  function decodeContent(res, body, cb) {
    var encoding = res.headers['content-encoding'];
    if (body.length === 0 || !encoding) {
      return cb(null, body, encoding);
    }

    encoding = encoding.toLowerCase();
    switch (encoding) {
      case 'gzip':
      case 'deflate':
        debug('unzip %d length body', body.length);
        zlib.unzip(body, function(err, data) {
          if (err && err.name === 'Error') {
            err.name = 'UnzipError';
          }
          cb(err, data);
        });
        break;
      default:
        cb(null, body, encoding);
    }
  }

  var writeStream = args.writeStream;
  var isWriteStreamClose = false;

  debug('Request#%d %s %s with headers %j, options.path: %s',
    reqId, method, url, options.headers, options.path);

  args.requestUrls.push(parsedUrl.href);

  function onResponse(res) {
    socketHandledResponses = res.socket[SOCKET_RESPONSE_COUNT] = (res.socket[SOCKET_RESPONSE_COUNT] || 0) + 1;
    if (timing) {
      timing.waiting = Date.now() - requestStartTime;
    }
    debug('Request#%d %s `req response` event emit: status %d, headers: %j',
      reqId, url, res.statusCode, res.headers);

    if (args.streaming) {
      var result = handleRedirect(res);
      if (result.redirect) {
        res.resume();
        return;
      }
      if (result.error) {
        res.resume();
        return done(result.error, null, res);
      }

      return done(null, null, res);
    }

    res.on('error', function () {
      debug('Request#%d %s: `res error` event emit, total size %d, socket handled %s requests and %s responses',
        reqId, url, responseSize, socketHandledRequests, socketHandledResponses);
    });

    res.on('aborted', function () {
      responseAborted = true;
      debug('Request#%d %s: `res aborted` event emit, total size %d',
        reqId, url, responseSize);
    });

    if (writeStream) {
      // If there's a writable stream to recieve the response data, just pipe the
      // response stream to that writable stream and call the callback when it has
      // finished writing.
      //
      // NOTE that when the response stream `res` emits an 'end' event it just
      // means that it has finished piping data to another stream. In the
      // meanwhile that writable stream may still writing data to the disk until
      // it emits a 'close' event.
      //
      // That means that we should not apply callback until the 'close' of the
      // writable stream is emited.
      //
      // See also:
      // - https://github.com/TBEDP/urllib/commit/959ac3365821e0e028c231a5e8efca6af410eabb
      // - http://nodejs.org/api/stream.html#stream_event_end
      // - http://nodejs.org/api/stream.html#stream_event_close_1
      var result = handleRedirect(res);
      if (result.redirect) {
        res.resume();
        return;
      }
      if (result.error) {
        res.resume();
        // end ths stream first
        writeStream.end();
        done(result.error, null, res);
        return;
      }

      // you can set consumeWriteStream false that only wait response end
      if (args.consumeWriteStream === false) {
        res.on('end', done.bind(null, null, null, res));
        pump(res, writeStream, function(err) {
          if (isWriteStreamClose) {
            return;
          }
          isWriteStreamClose = true;
          debug('Request#%d %s: writeStream close, error: %s', reqId, url, err);
        });
        return;
      }

      // node 0.10, 0.12: only emit res aborted, writeStream close not fired
      if (isNode010 || isNode012) {
        first([
          [ writeStream, 'close' ],
          [ res, 'aborted' ],
        ], function(_, stream, event) {
          debug('Request#%d %s: writeStream or res %s event emitted', reqId, url, event);
          done(__err || null, null, res);
        });
        res.pipe(writeStream);
        return;
      }

      debug('Request#%d %s: pump res to writeStream', reqId, url);
      pump(res, writeStream, function(err) {
        debug('Request#%d %s: writeStream close event emitted, error: %s, isWriteStreamClose: %s',
          reqId, url, err, isWriteStreamClose);
        if (isWriteStreamClose) {
          return;
        }
        isWriteStreamClose = true;
        done(__err || err, null, res);
      });
      return;
    }

    // Otherwise, just concat those buffers.
    //
    // NOTE that the `chunk` is not a String but a Buffer. It means that if
    // you simply concat two chunk with `+` you're actually converting both
    // Buffers into Strings before concating them. It'll cause problems when
    // dealing with multi-byte characters.
    //
    // The solution is to store each chunk in an array and concat them with
    // 'buffer-concat' when all chunks is recieved.
    //
    // See also:
    // http://cnodejs.org/topic/4faf65852e8fb5bc65113403

    var chunks = [];

    res.on('data', function (chunk) {
      debug('Request#%d %s: `res data` event emit, size %d', reqId, url, chunk.length);
      responseSize += chunk.length;
      chunks.push(chunk);
    });

    var isEmitted = false;
    function handleResponseCloseAndEnd(event) {
      debug('Request#%d %s: `res %s` event emit, total size %d, socket handled %s requests and %s responses',
        reqId, url, event, responseSize, socketHandledRequests, socketHandledResponses);
      if (isEmitted) {
        return;
      }
      isEmitted = true;

      var body = Buffer.concat(chunks, responseSize);
      debug('Request#%d %s: _dumped: %s',
        reqId, url, res._dumped);

      if (__err) {
        // req.abort() after `res data` event emit.
        return done(__err, body, res);
      }

      var result = handleRedirect(res);
      if (result.error) {
        return done(result.error, body, res);
      }
      if (result.redirect) {
        return;
      }

      decodeContent(res, body, function (err, data, encoding) {
        if (err) {
          return done(err, body, res);
        }
        // if body not decode, dont touch it
        if (!encoding && TEXT_DATA_TYPES.indexOf(args.dataType) >= 0) {
          // try to decode charset
          try {
            data = decodeBodyByCharset(data, res);
          } catch (e) {
            debug('decodeBodyByCharset error: %s', e);
            // if error, dont touch it
            return done(null, data, res);
          }

          if (args.dataType === 'json') {
            if (responseSize === 0) {
              data = null;
            } else {
              var r = parseJSON(data, fixJSONCtlChars);
              if (r.error) {
                err = r.error;
              } else {
                data = r.data;
              }
            }
          }
        }

        if (responseAborted) {
          // err = new Error('Remote socket was terminated before `response.end()` was called');
          // err.name = 'RemoteSocketClosedError';
          debug('Request#%d %s: Remote socket was terminated before `response.end()` was called', reqId, url);
        }

        done(err, data, res);
      });
    }

    // node >= 14 only emit close if req abort
    res.on('close', function () {
      handleResponseCloseAndEnd('close');
    });
    res.on('end', function () {
      handleResponseCloseAndEnd('end');
    });
  }

  var connectTimeout, responseTimeout;
  if (Array.isArray(args.timeout)) {
    connectTimeout = ms(args.timeout[0]);
    responseTimeout = ms(args.timeout[1]);
  } else {  // set both timeout equal
    connectTimeout = responseTimeout = ms(args.timeout);
  }
  debug('ConnectTimeout: %d, ResponseTimeout: %d', connectTimeout, responseTimeout);

  function startConnectTimer() {
    debug('Connect timer ticking, timeout: %d', connectTimeout);
    connectTimer = setTimeout(function () {
      connectTimer = null;
      if (statusCode === -1) {
        statusCode = -2;
      }
      var msg = 'Connect timeout for ' + connectTimeout + 'ms';
      var errorName = 'ConnectionTimeoutError';
      if (!req.socket) {
        errorName = 'SocketAssignTimeoutError';
        msg += ', working sockets is full';
      }
      __err = new Error(msg);
      __err.name = errorName;
      __err.requestId = reqId;
      debug('ConnectTimeout: Request#%d %s %s: %s, connected: %s', reqId, url, __err.name, msg, connected);
      abortRequest();
    }, connectTimeout);
  }

  function startResposneTimer() {
    debug('Response timer ticking, timeout: %d', responseTimeout);
    responseTimer = setTimeout(function () {
      responseTimer = null;
      var msg = 'Response timeout for ' + responseTimeout + 'ms';
      var errorName = 'ResponseTimeoutError';
      __err = new Error(msg);
      __err.name = errorName;
      __err.requestId = reqId;
      debug('ResponseTimeout: Request#%d %s %s: %s, connected: %s', reqId, url, __err.name, msg, connected);
      abortRequest();
    }, responseTimeout);
  }

  if (args.checkAddress) {
    var hostname = parsedUrl.hostname;
    // if request hostname is ip, custom lookup wont excute
    var family = null;
    if (ip.isV4Format(hostname)) {
      family = 4;
    } else if (ip.isV6Format(hostname)) {
      family = 6;
    }
    if (family) {
      if (!args.checkAddress(hostname, family)) {
        var err = new Error('illegal address');
        err.name = 'IllegalAddressError';
        err.hostname = hostname;
        err.ip = hostname;
        err.family = family;
        return done(err);
      }
    }
  }

  // request headers checker will throw error
  try {
    req = httplib.request(options, onResponse);
    if (args.trace) {
      req._callSite = {};
      Error.captureStackTrace(req._callSite, requestWithCallback);
    }
  } catch (err) {
    return done(err);
  }

  // environment detection: browser or nodejs
  if (typeof(window) === 'undefined') {
    // start connect timer just after `request` return, and just in nodejs environment
    startConnectTimer();
  }

  var isRequestAborted = false;
  function abortRequest() {
    if (isRequestAborted) {
      return;
    }
    isRequestAborted = true;

    debug('Request#%d %s abort, connected: %s', reqId, url, connected);
    // it wont case error event when req haven't been assigned a socket yet.
    if (!req.socket) {
      __err.noSocket = true;
      done(__err);
    }
    req.abort();
  }

  if (timing) {
    // request sent
    req.on('finish', function() {
      timing.requestSent = Date.now() - requestStartTime;
    });
  }

  req.once('socket', function (socket) {
    if (timing) {
      // socket queuing time
      timing.queuing = Date.now() - requestStartTime;
    }

    // https://github.com/nodejs/node/blob/master/lib/net.js#L377
    // https://github.com/nodejs/node/blob/v0.10.40-release/lib/net.js#L352
    // should use socket.socket on 0.10.x
    if (isNode010 && socket.socket) {
      socket = socket.socket;
    }

    var orginalSocketTimeout = getSocketTimeout(socket);
    if (orginalSocketTimeout && orginalSocketTimeout < responseTimeout) {
      // make sure socket live longer than the response timer
      var socketTimeout = responseTimeout + 500;
      debug('Request#%d socket.timeout(%s) < responseTimeout(%s), reset socket timeout to %s',
        reqId, orginalSocketTimeout, responseTimeout, socketTimeout);
      socket.setTimeout(socketTimeout);
    }

    socketHandledRequests = socket[SOCKET_REQUEST_COUNT] = (socket[SOCKET_REQUEST_COUNT] || 0) + 1;
    if (socket[SOCKET_RESPONSE_COUNT]) {
      socketHandledResponses = socket[SOCKET_RESPONSE_COUNT];
    }

    var readyState = socket.readyState;
    if (readyState === 'opening') {
      socket.once('lookup', function(err, ip, addressType) {
        debug('Request#%d %s lookup: %s, %s, %s', reqId, url, err, ip, addressType);
        if (timing) {
          timing.dnslookup = Date.now() - requestStartTime;
        }
        if (ip) {
          remoteAddress = ip;
        }
      });
      socket.once('connect', function() {
        if (timing) {
          // socket connected
          timing.connected = Date.now() - requestStartTime;
        }

        // cancel socket timer at first and start tick for TTFB
        cancelConnectTimer();
        startResposneTimer();

        debug('Request#%d %s new socket connected', reqId, url);
        connected = true;
        if (!remoteAddress) {
          remoteAddress = socket.remoteAddress;
        }
        remotePort = socket.remotePort;
      });
      return;
    }

    debug('Request#%d %s reuse socket connected, readyState: %s', reqId, url, readyState);
    connected = true;
    keepAliveSocket = true;
    if (!remoteAddress) {
      remoteAddress = socket.remoteAddress;
    }
    remotePort = socket.remotePort;

    // reuse socket, timer should be canceled.
    cancelConnectTimer();
    startResposneTimer();
  });

  if (writeStream) {
    writeStream.once('error', function(err) {
      err.message += ' (writeStream "error")';
      __err = err;
      debug('Request#%d %s `writeStream error` event emit, %s: %s', reqId, url, err.name, err.message);
      abortRequest();
    });
  }

  var isRequestError = false;
  function handleRequestError(err) {
    if (isRequestError || !err) {
      return;
    }
    isRequestError = true;

    if (err.name === 'Error') {
      err.name = connected ? 'ResponseError' : 'RequestError';
    }
    debug('Request#%d %s `req error` event emit, %s: %s', reqId, url, err.name, err.message);
    done(__err || err);
  }
  if (args.stream) {
    debug('Request#%d pump args.stream to req', reqId);
    pump(args.stream, req, handleRequestError);
  } else {
    req.end(body);
  }
  // when stream already consumed, req's `finish` event is emitted and pump will ignore error after pipe finished
  // but if server response timeout later, we will abort the request and emit an error in req
  // so we must always manually listen to req's `error` event here to ensure this error is handled
  req.on('error', handleRequestError);
  req.requestId = reqId;
  return req;
}

exports.requestWithCallback = requestWithCallback;

var JSONCtlCharsMap = {
  '"': '\\"',       // \u0022
  '\\': '\\\\',     // \u005c
  '\b': '\\b',      // \u0008
  '\f': '\\f',      // \u000c
  '\n': '\\n',      // \u000a
  '\r': '\\r',      // \u000d
  '\t': '\\t'       // \u0009
};
var JSONCtlCharsRE = /[\u0000-\u001F\u005C]/g;

function _replaceOneChar(c) {
  return JSONCtlCharsMap[c] || '\\u' + (c.charCodeAt(0) + 0x10000).toString(16).substr(1);
}

function replaceJSONCtlChars(str) {
  return str.replace(JSONCtlCharsRE, _replaceOneChar);
}

function parseJSON(data, fixJSONCtlChars) {
  var result = {
    error: null,
    data: null
  };
  if (fixJSONCtlChars) {
    if (typeof fixJSONCtlChars === 'function') {
      data = fixJSONCtlChars(data);
    } else {
      // https://github.com/node-modules/urllib/pull/77
      // remote the control characters (U+0000 through U+001F)
      data = replaceJSONCtlChars(data);
    }
  }
  try {
    result.data = JSON.parse(data);
  } catch (err) {
    if (err.name === 'SyntaxError') {
      err.name = 'JSONResponseFormatError';
    }
    if (data.length > 1024) {
      // show 0~512 ... -512~end data
      err.message += ' (data json format: ' +
        JSON.stringify(data.slice(0, 512)) + ' ...skip... ' + JSON.stringify(data.slice(data.length - 512)) + ')';
    } else {
      err.message += ' (data json format: ' + JSON.stringify(data) + ')';
    }
    result.error = err;
  }
  return result;
}


/**
 * decode response body by parse `content-type`'s charset
 * @param {Buffer} data
 * @param {Http(s)Response} res
 * @return {String}
 */
function decodeBodyByCharset(data, res) {
  var type = res.headers['content-type'];
  if (!type) {
    return data.toString();
  }

  var type = parseContentType(type);
  var charset = type.parameters.charset || 'utf-8';

  if (!Buffer.isEncoding(charset)) {
    if (!_iconv) {
      _iconv = require('iconv-lite');
    }
    return _iconv.decode(data, charset);
  }

  return data.toString(charset);
}

function getAgent(agent, defaultAgent) {
  return agent === undefined ? defaultAgent : agent;
}

function parseContentType(str) {
  try {
    return contentTypeParser.parse(str);
  } catch (err) {
    // ignore content-type error, tread as default
    return { parameters: {} };
  }
}

function addLongStackTrace(err, req) {
  if (!req) {
    return;
  }
  var callSiteStack = req._callSite && req._callSite.stack;
  if (!callSiteStack || typeof callSiteStack !== 'string') {
    return;
  }
  if (err._longStack) {
    return;
  }
  var index = callSiteStack.indexOf('\n');
  if (index !== -1) {
    err._longStack = true;
    err.stack += LONG_STACK_DELIMITER + callSiteStack.substr(index + 1);
  }
}

// node 8 don't has timeout attribute on socket
// https://github.com/nodejs/node/pull/21204/files#diff-e6ef024c3775d787c38487a6309e491dR408
function getSocketTimeout(socket) {
  return socket.timeout || socket._idleTimeout;
}
