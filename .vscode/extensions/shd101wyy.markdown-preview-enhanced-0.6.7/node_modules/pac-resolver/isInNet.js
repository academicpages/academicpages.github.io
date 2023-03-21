
/**
 * Module dependencies.
 */

var dns = require('dns');
var Netmask = require('netmask').Netmask;

/**
 * Module exports.
 */

module.exports = isInNet;

isInNet.async = true;

/**
 * True iff the IP address of the host matches the specified IP address pattern.
 *
 * Pattern and mask specification is done the same way as for SOCKS configuration.
 *
 * Examples:
 *
 * ``` js
 * isInNet(host, "198.95.249.79", "255.255.255.255")
 *   // is true iff the IP address of host matches exactly 198.95.249.79.
 *
 * isInNet(host, "198.95.0.0", "255.255.0.0")
 *   // is true iff the IP address of the host matches 198.95.*.*.
 * ```
 *
 * @param {String} host a DNS hostname, or IP address. If a hostname is passed,
 *   it will be resoved into an IP address by this function.
 * @param {String} pattern an IP address pattern in the dot-separated format mask.
 * @param {String} mask for the IP address pattern informing which parts of the
 *   IP address should be matched against. 0 means ignore, 255 means match.
 * @return {Boolean}
 */

function isInNet (host, pattern, mask, fn) {
  var family = 4;
  dns.lookup(host, family, function (err, ip) {
    if (err) return fn(err);
    if (!ip) ip = '127.0.0.1';
    var netmask = new Netmask(pattern, mask);
    fn(null, netmask.contains(ip));
  });
}
