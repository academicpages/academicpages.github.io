copy-to
=======

[![Build Status](https://travis-ci.org/node-modules/copy-to.svg?branch=master)](https://travis-ci.org/node-modules/copy-to)

copy an object's properties to another one, include propertiy, getter and setter.

## Install

```
npm install copy-to
```

## Usage

```js
copy(src).to(des);
copy(src).toCover(des);
copy(src).override(des);

copy(src).pick('proName1', 'proName2').to(des);
copy(src).pick('proName1', 'proName2').toCover(des);
copy(src).pick('proName1', 'proName2').override(des);

copy(src).and(other).to(des);
copy(src).and(other).toCover(des);
copy(src).and(second).and(third).to(des);

copy(src).and(other).pick('proName1', 'proName2').to(des);
copy(src).and(other).pick('proName1', 'proName2').toCover(des);
copy(src).and(second).and(third).pick('proName1', 'proName2').to(des);
```

It won't copy access(getter / setter) by default, if you want to copy them, please use:

```js
copy(src).withAccess().and(other).to(des);
```

## Example

```js
var copy = require('copy-to');

var src = {
  _name: 'foo',
  set name(val) {
    this._name = val;
  },
  get name() {
    return this._name;
  },
  show: function () {
    console.log(this._name);
  }
};

var des = {
  _name: 'bar'
};

copy(src).to(des);
copy(src).toCover(des);
copy(src).pick('_name', 'name').to(des);
copy(src).pick('_name', 'name').toCover(des);
```

## License
MIT
