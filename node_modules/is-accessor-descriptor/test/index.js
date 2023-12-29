'use strict';

var test = require('tape');
var isDescriptor = require('../');
var noop = function () {};

test('isDescriptor', function (t) {
	t.test('value type', function (st) {
		st.notOk(isDescriptor('a'), 'string is not a descriptor');
		st.notOk(isDescriptor(null), 'null is not a descriptor');
		st.notOk(isDescriptor([]), 'Array is not a descriptor');

		st.end();
	});

	t.test('is false when the object has data descriptor properties:', function (st) {
		st.notOk(isDescriptor({ get: noop, writable: true }));
		st.notOk(isDescriptor({ get: noop, value: true }));

		st.end();
	});

	t.test('is not false when unrecognized properties are defined:', function (st) {
		st.ok(isDescriptor({ get: noop, foo: true }));
		st.ok(isDescriptor({ get: noop, bar: true }));

		st.end();
	});

	t.test('is false when a get or set are not functions:', function (st) {
		st.notOk(isDescriptor({ get: noop, set: 'baz' }));
		st.notOk(isDescriptor({ get: 'foo', set: noop }));
		st.notOk(isDescriptor({ get: 'foo', bar: 'baz' }));
		st.notOk(isDescriptor({ get: 'foo', set: 'baz' }));
		st.notOk(isDescriptor({ get: 'foo' }));

		st.end();
	});

	t.test('is true when "get" is not defined:', function (st) {
		st.ok(isDescriptor({ set: noop }));

		st.end();
	});

	t.test('is true when the object has valid properties:', function (st) {
		st.ok(isDescriptor({ get: noop, set: noop }));
		st.ok(isDescriptor({ get: noop }));

		st.end();
	});

	t.test('is false when a value is not the correct type:', function (st) {
		st.notOk(isDescriptor({ get: noop, set: noop, enumerable: 'foo' }));
		st.notOk(isDescriptor({ set: noop, configurable: 'foo' }));
		st.notOk(isDescriptor({ get: noop, configurable: 'foo' }));

		st.end();
	});

	t.end();
});
