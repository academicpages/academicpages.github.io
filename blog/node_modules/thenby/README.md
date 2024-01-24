<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->


- [thenBy.js usage](#thenbyjs-usage)
    - [Sort by property names](#sort-by-property-names)
    - [Sort by unary functions](#sort-by-unary-functions)
  - [Extra options](#extra-options)
    - [Sort descending](#sort-descending)
    - [Case insensitive sorting](#case-insensitive-sorting)
    - [Custom compare function](#custom-compare-function)
    - [Internationalization: Using javascripts native `Intl.Collator`](#internationalization-using-javascripts-native-intlcollator)
  - [A word on performance](#a-word-on-performance)
  - [Installing](#installing)
    - [Install in your HTML](#install-in-your-html)
    - [Install using npm or yarn](#install-using-npm-or-yarn)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

# thenBy.js usage

  [![NPM Version][npm-image]][npm-url]
  [![NPM Downloads][downloads-image]][downloads-url]

`thenBy` is a javascript micro library that helps sorting arrays on multiple keys. It allows you to use the [native Array::sort() method](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/sort) of javascript, but pass in multiple functions to sort that are composed with `firstBy().thenBy().thenBy()` style.

Example:
```javascript
// first by length of name, then by population, then by ID
data.sort(
    firstBy(function (v1, v2) { return v1.name.length - v2.name.length; })
    .thenBy(function (v1, v2) { return v1.population - v2.population; })
    .thenBy(function (v1, v2) { return v1.id - v2.id; })
);
```
`thenBy` also offers some nice shortcuts that make the most common ways of sorting even easier and more readable.

### Sort by property names
Javascript sorting relies heavily on passing discriminator functions that return -1, 0 or 1 for a pair of items. While this is very flexible, often you want to sort on the value of a simple property. As a convenience, thenBy.js builds the appropriate compare function for you if you pass in a property name (instead of a function). The example above would then look like this:
```javascript
// first by length of name, then by population, then by ID
data.sort(
    firstBy(function (v1, v2) { return v1.name.length - v2.name.length; })
    .thenBy("population")
    .thenBy("id")
);
```

If an element doesn't have the property defined, it will sort like the empty string (""). Typically, this will be at the top.

### Sort by unary functions
You can also pass a function that takes a single item and returns its sorting key. This turns the above expression into:
```javascript
// first by length of name, then by population, then by ID
data.sort(
    firstBy(function (v) { return v.name.length; })
    .thenBy("population")
    .thenBy("id")
);
```

Note that javascript contains a number of standard functions that can be passed in here as well. The Number() function will make your sorting sort on numeric values instead of lexical values:
```javascript
var values = ["2", "20", "03", "-2", "0", 200, "2"];
var sorted = values.sort(firstBy(Number));
```
## Extra options
### Sort descending
thenBy.js allows you to pass in a second parameter for `direction`. If you pass in 'desc' or -1, the sorting will be reversed. So:
```javascript
// first by length of name descending, then by population descending, then by ID ascending
data.sort(
    firstBy(function (v1, v2) { return v1.name.length - v2.name.length; }, -1)
    .thenBy("population", "desc")
    .thenBy("id")
);
```

### Case insensitive sorting
(as of v1.2.0) All of the shortcut methods allow you to sort case insensitive as well. The second parameter expects an options object (if it is a number, it is interpreted as `direction` as above). The ignoreCase property can be set to true, like this:
```javascript
// first by name, case insensitive, then by population
data.sort(
    firstBy("name", {ignoreCase:true})
    .thenBy("population")
);
```
If you want to use both descending and ignoreCase, you have to use the options syntax for direction as well:
```javascript
// sort by name, case insensitive and descending
data.sort(firstBy("name", {ignoreCase:true, direction:"desc"}));
```
### Custom compare function
If you have more specific wishes for the exact sort order, but still want to use the convenience of unary functions or sorting on property names, you can pass in you own compare function in the options. Here we use a compare function that known about the relative values of playing cards::

```javascript
const cards = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'];
var cardCompare = (c1, c2) =>{
    return cards.indexOf(c1) - cards.indexOf(c2);
}
var handOfCards =  [
        { id: 7, suit:"c", card:"A" },
        { id: 8, suit:"d", card:"10" },
        // etc
    ];
handOfCards.sort(firstBy("card", {cmp: cardCompare, direction: "desc"}));

```
You can use the `cmp` function together with `direction`, but not with `ignoreCase` (for obvious reasons). 

### Internationalization: Using javascripts native `Intl.Collator`
One of the more interesting custom compare functions you may want to pass in is the native `compare` function that is exposed by `Intl.Collator`. This compare function knows about the different sorting rules in different cultures. Many browsers have these implemented, but in NodeJS, the API is implemented, but only for the English culture. You would use it with thenBy like this:

```javascript
// in German, ä sorts with a
var germanCompare = new Intl.Collator('de').compare;
// in Swedish, ä sorts after z
var swedishCompare = new Intl.Collator('sv').compare;
data.sort(
    firstBy("name", {cmp: swedishCompare})
);
```
Check the [details on using Intl.Collator](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Collator).

## A word on performance
thenBy constructs a comparer function for you. It does this by combining the functions you pass in with a number of small utility functions that perform tasks like "reverting", "combining the current sort order with the previous one", etc. Also, these operations try to work correctly, no matter what content is in the sorted array. There are two steps here that cost time: constructing the über-function and running it. The construction time should always be negligible. The run time however can be slower than when you carefully handcraft the compare function. Still, *normally you shouldn't worry about this*, but if you're sorting very large sets, it could matter. For example, there is some overhead in making several small functions call each other instead of creating one piece of code. Also, if you know your data well, and know that a specific field is *alwways present* and is *always a number*, you could code a significantly faster compare function then thenBy's results. The unit tests contain an extreme example.

If you use thenBy to combine multiple compare functions into one (where each function expects two parameters), the difference is small. Using unary functions adds some overhead, using direction:desc adds some, using only a property name adds a little, but will check for missing values, which could be optimized. Ignoring case will slow down, but not more so than when handcoded.   

## Installing
### Install in your HTML
To include it into your page/project, just paste the minified code from https://raw.github.com/Teun/thenBy.js/master/thenBy.min.js into yours (699 characters). If you don't want the `firstBy` function in your global namespace, you can assign it to a local variable (see sample.htm).

### Install using npm or yarn
```npm install thenby```

or

```yarn add thenby```

then in your app:

```var firstBy = require('thenby');```

or in TypeScript/ES6:

```import {firstBy} from "thenby";```

For a small demo of how TypeScript support looks in a good editor (i.e. VS Code), [check this short video](https://youtu.be/mKJovFLyxro).


Thanks a lot to [bergus](https://github.com/bergus), [hagabaka](https://github.com/hagabaka), [infolyzer](https://github.com/infolyzer) and [Foxhoundn](https://github.com/Foxhoundn) for their improvements.
Thanks to [jsgoupil](https://github.com/jsgoupil) and [HonoluluHenk](https://github.com/HonoluluHenk) for their help on the TypeScript declaration.


[npm-image]: https://img.shields.io/npm/v/thenby.svg
[npm-url]: https://npmjs.org/package/thenby
[downloads-image]: https://img.shields.io/npm/dm/thenby.svg
[downloads-url]: https://npmjs.org/package/thenby
