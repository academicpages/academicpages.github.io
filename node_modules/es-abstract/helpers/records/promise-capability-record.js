'use strict';

var hasOwn = require('hasown');

module.exports = function isPromiseCapabilityRecord(value) {
	return !!value
        && hasOwn(value, '[[Resolve]]')
        && typeof value['[[Resolve]]'] === 'function'
        && hasOwn(value, '[[Reject]]')
        && typeof value['[[Reject]]'] === 'function'
        && hasOwn(value, '[[Promise]]')
        && value['[[Promise]]']
        && typeof value['[[Promise]]'].then === 'function';
};
