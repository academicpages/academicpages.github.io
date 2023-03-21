/*!
 * utility - lib/utility.js
 *
 * Copyright(c) 2012 - 2013 fengmk2 <fengmk2@gmail.com>
 * MIT Licensed
 */

"use strict";

/**
 * Module dependencies.
 */

var crypto = require('crypto');
var address = require('address');

/**
 * A empty function.
 *
 * @return {Function}
 * @public
 */
exports.noop = function () {};

function sortObject(o) {
  if (!o || Array.isArray(o) || typeof o !== 'object') {
    return o;
  }
  var keys = Object.keys(o);
  keys.sort();
  var values = [];
  for (var i = 0; i < keys.length; i++) {
    var k = keys[i];
    values.push([k, sortObject(o[k])]);
  }
  return values;
}

/**
 * hash
 *
 * @param {String} method hash method, e.g.: 'md5', 'sha1'
 * @param {String|Buffer} s
 * @param {String} [format] output string format, could be 'hex' or 'base64'. default is 'hex'.
 * @return {String} md5 hash string
 * @public
 */
exports.hash = function hash(method, s, format) {
  var sum = crypto.createHash(method);
  var isBuffer = Buffer.isBuffer(s);
  if (!isBuffer && typeof s === 'object') {
    s = JSON.stringify(sortObject(s));
  }
  sum.update(s, isBuffer ? 'binary' : 'utf8');
  return sum.digest(format || 'hex');
};

/**
 * md5 hash
 *
 * @param {String|Buffer} s
 * @param {String} [format] output string format, could be 'hex' or 'base64'. default is 'hex'.
 * @return {String} md5 hash string
 * @public
 */
exports.md5 = function (s, format) {
  return exports.hash('md5', s, format);
};

/**
 * sha1 hash
 *
 * @param {String|Buffer} s
 * @param {String} [format] output string format, could be 'hex' or 'base64'. default is 'hex'.
 * @return {String} sha1 hash string
 * @public
 */
exports.sha1 = function (s, format) {
  return exports.hash('sha1', s, format);
};

/**
 * HMAC algorithm.
 *
 * Equal bash:
 *
 * ```bash
 * $ echo -n "$data" | openssl dgst -binary -$algorithm -hmac "$key" | openssl $encoding
 * ```
 *
 * @param {String} algorithm, dependent on the available algorithms supported by the version of OpenSSL on the platform.
 *   Examples are 'sha1', 'md5', 'sha256', 'sha512', etc.
 *   On recent releases, `openssl list-message-digest-algorithms` will display the available digest algorithms.
 * @param {String} key, the hmac key to be used.
 * @param {String|Buffer} data, content string.
 * @param {String} [encoding='base64']
 * @return {String} digest string.
 */
exports.hmac = function (algorithm, key, data, encoding) {
  encoding = encoding || 'base64';
  var hmac = crypto.createHmac(algorithm, key);
  hmac.update(data, Buffer.isBuffer(data) ? 'binary' : 'utf8');
  return hmac.digest(encoding);
};

/**
 * Base64 encode string.
 *
 * @param {String|Buffer} s
 * @param {Boolean} [urlsafe=false] Encode string s using a URL-safe alphabet,
 *   which substitutes - instead of + and _ instead of / in the standard Base64 alphabet.
 * @return {String} base64 encode format string.
 */
