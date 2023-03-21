'use strict';

/**
 * Module exports.
 */

module.exports = exports = PacProxyAgent;

/**
 * Supported "protocols". Delegates out to the `get-uri` module.
 */

var getUri = require('get-uri');
Object.defineProperty(exports, 'protocols', {
  enumerable: true,
  configurable: true,
  get: function () { return Object.keys(getUri.protocols); }
});

/**
 * Module dependencies.
 */

var net = require('net');
var tls = require('tls');
var crypto = require('crypto');
var parse = require('url').parse;
var format = require('url').format;
var Agent = require('agent-base');
var HttpProxyAgent = require('http-proxy-agent');
var HttpsProxyAgent = require('https-proxy-agent');
var SocksProxyAgent = require('socks-proxy-agent');
var PacResolver = require('pac-resolver');
var getRawBody = require('raw-body');
var inherits = require('util').inherits;
var debug = require('debug')('pac-proxy-agent');

/**
 * The `PacProxyAgent` class.
 *
 * A few different "protocol" modes are supported (supported protocols are
 * backed by the `get-uri` module):
 *
 *   - "pac+data", "data" - refers to an embedded "data:" URI
 *   - "pac+file", "file" - refers to a local file
 *   - "pac+ftp", "ftp" - refers to a file located on an FTP server
 *   - "pac+http", "http" - refers to an HTTP endpoint
 *   - "pac+https", "https" - refers to an HTTPS endpoint
 *
 * @api public
 */

function PacProxyAgent (uri, opts) {
  if (!(this instanceof PacProxyAgent)) return new PacProxyAgent(uri, opts);

  // was an options object passed in first?
  if ('object' === typeof uri) {
    opts = uri;

    // result of a url.parse() call?
    if (opts.href) {
      if (opts.path && !opts.pathname) {
        opts.pathname = opts.path;
      }
      opts.slashes = true;
      uri = format(opts);
    } else {
      uri = opts.uri;
    }
  }
  if (!opts) opts = {};

  if (!uri) throw new Error('a PAC file URI must be specified!');
  debug('creating PacProxyAgent with URI %o and options %o', uri, opts);

  Agent.call(this, connect);

  // strip the "pac+" prefix
  this.uri = uri.replace(/^pac\+/i, '');

  this.sandbox = opts.sandbox;

  this.proxy = opts;

  this.cache = this._resolver = null;
}
inherits(PacProxyAgent, Agent);

/**
 * Loads the PAC proxy file from the source if necessary, and returns
 * a generated `FindProxyForURL()` resolver function to use.
 *
 * @param {Function} fn callback function
 * @api private
 */

PacProxyAgent.prototype.loadResolver = function (fn) {
  var self = this;

  // kick things off by attempting to (re)load the contents of the PAC file URI
  this.loadPacFile(onpacfile);

  // loadPacFile() callback function
  function onpacfile (err, code) {
    if (err) {
      if ('ENOTMODIFIED' == err.code) {
        debug('got ENOTMODIFIED response, reusing previous proxy resolver');
        fn(null, self._resolver);
      } else {
        fn(err);
      }
      return;
    }

    // create a sha1 hash of the JS code
    var hash = crypto.createHash('sha1').update(code).digest('hex');

    if (self._resolver && self._resolver.hash == hash) {
      debug('same sha1 hash for code - contents have not changed, reusing previous proxy resolver');
      fn(null, self._resolver);
      return;
    }

    // cache the resolver
    debug('creating new proxy resolver instance');
    self._resolver = new PacResolver(code, {
      filename: self.uri,
      sandbox: self.sandbox
    });

    // store that sha1 hash on the resolver instance
    // for future comparison purposes
    self._resolver.hash = hash;

    fn(null, self._resolver);
  }
};

/**
 * Loads the contents of the PAC proxy file.
 *
 * @param {Function} fn callback function
 * @api private
 */

PacProxyAgent.prototype.loadPacFile = function (fn) {
  debug('loading PAC file: %o', this.uri);
  var self = this;

  // delegate out to the `get-uri` module
  var opts = {};
  if (this.cache) {
    opts.cache = this.cache;
  }
  getUri(this.uri, opts, onstream);

  function onstream (err, rs) {
    if (err) return fn(err);
    debug('got stream.Readable instance for URI');
    self.cache = rs;
    getRawBody(rs, 'utf8', onbuffer);
  }

  function onbuffer (err, buf) {
    if (err) return fn(err);
    debug('read %o byte PAC file from URI', buf.length);
    fn(null, buf);
  }
};

/**
 * Called when the node-core HTTP client library is creating a new HTTP request.
 *
 * @api public
 */

function connect (req, opts, fn) {
  var url;
  var host;
  var self = this;
  var secure = Boolean(opts.secureEndpoint);

  // first we need get a generated FindProxyForURL() function,
  // either cached or retreived from the source
  this.loadResolver(onresolver);

  // `loadResolver()` callback function
  function onresolver (err, FindProxyForURL) {
    if (err) return fn(err);

    // calculate the `url` parameter
    var defaultPort = secure ? 443 : 80;
    var path = req.path;
    var firstQuestion = path.indexOf('?');
    var search;
    if (-1 != firstQuestion) {
      search = path.substring(firstQuestion);
      path = path.substring(0, firstQuestion);
    }
    url = format(Object.assign({}, opts, {
      protocol: secure ? 'https:' : 'http:',
      pathname: path,
      search: search,

      // need to use `hostname` instead of `host` otherwise `port` is ignored
      hostname: opts.host,
      host: null,

      // set `port` to null when it is the protocol default port (80 / 443)
      port: defaultPort == opts.port ? null : opts.port
    }));

    // calculate the `host` parameter
    host = parse(url).hostname;

    debug('url: %o, host: %o', url, host);
    FindProxyForURL(url, host, onproxy);
  }

  // `FindProxyForURL()` callback function
  function onproxy (err, proxy) {
    if (err) return fn(err);

    // default to "DIRECT" if a falsey value was returned (or nothing)
    if (!proxy) proxy = 'DIRECT';

    var proxies = String(proxy).trim().split(/\s*;\s*/g).filter(Boolean);

    // XXX: right now, only the first proxy specified will be used
    var first = proxies[0];
    debug('using proxy: %o', first);

    var agent;
    var parts = first.split(/\s+/);
    var type = parts[0];

    if ('DIRECT' == type) {
      // direct connection to the destination endpoint
      var socket;
      if (secure) {
        socket = tls.connect(opts);
      } else {
        socket = net.connect(opts);
      }
      return fn(null, socket);
    } else if ('SOCKS' == type) {
      // use a SOCKS proxy
      agent = new SocksProxyAgent('socks://' + parts[1]);
    } else if ('PROXY' == type || 'HTTPS' == type) {
      // use an HTTP or HTTPS proxy
      // http://dev.chromium.org/developers/design-documents/secure-web-proxy
      var proxyURL = ('HTTPS' === type ? 'https' : 'http') + '://' + parts[1];
      var proxy = Object.assign({}, self.proxy, parse(proxyURL));
      if (secure) {
        agent = new HttpsProxyAgent(proxy);
      } else {
        agent = new HttpProxyAgent(proxy);
      }
    } else {
      throw new Error('Unknown proxy type: ' + type);
    }
    if (agent) agent.callback(req, opts, fn);
  }
}
