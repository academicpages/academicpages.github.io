# is-accessor-descriptor <sup>[![Version Badge][npm-version-svg]][package-url]</sup>

[![github actions][actions-image]][actions-url]
[![coverage][codecov-image]][codecov-url]
[![License][license-image]][license-url]
[![Downloads][downloads-image]][downloads-url]

[![npm badge][npm-badge-png]][package-url]

> Returns true if a value has the characteristics of a valid JavaScript accessor descriptor.

## Examples

```js
var isAccessor = require('is-accessor-descriptor');
var assert = require('assert');

assert.equal(isAccessor({ get: function() {} }), true);
```

You may also pass an object and property name to check if the property is an accessor:

```js
assert.equal(isAccessor({ bar: {} }, 'bar'), true);
```

## Examples

`false` when not an object

```js
assert.equal(isAccessor('a'), false);
assert.equal(isAccessor(null), false);
```

`true` when the object has valid properties

and the properties all have the correct JavaScript types:

```js
assert.equal(isAccessor({ get() {}, set() {} }), true);
assert.equal(isAccessor({ get() {} }), true);
assert.equal(isAccessor({ set() {} }), true);
```

`false` when the object has invalid properties

```js
assert.equal(isAccessor({ get() {}, set() {}, enumerable: 'baz' }), false);
assert.equal(isAccessor({ get() {}, writable: true }), false);
assert.equal(isAccessor({ get() {}, value: true }), false);
```

`false` when an accessor is not a function

```js
isAccessor({ get() {}, set: 'baz' });
isAccessor({ get: 'foo', set() {} });
isAccessor({ get: 'foo', bar: 'baz' });
isAccessor({ get: 'foo', set: 'baz' });
//=> false
```

`false` when a value is not the correct type

```js
isAccessor({ get() {}, set() {}, enumerable: 'foo' });
isAccessor({ set() {}, configurable: 'foo' });
isAccessor({ get() {}, configurable: 'foo' });
//=> false
```

### Related projects

You might also be interested in these projects:

* [is-data-descriptor](https://www.npmjs.com/package/is-data-descriptor): Returns true if a value has the characteristics of a valid JavaScript data descriptor.
* [is-descriptor](https://www.npmjs.com/package/is-descriptor): Returns true if a value has the characteristics of a valid JavaScript descriptor. Works for… [more](https://github.com/inspect-js/is-descriptor)
* [is-object](https://www.npmjs.com/package/is-object): Returns true if the value is an object and not an array or null.

## Tests
Simply clone the repo, `npm install`, and run `npm test`

[package-url]: https://npmjs.org/package/is-accessor-descriptor
[npm-version-svg]: https://versionbadg.es/inspect-js/is-accessor-descriptor.svg
[deps-svg]: https://david-dm.org/inspect-js/is-accessor-descriptor.svg
[deps-url]: https://david-dm.org/inspect-js/is-accessor-descriptor
[dev-deps-svg]: https://david-dm.org/inspect-js/is-accessor-descriptor/dev-status.svg
[dev-deps-url]: https://david-dm.org/inspect-js/is-accessor-descriptor#info=devDependencies
[npm-badge-png]: https://nodei.co/npm/is-accessor-descriptor.png?downloads=true&stars=true
[license-image]: https://img.shields.io/npm/l/is-accessor-descriptor.svg
[license-url]: LICENSE
[downloads-image]: https://img.shields.io/npm/dm/is-accessor-descriptor.svg
[downloads-url]: https://npm-stat.com/charts.html?package=is-accessor-descriptor
[codecov-image]: https://codecov.io/gh/inspect-js/is-accessor-descriptor/branch/main/graphs/badge.svg
[codecov-url]: https://app.codecov.io/gh/inspect-js/is-accessor-descriptor/
[actions-image]: https://img.shields.io/endpoint?url=https://github-actions-badge-u3jn4tfpocch.runkit.sh/inspect-js/is-accessor-descriptor
[actions-url]: https://github.com/inspect-js/is-accessor-descriptor/actions
