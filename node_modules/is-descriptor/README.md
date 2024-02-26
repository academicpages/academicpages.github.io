# is-descriptor <sup>[![Version Badge][npm-version-svg]][package-url]</sup>

[![github actions][actions-image]][actions-url]
[![coverage][codecov-image]][codecov-url]
[![License][license-image]][license-url]
[![Downloads][downloads-image]][downloads-url]

[![npm badge][npm-badge-png]][package-url]

> Returns true if a value has the characteristics of a valid JavaScript descriptor. Works for data descriptors and accessor descriptors.

## Usage

```js
const isDescriptor = require('is-descriptor');
const assert = require('assert');

assert.equal(isDescriptor({ value: 'foo' }), true);
assert.equal(isDescriptor({ get() {}, set() {} }), true);
assert.equal(isDescriptor({ get: 'foo', set() {} }), false);
```

You may also check for a descriptor by passing an object as the first argument and property name (`string`) as the second argument.

```js
const obj = { foo: 'abc' };

Object.defineProperty(obj, 'bar', {
  value: 'xyz'
});

assert.equal(isDescriptor(obj, 'foo'), true);
assert.equal(isDescriptor(obj, 'bar'), true);
```

## Examples

### value type

`false` when not an object

```js
assert.equal(isDescriptor('a'), false);
assert.equal(isDescriptor(null), false);
assert.equal(isDescriptor([]), false);
```

### data descriptor

`true` when the object has valid properties with valid values.

```js
assert.equal(isDescriptor({ value: 'foo' }), true);
assert.equal(isDescriptor({ value() {} }), true);
```

`false` when the object has invalid properties

```js
assert.equal(isDescriptor({ value: 'foo', enumerable: 'baz' }), false);
assert.equal(isDescriptor({ value: 'foo', configurable: 'baz' }), false);
assert.equal(isDescriptor({ value: 'foo', get() {} }), false);
assert.equal(isDescriptor({ get() {}, value() {} }), false);
```

`false` when a value is not the correct type

```js
assert.equal(isDescriptor({ value: 'foo', enumerable: 'foo' }), false);
assert.equal(isDescriptor({ value: 'foo', configurable: 'foo' }), false);
assert.equal(isDescriptor({ value: 'foo', writable: 'foo' }), false);
```

### accessor descriptor

`true` when the object has valid properties with valid values.

```js
assert.equal(isDescriptor({ get() {}, set() {} }), true);
assert.equal(isDescriptor({ get() {} }), true);
assert.equal(isDescriptor({ set() {} }), true);
```

`false` when the object has invalid properties

```js
assert.equal(isDescriptor({ get() {}, set() {}, enumerable: 'baz' }), false);
assert.equal(isDescriptor({ get() {}, writable: true }), false);
assert.equal(isDescriptor({ get() {}, value: true }), false);
```

`false` when an accessor is not a function

```js
assert.equal(isDescriptor({ get() {}, set: 'baz' }), false);
assert.equal(isDescriptor({ get: 'foo', set() {} }), false);
assert.equal(isDescriptor({ get: 'foo', bar: 'baz' }), false);
assert.equal(isDescriptor({ get: 'foo', set: 'baz' }), false);
```

`false` when a value is not the correct type

```js
assert.equal(isDescriptor({ get() {}, set() {}, enumerable: 'foo' }), false);
assert.equal(isDescriptor({ set() {}, configurable: 'foo' }), false);
assert.equal(isDescriptor({ get() {}, configurable: 'foo' }), false);
```

### Related projects

You might also be interested in these projects:

* [is-accessor-descriptor](https://www.npmjs.com/package/is-accessor-descriptor): Returns true if a value has the characteristics of a valid JavaScript accessor descriptor.
* [is-data-descriptor](https://www.npmjs.com/package/is-data-descriptor): Returns true if a value has the characteristics of a valid JavaScript data descriptor.
* [is-object](https://www.npmjs.com/package/is-object): Returns true if the value is an object and not an array or null.

## Tests
Simply clone the repo, `npm install`, and run `npm test`

[package-url]: https://npmjs.org/package/is-descriptor
[npm-version-svg]: https://versionbadg.es/inspect-js/is-descriptor.svg
[deps-svg]: https://david-dm.org/inspect-js/is-descriptor.svg
[deps-url]: https://david-dm.org/inspect-js/is-descriptor
[dev-deps-svg]: https://david-dm.org/inspect-js/is-descriptor/dev-status.svg
[dev-deps-url]: https://david-dm.org/inspect-js/is-descriptor#info=devDependencies
[npm-badge-png]: https://nodei.co/npm/is-descriptor.png?downloads=true&stars=true
[license-image]: https://img.shields.io/npm/l/is-descriptor.svg
[license-url]: LICENSE
[downloads-image]: https://img.shields.io/npm/dm/is-descriptor.svg
[downloads-url]: https://npm-stat.com/charts.html?package=is-descriptor
[codecov-image]: https://codecov.io/gh/inspect-js/is-descriptor/branch/main/graphs/badge.svg
[codecov-url]: https://app.codecov.io/gh/inspect-js/is-descriptor/
[actions-image]: https://img.shields.io/endpoint?url=https://github-actions-badge-u3jn4tfpocch.runkit.sh/inspect-js/is-descriptor
[actions-url]: https://github.com/inspect-js/is-descriptor/actions