exports.base64encode = function (s, urlsafe) {
  if (!Buffer.isBuffer(s)) {
    s = new Buffer(s);
  }
  var encode = s.toString('base64');
  if (urlsafe) {
    encode = encode.replace(/\+/g, '-').replace(/\//g, '_');
  }
  return encode;
};

/**
 * Base64 string decode.
 *
 * @param {String} encode, base64 encoding string.
 * @param {Boolean} [urlsafe=false] Decode string s using a URL-safe alphabet,
 *   which substitutes - instead of + and _ instead of / in the standard Base64 alphabet.
 * @return {String} plain text.
 */
exports.base64decode = function (encode, urlsafe) {
  if (urlsafe) {
    encode = encode.replace(/\-/g, '+').replace(/_/g, '/');
  }
  encode = new Buffer(encode, 'base64');
  return encode.toString();
};

/**
 * Escape the given string of `html`.
 *
 * @param {String} html
 * @return {String}
 * @public
 */
exports.escape = function (html) {
  return String(html)
    .replace(/&(?!\w+;)/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;');
};

/**
 * Array random slice with items count.
 * @param {Array} arr
 * @param {Number} num, number of sub items.
 * @return {Array}
 */
exports.randomSlice = function (arr, num) {
  if (!num || num >= arr.length) {
    return arr.slice();
  }
  var index = Math.floor(Math.random() * arr.length);
  var a = [];
  for (var i = 0, j = index; i < num; i++) {
    a.push(arr[j++]);
    if (j === arr.length) {
      j = 0;
    }
  }
  return a;
};

/**
 * Safe encodeURIComponent, won't throw any error.
 * If `encodeURIComponent` error happen, just return the original value.
 *
 * @param {String} text
 * @return {String} URL encode string.
 */
exports.encodeURIComponent = function (text) {
  try {
    return encodeURIComponent(text);
  } catch (e) {
    return text;
  }
};

/**
 * Safe decodeURIComponent, won't throw any error.
 * If `decodeURIComponent` error happen, just return the original value.
 *
 * @param {String} encodeText
 * @return {String} URL decode original string.
 */
exports.decodeURIComponent = function (encodeText) {
  try {
    return decodeURIComponent(encodeText);
  } catch (e) {
    return encodeText;
  }
};

var MONTHS = [
  'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'
];

// only set once.
var TIMEZONE = ' ';
var _hourOffset = parseInt(-(new Date().getTimezoneOffset()) / 60, 10);
if (_hourOffset >= 0) {
  TIMEZONE += '+';
} else {
  TIMEZONE += '-';
}
_hourOffset = Math.abs(_hourOffset);
if (_hourOffset < 10) {
  _hourOffset = '0' + _hourOffset;
}
TIMEZONE += _hourOffset + '00';

/**
 * Access log format date. format: `moment().format('DD/MMM/YYYY:HH:mm:ss ZZ')`
 *
 * @return {String}
 */
exports.accessLogDate = function (d) {
  // 16/Apr/2013:16:40:09 +0800
  d = d || new Date();
  var date = d.getDate();
  if (date < 10) {
    date = '0' + date;
  }
  var hours = d.getHours();
  if (hours < 10) {
    hours = '0' + hours;
  }
  var mintues = d.getMinutes();
  if (mintues < 10) {
    mintues = '0' + mintues;
  }
  var seconds = d.getSeconds();
  if (seconds < 10) {
    seconds = '0' + seconds;
  }
  return date + '/' + MONTHS[d.getMonth()] + '/' + d.getFullYear() +
    ':' + hours + ':' + mintues + ':' + seconds + TIMEZONE;
};

/**
 * Normal log format date. format: `moment().format('YYYY-MM-DD HH:mm:ss.SSS')`
 *
 * @return {String}
 */
exports.logDate = exports.YYYYMMDDHHmmssSSS = function (d) {
  d = d || new Date();
  var date = d.getDate();
  if (date < 10) {
    date = '0' + date;
  }
  var month = d.getMonth() + 1;
  if (month < 10) {
    month = '0' + month;
  }
  var hours = d.getHours();
  if (hours < 10) {
    hours = '0' + hours;
  }
  var mintues = d.getMinutes();
  if (mintues < 10) {
    mintues = '0' + mintues;
  }
  var seconds = d.getSeconds();
  if (seconds < 10) {
    seconds = '0' + seconds;
  }
  var milliseconds = d.getMilliseconds();
  if (milliseconds < 10) {
    milliseconds = '00' + milliseconds;
  } else if (milliseconds < 100) {
    milliseconds = '0' + milliseconds;
  }
  return d.getFullYear() + '-' + month + '-' + date + ' ' +
    hours + ':' + mintues + ':' + seconds + '.' + milliseconds;
};

/**
 * `moment().format('YYYY-MM-DD HH:mm:ss')` format date string.
 *
 * @return {String}
 */
exports.YYYYMMDDHHmmss = function (d) {
  d = d || new Date();
  var date = d.getDate();
  if (date < 10) {
    date = '0' + date;
  }
  var month = d.getMonth() + 1;
  if (month < 10) {
    month = '0' + month;
  }
  var hours = d.getHours();
  if (hours < 10) {
    hours = '0' + hours;
  }
  var mintues = d.getMinutes();
  if (mintues < 10) {
    mintues = '0' + mintues;
  }
  var seconds = d.getSeconds();
  if (seconds < 10) {
    seconds = '0' + seconds;
  }
  return d.getFullYear() + '-' + month + '-' + date + ' ' +
    hours + ':' + mintues + ':' + seconds;
};

/**
 * `moment().format('YYYY-MM-DD')` format date string.
 *
 * @return {String}
 */
exports.YYYYMMDD = function YYYYMMDD(d) {
  d = d || new Date();
  var date = d.getDate();
  if (date < 10) {
    date = '0' + date;
  }
  var month = d.getMonth() + 1;
  if (month < 10) {
    month = '0' + month;
  }
  return d.getFullYear() + '-' + month + '-' + date;
};

/**
 * return datetime struct.
 *
 * @return {Object} date
 *  - {Number} YYYYMMDD, 20130401
 *  - {Number} H, 0, 1, 9, 12, 23
 */
exports.datestruct = function (now) {
  now = now || new Date();
  return {
    YYYYMMDD: now.getFullYear() * 10000 + (now.getMonth() + 1) * 100 + now.getDate(),
    H: now.getHours()
  };
};

var _showWarnning = false;

/**
 * Get current machine IPv4
 *
 * @param {String} [interfaceName] interface name, default is 'eth' on linux, 'en' on mac os.
 * @return {String} IP address
 */
exports.getIP = exports.getIPv4 = function (interfaceName) {
  if (!_showWarnning) {
    _showWarnning = true;
    console.warn('[WARNNING] getIP() remove, PLEASE use `https://github.com/fengmk2/address` module instead');
  }
  return address.ip(interfaceName);
};

/**
 * Get current machine IPv6
 *
 * @param {String} [interfaceName] interface name, default is 'eth' on linux, 'en' on mac os.
 * @return {String} IP address
 */
exports.getIPv6 = function (interfaceName) {
  return address.ipv6(interfaceName);
};

/**
 * Get a function parameter's names.
 *
 * @param {Function} func
 * @param {Boolean} [useCache], default is true
 * @return {Array} names
 */
exports.getParamNames = function (func, cache) {
  cache = cache !== false;
  if (cache && func.__cache_names) {
    return func.__cache_names;
  }
  var str = func.toString();
  var names = str.slice(str.indexOf('(') + 1, str.indexOf(')')).match(/([^\s,]+)/g) || [];
  func.__cache_names = names;
  return names;
};

// http://www.2ality.com/2013/10/safe-integers.html
exports.MAX_SAFE_INTEGER = Math.pow(2, 53) - 1;
exports.MIN_SAFE_INTEGER = -exports.MAX_SAFE_INTEGER;
var MAX_SAFE_INTEGER_STR = exports.MAX_SAFE_INTEGER_STR = String(exports.MAX_SAFE_INTEGER);
var MAX_SAFE_INTEGER_STR_LENGTH = MAX_SAFE_INTEGER_STR.length;

/**
 * Detect a number string can safe convert to Javascript Number.
 *
 * @param {String} s number format string, like `"123"`, `"-1000123123123123123123"`
 * @return {Boolean}
 */
exports.isSafeNumberString = function (s) {
  if (s[0] === '-') {
    s = s.substring(1);
  }
  if (s.length < MAX_SAFE_INTEGER_STR_LENGTH || (s.length === MAX_SAFE_INTEGER_STR_LENGTH && s <= MAX_SAFE_INTEGER_STR)) {
    return true;
  }
  return false;
};

/**
 * Convert string to Number if string in safe Number scope.
 *
 * @param {String} s number format string.
 * @return {Number|String} success will return Number, otherise return the original string.
 */
exports.toSafeNumber = function (s) {
  if (typeof s === 'number') {
    return s;
  }

  return exports.isSafeNumberString(s) ? Number(s) : s;
};

/**
 * Get Unix's timestamp in seconds.
 * @return {Number}
 */
exports.timestamp = function (t) {
  if (t) {
    var v = t;
    if (typeof v === 'string') {
      v = Number(v);
    }
    if (String(t).length === 10) {
      v *= 1000;
    }
    return new Date(v);
  }
  return Math.round(Date.now() / 1000);
};

var _setImmediate = typeof setImmediate === 'function' ? setImmediate : process.nextTick;

exports.setImmediate = function (callback) {
  _setImmediate(callback);
};

exports.randomString = function (length, charSet) {
  var result = [];
  length = length || 16;
  charSet = charSet || 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';

  while (length--) {
    result.push(charSet[Math.floor(Math.random() * charSet.length)]);
  }
  return result.join('');
};

exports.has = function (obj, prop) {
  return Object.prototype.hasOwnProperty.call(obj, prop);
};
