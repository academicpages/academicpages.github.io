
1.16.3 / 2019-11-20
==================

**fixes**
  * [[`cf79437`](http://github.com/node-modules/utility/commit/cf794378d9a567b2acdbe894fb0fe86bb11c8e31)] - fix: do not use ECMAScript6 syntax. (#52) (ULIVZ <<472590061@qq.com>>)

1.16.2 / 2019-11-19
==================

**fixes**
  * [[`bb8f5d4`](http://github.com/node-modules/utility/commit/bb8f5d4becb61df6e8ce1788a172f8ae4e9937b4)] - fix: getParamNames throw when input is not function (#51) (Daniels.Sun <<better.sunjian@gmail.com>>)

**others**
  * [[`7016803`](http://github.com/node-modules/utility/commit/7016803364f22c70c42da59870eee64dd1d99020)] - build: add node 12 in ci (dead-horse <<dead_horse@qq.com>>)

1.16.1 / 2019-03-25
==================

**fixes**
  * [[`a8b0c0d`](http://github.com/node-modules/utility/commit/a8b0c0d38e7d2f6c85169975cfc7f2f1a033c310)] - fix: detect number first before check NaN (#48) (fengmk2 <<fengmk2@gmail.com>>)

1.16.0 / 2019-03-25
==================

**features**
  * [[`16104be`](http://github.com/node-modules/utility/commit/16104befbfde9c2a0bf95b88029436c4a182b1bb)] - feat: add getOwnEnumerables(obj, ignoreNull) (#47) (fengmk2 <<fengmk2@gmail.com>>)

1.15.1 / 2019-03-13
==================

**features**
  * [[`b092817`](http://github.com/node-modules/utility/commit/b092817be0c4de459bde180e754ba4872e715027)] - feat: support for ts (#45) (yyge <<33921398+ddzy@users.noreply.github.com>>)

**others**
  * [[`09bd9d0`](http://github.com/node-modules/utility/commit/09bd9d061b57a2ef6b24a39b41063f51cf251fc1)] - chore: package.json files add [index.d.ts] (#46) (ccccQ <<chenqiuws@gmail.com>>)
  * [[`7c102f4`](http://github.com/node-modules/utility/commit/7c102f4aff81e44b96629d692ce74f22cc02919f)] - test: travis support windows (#40) (fengmk2 <<fengmk2@gmail.com>>)
  * [[`fdd2d27`](http://github.com/node-modules/utility/commit/fdd2d27ce99c25458795ad1e7555370498c051bd)] - chore: fix typo function name of sha256 (#39) (fengmk2 <<fengmk2@gmail.com>>)

1.15.0 / 2018-09-12
==================

**features**
  * [[`e3ae527`](http://github.com/node-modules/utility/commit/e3ae5277161e8870e097897f0dd41cd783170182)] - feat: add utility.unescape (#38) (Yiyu He <<dead_horse@qq.com>>)

**others**
  * [[`50fb750`](http://github.com/node-modules/utility/commit/50fb750d0f24b7b47f0ef6e2ba5c42e5b2c7166a)] - chore: use ^ as deps version (#37) (fengmk2 <<fengmk2@gmail.com>>)

1.14.0 / 2018-06-29
==================

**features**
  * [[`d401917`](http://github.com/node-modules/utility/commit/d401917f20f89c52be237279d575c695f1bf6ae0)] - feat: add replacer and space to writeJSON* (#34) (Khaidi Chu <<i@2333.moe>>)

1.13.1 / 2017-10-17
==================

**fixes**
  * [[`fbbf905`](http://github.com/node-modules/utility/commit/fbbf905880185dce1e9cf980112a0f0b890e5969)] - fix: don't use arrow function (#31) (Yiyu He <<dead_horse@qq.com>>)

1.13.0 / 2017-10-17
==================

**features**
  * [[`8a84707`](https://github.com/node-modules/utility.git/commit/8a847077b4d543193e4ca2f9ff69068a48d84909)] - feat: add readJSON and writeJSON (#29) (Haoliang Gao <<sakura9515@gmail.com>>)

1.12.0 / 2017-04-19
==================

  * feat: add includesInvalidHttpHeaderChar() to detect invalid char
  * test: add url test for replaceInvalidHttpHeaderChar
  * chore: remove unused comments
  * feat: replacement support function format

1.11.0 / 2017-02-21
==================

  * feat: add utility.assign (#27)

1.10.0 / 2017-02-14
==================

  * feat: add replace invalid http header character (#26)

1.9.0 / 2016-11-14
==================

  * feat: add utils.random function (#25)
  * bench: add Array.from(arguments) bench test

1.8.0 / 2016-05-09
==================

  * feat(array): impl faster splice one element on array (#24)

1.7.1 / 2016-05-03
==================

  * refactor: use faster empty object instead of Object.create(null) (#23)

1.7.0 / 2016-04-07
==================

  * benchmark: update arguments to array
  * chore: add doc
  * feat: add utility.argumentsToArray
  * chore: add david-dm status badge
  * deps: remove unuse mm module
  * test: use ava and nyc instead of mocha and istanbul
  * bench: add string and tpl string benchmark

1.6.0 / 2015-12-04
==================

 * refactor: use escape-html

1.5.0 / 2015-11-25
==================

 * feat: utility.dig
 * test(date): fix timezone on test assert
 * feat(date): make YYYYMMDDHHmmss() support param not Date
 * test: use codecov.io

1.4.0 / 2015-05-22
==================

 * feat(JSON): add strict JSON parse

1.3.2 / 2015-05-08
==================

 * feat(crypto): add sha256 hash

1.3.1 / 2015-04-09
==================

 * fix(crypto): base64decode support return buffer

1.3.0 / 2015-01-31
==================

  * feat(string): add string replace

1.2.1 / 2014-11-14
==================

 * setImmediate support argmuents

1.2.0 / 2014-09-14
==================

 * add utility.try

1.1.0 / 2014-08-23
==================

 * add split(str, sep=,)

1.0.0 / 2014-08-01
==================

 * remove address methods, please use `address` module

0.1.16 / 2014-07-07
==================

 * fix deps

0.1.15 / 2014-07-07
==================

 * YYYYMMDDHHmmss() support custom dateSep

0.1.14 / 2014-06-25
==================

 * support `YYYYMMDD(d, sep)`
 * add YYYYMMDDHHmmss benchmark
 * add sha1 to readme
 * add random string benchmark

0.1.13 / 2014-04-24
==================

 * utils.YYYYMMDDHHmmssSSS(','); // '2013-04-17 14:43:02,674'

0.1.12 / 2014-04-03
==================

 * support var map = util.map({a: 1})

0.1.11 / 2014-03-15 
==================

  * add sha1()
  * remove config from scripts

0.1.10 / 2014-01-08 
==================

  * add randomString() and has() (@dead-horse)
  * install from cnpm

0.1.9 / 2013-12-09 
==================

  * add YYYYMMDD()

0.1.8 / 2013-11-25 
==================

  * support sub object md5

0.1.7 / 2013-11-23 
==================

  * support timestamp string

0.1.6 / 2013-11-23 
==================

  * parse timestamp

0.1.5 / 2013-11-23 
==================

  * hash object
  * add npm image

0.1.4 / 2013-11-16 
==================

  * utils.setImmediate()
  * fix test case

0.1.3 / 2013-10-23 
==================

  * add number utils: toSafeNumber()

0.1.2 / 2013-10-07 
==================

  * add utils.YYYYMMDDHHmmss()

0.1.1 / 2013-09-23 
==================

  * add base64 format md5

0.1.0 / 2013-09-03 
==================

  * add timestamp()

0.0.13 / 2013-07-31 
==================

  * move getIP() to address, fixed #2

0.0.12 / 2013-06-27 
==================

  * utils.getParamNames(): get a function parameters names

0.0.11 / 2013-06-25 
==================

  * fixed interface name wrong on liunx

0.0.10 / 2013-06-25 
==================

  * add getIP()
  * add more test cases

0.0.9 / 2013-05-08 
==================

  * Safe encodeURIComponent and decodeURIComponent

0.0.8 / 2013-05-06 
==================

  * add randomSlice() fixed #1

0.0.7 / 2013-04-17 
==================

  * fixed timezone +0000 and test cases

0.0.6 / 2013-04-17 
==================

  * utils.logDate(); // '2013-04-17 14:43:02.674'

0.0.5 / 2013-04-16 
==================

  * faster accesslogDate() impl
  * add benchmark

0.0.4 / 2013-04-16 
==================

  * add accessLogDate()

0.0.3 / 2013-03-06 
==================

  * add hmac()
  * update copyright year
  * update md5 readme

0.0.2 / 2013-01-31 
==================

  * add base64 encode and urlsafe base64 encode
  * add html escape()
  * update makefile

0.0.1 / 2012-11-13 
==================

  * first commit
