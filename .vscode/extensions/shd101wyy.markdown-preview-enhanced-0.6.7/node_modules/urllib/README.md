# urllib

[![NPM version][npm-image]][npm-url]
[![build status][travis-image]][travis-url]
[![Build Status](https://dev.azure.com/eggjs/egg/_apis/build/status/node-modules.urllib)](https://dev.azure.com/eggjs/egg/_build/latest?definitionId=7)
[![Test coverage][codecov-image]][codecov-url]
[![David deps][david-image]][david-url]
[![Known Vulnerabilities][snyk-image]][snyk-url]
[![npm download][download-image]][download-url]

[npm-image]: https://img.shields.io/npm/v/urllib.svg?style=flat-square
[npm-url]: https://npmjs.org/package/urllib
[travis-image]: https://img.shields.io/travis/node-modules/urllib.svg?style=flat-square
[travis-url]: https://travis-ci.org/node-modules/urllib
[codecov-image]: https://codecov.io/gh/node-modules/urllib/branch/master/graph/badge.svg
[codecov-url]: https://codecov.io/gh/node-modules/urllib
[david-image]: https://img.shields.io/david/node-modules/urllib.svg?style=flat-square
[david-url]: https://david-dm.org/node-modules/urllib
[snyk-image]: https://snyk.io/test/npm/urllib/badge.svg?style=flat-square
[snyk-url]: https://snyk.io/test/npm/urllib
[download-image]: https://img.shields.io/npm/dm/urllib.svg?style=flat-square
[download-url]: https://npmjs.org/package/urllib

Request HTTP URLs in a complex world — basic
and digest authentication, redirections, cookies, timeout and more.

## Install

```bash
$ npm install urllib --save
```

## Usage

### callback

```js
var urllib = require('urllib');

urllib.request('http://cnodejs.org/', function (err, data, res) {
  if (err) {
    throw err; // you need to handle error
  }
  console.log(res.statusCode);
  console.log(res.headers);
  // data is Buffer instance
  console.log(data.toString());
});
```

### Promise

If you've installed [bluebird][bluebird],
[bluebird][bluebird] will be used.
`urllib` does not install [bluebird][bluebird] for you.

Otherwise, if you're using a node that has native v8 Promises (v0.11.13+),
then that will be used.

Otherwise, this library will crash the process and exit,
so you might as well install [bluebird][bluebird] as a dependency!

```js
var urllib = require('urllib');

urllib.request('http://nodejs.org').then(function (result) {
  // result: {data: buffer, res: response object}
  console.log('status: %s, body size: %d, headers: %j', result.res.statusCode, result.data.length, result.res.headers);
}).catch(function (err) {
  console.error(err);
});
```

### co & generator

If you are using [co](https://github.com/visionmedia/co) or [koa](https://github.com/koajs/koa):

```js
var co = require('co');
var urllib = require('urllib');

co(function* () {
  var result = yield urllib.requestThunk('http://nodejs.org');
  console.log('status: %s, body size: %d, headers: %j',
    result.status, result.data.length, result.headers);
})();
```

## Global `response` event

You should create a urllib instance first.

```js
var httpclient = require('urllib').create();

httpclient.on('response', function (info) {
  error: err,
  ctx: args.ctx,
  req: {
    url: url,
    options: options,
    size: requestSize,
  },
  res: res
});

httpclient.request('http://nodejs.org', function (err, body) {
  console.log('body size: %d', body.length);
});
```

## API Doc

### Method: `http.request(url[, options][, callback])`

#### Arguments

- **url** String | Object - The URL to request, either a String or a Object that return by [url.parse](http://nodejs.org/api/url.html#url_url_parse_urlstr_parsequerystring_slashesdenotehost).
- ***options*** Object - Optional
    - ***method*** String - Request method, defaults to `GET`. Could be `GET`, `POST`, `DELETE` or `PUT`. Alias 'type'.
    - ***data*** Object - Data to be sent. Will be stringify automatically.
    - ***dataAsQueryString*** Boolean - Force convert `data` to query string.
    - ***content*** String | [Buffer](http://nodejs.org/api/buffer.html) - Manually set the content of payload. If set, `data` will be ignored.
    - ***stream*** [stream.Readable](http://nodejs.org/api/stream.html#stream_class_stream_readable) - Stream to be pipe to the remote. If set, `data` and `content` will be ignored.
    - ***writeStream*** [stream.Writable](http://nodejs.org/api/stream.html#stream_class_stream_writable) - A writable stream to be piped by the response stream. Responding data will be write to this stream and `callback` will be called with `data` set `null` after finished writing.
    - ***files*** {Array<ReadStream|Buffer|String> | Object | ReadStream | Buffer | String - The files will send with `multipart/form-data` format, base on `formstream`. If `method` not set, will use `POST` method by default.
    - ***consumeWriteStream*** [true] - consume the writeStream, invoke the callback after writeStream close.
    - ***contentType*** String - Type of request data. Could be `json`. If it's `json`, will auto set `Content-Type: application/json` header.
    - ***nestedQuerystring*** Boolean - urllib default use querystring to stringify form data which don't support nested object, will use [qs](https://github.com/ljharb/qs) instead of querystring to support nested object by set this option to true.
    - ***dataType*** String - Type of response data. Could be `text` or `json`. If it's `text`, the `callback`ed `data` would be a String. If it's `json`, the `data` of callback would be a parsed JSON Object and will auto set `Accept: application/json` header. Default `callback`ed `data` would be a `Buffer`.
    - **fixJSONCtlChars** Boolean - Fix the control characters (U+0000 through U+001F) before JSON parse response. Default is `false`.
    - ***headers*** Object - Request headers.
    - ***timeout*** Number | Array - Request timeout in milliseconds for connecting phase and response receiving phase. Defaults to `exports.TIMEOUT`, both are 5s. You can use `timeout: 5000` to tell urllib use same timeout on two phase or set them seperately such as `timeout: [3000, 5000]`, which will set connecting timeout to 3s and response 5s.
    - ***auth*** String - `username:password` used in HTTP Basic Authorization.
    - ***digestAuth*** String - `username:password` used in HTTP [Digest Authorization](http://en.wikipedia.org/wiki/Digest_access_authentication).
    - ***agent*** [http.Agent](http://nodejs.org/api/http.html#http_class_http_agent) - HTTP Agent object.
      Set `false` if you does not use agent.
    - ***httpsAgent*** [https.Agent](http://nodejs.org/api/https.html#https_class_https_agent) - HTTPS Agent object.
      Set `false` if you does not use agent.
    - ***ca*** String | Buffer | Array - An array of strings or Buffers of trusted certificates.
      If this is omitted several well known "root" CAs will be used, like VeriSign.
      These are used to authorize connections.
      **Notes**: This is necessary only if the server uses the self-signed certificate
    - ***rejectUnauthorized*** Boolean - If true, the server certificate is verified against the list of supplied CAs.
      An 'error' event is emitted if verification fails. Default: true.
    - ***pfx*** String | Buffer - A string or Buffer containing the private key,
      certificate and CA certs of the server in PFX or PKCS12 format.
    - ***key*** String | Buffer - A string or Buffer containing the private key of the client in PEM format.
      **Notes**: This is necessary only if using the client certificate authentication
    - ***cert*** String | Buffer - A string or Buffer containing the certificate key of the client in PEM format.
      **Notes**: This is necessary only if using the client certificate authentication
    - ***passphrase*** String - A string of passphrase for the private key or pfx.
    - ***ciphers*** String - A string describing the ciphers to use or exclude.
    - ***secureProtocol*** String - The SSL method to use, e.g. SSLv3_method to force SSL version 3.
    - ***followRedirect*** Boolean - follow HTTP 3xx responses as redirects. defaults to false.
    - ***maxRedirects*** Number - The maximum number of redirects to follow, defaults to 10.
    - ***formatRedirectUrl*** Function - Format the redirect url by your self. Default is `url.resolve(from, to)`.
    - ***beforeRequest*** Function - Before request hook, you can change every thing here.
    - ***streaming*** Boolean - let you get the `res` object when request  connected, default `false`. alias `customResponse`
    - ***gzip*** Boolean - Accept gzip response content and auto decode it, default is `false`.
    - ***timing*** Boolean - Enable timing or not, default is `false`.
    - ***enableProxy*** Boolean - Enable proxy request, default is `false`.
    - ***proxy*** String | Object - proxy agent uri or options, default is `null`.
    - ***lookup*** Function - Custom DNS lookup function, default is `dns.lookup`. Require node >= 4.0.0(for http protocol) and node >=8(for https protocol)
    - ***checkAddress*** Function: optional, check request address to protect from SSRF and similar attacks. It receive tow arguments(`ip` and `family`) and should return true or false to identified the address is legal or not. It rely on `lookup` and have the same version requirement.
    - ***trace*** Boolean - Enable capture stack include call site of library entrance, default is `false`.
- ***callback(err, data, res)*** Function - Optional callback.
    - **err** Error - Would be `null` if no error accured.
    - **data** Buffer | Object - The data responsed. Would be a Buffer if `dataType` is set to `text` or an JSON parsed into Object if it's set to `json`.
    - **res** [http.IncomingMessage](http://nodejs.org/api/http.html#http_http_incomingmessage) - The response.

#### Returns

[http.ClientRequest](http://nodejs.org/api/http.html#http_class_http_clientrequest) - The request.

Calling `.abort()` method of the request stream can cancel the request.

#### Options: `options.data`

When making a request:

```js
urllib.request('http://example.com', {
  method: 'GET',
  data: {
    'a': 'hello',
    'b': 'world'
  }
});
```

For `GET` request, `data` will be stringify to query string, e.g. `http://example.com/?a=hello&b=world`.

For others like `POST`, `PATCH` or `PUT` request,
in defaults, the `data` will be stringify into `application/x-www-form-urlencoded` format
if `Content-Type` header is not set.

If `Content-type` is `application/json`, the `data` will be `JSON.stringify` to JSON data format.

#### Options: `options.content`

`options.content` is useful when you wish to construct the request body by yourself,
for example making a `Content-Type: application/json` request.

Notes that if you want to send a JSON body, you should stringify it yourself:

```js
urllib.request('http://example.com', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json'
  },
  content: JSON.stringify({
    a: 'hello',
    b: 'world'
  })
});
```

It would make a HTTP request like:

```http
POST / HTTP/1.1
Host: example.com
Content-Type: application/json

{
  "a": "hello",
  "b": "world"
}
```

This exmaple can use `options.data` with `application/json` content type:

```js
urllib.request('http://example.com', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json'
  },
  data: {
    a: 'hello',
    b: 'world'
  }
});
```

#### Options: `options.files`

Upload a file with a `hello` field.

```js
var urllib = request('urllib');

var req = urllib.request('http://my.server.com/upload', {
  files: __filename,
  data: {
    hello: 'hello urllib',
  },
}, function (err, data, res) {
  // upload finished
});
```

Upload multi files with a `hello` field.

```js
var urllib = request('urllib');

var req = urllib.request('http://my.server.com/upload', {
  files: [
    __filename,
    fs.createReadStream(__filename),
    Buffer.from('mock file content'),
  ],
  data: {
    hello: 'hello urllib with multi files',
  },
}, function (err, data, res) {
  // upload finished
});
```

Custom file field name with `uploadfile`.

```js
var urllib = request('urllib');

var req = urllib.request('http://my.server.com/upload', {
  files: {
    uploadfile: __filename,
  },
}, function (err, data, res) {
  // upload finished
});
```

#### Options: `options.stream`

Uploads a file with [formstream](https://github.com/node-modules/formstream):

```js
var urllib = require('urllib');
var formstream = require('formstream');

var form = formstream();
form.file('file', __filename);
form.field('hello', '你好urllib');

var req = urllib.request('http://my.server.com/upload', {
  method: 'POST',
  headers: form.headers(),
  stream: form
}, function (err, data, res) {
  // upload finished
});
```

### Response Object

Response is normal object, it contains:

* `status` or `statusCode`: response status code.
  * `-1` meaning some network error like `ENOTFOUND`
  * `-2` meaning ConnectionTimeoutError
* `statusMessage`: response status message.
* `headers`: response http headers, default is `{}`
* `size`: response size
* `aborted`: response was aborted or not
* `rt`: total request and response time in ms.
* `timing`: timing object if timing enable.
* `remoteAddress`: http server ip address
* `remotePort`: http server ip port
* `socketHandledRequests`: socket already handled request count
* `socketHandledResponses`: socket already handled response count

#### Response: `res.aborted`

If the underlaying connection was terminated before `response.end()` was called,
`res.aborted` should be `true`.

```js
require('http').createServer(function (req, res) {
  req.resume();
  req.on('end', function () {
    res.write('foo haha\n');
    setTimeout(function () {
      res.write('foo haha 2');
      setTimeout(function () {
        res.socket.end();
      }, 300);
    }, 200);
    return;
  });
}).listen(1984);

urllib.request('http://127.0.0.1:1984/socket.end', function (err, data, res) {
  data.toString().should.equal('foo haha\nfoo haha 2');
  should.ok(res.aborted);
  done();
});
```

### HttpClient2

HttpClient2 is a new instance for future. request method only return a promise, compatible with `async/await` and generator in co.

#### Options

options extends from urllib, besides below

- ***retry*** Number - a retry count, when get an error, it will request again until reach the retry count.
- ***retryDelay*** Number - wait a delay(ms) between retries.
- ***isRetry*** Function - determine whether retry, a response object as the first argument. it will retry when status >= 500 by default. Request error is not included.

## Proxy

Support both `http` and `https` protocol.

**Notice: Only support on Node.js >= 4.0.0**

### Programming

```js
urllib.request('https://twitter.com/', {
  enableProxy: true,
  proxy: 'http://localhost:8008',
}, (err, data, res) => {
  console.log(res.status, res.headers);
});
```

### System environment variable

- http

```bash
HTTP_PROXY=http://localhost:8008
http_proxy=http://localhost:8008
```

- https

```bash
HTTP_PROXY=http://localhost:8008
http_proxy=http://localhost:8008
HTTPS_PROXY=https://localhost:8008
https_proxy=https://localhost:8008
```

```bash
$ http_proxy=http://localhost:8008 node index.js
```

### Trace
If set trace true, error stack will contains full call stack, like
```
Error: connect ECONNREFUSED 127.0.0.1:11
    at TCPConnectWrap.afterConnect [as oncomplete] (net.js:1113:14)
    --------------------
    at ~/workspace/urllib/lib/urllib.js:150:13
    at new Promise (<anonymous>)
    at Object.request (~/workspace/urllib/lib/urllib.js:149:10)
    at Context.<anonymous> (~/workspace/urllib/test/urllib_promise.test.js:49:19)
    ....
```

When open the trace, urllib may have poor perfomance, please consider carefully.

## TODO

* [ ] Support component
* [ ] Browser env use Ajax
* [√] Support Proxy
* [√] Upload file like form upload
* [√] Auto redirect handle
* [√] https & self-signed certificate
* [√] Connection timeout & Response timeout
* [√] Support `Accept-Encoding=gzip` by `options.gzip = true`
* [√] Support [Digest access authentication](http://en.wikipedia.org/wiki/Digest_access_authentication)

<!-- GITCONTRIBUTOR_START -->

## Contributors

|[<img src="https://avatars0.githubusercontent.com/u/156269?v=4" width="100px;"/><br/><sub><b>fengmk2</b></sub>](https://github.com/fengmk2)<br/>|[<img src="https://avatars3.githubusercontent.com/u/985607?v=4" width="100px;"/><br/><sub><b>dead-horse</b></sub>](https://github.com/dead-horse)<br/>|[<img src="https://avatars2.githubusercontent.com/u/288288?v=4" width="100px;"/><br/><sub><b>xingrz</b></sub>](https://github.com/xingrz)<br/>|[<img src="https://avatars3.githubusercontent.com/u/327019?v=4" width="100px;"/><br/><sub><b>JacksonTian</b></sub>](https://github.com/JacksonTian)<br/>|[<img src="https://avatars3.githubusercontent.com/u/543405?v=4" width="100px;"/><br/><sub><b>ibigbug</b></sub>](https://github.com/ibigbug)<br/>|[<img src="https://avatars1.githubusercontent.com/u/14790466?v=4" width="100px;"/><br/><sub><b>greenkeeperio-bot</b></sub>](https://github.com/greenkeeperio-bot)<br/>|
| :---: | :---: | :---: | :---: | :---: | :---: |
|[<img src="https://avatars1.githubusercontent.com/u/360661?v=4" width="100px;"/><br/><sub><b>popomore</b></sub>](https://github.com/popomore)<br/>|[<img src="https://avatars2.githubusercontent.com/u/2569835?v=4" width="100px;"/><br/><sub><b>haoxins</b></sub>](https://github.com/haoxins)<br/>|[<img src="https://avatars3.githubusercontent.com/u/5381764?v=4" width="100px;"/><br/><sub><b>paambaati</b></sub>](https://github.com/paambaati)<br/>|[<img src="https://avatars1.githubusercontent.com/u/1147375?v=4" width="100px;"/><br/><sub><b>alsotang</b></sub>](https://github.com/alsotang)<br/>|[<img src="https://avatars1.githubusercontent.com/u/546535?v=4" width="100px;"/><br/><sub><b>leoner</b></sub>](https://github.com/leoner)<br/>|[<img src="https://avatars3.githubusercontent.com/u/1747852?v=4" width="100px;"/><br/><sub><b>isayme</b></sub>](https://github.com/isayme)<br/>|
|[<img src="https://avatars0.githubusercontent.com/u/252317?v=4" width="100px;"/><br/><sub><b>cyjake</b></sub>](https://github.com/cyjake)<br/>|[<img src="https://avatars0.githubusercontent.com/u/5856440?v=4" width="100px;"/><br/><sub><b>whxaxes</b></sub>](https://github.com/whxaxes)<br/>|[<img src="https://avatars1.githubusercontent.com/u/5139554?v=4" width="100px;"/><br/><sub><b>danielwpz</b></sub>](https://github.com/danielwpz)<br/>|[<img src="https://avatars1.githubusercontent.com/u/32407?v=4" width="100px;"/><br/><sub><b>jedahan</b></sub>](https://github.com/jedahan)<br/>|[<img src="https://avatars1.githubusercontent.com/u/17075261?v=4" width="100px;"/><br/><sub><b>nick-ng</b></sub>](https://github.com/nick-ng)<br/>|[<img src="https://avatars2.githubusercontent.com/u/1706595?v=4" width="100px;"/><br/><sub><b>rishavsharan</b></sub>](https://github.com/rishavsharan)<br/>|
|[<img src="https://avatars0.githubusercontent.com/u/535479?v=4" width="100px;"/><br/><sub><b>aleafs</b></sub>](https://github.com/aleafs)<br/>|[<img src="https://avatars1.githubusercontent.com/u/3689968?v=4" width="100px;"/><br/><sub><b>Amunu</b></sub>](https://github.com/Amunu)<br/>|[<img src="https://avatars3.githubusercontent.com/in/9426?v=4" width="100px;"/><br/><sub><b>azure-pipelines[bot]</b></sub>](https://github.com/apps/azure-pipelines)<br/>|[<img src="https://avatars3.githubusercontent.com/u/929503?v=4" width="100px;"/><br/><sub><b>yuzhigang33</b></sub>](https://github.com/yuzhigang33)<br/>|[<img src="https://avatars1.githubusercontent.com/u/981128?v=4" width="100px;"/><br/><sub><b>fishbar</b></sub>](https://github.com/fishbar)<br/>|[<img src="https://avatars2.githubusercontent.com/u/1207064?v=4" width="100px;"/><br/><sub><b>gxcsoccer</b></sub>](https://github.com/gxcsoccer)<br/>|
[<img src="https://avatars1.githubusercontent.com/u/6897780?v=4" width="100px;"/><br/><sub><b>killagu</b></sub>](https://github.com/killagu)<br/>|[<img src="https://avatars0.githubusercontent.com/u/17476119?v=4" width="100px;"/><br/><sub><b>mars-coder</b></sub>](https://github.com/mars-coder)<br/>|[<img src="https://avatars1.githubusercontent.com/u/929179?v=4" width="100px;"/><br/><sub><b>rockdai</b></sub>](https://github.com/rockdai)<br/>|[<img src="https://avatars2.githubusercontent.com/u/13050025?v=4" width="100px;"/><br/><sub><b>aladdin-add</b></sub>](https://github.com/aladdin-add)<br/>

This project follows the git-contributor [spec](https://github.com/xudafeng/git-contributor), auto updated at `Mon May 06 2019 19:30:19 GMT+0800`.

<!-- GITCONTRIBUTOR_END -->

## License

[MIT](LICENSE.txt)


[bluebird]: https://github.com/petkaantonov/bluebird
