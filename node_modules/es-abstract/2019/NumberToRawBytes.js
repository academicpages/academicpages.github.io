'use strict';

var GetIntrinsic = require('get-intrinsic');

var $floor = GetIntrinsic('%Math.floor%');
var $log = GetIntrinsic('%Math.log%');
var $log2E = GetIntrinsic('%Math.LOG2E%');
var $log2 = GetIntrinsic('%Math.log2%', true) || function log2(x) {
	return $log(x) * $log2E;
};
var $parseInt = GetIntrinsic('%parseInt%');
var $pow = GetIntrinsic('%Math.pow%');
var $TypeError = GetIntrinsic('%TypeError%');

var callBound = require('call-bind/callBound');

var $reverse = callBound('Array.prototype.reverse');
var $numberToString = callBound('Number.prototype.toString');
var $strSlice = callBound('String.prototype.slice');

var abs = require('./abs');
var hasOwnProperty = require('./HasOwnProperty');
var ToInt16 = require('./ToInt16');
var ToInt32 = require('./ToInt32');
var ToInt8 = require('./ToInt8');
var ToUint16 = require('./ToUint16');
var ToUint32 = require('./ToUint32');
var ToUint8 = require('./ToUint8');
var ToUint8Clamp = require('./ToUint8Clamp');
var Type = require('./Type');

var isNaN = require('../helpers/isNaN');
var isFinite = require('../helpers/isFinite');

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

var TypeToAO = {
	__proto__: null,
	Int8: ToInt8,
	Uint8: ToUint8,
	Uint8C: ToUint8Clamp,
	Int16: ToInt16,
	Uint16: ToUint16,
	Int32: ToInt32,
	Uint32: ToUint32
};

// https://262.ecma-international.org/8.0/#sec-numbertorawbytes

module.exports = function NumberToRawBytes(type, value, isLittleEndian) {
	if (typeof type !== 'string' || !hasOwnProperty(TypeToSizes, type)) {
		throw new $TypeError('Assertion failed: `type` must be a TypedArray element type: ' + keys(TypeToSizes));
	}
	if (Type(value) !== 'Number') {
		throw new $TypeError('Assertion failed: `value` must be a Number');
	}
	if (Type(isLittleEndian) !== 'Boolean') {
		throw new $TypeError('Assertion failed: `isLittleEndian` must be a Boolean');
	}

	var rawBytes = [];
	var exponent;

	if (type === 'Float32') { // step 1
		if (isNaN(value)) {
			return isLittleEndian ? [0, 0, 192, 127] : [127, 192, 0, 0]; // hardcoded
		}

		var leastSig;

		if (value === 0) {
			leastSig = Object.is(value, -0) ? 0x80 : 0;
			return isLittleEndian ? [0, 0, 0, leastSig] : [leastSig, 0, 0, 0];
		}

		if (!isFinite(value)) {
			leastSig = value < 0 ? 255 : 127;
			return isLittleEndian ? [0, 0, 128, leastSig] : [leastSig, 128, 0, 0];
		}

		var sign = value < 0 ? 1 : 0;
		value = abs(value); // eslint-disable-line no-param-reassign

		exponent = 0;
		while (value >= 2) {
			exponent += 1;
			value /= 2; // eslint-disable-line no-param-reassign
		}

		while (value < 1) {
			exponent -= 1;
			value *= 2; // eslint-disable-line no-param-reassign
		}

		var mantissa = value - 1;
		mantissa *= $pow(2, 23);
		mantissa = $floor(mantissa);

		exponent += 127;
		exponent = exponent << 23;

		var result = sign << 31;
		result |= exponent;
		result |= mantissa;

		var byte0 = result & 255;
		result = result >> 8;
		var byte1 = result & 255;
		result = result >> 8;
		var byte2 = result & 255;
		result = result >> 8;
		var byte3 = result & 255;

		if (isLittleEndian) {
			return [byte0, byte1, byte2, byte3];
		}
		return [byte3, byte2, byte1, byte0];
	} else if (type === 'Float64') { // step 2
		if (value === 0) {
			leastSig = Object.is(value, -0) ? 0x80 : 0;
			return isLittleEndian ? [0, 0, 0, 0, 0, 0, 0, leastSig] : [leastSig, 0, 0, 0, 0, 0, 0, 0];
		}
		if (isNaN(value)) {
			return isLittleEndian ? [0, 0, 0, 0, 0, 0, 248, 127] : [127, 248, 0, 0, 0, 0, 0, 0];
		}
		if (!isFinite(value)) {
			var infBytes = value < 0 ? [0, 0, 0, 0, 0, 0, 240, 255] : [0, 0, 0, 0, 0, 0, 240, 127];
			return isLittleEndian ? infBytes : $reverse(infBytes);
		}

		var isNegative = value < 0;
		if (isNegative) { value = -value; } // eslint-disable-line no-param-reassign

		exponent = $floor($log2(value));
		var significand = (value / $pow(2, exponent)) - 1;

		var bitString = '';
		for (var i = 0; i < 52; i++) {
			significand *= 2;
			if (significand >= 1) {
				bitString += '1';
				significand -= 1;
			} else {
				bitString += '0';
			}
		}

		exponent += 1023;
		var exponentBits = $numberToString(exponent, 2);
		while (exponentBits.length < 11) { exponentBits = '0' + exponentBits; }

		var fullBitString = (isNegative ? '1' : '0') + exponentBits + bitString;
		while (fullBitString.length < 64) { fullBitString = '0' + fullBitString; }

		for (i = 0; i < 8; i++) {
			rawBytes[i] = $parseInt($strSlice(fullBitString, i * 8, (i + 1) * 8), 2);
		}

		return isLittleEndian ? $reverse(rawBytes) : rawBytes;
	} // step 3

	var n = TypeToSizes[type]; // step 3.a

	var convOp = TypeToAO[type]; // step 3.b

	var intValue = convOp(value); // step 3.c

	/*
	if (intValue >= 0) { // step 3.d
		// Let rawBytes be a List containing the n-byte binary encoding of intValue. If isLittleEndian is false, the bytes are ordered in big endian order. Otherwise, the bytes are ordered in little endian order.
	} else { // step 3.e
		// Let rawBytes be a List containing the n-byte binary 2's complement encoding of intValue. If isLittleEndian is false, the bytes are ordered in big endian order. Otherwise, the bytes are ordered in little endian order.
	}
    */
	if (intValue < 0) {
		intValue = intValue >>> 0;
	}
	for (i = 0; i < n; i++) {
		rawBytes[isLittleEndian ? i : n - 1 - i] = intValue & 0xff;
		intValue = intValue >> 8;
	}

	return rawBytes; // step 4
};
