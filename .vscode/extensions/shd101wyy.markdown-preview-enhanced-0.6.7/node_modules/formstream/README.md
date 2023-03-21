# formstream

[![NPM version][npm-image]][npm-url]
[![build status][travis-image]][travis-url]
[![Test coverage][coveralls-image]][coveralls-url]
[![David deps][david-image]][david-url]
[![npm download][download-image]][download-url]

[npm-image]: https://img.shields.io/npm/v/formstream.svg?style=flat-square
[npm-url]: https://npmjs.org/package/formstream
[travis-image]: https://img.shields.io/travis/node-modules/formstream.svg?style=flat-square
[travis-url]: https://travis-ci.org/node-modules/formstream
[coveralls-image]: https://img.shields.io/coveralls/node-modules/formstream.svg?style=flat-square
[coveralls-url]: https://coveralls.io/r/node-modules/formstream?branch=master
[david-image]: https://img.shields.io/david/node-modules/formstream.svg?style=flat-square
[david-url]: https://david-dm.org/node-modules/formstream
[download-image]: https://img.shields.io/npm/dm/formstream.svg?style=flat-square
[download-url]: https://npmjs.org/package/formstream

A [multipart/form-data](http://tools.ietf.org/html/rfc2388) encoded stream, helper for file upload.

## Install

```bash
$ npm install formstream
```

## Quick Start

```js
var formstream = require('formstream');
var http = require('http');

var form = formstream();

// form.file('file', filepath, filename);
form.file('file', './logo.png', 'upload-logo.png');

// other form fields
form.field('foo', 'fengmk2').field('love', 'aerdeng');

// even send file content buffer directly
// form.buffer(name, buffer, filename, mimeType)
form.buffer('file2', new Buffer('This is file2 content.'), 'foo.txt');

var options = {
  method: 'POST',
  host: 'upload.cnodejs.net',
  path: '/store',
  headers: form.headers()
};
var req = http.request(options, function (res) {
  console.log('Status: %s', res.statusCode);
  res.on('data', function (data) {
    console.log(data.toString());
  });
});

form.pipe(req);
```

### Chaining

```js
var fs = require('fs');
var formstream = require('formstream');

var filepath = './logo.png';
fs.stat(filepath, function (err, stat) {
  formstream().field('status', 'share picture')
      .field('access_token', 'your access token')
      .file('pic', filepath, 'logo.png', stat.size)
      .pipe(process.stdout); // your request stream
});
```

## API Doc

### formstream()

Create a form instance.

#### Returns

Form - form instance

### FormStream#field(name, value)

Add a normal field to the form.

#### Arguments

- **name** String - Name of field
- **value** String - Value of field

#### Returns

Form - form instance

### FormStream#file(name, filepath[, filename][, filesize])

Add a local file to be uploaded to the form.

#### Arguments

- **name** String - Name of file field
- **filepath** String - Local path of the file to be uploaded
- ***filename*** String - Optional. Name of the file (will be the base name of `filepath` if empty)
- ***filesize*** Number - Optional. Size of the file (will not generate `Content-Length` header if not specified)

#### Returns

Form - form instance

### FormStream#buffer(name, buffer, filename[, contentType])

Add a buffer as a file to upload.

#### Arguments

- **name** String - Name of field
- **buffer** Buffer - The buffer to be uploaded
- **filename** String - The file name that tells the remote server
- ***contentType*** String - Optional. Content-Type (aka. MIME Type) of content (will be infered with `filename` if empty)

#### Returns

Form - form instance

### FormStream#stream(name, stream, filename[, contentType][, size])

Add a readable stream as a file to upload. Event 'error' will be emitted if an error occured.

#### Arguments

- **name** String - Name of field
- **stream** [stream.Readable](http://nodejs.org/api/stream.html#stream_class_stream_readable) - A readable stream to be piped
- **filename** String - The file name that tells the remote server
- ***contentType*** String - Optional. Content-Type (aka. MIME Type) of content (will be infered with `filename` if empty)
- ***size*** Number - Optional. Size of the stream (will not generate `Content-Length` header if not specified)

#### Returns

Form - form instance

### FormStream#headers([headers])

Get headers for the request.

#### Arguments

- ***headers*** Object - Additional headers

#### Example

```js
var headers = form.headers({
  'Authorization': 'Bearer kei2akc92jmznvnkeh09sknzdk',
  'Accept': 'application/vnd.github.v3.full+json'
});
```

#### Returns

Object - Headers to be sent.

### Event 'error'

Emitted if there was an error receiving data.

### Event 'data'

The 'data' event emits when a Buffer was used.

See [Node.js Documentation](http://nodejs.org/api/stream.html#stream_event_data) for more.

### Event 'end'

Emitted when the stream has received no more 'data' events will happen.

See [Node.js Documentation](http://nodejs.org/api/stream.html#stream_event_end) for more.

## License

(The MIT License)

Copyright (c) 2012 - 2014 fengmk2 &lt;fengmk2@gmail.com&gt;
Copyright(c) node-modules and other contributors.

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
