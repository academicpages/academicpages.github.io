'use strict';

var GetIntrinsic = require('get-intrinsic');
var callBound = require('call-bind/callBound');

var $pow = GetIntrinsic('%Math.pow%');
var $RangeError = GetIntrinsic('%RangeError%');
var $TypeError = GetIntrinsic('%TypeError%');

var $charAt = callBound('String.prototype.charAt');
var $reverse = callBound('Array.prototype.reverse');
var $slice = callBound('Array.prototype.slice');

var hasOwnProperty = require('./HasOwnProperty');
var IsArray = require('./IsArray');
var Type = require('./Type');

var every = require('../helpers/every');
var isByteValue = require('../helpers/isByteValue');

var keys = require('object-keys');

// https://262.ecma-international.org/8.0/#table-50
var TypeToSizes = {
	__proto__: null,
	Int8: 1,
	Uint8: 1,
	Uint8C: 1,
	Int16: 2,
	Uint16: 2,
	Int32: 4,
	Uint32: 4,
	Float32: 4,
	Float64: 8
};

// https://262.ecma-international.org/8.0/#sec-rawbytestonumber

module.exports = function RawBytesToNumber(type, rawBytes, isLittleEndian) {
	if (typeof type !== 'string' || !hasOwnProperty(TypeToSizes, type)) {
		throw new $TypeError('Assertion failed: `type` must be a TypedArray element type: ' + keys(TypeToSizes));
	}
	if (!IsArray(rawBytes) || !every(rawBytes, isByteValue)) {
		throw new $TypeError('Assertion failed: `rawBytes` must be an Array of bytes');
	}
	if (Type(isLittleEndian) !== 'Boolean') {
		throw new $TypeError('Assertion failed: `isLittleEndian` must be a Boolean');
	}

	var elementSize = TypeToSizes[type]; // step 1

	if (rawBytes.length !== elementSize) {
		// this assertion is not in the spec, but it'd be an editorial error if it were ever violated
		throw new $RangeError('Assertion failed: `rawBytes` must have a length of ' + elementSize + ' for type ' + type);
	}

	// eslint-disable-next-line no-param-reassign
	rawBytes = $slice(rawBytes, 0, elementSize);
	if (!isLittleEndian) {
		// eslint-disable-next-line no-param-reassign
		rawBytes = $reverse(rawBytes); // step 2
	}

	/* eslint no-redeclare: 1 */
	if (type === 'Float32') { // step 3
		/*
        Let value be the byte elements of rawBytes concatenated and interpreted as a little-endian bit string encoding of an IEEE 754-2008 binary32 value.
If value is an IEEE 754-2008 binary32 NaN value, return the NaN Number value.
Return the Number value that corresponds to value.
        */
		var sign = (rawBytes[3] & 0x80) >> 7; // first bit
		var exponent = ((rawBytes[3] & 0x7F) << 1) // 7 bits from index 3
			| ((rawBytes[2] & 0x80) >> 7); // 1 bit from index 2
		var mantissa = ((rawBytes[2] & 0x7F) << 16) // 7 bits from index 2
			| (rawBytes[1] << 8) // 8 bits from index 1
			| rawBytes[0]; // 8 bits from index 0

		if (exponent === 0 && mantissa === 0) {
			return sign === 0 ? 0 : -0;
		}
		if (exponent === 0xFF && mantissa === 0) {
			return sign === 0 ? Infinity : -Infinity;
		}
		if (exponent === 0xFF && mantissa !== 0) {
			return NaN;
		}

		exponent -= 127; // subtract the bias

		// return $pow(-1, sign) * mantissa / $pow(2, 23) * $pow(2, exponent);
		// return $pow(-1, sign) * (mantissa + 0x1000000) * $pow(2, exponent - 23);
		return $pow(-1, sign) * (1 + (mantissa / $pow(2, 23))) * $pow(2, exponent);
	}

	if (type === 'Float64') { // step 4
		/*
        Let value be the byte elements of rawBytes concatenated and interpreted as a little-endian bit string encoding of an IEEE 754-2008 binary64 value.
If value is an IEEE 754-2008 binary64 NaN value, return the NaN Number value.
Return the Number value that corresponds to value.
        */
		var sign = rawBytes[7] & 0x80 ? -1 : 1; // first bit
		var exponent = ((rawBytes[7] & 0x7F) << 4) // 7 bits from index 7
			| ((rawBytes[6] & 0xF0) >> 4); // 4 bits from index 6
		var mantissa = ((rawBytes[6] & 0x0F) * 0x1000000000000) // 4 bits from index 6
			+ (rawBytes[5] * 0x10000000000) // 8 bits from index 5
			+ (rawBytes[4] * 0x100000000) // 8 bits from index 4
			+ (rawBytes[3] * 0x1000000) // 8 bits from index 3
			+ (rawBytes[2] * 0x10000) // 8 bits from index 2
			+ (rawBytes[1] * 0x100) // 8 bits from index 1
			+ rawBytes[0]; // 8 bits from index 0

		if (exponent === 0 && mantissa === 0) {
			return sign * 0;
		}
		if (exponent === 0x7FF && mantissa !== 0) {
			return NaN;
		}
		if (exponent === 0x7FF && mantissa === 0) {
			return sign * Infinity;
		}

		exponent -= 1023; // subtract the bias

		return sign * (mantissa + 0x10000000000000) * $pow(2, exponent - 52);
	}

	// this is common to both branches
	var intValue = 0;
	for (var i = 0; i < rawBytes.length; i++) {
		intValue |= rawBytes[i] << (8 * i);
	}
	/*
	Let intValue be the byte elements of rawBytes concatenated and interpreted as a bit string encoding of an unsigned little-endian binary number.
	*/

	if ($charAt(type, 0) !== 'U') { // steps 5-6
		// Let intValue be the byte elements of rawBytes concatenated and interpreted as a bit string encoding of a binary little-endian 2's complement number of bit length elementSize × 8.
		var bitLength = elementSize * 8;
		if (bitLength < 32) {
			intValue = (intValue << (32 - bitLength)) >> (32 - bitLength);
		}
	}

	return intValue; // step 7
};
