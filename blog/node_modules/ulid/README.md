<h1 align="center">
	<br>
	<br>
	<img width="360" src="logo.png" alt="ulid">
	<br>
	<br>
	<br>
</h1>

[![Build Status](https://travis-ci.org/ulid/javascript.svg?branch=master)](https://travis-ci.org/ulid/javascript) [![codecov](https://codecov.io/gh/ulid/javascript/branch/master/graph/badge.svg)](https://codecov.io/gh/ulid/javascript)
[![npm](https://img.shields.io/npm/dm/localeval.svg)](https://www.npmjs.com/package/ulid)

# Universally Unique Lexicographically Sortable Identifier

UUID can be suboptimal for many uses-cases because:

- It isn't the most character efficient way of encoding 128 bits of randomness
- UUID v1/v2 is impractical in many environments, as it requires access to a unique, stable MAC address
- UUID v3/v5 requires a unique seed and produces randomly distributed IDs, which can cause fragmentation in many data structures
- UUID v4 provides no other information than randomness which can cause fragmentation in many data structures

Instead, herein is proposed ULID:

- 128-bit compatibility with UUID
- 1.21e+24 unique ULIDs per millisecond
- Lexicographically sortable!
- Canonically encoded as a 26 character string, as opposed to the 36 character UUID
- Uses Crockford's base32 for better efficiency and readability (5 bits per character)
- Case insensitive
- No special characters (URL safe)
- Monotonic sort order (correctly detects and handles the same millisecond)

## Installation

```
npm install --save ulid
```

## Import

**TypeScript, ES6+, Babel, Webpack, Rollup, etc.. environments**
```javascript
import { ulid } from 'ulid'

ulid() // 01ARZ3NDEKTSV4RRFFQ69G5FAV
```

**CommonJS environments**
```javascript
const ULID = require('ulid')

ULID.ulid()
```

**AMD (RequireJS) environments**
```javascript
define(['ULID'] , function (ULID) {
  ULID.ulid()
});
```

**Browser**
```html
<script src="/path/to/ulid.js"></script>
<script>
    ULID.ulid()
</script>
```

## Usage

To generate a ULID, simply run the function!

```javascript
import { ulid } from 'ulid'

ulid() // 01ARZ3NDEKTSV4RRFFQ69G5FAV
```

### Seed Time

You can also input a seed time which will consistently give you the same string for the time component. This is useful for migrating to ulid.

```javascript
ulid(1469918176385) // 01ARYZ6S41TSV4RRFFQ69G5FAV
```

### Monotonic ULIDs

To generate monotonically increasing ULIDs, create a monotonic counter.

*Note that the same seed time is being passed in for this example to demonstrate its behaviour when generating multiple ULIDs within the same millisecond*

```javascript
import { monotonicFactory } from 'ulid'

const ulid = monotonicFactory()

// Strict ordering for the same timestamp, by incrementing the least-significant random bit by 1
ulid(150000) // 000XAL6S41ACTAV9WEVGEMMVR8
ulid(150000) // 000XAL6S41ACTAV9WEVGEMMVR9
ulid(150000) // 000XAL6S41ACTAV9WEVGEMMVRA
ulid(150000) // 000XAL6S41ACTAV9WEVGEMMVRB
ulid(150000) // 000XAL6S41ACTAV9WEVGEMMVRC

// Even if a lower timestamp is passed (or generated), it will preserve sort order
ulid(100000) // 000XAL6S41ACTAV9WEVGEMMVRD
```

### Pseudo-Random Number Generators

`ulid` automatically detects a suitable (cryptographically-secure) PRNG. In the browser it will use `crypto.getRandomValues` and on node it will use `crypto.randomBytes`.

#### Allowing the insecure `Math.random`

By default, `ulid` will not use `Math.random`, because that is insecure. To allow the use of `Math.random`, you'll have to use `factory` and `detectPrng`.

```javascript
import { factory, detectPrng } from 'ulid'

const prng = detectPrng(true) // pass `true` to allow insecure
const ulid = factory(prng)

ulid() // 01BXAVRG61YJ5YSBRM51702F6M
```

#### Use your own PRNG

To use your own pseudo-random number generator, import the factory, and pass it your generator function.

```javascript
import { factory } from 'ulid'
import prng from 'somewhere'

const ulid = factory(prng)

ulid() // 01BXAVRG61YJ5YSBRM51702F6M
```

You can also pass in a `prng` to the `monotonicFactory` function.

```javascript
import { monotonicFactory } from 'ulid'
import prng from 'somewhere'

const ulid = monotonicFactory(prng)

ulid() // 01BXAVRG61YJ5YSBRM51702F6M
```

## Implementations in other languages

Refer to [ulid/spec](https://github.com/ulid/spec)

## Specification

Refer to [ulid/spec](https://github.com/ulid/spec)

## Test Suite

```
npm test
```

## Performance

```
npm run perf
```

```
ulid
336,331,131 op/s » encodeTime
102,041,736 op/s » encodeRandom
17,408 op/s » generate


Suites:  1
Benches: 3
Elapsed: 7,285.75 ms
```
