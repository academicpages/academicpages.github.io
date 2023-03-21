# block-stream2

transform input into equally-sized chunks as output

streams3 version of
[block-stream](https://npmjs.org/package/block-stream)

[![build status](https://secure.travis-ci.org/substack/block-stream2.png)](http://travis-ci.org/substack/block-stream2)

# example

``` js
const block = require('block-stream2');
const through = require('through2');

process.stdin
    .pipe(block({ size: 16, zeroPadding: true }))
    .pipe(through((buf, enc, next) => {
        const str = buf.toString().replace(/[\x00-\x1f]/g, chr);
        console.log(`buf[${buf.length}]=${str}`);
        next();
    }))
;
function chr (s) { return `\\x${pad(s.charCodeAt(0).toString(16),2)}` }
function pad (s, n) { return Array(n - s.length + 1).join('0') + s }
```

```
$ echo {c,d,f}{a,e,i,o,u}{t,g,r} | node example/stream.js
buf[16]=cat cag car cet
buf[16]=ceg cer cit cig
buf[16]=cir cot cog cor
buf[16]=cut cug cur dat
buf[16]=dag dar det deg
buf[16]=der dit dig dir
buf[16]=dot dog dor dut
buf[16]=dug dur fat fag
buf[16]=far fet feg fer
buf[16]=fit fig fir fot
buf[16]=fog for fut fug
buf[16]=fur\x0a\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00
```

# methods

``` js
const block = require('block-stream2');
```

## const b = block(opts)
## const b = block(size, opts)

Create a new transform stream `b` that outputs chunks of length `size` or
`opts.size`.

When `opts.zeroPadding` is false, do not zero-pad the last chunk.

# install

With [npm](https://npmjs.org) do:

```
npm install block-stream2
```

# license

MIT
