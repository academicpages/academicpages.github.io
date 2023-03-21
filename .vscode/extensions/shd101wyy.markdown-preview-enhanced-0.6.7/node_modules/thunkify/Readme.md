# thunkify

  Turn a regular node function into one which returns a thunk,
  useful for generator-based flow control such as [co](https://github.com/visionmedia/co).

## Installation

```
$ npm install thunkify
```

## Example

```js
var thunkify = require('thunkify');
var fs = require('fs');

var read = thunkify(fs.readFile);

read('package.json', 'utf8')(function(err, str){
  
});
```

# License

  MIT
