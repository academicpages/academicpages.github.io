'use strict';

var hasOwn = require('hasown');

// accessor descriptor properties
var accessor = {
	__proto__: null,
	configurable: 'boolean',
	enumerable: 'boolean',
	get: 'function',
	set: 'function'
};

module.exports = function isAccessorDescriptor(obj, prop) {
	if (typeof prop === 'string') {
		var val = Object.getOwnPropertyDescriptor(obj, prop);
		return typeof val !== 'undefined';
	}

	if (!obj || typeof obj !== 'object') {
		return false;
	}

	if (hasOwn(obj, 'value') || hasOwn(obj, 'writable')) {
		return false;
	}

	// one of them must be a function
	if (
		(!hasOwn(obj, 'get') || typeof obj.get !== 'function')
		&& (!hasOwn(obj, 'set') || typeof obj.set !== 'function')
	) {
		return false;
	}

	// both of them must be a function or undefined
	if (
		(hasOwn(obj, 'get') && typeof obj.get !== 'function' && typeof obj.get !== 'undefined')
		|| (hasOwn(obj, 'set') && typeof obj.set !== 'function' && typeof obj.set !== 'undefined')
	) {
		return false;
	}

	for (var key in obj) { // eslint-disable-line no-restricted-syntax
		if (hasOwn(obj, key) && hasOwn(accessor, key) && typeof obj[key] !== accessor[key] && typeof obj[key] !== 'undefined') {
			return false;
		}
	}
	return true;
};
