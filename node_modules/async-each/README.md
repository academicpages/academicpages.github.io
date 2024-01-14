# async-each

No-bullshit, ultra-simple, 40-lines-of-code async parallel forEach function for JavaScript.

We don't need junky 30K async libs. Really.

For browsers and node.js.

## Usage

`npm install async-each` if you're using NPM.

For browsers, just include async-each before your scripts and use global variable `asyncEach`

* `each(array, iterator, callback)` — `Array`, `Function`, `(optional) Function`
* `iterator(item, next)` receives current item and a callback that will mark the item as done. `next` callback receives optional `error, transformedItem` arguments.
* `callback(error, transformedArray)` optionally receives first error and transformed result `Array`.

```javascript
var each = require('async-each');
each(['a.js', 'b.js', 'c.js'], fs.readFile, function(error, contents) {
  if (error) console.error(error);
  console.log('Contents for a, b and c:', contents);
});

asyncEach(list, fn, callback); // use global var in browser
```

## License

The MIT License (MIT)

Copyright (c) 2016 Paul Miller [(paulmillr.com)](https://paulmillr.com)

See [LICENSE](https://github.com/paulmillr/async-each/blob/master/LICENSE) file.
