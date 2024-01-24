# is-data-descriptor <sup>[![Version Badge][npm-version-svg]][package-url]</sup>

[![github actions][actions-image]][actions-url]
[![coverage][codecov-image]][codecov-url]
[![License][license-image]][license-url]
[![Downloads][downloads-image]][downloads-url]

[![npm badge][npm-badge-png]][package-url]

> Returns true if a value has the characteristics of a valid JavaScript data descriptor.

## Install

Install with [npm](https://npmjs.com/):

```sh
$ npm install --save is-data-descriptor
```

## Usage

```js
var isDataDesc = require('is-data-descriptor');
var assert = require('assert');
```

## Examples

`true` when the descriptor has valid properties with valid values.

```js
// `value` can be anything
assert.equal(isDataDesc({ value: 'foo' }), true);
assert.equal(isDataDesc({ value: function () {} }), true);
assert.equal(isDataDesc({ value: true }), true);
```

`false` when not an object

```js
assert.equal(isDataDesc('a'), false);
assert.equal(isDataDesc(null), false);
```

`false` when the object has invalid properties

```js
assert.equal(isDataDesc({ value: 'foo', enumerable: 'baz' }), false);
assert.equal(isDataDesc({ value: 'foo', configurable: 'baz' }), false);
assert.equal(isDataDesc({ value: 'foo', get() {} }), false);
assert.equal(isDataDesc({ get() {}, value: 'foo' }), false);
```

`false` when a value is not the correct type

```js
assert.equal(isDataDesc({ value: 'foo', enumerable: 'foo' }), false);
assert.equal(isDataDesc({ value: 'foo', configurable: 'foo' }), false);
assert.equal(isDataDesc({ value: 'foo', writable: 'foo' }), false);
```

## Valid properties

The only valid data descriptor properties are the following:

* `configurable` (required)
* `enumerable` (required)
* `value` (optional)
* `writable` (optional)

To be a valid data descriptor, either `value` or `writable` must be defined.

**Invalid properties**

A descriptor may have additional _invalid_ properties (an error will **not** be thrown).

```js
var foo = {};

Object.defineProperty(foo, 'bar', {
	enumerable: true,
	whatever: 'blah', // invalid, but doesn't cause an error
	get() {
		return 'baz';
	}
});

assert.equal(foo.bar, 'baz');
```

### Related projects

You might also be interested in these projects:

* [is-accessor-descriptor](https://npmjs.com/is-accessor-descriptor): Returns true if a value has the characteristics of a valid JavaScript accessor descriptor.
* [is-descriptor](https://npmjs.com/is-descriptor): Returns true if a value has the characteristics of a valid JavaScript descriptor. Works for… [more](https://npmjs.com/is-descriptor)

[package-url]: https://npmjs.org/package/is-data-descriptor
[npm-version-svg]: https://versionbadg.es/inspect-js/is-data-descriptor.svg
[deps-svg]: https://david-dm.org/inspect-js/is-data-descriptor.svg
[deps-url]: https://david-dm.org/inspect-js/is-data-descriptor
[dev-deps-svg]: https://david-dm.org/inspect-js/is-data-descriptor/dev-status.svg
[dev-deps-url]: https://david-dm.org/inspect-js/is-data-descriptor#info=devDependencies
[npm-badge-png]: https://nodei.co/npm/is-data-descriptor.png?downloads=true&stars=true
[license-image]: https://img.shields.io/npm/l/is-data-descriptor.svg
[license-url]: LICENSE
[downloads-image]: https://img.shields.io/npm/dm/is-data-descriptor.svg
[downloads-url]: https://npm-stat.com/charts.html?package=is-data-descriptor
[codecov-image]: https://codecov.io/gh/inspect-js/is-data-descriptor/branch/main/graphs/badge.svg
[codecov-url]: https://app.codecov.io/gh/inspect-js/is-data-descriptor/
[actions-image]: https://img.shields.io/endpoint?url=https://github-actions-badge-u3jn4tfpocch.runkit.sh/inspect-js/is-data-descriptor
[actions-url]: https://github.com/inspect-js/is-data-descriptor/actions
