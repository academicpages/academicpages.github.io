'use strict';

// http://www.2ality.com/2013/10/safe-integers.html
// http://es6.ruanyifeng.com/#docs/number
exports.MAX_SAFE_INTEGER = Number.MAX_SAFE_INTEGER || Math.pow(2, 53) - 1;
exports.MIN_SAFE_INTEGER = -exports.MAX_SAFE_INTEGER;
var MAX_SAFE_INTEGER_STR = exports.MAX_SAFE_INTEGER_STR = String(exports.MAX_SAFE_INTEGER);
var MAX_SAFE_INTEGER_STR_LENGTH = MAX_SAFE_INTEGER_STR.length;

/**
 * Detect a number string can safe convert to Javascript Number.
 *
 * @param {String} s number format string, like `"123"`, `"-1000123123123123123123"`
 * @return {Boolean}
 */
exports.isSafeNumberString = function isSafeNumberString(s) {
  if (s[0] === '-') {
    s = s.substring(1);
  }
  if (s.length < MAX_SAFE_INTEGER_STR_LENGTH ||
    (s.length === MAX_SAFE_INTEGER_STR_LENGTH && s <= MAX_SAFE_INTEGER_STR)) {
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
exports.toSafeNumber = function toSafeNumber(s) {
  if (typeof s === 'number') {
    return s;
  }

  return exports.isSafeNumberString(s) ? Number(s) : s;
};

/**
 * Produces a random integer between the inclusive `lower` and `upper` bounds.
 *
 * @param {Number} lower The lower bound.
 * @param {Number} upper The upper bound.
 * @return {Number} Returns the random number.
 */
exports.random = function random(lower, upper) {
  if (lower === undefined && upper === undefined) {
    return 0;
  }
  if (upper === undefined) {
    upper = lower;
    lower = 0;
  }
  var temp;
  if (lower > upper) {
    temp = lower;
    lower = upper;
    upper = temp;
  }
  return Math.floor(lower + Math.random() * (upper - lower));
};
