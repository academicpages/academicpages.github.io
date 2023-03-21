
2.35.0 / 2020-05-15
==================

**features**
  * [[`47c21bd`](http://github.com/node-modules/urllib/commit/47c21bd93648080589bdc6528d9e9cf3e0489951)] - feat: change header to lowercase (#337) (TZ | 天猪 <<atian25@qq.com>>)

**fixes**
  * [[`8f2ca64`](http://github.com/node-modules/urllib/commit/8f2ca648608995d140d0ca3873ef728bdbd4ee41)] - fix: need to handle response data on close event (#340) (fengmk2 <<fengmk2@gmail.com>>)
  * [[`175ad2b`](http://github.com/node-modules/urllib/commit/175ad2b3e17196626c701ef72396dd6932d14c7a)] - fix: res.socket is null in node-v14.x (#339) (hyj1991 <<yeekwanvong@gmail.com>>)

2.34.2 / 2019-12-09
==================

**fixes**
  * [[`67d5b1c`](http://github.com/node-modules/urllib/commit/67d5b1c35dc302778aa4b992ea4998fe427e3cc8)] - fix: index.d.ts (#334) (Daniels.Sun <<better.sunjian@gmail.com>>)

2.34.1 / 2019-09-02
==================

**fixes**
  * [[`3da9339`](http://github.com/node-modules/urllib/commit/3da9339aacf4aa59c17b40ff1793d320bc9d9f61)] - fix: rejectUnauthorized under Node.js 12 (#328) (Khaidi Chu <<i@2333.moe>>)

**others**
  * [[`061f600`](http://github.com/node-modules/urllib/commit/061f60075249c136b1ca7e1e2519dae25cb9e55d)] - test: add a test case for posting xml data to reflect #69 (#324) (Jeff <<jeff.tian@outlook.com>>)

2.34.0 / 2019-05-07
==================

**features**
  * [[`11f5d34`](http://github.com/node-modules/urllib/commit/11f5d34ea3d8aafbda4f3f5345d6dcfe7e20daa2)] - feat: support multipart/form-data by default (#322) (fengmk2 <<fengmk2@gmail.com>>)

**others**
  * [[`3c24781`](http://github.com/node-modules/urllib/commit/3c2478100f8490a0fd6f4c49772c682d38fcf43e)] - chore: update contributors (fengmk2 <<fengmk2@gmail.com>>)

2.33.4 / 2019-05-06
==================

**fixes**
  * [[`1f9566c`](http://github.com/node-modules/urllib/commit/1f9566c3dbb0be02e895647ced2d8eba06ce28aa)] - fix: don't parse URL on node 4 (#321) (fengmk2 <<fengmk2@gmail.com>>)
  * [[`3384e53`](http://github.com/node-modules/urllib/commit/3384e53e8447a5cb06402a43d07d7eb19a24bb62)] - fix: normalize url with WHATWG URL to solve #319 (#320) (Chen Yangjian <<252317+cyjake@users.noreply.github.com>>)

2.33.3 / 2019-04-11
==================

**others**
  * [[`e08f71a`](http://github.com/node-modules/urllib/commit/e08f71af8c261318289d056260a156eca9d6a274)] - upgrade: proxy-agent@3.1.0 (#315) (薛定谔的猫 <<weiran.zsd@outlook.com>>)

2.33.2 / 2019-03-26
==================

**fixes**
  * [[`a2a8a1d`](http://github.com/node-modules/urllib/commit/a2a8a1de8088f1a1b6f96de9e9c2cee408bc165b)] - fix: only copy enumerable and ownProperty value of args.headers (#313) (fengmk2 <<fengmk2@gmail.com>>)

2.33.1 / 2019-03-21
==================

**fixes**
  * [[`f8091ce`](http://github.com/node-modules/urllib/commit/f8091ce41885178f4a1b50d6daf79a77bdead9f0)] - fix: cancel connect timer when done is called (Daniel Wang <<danielwpz@gmail.com>>)

2.33.0 / 2019-01-09
==================

**features**
  * [[`a5df9d5`](http://github.com/node-modules/urllib/commit/a5df9d5257a8d18dd0d71f7c76aff7f6464e9484)] - feat: add typescript definition (#308) (Haoliang Gao <<sakura9515@gmail.com>>)

**others**
  * [[`47ad864`](http://github.com/node-modules/urllib/commit/47ad864eba92a1e0f5a730adad6e8582af3fdbd8)] - test: add test case for streaming timeout (#307) (Yiyu He <<dead_horse@qq.com>>)

2.32.0 / 2019-01-07
==================

**features**
  * [[`a42445e`](http://github.com/node-modules/urllib/commit/a42445edfcaa17b9840afa8b4e06d1928d58ab53)] - feat: Expose status message from original Response (#306) (GP ✅ <<exchequer598@gmail.com>>)

2.31.3 / 2018-11-30
==================

**fixes**
  * [[`98a1622`](http://github.com/node-modules/urllib/commit/98a16225aa21b37c2bfbfe318fe1803eedbd2d0c)] - fix: ensure timeout error is handled when request with stream (#305) (Yiyu He <<dead_horse@qq.com>>)

**others**
  * [[`2bb86c0`](http://github.com/node-modules/urllib/commit/2bb86c0fe1f34cf8d12e397158e714a86f697093)] - test: only use junit report on azure-pipelines (#304) (fengmk2 <<fengmk2@gmail.com>>)
  * [[`bd869c7`](http://github.com/node-modules/urllib/commit/bd869c704387d3159ca50bf1976c6c70358b3ee4)] - test: Publish test results to Azure Pipelines (#303) (Rishav Sharan <<rishav.sharan@microsoft.com>>)

2.31.2 / 2018-11-13
==================

**fixes**
  * [[`227618a`](http://github.com/node-modules/urllib/commit/227618ad0ceef68b409ba7ec9328bdcaba513b3e)] - fix: allow agent set to null (#301) (fengmk2 <<fengmk2@gmail.com>>)

2.31.1 / 2018-11-01
==================

**fixes**
  * [[`83fc316`](http://github.com/node-modules/urllib/commit/83fc3165aa477bd7b034c075ae133a52627fc12b)] - fix: Omit the 'Accept-Encoding' header if it is explicitly set to 'null' (#298) (GP ✅ <<exchequer598@gmail.com>>)
  * [[`36c24c3`](http://github.com/node-modules/urllib/commit/36c24c3f54b6115c178540803a9ffae733bba063)] - fix: should autofix socket timeout by request.timeout (#300) (fengmk2 <<fengmk2@gmail.com>>)

2.31.0 / 2018-10-24
==================

**features**
  * [[`28c38d2`](http://github.com/node-modules/urllib/commit/28c38d2451d85669decfdaf16ea07eaf958d41eb)] - feat: support agentkeepalive@4 (#297) (fengmk2 <<fengmk2@gmail.com>>)
  * [[`c79eefc`](http://github.com/node-modules/urllib/commit/c79eefc9843fb6a2aeb9e728ed4f8f912e8866ad)] - feat: Do not set User-Agent if the header is explicitly set to null (GP <<exchequer598@gmail.com>>)

2.30.0 / 2018-09-26
==================

**features**
  * [[`b760530`](http://github.com/node-modules/urllib/commit/b76053020923f4d99a1c93cf2e16e0c5ba10bacf)] - feat: implement trace option like mysql client (#290) (killa <<killa123@126.com>>)

**others**
  * [[`5e80ee8`](http://github.com/node-modules/urllib/commit/5e80ee8f3e8992da98b0a270de5a9298627841c7)] - test: run ci on azure-pipelines (#292) (azure-pipelines[bot] <<azure-pipelines[bot]@users.noreply.github.com>>)

2.29.1 / 2018-07-26
==================

**fixes**
  * [[`ab39245`](http://github.com/node-modules/urllib/commit/ab39245ecb8d75f56b559c193b26c4a19e7bbbfe)] - fix: keep exists accept header on dataType = json (#289) (fengmk2 <<fengmk2@gmail.com>>)

2.29.0 / 2018-07-03
==================

**features**
  * [[`4ca0c48`](http://github.com/node-modules/urllib/commit/4ca0c486699ff9e7e8b59f381a963a1133b59a96)] - feat: add socket handled request and response count (#288) (fengmk2 <<fengmk2@gmail.com>>)

2.28.1 / 2018-06-01
==================

**fixes**
  * [[`6bc31b9`](http://github.com/node-modules/urllib/commit/6bc31b9af77bbf5c4acab7e430116b071160b6d5)] - fix: use pump to close request stream (#287) (fengmk2 <<fengmk2@gmail.com>>)

**others**
  * [[`8087683`](http://github.com/node-modules/urllib/commit/8087683710118088891a580666b149181e1cab86)] - test: add node 10 support (#285) (fengmk2 <<fengmk2@gmail.com>>)

2.28.0 / 2018-05-25
==================

**features**
  * [[`c0221ff`](http://github.com/node-modules/urllib/commit/c0221ff08934519bacbcf96660f126d5d6279c02)] - feat: support deflate compress for response (#283) (iSayme <<isaymeorg@gmail.com>>)

**others**
  * [[`60ea1f6`](http://github.com/node-modules/urllib/commit/60ea1f653a29e0c8949fb3be5d82fe1fddf2a0f3)] - test: update url, the /:package/* not avalable anymore (#284) (iSayme <<isaymeorg@gmail.com>>)

2.27.0 / 2018-03-26
==================

**features**
  * [[`a6c93fd`](http://github.com/node-modules/urllib/commit/a6c93fd07e75e45c6eda09c732d0b72ff5dc9199)] - feat: support args.checkAddress (#279) (Yiyu He <<dead_horse@qq.com>>)

2.26.0 / 2018-02-28
==================

**features**
  * [[`d6e7c58`](http://github.com/node-modules/urllib/commit/d6e7c58b3688d415091ddc0c845b7cb8d57e20cc)] - feat: support Keep-Alive Header (#275) (fengmk2 <<fengmk2@gmail.com>>)

2.25.4 / 2018-01-18
==================

**fixes**
  * [[`9c496a0`](http://github.com/node-modules/urllib/commit/9c496a0510ee17f72129e1298cf310a8b1aee327)] - fix: Changed to "new (require('proxy-agent'))(proxy)" (#273) (Nick Ng <<nick-ng@users.noreply.github.com>>)

2.25.3 / 2017-12-29
==================

**fixes**
  * [[`e3df75e`](http://github.com/node-modules/urllib/commit/e3df75e249f67c943ac42d61abd1649291ba5f74)] - fix: res.requestUrls should be string array (#271) (hui <<kangpangpang@gmail.com>>)

2.25.2 / 2017-12-28
==================

**fixes**
  * [[`2df6906`](http://github.com/node-modules/urllib/commit/2df6906d188bc53aa2d24efa0d318e52cccf9d78)] - fix: make sure request event url should be a string (#270) (hui <<kangpangpang@gmail.com>>)

2.25.1 / 2017-10-20
==================

**fixes**
  * [[`ac9bc64`](http://github.com/node-modules/urllib/commit/ac9bc645149ffa5d9a1e8450ba00721a92d18f13)] - fix: don't change args.headers (#267) (fengmk2 <<fengmk2@gmail.com>>)

**others**
  * [[`b798546`](http://github.com/node-modules/urllib/commit/b798546ef240de7a4dbe8ba5feb05536a4912b1b)] - docs: fixed spelling mistake (#266) (Axes <<whxaxes@qq.com>>)

2.25.0 / 2017-09-08
==================

**features**
  * [[`95cabd6`](http://github.com/node-modules/urllib/commit/95cabd650ffb4996819570dea2518dea875d8452)] - feat: support custom fixJSONCtlChars function (#264) (fengmk2 <<fengmk2@gmail.com>>)

2.24.0 / 2017-07-31
==================

  * feat: support http(s) proxy (#226)

2.23.0 / 2017-07-18
==================

  * test: skip test.webdav.org test cases
  * feat: add defaultArgs on HttpClient

2.22.0 / 2017-04-10
==================

  * feat: add options.nestedQuerystring (#254)

2.21.2 / 2017-03-19
==================

  * fix: don't listen response aborted on node > 0.12 (#252)

2.21.1 / 2017-03-16
==================

  * fix: throw when write to stream timeout (#251)

2.21.0 / 2017-02-27
==================

  * fix: should pass options to httpclient2 (#249)
  * test: fix Promise not defined on 0.10
  * test: use assert instead of should
  * feat: add retry delay on httpclient2

2.20.0 / 2017-02-06
==================

  * deps: bump deps versions
  * fix: keep the same req object across request and response event

2.19.0 / 2016-12-14
==================

  * feat: add `dataAsQueryString` params for convert data to query string (#240)

2.18.0 / 2016-12-07
==================

  * fix: use nextTick to prevent promise handling error.
  * refactor: move to separated files
  * feat: add retry option

2.17.1 / 2016-11-25
==================

  * add environment detection for connect timer, because no socket event in browser env (#236)

2.17.0 / 2016-10-13
==================

  * feat: add -2 status for connect timeout (#224)

2.16.1 / 2016-10-10
==================

  * fix: parse content-type (#221)

2.16.0 / 2016-09-27
==================

  * feat: add custom dns lookup function (#220)

2.15.1 / 2016-09-26
==================

  * fix: httpclient support set agent to false (#219)

2.15.0 / 2016-09-21
==================

  * feat: export remoteAddress and remotePort (#216)

2.14.0 / 2016-09-19
==================

  * feat: allow user to rewrite redirect url (#214)

2.13.2 / 2016-09-18
==================

  * fix: response size should use last one (#213)

2.13.1 / 2016-09-10
==================

  * fix: add missing ctx on request event (#210)

2.13.0 / 2016-08-09
==================

  * feat: timing (#204)
  * docs: fix res.aborted description

2.12.0 / 2016-08-08
==================

  * feat: support connect and response timeouts (#201)

2.11.1 / 2016-08-04
==================

  * fix: catch http.request sync error (#199)

2.11.0 / 2016-06-26
==================

  * deps: upgrade deps from ~ to ^ (#189)

2.10.0 / 2016-06-21
==================

  * feat: add an options consumeWriteStream (#187)
  * chore(package): update statuses to version 1.3.0 (#174)

2.9.1 / 2016-05-09
==================

  * fix: check url before request (#172)
  * chore(package): update any-promise to version 1.2.0 (#171)

2.9.0 / 2016-04-21
==================

  * feat: log all requested urls (#169)
  * deps: agentkeepalive@2.1.1

2.8.0 / 2016-02-27
==================

  * test: improve coverage
  * feat: http default protocol for URL argument

2.7.3 / 2016-02-27
==================

  * deps: upgrade out of date deps

2.7.2 / 2016-02-25
==================

  * test: support windows
  * fix: keep headers.Host on `location: /foo` redirect
  * test: use npmjs.com on travis ci
  * fix: jshint style
  * deps: any-promise instead of native-or-blubird

2.7.1 / 2016-02-02
==================

  * fix: clean up headers.Host before redirect request start
  * chore: update authors

2.7.0 / 2016-01-14
==================

  * feat: response event include data property
  * chore: Add host info into debug

2.6.0 / 2015-12-09
==================

 * test: fix unstable test cases
 * feat: enhance global events
 * chore(package): update semver to version 5.1.0
 * chore(package): update should to version 7.1.1

2.5.0 / 2015-09-30
==================

 * test: fix test url
 * feat: remove request# in error message
 * test: add streaming upload test
 * test: use codecov.io

2.4.0 / 2015-08-20
==================

 * feat: add options.fixJSONCtlChars to fix JSON control characters
 * Fix a typo in comment

2.3.11 / 2015-08-12
==================

 * fix: httpclient support curl too

2.3.10 / 2015-08-12
==================

 * fix: add alias urllib.curl()
 * chore: add decodeBodyByCharset error debug log

2.3.9 / 2015-07-23
==================

 * feat: show json format data when json parse error

2.3.8 / 2015-06-06
==================

 * fix: need to clear timer after follow redirect

2.3.7 / 2015-06-04
==================

 * test: use cnpmjs.org instead of taobao.com
 * fix: need to resume res before next redirect request start

2.3.6 / 2015-06-03
==================

 * fix: support 303, 305, 307 redirect status code

2.3.5 / 2015-05-11
==================

 * fix: followRedirect support customResponse.

2.3.4 / 2015-04-19
==================

 * feat: show agent status message when request error

2.3.3 / 2015-03-30
==================

 * fix: add ciphers and secureProtocol params support for https request

2.3.2 / 2015-03-29
==================

 * refactor: httpclient custom agent property

2.3.1 / 2015-03-08
==================

 * fix: auto decode gzip content

2.3.0 / 2015-02-16
==================

 * feat: mark off connection state and response state

2.2.2 / 2015-01-21
==================

 * remove unuse event handlers

2.2.1 / 2014-12-10
==================

 * refactor and add more comments
 * add path to error (@coderhaoxin)
 * fix promise example in readme

2.2.0 / 2014-11-28
==================

 * add customResponse option (@fishbar)

2.1.0 / 2014-11-15
==================

 * humanize timeout

2.0.2 / 2014-11-01
==================

 * chore: bump deps version and make test more stable
 * refactor: dont add new property on res object

2.0.1 / 2014-10-15
==================

 * add args.contentType option (@coderhaoxin)
 * Simply the HTTPClient implementation (@JacksonTian)
 * refine urllib code (@JacksonTian)

2.0.0 / 2014-10-13
==================

 * support auto decode charset when dataType set

1.5.2 / 2014-09-15
==================

 * do not check ssl, fix hang up in some node version

1.5.1 / 2014-09-10
==================

 * httpclient add requestThunk()

1.5.0 / 2014-09-10
==================

 * add requestThunk to support co

1.4.1 / 2014-08-28
==================

 * HttpClient support agent and httpsAgent

1.4.0 / 2014-08-27
==================

 * add SocketAssignTimeoutError. #37

1.3.1 / 2014-08-27
==================

 * convert data to string when dataType is text

1.3.0 / 2014-08-26
==================

 * add urllib instance

1.2.1 / 2014-08-26
==================

 * add args.ctx for response event easy logging

1.2.0 / 2014-08-26
==================

 * format Response object fields

1.1.0 / 2014-08-25
==================

 * global `response` event. fixed #35

1.0.0 / 2014-08-25
==================

 * return Promise when callback missing. fixed #33
 * rm Makefile
 * use flat image

0.5.17 / 2014-08-08
==================

 * Remove aborted. joyent/node#7457
 * missing I in urllib logo

0.5.16 / 2014-05-15
==================

 * fix test cases
 * change .once to .on (@alsotang)

0.5.15 / 2014-05-04
==================

 * make callback is optional. close #29
 * rm 0.8 from travis

0.5.14 / 2014-04-21
==================

 * fix #28 user-agent logic bug

0.5.13 / 2014-03-31
==================

 * use digest-header module

0.5.12 / 2014-03-29
==================

 * support Digest access authentication. fix #27
 * add co-urllib desc

0.5.11 / 2014-03-13 
==================

  * improve user-agent, add node version and plaform detail

0.5.10 / 2014-03-11 
==================

  * if body not decode, dont touch it

0.5.9 / 2014-03-10 
==================

  * Support `options.gzip = true` to handle gzip response. fixed #26

0.5.8 / 2014-03-07 
==================

  * remove buffer-concat

0.5.7 / 2014-03-07 
==================

  * no more deps on buffer-concat
  * add default User-Agent: node-urllib/x.x.x
  * add jshint

0.5.6 / 2014-03-05 
==================

  * add data/res to error
  * fix typo (@coderhaoxin)
  * access npmjs.org https
  * fix test cases and use autod
  * install from cnpm
  * no more support on node 0.6.x

0.5.5 / 2013-12-10 
==================

  * should pass done instead of callback and end the writeStream
  * support args.writeStream with follow redirect (@dead-horse)

0.5.4 / 2013-11-09 
==================

  * fix timeout not effect bug

0.5.3 / 2013-10-18 
==================

  * add args.beforeRequest(options) hook to change options before http send

0.5.2 / 2013-09-23 
==================

  * add JSONResponseFormatError; append request url infomation to err.message

0.5.1 / 2013-08-23 
==================

  * detect connect timeout or response timeout fixed #18
  * update doc

0.5.0 / 2013-08-11 
==================

  * Support max redirects to protect loop redirect
  * Auto redirect handle (@ibigbug)

0.4.4 / 2013-08-10 
==================

  * handle json response to null when data size is zero

0.4.3 / 2013-08-10 
==================

  * Auto convert data to json string when content-type is 'json' fixed #15
  * add drone.io status build image

0.4.2 / 2013-08-10 
==================

  * fix SELF_SIGNED_CERT_IN_CHAIN test case on node 0.8 and 0.6
  * [√] https & self-signed certificate

0.4.1 / 2013-08-05 
==================

  * return RemoteSocketClosedError when Remote socket was terminated before `response.end()` was called

0.4.0 / 2013-08-05 
==================

  * If the underlaying connection was terminated before `response.end()` was called, `res.aborted` should be `true`. fixed #14
  * fixed test case for 0.6
  * add res.socket.end() test cases
  * remove 0.11 from travis

0.3.8 / 2013-08-02 
==================

  * add debug log

0.3.7 / 2013-07-11 
==================

  * PATCH method is also "application/x-www-form-urlencoded" by default
  * replace logo

0.3.6 / 2013-07-11 
==================

  * fixed bug in processing query string #13 (@xingrz)
  * updated readme example (@xingrz)
  * update authors
  * API docs (@xingrz)

0.3.5 / 2013-07-10 
==================

  * fixed writeSteam receive incomplete bug
  * update makefile
  * add coveralls
  * remove 0.11 from travis
  * add patch for node 0.6
  * fixed https request timeout tests
  * use blanket instead of jscover

0.3.4 / 2013-03-06 
==================

  * fixed #8 auto add application/x-www-form-urlencoded
  * fixed existsSync for node < 0.8

0.3.3 / 2012-12-14 
==================

  * support writeStream

0.3.2 / 2012-11-08 
==================

  * fixed #4 support urllib.request(options, args, callback)
  * fixed usage demo bug
  * fixed readme

0.3.1 / 2012-11-05 
==================

  * fixed #2 support stream and return the req object.
  * use jscover instead of jscoverage

0.3.0 / 2012-10-10 
==================

  * add coverage results
  * Bash auth support: `http://user:password@http://demo.com` .
