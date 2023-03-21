
/**
 * Module dependencies.
 */

var inherits = require('util').inherits;

/**
 * Module exports.
 */

module.exports = NotModifiedError;

/**
 * Error subclass to use when the source has not been modified.
 *
 * @param {String} message optional "message" property to set
 * @api protected
 */

function NotModifiedError (message) {
  this.name = 'NotModifiedError';
  this.code = 'ENOTMODIFIED';
  this.message = message || 'Source has not been modified since the provied "cache", re-use previous results';
  Error.captureStackTrace(this, NotModifiedError);
}

inherits(NotModifiedError, Error);
