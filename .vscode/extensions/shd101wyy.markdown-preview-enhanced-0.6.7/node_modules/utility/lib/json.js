'use strict';

var fs = require('mz/fs');
var path = require('path');
var mkdirp = require('mkdirp');

exports.strictJSONParse = function (str) {
  var obj = JSON.parse(str);
  if (!obj || typeof obj !== 'object') {
    throw new Error('JSON string is not object');
  }
  return obj;
};

exports.readJSONSync = function(filepath) {
  if (!fs.existsSync(filepath)) {
    throw new Error(filepath + ' is not found');
  }
  return JSON.parse(fs.readFileSync(filepath));
};

exports.writeJSONSync = function(filepath, str, options) {
  options = options || {};
  if (!('space' in options)) {
    options.space = 2;
  }

  mkdirp.sync(path.dirname(filepath));
  if (typeof str === 'object') {
    str = JSON.stringify(str, options.replacer, options.space) + '\n';
  }

  fs.writeFileSync(filepath, str);
};

exports.readJSON = function(filepath) {
  return fs.exists(filepath)
    .then(function(exists) {
      if (!exists) {
        throw new Error(filepath + ' is not found');
      }
      return fs.readFile(filepath);
    })
    .then(function(buf) {
      return JSON.parse(buf);
    });
};

exports.writeJSON = function(filepath, str, options) {
  options = options || {};
  if (!('space' in options)) {
    options.space = 2;
  }

  if (typeof str === 'object') {
    str = JSON.stringify(str, options.replacer, options.space) + '\n';
  }

  return mkdir(path.dirname(filepath))
    .then(function() {
      return fs.writeFile(filepath, str);
    });
};

function mkdir(dir) {
  return new Promise(function(resolve, reject) {
    mkdirp(dir, function(err) {
      if (err) {
        return reject(err);
      }
      resolve();
    });
  });
}
