'use strict';

var util = require('util');
var debug = require('debug')('urllib');
var ms = require('humanize-ms');
var HttpClient = require('./httpclient');

var _Promise;

module.exports = HttpClient2;

function HttpClient2(options) {
  HttpClient.call(this, options);
}

util.inherits(HttpClient2, HttpClient);

HttpClient2.prototype.request = HttpClient2.prototype.curl = function request(url, args) {
  var self = this;
  args = args || {};
  args.retry = args.retry || 0;
  if (args.retryDelay) {
    args.retryDelay = ms(args.retryDelay);
  }
  args.isRetry = args.isRetry || function(res) {
    return res.status >= 500;
  };
  return HttpClient.prototype.request.call(self, url, args)
  .then(function(res) {
    if (args.retry > 0 && typeof args.isRetry === 'function' && args.isRetry(res)) {
      args.retry--;
      debug('retry request %s, remain %s', url, args.retry);
      if (args.retryDelay) {
        debug('retry after %sms', args.retryDelay);
        return sleep(args.retryDelay).then(function() { return self.request(url, args); });
      }
      return self.request(url, args);
    }
    return res;
  })
  .catch(function(err) {
    if (args.retry > 0) {
      args.retry--;
      debug('retry request %s, remain %s, err %s', url, args.retry, err);
      if (args.retryDelay) {
        debug('retry after %sms', args.retryDelay);
        return sleep(args.retryDelay).then(function() { return self.request(url, args); });
      }
      return self.request(url, args);
    }
    throw err;
  });
};

HttpClient2.prototype.requestThunk = function requestThunk(url, args) {
  var self = this;
  return function(callback) {
    self.request(url, args)
    .then(function(res) {
      var cb = callback;
      // make sure cb(null, res) throw error won't emit catch callback below
      callback = null;
      cb(null, res);
    })
    .catch(function(err) {
      if (!callback) {
        // TODO: how to handle this error?
        return;
      }
      callback(err);
    });
  };
};

function sleep(ms) {
  if (!_Promise) {
    _Promise = require('any-promise');
  }

  return new _Promise(function(resolve) {
    setTimeout(resolve, ms);
  });
}
