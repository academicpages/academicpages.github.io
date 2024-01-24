'use strict';

var GetIntrinsic = require('get-intrinsic');

var $TypeError = GetIntrinsic('%TypeError%');
var $SyntaxError = GetIntrinsic('%SyntaxError%');

var hasOwn = require('hasown');
var isInteger = require('./isInteger');

var isMatchRecord = require('./isMatchRecord');

var predicates = {
	// https://262.ecma-international.org/6.0/#sec-property-descriptor-specification-type
	'Property Descriptor': function isPropertyDescriptor(Desc) {
		var allowed = {
			'[[Configurable]]': true,
			'[[Enumerable]]': true,
			'[[Get]]': true,
			'[[Set]]': true,
			'[[Value]]': true,
			'[[Writable]]': true
		};

		if (!Desc) {
			return false;
		}
		for (var key in Desc) { // eslint-disable-line
			if (hasOwn(Desc, key) && !allowed[key]) {
				return false;
			}
		}

		var isData = hasOwn(Desc, '[[Value]]');
		var IsAccessor = hasOwn(Desc, '[[Get]]') || hasOwn(Desc, '[[Set]]');
		if (isData && IsAccessor) {
			throw new $TypeError('Property Descriptors may not be both accessor and data descriptors');
		}
		return true;
	},
	// https://262.ecma-international.org/13.0/#sec-match-records
	'Match Record': isMatchRecord,
	'Iterator Record': function isIteratorRecord(value) {
		return hasOwn(value, '[[Iterator]]') && hasOwn(value, '[[NextMethod]]') && hasOwn(value, '[[Done]]');
	},
	'PromiseCapability Record': function isPromiseCapabilityRecord(value) {
		return !!value
			&& hasOwn(value, '[[Resolve]]')
			&& typeof value['[[Resolve]]'] === 'function'
			&& hasOwn(value, '[[Reject]]')
			&& typeof value['[[Reject]]'] === 'function'
			&& hasOwn(value, '[[Promise]]')
			&& value['[[Promise]]']
			&& typeof value['[[Promise]]'].then === 'function';
	},
	'AsyncGeneratorRequest Record': function isAsyncGeneratorRequestRecord(value) {
		return !!value
			&& hasOwn(value, '[[Completion]]') // TODO: confirm is a completion record
			&& hasOwn(value, '[[Capability]]')
			&& predicates['PromiseCapability Record'](value['[[Capability]]']);
	},
	'RegExp Record': function isRegExpRecord(value) {
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
	}
};

module.exports = function assertRecord(Type, recordType, argumentName, value) {
	var predicate = predicates[recordType];
	if (typeof predicate !== 'function') {
		throw new $SyntaxError('unknown record type: ' + recordType);
	}
	if (Type(value) !== 'Object' || !predicate(value)) {
		throw new $TypeError(argumentName + ' must be a ' + recordType);
	}
};
