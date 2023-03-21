
/**
 * Module dependencies.
 */

var dns = require('dns');

/**
 * Module exports.
 */

module.exports = isResolvable;

isResolvable.async = true;

/**
 * Tries to resolve the hostname. Returns true if succeeds.
 *
 * @param {String} host is the hostname from the URL.
 * @return {Boolean}
 */

function isResolvable (host, fn) {
  var family = 4;
  dns.lookup(host, family, function (err, ip) {
    fn(null, !err);
  });
}
