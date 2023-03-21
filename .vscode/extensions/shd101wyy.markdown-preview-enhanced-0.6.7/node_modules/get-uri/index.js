'use strict';

/**
 * Module dependencies.
 */

var parse = require('url').parse;
var debug = require('debug')('get-uri');

/**
 * Module exports.
 */

module.exports = exports = getUri;

/**
 * Supported "protocols".
 */

exports.protocols = {
  data: require('./data'),
  file: require('./file'),
  ftp: require('./ftp'),
  http: require('./http'),
  https: require('./https')
};

/**
 * Async function that returns a `stream.Readable` instance to the
 * callback function that will output the contents of the given URI.
 *
 * For caching purposes, you can pass in a `stream` instance from a previous
 * `getUri()` call as a `cache: stream` option, and if the destination has
 * not changed since the last time the endpoint was retreived then the callback
 * will be invoked with an Error object with `code` set to "ENOTMODIFIED" and
 * `null` for the "stream" instance argument. In this case, you can skip
 * retreiving the file again and continue to use the previous payload.
 *
 * @param {String} uri URI to retrieve
 * @param {Object} opts optional "options" object
 * @param {Function} fn callback function
 * @api public
 */

function getUri (uri, opts, fn) {
  debug('getUri(%o)', uri);

  if ('function' == typeof opts) {
    fn = opts;
    opts = null;
  }
  if ('function' != typeof fn) {
    throw new TypeError('a callback function must be provided');
  }

  if (!uri) return fn(new TypeError('must pass in a URI to "get"'));

  var parsed = parse(uri);
  var protocol = parsed.protocol;
  if (!protocol) return fn(new TypeError('URI does not contain a protocol: ' + uri));

  // strip trailing :
  protocol = protocol.replace(/\:$/, '');

  var getter = exports.protocols[protocol];

  if ('function' != typeof getter)
    return fn(new TypeError('unsupported protocol "' + protocol + '" specified in URI: ' + uri));

  getter(parsed, opts || {}, fn);
}
