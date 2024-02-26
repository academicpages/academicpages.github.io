'use strict';

// / <reference types="node" />

var callBind = require('call-bind');
var forEach = require('for-each');
var gOPD = require('gopd');
var hasProto = require('has-proto')();
var isTypedArray = require('is-typed-array');
var typedArrays = require('possible-typed-array-names');

/** @typedef {Int8Array | Uint8Array | Uint8ClampedArray | Int16Array | Uint16Array | Int32Array | Uint32Array | Float32Array | Float64Array | BigInt64Array | BigUint64Array} TypedArray */
/** @typedef {typeof typedArrays[number]} TypedArrayName */
/** @typedef {(value: TypedArray) => number} TypedArrayLengthGetter */

/** @type {Object.<TypedArrayName, TypedArrayLengthGetter>} */
var getters = {};
var oDP = Object.defineProperty;
if (gOPD) {
	var getLength = /** @type {TypedArrayLengthGetter} */ function (x) {
		return x.length;
	};
	forEach(typedArrays, /** @type {(typedArray: TypedArrayName) => void} */ function (typedArray) {
		var TA = global[typedArray];
		// In Safari 7, Typed Array constructors are typeof object
		if (typeof TA === 'function' || typeof TA === 'object') {
			var Proto = TA.prototype;
			// @ts-expect-error TS doesn't narrow types inside callbacks, which is weird
			var descriptor = gOPD(Proto, 'length');
			if (!descriptor && hasProto) {
				var superProto = Proto.__proto__; // eslint-disable-line no-proto
				// @ts-expect-error TS doesn't narrow types inside callbacks, which is weird
				descriptor = gOPD(superProto, 'length');
			}
			// Opera 12.16 has a magic length data property on instances AND on Proto
			if (descriptor && descriptor.get) {
				getters[typedArray] = callBind(descriptor.get);
			} else if (oDP) {
				// this is likely an engine where instances have a magic length data property
				var arr = new global[typedArray](2);
				// @ts-expect-error TS doesn't narrow types inside callbacks, which is weird
				descriptor = gOPD(arr, 'length');
				if (descriptor && descriptor.configurable) {
					oDP(arr, 'length', { value: 3 });
				}
				if (arr.length === 2) {
					getters[typedArray] = getLength;
				}
			}
		}
	});
}

/** @type {TypedArrayLengthGetter} */
var tryTypedArrays = function tryAllTypedArrays(value) {
	/** @type {number} */ var foundLength;
	forEach(getters, /** @type {(getter: TypedArrayLengthGetter) => void} */ function (getter) {
		if (typeof foundLength !== 'number') {
			try {
				var length = getter(value);
				if (typeof length === 'number') {
					foundLength = length;
				}
			} catch (e) {}
		}
	});
	// @ts-expect-error TS can't guarantee the above callback is invoked sync
	return foundLength;
};

/** @type {import('.')} */
module.exports = function typedArrayLength(value) {
	if (!isTypedArray(value)) {
		return false;
	}
	return tryTypedArrays(value);
};
