/*!
 * utility - benchmark/get_paramnames.js
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

var foo = function (cid, startDate, endDate, rate, callback) {
  console.log('Date.now(): %j', Date.now());
  console.log('Date.now(): %j', Date.now());
  console.log('Date.now(): %j', Date.now());
  console.log('Date.now(): %j', Date.now());
  console.log('Date.now(): %j', Date.now());
  console.log('Date.now(): %j', Date.now());
  console.log('Date.now(): %j', Date.now());
  console.log('Date.now(): %j', Date.now());
  console.log('Date.now(): %j', Date.now());
  console.log('Date.now(): %j', Date.now());
  console.log('Date.now(): %j', Date.now());
  console.log('Date.now(): %j', Date.now());
  console.log('Date.now(): %j', Date.now());
  console.log('Date.now(): %j', Date.now());
  console.log('Date.now(): %j', Date.now());
  console.log('Date.now(): %j', Date.now());
  console.log('Date.now(): %j', Date.now());
  console.log('Date.now(): %j', Date.now());
};

console.log('cache:', utils.getParamNames(foo));
console.log('no cache:', utils.getParamNames(foo, false));
console.log('------------------------');

suite
.add("utils.getParamNames(foo)", function () {
  utils.getParamNames(foo);
})
.add("utils.getParamNames(foo, false) no cache", function () {
  utils.getParamNames(foo, false);
})

// add listeners
.on('cycle', function (event) {
  console.log(String(event.target));
})
.on('complete', function () {
  console.log('Fastest is ' + this.filter('fastest').pluck('name'));
})
.run({ async: false });
