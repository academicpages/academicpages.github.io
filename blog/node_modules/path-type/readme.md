# path-type

> Check if a path is a file, directory, or symlink

## Install

```
$ npm install path-type
```

## Usage

```js
import {isFile} from 'path-type';

console.log(await isFile('package.json'));
//=> true
```

## API

### isFile(path)

Check whether the passed `path` is a file.

Returns a `Promise<boolean>`.

#### path

Type: `string`

The path to check.

### isDirectory(path)

Check whether the passed `path` is a directory.

Returns a `Promise<boolean>`.

### isSymlink(path)

Check whether the passed `path` is a symlink.

Returns a `Promise<boolean>`.

### isFileSync(path)

Synchronously check whether the passed `path` is a file.

Returns a `boolean`.

### isDirectorySync(path)

Synchronously check whether the passed `path` is a directory.

Returns a `boolean`.

### isSymlinkSync(path)

Synchronously check whether the passed `path` is a symlink.

Returns a `boolean`.

---

<div align="center">
	<b>
		<a href="https://tidelift.com/subscription/pkg/npm-path-type?utm_source=npm-path-type&utm_medium=referral&utm_campaign=readme">Get professional support for this package with a Tidelift subscription</a>
	</b>
	<br>
	<sub>
		Tidelift helps make open source sustainable for maintainers while giving companies<br>assurances about security, maintenance, and licensing for their dependencies.
	</sub>
</div>
