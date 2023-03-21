
/**
 * Module exports.
 */

module.exports = localHostOrDomainIs;

/**
 * Is true if the hostname matches exactly the specified hostname, or if there is
 * no domain name part in the hostname, but the unqualified hostname matches.
 *
 * Examples:
 *
 * ``` js
 * localHostOrDomainIs("www.netscape.com", "www.netscape.com")
 *   // is true (exact match).
 *
 * localHostOrDomainIs("www", "www.netscape.com")
 *   // is true (hostname match, domain not specified).
 *
 * localHostOrDomainIs("www.mcom.com", "www.netscape.com")
 *   // is false (domain name mismatch).
 *
 * localHostOrDomainIs("home.netscape.com", "www.netscape.com")
 *   // is false (hostname mismatch).
 * ```
 *
 * @param {String} host the hostname from the URL.
 * @param {String} hostdom fully qualified hostname to match against.
 * @return {Boolean}
 */

function localHostOrDomainIs (host, hostdom) {
  var parts = String(host).split('.');
  var domparts = String(hostdom).split('.');
  var matches = true;

  for (var i = 0; i < parts.length; i++) {
    if (parts[i] !== domparts[i]) {
      matches = false;
      break;
    }
  }

  return matches;
}
