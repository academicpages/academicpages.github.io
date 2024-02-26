# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/)
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [v3.0.3](https://github.com/inspect-js/is-accessor-descriptor/compare/v3.0.2...v3.0.3) - 2023-10-25

### Commits

- [Dev Deps] update `@ljharb/eslint-config`, `aud`, `has-property-descriptors`, `tape` [`908044d`](https://github.com/inspect-js/is-accessor-descriptor/commit/908044d05559496cddf61b8f634641e879305f24)
- [Refactor] use `hasown` [`8b94cc1`](https://github.com/inspect-js/is-accessor-descriptor/commit/8b94cc153ba580143fe27bab0437199e873e58e3)

## [v3.0.2](https://github.com/inspect-js/is-accessor-descriptor/compare/v3.0.1...v3.0.2) - 2023-04-27

### Commits

- [eslint] cleanup [`c0a3a34`](https://github.com/inspect-js/is-accessor-descriptor/commit/c0a3a34eabaed6634dd674600df2c647688d3a31)
- [Tests] travis -&gt; Github Actions; add `safe-publish-latest`, `npmignore`, `auto-changelog`, `evalmd`, `aud` [`a45de10`](https://github.com/inspect-js/is-accessor-descriptor/commit/a45de10c8020a350df860c2c4fe7697a74cdb943)
- [readme] clean up docs, URLs, package.json, etc [`d2f3547`](https://github.com/inspect-js/is-accessor-descriptor/commit/d2f354741f4fecc8c0e1ed6a83d351028a2ce2ba)
- [New] increase support from node 6 down to node 0.4 [`825f88e`](https://github.com/inspect-js/is-accessor-descriptor/commit/825f88e69da75476b638e9879296a37d370ce9fd)
- [Tests] convert from mocha to tape [`072d097`](https://github.com/inspect-js/is-accessor-descriptor/commit/072d097f5bbe1d6383ec38c13bbe67b491c0c671)
- [Docs] remove `verb` [`7567b54`](https://github.com/inspect-js/is-accessor-descriptor/commit/7567b54961b87af9ae890584089f5f29f19d8537)
- [Tests] use `has-property-descriptors` to skip true getter tests in older engines [`0e26d80`](https://github.com/inspect-js/is-accessor-descriptor/commit/0e26d806b7f97e23f287eac39bb352e772ac3f3b)
- [Fix] when an object/key pair is provided, check arguments.length instead of key truthiness [`3962d00`](https://github.com/inspect-js/is-accessor-descriptor/commit/3962d006fbe65dce0bc0847e278af142829057cb)
- [Tests] add coverage [`6337da4`](https://github.com/inspect-js/is-accessor-descriptor/commit/6337da417af127694412e5f18ba853f47b9a4270)
- [meta] switch from `files` field to npmignore; add `exports` [`6e870be`](https://github.com/inspect-js/is-accessor-descriptor/commit/6e870be859d17221b11b8c9f2fcb3e8a1e649598)

## [v3.0.1](https://github.com/inspect-js/is-accessor-descriptor/compare/v3.0.0...v3.0.1) - 2018-12-13

### Commits

- cleanup readme [`5cce1d2`](https://github.com/inspect-js/is-accessor-descriptor/commit/5cce1d212f887f9b4afe2b29dd95d657e1ea210c)
- remove unnecessary check [`288d4b9`](https://github.com/inspect-js/is-accessor-descriptor/commit/288d4b9f407bd7a01a606456ac40b7c29d7fd407)

## [v3.0.0](https://github.com/inspect-js/is-accessor-descriptor/compare/v2.0.0...v3.0.0) - 2018-12-13

### Commits

- refactor [`d01d897`](https://github.com/inspect-js/is-accessor-descriptor/commit/d01d897175f09d3fb285a6bb22e4eb46a46a6045)

## [v2.0.0](https://github.com/inspect-js/is-accessor-descriptor/compare/v1.0.1...v2.0.0) - 2017-12-04

### Commits

- refactor to be stricter [`f7370ef`](https://github.com/inspect-js/is-accessor-descriptor/commit/f7370efe312e338c7f3175d76b973bdd838d0d27)
- update docs [`fd1764c`](https://github.com/inspect-js/is-accessor-descriptor/commit/fd1764c14dc6bfba668cb502dad57e5e03855ecf)

## [v1.0.1](https://github.com/inspect-js/is-accessor-descriptor/compare/v1.0.0...v1.0.1) - 2023-10-26

### Commits

- [eslint] actually use eslint [`a05c057`](https://github.com/inspect-js/is-accessor-descriptor/commit/a05c0576662de977798bcba0ffa037a1ffdb9f68)
- [readme] clean up docs, URLs, package.json, etc [`6648dcd`](https://github.com/inspect-js/is-accessor-descriptor/commit/6648dcde8c01fcb36f7d6aaa3f70e3563df54b67)
- [meta] update `.gitignore` [`cba0ea0`](https://github.com/inspect-js/is-accessor-descriptor/commit/cba0ea006594dd4583ba671c1643a1e96aaab7ff)
- [readme] remove verb [`2f07da4`](https://github.com/inspect-js/is-accessor-descriptor/commit/2f07da493d0c824b5738675999ea4a3db541c84e)
- [Tests] switch to tape [`7e39202`](https://github.com/inspect-js/is-accessor-descriptor/commit/7e392020781a23f4c1276e78da4bf8a798021d85)
- [Tests] migrate from travis to github actions [`aa436b0`](https://github.com/inspect-js/is-accessor-descriptor/commit/aa436b0bbeb03c1281e816445e4d495e582274c7)
- [Fix] properly handle an accessor descriptor with only a setter [`04647f4`](https://github.com/inspect-js/is-accessor-descriptor/commit/04647f45870a2d3a78e2ae8adf07b0e9d47e0fc9)
- [Refactor] properly guard for-in loop [`a0454cc`](https://github.com/inspect-js/is-accessor-descriptor/commit/a0454cca3ea0610c8cf5e0b70bd581689ded929a)
- [Fix] allow any non-primitive; arrays and functions are objects too [`123e3c3`](https://github.com/inspect-js/is-accessor-descriptor/commit/123e3c3da341a1a397e274805df88ed13646442f)
- [Refactor] use `hasown` [`7ad36a0`](https://github.com/inspect-js/is-accessor-descriptor/commit/7ad36a05be98c7f0ae3f4dc9b3a3df1fa392c7fd)
- [readme] fix incorrect example [`3ee754a`](https://github.com/inspect-js/is-accessor-descriptor/commit/3ee754af6cb65c690ccd9ade150b33e8ec2808f8)
- [Tests] move tests to test dir [`5d70880`](https://github.com/inspect-js/is-accessor-descriptor/commit/5d70880ae2256d1f5927dab02c0bf8fe78cafef3)
- [Dev Deps] add missing `npmignore` [`97ce4bc`](https://github.com/inspect-js/is-accessor-descriptor/commit/97ce4bca878e775672e3d7349906bd7fc7db5f24)
- [Robustness] use a null object just in case [`675af5b`](https://github.com/inspect-js/is-accessor-descriptor/commit/675af5b191ebe9e18fb65c0aecb2a5ae65a535e0)

## [v1.0.0](https://github.com/inspect-js/is-accessor-descriptor/compare/v0.1.6...v1.0.0) - 2017-11-01

### Merged

- Pin mocha to version 3 to support Node 0.12 [`#3`](https://github.com/inspect-js/is-accessor-descriptor/pull/3)
- Update kind-of to version 6.0 [`#2`](https://github.com/inspect-js/is-accessor-descriptor/pull/2)

### Commits

- run update [`2489800`](https://github.com/inspect-js/is-accessor-descriptor/commit/2489800869cbecf53e9bc3596916abf2e6008edb)
- run verb to generate readme documentation [`22b0a26`](https://github.com/inspect-js/is-accessor-descriptor/commit/22b0a2617ccbebd131247c29e3700ca860d37d06)
- remove should [`4b10d2a`](https://github.com/inspect-js/is-accessor-descriptor/commit/4b10d2aa721021d5f7af69c47f49a1691a8c3fcd)

## [v0.1.6](https://github.com/inspect-js/is-accessor-descriptor/compare/v0.1.5...v0.1.6) - 2015-12-28

### Commits

- update docs [`914d85d`](https://github.com/inspect-js/is-accessor-descriptor/commit/914d85d44b914b8b693889081942bf95ea172914)
- update related projects [`92679ea`](https://github.com/inspect-js/is-accessor-descriptor/commit/92679eab1c0eb16eef052218e309aa55b10ce606)

## [v0.1.5](https://github.com/inspect-js/is-accessor-descriptor/compare/v0.1.4...v0.1.5) - 2015-12-28

### Commits

- run update [`139251c`](https://github.com/inspect-js/is-accessor-descriptor/commit/139251c5225d7cdc2b6d16e5c6c713b515643ce8)
- improve checks for valid/invalid properties [`de1be1e`](https://github.com/inspect-js/is-accessor-descriptor/commit/de1be1e6250ca2f084f5d0ac43fed8dd4f607376)
- use verb layout, add verb plugin for formatting markdown [`2324242`](https://github.com/inspect-js/is-accessor-descriptor/commit/23242429e18e6f518318cf1568ec53c636bc1085)
- run verb to generate readme [`84587a4`](https://github.com/inspect-js/is-accessor-descriptor/commit/84587a4269640683049cb06aa75ae9e33165b5fe)

## [v0.1.4](https://github.com/inspect-js/is-accessor-descriptor/compare/v0.1.3...v0.1.4) - 2015-12-20

### Commits

- lint [`d076464`](https://github.com/inspect-js/is-accessor-descriptor/commit/d0764648b3428e7f01303ea7835e25be9d1b5c21)
- generate docs [`12e2143`](https://github.com/inspect-js/is-accessor-descriptor/commit/12e2143ca3d93ece7ae73ee3fcbdb8952d7c5091)

## [v0.1.3](https://github.com/inspect-js/is-accessor-descriptor/compare/v0.1.2...v0.1.3) - 2015-10-04

### Commits

- files prop [`0bcef73`](https://github.com/inspect-js/is-accessor-descriptor/commit/0bcef73f2c7c90be7e05f3dd56f02fbe67790897)

## [v0.1.2](https://github.com/inspect-js/is-accessor-descriptor/compare/v0.1.1...v0.1.2) - 2015-10-04

### Commits

- lazy-cache [`fc6da15`](https://github.com/inspect-js/is-accessor-descriptor/commit/fc6da15ecef4a18c20f102a412d596407bb86a5c)
- update docs [`943c0cd`](https://github.com/inspect-js/is-accessor-descriptor/commit/943c0cd4d709eff029fa3880560aec27c0d0f458)

## v0.1.1 - 2015-08-31

### Commits

- first commit [`dca2279`](https://github.com/inspect-js/is-accessor-descriptor/commit/dca22793793cf208e65d8daee9d949d76252b647)
- 0.1.1 readme [`27c92b6`](https://github.com/inspect-js/is-accessor-descriptor/commit/27c92b65b85b9bfb39945d646f223cbfd262ab41)
- 0.1.1 docs [`09beed6`](https://github.com/inspect-js/is-accessor-descriptor/commit/09beed68a3c5a5ea76128d5faf2933848181750d)
- lint [`aa03d9b`](https://github.com/inspect-js/is-accessor-descriptor/commit/aa03d9ba1e65e2e71be0add9de75d25cc981e9e2)
