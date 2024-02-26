'use strict';

var hasOwn = require('hasown');

var isInteger = require('../isInteger');

module.exports = function isRegExpRecord(value) {
	return value
        && hasOwn(value, '[[IgnoreCase]]')
        && typeof value['[[IgnoreCase]]'] === 'boolean'
        && hasOwn(value, '[[Multiline]]')
        && typeof value['[[Multiline]]'] === 'boolean'
        && hasOwn(value, '[[DotAll]]')
        && typeof value['[[DotAll]]'] === 'boolean'
        && hasOwn(value, '[[Unicode]]')
        && typeof value['[[Unicode]]'] === 'boolean'
        && hasOwn(value, '[[CapturingGroupsCount]]')
        && typeof value['[[CapturingGroupsCount]]'] === 'number'
        && isInteger(value['[[CapturingGroupsCount]]'])
        && value['[[CapturingGroupsCount]]'] >= 0;
};
