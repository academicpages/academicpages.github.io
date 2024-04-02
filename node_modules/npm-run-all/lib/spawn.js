"use strict";

Object.defineProperty(exports, "__esModule", {
  value: true
});
/**
 * @author Toru Nagashima
 * @copyright 2015 Toru Nagashima. All rights reserved.
 * See LICENSE file in root directory for full license.
 */

/**
 * Launches a new process with the given command.
 * This is {@link ./spawn-posix.js:spawn} or {@link ./spawn-win32.js:spawn}
 * @private
 */
exports.default = require(process.platform === "win32" ? "./spawn-win32" : "./spawn-posix").default;