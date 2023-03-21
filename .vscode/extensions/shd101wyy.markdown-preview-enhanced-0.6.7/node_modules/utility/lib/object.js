'use strict';

/**
 * High performance assign before node6
 * @param {Object} target - target object
 * @param {Object | Array} objects - object assign from
 * @return {Object} - return target object
 */
exports.assign = function(target, objects) {
  if (!Array.isArray(objects)) {
    objects = [ objects ];
  }

  for (var i = 0; i < objects.length; i++) {
    var obj = objects[i];
    if (obj) {
      var keys = Object.keys(obj);
      for (var j = 0; j < keys.length; j++) {
        var key = keys[j];
        target[key] = obj[key];
      }
    }
  }
  return target;
};

exports.has = function has(obj, prop) {
  return Object.prototype.hasOwnProperty.call(obj, prop);
};

/**
 * Get all enumerable and ownership of property names
 * @param {Object} obj - detect object
 * @param {Boolean} [ignoreNull] - ignore null, undefined or NaN property
 * @return {Array<String>} property names
 */
exports.getOwnEnumerables = function getOwnEnumerables(obj, ignoreNull) {
  if (!obj || typeof obj !== 'object' || Array.isArray(obj)) {
    return [];
  }
  return Object.keys(obj).filter(function(key) {
    if (ignoreNull) {
      var value = obj[key];
      if (value === null || value === undefined || Number.isNaN(value)) {
        return false;
      }
    }
    return exports.has(obj, key);
  });
};

/**
 * generate a real map object(clean object), no constructor, no __proto__
 * @param {Object} [obj] - init object, optional
 * @return {Object}
 */
exports.map = function map(obj) {
  var map = new EmptyObject();
  if (!obj) {
    return map;
  }

  for (var key in obj) {
    map[key] = obj[key];
  }
  return map;
};

// faster way like `Object.create(null)` to get a 'clean' empty object
// https://github.com/nodejs/node/blob/master/lib/events.js#L5
// https://cnodejs.org/topic/571e0c445a26c4a841ecbcf1
function EmptyObject() {}
EmptyObject.prototype = Object.create(null);
