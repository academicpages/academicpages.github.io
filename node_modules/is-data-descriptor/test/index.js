'use strict';

var test = require('tape');
var isDescriptor = require('../');
var noop = function () {};

test('isDescriptor', function (t) {
	t.test('value type', function (st) {
		st.notOk(isDescriptor('a'), 'string is not a descriptor');
		st.notOk(isDescriptor(null), 'null is not a descriptor');

		st.end();
	});

	t.test('should not be false when the object has unknown properties:', function (st) {
		st.ok(isDescriptor({ value: 'foo', bar: 'baz' }));
		st.ok(isDescriptor({ value: 'foo', bar: 'baz' }));

		st.end();
	});

	t.test('should be false when the object has accessor properties', function (st) {
		st.notOk(isDescriptor({ value: 'foo', get: noop }));
		st.notOk(isDescriptor({ set: noop, value: noop }));

		st.end();
	});

	t.test('should be true when the object has valid data-descriptor properties', function (st) {
		st.ok(isDescriptor({ value: 'foo' }));
		st.ok(isDescriptor({ value: noop }));

		st.end();
	});

	t.test('should be false when valid properties are invalid types', function (st) {
		st.notOk(isDescriptor({ value: 'foo', enumerable: 'foo' }));
		st.notOk(isDescriptor({ value: 'foo', configurable: 'foo' }));
		st.notOk(isDescriptor({ value: 'foo', writable: 'foo' }));

		st.end();
	});

	t.test('should be true when a value is a valid data descriptor', function (st) {
		st.ok(isDescriptor({ value: 'foo' }));
		st.ok(isDescriptor({ writable: true }));

		st.end();
	});

	t.test('should be false when the value is not a valid descriptor', function (st) {
		st.notOk(isDescriptor('foo'));
		st.notOk(isDescriptor({}));
		st.notOk(isDescriptor({ configurable: true }));
		st.notOk(isDescriptor({ enumerable: true }));
		st.notOk(isDescriptor({
			get: undefined,
			set: undefined,
			enumerable: true,
			configurable: true,
		}));

		st.end();
	});

	t.end();
});
