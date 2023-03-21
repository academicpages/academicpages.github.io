
/**
 * Module dependencies.
 */

var crypto = require('crypto');
var Readable = require('readable-stream');;
var dataUriToBuffer = require('data-uri-to-buffer');
var NotModifiedError = require('./notmodified');
var debug = require('debug')('get-uri:data');

/**
 * Module exports.
 */

module.exports = get;

/**
 * Returns a Readable stream from a "data:" URI.
 *
 * @api protected
 */

function get (parsed, opts, fn) {
  var uri = parsed.href;
  var cache = opts.cache;

  // need to create a SHA1 hash of the URI string, for cacheability checks
  // in future `getUri()` calls with the same data URI passed in.
  var shasum = crypto.createHash('sha1');
  shasum.update(uri);
  var hash = shasum.digest('hex');
  debug('generated SHA1 hash for "data:" URI: %o', hash);

  // check if the cache is the same "data:" URI that was previously passed in.
  if (cache && cache.hash == hash) {
    debug('got matching cache SHA1 hash: %o', hash);
    fn(new NotModifiedError());
  } else {
    debug('creating Readable stream from "data:" URI buffer');
    var buf = dataUriToBuffer(uri, opts);
    var rs = new Readable();
    rs._read = read(buf);
    buf = null;
    rs.hash = hash;
    fn(null, rs);
  }
}

/**
 * Function that returns a Readable `_read` function implementation.
 *
 * @api private
 */

function read (buf) {
  return function (n) {
    this.push(buf);
    this.push(null);
    buf = null;
  };
}
