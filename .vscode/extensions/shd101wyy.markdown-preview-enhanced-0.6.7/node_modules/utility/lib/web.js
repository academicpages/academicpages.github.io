'use strict';

/**
 * Escape the given string of `html`.
 *
 * @param {String} html
 * @return {String}
 * @public
 */
exports.escape = require('escape-html');


/**
 * Unescape the given string from html
 * @param {String} html
 * @param {String} type
 * @return {String}
 * @public
 */
exports.unescape = require('unescape');

/**
 * Safe encodeURIComponent, won't throw any error.
 * If `encodeURIComponent` error happen, just return the original value.
 *
 * @param {String} text
 * @return {String} URL encode string.
 */
exports.encodeURIComponent = function encodeURIComponent_(text) {
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
exports.decodeURIComponent = function decodeURIComponent_(encodeText) {
  try {
    return decodeURIComponent(encodeText);
  } catch (e) {
    return encodeText;
  }
};
