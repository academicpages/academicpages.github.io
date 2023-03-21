'use strict';

var debug = require('debug')('urllib:detect_proxy_agent');
var getProxyFromURI = require('./get_proxy_from_uri');

var proxyAgents = {};

function detectProxyAgent(uri, args) {
  if (!args.enableProxy && !process.env.URLLIB_ENABLE_PROXY) {
    return null;
  }
  var proxy = args.proxy || process.env.URLLIB_PROXY;
  if (!proxy) {
    proxy = getProxyFromURI(uri);
    if (!proxy) {
      return null;
    }
  }

  var proxyAgent = proxyAgents[proxy];
  if (!proxyAgent) {
    debug('create new proxy %s', proxy);
    // lazy require, only support node >= 4
    proxyAgent = proxyAgents[proxy] = new (require('proxy-agent'))(proxy);
  }
  debug('get proxy: %s', proxy);
  return proxyAgent;
}

module.exports = detectProxyAgent;
module.exports.proxyAgents = proxyAgents;
