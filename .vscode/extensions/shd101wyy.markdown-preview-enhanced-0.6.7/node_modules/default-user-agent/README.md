default-user-agent
=======

[![NPM version][npm-image]][npm-url]
[![build status][travis-image]][travis-url]
[![Test coverage][coveralls-image]][coveralls-url]
[![Gittip][gittip-image]][gittip-url]
[![David deps][david-image]][david-url]
[![npm download][download-image]][download-url]

[npm-image]: https://img.shields.io/npm/v/default-user-agent.svg?style=flat-square
[npm-url]: https://npmjs.org/package/default-user-agent
[travis-image]: https://img.shields.io/travis/node-modules/default-user-agent.svg?style=flat-square
[travis-url]: https://travis-ci.org/node-modules/default-user-agent
[coveralls-image]: https://img.shields.io/coveralls/node-modules/default-user-agent.svg?style=flat-square
[coveralls-url]: https://coveralls.io/r/node-modules/default-user-agent?branch=master
[gittip-image]: https://img.shields.io/gittip/fengmk2.svg?style=flat-square
[gittip-url]: https://www.gittip.com/fengmk2/
[david-image]: https://img.shields.io/david/node-modules/default-user-agent.svg?style=flat-square
[david-url]: https://david-dm.org/node-modules/default-user-agent
[download-image]: https://img.shields.io/npm/dm/default-user-agent.svg?style=flat-square
[download-url]: https://npmjs.org/package/default-user-agent

Default user agent string for Node.js http request

## Install

```bash
$ npm install default-user-agent
```

## Usage

```js
var ua = require('default-user-agent');

// darwin
console.log(ua()); // 'Node.js/0.11.15 (OS X Yosemite; x64)'
console.log(ua('urllib', '0.0.1')); // 'urllib/0.0.1 Node.js/0.11.15 (OS X Yosemite; x64)'

// linux
// 'Node.js/0.11.15 (Linux 3.13; x64)'
```

## License

[MIT](LICENSE.txt)
