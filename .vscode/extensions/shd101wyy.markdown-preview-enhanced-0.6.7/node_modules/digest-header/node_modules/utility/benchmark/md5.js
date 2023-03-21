/*!
 * utility - benchmark/md5.js
 *
 * Copyright(c) 2013 fengmk2 <fengmk2@gmail.com>
 * MIT Licensed
 */

"use strict";

/**
 * Module dependencies.
 */

var utils = require('../');
var Benchmark = require('benchmark');
var suite = new Benchmark.Suite();

console.log("utils.md5({foo: 'bar', bar: 'foo', v: [1, 2, 3]})", utils.md5({foo: 'bar', bar: 'foo', v: [1, 2, 3]}));
console.log("utils.md5(JSON.stringify({foo: 'bar', bar: 'foo', v: [1, 2, 3]}))",
  utils.md5(JSON.stringify({foo: 'bar', bar: 'foo', v: [1, 2, 3]})));
console.log("utils.md5('苏千')", utils.md5('苏千'));
console.log('------------------------');

suite
.add("utils.md5({foo: 'bar', bar: 'foo', v: [1, 2, 3]})", function () {
  utils.md5({foo: 'bar', bar: 'foo', v: [1, 2, 3]});
})
.add("utils.md5(JSON.stringify({foo: 'bar', bar: 'foo', v: [1, 2, 3]})))", function () {
  utils.md5(JSON.stringify({foo: 'bar', bar: 'foo', v: [1, 2, 3]}));
})
.add("utils.md5('苏千')", function () {
  utils.md5('苏千');
})

// add listeners
.on('cycle', function (event) {
  console.log(String(event.target));
})
.on('complete', function () {
  console.log('Fastest is ' + this.filter('fastest').pluck('name'));
})
.run({ async: false });
