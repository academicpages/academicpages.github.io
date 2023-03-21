'use strict';

var EventEmitter = require('events').EventEmitter;
var util = require('util');
var utility = require('utility');
var urllib = require('./urllib');

module.exports = HttpClient;

function HttpClient(options) {
  EventEmitter.call(this);
  options = options || {};

  if (options.agent !== undefined) {
    this.agent = options.agent;
    this.hasCustomAgent = true;
  } else {
    this.agent = urllib.agent;
    this.hasCustomAgent = false;
  }

  if (options.httpsAgent !== undefined) {
    this.httpsAgent = options.httpsAgent;
    this.hasCustomHttpsAgent = true;
  } else {
    this.httpsAgent = urllib.httpsAgent;
    this.hasCustomHttpsAgent = false;
  }
  this.defaultArgs = options.defaultArgs;
}
util.inherits(HttpClient, EventEmitter);

HttpClient.prototype.request = HttpClient.prototype.curl = function (url, args, callback) {
  if (typeof args === 'function') {
    callback = args;
    args = null;
  }
  args = args || {};
  if (this.defaultArgs) {
    args = utility.assign({}, [ this.defaultArgs, args ]);
  }
  args.emitter = this;
  args.agent = getAgent(args.agent, this.agent);
  args.httpsAgent = getAgent(args.httpsAgent, this.httpsAgent);
  return urllib.request(url, args, callback);
};

HttpClient.prototype.requestThunk = function (url, args) {
  args = args || {};
  if (this.defaultArgs) {
    args = utility.assign({}, [ this.defaultArgs, args ]);
  }
  args.emitter = this;
  args.agent = getAgent(args.agent, this.agent);
  args.httpsAgent = getAgent(args.httpsAgent, this.httpsAgent);
  return urllib.requestThunk(url, args);
};

function getAgent(agent, defaultAgent) {
  return agent === undefined ? defaultAgent : agent;
}
