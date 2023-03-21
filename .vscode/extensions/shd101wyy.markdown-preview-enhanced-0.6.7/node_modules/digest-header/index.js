/**!
 * digest-header - index.js
 *
 * Copyright(c) fengmk2 and other contributors.
 * MIT Licensed
 *
 * Authors:
 *   fengmk2 <fengmk2@gmail.com> (http://fengmk2.github.com)
 */

'use strict';

/**
 * Module dependencies.
 */

var crypto = require('crypto');
var utility = require('utility');

var AUTH_KEY_VALUE_RE = /(\w+)=["']?([^'"]+)["']?/;
var NC = 0;
var NC_PAD = '00000000';

function digestAuthHeader(method, uri, wwwAuthenticate, userpass) {
  var parts = wwwAuthenticate.split(',');
  var opts = {};
  for (var i = 0; i < parts.length; i++) {
    var m = parts[i].match(AUTH_KEY_VALUE_RE);
    if (m) {
      opts[m[1]] = m[2].replace(/["']/g, '');
    }
  }

  if (!opts.realm || !opts.nonce) {
    return '';
  }

  var qop = opts.qop || '';

  // WWW-Authenticate: Digest realm="testrealm@host.com",
  //                       qop="auth,auth-int",
  //                       nonce="dcd98b7102dd2f0e8b11d0f600bfb0c093",
  //                       opaque="5ccc069c403ebaf9f0171e9517f40e41"
  // Authorization: Digest username="Mufasa",
  //                    realm="testrealm@host.com",
  //                    nonce="dcd98b7102dd2f0e8b11d0f600bfb0c093",
  //                    uri="/dir/index.html",
  //                    qop=auth,
  //                    nc=00000001,
  //                    cnonce="0a4f113b",
  //                    response="6629fae49393a05397450978507c4ef1",
  //                    opaque="5ccc069c403ebaf9f0171e9517f40e41"
  // HA1 = MD5( "Mufasa:testrealm@host.com:Circle Of Life" )
  //      = 939e7578ed9e3c518a452acee763bce9
  //
  //  HA2 = MD5( "GET:/dir/index.html" )
  //      = 39aff3a2bab6126f332b942af96d3366
  //
  //  Response = MD5( "939e7578ed9e3c518a452acee763bce9:\
  //                   dcd98b7102dd2f0e8b11d0f600bfb0c093:\
  //                   00000001:0a4f113b:auth:\
  //                   39aff3a2bab6126f332b942af96d3366" )
  //           = 6629fae49393a05397450978507c4ef1
  userpass = userpass.split(':');

  var nc = String(++NC);
  nc = NC_PAD.substring(nc.length) + nc;
  var cnonce = crypto.randomBytes(8).toString('hex');

  var ha1 = utility.md5(userpass[0] + ':' + opts.realm + ':' + userpass[1]);
  var ha2 = utility.md5(method.toUpperCase() + ':' + uri);
  var s = ha1 + ':' + opts.nonce;
  if (qop) {
    qop = qop.split(',')[0];
    s += ':' + nc + ':' + cnonce + ':' + qop;
  }
  s += ':' + ha2;
  var response = utility.md5(s);
  var authstring = 'Digest username="' + userpass[0] + '", realm="' + opts.realm
    + '", nonce="' + opts.nonce + '", uri="' + uri
    + '", response="' + response + '"';
  if (opts.opaque) {
    authstring += ', opaque="' + opts.opaque + '"';
  }
  if (qop) {
    authstring +=', qop=' + qop + ', nc=' + nc + ', cnonce="' + cnonce + '"';
  }
  return authstring;
}

module.exports = digestAuthHeader;
