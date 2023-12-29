'use strict';

var test = require('tape');
var isDescriptor = require('../');
var noop = function () {};

test('isDescriptor', function (t) {
	t.test('is false when not an object:', function (st) {
		st.notOk(isDescriptor('a'));
		st.notOk(isDescriptor(null));
		st.notOk(isDescriptor([]));

		st.end();
	});

	t.test('returns true if the property exists', function (st) {
		var obj = { foo: null };

		Object.defineProperty(obj, 'bar', {
			value: 'xyz'
		});

		Object.defineProperty(obj, 'baz', {
			get: function () {
				return 'aaa';
			}
		});

		st.ok(isDescriptor(obj, 'foo'));
		st.ok(isDescriptor(obj, 'bar'));
		st.ok(isDescriptor(obj, 'baz'));

		st.end();
	});

	t.test('data descriptor:', function (st) {
		st.test('is false when the object has invalid properties:', function (s2t) {
			s2t.notOk(isDescriptor({ value: 'foo', get: noop }));
			s2t.notOk(isDescriptor({ get: noop, value: noop }));

			s2t.end();
		});

		st.test('is not false when the object has unrecognize properties:', function (s2t) {
			s2t.ok(isDescriptor({ value: 'foo', bar: 'baz' }));
			s2t.ok(isDescriptor({ value: 'foo', bar: 'baz' }));

			s2t.end();
		});

		st.test('is true when the object has valid properties:', function (s2t) {
			s2t.ok(isDescriptor({ value: 'foo' }));
			s2t.ok(isDescriptor({ value: noop }));

			s2t.end();
		});

		st.test('is false when a value is not the correct type:', function (s2t) {
			s2t.notOk(isDescriptor({ value: 'foo', enumerable: 'foo' }));
			s2t.notOk(isDescriptor({ value: 'foo', configurable: 'foo' }));
			s2t.notOk(isDescriptor({ value: 'foo', writable: 'foo' }));

			s2t.end();
		});

		st.end();
	});

	t.test('accessor descriptor:', function (st) {
		st.test('should be false when the object has invalid properties:', function (s2t) {
			s2t.ok(!isDescriptor({ get: noop, writable: true }));
			s2t.ok(!isDescriptor({ get: noop, value: true }));

			s2t.end();
		});

		st.test('is not false when the object has unrecognize properties:', function (s2t) {
			s2t.ok(isDescriptor({ get: noop, set: noop, bar: 'baz' }));

			s2t.end();
		});

		st.test('is false when an accessor is not a function:', function (s2t) {
			s2t.notOk(isDescriptor({ get: noop, set: 'baz' }));
			s2t.notOk(isDescriptor({ get: 'foo', set: noop }));
			s2t.notOk(isDescriptor({ get: 'foo', bar: 'baz' }));
			s2t.notOk(isDescriptor({ get: 'foo', set: 'baz' }));

			s2t.end();
		});

		st.test('is false when "get" or "set" is not a function', function (s2t) {
			s2t.notOk(isDescriptor({ set: 'foo' }));
			s2t.notOk(isDescriptor({ get: 'foo' }));

			s2t.end();
		});

		st.test('is true when the object has valid properties:', function (s2t) {
			s2t.ok(isDescriptor({ get: noop, set: noop }));
			s2t.ok(isDescriptor({ get: noop }));

			s2t.end();
		});

		st.test('is false when a value is not the correct type:', function (s2t) {
			s2t.notOk(isDescriptor({ get: noop, set: noop, enumerable: 'foo' }));
			s2t.notOk(isDescriptor({ set: noop, configurable: 'foo' }));
			s2t.notOk(isDescriptor({ get: noop, configurable: 'foo' }));

			s2t.end();
		});

		st.end();
	});
});
