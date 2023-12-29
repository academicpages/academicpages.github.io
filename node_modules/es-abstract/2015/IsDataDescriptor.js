'use strict';

var hasOwn = require('hasown');

var Type = require('./Type');

var assertRecord = require('../helpers/assertRecord');

// https://262.ecma-international.org/5.1/#sec-8.10.2

module.exports = function IsDataDescriptor(Desc) {
	if (typeof Desc === 'undefined') {
		return false;
	}

	assertRecord(Type, 'Property Descriptor', 'Desc', Desc);

	if (!hasOwn(Desc, '[[Value]]') && !hasOwn(Desc, '[[Writable]]')) {
		return false;
	}

	return true;
};
