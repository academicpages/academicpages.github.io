'use strict';

exports.randomString = function randomString(length, charSet) {
  var result = [];
  length = length || 16;
  charSet = charSet || 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';

  while (length--) {
    result.push(charSet[Math.floor(Math.random() * charSet.length)]);
  }
  return result.join('');
};

/**
 * split string to array
 * @param  {String} str
 * @param  {String} [sep] default is ','
 * @return {Array}
 */
exports.split = function split(str, sep) {
  str = str || '';
  sep = sep || ',';
  var items = str.split(sep);
  var needs = [];
  for (var i = 0; i < items.length; i++) {
    var s = items[i].trim();
    if (s.length > 0) {
      needs.push(s);
    }
  }
  return needs;
};
// always optimized
exports.splitAlwaysOptimized = function splitAlwaysOptimized() {
  var str = '';
  var sep = ',';
  if (arguments.length === 1) {
    str = arguments[0] || '';
  } else if (arguments.length === 2) {
    str = arguments[0] || '';
    sep = arguments[1] || ',';
  }
  var items = str.split(sep);
  var needs = [];
  for (var i = 0; i < items.length; i++) {
    var s = items[i].trim();
    if (s.length > 0) {
      needs.push(s);
    }
  }
  return needs;
};

/**
 * Replace string
 *
 * @param  {String} str
 * @param  {String|RegExp} substr
 * @param  {String|Function} newSubstr
 * @return {String}
 */
exports.replace = function replace(str, substr, newSubstr) {
  var replaceFunction = newSubstr;
  if (typeof replaceFunction !== 'function') {
    replaceFunction = function () {
      return newSubstr;
    };
  }
  return str.replace(substr, replaceFunction);
};

// original source https://github.com/nodejs/node/blob/v7.5.0/lib/_http_common.js#L300
/**
 * True if val contains an invalid field-vchar
 *  field-value    = *( field-content / obs-fold )
 *  field-content  = field-vchar [ 1*( SP / HTAB ) field-vchar ]
 *  field-vchar    = VCHAR / obs-text
 *
 * checkInvalidHeaderChar() is currently designed to be inlinable by v8,
 * so take care when making changes to the implementation so that the source
 * code size does not exceed v8's default max_inlined_source_size setting.
 **/
var validHdrChars = [
  0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, // 0 - 15
  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, // 16 - 31
  1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, // 32 - 47
  1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, // 48 - 63
  1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, // 64 - 79
  1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, // 80 - 95
  1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, // 96 - 111
  1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, // 112 - 127
  1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, // 128 ...
  1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
  1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
  1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
  1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
  1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
  1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
  1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,  // ... 255
];

/**
 * Replace invalid http header characters with replacement
 *
 * @param  {String} val
 * @param  {String|Function} replacement - can be `function(char)`
 * @return {Object}
 */
exports.replaceInvalidHttpHeaderChar = function replaceInvalidHttpHeaderChar(val, replacement) {
  replacement = replacement || ' ';
  var invalid = false;

  if (!val || typeof val !== 'string') {
    return {
      val: val,
      invalid: invalid,
    };
  }

  var replacementType = typeof replacement;
  var chars;
  for (var i = 0; i < val.length; ++i) {
    if (!validHdrChars[val.charCodeAt(i)]) {
      // delay create chars
      chars = chars || val.split('');
      if (replacementType === 'function') {
        chars[i] = replacement(chars[i]);
      } else {
        chars[i] = replacement;
      }
    }
  }

  if (chars) {
    val = chars.join('');
    invalid = true;
  }

  return {
    val: val,
    invalid: invalid,
  };
};

/**
 * Detect invalid http header characters in a string
 *
 * @param {String} val
 * @return {Boolean}
 */
exports.includesInvalidHttpHeaderChar = function includesInvalidHttpHeaderChar(val) {
  if (!val || typeof val !== 'string') {
    return false;
  }

  for (var i = 0; i < val.length; ++i) {
    if (!validHdrChars[val.charCodeAt(i)]) {
      return true;
    }
  }

  return false;
};
