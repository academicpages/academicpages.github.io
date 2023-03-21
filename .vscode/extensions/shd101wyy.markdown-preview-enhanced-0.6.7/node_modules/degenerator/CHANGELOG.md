1.0.4 / 2016-06-22
==================

* [[`a72ad259af`](https://github.com/TooTallNate/degenerator/commit/a72ad259af)] - rename History.md to CHANGELOG.md (Nathan Rajlich)
* [[`eadfa34af3`](https://github.com/TooTallNate/degenerator/commit/eadfa34af3)] - don't turn anonymous functions into generators (Nathan Rajlich)
* [[`285af6ba6c`](https://github.com/TooTallNate/degenerator/commit/285af6ba6c)] - update deps (Nathan Rajlich)

1.0.3 / 2016-06-22
==================

  * travis: test node v0.12, v4, iojs v1, v2, v3, v5, and v6
  * package: loosen restriction on deps
  * package: update to use newer ast-types (#8, @piotr1212)

1.0.2 / 2015-06-22
==================

  * package: update "esprima" to ~v2.3.0 (#6, @tgriesser)

1.0.1 / 2015-03-11
==================

  * package: use "https" for git URL (#1, @aarongundel)

1.0.0 / 2014-11-22
==================

  * updating to v1.0.0 for better defined semver semantics

0.0.4 / 2014-11-22
==================

  * test: fix whitespace
  * test: add test case for TooTallNate/node-pac-resolver#3
  * package: update "mocha" to v2.0.1
  * .travis: don't test node v0.9.x
  * README: use svg for Travis badge
  * test: add test case for multiple functions defined in one file
  * index: do two passes on the AST, add all local function names to `names` array
  * test: add a test fixture for the README example
  * test: add support for defining the function names from within the test fixture

0.0.3 / 2014-04-04
==================

  * package: update outdated dependencies
  * package: add "respository" field
  * index: add JSDoc comments
  * index: remove `opts` option logic
  * add .travis.yml file
  * test: initial test

0.0.2 / 2013-12-06
==================

  * index: implement the `names` array functionality
  * index: fix nested function invocations

0.0.1 / 2013-12-06
==================

  * gitignore: ignore ?.js dev files
  * README++
  * add .gitignore file
  * index: slight cleanup
  * initial commit
