# onchange

Use glob patterns to watch file sets and run a command when anything is added, changed or deleted.

## Install

```sh
npm install onchange
```

## Usage

```sh
onchange 'app/**/*.js' 'test/**/*.js' -- npm test
```

You can match as many glob patterns as you like, just put the command you want to run after the `--` and it will run any time a file matching any of the globs is added changed or deleted.

If you want a more verbose output, include the `-v` flag. For example:

```sh
onchange 'app/**/*.js' 'test/**/*.js' -v -- npm test
```

To use the event and file that changed, use `{{event}}` or `{{changed}}` anywhere in the command after `--`. For example:

```sh
onchange '**/*.js' -- echo '{{event}} to {{changed}}'
```

To execute the command on the first run, include the `-i` flag: For example:

```sh
onchange '**/*.js' -i -- npm start
```

To exclude matches:

```sh
onchange '**/*.ts' -e 'dist/**/*.js' -- tslint
```

To wait for the current process to exit between restarts:

```sh
onchange '**/*.js' -w -- npm test
```

## TypeScript

Includes [typings](index.d.ts) for TypeScript users.

---

### Copyright (c) 2013 Stephen Belanger

#### Licensed under MIT License

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
