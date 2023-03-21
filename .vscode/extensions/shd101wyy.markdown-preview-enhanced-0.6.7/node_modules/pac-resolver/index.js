'use strict';

/**
 * Module dependencies.
 */

var co = require('co');
var vm = require('vm');
var parse = require('url').parse;
var thunkify = require('thunkify');
var degenerator = require('degenerator');

/**
 * Built-in PAC functions.
 */

var dateRange = require('./dateRange');
var dnsDomainIs = require('./dnsDomainIs');
var dnsDomainLevels = require('./dnsDomainLevels');
var dnsResolve = require('./dnsResolve');
var isInNet = require('./isInNet');
var isPlainHostName = require('./isPlainHostName');
var isResolvable = require('./isResolvable');
var localHostOrDomainIs = require('./localHostOrDomainIs');
var myIpAddress = require('./myIpAddress');
var shExpMatch = require('./shExpMatch');
var timeRange = require('./timeRange');
var weekdayRange = require('./weekdayRange');

/**
 * Module exports.
 */

module.exports = generate;

/**
 * Returns an asyncronous `FindProxyForURL` function from the
 * given JS string (from a PAC file).
 *
 * @param {String} str JS string
 * @param {Object} opts optional "options" object
 * @return {Function} async resolver function
 */

function generate (_str, opts) {
  var i;
  var str = String(_str)

  // the sandbox to use for the vm
  var sandbox = {
    dateRange: dateRange,
    dnsDomainIs: dnsDomainIs,
    dnsDomainLevels: dnsDomainLevels,
    dnsResolve: dnsResolve,
    isInNet: isInNet,
    isPlainHostName: isPlainHostName,
    isResolvable: isResolvable,
    localHostOrDomainIs: localHostOrDomainIs,
    myIpAddress: myIpAddress,
    shExpMatch: shExpMatch,
    timeRange: timeRange,
    weekdayRange: weekdayRange
  };

  // copy the properties from the user-provided `sandbox` onto ours
  if (opts && opts.sandbox) {
    for (i in opts.sandbox) {
      sandbox[i] = opts.sandbox[i];
    }
  }

  // construct the array of async function names to add `yield` calls to.
  // user-provided async functions added to the `sandbox` must have an
  // `async = true` property set on the function instance
  var names = [];
  for (i in sandbox) {
    if (sandbox[i].async) {
      names.push(i);
      sandbox[i] = thunkify(sandbox[i]);
    }
  }
  //console.log(names);

  // convert the JS FindProxyForURL function into a generator function
  var js = degenerator(str, names);

  // filename of the pac file for the vm
  var filename = (opts && opts.filename) || 'proxy.pac';

  // evaluate the JS string and extract the FindProxyForURL generator function
  var fn = vm.runInNewContext(js + ';FindProxyForURL', sandbox, filename);
  if ('function' != typeof fn) {
    throw new TypeError('PAC file JavaScript contents must define a `FindProxyForURL` function');
  }

  // return the async resolver function
  var resolver = co.wrap(fn);

  return function FindProxyForURL (url, _host, _callback) {
    let host
    let callback
    switch (arguments.length) {
      case 3:
        host = _host
        callback = _callback
        break;
      case 2:
        if (typeof _host === 'function') {
          callback = _host
        } else {
          host = _host
        }
        break;
    }

    if (!host) {
      host = parse(url).hostname;
    }

    const promise = resolver(url, host, callback);

    if (typeof callback === 'function') {
      toCallback(promise, callback)
    } else {
      return promise
    }
  };
}

function toCallback (promise, callback) {
  let called = false
  function resolve(rtn) {
    if (called) return
    called = true
    callback(null, rtn)
  }
  function reject(err) {
    if (called) return
    called = true
    callback(err)
  }
  promise.then(resolve, reject)
}
