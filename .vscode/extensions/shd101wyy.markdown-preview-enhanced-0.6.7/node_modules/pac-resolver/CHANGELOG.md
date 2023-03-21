3.0.0 / 2017-06-13
==================

* [[`bc67e2f3c6`](https://github.com/TooTallNate/node-pac-resolver/commit/bc67e2f3c6)] - **BREAKING**: return a Promise from `FindProxyForURL()` (Nathan Rajlich)
* [[`d75f37bd85`](https://github.com/TooTallNate/node-pac-resolver/commit/d75f37bd85)] - document Promise based API (Nathan Rajlich)
* [[`e746acef18`](https://github.com/TooTallNate/node-pac-resolver/commit/e746acef18)] - coerce the input JS into a String (Nathan Rajlich)
* [[`bb61571ec9`](https://github.com/TooTallNate/node-pac-resolver/commit/bb61571ec9)] - update "mocha" to v3.4.2 (Nathan Rajlich)
* [[`ab5177faa4`](https://github.com/TooTallNate/node-pac-resolver/commit/ab5177faa4)] - add "use strict" (Nathan Rajlich)
* [[`db58c2c5e8`](https://github.com/TooTallNate/node-pac-resolver/commit/db58c2c5e8)] - update dependencies (Nathan Rajlich)
* [[`28ddb49d7b`](https://github.com/TooTallNate/node-pac-resolver/commit/28ddb49d7b)] - remove Node.js 0.8 npm update command from Travis-CI (Nathan Rajlich)
* [[`2289c0478c`](https://github.com/TooTallNate/node-pac-resolver/commit/2289c0478c)] - fix commit URLs in changelog (Nathan Rajlich)
* [[`132efe7c15`](https://github.com/TooTallNate/node-pac-resolver/commit/132efe7c15)] - test Node 8 in Travis (Nathan Rajlich)

2.0.0 / 2016-09-26
==================

* [[`df860eb96b`](https://github.com/TooTallNate/node-pac-resolver/commit/df860eb96b)] - **BREAKING** remove "regenerator", drops Node.js < v1 support (Nathan Rajlich)

1.3.0 / 2016-09-26
==================

* [[`58a3f9e62e`](https://github.com/TooTallNate/node-pac-resolver/commit/58a3f9e62e)] - Implemented `timeRange` function (Utsav Kesharwani) (#15)
* [[`a93a815f0d`](https://github.com/TooTallNate/node-pac-resolver/commit/a93a815f0d)] - Implemented `weekdayRange` function (Utsav Kesharwani) (#14)
* [[`8af3e689eb`](https://github.com/TooTallNate/node-pac-resolver/commit/8af3e689eb)] - **test**: fix typo in test names (Nathan Rajlich)
* [[`e0ddf63765`](https://github.com/TooTallNate/node-pac-resolver/commit/e0ddf63765)] - **travis**: test Node.js v0.8, v1, v2, v3, v4, v5, and v6 (Nathan Rajlich)
* [[`e3c28eedec`](https://github.com/TooTallNate/node-pac-resolver/commit/e3c28eedec)] - **myIpAddress**: fallback to querying local system for IP (tehdeadone) (#10)
* [[`40de3f9a22`](https://github.com/TooTallNate/node-pac-resolver/commit/40de3f9a22)] - **package**: require "degenerator" at least v1.0.2 (Nathan Rajlich)
* [[`29009b3c38`](https://github.com/TooTallNate/node-pac-resolver/commit/29009b3c38)] - **package**: specify any "mocha" v2 (Nathan Rajlich)

1.2.6 / 2015-02-21
==================

  * package: update "regenerator" to v0.8.3 (#9, @RichardLitt)

1.2.5 / 2015-02-20
==================

  * travis: test node v0.12, don't test v0.8, v0.11
  * update regenerator to newest version (#7, @RichardLitt)
  * fix spelling errors (#4, @RichardLitt)
  * README: use svg for Travis-CI badge

1.2.4 / 2014-11-22
==================

  * package: downgrade "co" back down to v3.0.6

1.2.3 / 2014-11-22
==================

  * package: update "co" to v3.1.0
  * package: update "degenerator" to v1.0.0
  * test: add test case for #3

1.2.2 / 2014-05-20
==================

  * package: update "regenerator" to v0.4.7
  * package: update "thunkify" to v2.1.1
  * package: use ~ for "netmask" version
  * package: update "co" to v3.0.6
  * .travis: don't test node v0.9.x

1.2.1 / 2014-04-04
==================

  * package: update outdated dependencies

1.2.0 / 2014-01-28
==================

  * README: document the `opts` options argument
  * README: document how to add custom functions to the sandbox
  * refactor: only add `yield` calls to the real async functions

1.1.0 / 2014-01-25
==================

  * index: make the `filename` configurable
  * index: make the `sandbox` configurable
  * index: add an `opts` argument
  * README++

1.0.0 / 2014-01-08
==================

  * index: don't default to "DIRECT" if a falsey value is returned

0.0.2 / 2013-12-29
==================

  * package: update "netmask" to v1.0.4
  * test: fix test names
  * myIpAddress: add comment about Google Public DNS
  * myIpAddress: use a slightly better host/port combo
  * test: fix test names
  * test: add "official docs Example #5" tests
  * test: add "official docs Example #1b tests
  * test: add "official docs Example #1 tests
  * add `timeRange()` skeleton function
  * add `dateRange()` skeleton function
  * add `weekdayRange()` skeleton function
  * index: add `isResolvable()` to the sandbox
  * implement `isResolvable()`

0.0.1 / 2013-12-09
==================

  * .gitignore: ignore local dev files
  * shExpMatch: implement basic "shell expression" functionality
  * package: remove "minimatch"
  * test: add initial `shExpMatch()` function tests
  * myIpAddress: refactor to use a different "technique"
  * myIpAddress: trying to debug failing Travis-CI...
  * test: add `myIpAddress()` test
  * isInNet: properly implement the `isInNet()` function
  * dnsResolve: switch to `dns.lookup()`
  * dnsDomainLevels: fix typo
  * test: add `dnsDomainLevels()` tests
  * test: add `dnsDomainIs()` tests
  * test: add `dnsResolve()` tests
  * dnsResolve: return a "string", not an Array
  * dnsResolve: use `dns.resolve4()`
  * test: add isPlainHostName() tests
  * implement `localHostOrDomainIs()`
  * package: remove --harmony-generators flag from `npm test`
  * dnsDomainIs: add examples to jsdocs
  * shExpMatch: fix comment
  * add .travis.yml file
  * implement `dnsDomainLevels()`
  * implement `myIpAddress()`
  * add README.md
  * add initial `isInNet()` implementation
  * isPlainHostName: fix comment
  * implement `dnsResolve()`
  * test: initial test cases
  * implement `isPlainHostName()`
  * index: expose `shExpMatch` to the sandbox
  * index: pass the `url` and `host` variables into the resolver
  * shExpMatch: turn into a thunk
  * index: cache the regenerator `wrapGenerator` function
  * dnsDomainIs: turn into a thunk
  * use `degenerator` to compile the PAC proxy file
  * package: update "description"
  * package: using "mocha" for `npm test`
  * index: default the return value to "DIRECT"
  * initial commit
