'use strict';

var hasOwn = require('hasown');

module.exports = function isIteratorRecord(value) {
	return value
        && hasOwn(value, '[[Iterator]]')
        && hasOwn(value, '[[NextMethod]]')
        && typeof value['[[NextMethod]]'] === 'function'
        && hasOwn(value, '[[Done]]')
        && typeof value['[[Done]]'] === 'boolean';
};
