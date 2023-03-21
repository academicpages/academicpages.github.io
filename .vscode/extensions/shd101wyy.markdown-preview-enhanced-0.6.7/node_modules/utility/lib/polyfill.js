'use strict';

exports.setImmediate = typeof setImmediate === 'function'
  ? setImmediate
  : function(fn){
    process.nextTick(fn.bind.apply(fn, arguments));
  };
