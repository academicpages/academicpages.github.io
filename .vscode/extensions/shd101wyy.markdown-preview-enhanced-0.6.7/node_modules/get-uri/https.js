
/**
 * Module dependencies.
 */

var http = require('./http');
var https = require('https');

/**
 * Module exports.
 */

module.exports = get;

/**
 * Returns a Readable stream from an "https:" URI.
 *
 * @api protected
 */

function get (parsed, opts, fn) {
  opts.http = https;
  http(parsed, opts, fn);
}
