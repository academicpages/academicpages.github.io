/*!
 * utility - benchmark/date_YYYYMMDD.js
 * Copyright(c) 2013 fengmk2 <fengmk2@gmail.com>
 * MIT Licensed
 */

"use strict";

/**
 * Module dependencies.
 */

// http://jsperf.com/access-log-date-format

var utils = require('../');
var moment = require('moment');
var Benchmark = require('benchmark');
var suite = new Benchmark.Suite();

console.log('parseInt(moment().format("YYYYMMDD"), 10): %j', parseInt(moment().format('YYYYMMDD'), 10));
console.log('utils.datestruct().YYYYMMDD: %j', utils.datestruct().YYYYMMDD);
console.log('new Date().toString(): %j', new Date().toString());
console.log('------------------------');

suite
.add("parseInt(moment().format('YYYYMMDD'), 10)", function () {
  parseInt(moment().format('YYYYMMDD'), 10);
})
.add('utils.datestruct().YYYYMMDD', function () {
  utils.datestruct().YYYYMMDD;
})
.add('new Date().toString()', function () {
  new Date().toString();
})
// add listeners
.on('cycle', function (event) {
  console.log(String(event.target));
})
.on('complete', function () {
  console.log('Fastest is ' + this.filter('fastest').pluck('name'));
})
.run({ async: false });
