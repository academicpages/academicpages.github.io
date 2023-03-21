'use strict';

/**
 * optimize try catch
 * @param {Function} fn
 * @return {Object}
 *   - {Error} error
 *   - {Mix} value
 */
exports.try = function (fn) {
  var res = {
    error: undefined,
    value: undefined
  };

  try {
    res.value = fn();
  } catch (err) {
    res.error = err instanceof Error
      ? err
      : new Error(err);
  }

  return res;
};


/**
 * @description Deal with typescript
 */
exports.UNSTABLE_METHOD = {
  try: exports.try,
};


/**
 * avoid if (a && a.b && a.b.c)
 * @param {Object} obj
 * @param {...String} keys
 * @return {Object}
 */
exports.dig = function (obj) {
  if (!obj) {
    return;
  }
  if (arguments.length <= 1) {
    return obj;
  }

  var value = obj[arguments[1]];
  for (var i = 2; i < arguments.length; i++) {
    if (!value) {
      break;
    }
    value = value[arguments[i]];
  }

  return value;
};

/**
 * optimize arguments to array
 * @param {Arguments} args
 * @return {Array}
 */
exports.argumentsToArray = function (args) {
  var res = new Array(args.length);
  for (var i = 0; i < args.length; i++) {
    res[i] = args[i];
  }
  return res;
};
