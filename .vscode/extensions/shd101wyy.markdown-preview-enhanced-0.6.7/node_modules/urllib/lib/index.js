'use strict';

var urllib = require('./urllib');

exports.USER_AGENT = urllib.USER_AGENT;
exports.TIMEOUT = urllib.TIMEOUT;
exports.TIMEOUTS = urllib.TIMEOUTS;
exports.agent = urllib.agent;
exports.httpsAgent = urllib.httpsAgent;

exports.curl = urllib.curl;
exports.request = urllib.request;
exports.requestWithCallback = urllib.requestWithCallback;
exports.requestThunk = urllib.requestThunk;

exports.HttpClient = require('./httpclient');
exports.HttpClient2 = require('./httpclient2');

exports.create = function (options) {
  return new exports.HttpClient(options);
};
