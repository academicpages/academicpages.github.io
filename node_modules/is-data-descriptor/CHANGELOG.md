# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/)
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [v2.1.2](https://github.com/inspect-js/is-data-descriptor/compare/v2.1.1...v2.1.2) - 2023-10-25

### Commits

- [Refactor] use `hasown` [`77ad812`](https://github.com/inspect-js/is-data-descriptor/commit/77ad8129c7543f6826e2cbcadc015cc815ef94b7)
- [Dev Deps] update `@ljharb/eslint-config`, `aud`, `tape` [`88f2cb7`](https://github.com/inspect-js/is-data-descriptor/commit/88f2cb744242131a98086967ea4a3c5d42c6fa77)

## [v2.1.1](https://github.com/inspect-js/is-data-descriptor/compare/v2.1.0...v2.1.1) - 2023-04-27

### Commits

- [Fix] when an object/key pair is provided, check arguments.length instead of key truthiness [`72692d3`](https://github.com/inspect-js/is-data-descriptor/commit/72692d3c1184e4d1f11faecbc9446b21cf5610a1)
- [readme] remove empty section [`72ec85b`](https://github.com/inspect-js/is-data-descriptor/commit/72ec85b9c4d781d551f19e595cca91b5f933d90d)

## [v2.1.0](https://github.com/inspect-js/is-data-descriptor/compare/v2.0.0...v2.1.0) - 2023-04-27

### Commits

- [eslint] cleanup [`c18a236`](https://github.com/inspect-js/is-data-descriptor/commit/c18a23640c00f32fca39112381b5cabdaa6a9a55)
- [Tests] travis -&gt; Github Actions; add `safe-publish-latest`, `npmignore`, `auto-changelog`, `evalmd`, `aud` [`5758410`](https://github.com/inspect-js/is-data-descriptor/commit/5758410ec503add0727f2215633e5b1998c21293)
- [readme] clean up docs, URLs, package.json, etc [`28f61dd`](https://github.com/inspect-js/is-data-descriptor/commit/28f61dd676d8661ca7468e091ddf2e22bf4a8da2)
- [Docs] remove verb [`e20d28c`](https://github.com/inspect-js/is-data-descriptor/commit/e20d28cc86ce8a7cbc4beb0f306e5a4034b6d704)
- [Tests] convert from mocha to tape [`666c175`](https://github.com/inspect-js/is-data-descriptor/commit/666c1755f29668098dc07fbda0eb1d354a4da640)
- [New] increase support from node 6 down to node 0.4 [`aa43b69`](https://github.com/inspect-js/is-data-descriptor/commit/aa43b699b4a53b97e7af13f4d49eb7a21d253d99)
- [Tests] add coverage [`8f094f6`](https://github.com/inspect-js/is-data-descriptor/commit/8f094f6809514862f367c07bd879f2de42f4d9d0)
- [meta] switch from `files` field to npmignore; add `exports` [`2769e1d`](https://github.com/inspect-js/is-data-descriptor/commit/2769e1d408330b05331a40216e7a6bdce2322f69)
- [Deps] remove unused `kind-of` [`bc87bcd`](https://github.com/inspect-js/is-data-descriptor/commit/bc87bcd5f9abfa3ac8bcd2daf85ca9c380cb225d)

## [v2.0.0](https://github.com/inspect-js/is-data-descriptor/compare/v1.0.1...v2.0.0) - 2018-12-13

### Commits

- refactor [`8dcc492`](https://github.com/inspect-js/is-data-descriptor/commit/8dcc492bfb8e6d5b7964c1c566cdfe27ffbd8b0a)

## [v1.0.1](https://github.com/inspect-js/is-data-descriptor/compare/v1.0.0...v1.0.1) - 2023-10-26

### Commits

- [eslint] actually use eslint [`65fed07`](https://github.com/inspect-js/is-data-descriptor/commit/65fed07b2dde027da64f303c21a44a4375a2e2bd)
- [readme] clean up readme, remove verb [`10ad663`](https://github.com/inspect-js/is-data-descriptor/commit/10ad663093b0ed9c9c0c13c6db4ead4351b8670e)
- [meta] clean up package.json [`7f76a01`](https://github.com/inspect-js/is-data-descriptor/commit/7f76a015050fc87e9b394440c3b5283cf55b2c82)
- [meta] update `.gitignore` [`a2ca593`](https://github.com/inspect-js/is-data-descriptor/commit/a2ca593bb1173e73f23eb401e455249c71c2eda8)
- [Tests] switch to tape [`70540e5`](https://github.com/inspect-js/is-data-descriptor/commit/70540e5449ef3239051d4e40dce8a5a1978d1634)
- [Tests] migrate from travis to github actions [`eee138d`](https://github.com/inspect-js/is-data-descriptor/commit/eee138d84d57191310acf3e7fdc83f5951570188)
- [Fix] properly return false for an accessor descriptor [`2c213cd`](https://github.com/inspect-js/is-data-descriptor/commit/2c213cd67d558c169a02892dc52592ca1d5d8f40)
- [Performance] move data object to module level [`37688a1`](https://github.com/inspect-js/is-data-descriptor/commit/37688a1653f3a2a364f14bb396803413cb435963)
- [Fix] allow any non-primitive; arrays and functions are objects too [`197c77a`](https://github.com/inspect-js/is-data-descriptor/commit/197c77a39c53d12d7a091bcc029fcf7d75ce3a26)
- Only apps should have lockfiles [`20aa6e5`](https://github.com/inspect-js/is-data-descriptor/commit/20aa6e513aeb4bb84be63e278ce073c860deeade)
- [Robustness] switch to `hasown` [`aa48e2f`](https://github.com/inspect-js/is-data-descriptor/commit/aa48e2f61b3fb29e80cf655618d1573a21e8433e)
- [Fix] properly guard for-in loop [`014971e`](https://github.com/inspect-js/is-data-descriptor/commit/014971ea90715c2675511b89d05df00d4be10ecf)
- [Robustness] use a null object just in case [`ab05aad`](https://github.com/inspect-js/is-data-descriptor/commit/ab05aad03368d202505c4acde07ebc22f8da128d)

## [v1.0.0](https://github.com/inspect-js/is-data-descriptor/compare/v0.1.4...v1.0.0) - 2017-11-01

### Merged

- Update kind-of to version 6.0 [`#1`](https://github.com/inspect-js/is-data-descriptor/pull/1)
- Pin mocha to version 3 to support Node 0.12 [`#2`](https://github.com/inspect-js/is-data-descriptor/pull/2)

### Commits

- run update [`63e5992`](https://github.com/inspect-js/is-data-descriptor/commit/63e5992c6b953d652952cecb93468897ae8e5e29)
- update verb, generate readme documentation [`42dcba2`](https://github.com/inspect-js/is-data-descriptor/commit/42dcba2627fe655daa21aec843ca8de849f26cd6)
- minor edits [`23164cb`](https://github.com/inspect-js/is-data-descriptor/commit/23164cbc3496f7b13ec470781f05636ef610eecb)

## [v0.1.4](https://github.com/inspect-js/is-data-descriptor/compare/v0.1.3...v0.1.4) - 2015-12-28

### Fixed

- fixes https://github.com/jonschlinkert/is-descriptor/issues/2 [`#2`](https://github.com/jonschlinkert/is-descriptor/issues/2)

### Commits

- lint [`6d69a34`](https://github.com/inspect-js/is-data-descriptor/commit/6d69a34001d6191d7874cd28aebcdc5441f06f70)
- lint, update lazy-cache [`58bcd4e`](https://github.com/inspect-js/is-data-descriptor/commit/58bcd4ea72f000c83fb167024cf116d4c357440e)
- generate docs with verb [`e6317db`](https://github.com/inspect-js/is-data-descriptor/commit/e6317dbcb27a95281a60120bac83f5938dda4e2c)
- update docs [`fb2e768`](https://github.com/inspect-js/is-data-descriptor/commit/fb2e7689724ad948673734865999051aec2da552)
- generate docs [`bd0ea52`](https://github.com/inspect-js/is-data-descriptor/commit/bd0ea52c7a80223bedc90aadd43e466169907c2a)
- adds verb plugin [`7657b81`](https://github.com/inspect-js/is-data-descriptor/commit/7657b8188aa6fd003586bdb4e791e02dce21bc99)

## [v0.1.3](https://github.com/inspect-js/is-data-descriptor/compare/v0.1.2...v0.1.3) - 2015-10-04

### Commits

- files prop [`b0b7700`](https://github.com/inspect-js/is-data-descriptor/commit/b0b77004c51fec564e68bf6ff89fd4a169915d5b)

## [v0.1.2](https://github.com/inspect-js/is-data-descriptor/compare/v0.1.1...v0.1.2) - 2015-10-04

### Commits

- lazy-cache [`49a868c`](https://github.com/inspect-js/is-data-descriptor/commit/49a868c410a1651367315763e24c796e0b5127ce)
- update readme [`936d3f4`](https://github.com/inspect-js/is-data-descriptor/commit/936d3f4327f782c9e0d0ef120c68a81bb987ce72)

## v0.1.1 - 2015-08-31

### Commits

- first commit [`a1915ae`](https://github.com/inspect-js/is-data-descriptor/commit/a1915ae8a9a4a633d18630102264d266b6e08f08)
- 0.1.1 readme [`8fd6ad0`](https://github.com/inspect-js/is-data-descriptor/commit/8fd6ad0e1b49fa4a22293bfdd807762863afbd5e)
- 0.1.1 docs [`5e54369`](https://github.com/inspect-js/is-data-descriptor/commit/5e543699944b7ee5fe091399dc4186bcace47e3e)
- 0.1.1 docs [`8ec34af`](https://github.com/inspect-js/is-data-descriptor/commit/8ec34af8e80d0f8e386c6bff57e2e4b18d4e0afb)
- lint [`d265658`](https://github.com/inspect-js/is-data-descriptor/commit/d265658d986a688bf217461ca9c24d9c5300bdc8)
