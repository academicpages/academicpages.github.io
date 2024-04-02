'use strict';

var GetIntrinsic = require('get-intrinsic');

var $defineProperty = GetIntrinsic('%Object.defineProperty%', true);

var hasToStringTag = require('has-tostringtag/shams')();
var hasOwn = require('hasown');

var toStringTag = hasToStringTag ? Symbol.toStringTag : null;

/** @type {import('.')} */
module.exports = function setToStringTag(object, value) {
	var overrideIfSet = arguments.length > 2 && arguments[2] && arguments[2].force;
	if (toStringTag && (overrideIfSet || !hasOwn(object, toStringTag))) {
		if ($defineProperty) {
			$defineProperty(object, toStringTag, {
				configurable: true,
				enumerable: false,
				value: value,
				writable: false
			});
		} else {
			object[toStringTag] = value; // eslint-disable-line no-param-reassign
		}
	}
};
