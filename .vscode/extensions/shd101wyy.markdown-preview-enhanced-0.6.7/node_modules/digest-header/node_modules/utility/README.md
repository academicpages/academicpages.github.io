utility [![Build Status](https://secure.travis-ci.org/fengmk2/utility.png)](http://travis-ci.org/fengmk2/utility) [![Coverage Status](https://coveralls.io/repos/fengmk2/utility/badge.png)](https://coveralls.io/r/fengmk2/utility)
=======

[![NPM](https://nodei.co/npm/utility.png?downloads=true&stars=true)](https://nodei.co/npm/utility)

![logo](https://raw.github.com/fengmk2/utility/master/logo.png)

A collection of useful utilities.

## Install

```bash
$ npm install utility
```

## Usage

```js
var utils = require('utility');

// md5 hash
utils.md5('@Python发烧友'); // '1369e7668bc600f0d90c06f5e395d7a9'
utils.md5(new Buffer('')); // 'd41d8cd98f00b204e9800998ecf8427e'
// md5 hase output base64
utils.md5('苏千', 'base64'); // 'X3M8R8WKB31hJXECstREgQ=='

// Object md5 hash
utils.md5({foo: 'bar', bar: 'foo'}).should.equal(utils.md5({bar: 'foo', foo: 'bar'}));

// hmac
// hmac-sha1 with base64 output encoding
utils.hmac('sha1', 'I am a key', 'hello world'); // 'pO6J0LKDxRRkvSECSEdxwKx84L0='

// base64 encode
utils.base64encode('你好￥'); // '5L2g5aW977+l'
utils.base64decode('5L2g5aW977+l') // '你好￥'

// urlsafe base64 encode
utils.base64encode('你好￥', true); // '5L2g5aW977-l'
utils.base64decode('5L2g5aW977-l', true); // '你好￥'

// empty function
process.nextTick(utils.noop);
function foo(callback) {
  callback = callback || utils.noop;
}

// html escape
utils.escape('<script/>"& &amp;'); // '&lt;script/&gt;&quot;&amp; &amp;'

// Safe encodeURIComponent and decodeURIComponent
utils.decodeURIComponent(utils.encodeURIComponent('你好, nodejs')).should.equal('你好, nodejs');

// get first ip
[WARNNING] getIP() remove, PLEASE use `https://github.com/fengmk2/address` module instead

// get a function parameter's names
utils.getParamNames(function (key1, key2) {}); // ['key1', 'key2']

// get a random string, default length is 16
utils.randomString(32, '1234567890'); //18774480824014856763726145106142

// check if object has this property
utils.has({hello: 'world'}, 'hello'); //true
```

### Date utils

```js
// accessLogDate
utils.accessLogDate(); // '16/Apr/2013:16:40:09 +0800'

// logDate,
// 'YYYY-MM-DD HH:mm:ss.SSS' format date string
utils.logDate(); // '2013-04-17 14:43:02.674'
utils.YYYYMMDDHHmmssSSS(); // '2013-04-17 14:43:02.674'

// 'YYYY-MM-DD HH:mm:ss' format date string
utils.YYYYMMDDHHmmss(); // '2013-04-17 14:43:02'

// 'YYYY-MM-DD' format date string
utils.YYYYMMDD(); // '2013-04-17'

// datestruct
utils.datestruct(); // { YYYYMMDD: 20130416, H: 8 }

// Unix's timestamp
utils.timestamp(); // 1378153226

// Parse timestamp
// seconds
utils.timestamp(1385091596); // Fri Nov 22 2013 11:39:56 GMT+0800 (CST)
// millseconds
utils.timestamp(1385091596000); // Fri Nov 22 2013 11:39:56 GMT+0800 (CST)
```

### Number utils

```js
// Detect a number string can safe convert to Javascript Number.: `-9007199254740991 ~ 9007199254740991`
utils.isSafeNumberString('9007199254740991'); // true
utils.isSafeNumberString('9007199254740993'); // false

// Convert string to number safe:
utils.toSafeNumber('9007199254740991'); // 9007199254740991
utils.toSafeNumber('9007199254740993'); // '9007199254740993'
```

### Timers

```js
utils.setImmediate(function () {
  console.log('hi');
});
```

## benchmark

* [jsperf: access log date format](http://jsperf.com/access-log-date-format)
* [benchmark/date_format.js](https://github.com/fengmk2/utility/blob/master/benchmark/date_format.js)

```bash
$ node benchmark/date_format.js

moment().format("DD/MMM/YYYY:HH:mm:ss ZZ"): "16/Apr/2013:21:12:32 +0800"
utils.accessLogDate(): "16/Apr/2013:21:12:32 +0800"
fasterAccessDate(): "16/Apr/2013:21:12:32 +0800"
fasterAccessDate2(): "16/Apr/2013:21:12:32 +0800"
new Date().toString(): "Tue Apr 16 2013 21:12:32 GMT+0800 (CST)"
Date(): "Tue Apr 16 2013 21:12:32 GMT+0800 (CST)"
Date.now(): 1366117952162
------------------------
moment().format('DD/MMM/YYYY:HH:mm:ss ZZ') x 68,300 ops/sec ±5.05% (91 runs sampled)
utils.accessLogDate() x 1,341,341 ops/sec ±2.72% (90 runs sampled)
fasterAccessDate() x 357,833 ops/sec ±1.32% (98 runs sampled)
fasterAccessDate2() x 301,607 ops/sec ±5.03% (83 runs sampled)
new Date().toString() x 738,499 ops/sec ±3.54% (86 runs sampled)
Date() x 794,724 ops/sec ±2.77% (95 runs sampled)
Date.now() x 8,327,685 ops/sec ±1.85% (94 runs sampled)
Fastest is Date.now()
```

[benchmark/date_YYYYMMDD.js](https://github.com/fengmk2/utility/blob/master/benchmark/date_YYYYMMDD.js)

```bash
$ node benchmark/date_YYYYMMDD.js

parseInt(moment().format("YYYYMMDD"), 10): 20130416
utils.datestruct().YYYYMMDD: 20130416
new Date().toString(): "Tue Apr 16 2013 21:12:02 GMT+0800 (CST)"
------------------------
parseInt(moment().format('YYYYMMDD'), 10) x 129,604 ops/sec ±0.46% (101 runs sampled)
utils.datestruct().YYYYMMDD x 2,317,461 ops/sec ±1.38% (95 runs sampled)
new Date().toString() x 816,731 ops/sec ±3.46% (93 runs sampled)
Fastest is utils.datestruct().YYYYMMDD

```

## Authors

```bash
$ git summary

 project  : utility
 repo age : 1 year, 2 months
 active   : 24 days
 commits  : 61
 files    : 17
 authors  :
    58  fengmk2                 95.1%
     3  dead-horse              4.9%
```

## License

(The MIT License)

Copyright (c) 2012 - 2013 fengmk2 &lt;fengmk2@gmail.com&gt;

Permission is hereby granted, free of charge, to any person obtaining
a copy of this software and associated documentation files (the
'Software'), to deal in the Software without restriction, including
without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject to
the following conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED 'AS IS', WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
