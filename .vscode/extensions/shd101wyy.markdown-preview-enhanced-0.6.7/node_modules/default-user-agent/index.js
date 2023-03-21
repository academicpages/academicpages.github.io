/**!
 * default-user-agent - index.js
 *
 * Copyright(c) fengmk2 and other contributors.
 * MIT Licensed
 *
 * Authors:
 *   fengmk2 <fengmk2@gmail.com> (http://fengmk2.com)
 */

'use strict';

/**
 * Module dependencies.
 */

var osName = require('os-name');

var USER_AGENT = 'Node.js/' + process.version.slice(1)
  + ' (' + osName() + '; ' + process.arch + ')';

module.exports = function ua(name, version) {
  if (arguments.length !== 2) {
    return USER_AGENT;
  }
  return name + '/' + version + ' ' + USER_AGENT;
};
