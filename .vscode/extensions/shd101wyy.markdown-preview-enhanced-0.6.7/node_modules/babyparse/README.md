Baby Parse
=========

Fast and reliable CSV parser based on [Papa Parse](http://papaparse.com). Papa Parse is for the browser, Baby Parse is for Node.js.

This package has all the functionality of Papa Parse except for web workers and parsing directly from files. You can pass a string to Baby Parse and use any of the other config options as described in the [Papa Parse documentation](http://papaparse.com/docs).

Installation
-----

```js
// simply install using npm
npm install babyparse
```

Basic Usage
-----

```js
// pass in the contents of a csv file
parsed = Baby.parse(csv);

// voila
rows = parsed.data;
```


Parse File(s)
-----

Baby Parse will assume the input is a filename if it ends in .csv or .txt.

```js
// Parse single file
parsed = Baby.parseFiles(file[, config])

rows = parsed.data
```

```js
// Parse multiple files
// Files can be either an array of strings or objects { file: filename[, config: config] }
// When using and array of objects and you include a config it will be used in place of the global config
parsed = Baby.parseFiles(files[, globalConfig])

rows = parsed[index].data
```


For a complete understanding of the power of this library, please refer to the [Papa Parse web site](http://papaparse.com).


Credits
-------

Rich Harris forked Papa Parse to make Baby Parse. [Matt Holt](https://twitter.com/mholt6) (the author of Papa Parse) helps maintain this fork.


License
-------

The original PapaParse is MIT licensed. So is BabyParse.
