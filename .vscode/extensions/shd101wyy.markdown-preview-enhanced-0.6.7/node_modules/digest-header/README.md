digest-header
=======

[![Build Status](https://secure.travis-ci.org/fengmk2/digest-header.png)](http://travis-ci.org/fengmk2/digest-header) [![Dependency Status](https://gemnasium.com/fengmk2/digest-header.png)](https://gemnasium.com/fengmk2/digest-header)

[![NPM](https://nodei.co/npm/digest-header.png?downloads=true&stars=true)](https://nodei.co/npm/digest-header/)

![logo](https://raw.github.com/fengmk2/digest-header/master/logo.png)

Digest access authentication header helper.

Coverage [100%](http://qtestbucket.qiniudn.com/cov/html/node-v0.11.12/digest-header/0.0.0/index.html)

## Install

```bash
$ npm install digest-header
```

## Usage

```js
var digest = require('digest-header');

var method = 'GET';
var uri = '/admin';
var wwwAuthenticate = res.headers['WWW-Authenticate'];
var userpass = 'user:pass';
var auth = digest(method, uri, wwwAuthenticate, userpass);
```

## License

(The MIT License)

Copyright (c) 2014 fengmk2 &lt;fengmk2@gmail.com&gt; and other contributors

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
