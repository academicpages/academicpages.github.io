'use strict';

var GetIntrinsic = require('get-intrinsic');

var $RangeError = GetIntrinsic('%RangeError%');
var $TypeError = GetIntrinsic('%TypeError%');

var callBound = require('call-bind/callBound');

// node 0.10 doesn't have a prototype method
var $byteOffset = callBound('TypedArray.prototype.byteOffset', true) || function (x) { return x.byteOffset; };

var ToIndex = require('./ToIndex');
var TypedArrayElementSize = require('./TypedArrayElementSize');

var isTypedArray = require('is-typed-array');
var typedArrayLength = require('typed-array-length');

// https://262.ecma-international.org/13.0/#sec-validateatomicaccess

module.exports = function ValidateAtomicAccess(typedArray, requestIndex) {
	if (!isTypedArray(typedArray)) {
		throw new $TypeError('Assertion failed: `typedArray` must be a TypedArray');
	}

	var length = typedArrayLength(typedArray); // step 1

	var accessIndex = ToIndex(requestIndex); // step 2

	/*
	// this assertion can never be reached
	if (!(accessIndex >= 0)) {
		throw new $TypeError('Assertion failed: accessIndex >= 0'); // step 4
	}
	*/

	if (accessIndex >= length) {
		throw new $RangeError('index out of range'); // step 4
	}

	var elementSize = TypedArrayElementSize(typedArray); // step 5

	var offset = $byteOffset(typedArray); // step 6

	return (accessIndex * elementSize) + offset; // step 7
};
