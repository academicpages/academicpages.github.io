define(() => { return /******/ (() => { // webpackBootstrap
/******/ 	var __webpack_modules__ = ({

/***/ 8299:
/***/ ((module, __unused_webpack_exports, __webpack_require__) => {

__webpack_require__(9122);
module.exports = __webpack_require__(8544).RegExp.escape;

/***/ }),

/***/ 6819:
/***/ ((module) => {

module.exports = function (it) {
  if (typeof it != 'function') throw TypeError(it + ' is not a function!');
  return it;
};

/***/ }),

/***/ 9855:
/***/ ((module, __unused_webpack_exports, __webpack_require__) => {

var cof = __webpack_require__(3679);
module.exports = function (it, msg) {
  if (typeof it != 'number' && cof(it) != 'Number') throw TypeError(msg);
  return +it;
};

/***/ }),

/***/ 4339:
/***/ ((module, __unused_webpack_exports, __webpack_require__) => {

// 22.1.3.31 Array.prototype[@@unscopables]
var UNSCOPABLES = __webpack_require__(3336)('unscopables');
var ArrayProto = Array.prototype;
if (ArrayProto[UNSCOPABLES] == undefined) __webpack_require__(8012)(ArrayProto, UNSCOPABLES, {});
module.exports = function (key) {
  ArrayProto[UNSCOPABLES][key] = true;
};

/***/ }),

/***/ 1330:
/***/ ((module, __unused_webpack_exports, __webpack_require__) => {

"use strict";


var at = __webpack_require__(3593)(true);

// `AdvanceStringIndex` abstract operation
// https://tc39.github.io/ecma262/#sec-advancestringindex
module.exports = function (S, index, unicode) {
  return index + (unicode ? at(S, index).length : 1);
};

/***/ }),

/***/ 2702:
/***/ ((module) => {

module.exports = function (it, Constructor, name, forbiddenField) {
  if (!(it instanceof Constructor) || forbiddenField !== undefined && forbiddenField in it) {
    throw TypeError(name + ': incorrect invocation!');
  }
  return it;
};

/***/ }),

/***/ 6154:
/***/ ((module, __unused_webpack_exports, __webpack_require__) => {

var isObject = __webpack_require__(7156);
module.exports = function (it) {
  if (!isObject(it)) throw TypeError(it + ' is not an object!');
  return it;
};

/***/ }),

/***/ 2147:
/***/ ((module, __unused_webpack_exports, __webpack_require__) => {

"use strict";
// 22.1.3.3 Array.prototype.copyWithin(target, start, end = this.length)


var toObject = __webpack_require__(2515);
var toAbsoluteIndex = __webpack_require__(6241);
var toLength = __webpack_require__(8315);
module.exports = [].copyWithin || function copyWithin(target /* = 0 */, start /* = 0, end = @length */) {
  var O = toObject(this);
  var len = toLength(O.length);
  var to = toAbsoluteIndex(target, len);
  var from = toAbsoluteIndex(start, len);
  var end = arguments.length > 2 ? arguments[2] : undefined;
  var count = Math.min((end === undefined ? len : toAbsoluteIndex(end, len)) - from, len - to);
  var inc = 1;
  if (from < to && to < from + count) {
    inc = -1;
    from += count - 1;
    to += count - 1;
  }
  while (count-- > 0) {
    if (from in O) O[to] = O[from];else delete O[to];
    to += inc;
    from += inc;
  }
  return O;
};

/***/ }),

/***/ 1132:
/***/ ((module, __unused_webpack_exports, __webpack_require__) => {

"use strict";
// 22.1.3.6 Array.prototype.fill(value, start = 0, end = this.length)


var toObject = __webpack_require__(2515);
var toAbsoluteIndex = __webpack_require__(6241);
var toLength = __webpack_require__(8315);
module.exports = function fill(value /* , start = 0, end = @length */) {
  var O = toObject(this);
  var length = toLength(O.length);
  var aLen = arguments.length;
  var index = toAbsoluteIndex(aLen > 1 ? arguments[1] : undefined, length);
  var end = aLen > 2 ? arguments[2] : undefined;
  var endPos = end === undefined ? length : toAbsoluteIndex(end, length);
  while (endPos > index) {
    O[index++] = value;
  }
  return O;
};

/***/ }),

/***/ 5273:
/***/ ((module, __unused_webpack_exports, __webpack_require__) => {

var forOf = __webpack_require__(2734);
module.exports = function (iter, ITERATOR) {
  var result = [];
  forOf(iter, false, result.push, result, ITERATOR);
  return result;
};

/***/ }),

/***/ 4687:
/***/ ((module, __unused_webpack_exports, __webpack_require__) => {

// false -> Array#indexOf
// true  -> Array#includes
var toIObject = __webpack_require__(8499);
var toLength = __webpack_require__(8315);
var toAbsoluteIndex = __webpack_require__(6241);
module.exports = function (IS_INCLUDES) {
  return function ($this, el, fromIndex) {
    var O = toIObject($this);
    var length = toLength(O.length);
    var index = toAbsoluteIndex(fromIndex, length);
    var value;
    // Array#includes uses SameValueZero equality algorithm
    // eslint-disable-next-line no-self-compare
    if (IS_INCLUDES && el != el) while (length > index) {
      value = O[index++];
      // eslint-disable-next-line no-self-compare
      if (value != value) return true;
      // Array#indexOf ignores holes, Array#includes - not
    } else for (; length > index; index++) {
      if (IS_INCLUDES || index in O) {
        if (O[index] === el) return IS_INCLUDES || index || 0;
      }
    }
    return !IS_INCLUDES && -1;
  };
};

/***/ }),

/***/ 3970:
/***/ ((module, __unused_webpack_exports, __webpack_require__) => {

// 0 -> Array#forEach
// 1 -> Array#map
// 2 -> Array#filter
// 3 -> Array#some
// 4 -> Array#every
// 5 -> Array#find
// 6 -> Array#findIndex
var ctx = __webpack_require__(566);
var IObject = __webpack_require__(331);
var toObject = __webpack_require__(2515);
var toLength = __webpack_require__(8315);
var asc = __webpack_require__(5486);
module.exports = function (TYPE, $create) {
  var IS_MAP = TYPE == 1;
  var IS_FILTER = TYPE == 2;
  var IS_SOME = TYPE == 3;
  var IS_EVERY = TYPE == 4;
  var IS_FIND_INDEX = TYPE == 6;
  var NO_HOLES = TYPE == 5 || IS_FIND_INDEX;
  var create = $create || asc;
  return function ($this, callbackfn, that) {
    var O = toObject($this);
    var self = IObject(O);
    var f = ctx(callbackfn, that, 3);
    var length = toLength(self.length);
    var index = 0;
    var result = IS_MAP ? create($this, length) : IS_FILTER ? create($this, 0) : undefined;
    var val, res;
    for (; length > index; index++) {
      if (NO_HOLES || index in self) {
        val = self[index];
        res = f(val, index, O);
        if (TYPE) {
          if (IS_MAP) result[index] = res; // map
          else if (res) switch (TYPE) {
            case 3:
              return true;
            // some
            case 5:
              return val;
            // find
            case 6:
              return index;
            // findIndex
            case 2:
              result.push(val);
            // filter
          } else if (IS_EVERY) return false; // every
        }
      }
    }

    return IS_FIND_INDEX ? -1 : IS_SOME || IS_EVERY ? IS_EVERY : result;
  };
};

/***/ }),

/***/ 6419:
/***/ ((module, __unused_webpack_exports, __webpack_require__) => {

var aFunction = __webpack_require__(6819);
var toObject = __webpack_require__(2515);
var IObject = __webpack_require__(331);
var toLength = __webpack_require__(8315);
module.exports = function (that, callbackfn, aLen, memo, isRight) {
  aFunction(callbackfn);
  var O = toObject(that);
  var self = IObject(O);
  var length = toLength(O.length);
  var index = isRight ? length - 1 : 0;
  var i = isRight ? -1 : 1;
  if (aLen < 2) for (;;) {
    if (index in self) {
      memo = self[index];
      index += i;
      break;
    }
    index += i;
    if (isRight ? index < 0 : length <= index) {
      throw TypeError('Reduce of empty array with no initial value');
    }
  }
  for (; isRight ? index >= 0 : length > index; index += i) {
    if (index in self) {
      memo = callbackfn(memo, self[index], index, O);
    }
  }
  return memo;
};

/***/ }),

/***/ 2642:
/***/ ((module, __unused_webpack_exports, __webpack_require__) => {

var isObject = __webpack_require__(7156);
var isArray = __webpack_require__(1320);
var SPECIES = __webpack_require__(3336)('species');
module.exports = function (original) {
  var C;
  if (isArray(original)) {
    C = original.constructor;
    // cross-realm fallback
    if (typeof C == 'function' && (C === Array || isArray(C.prototype))) C = undefined;
    if (isObject(C)) {
      C = C[SPECIES];
      if (C === null) C = undefined;
    }
  }
  return C === undefined ? Array : C;
};

/***/ }),

/***/ 5486:
/***/ ((module, __unused_webpack_exports, __webpack_require__) => {

// 9.4.2.3 ArraySpeciesCreate(originalArray, length)
var speciesConstructor = __webpack_require__(2642);
module.exports = function (original, length) {
  return new (speciesConstructor(original))(length);
};

/***/ }),

/***/ 8327:
/***/ ((module, __unused_webpack_exports, __webpack_require__) => {

"use strict";


var aFunction = __webpack_require__(6819);
var isObject = __webpack_require__(7156);
var invoke = __webpack_require__(2765);
var arraySlice = [].slice;
var factories = {};
var construct = function construct(F, len, args) {
  if (!(len in factories)) {
    for (var n = [], i = 0; i < len; i++) {
      n[i] = 'a[' + i + ']';
    }
    // eslint-disable-next-line no-new-func
    factories[len] = Function('F,a', 'return new F(' + n.join(',') + ')');
  }
  return factories[len](F, args);
};
module.exports = Function.bind || function bind(that /* , ...args */) {
  var fn = aFunction(this);
  var partArgs = arraySlice.call(arguments, 1);
  var bound = function bound( /* args... */
  ) {
    var args = partArgs.concat(arraySlice.call(arguments));
    return this instanceof bound ? construct(fn, args.length, args) : invoke(fn, args, that);
  };
  if (isObject(fn.prototype)) bound.prototype = fn.prototype;
  return bound;
};

/***/ }),

/***/ 2858:
/***/ ((module, __unused_webpack_exports, __webpack_require__) => {

// getting tag from 19.1.3.6 Object.prototype.toString()
var cof = __webpack_require__(3679);
var TAG = __webpack_require__(3336)('toStringTag');
// ES3 wrong here
var ARG = cof(function () {
  return arguments;
}()) == 'Arguments';

// fallback for IE11 Script Access Denied error
var tryGet = function tryGet(it, key) {
  try {
    return it[key];
  } catch (e) {/* empty */}
};
module.exports = function (it) {
  var O, T, B;
  return it === undefined ? 'Undefined' : it === null ? 'Null'
  // @@toStringTag case
  : typeof (T = tryGet(O = Object(it), TAG)) == 'string' ? T
  // builtinTag case
  : ARG ? cof(O)
  // ES3 arguments fallback
  : (B = cof(O)) == 'Object' && typeof O.callee == 'function' ? 'Arguments' : B;
};

/***/ }),

/***/ 3679:
/***/ ((module) => {

var toString = {}.toString;
module.exports = function (it) {
  return toString.call(it).slice(8, -1);
};

/***/ }),

/***/ 4396:
/***/ ((module, __unused_webpack_exports, __webpack_require__) => {

"use strict";


var dP = (__webpack_require__(4835).f);
var create = __webpack_require__(4275);
var redefineAll = __webpack_require__(7228);
var ctx = __webpack_require__(566);
var anInstance = __webpack_require__(2702);
var forOf = __webpack_require__(2734);
var $iterDefine = __webpack_require__(4873);
var step = __webpack_require__(7218);
var setSpecies = __webpack_require__(4798);
var DESCRIPTORS = __webpack_require__(4926);
var fastKey = (__webpack_require__(3763).fastKey);
var validate = __webpack_require__(8546);
var SIZE = DESCRIPTORS ? '_s' : 'size';
var getEntry = function getEntry(that, key) {
  // fast case
  var index = fastKey(key);
  var entry;
  if (index !== 'F') return that._i[index];
  // frozen object case
  for (entry = that._f; entry; entry = entry.n) {
    if (entry.k == key) return entry;
  }
};
module.exports = {
  getConstructor: function getConstructor(wrapper, NAME, IS_MAP, ADDER) {
    var C = wrapper(function (that, iterable) {
      anInstance(that, C, NAME, '_i');
      that._t = NAME; // collection type
      that._i = create(null); // index
      that._f = undefined; // first entry
      that._l = undefined; // last entry
      that[SIZE] = 0; // size
      if (iterable != undefined) forOf(iterable, IS_MAP, that[ADDER], that);
    });
    redefineAll(C.prototype, {
      // 23.1.3.1 Map.prototype.clear()
      // 23.2.3.2 Set.prototype.clear()
      clear: function clear() {
        for (var that = validate(this, NAME), data = that._i, entry = that._f; entry; entry = entry.n) {
          entry.r = true;
          if (entry.p) entry.p = entry.p.n = undefined;
          delete data[entry.i];
        }
        that._f = that._l = undefined;
        that[SIZE] = 0;
      },
      // 23.1.3.3 Map.prototype.delete(key)
      // 23.2.3.4 Set.prototype.delete(value)
      'delete': function _delete(key) {
        var that = validate(this, NAME);
        var entry = getEntry(that, key);
        if (entry) {
          var next = entry.n;
          var prev = entry.p;
          delete that._i[entry.i];
          entry.r = true;
          if (prev) prev.n = next;
          if (next) next.p = prev;
          if (that._f == entry) that._f = next;
          if (that._l == entry) that._l = prev;
          that[SIZE]--;
        }
        return !!entry;
      },
      // 23.2.3.6 Set.prototype.forEach(callbackfn, thisArg = undefined)
      // 23.1.3.5 Map.prototype.forEach(callbackfn, thisArg = undefined)
      forEach: function forEach(callbackfn /* , that = undefined */) {
        validate(this, NAME);
        var f = ctx(callbackfn, arguments.length > 1 ? arguments[1] : undefined, 3);
        var entry;
        while (entry = entry ? entry.n : this._f) {
          f(entry.v, entry.k, this);
          // revert to the last existing entry
          while (entry && entry.r) {
            entry = entry.p;
          }
        }
      },
      // 23.1.3.7 Map.prototype.has(key)
      // 23.2.3.7 Set.prototype.has(value)
      has: function has(key) {
        return !!getEntry(validate(this, NAME), key);
      }
    });
    if (DESCRIPTORS) dP(C.prototype, 'size', {
      get: function get() {
        return validate(this, NAME)[SIZE];
      }
    });
    return C;
  },
  def: function def(that, key, value) {
    var entry = getEntry(that, key);
    var prev, index;
    // change existing entry
    if (entry) {
      entry.v = value;
      // create new entry
    } else {
      that._l = entry = {
        i: index = fastKey(key, true),
        // <- index
        k: key,
        // <- key
        v: value,
        // <- value
        p: prev = that._l,
        // <- previous entry
        n: undefined,
        // <- next entry
        r: false // <- removed
      };

      if (!that._f) that._f = entry;
      if (prev) prev.n = entry;
      that[SIZE]++;
      // add to index
      if (index !== 'F') that._i[index] = entry;
    }
    return that;
  },
  getEntry: getEntry,
  setStrong: function setStrong(C, NAME, IS_MAP) {
    // add .keys, .values, .entries, [@@iterator]
    // 23.1.3.4, 23.1.3.8, 23.1.3.11, 23.1.3.12, 23.2.3.5, 23.2.3.8, 23.2.3.10, 23.2.3.11
    $iterDefine(C, NAME, function (iterated, kind) {
      this._t = validate(iterated, NAME); // target
      this._k = kind; // kind
      this._l = undefined; // previous
    }, function () {
      var that = this;
      var kind = that._k;
      var entry = that._l;
      // revert to the last existing entry
      while (entry && entry.r) {
        entry = entry.p;
      }
      // get next entry
      if (!that._t || !(that._l = entry = entry ? entry.n : that._t._f)) {
        // or finish the iteration
        that._t = undefined;
        return step(1);
      }
      // return step by kind
      if (kind == 'keys') return step(0, entry.k);
      if (kind == 'values') return step(0, entry.v);
      return step(0, [entry.k, entry.v]);
    }, IS_MAP ? 'entries' : 'values', !IS_MAP, true);

    // add [@@species], 23.1.2.2, 23.2.2.2
    setSpecies(NAME);
  }
};

/***/ }),

/***/ 1872:
/***/ ((module, __unused_webpack_exports, __webpack_require__) => {

// https://github.com/DavidBruant/Map-Set.prototype.toJSON
var classof = __webpack_require__(2858);
var from = __webpack_require__(5273);
module.exports = function (NAME) {
  return function toJSON() {
    if (classof(this) != NAME) throw TypeError(NAME + "#toJSON isn't generic");
    return from(this);
  };
};

/***/ }),

/***/ 4495:
/***/ ((module, __unused_webpack_exports, __webpack_require__) => {

"use strict";


var redefineAll = __webpack_require__(7228);
var getWeak = (__webpack_require__(3763).getWeak);
var anObject = __webpack_require__(6154);
var isObject = __webpack_require__(7156);
var anInstance = __webpack_require__(2702);
var forOf = __webpack_require__(2734);
var createArrayMethod = __webpack_require__(3970);
var $has = __webpack_require__(5389);
var validate = __webpack_require__(8546);
var arrayFind = createArrayMethod(5);
var arrayFindIndex = createArrayMethod(6);
var id = 0;

// fallback for uncaught frozen keys
var uncaughtFrozenStore = function uncaughtFrozenStore(that) {
  return that._l || (that._l = new UncaughtFrozenStore());
};
var UncaughtFrozenStore = function UncaughtFrozenStore() {
  this.a = [];
};
var findUncaughtFrozen = function findUncaughtFrozen(store, key) {
  return arrayFind(store.a, function (it) {
    return it[0] === key;
  });
};
UncaughtFrozenStore.prototype = {
  get: function get(key) {
    var entry = findUncaughtFrozen(this, key);
    if (entry) return entry[1];
  },
  has: function has(key) {
    return !!findUncaughtFrozen(this, key);
  },
  set: function set(key, value) {
    var entry = findUncaughtFrozen(this, key);
    if (entry) entry[1] = value;else this.a.push([key, value]);
  },
  'delete': function _delete(key) {
    var index = arrayFindIndex(this.a, function (it) {
      return it[0] === key;
    });
    if (~index) this.a.splice(index, 1);
    return !!~index;
  }
};
module.exports = {
  getConstructor: function getConstructor(wrapper, NAME, IS_MAP, ADDER) {
    var C = wrapper(function (that, iterable) {
      anInstance(that, C, NAME, '_i');
      that._t = NAME; // collection type
      that._i = id++; // collection id
      that._l = undefined; // leak store for uncaught frozen objects
      if (iterable != undefined) forOf(iterable, IS_MAP, that[ADDER], that);
    });
    redefineAll(C.prototype, {
      // 23.3.3.2 WeakMap.prototype.delete(key)
      // 23.4.3.3 WeakSet.prototype.delete(value)
      'delete': function _delete(key) {
        if (!isObject(key)) return false;
        var data = getWeak(key);
        if (data === true) return uncaughtFrozenStore(validate(this, NAME))['delete'](key);
        return data && $has(data, this._i) && delete data[this._i];
      },
      // 23.3.3.4 WeakMap.prototype.has(key)
      // 23.4.3.4 WeakSet.prototype.has(value)
      has: function has(key) {
        if (!isObject(key)) return false;
        var data = getWeak(key);
        if (data === true) return uncaughtFrozenStore(validate(this, NAME)).has(key);
        return data && $has(data, this._i);
      }
    });
    return C;
  },
  def: function def(that, key, value) {
    var data = getWeak(anObject(key), true);
    if (data === true) uncaughtFrozenStore(that).set(key, value);else data[that._i] = value;
    return that;
  },
  ufstore: uncaughtFrozenStore
};

/***/ }),

/***/ 1966:
/***/ ((module, __unused_webpack_exports, __webpack_require__) => {

"use strict";


var global = __webpack_require__(7381);
var $export = __webpack_require__(5913);
var redefine = __webpack_require__(7278);
var redefineAll = __webpack_require__(7228);
var meta = __webpack_require__(3763);
var forOf = __webpack_require__(2734);
var anInstance = __webpack_require__(2702);
var isObject = __webpack_require__(7156);
var fails = __webpack_require__(5810);
var $iterDetect = __webpack_require__(5508);
var setToStringTag = __webpack_require__(8094);
var inheritIfRequired = __webpack_require__(3654);
module.exports = function (NAME, wrapper, methods, common, IS_MAP, IS_WEAK) {
  var Base = global[NAME];
  var C = Base;
  var ADDER = IS_MAP ? 'set' : 'add';
  var proto = C && C.prototype;
  var O = {};
  var fixMethod = function fixMethod(KEY) {
    var fn = proto[KEY];
    redefine(proto, KEY, KEY == 'delete' ? function (a) {
      return IS_WEAK && !isObject(a) ? false : fn.call(this, a === 0 ? 0 : a);
    } : KEY == 'has' ? function has(a) {
      return IS_WEAK && !isObject(a) ? false : fn.call(this, a === 0 ? 0 : a);
    } : KEY == 'get' ? function get(a) {
      return IS_WEAK && !isObject(a) ? undefined : fn.call(this, a === 0 ? 0 : a);
    } : KEY == 'add' ? function add(a) {
      fn.call(this, a === 0 ? 0 : a);
      return this;
    } : function set(a, b) {
      fn.call(this, a === 0 ? 0 : a, b);
      return this;
    });
  };
  if (typeof C != 'function' || !(IS_WEAK || proto.forEach && !fails(function () {
    new C().entries().next();
  }))) {
    // create collection constructor
    C = common.getConstructor(wrapper, NAME, IS_MAP, ADDER);
    redefineAll(C.prototype, methods);
    meta.NEED = true;
  } else {
    var instance = new C();
    // early implementations not supports chaining
    var HASNT_CHAINING = instance[ADDER](IS_WEAK ? {} : -0, 1) != instance;
    // V8 ~  Chromium 40- weak-collections throws on primitives, but should return false
    var THROWS_ON_PRIMITIVES = fails(function () {
      instance.has(1);
    });
    // most early implementations doesn't supports iterables, most modern - not close it correctly
    var ACCEPT_ITERABLES = $iterDetect(function (iter) {
      new C(iter);
    }); // eslint-disable-line no-new
    // for early implementations -0 and +0 not the same
    var BUGGY_ZERO = !IS_WEAK && fails(function () {
      // V8 ~ Chromium 42- fails only with 5+ elements
      var $instance = new C();
      var index = 5;
      while (index--) {
        $instance[ADDER](index, index);
      }
      return !$instance.has(-0);
    });
    if (!ACCEPT_ITERABLES) {
      C = wrapper(function (target, iterable) {
        anInstance(target, C, NAME);
        var that = inheritIfRequired(new Base(), target, C);
        if (iterable != undefined) forOf(iterable, IS_MAP, that[ADDER], that);
        return that;
      });
      C.prototype = proto;
      proto.constructor = C;
    }
    if (THROWS_ON_PRIMITIVES || BUGGY_ZERO) {
      fixMethod('delete');
      fixMethod('has');
      IS_MAP && fixMethod('get');
    }
    if (BUGGY_ZERO || HASNT_CHAINING) fixMethod(ADDER);
    // weak collections should not contains .clear method
    if (IS_WEAK && proto.clear) delete proto.clear;
  }
  setToStringTag(C, NAME);
  O[NAME] = C;
  $export($export.G + $export.W + $export.F * (C != Base), O);
  if (!IS_WEAK) common.setStrong(C, NAME, IS_MAP);
  return C;
};

/***/ }),

/***/ 8544:
/***/ ((module) => {

var core = module.exports = {
  version: '2.6.12'
};
if (typeof __e == 'number') __e = core; // eslint-disable-line no-undef

/***/ }),

/***/ 1348:
/***/ ((module, __unused_webpack_exports, __webpack_require__) => {

"use strict";


var $defineProperty = __webpack_require__(4835);
var createDesc = __webpack_require__(6256);
module.exports = function (object, index, value) {
  if (index in object) $defineProperty.f(object, index, createDesc(0, value));else object[index] = value;
};

/***/ }),

/***/ 566:
/***/ ((module, __unused_webpack_exports, __webpack_require__) => {

// optional / simple context binding
var aFunction = __webpack_require__(6819);
module.exports = function (fn, that, length) {
  aFunction(fn);
  if (that === undefined) return fn;
  switch (length) {
    case 1:
      return function (a) {
        return fn.call(that, a);
      };
    case 2:
      return function (a, b) {
        return fn.call(that, a, b);
      };
    case 3:
      return function (a, b, c) {
        return fn.call(that, a, b, c);
      };
  }
  return function /* ...args */
  () {
    return fn.apply(that, arguments);
  };
};

/***/ }),

/***/ 2115:
/***/ ((module, __unused_webpack_exports, __webpack_require__) => {

"use strict";


// 20.3.4.36 / 15.9.5.43 Date.prototype.toISOString()
var fails = __webpack_require__(5810);
var getTime = Date.prototype.getTime;
var $toISOString = Date.prototype.toISOString;
var lz = function lz(num) {
  return num > 9 ? num : '0' + num;
};

// PhantomJS / old WebKit has a broken implementations
module.exports = fails(function () {
  return $toISOString.call(new Date(-5e13 - 1)) != '0385-07-25T07:06:39.999Z';
}) || !fails(function () {
  $toISOString.call(new Date(NaN));
}) ? function toISOString() {
  if (!isFinite(getTime.call(this))) throw RangeError('Invalid time value');
  var d = this;
  var y = d.getUTCFullYear();
  var m = d.getUTCMilliseconds();
  var s = y < 0 ? '-' : y > 9999 ? '+' : '';
  return s + ('00000' + Math.abs(y)).slice(s ? -6 : -4) + '-' + lz(d.getUTCMonth() + 1) + '-' + lz(d.getUTCDate()) + 'T' + lz(d.getUTCHours()) + ':' + lz(d.getUTCMinutes()) + ':' + lz(d.getUTCSeconds()) + '.' + (m > 99 ? m : '0' + lz(m)) + 'Z';
} : $toISOString;

/***/ }),

/***/ 296:
/***/ ((module, __unused_webpack_exports, __webpack_require__) => {

"use strict";


var anObject = __webpack_require__(6154);
var toPrimitive = __webpack_require__(8537);
var NUMBER = 'number';
module.exports = function (hint) {
  if (hint !== 'string' && hint !== NUMBER && hint !== 'default') throw TypeError('Incorrect hint');
  return toPrimitive(anObject(this), hint != NUMBER);
};

/***/ }),

/***/ 408:
/***/ ((module) => {

// 7.2.1 RequireObjectCoercible(argument)
module.exports = function (it) {
  if (it == undefined) throw TypeError("Can't call method on  " + it);
  return it;
};

/***/ }),

/***/ 4926:
/***/ ((module, __unused_webpack_exports, __webpack_require__) => {

// Thank's IE8 for his funny defineProperty
module.exports = !__webpack_require__(5810)(function () {
  return Object.defineProperty({}, 'a', {
    get: function get() {
      return 7;
    }
  }).a != 7;
});

/***/ }),

/***/ 2241:
/***/ ((module, __unused_webpack_exports, __webpack_require__) => {

var isObject = __webpack_require__(7156);
var document = (__webpack_require__(7381).document);
// typeof document.createElement is 'object' in old IE
var is = isObject(document) && isObject(document.createElement);
module.exports = function (it) {
  return is ? document.createElement(it) : {};
};

/***/ }),

/***/ 6921:
/***/ ((module) => {

// IE 8- don't enum bug keys
module.exports = 'constructor,hasOwnProperty,isPrototypeOf,propertyIsEnumerable,toLocaleString,toString,valueOf'.split(',');

/***/ }),

/***/ 8727:
/***/ ((module, __unused_webpack_exports, __webpack_require__) => {

// all enumerable object keys, includes symbols
var getKeys = __webpack_require__(9924);
var gOPS = __webpack_require__(5421);
var pIE = __webpack_require__(4616);
module.exports = function (it) {
  var result = getKeys(it);
  var getSymbols = gOPS.f;
  if (getSymbols) {
    var symbols = getSymbols(it);
    var isEnum = pIE.f;
    var i = 0;
    var key;
    while (symbols.length > i) {
      if (isEnum.call(it, key = symbols[i++])) result.push(key);
    }
  }
  return result;
};

/***/ }),

/***/ 5913:
/***/ ((module, __unused_webpack_exports, __webpack_require__) => {

var global = __webpack_require__(7381);
var core = __webpack_require__(8544);
var hide = __webpack_require__(8012);
var redefine = __webpack_require__(7278);
var ctx = __webpack_require__(566);
var PROTOTYPE = 'prototype';
var $export = function $export(type, name, source) {
  var IS_FORCED = type & $export.F;
  var IS_GLOBAL = type & $export.G;
  var IS_STATIC = type & $export.S;
  var IS_PROTO = type & $export.P;
  var IS_BIND = type & $export.B;
  var target = IS_GLOBAL ? global : IS_STATIC ? global[name] || (global[name] = {}) : (global[name] || {})[PROTOTYPE];
  var exports = IS_GLOBAL ? core : core[name] || (core[name] = {});
  var expProto = exports[PROTOTYPE] || (exports[PROTOTYPE] = {});
  var key, own, out, exp;
  if (IS_GLOBAL) source = name;
  for (key in source) {
    // contains in native
    own = !IS_FORCED && target && target[key] !== undefined;
    // export native or passed
    out = (own ? target : source)[key];
    // bind timers to global for call from export context
    exp = IS_BIND && own ? ctx(out, global) : IS_PROTO && typeof out == 'function' ? ctx(Function.call, out) : out;
    // extend global
    if (target) redefine(target, key, out, type & $export.U);
    // export
    if (exports[key] != out) hide(exports, key, exp);
    if (IS_PROTO && expProto[key] != out) expProto[key] = out;
  }
};
global.core = core;
// type bitmap
$export.F = 1; // forced
$export.G = 2; // global
$export.S = 4; // static
$export.P = 8; // proto
$export.B = 16; // bind
$export.W = 32; // wrap
$export.U = 64; // safe
$export.R = 128; // real proto method for `library`
module.exports = $export;

/***/ }),

/***/ 3483:
/***/ ((module, __unused_webpack_exports, __webpack_require__) => {

var MATCH = __webpack_require__(3336)('match');
module.exports = function (KEY) {
  var re = /./;
  try {
    '/./'[KEY](re);
  } catch (e) {
    try {
      re[MATCH] = false;
      return !'/./'[KEY](re);
    } catch (f) {/* empty */}
  }
  return true;
};

/***/ }),

/***/ 5810:
/***/ ((module) => {

module.exports = function (exec) {
  try {
    return !!exec();
  } catch (e) {
    return true;
  }
};

/***/ }),

/***/ 8644:
/***/ ((module, __unused_webpack_exports, __webpack_require__) => {

"use strict";


__webpack_require__(5997);
var redefine = __webpack_require__(7278);
var hide = __webpack_require__(8012);
var fails = __webpack_require__(5810);
var defined = __webpack_require__(408);
var wks = __webpack_require__(3336);
var regexpExec = __webpack_require__(6997);
var SPECIES = wks('species');
var REPLACE_SUPPORTS_NAMED_GROUPS = !fails(function () {
  // #replace needs built-in support for named groups.
  // #match works fine because it just return the exec results, even if it has
  // a "grops" property.
  var re = /./;
  re.exec = function () {
    var result = [];
    result.groups = {
      a: '7'
    };
    return result;
  };
  return ''.replace(re, '$<a>') !== '7';
});
var SPLIT_WORKS_WITH_OVERWRITTEN_EXEC = function () {
  // Chrome 51 has a buggy "split" implementation when RegExp#exec !== nativeExec
  var re = /(?:)/;
  var originalExec = re.exec;
  re.exec = function () {
    return originalExec.apply(this, arguments);
  };
  var result = 'ab'.split(re);
  return result.length === 2 && result[0] === 'a' && result[1] === 'b';
}();
module.exports = function (KEY, length, exec) {
  var SYMBOL = wks(KEY);
  var DELEGATES_TO_SYMBOL = !fails(function () {
    // String methods call symbol-named RegEp methods
    var O = {};
    O[SYMBOL] = function () {
      return 7;
    };
    return ''[KEY](O) != 7;
  });
  var DELEGATES_TO_EXEC = DELEGATES_TO_SYMBOL ? !fails(function () {
    // Symbol-named RegExp methods call .exec
    var execCalled = false;
    var re = /a/;
    re.exec = function () {
      execCalled = true;
      return null;
    };
    if (KEY === 'split') {
      // RegExp[@@split] doesn't call the regex's exec method, but first creates
      // a new one. We need to return the patched regex when creating the new one.
      re.constructor = {};
      re.constructor[SPECIES] = function () {
        return re;
      };
    }
    re[SYMBOL]('');
    return !execCalled;
  }) : undefined;
  if (!DELEGATES_TO_SYMBOL || !DELEGATES_TO_EXEC || KEY === 'replace' && !REPLACE_SUPPORTS_NAMED_GROUPS || KEY === 'split' && !SPLIT_WORKS_WITH_OVERWRITTEN_EXEC) {
    var nativeRegExpMethod = /./[SYMBOL];
    var fns = exec(defined, SYMBOL, ''[KEY], function maybeCallNative(nativeMethod, regexp, str, arg2, forceStringMethod) {
      if (regexp.exec === regexpExec) {
        if (DELEGATES_TO_SYMBOL && !forceStringMethod) {
          // The native String method already delegates to @@method (this
          // polyfilled function), leasing to infinite recursion.
          // We avoid it by directly calling the native @@method method.
          return {
            done: true,
            value: nativeRegExpMethod.call(regexp, str, arg2)
          };
        }
        return {
          done: true,
          value: nativeMethod.call(str, regexp, arg2)
        };
      }
      return {
        done: false
      };
    });
    var strfn = fns[0];
    var rxfn = fns[1];
    redefine(String.prototype, KEY, strfn);
    hide(RegExp.prototype, SYMBOL, length == 2
    // 21.2.5.8 RegExp.prototype[@@replace](string, replaceValue)
    // 21.2.5.11 RegExp.prototype[@@split](string, limit)
    ? function (string, arg) {
      return rxfn.call(string, this, arg);
    }
    // 21.2.5.6 RegExp.prototype[@@match](string)
    // 21.2.5.9 RegExp.prototype[@@search](string)
    : function (string) {
      return rxfn.call(string, this);
    });
  }
};

/***/ }),

/***/ 2188:
/***/ ((module, __unused_webpack_exports, __webpack_require__) => {

"use strict";


// 21.2.5.3 get RegExp.prototype.flags
var anObject = __webpack_require__(6154);
module.exports = function () {
  var that = anObject(this);
  var result = '';
  if (that.global) result += 'g';
  if (that.ignoreCase) result += 'i';
  if (that.multiline) result += 'm';
  if (that.unicode) result += 'u';
  if (that.sticky) result += 'y';
  return result;
};

/***/ }),

/***/ 3120:
/***/ ((module, __unused_webpack_exports, __webpack_require__) => {

"use strict";


// https://tc39.github.io/proposal-flatMap/#sec-FlattenIntoArray
var isArray = __webpack_require__(1320);
var isObject = __webpack_require__(7156);
var toLength = __webpack_require__(8315);
var ctx = __webpack_require__(566);
var IS_CONCAT_SPREADABLE = __webpack_require__(3336)('isConcatSpreadable');
function flattenIntoArray(target, original, source, sourceLen, start, depth, mapper, thisArg) {
  var targetIndex = start;
  var sourceIndex = 0;
  var mapFn = mapper ? ctx(mapper, thisArg, 3) : false;
  var element, spreadable;
  while (sourceIndex < sourceLen) {
    if (sourceIndex in source) {
      element = mapFn ? mapFn(source[sourceIndex], sourceIndex, original) : source[sourceIndex];
      spreadable = false;
      if (isObject(element)) {
        spreadable = element[IS_CONCAT_SPREADABLE];
        spreadable = spreadable !== undefined ? !!spreadable : isArray(element);
      }
      if (spreadable && depth > 0) {
        targetIndex = flattenIntoArray(target, original, element, toLength(element.length), targetIndex, depth - 1) - 1;
      } else {
        if (targetIndex >= 0x1fffffffffffff) throw TypeError();
        target[targetIndex] = element;
      }
      targetIndex++;
    }
    sourceIndex++;
  }
  return targetIndex;
}
module.exports = flattenIntoArray;

/***/ }),

/***/ 2734:
/***/ ((module, __unused_webpack_exports, __webpack_require__) => {

var ctx = __webpack_require__(566);
var call = __webpack_require__(2471);
var isArrayIter = __webpack_require__(7063);
var anObject = __webpack_require__(6154);
var toLength = __webpack_require__(8315);
var getIterFn = __webpack_require__(7637);
var BREAK = {};
var RETURN = {};
var exports = module.exports = function (iterable, entries, fn, that, ITERATOR) {
  var iterFn = ITERATOR ? function () {
    return iterable;
  } : getIterFn(iterable);
  var f = ctx(fn, that, entries ? 2 : 1);
  var index = 0;
  var length, step, iterator, result;
  if (typeof iterFn != 'function') throw TypeError(iterable + ' is not iterable!');
  // fast case for arrays with default iterator
  if (isArrayIter(iterFn)) for (length = toLength(iterable.length); length > index; index++) {
    result = entries ? f(anObject(step = iterable[index])[0], step[1]) : f(iterable[index]);
    if (result === BREAK || result === RETURN) return result;
  } else for (iterator = iterFn.call(iterable); !(step = iterator.next()).done;) {
    result = call(iterator, f, step.value, entries);
    if (result === BREAK || result === RETURN) return result;
  }
};
exports.BREAK = BREAK;
exports.RETURN = RETURN;

/***/ }),

/***/ 1174:
/***/ ((module, __unused_webpack_exports, __webpack_require__) => {

module.exports = __webpack_require__(3192)('native-function-to-string', Function.toString);

/***/ }),

/***/ 7381:
/***/ ((module) => {

// https://github.com/zloirock/core-js/issues/86#issuecomment-115759028
var global = module.exports = typeof window != 'undefined' && window.Math == Math ? window : typeof self != 'undefined' && self.Math == Math ? self
// eslint-disable-next-line no-new-func
: Function('return this')();
if (typeof __g == 'number') __g = global; // eslint-disable-line no-undef

/***/ }),

/***/ 5389:
/***/ ((module) => {

var hasOwnProperty = {}.hasOwnProperty;
module.exports = function (it, key) {
  return hasOwnProperty.call(it, key);
};

/***/ }),

/***/ 8012:
/***/ ((module, __unused_webpack_exports, __webpack_require__) => {

var dP = __webpack_require__(4835);
var createDesc = __webpack_require__(6256);
module.exports = __webpack_require__(4926) ? function (object, key, value) {
  return dP.f(object, key, createDesc(1, value));
} : function (object, key, value) {
  object[key] = value;
  return object;
};

/***/ }),

/***/ 1225:
/***/ ((module, __unused_webpack_exports, __webpack_require__) => {

var document = (__webpack_require__(7381).document);
module.exports = document && document.documentElement;

/***/ }),

/***/ 5142:
/***/ ((module, __unused_webpack_exports, __webpack_require__) => {

module.exports = !__webpack_require__(4926) && !__webpack_require__(5810)(function () {
  return Object.defineProperty(__webpack_require__(2241)('div'), 'a', {
    get: function get() {
      return 7;
    }
  }).a != 7;
});

/***/ }),

/***/ 3654:
/***/ ((module, __unused_webpack_exports, __webpack_require__) => {

var isObject = __webpack_require__(7156);
var setPrototypeOf = (__webpack_require__(6931).set);
module.exports = function (that, target, C) {
  var S = target.constructor;
  var P;
  if (S !== C && typeof S == 'function' && (P = S.prototype) !== C.prototype && isObject(P) && setPrototypeOf) {
    setPrototypeOf(that, P);
  }
  return that;
};

/***/ }),

/***/ 2765:
/***/ ((module) => {

// fast apply, http://jsperf.lnkit.com/fast-apply/5
module.exports = function (fn, args, that) {
  var un = that === undefined;
  switch (args.length) {
    case 0:
      return un ? fn() : fn.call(that);
    case 1:
      return un ? fn(args[0]) : fn.call(that, args[0]);
    case 2:
      return un ? fn(args[0], args[1]) : fn.call(that, args[0], args[1]);
    case 3:
      return un ? fn(args[0], args[1], args[2]) : fn.call(that, args[0], args[1], args[2]);
    case 4:
      return un ? fn(args[0], args[1], args[2], args[3]) : fn.call(that, args[0], args[1], args[2], args[3]);
  }
  return fn.apply(that, args);
};

/***/ }),

/***/ 331:
/***/ ((module, __unused_webpack_exports, __webpack_require__) => {

// fallback for non-array-like ES3 and non-enumerable old V8 strings
var cof = __webpack_require__(3679);
// eslint-disable-next-line no-prototype-builtins
module.exports = Object('z').propertyIsEnumerable(0) ? Object : function (it) {
  return cof(it) == 'String' ? it.split('') : Object(it);
};

/***/ }),

/***/ 7063:
/***/ ((module, __unused_webpack_exports, __webpack_require__) => {

// check on default Array iterator
var Iterators = __webpack_require__(5301);
var ITERATOR = __webpack_require__(3336)('iterator');
var ArrayProto = Array.prototype;
module.exports = function (it) {
  return it !== undefined && (Iterators.Array === it || ArrayProto[ITERATOR] === it);
};

/***/ }),

/***/ 1320:
/***/ ((module, __unused_webpack_exports, __webpack_require__) => {

// 7.2.2 IsArray(argument)
var cof = __webpack_require__(3679);
module.exports = Array.isArray || function isArray(arg) {
  return cof(arg) == 'Array';
};

/***/ }),

/***/ 5127:
/***/ ((module, __unused_webpack_exports, __webpack_require__) => {

// 20.1.2.3 Number.isInteger(number)
var isObject = __webpack_require__(7156);
var floor = Math.floor;
module.exports = function isInteger(it) {
  return !isObject(it) && isFinite(it) && floor(it) === it;
};

/***/ }),

/***/ 7156:
/***/ ((module) => {

function _typeof(obj) { "@babel/helpers - typeof"; return _typeof = "function" == typeof Symbol && "symbol" == typeof Symbol.iterator ? function (obj) { return typeof obj; } : function (obj) { return obj && "function" == typeof Symbol && obj.constructor === Symbol && obj !== Symbol.prototype ? "symbol" : typeof obj; }, _typeof(obj); }
module.exports = function (it) {
  return _typeof(it) === 'object' ? it !== null : typeof it === 'function';
};

/***/ }),

/***/ 1993:
/***/ ((module, __unused_webpack_exports, __webpack_require__) => {

// 7.2.8 IsRegExp(argument)
var isObject = __webpack_require__(7156);
var cof = __webpack_require__(3679);
var MATCH = __webpack_require__(3336)('match');
module.exports = function (it) {
  var isRegExp;
  return isObject(it) && ((isRegExp = it[MATCH]) !== undefined ? !!isRegExp : cof(it) == 'RegExp');
};

/***/ }),

/***/ 2471:
/***/ ((module, __unused_webpack_exports, __webpack_require__) => {

// call something on iterator step with safe closing on error
var anObject = __webpack_require__(6154);
module.exports = function (iterator, fn, value, entries) {
  try {
    return entries ? fn(anObject(value)[0], value[1]) : fn(value);
    // 7.4.6 IteratorClose(iterator, completion)
  } catch (e) {
    var ret = iterator['return'];
    if (ret !== undefined) anObject(ret.call(iterator));
    throw e;
  }
};

/***/ }),

/***/ 8258:
/***/ ((module, __unused_webpack_exports, __webpack_require__) => {

"use strict";


var create = __webpack_require__(4275);
var descriptor = __webpack_require__(6256);
var setToStringTag = __webpack_require__(8094);
var IteratorPrototype = {};

// 25.1.2.1.1 %IteratorPrototype%[@@iterator]()
__webpack_require__(8012)(IteratorPrototype, __webpack_require__(3336)('iterator'), function () {
  return this;
});
module.exports = function (Constructor, NAME, next) {
  Constructor.prototype = create(IteratorPrototype, {
    next: descriptor(1, next)
  });
  setToStringTag(Constructor, NAME + ' Iterator');
};

/***/ }),

/***/ 4873:
/***/ ((module, __unused_webpack_exports, __webpack_require__) => {

"use strict";


var LIBRARY = __webpack_require__(4219);
var $export = __webpack_require__(5913);
var redefine = __webpack_require__(7278);
var hide = __webpack_require__(8012);
var Iterators = __webpack_require__(5301);
var $iterCreate = __webpack_require__(8258);
var setToStringTag = __webpack_require__(8094);
var getPrototypeOf = __webpack_require__(4153);
var ITERATOR = __webpack_require__(3336)('iterator');
var BUGGY = !([].keys && 'next' in [].keys()); // Safari has buggy iterators w/o `next`
var FF_ITERATOR = '@@iterator';
var KEYS = 'keys';
var VALUES = 'values';
var returnThis = function returnThis() {
  return this;
};
module.exports = function (Base, NAME, Constructor, next, DEFAULT, IS_SET, FORCED) {
  $iterCreate(Constructor, NAME, next);
  var getMethod = function getMethod(kind) {
    if (!BUGGY && kind in proto) return proto[kind];
    switch (kind) {
      case KEYS:
        return function keys() {
          return new Constructor(this, kind);
        };
      case VALUES:
        return function values() {
          return new Constructor(this, kind);
        };
    }
    return function entries() {
      return new Constructor(this, kind);
    };
  };
  var TAG = NAME + ' Iterator';
  var DEF_VALUES = DEFAULT == VALUES;
  var VALUES_BUG = false;
  var proto = Base.prototype;
  var $native = proto[ITERATOR] || proto[FF_ITERATOR] || DEFAULT && proto[DEFAULT];
  var $default = $native || getMethod(DEFAULT);
  var $entries = DEFAULT ? !DEF_VALUES ? $default : getMethod('entries') : undefined;
  var $anyNative = NAME == 'Array' ? proto.entries || $native : $native;
  var methods, key, IteratorPrototype;
  // Fix native
  if ($anyNative) {
    IteratorPrototype = getPrototypeOf($anyNative.call(new Base()));
    if (IteratorPrototype !== Object.prototype && IteratorPrototype.next) {
      // Set @@toStringTag to native iterators
      setToStringTag(IteratorPrototype, TAG, true);
      // fix for some old engines
      if (!LIBRARY && typeof IteratorPrototype[ITERATOR] != 'function') hide(IteratorPrototype, ITERATOR, returnThis);
    }
  }
  // fix Array#{values, @@iterator}.name in V8 / FF
  if (DEF_VALUES && $native && $native.name !== VALUES) {
    VALUES_BUG = true;
    $default = function values() {
      return $native.call(this);
    };
  }
  // Define iterator
  if ((!LIBRARY || FORCED) && (BUGGY || VALUES_BUG || !proto[ITERATOR])) {
    hide(proto, ITERATOR, $default);
  }
  // Plug for library
  Iterators[NAME] = $default;
  Iterators[TAG] = returnThis;
  if (DEFAULT) {
    methods = {
      values: DEF_VALUES ? $default : getMethod(VALUES),
      keys: IS_SET ? $default : getMethod(KEYS),
      entries: $entries
    };
    if (FORCED) for (key in methods) {
      if (!(key in proto)) redefine(proto, key, methods[key]);
    } else $export($export.P + $export.F * (BUGGY || VALUES_BUG), NAME, methods);
  }
  return methods;
};

/***/ }),

/***/ 5508:
/***/ ((module, __unused_webpack_exports, __webpack_require__) => {

var ITERATOR = __webpack_require__(3336)('iterator');
var SAFE_CLOSING = false;
try {
  var riter = [7][ITERATOR]();
  riter['return'] = function () {
    SAFE_CLOSING = true;
  };
  // eslint-disable-next-line no-throw-literal
  Array.from(riter, function () {
    throw 2;
  });
} catch (e) {/* empty */}
module.exports = function (exec, skipClosing) {
  if (!skipClosing && !SAFE_CLOSING) return false;
  var safe = false;
  try {
    var arr = [7];
    var iter = arr[ITERATOR]();
    iter.next = function () {
      return {
        done: safe = true
      };
    };
    arr[ITERATOR] = function () {
      return iter;
    };
    exec(arr);
  } catch (e) {/* empty */}
  return safe;
};

/***/ }),

/***/ 7218:
/***/ ((module) => {

module.exports = function (done, value) {
  return {
    value: value,
    done: !!done
  };
};

/***/ }),

/***/ 5301:
/***/ ((module) => {

module.exports = {};

/***/ }),

/***/ 4219:
/***/ ((module) => {

module.exports = false;

/***/ }),

/***/ 4774:
/***/ ((module) => {

// 20.2.2.14 Math.expm1(x)
var $expm1 = Math.expm1;
module.exports = !$expm1
// Old FF bug
|| $expm1(10) > 22025.465794806719 || $expm1(10) < 22025.4657948067165168
// Tor Browser bug
|| $expm1(-2e-17) != -2e-17 ? function expm1(x) {
  return (x = +x) == 0 ? x : x > -1e-6 && x < 1e-6 ? x + x * x / 2 : Math.exp(x) - 1;
} : $expm1;

/***/ }),

/***/ 3800:
/***/ ((module, __unused_webpack_exports, __webpack_require__) => {

// 20.2.2.16 Math.fround(x)
var sign = __webpack_require__(4012);
var pow = Math.pow;
var EPSILON = pow(2, -52);
var EPSILON32 = pow(2, -23);
var MAX32 = pow(2, 127) * (2 - EPSILON32);
var MIN32 = pow(2, -126);
var roundTiesToEven = function roundTiesToEven(n) {
  return n + 1 / EPSILON - 1 / EPSILON;
};
module.exports = Math.fround || function fround(x) {
  var $abs = Math.abs(x);
  var $sign = sign(x);
  var a, result;
  if ($abs < MIN32) return $sign * roundTiesToEven($abs / MIN32 / EPSILON32) * MIN32 * EPSILON32;
  a = (1 + EPSILON32 / EPSILON) * $abs;
  result = a - (a - $abs);
  // eslint-disable-next-line no-self-compare
  if (result > MAX32 || result != result) return $sign * Infinity;
  return $sign * result;
};

/***/ }),

/***/ 5447:
/***/ ((module) => {

// 20.2.2.20 Math.log1p(x)
module.exports = Math.log1p || function log1p(x) {
  return (x = +x) > -1e-8 && x < 1e-8 ? x - x * x / 2 : Math.log(1 + x);
};

/***/ }),

/***/ 8124:
/***/ ((module) => {

// https://rwaldron.github.io/proposal-math-extensions/
module.exports = Math.scale || function scale(x, inLow, inHigh, outLow, outHigh) {
  if (arguments.length === 0
  // eslint-disable-next-line no-self-compare
  || x != x
  // eslint-disable-next-line no-self-compare
  || inLow != inLow
  // eslint-disable-next-line no-self-compare
  || inHigh != inHigh
  // eslint-disable-next-line no-self-compare
  || outLow != outLow
  // eslint-disable-next-line no-self-compare
  || outHigh != outHigh) return NaN;
  if (x === Infinity || x === -Infinity) return x;
  return (x - inLow) * (outHigh - outLow) / (inHigh - inLow) + outLow;
};

/***/ }),

/***/ 4012:
/***/ ((module) => {

// 20.2.2.28 Math.sign(x)
module.exports = Math.sign || function sign(x) {
  // eslint-disable-next-line no-self-compare
  return (x = +x) == 0 || x != x ? x : x < 0 ? -1 : 1;
};

/***/ }),

/***/ 3763:
/***/ ((module, __unused_webpack_exports, __webpack_require__) => {

function _typeof(obj) { "@babel/helpers - typeof"; return _typeof = "function" == typeof Symbol && "symbol" == typeof Symbol.iterator ? function (obj) { return typeof obj; } : function (obj) { return obj && "function" == typeof Symbol && obj.constructor === Symbol && obj !== Symbol.prototype ? "symbol" : typeof obj; }, _typeof(obj); }
var META = __webpack_require__(7936)('meta');
var isObject = __webpack_require__(7156);
var has = __webpack_require__(5389);
var setDesc = (__webpack_require__(4835).f);
var id = 0;
var isExtensible = Object.isExtensible || function () {
  return true;
};
var FREEZE = !__webpack_require__(5810)(function () {
  return isExtensible(Object.preventExtensions({}));
});
var setMeta = function setMeta(it) {
  setDesc(it, META, {
    value: {
      i: 'O' + ++id,
      // object ID
      w: {} // weak collections IDs
    }
  });
};

var fastKey = function fastKey(it, create) {
  // return primitive with prefix
  if (!isObject(it)) return _typeof(it) == 'symbol' ? it : (typeof it == 'string' ? 'S' : 'P') + it;
  if (!has(it, META)) {
    // can't set metadata to uncaught frozen object
    if (!isExtensible(it)) return 'F';
    // not necessary to add metadata
    if (!create) return 'E';
    // add missing metadata
    setMeta(it);
    // return object ID
  }
  return it[META].i;
};
var getWeak = function getWeak(it, create) {
  if (!has(it, META)) {
    // can't set metadata to uncaught frozen object
    if (!isExtensible(it)) return true;
    // not necessary to add metadata
    if (!create) return false;
    // add missing metadata
    setMeta(it);
    // return hash weak collections IDs
  }
  return it[META].w;
};
// add metadata on freeze-family methods calling
var onFreeze = function onFreeze(it) {
  if (FREEZE && meta.NEED && isExtensible(it) && !has(it, META)) setMeta(it);
  return it;
};
var meta = module.exports = {
  KEY: META,
  NEED: false,
  fastKey: fastKey,
  getWeak: getWeak,
  onFreeze: onFreeze
};

/***/ }),

/***/ 8953:
/***/ ((module, __unused_webpack_exports, __webpack_require__) => {

function _typeof(obj) { "@babel/helpers - typeof"; return _typeof = "function" == typeof Symbol && "symbol" == typeof Symbol.iterator ? function (obj) { return typeof obj; } : function (obj) { return obj && "function" == typeof Symbol && obj.constructor === Symbol && obj !== Symbol.prototype ? "symbol" : typeof obj; }, _typeof(obj); }
var Map = __webpack_require__(8969);
var $export = __webpack_require__(5913);
var shared = __webpack_require__(3192)('metadata');
var store = shared.store || (shared.store = new (__webpack_require__(3491))());
var getOrCreateMetadataMap = function getOrCreateMetadataMap(target, targetKey, create) {
  var targetMetadata = store.get(target);
  if (!targetMetadata) {
    if (!create) return undefined;
    store.set(target, targetMetadata = new Map());
  }
  var keyMetadata = targetMetadata.get(targetKey);
  if (!keyMetadata) {
    if (!create) return undefined;
    targetMetadata.set(targetKey, keyMetadata = new Map());
  }
  return keyMetadata;
};
var ordinaryHasOwnMetadata = function ordinaryHasOwnMetadata(MetadataKey, O, P) {
  var metadataMap = getOrCreateMetadataMap(O, P, false);
  return metadataMap === undefined ? false : metadataMap.has(MetadataKey);
};
var ordinaryGetOwnMetadata = function ordinaryGetOwnMetadata(MetadataKey, O, P) {
  var metadataMap = getOrCreateMetadataMap(O, P, false);
  return metadataMap === undefined ? undefined : metadataMap.get(MetadataKey);
};
var ordinaryDefineOwnMetadata = function ordinaryDefineOwnMetadata(MetadataKey, MetadataValue, O, P) {
  getOrCreateMetadataMap(O, P, true).set(MetadataKey, MetadataValue);
};
var ordinaryOwnMetadataKeys = function ordinaryOwnMetadataKeys(target, targetKey) {
  var metadataMap = getOrCreateMetadataMap(target, targetKey, false);
  var keys = [];
  if (metadataMap) metadataMap.forEach(function (_, key) {
    keys.push(key);
  });
  return keys;
};
var toMetaKey = function toMetaKey(it) {
  return it === undefined || _typeof(it) == 'symbol' ? it : String(it);
};
var exp = function exp(O) {
  $export($export.S, 'Reflect', O);
};
module.exports = {
  store: store,
  map: getOrCreateMetadataMap,
  has: ordinaryHasOwnMetadata,
  get: ordinaryGetOwnMetadata,
  set: ordinaryDefineOwnMetadata,
  keys: ordinaryOwnMetadataKeys,
  key: toMetaKey,
  exp: exp
};

/***/ }),

/***/ 1842:
/***/ ((module, __unused_webpack_exports, __webpack_require__) => {

var global = __webpack_require__(7381);
var macrotask = (__webpack_require__(8220).set);
var Observer = global.MutationObserver || global.WebKitMutationObserver;
var process = global.process;
var Promise = global.Promise;
var isNode = __webpack_require__(3679)(process) == 'process';
module.exports = function () {
  var head, last, notify;
  var flush = function flush() {
    var parent, fn;
    if (isNode && (parent = process.domain)) parent.exit();
    while (head) {
      fn = head.fn;
      head = head.next;
      try {
        fn();
      } catch (e) {
        if (head) notify();else last = undefined;
        throw e;
      }
    }
    last = undefined;
    if (parent) parent.enter();
  };

  // Node.js
  if (isNode) {
    notify = function notify() {
      process.nextTick(flush);
    };
    // browsers with MutationObserver, except iOS Safari - https://github.com/zloirock/core-js/issues/339
  } else if (Observer && !(global.navigator && global.navigator.standalone)) {
    var toggle = true;
    var node = document.createTextNode('');
    new Observer(flush).observe(node, {
      characterData: true
    }); // eslint-disable-line no-new
    notify = function notify() {
      node.data = toggle = !toggle;
    };
    // environments with maybe non-completely correct, but existent Promise
  } else if (Promise && Promise.resolve) {
    // Promise.resolve without an argument throws an error in LG WebOS 2
    var promise = Promise.resolve(undefined);
    notify = function notify() {
      promise.then(flush);
    };
    // for other environments - macrotask based on:
    // - setImmediate
    // - MessageChannel
    // - window.postMessag
    // - onreadystatechange
    // - setTimeout
  } else {
    notify = function notify() {
      // strange IE + webpack dev server bug - use .call(global)
      macrotask.call(global, flush);
    };
  }
  return function (fn) {
    var task = {
      fn: fn,
      next: undefined
    };
    if (last) last.next = task;
    if (!head) {
      head = task;
      notify();
    }
    last = task;
  };
};

/***/ }),

/***/ 4086:
/***/ ((module, __unused_webpack_exports, __webpack_require__) => {

"use strict";


// 25.4.1.5 NewPromiseCapability(C)
var aFunction = __webpack_require__(6819);
function PromiseCapability(C) {
  var resolve, reject;
  this.promise = new C(function ($$resolve, $$reject) {
    if (resolve !== undefined || reject !== undefined) throw TypeError('Bad Promise constructor');
    resolve = $$resolve;
    reject = $$reject;
  });
  this.resolve = aFunction(resolve);
  this.reject = aFunction(reject);
}
module.exports.f = function (C) {
  return new PromiseCapability(C);
};

/***/ }),

/***/ 8559:
/***/ ((module, __unused_webpack_exports, __webpack_require__) => {

"use strict";


// 19.1.2.1 Object.assign(target, source, ...)
var DESCRIPTORS = __webpack_require__(4926);
var getKeys = __webpack_require__(9924);
var gOPS = __webpack_require__(5421);
var pIE = __webpack_require__(4616);
var toObject = __webpack_require__(2515);
var IObject = __webpack_require__(331);
var $assign = Object.assign;

// should work with symbols and should have deterministic property order (V8 bug)
module.exports = !$assign || __webpack_require__(5810)(function () {
  var A = {};
  var B = {};
  // eslint-disable-next-line no-undef
  var S = Symbol();
  var K = 'abcdefghijklmnopqrst';
  A[S] = 7;
  K.split('').forEach(function (k) {
    B[k] = k;
  });
  return $assign({}, A)[S] != 7 || Object.keys($assign({}, B)).join('') != K;
}) ? function assign(target, source) {
  // eslint-disable-line no-unused-vars
  var T = toObject(target);
  var aLen = arguments.length;
  var index = 1;
  var getSymbols = gOPS.f;
  var isEnum = pIE.f;
  while (aLen > index) {
    var S = IObject(arguments[index++]);
    var keys = getSymbols ? getKeys(S).concat(getSymbols(S)) : getKeys(S);
    var length = keys.length;
    var j = 0;
    var key;
    while (length > j) {
      key = keys[j++];
      if (!DESCRIPTORS || isEnum.call(S, key)) T[key] = S[key];
    }
  }
  return T;
} : $assign;

/***/ }),

/***/ 4275:
/***/ ((module, __unused_webpack_exports, __webpack_require__) => {

// 19.1.2.2 / 15.2.3.5 Object.create(O [, Properties])
var anObject = __webpack_require__(6154);
var dPs = __webpack_require__(6447);
var enumBugKeys = __webpack_require__(6921);
var IE_PROTO = __webpack_require__(8662)('IE_PROTO');
var Empty = function Empty() {/* empty */};
var PROTOTYPE = 'prototype';

// Create object with fake `null` prototype: use iframe Object with cleared prototype
var _createDict = function createDict() {
  // Thrash, waste and sodomy: IE GC bug
  var iframe = __webpack_require__(2241)('iframe');
  var i = enumBugKeys.length;
  var lt = '<';
  var gt = '>';
  var iframeDocument;
  iframe.style.display = 'none';
  (__webpack_require__(1225).appendChild)(iframe);
  iframe.src = 'javascript:'; // eslint-disable-line no-script-url
  // createDict = iframe.contentWindow.Object;
  // html.removeChild(iframe);
  iframeDocument = iframe.contentWindow.document;
  iframeDocument.open();
  iframeDocument.write(lt + 'script' + gt + 'document.F=Object' + lt + '/script' + gt);
  iframeDocument.close();
  _createDict = iframeDocument.F;
  while (i--) {
    delete _createDict[PROTOTYPE][enumBugKeys[i]];
  }
  return _createDict();
};
module.exports = Object.create || function create(O, Properties) {
  var result;
  if (O !== null) {
    Empty[PROTOTYPE] = anObject(O);
    result = new Empty();
    Empty[PROTOTYPE] = null;
    // add "__proto__" for Object.getPrototypeOf polyfill
    result[IE_PROTO] = O;
  } else result = _createDict();
  return Properties === undefined ? result : dPs(result, Properties);
};

/***/ }),

/***/ 4835:
/***/ ((__unused_webpack_module, exports, __webpack_require__) => {

var anObject = __webpack_require__(6154);
var IE8_DOM_DEFINE = __webpack_require__(5142);
var toPrimitive = __webpack_require__(8537);
var dP = Object.defineProperty;
exports.f = __webpack_require__(4926) ? Object.defineProperty : function defineProperty(O, P, Attributes) {
  anObject(O);
  P = toPrimitive(P, true);
  anObject(Attributes);
  if (IE8_DOM_DEFINE) try {
    return dP(O, P, Attributes);
  } catch (e) {/* empty */}
  if ('get' in Attributes || 'set' in Attributes) throw TypeError('Accessors not supported!');
  if ('value' in Attributes) O[P] = Attributes.value;
  return O;
};

/***/ }),

/***/ 6447:
/***/ ((module, __unused_webpack_exports, __webpack_require__) => {

var dP = __webpack_require__(4835);
var anObject = __webpack_require__(6154);
var getKeys = __webpack_require__(9924);
module.exports = __webpack_require__(4926) ? Object.defineProperties : function defineProperties(O, Properties) {
  anObject(O);
  var keys = getKeys(Properties);
  var length = keys.length;
  var i = 0;
  var P;
  while (length > i) {
    dP.f(O, P = keys[i++], Properties[P]);
  }
  return O;
};

/***/ }),

/***/ 8249:
/***/ ((module, __unused_webpack_exports, __webpack_require__) => {

"use strict";


// Forced replacement prototype accessors methods
module.exports = __webpack_require__(4219) || !__webpack_require__(5810)(function () {
  var K = Math.random();
  // In FF throws only define methods
  // eslint-disable-next-line no-undef, no-useless-call
  __defineSetter__.call(null, K, function () {/* empty */});
  delete __webpack_require__(7381)[K];
});

/***/ }),

/***/ 3299:
/***/ ((__unused_webpack_module, exports, __webpack_require__) => {

var pIE = __webpack_require__(4616);
var createDesc = __webpack_require__(6256);
var toIObject = __webpack_require__(8499);
var toPrimitive = __webpack_require__(8537);
var has = __webpack_require__(5389);
var IE8_DOM_DEFINE = __webpack_require__(5142);
var gOPD = Object.getOwnPropertyDescriptor;
exports.f = __webpack_require__(4926) ? gOPD : function getOwnPropertyDescriptor(O, P) {
  O = toIObject(O);
  P = toPrimitive(P, true);
  if (IE8_DOM_DEFINE) try {
    return gOPD(O, P);
  } catch (e) {/* empty */}
  if (has(O, P)) return createDesc(!pIE.f.call(O, P), O[P]);
};

/***/ }),

/***/ 3136:
/***/ ((module, __unused_webpack_exports, __webpack_require__) => {

function _typeof(obj) { "@babel/helpers - typeof"; return _typeof = "function" == typeof Symbol && "symbol" == typeof Symbol.iterator ? function (obj) { return typeof obj; } : function (obj) { return obj && "function" == typeof Symbol && obj.constructor === Symbol && obj !== Symbol.prototype ? "symbol" : typeof obj; }, _typeof(obj); }
// fallback for IE11 buggy Object.getOwnPropertyNames with iframe and window
var toIObject = __webpack_require__(8499);
var gOPN = (__webpack_require__(2982).f);
var toString = {}.toString;
var windowNames = (typeof window === "undefined" ? "undefined" : _typeof(window)) == 'object' && window && Object.getOwnPropertyNames ? Object.getOwnPropertyNames(window) : [];
var getWindowNames = function getWindowNames(it) {
  try {
    return gOPN(it);
  } catch (e) {
    return windowNames.slice();
  }
};
module.exports.f = function getOwnPropertyNames(it) {
  return windowNames && toString.call(it) == '[object Window]' ? getWindowNames(it) : gOPN(toIObject(it));
};

/***/ }),

/***/ 2982:
/***/ ((__unused_webpack_module, exports, __webpack_require__) => {

// 19.1.2.7 / 15.2.3.4 Object.getOwnPropertyNames(O)
var $keys = __webpack_require__(7960);
var hiddenKeys = (__webpack_require__(6921).concat)('length', 'prototype');
exports.f = Object.getOwnPropertyNames || function getOwnPropertyNames(O) {
  return $keys(O, hiddenKeys);
};

/***/ }),

/***/ 5421:
/***/ ((__unused_webpack_module, exports) => {

exports.f = Object.getOwnPropertySymbols;

/***/ }),

/***/ 4153:
/***/ ((module, __unused_webpack_exports, __webpack_require__) => {

// 19.1.2.9 / 15.2.3.2 Object.getPrototypeOf(O)
var has = __webpack_require__(5389);
var toObject = __webpack_require__(2515);
var IE_PROTO = __webpack_require__(8662)('IE_PROTO');
var ObjectProto = Object.prototype;
module.exports = Object.getPrototypeOf || function (O) {
  O = toObject(O);
  if (has(O, IE_PROTO)) return O[IE_PROTO];
  if (typeof O.constructor == 'function' && O instanceof O.constructor) {
    return O.constructor.prototype;
  }
  return O instanceof Object ? ObjectProto : null;
};

/***/ }),

/***/ 7960:
/***/ ((module, __unused_webpack_exports, __webpack_require__) => {

var has = __webpack_require__(5389);
var toIObject = __webpack_require__(8499);
var arrayIndexOf = __webpack_require__(4687)(false);
var IE_PROTO = __webpack_require__(8662)('IE_PROTO');
module.exports = function (object, names) {
  var O = toIObject(object);
  var i = 0;
  var result = [];
  var key;
  for (key in O) {
    if (key != IE_PROTO) has(O, key) && result.push(key);
  }
  // Don't enum bug & hidden keys
  while (names.length > i) {
    if (has(O, key = names[i++])) {
      ~arrayIndexOf(result, key) || result.push(key);
    }
  }
  return result;
};

/***/ }),

/***/ 9924:
/***/ ((module, __unused_webpack_exports, __webpack_require__) => {

// 19.1.2.14 / 15.2.3.14 Object.keys(O)
var $keys = __webpack_require__(7960);
var enumBugKeys = __webpack_require__(6921);
module.exports = Object.keys || function keys(O) {
  return $keys(O, enumBugKeys);
};

/***/ }),

/***/ 4616:
/***/ ((__unused_webpack_module, exports) => {

exports.f = {}.propertyIsEnumerable;

/***/ }),

/***/ 4057:
/***/ ((module, __unused_webpack_exports, __webpack_require__) => {

// most Object methods by ES6 should accept primitives
var $export = __webpack_require__(5913);
var core = __webpack_require__(8544);
var fails = __webpack_require__(5810);
module.exports = function (KEY, exec) {
  var fn = (core.Object || {})[KEY] || Object[KEY];
  var exp = {};
  exp[KEY] = exec(fn);
  $export($export.S + $export.F * fails(function () {
    fn(1);
  }), 'Object', exp);
};

/***/ }),

/***/ 8941:
/***/ ((module, __unused_webpack_exports, __webpack_require__) => {

var DESCRIPTORS = __webpack_require__(4926);
var getKeys = __webpack_require__(9924);
var toIObject = __webpack_require__(8499);
var isEnum = (__webpack_require__(4616).f);
module.exports = function (isEntries) {
  return function (it) {
    var O = toIObject(it);
    var keys = getKeys(O);
    var length = keys.length;
    var i = 0;
    var result = [];
    var key;
    while (length > i) {
      key = keys[i++];
      if (!DESCRIPTORS || isEnum.call(O, key)) {
        result.push(isEntries ? [key, O[key]] : O[key]);
      }
    }
    return result;
  };
};

/***/ }),

/***/ 2600:
/***/ ((module, __unused_webpack_exports, __webpack_require__) => {

// all object keys, includes non-enumerable and symbols
var gOPN = __webpack_require__(2982);
var gOPS = __webpack_require__(5421);
var anObject = __webpack_require__(6154);
var Reflect = (__webpack_require__(7381).Reflect);
module.exports = Reflect && Reflect.ownKeys || function ownKeys(it) {
  var keys = gOPN.f(anObject(it));
  var getSymbols = gOPS.f;
  return getSymbols ? keys.concat(getSymbols(it)) : keys;
};

/***/ }),

/***/ 5031:
/***/ ((module, __unused_webpack_exports, __webpack_require__) => {

var $parseFloat = (__webpack_require__(7381).parseFloat);
var $trim = (__webpack_require__(618).trim);
module.exports = 1 / $parseFloat(__webpack_require__(3596) + '-0') !== -Infinity ? function parseFloat(str) {
  var string = $trim(String(str), 3);
  var result = $parseFloat(string);
  return result === 0 && string.charAt(0) == '-' ? -0 : result;
} : $parseFloat;

/***/ }),

/***/ 6971:
/***/ ((module, __unused_webpack_exports, __webpack_require__) => {

var $parseInt = (__webpack_require__(7381).parseInt);
var $trim = (__webpack_require__(618).trim);
var ws = __webpack_require__(3596);
var hex = /^[-+]?0[xX]/;
module.exports = $parseInt(ws + '08') !== 8 || $parseInt(ws + '0x16') !== 22 ? function parseInt(str, radix) {
  var string = $trim(String(str), 3);
  return $parseInt(string, radix >>> 0 || (hex.test(string) ? 16 : 10));
} : $parseInt;

/***/ }),

/***/ 8228:
/***/ ((module) => {

module.exports = function (exec) {
  try {
    return {
      e: false,
      v: exec()
    };
  } catch (e) {
    return {
      e: true,
      v: e
    };
  }
};

/***/ }),

/***/ 3507:
/***/ ((module, __unused_webpack_exports, __webpack_require__) => {

var anObject = __webpack_require__(6154);
var isObject = __webpack_require__(7156);
var newPromiseCapability = __webpack_require__(4086);
module.exports = function (C, x) {
  anObject(C);
  if (isObject(x) && x.constructor === C) return x;
  var promiseCapability = newPromiseCapability.f(C);
  var resolve = promiseCapability.resolve;
  resolve(x);
  return promiseCapability.promise;
};

/***/ }),

/***/ 6256:
/***/ ((module) => {

module.exports = function (bitmap, value) {
  return {
    enumerable: !(bitmap & 1),
    configurable: !(bitmap & 2),
    writable: !(bitmap & 4),
    value: value
  };
};

/***/ }),

/***/ 7228:
/***/ ((module, __unused_webpack_exports, __webpack_require__) => {

var redefine = __webpack_require__(7278);
module.exports = function (target, src, safe) {
  for (var key in src) {
    redefine(target, key, src[key], safe);
  }
  return target;
};

/***/ }),

/***/ 7278:
/***/ ((module, __unused_webpack_exports, __webpack_require__) => {

var global = __webpack_require__(7381);
var hide = __webpack_require__(8012);
var has = __webpack_require__(5389);
var SRC = __webpack_require__(7936)('src');
var $toString = __webpack_require__(1174);
var TO_STRING = 'toString';
var TPL = ('' + $toString).split(TO_STRING);
(__webpack_require__(8544).inspectSource) = function (it) {
  return $toString.call(it);
};
(module.exports = function (O, key, val, safe) {
  var isFunction = typeof val == 'function';
  if (isFunction) has(val, 'name') || hide(val, 'name', key);
  if (O[key] === val) return;
  if (isFunction) has(val, SRC) || hide(val, SRC, O[key] ? '' + O[key] : TPL.join(String(key)));
  if (O === global) {
    O[key] = val;
  } else if (!safe) {
    delete O[key];
    hide(O, key, val);
  } else if (O[key]) {
    O[key] = val;
  } else {
    hide(O, key, val);
  }
  // add fake Function#toString for correct work wrapped methods / constructors with methods like LoDash isNative
})(Function.prototype, TO_STRING, function toString() {
  return typeof this == 'function' && this[SRC] || $toString.call(this);
});

/***/ }),

/***/ 4585:
/***/ ((module, __unused_webpack_exports, __webpack_require__) => {

"use strict";


function _typeof(obj) { "@babel/helpers - typeof"; return _typeof = "function" == typeof Symbol && "symbol" == typeof Symbol.iterator ? function (obj) { return typeof obj; } : function (obj) { return obj && "function" == typeof Symbol && obj.constructor === Symbol && obj !== Symbol.prototype ? "symbol" : typeof obj; }, _typeof(obj); }
var classof = __webpack_require__(2858);
var builtinExec = RegExp.prototype.exec;

// `RegExpExec` abstract operation
// https://tc39.github.io/ecma262/#sec-regexpexec
module.exports = function (R, S) {
  var exec = R.exec;
  if (typeof exec === 'function') {
    var result = exec.call(R, S);
    if (_typeof(result) !== 'object') {
      throw new TypeError('RegExp exec method returned something other than an Object or null');
    }
    return result;
  }
  if (classof(R) !== 'RegExp') {
    throw new TypeError('RegExp#exec called on incompatible receiver');
  }
  return builtinExec.call(R, S);
};

/***/ }),

/***/ 6997:
/***/ ((module, __unused_webpack_exports, __webpack_require__) => {

"use strict";


var regexpFlags = __webpack_require__(2188);
var nativeExec = RegExp.prototype.exec;
// This always refers to the native implementation, because the
// String#replace polyfill uses ./fix-regexp-well-known-symbol-logic.js,
// which loads this file before patching the method.
var nativeReplace = String.prototype.replace;
var patchedExec = nativeExec;
var LAST_INDEX = 'lastIndex';
var UPDATES_LAST_INDEX_WRONG = function () {
  var re1 = /a/,
    re2 = /b*/g;
  nativeExec.call(re1, 'a');
  nativeExec.call(re2, 'a');
  return re1[LAST_INDEX] !== 0 || re2[LAST_INDEX] !== 0;
}();

// nonparticipating capturing group, copied from es5-shim's String#split patch.
var NPCG_INCLUDED = /()??/.exec('')[1] !== undefined;
var PATCH = UPDATES_LAST_INDEX_WRONG || NPCG_INCLUDED;
if (PATCH) {
  patchedExec = function exec(str) {
    var re = this;
    var lastIndex, reCopy, match, i;
    if (NPCG_INCLUDED) {
      reCopy = new RegExp('^' + re.source + '$(?!\\s)', regexpFlags.call(re));
    }
    if (UPDATES_LAST_INDEX_WRONG) lastIndex = re[LAST_INDEX];
    match = nativeExec.call(re, str);
    if (UPDATES_LAST_INDEX_WRONG && match) {
      re[LAST_INDEX] = re.global ? match.index + match[0].length : lastIndex;
    }
    if (NPCG_INCLUDED && match && match.length > 1) {
      // Fix browsers whose `exec` methods don't consistently return `undefined`
      // for NPCG, like IE8. NOTE: This doesn' work for /(.?)?/
      // eslint-disable-next-line no-loop-func
      nativeReplace.call(match[0], reCopy, function () {
        for (i = 1; i < arguments.length - 2; i++) {
          if (arguments[i] === undefined) match[i] = undefined;
        }
      });
    }
    return match;
  };
}
module.exports = patchedExec;

/***/ }),

/***/ 6813:
/***/ ((module) => {

module.exports = function (regExp, replace) {
  var replacer = replace === Object(replace) ? function (part) {
    return replace[part];
  } : replace;
  return function (it) {
    return String(it).replace(regExp, replacer);
  };
};

/***/ }),

/***/ 4261:
/***/ ((module) => {

// 7.2.9 SameValue(x, y)
module.exports = Object.is || function is(x, y) {
  // eslint-disable-next-line no-self-compare
  return x === y ? x !== 0 || 1 / x === 1 / y : x != x && y != y;
};

/***/ }),

/***/ 7598:
/***/ ((module, __unused_webpack_exports, __webpack_require__) => {

"use strict";


// https://tc39.github.io/proposal-setmap-offrom/
var $export = __webpack_require__(5913);
var aFunction = __webpack_require__(6819);
var ctx = __webpack_require__(566);
var forOf = __webpack_require__(2734);
module.exports = function (COLLECTION) {
  $export($export.S, COLLECTION, {
    from: function from(source /* , mapFn, thisArg */) {
      var mapFn = arguments[1];
      var mapping, A, n, cb;
      aFunction(this);
      mapping = mapFn !== undefined;
      if (mapping) aFunction(mapFn);
      if (source == undefined) return new this();
      A = [];
      if (mapping) {
        n = 0;
        cb = ctx(mapFn, arguments[2], 2);
        forOf(source, false, function (nextItem) {
          A.push(cb(nextItem, n++));
        });
      } else {
        forOf(source, false, A.push, A);
      }
      return new this(A);
    }
  });
};

/***/ }),

/***/ 5329:
/***/ ((module, __unused_webpack_exports, __webpack_require__) => {

"use strict";


// https://tc39.github.io/proposal-setmap-offrom/
var $export = __webpack_require__(5913);
module.exports = function (COLLECTION) {
  $export($export.S, COLLECTION, {
    of: function of() {
      var length = arguments.length;
      var A = new Array(length);
      while (length--) {
        A[length] = arguments[length];
      }
      return new this(A);
    }
  });
};

/***/ }),

/***/ 6931:
/***/ ((module, __unused_webpack_exports, __webpack_require__) => {

// Works with __proto__ only. Old v8 can't work with null proto objects.
/* eslint-disable no-proto */
var isObject = __webpack_require__(7156);
var anObject = __webpack_require__(6154);
var check = function check(O, proto) {
  anObject(O);
  if (!isObject(proto) && proto !== null) throw TypeError(proto + ": can't set as prototype!");
};
module.exports = {
  set: Object.setPrototypeOf || ('__proto__' in {} ?
  // eslint-disable-line
  function (test, buggy, set) {
    try {
      set = __webpack_require__(566)(Function.call, (__webpack_require__(3299).f)(Object.prototype, '__proto__').set, 2);
      set(test, []);
      buggy = !(test instanceof Array);
    } catch (e) {
      buggy = true;
    }
    return function setPrototypeOf(O, proto) {
      check(O, proto);
      if (buggy) O.__proto__ = proto;else set(O, proto);
      return O;
    };
  }({}, false) : undefined),
  check: check
};

/***/ }),

/***/ 4798:
/***/ ((module, __unused_webpack_exports, __webpack_require__) => {

"use strict";


var global = __webpack_require__(7381);
var dP = __webpack_require__(4835);
var DESCRIPTORS = __webpack_require__(4926);
var SPECIES = __webpack_require__(3336)('species');
module.exports = function (KEY) {
  var C = global[KEY];
  if (DESCRIPTORS && C && !C[SPECIES]) dP.f(C, SPECIES, {
    configurable: true,
    get: function get() {
      return this;
    }
  });
};

/***/ }),

/***/ 8094:
/***/ ((module, __unused_webpack_exports, __webpack_require__) => {

var def = (__webpack_require__(4835).f);
var has = __webpack_require__(5389);
var TAG = __webpack_require__(3336)('toStringTag');
module.exports = function (it, tag, stat) {
  if (it && !has(it = stat ? it : it.prototype, TAG)) def(it, TAG, {
    configurable: true,
    value: tag
  });
};

/***/ }),

/***/ 8662:
/***/ ((module, __unused_webpack_exports, __webpack_require__) => {

var shared = __webpack_require__(3192)('keys');
var uid = __webpack_require__(7936);
module.exports = function (key) {
  return shared[key] || (shared[key] = uid(key));
};

/***/ }),

/***/ 3192:
/***/ ((module, __unused_webpack_exports, __webpack_require__) => {

var core = __webpack_require__(8544);
var global = __webpack_require__(7381);
var SHARED = '__core-js_shared__';
var store = global[SHARED] || (global[SHARED] = {});
(module.exports = function (key, value) {
  return store[key] || (store[key] = value !== undefined ? value : {});
})('versions', []).push({
  version: core.version,
  mode: __webpack_require__(4219) ? 'pure' : 'global',
  copyright: '© 2020 Denis Pushkarev (zloirock.ru)'
});

/***/ }),

/***/ 2035:
/***/ ((module, __unused_webpack_exports, __webpack_require__) => {

// 7.3.20 SpeciesConstructor(O, defaultConstructor)
var anObject = __webpack_require__(6154);
var aFunction = __webpack_require__(6819);
var SPECIES = __webpack_require__(3336)('species');
module.exports = function (O, D) {
  var C = anObject(O).constructor;
  var S;
  return C === undefined || (S = anObject(C)[SPECIES]) == undefined ? D : aFunction(S);
};

/***/ }),

/***/ 1411:
/***/ ((module, __unused_webpack_exports, __webpack_require__) => {

"use strict";


var fails = __webpack_require__(5810);
module.exports = function (method, arg) {
  return !!method && fails(function () {
    // eslint-disable-next-line no-useless-call
    arg ? method.call(null, function () {/* empty */}, 1) : method.call(null);
  });
};

/***/ }),

/***/ 3593:
/***/ ((module, __unused_webpack_exports, __webpack_require__) => {

var toInteger = __webpack_require__(3230);
var defined = __webpack_require__(408);
// true  -> String#at
// false -> String#codePointAt
module.exports = function (TO_STRING) {
  return function (that, pos) {
    var s = String(defined(that));
    var i = toInteger(pos);
    var l = s.length;
    var a, b;
    if (i < 0 || i >= l) return TO_STRING ? '' : undefined;
    a = s.charCodeAt(i);
    return a < 0xd800 || a > 0xdbff || i + 1 === l || (b = s.charCodeAt(i + 1)) < 0xdc00 || b > 0xdfff ? TO_STRING ? s.charAt(i) : a : TO_STRING ? s.slice(i, i + 2) : (a - 0xd800 << 10) + (b - 0xdc00) + 0x10000;
  };
};

/***/ }),

/***/ 2376:
/***/ ((module, __unused_webpack_exports, __webpack_require__) => {

// helper for String#{startsWith, endsWith, includes}
var isRegExp = __webpack_require__(1993);
var defined = __webpack_require__(408);
module.exports = function (that, searchString, NAME) {
  if (isRegExp(searchString)) throw TypeError('String#' + NAME + " doesn't accept regex!");
  return String(defined(that));
};

/***/ }),

/***/ 9927:
/***/ ((module, __unused_webpack_exports, __webpack_require__) => {

var $export = __webpack_require__(5913);
var fails = __webpack_require__(5810);
var defined = __webpack_require__(408);
var quot = /"/g;
// B.2.3.2.1 CreateHTML(string, tag, attribute, value)
var createHTML = function createHTML(string, tag, attribute, value) {
  var S = String(defined(string));
  var p1 = '<' + tag;
  if (attribute !== '') p1 += ' ' + attribute + '="' + String(value).replace(quot, '&quot;') + '"';
  return p1 + '>' + S + '</' + tag + '>';
};
module.exports = function (NAME, exec) {
  var O = {};
  O[NAME] = exec(createHTML);
  $export($export.P + $export.F * fails(function () {
    var test = ''[NAME]('"');
    return test !== test.toLowerCase() || test.split('"').length > 3;
  }), 'String', O);
};

/***/ }),

/***/ 1925:
/***/ ((module, __unused_webpack_exports, __webpack_require__) => {

// https://github.com/tc39/proposal-string-pad-start-end
var toLength = __webpack_require__(8315);
var repeat = __webpack_require__(1924);
var defined = __webpack_require__(408);
module.exports = function (that, maxLength, fillString, left) {
  var S = String(defined(that));
  var stringLength = S.length;
  var fillStr = fillString === undefined ? ' ' : String(fillString);
  var intMaxLength = toLength(maxLength);
  if (intMaxLength <= stringLength || fillStr == '') return S;
  var fillLen = intMaxLength - stringLength;
  var stringFiller = repeat.call(fillStr, Math.ceil(fillLen / fillStr.length));
  if (stringFiller.length > fillLen) stringFiller = stringFiller.slice(0, fillLen);
  return left ? stringFiller + S : S + stringFiller;
};

/***/ }),

/***/ 1924:
/***/ ((module, __unused_webpack_exports, __webpack_require__) => {

"use strict";


var toInteger = __webpack_require__(3230);
var defined = __webpack_require__(408);
module.exports = function repeat(count) {
  var str = String(defined(this));
  var res = '';
  var n = toInteger(count);
  if (n < 0 || n == Infinity) throw RangeError("Count can't be negative");
  for (; n > 0; (n >>>= 1) && (str += str)) {
    if (n & 1) res += str;
  }
  return res;
};

/***/ }),

/***/ 618:
/***/ ((module, __unused_webpack_exports, __webpack_require__) => {

var $export = __webpack_require__(5913);
var defined = __webpack_require__(408);
var fails = __webpack_require__(5810);
var spaces = __webpack_require__(3596);
var space = '[' + spaces + ']';
var non = "\u200B\x85";
var ltrim = RegExp('^' + space + space + '*');
var rtrim = RegExp(space + space + '*$');
var exporter = function exporter(KEY, exec, ALIAS) {
  var exp = {};
  var FORCE = fails(function () {
    return !!spaces[KEY]() || non[KEY]() != non;
  });
  var fn = exp[KEY] = FORCE ? exec(trim) : spaces[KEY];
  if (ALIAS) exp[ALIAS] = fn;
  $export($export.P + $export.F * FORCE, 'String', exp);
};

// 1 -> String#trimLeft
// 2 -> String#trimRight
// 3 -> String#trim
var trim = exporter.trim = function (string, TYPE) {
  string = String(defined(string));
  if (TYPE & 1) string = string.replace(ltrim, '');
  if (TYPE & 2) string = string.replace(rtrim, '');
  return string;
};
module.exports = exporter;

/***/ }),

/***/ 3596:
/***/ ((module) => {

module.exports = "\t\n\x0B\f\r \xA0\u1680\u180E\u2000\u2001\u2002\u2003" + "\u2004\u2005\u2006\u2007\u2008\u2009\u200A\u202F\u205F\u3000\u2028\u2029\uFEFF";

/***/ }),

/***/ 8220:
/***/ ((module, __unused_webpack_exports, __webpack_require__) => {

var ctx = __webpack_require__(566);
var invoke = __webpack_require__(2765);
var html = __webpack_require__(1225);
var cel = __webpack_require__(2241);
var global = __webpack_require__(7381);
var process = global.process;
var setTask = global.setImmediate;
var clearTask = global.clearImmediate;
var MessageChannel = global.MessageChannel;
var Dispatch = global.Dispatch;
var counter = 0;
var queue = {};
var ONREADYSTATECHANGE = 'onreadystatechange';
var defer, channel, port;
var run = function run() {
  var id = +this;
  // eslint-disable-next-line no-prototype-builtins
  if (queue.hasOwnProperty(id)) {
    var fn = queue[id];
    delete queue[id];
    fn();
  }
};
var listener = function listener(event) {
  run.call(event.data);
};
// Node.js 0.9+ & IE10+ has setImmediate, otherwise:
if (!setTask || !clearTask) {
  setTask = function setImmediate(fn) {
    var args = [];
    var i = 1;
    while (arguments.length > i) {
      args.push(arguments[i++]);
    }
    queue[++counter] = function () {
      // eslint-disable-next-line no-new-func
      invoke(typeof fn == 'function' ? fn : Function(fn), args);
    };
    defer(counter);
    return counter;
  };
  clearTask = function clearImmediate(id) {
    delete queue[id];
  };
  // Node.js 0.8-
  if (__webpack_require__(3679)(process) == 'process') {
    defer = function defer(id) {
      process.nextTick(ctx(run, id, 1));
    };
    // Sphere (JS game engine) Dispatch API
  } else if (Dispatch && Dispatch.now) {
    defer = function defer(id) {
      Dispatch.now(ctx(run, id, 1));
    };
    // Browsers with MessageChannel, includes WebWorkers
  } else if (MessageChannel) {
    channel = new MessageChannel();
    port = channel.port2;
    channel.port1.onmessage = listener;
    defer = ctx(port.postMessage, port, 1);
    // Browsers with postMessage, skip WebWorkers
    // IE8 has postMessage, but it's sync & typeof its postMessage is 'object'
  } else if (global.addEventListener && typeof postMessage == 'function' && !global.importScripts) {
    defer = function defer(id) {
      global.postMessage(id + '', '*');
    };
    global.addEventListener('message', listener, false);
    // IE8-
  } else if (ONREADYSTATECHANGE in cel('script')) {
    defer = function defer(id) {
      html.appendChild(cel('script'))[ONREADYSTATECHANGE] = function () {
        html.removeChild(this);
        run.call(id);
      };
    };
    // Rest old browsers
  } else {
    defer = function defer(id) {
      setTimeout(ctx(run, id, 1), 0);
    };
  }
}
module.exports = {
  set: setTask,
  clear: clearTask
};

/***/ }),

/***/ 6241:
/***/ ((module, __unused_webpack_exports, __webpack_require__) => {

var toInteger = __webpack_require__(3230);
var max = Math.max;
var min = Math.min;
module.exports = function (index, length) {
  index = toInteger(index);
  return index < 0 ? max(index + length, 0) : min(index, length);
};

/***/ }),

/***/ 3472:
/***/ ((module, __unused_webpack_exports, __webpack_require__) => {

// https://tc39.github.io/ecma262/#sec-toindex
var toInteger = __webpack_require__(3230);
var toLength = __webpack_require__(8315);
module.exports = function (it) {
  if (it === undefined) return 0;
  var number = toInteger(it);
  var length = toLength(number);
  if (number !== length) throw RangeError('Wrong length!');
  return length;
};

/***/ }),

/***/ 3230:
/***/ ((module) => {

// 7.1.4 ToInteger
var ceil = Math.ceil;
var floor = Math.floor;
module.exports = function (it) {
  return isNaN(it = +it) ? 0 : (it > 0 ? floor : ceil)(it);
};

/***/ }),

/***/ 8499:
/***/ ((module, __unused_webpack_exports, __webpack_require__) => {

// to indexed object, toObject with fallback for non-array-like ES3 strings
var IObject = __webpack_require__(331);
var defined = __webpack_require__(408);
module.exports = function (it) {
  return IObject(defined(it));
};

/***/ }),

/***/ 8315:
/***/ ((module, __unused_webpack_exports, __webpack_require__) => {

// 7.1.15 ToLength
var toInteger = __webpack_require__(3230);
var min = Math.min;
module.exports = function (it) {
  return it > 0 ? min(toInteger(it), 0x1fffffffffffff) : 0; // pow(2, 53) - 1 == 9007199254740991
};

/***/ }),

/***/ 2515:
/***/ ((module, __unused_webpack_exports, __webpack_require__) => {

// 7.1.13 ToObject(argument)
var defined = __webpack_require__(408);
module.exports = function (it) {
  return Object(defined(it));
};

/***/ }),

/***/ 8537:
/***/ ((module, __unused_webpack_exports, __webpack_require__) => {

// 7.1.1 ToPrimitive(input [, PreferredType])
var isObject = __webpack_require__(7156);
// instead of the ES6 spec version, we didn't implement @@toPrimitive case
// and the second argument - flag - preferred type is a string
module.exports = function (it, S) {
  if (!isObject(it)) return it;
  var fn, val;
  if (S && typeof (fn = it.toString) == 'function' && !isObject(val = fn.call(it))) return val;
  if (typeof (fn = it.valueOf) == 'function' && !isObject(val = fn.call(it))) return val;
  if (!S && typeof (fn = it.toString) == 'function' && !isObject(val = fn.call(it))) return val;
  throw TypeError("Can't convert object to primitive value");
};

/***/ }),

/***/ 431:
/***/ ((module, __unused_webpack_exports, __webpack_require__) => {

"use strict";


function _typeof(obj) { "@babel/helpers - typeof"; return _typeof = "function" == typeof Symbol && "symbol" == typeof Symbol.iterator ? function (obj) { return typeof obj; } : function (obj) { return obj && "function" == typeof Symbol && obj.constructor === Symbol && obj !== Symbol.prototype ? "symbol" : typeof obj; }, _typeof(obj); }
if (__webpack_require__(4926)) {
  var LIBRARY = __webpack_require__(4219);
  var global = __webpack_require__(7381);
  var fails = __webpack_require__(5810);
  var $export = __webpack_require__(5913);
  var $typed = __webpack_require__(9161);
  var $buffer = __webpack_require__(9782);
  var ctx = __webpack_require__(566);
  var anInstance = __webpack_require__(2702);
  var propertyDesc = __webpack_require__(6256);
  var hide = __webpack_require__(8012);
  var redefineAll = __webpack_require__(7228);
  var toInteger = __webpack_require__(3230);
  var toLength = __webpack_require__(8315);
  var toIndex = __webpack_require__(3472);
  var toAbsoluteIndex = __webpack_require__(6241);
  var toPrimitive = __webpack_require__(8537);
  var has = __webpack_require__(5389);
  var classof = __webpack_require__(2858);
  var isObject = __webpack_require__(7156);
  var toObject = __webpack_require__(2515);
  var isArrayIter = __webpack_require__(7063);
  var create = __webpack_require__(4275);
  var getPrototypeOf = __webpack_require__(4153);
  var gOPN = (__webpack_require__(2982).f);
  var getIterFn = __webpack_require__(7637);
  var uid = __webpack_require__(7936);
  var wks = __webpack_require__(3336);
  var createArrayMethod = __webpack_require__(3970);
  var createArrayIncludes = __webpack_require__(4687);
  var speciesConstructor = __webpack_require__(2035);
  var ArrayIterators = __webpack_require__(4806);
  var Iterators = __webpack_require__(5301);
  var $iterDetect = __webpack_require__(5508);
  var setSpecies = __webpack_require__(4798);
  var arrayFill = __webpack_require__(1132);
  var arrayCopyWithin = __webpack_require__(2147);
  var $DP = __webpack_require__(4835);
  var $GOPD = __webpack_require__(3299);
  var dP = $DP.f;
  var gOPD = $GOPD.f;
  var RangeError = global.RangeError;
  var TypeError = global.TypeError;
  var Uint8Array = global.Uint8Array;
  var ARRAY_BUFFER = 'ArrayBuffer';
  var SHARED_BUFFER = 'Shared' + ARRAY_BUFFER;
  var BYTES_PER_ELEMENT = 'BYTES_PER_ELEMENT';
  var PROTOTYPE = 'prototype';
  var ArrayProto = Array[PROTOTYPE];
  var $ArrayBuffer = $buffer.ArrayBuffer;
  var $DataView = $buffer.DataView;
  var arrayForEach = createArrayMethod(0);
  var arrayFilter = createArrayMethod(2);
  var arraySome = createArrayMethod(3);
  var arrayEvery = createArrayMethod(4);
  var arrayFind = createArrayMethod(5);
  var arrayFindIndex = createArrayMethod(6);
  var arrayIncludes = createArrayIncludes(true);
  var arrayIndexOf = createArrayIncludes(false);
  var arrayValues = ArrayIterators.values;
  var arrayKeys = ArrayIterators.keys;
  var arrayEntries = ArrayIterators.entries;
  var arrayLastIndexOf = ArrayProto.lastIndexOf;
  var arrayReduce = ArrayProto.reduce;
  var arrayReduceRight = ArrayProto.reduceRight;
  var arrayJoin = ArrayProto.join;
  var arraySort = ArrayProto.sort;
  var arraySlice = ArrayProto.slice;
  var arrayToString = ArrayProto.toString;
  var arrayToLocaleString = ArrayProto.toLocaleString;
  var ITERATOR = wks('iterator');
  var TAG = wks('toStringTag');
  var TYPED_CONSTRUCTOR = uid('typed_constructor');
  var DEF_CONSTRUCTOR = uid('def_constructor');
  var ALL_CONSTRUCTORS = $typed.CONSTR;
  var TYPED_ARRAY = $typed.TYPED;
  var VIEW = $typed.VIEW;
  var WRONG_LENGTH = 'Wrong length!';
  var $map = createArrayMethod(1, function (O, length) {
    return allocate(speciesConstructor(O, O[DEF_CONSTRUCTOR]), length);
  });
  var LITTLE_ENDIAN = fails(function () {
    // eslint-disable-next-line no-undef
    return new Uint8Array(new Uint16Array([1]).buffer)[0] === 1;
  });
  var FORCED_SET = !!Uint8Array && !!Uint8Array[PROTOTYPE].set && fails(function () {
    new Uint8Array(1).set({});
  });
  var toOffset = function toOffset(it, BYTES) {
    var offset = toInteger(it);
    if (offset < 0 || offset % BYTES) throw RangeError('Wrong offset!');
    return offset;
  };
  var validate = function validate(it) {
    if (isObject(it) && TYPED_ARRAY in it) return it;
    throw TypeError(it + ' is not a typed array!');
  };
  var allocate = function allocate(C, length) {
    if (!(isObject(C) && TYPED_CONSTRUCTOR in C)) {
      throw TypeError('It is not a typed array constructor!');
    }
    return new C(length);
  };
  var speciesFromList = function speciesFromList(O, list) {
    return fromList(speciesConstructor(O, O[DEF_CONSTRUCTOR]), list);
  };
  var fromList = function fromList(C, list) {
    var index = 0;
    var length = list.length;
    var result = allocate(C, length);
    while (length > index) {
      result[index] = list[index++];
    }
    return result;
  };
  var addGetter = function addGetter(it, key, internal) {
    dP(it, key, {
      get: function get() {
        return this._d[internal];
      }
    });
  };
  var $from = function from(source /* , mapfn, thisArg */) {
    var O = toObject(source);
    var aLen = arguments.length;
    var mapfn = aLen > 1 ? arguments[1] : undefined;
    var mapping = mapfn !== undefined;
    var iterFn = getIterFn(O);
    var i, length, values, result, step, iterator;
    if (iterFn != undefined && !isArrayIter(iterFn)) {
      for (iterator = iterFn.call(O), values = [], i = 0; !(step = iterator.next()).done; i++) {
        values.push(step.value);
      }
      O = values;
    }
    if (mapping && aLen > 2) mapfn = ctx(mapfn, arguments[2], 2);
    for (i = 0, length = toLength(O.length), result = allocate(this, length); length > i; i++) {
      result[i] = mapping ? mapfn(O[i], i) : O[i];
    }
    return result;
  };
  var $of = function of( /* ...items */
  ) {
    var index = 0;
    var length = arguments.length;
    var result = allocate(this, length);
    while (length > index) {
      result[index] = arguments[index++];
    }
    return result;
  };

  // iOS Safari 6.x fails here
  var TO_LOCALE_BUG = !!Uint8Array && fails(function () {
    arrayToLocaleString.call(new Uint8Array(1));
  });
  var $toLocaleString = function toLocaleString() {
    return arrayToLocaleString.apply(TO_LOCALE_BUG ? arraySlice.call(validate(this)) : validate(this), arguments);
  };
  var proto = {
    copyWithin: function copyWithin(target, start /* , end */) {
      return arrayCopyWithin.call(validate(this), target, start, arguments.length > 2 ? arguments[2] : undefined);
    },
    every: function every(callbackfn /* , thisArg */) {
      return arrayEvery(validate(this), callbackfn, arguments.length > 1 ? arguments[1] : undefined);
    },
    fill: function fill(value /* , start, end */) {
      // eslint-disable-line no-unused-vars
      return arrayFill.apply(validate(this), arguments);
    },
    filter: function filter(callbackfn /* , thisArg */) {
      return speciesFromList(this, arrayFilter(validate(this), callbackfn, arguments.length > 1 ? arguments[1] : undefined));
    },
    find: function find(predicate /* , thisArg */) {
      return arrayFind(validate(this), predicate, arguments.length > 1 ? arguments[1] : undefined);
    },
    findIndex: function findIndex(predicate /* , thisArg */) {
      return arrayFindIndex(validate(this), predicate, arguments.length > 1 ? arguments[1] : undefined);
    },
    forEach: function forEach(callbackfn /* , thisArg */) {
      arrayForEach(validate(this), callbackfn, arguments.length > 1 ? arguments[1] : undefined);
    },
    indexOf: function indexOf(searchElement /* , fromIndex */) {
      return arrayIndexOf(validate(this), searchElement, arguments.length > 1 ? arguments[1] : undefined);
    },
    includes: function includes(searchElement /* , fromIndex */) {
      return arrayIncludes(validate(this), searchElement, arguments.length > 1 ? arguments[1] : undefined);
    },
    join: function join(separator) {
      // eslint-disable-line no-unused-vars
      return arrayJoin.apply(validate(this), arguments);
    },
    lastIndexOf: function lastIndexOf(searchElement /* , fromIndex */) {
      // eslint-disable-line no-unused-vars
      return arrayLastIndexOf.apply(validate(this), arguments);
    },
    map: function map(mapfn /* , thisArg */) {
      return $map(validate(this), mapfn, arguments.length > 1 ? arguments[1] : undefined);
    },
    reduce: function reduce(callbackfn /* , initialValue */) {
      // eslint-disable-line no-unused-vars
      return arrayReduce.apply(validate(this), arguments);
    },
    reduceRight: function reduceRight(callbackfn /* , initialValue */) {
      // eslint-disable-line no-unused-vars
      return arrayReduceRight.apply(validate(this), arguments);
    },
    reverse: function reverse() {
      var that = this;
      var length = validate(that).length;
      var middle = Math.floor(length / 2);
      var index = 0;
      var value;
      while (index < middle) {
        value = that[index];
        that[index++] = that[--length];
        that[length] = value;
      }
      return that;
    },
    some: function some(callbackfn /* , thisArg */) {
      return arraySome(validate(this), callbackfn, arguments.length > 1 ? arguments[1] : undefined);
    },
    sort: function sort(comparefn) {
      return arraySort.call(validate(this), comparefn);
    },
    subarray: function subarray(begin, end) {
      var O = validate(this);
      var length = O.length;
      var $begin = toAbsoluteIndex(begin, length);
      return new (speciesConstructor(O, O[DEF_CONSTRUCTOR]))(O.buffer, O.byteOffset + $begin * O.BYTES_PER_ELEMENT, toLength((end === undefined ? length : toAbsoluteIndex(end, length)) - $begin));
    }
  };
  var $slice = function slice(start, end) {
    return speciesFromList(this, arraySlice.call(validate(this), start, end));
  };
  var $set = function set(arrayLike /* , offset */) {
    validate(this);
    var offset = toOffset(arguments[1], 1);
    var length = this.length;
    var src = toObject(arrayLike);
    var len = toLength(src.length);
    var index = 0;
    if (len + offset > length) throw RangeError(WRONG_LENGTH);
    while (index < len) {
      this[offset + index] = src[index++];
    }
  };
  var $iterators = {
    entries: function entries() {
      return arrayEntries.call(validate(this));
    },
    keys: function keys() {
      return arrayKeys.call(validate(this));
    },
    values: function values() {
      return arrayValues.call(validate(this));
    }
  };
  var isTAIndex = function isTAIndex(target, key) {
    return isObject(target) && target[TYPED_ARRAY] && _typeof(key) != 'symbol' && key in target && String(+key) == String(key);
  };
  var $getDesc = function getOwnPropertyDescriptor(target, key) {
    return isTAIndex(target, key = toPrimitive(key, true)) ? propertyDesc(2, target[key]) : gOPD(target, key);
  };
  var $setDesc = function defineProperty(target, key, desc) {
    if (isTAIndex(target, key = toPrimitive(key, true)) && isObject(desc) && has(desc, 'value') && !has(desc, 'get') && !has(desc, 'set')
    // TODO: add validation descriptor w/o calling accessors
    && !desc.configurable && (!has(desc, 'writable') || desc.writable) && (!has(desc, 'enumerable') || desc.enumerable)) {
      target[key] = desc.value;
      return target;
    }
    return dP(target, key, desc);
  };
  if (!ALL_CONSTRUCTORS) {
    $GOPD.f = $getDesc;
    $DP.f = $setDesc;
  }
  $export($export.S + $export.F * !ALL_CONSTRUCTORS, 'Object', {
    getOwnPropertyDescriptor: $getDesc,
    defineProperty: $setDesc
  });
  if (fails(function () {
    arrayToString.call({});
  })) {
    arrayToString = arrayToLocaleString = function toString() {
      return arrayJoin.call(this);
    };
  }
  var $TypedArrayPrototype$ = redefineAll({}, proto);
  redefineAll($TypedArrayPrototype$, $iterators);
  hide($TypedArrayPrototype$, ITERATOR, $iterators.values);
  redefineAll($TypedArrayPrototype$, {
    slice: $slice,
    set: $set,
    constructor: function constructor() {/* noop */},
    toString: arrayToString,
    toLocaleString: $toLocaleString
  });
  addGetter($TypedArrayPrototype$, 'buffer', 'b');
  addGetter($TypedArrayPrototype$, 'byteOffset', 'o');
  addGetter($TypedArrayPrototype$, 'byteLength', 'l');
  addGetter($TypedArrayPrototype$, 'length', 'e');
  dP($TypedArrayPrototype$, TAG, {
    get: function get() {
      return this[TYPED_ARRAY];
    }
  });

  // eslint-disable-next-line max-statements
  module.exports = function (KEY, BYTES, wrapper, CLAMPED) {
    CLAMPED = !!CLAMPED;
    var NAME = KEY + (CLAMPED ? 'Clamped' : '') + 'Array';
    var GETTER = 'get' + KEY;
    var SETTER = 'set' + KEY;
    var TypedArray = global[NAME];
    var Base = TypedArray || {};
    var TAC = TypedArray && getPrototypeOf(TypedArray);
    var FORCED = !TypedArray || !$typed.ABV;
    var O = {};
    var TypedArrayPrototype = TypedArray && TypedArray[PROTOTYPE];
    var getter = function getter(that, index) {
      var data = that._d;
      return data.v[GETTER](index * BYTES + data.o, LITTLE_ENDIAN);
    };
    var setter = function setter(that, index, value) {
      var data = that._d;
      if (CLAMPED) value = (value = Math.round(value)) < 0 ? 0 : value > 0xff ? 0xff : value & 0xff;
      data.v[SETTER](index * BYTES + data.o, value, LITTLE_ENDIAN);
    };
    var addElement = function addElement(that, index) {
      dP(that, index, {
        get: function get() {
          return getter(this, index);
        },
        set: function set(value) {
          return setter(this, index, value);
        },
        enumerable: true
      });
    };
    if (FORCED) {
      TypedArray = wrapper(function (that, data, $offset, $length) {
        anInstance(that, TypedArray, NAME, '_d');
        var index = 0;
        var offset = 0;
        var buffer, byteLength, length, klass;
        if (!isObject(data)) {
          length = toIndex(data);
          byteLength = length * BYTES;
          buffer = new $ArrayBuffer(byteLength);
        } else if (data instanceof $ArrayBuffer || (klass = classof(data)) == ARRAY_BUFFER || klass == SHARED_BUFFER) {
          buffer = data;
          offset = toOffset($offset, BYTES);
          var $len = data.byteLength;
          if ($length === undefined) {
            if ($len % BYTES) throw RangeError(WRONG_LENGTH);
            byteLength = $len - offset;
            if (byteLength < 0) throw RangeError(WRONG_LENGTH);
          } else {
            byteLength = toLength($length) * BYTES;
            if (byteLength + offset > $len) throw RangeError(WRONG_LENGTH);
          }
          length = byteLength / BYTES;
        } else if (TYPED_ARRAY in data) {
          return fromList(TypedArray, data);
        } else {
          return $from.call(TypedArray, data);
        }
        hide(that, '_d', {
          b: buffer,
          o: offset,
          l: byteLength,
          e: length,
          v: new $DataView(buffer)
        });
        while (index < length) {
          addElement(that, index++);
        }
      });
      TypedArrayPrototype = TypedArray[PROTOTYPE] = create($TypedArrayPrototype$);
      hide(TypedArrayPrototype, 'constructor', TypedArray);
    } else if (!fails(function () {
      TypedArray(1);
    }) || !fails(function () {
      new TypedArray(-1); // eslint-disable-line no-new
    }) || !$iterDetect(function (iter) {
      new TypedArray(); // eslint-disable-line no-new
      new TypedArray(null); // eslint-disable-line no-new
      new TypedArray(1.5); // eslint-disable-line no-new
      new TypedArray(iter); // eslint-disable-line no-new
    }, true)) {
      TypedArray = wrapper(function (that, data, $offset, $length) {
        anInstance(that, TypedArray, NAME);
        var klass;
        // `ws` module bug, temporarily remove validation length for Uint8Array
        // https://github.com/websockets/ws/pull/645
        if (!isObject(data)) return new Base(toIndex(data));
        if (data instanceof $ArrayBuffer || (klass = classof(data)) == ARRAY_BUFFER || klass == SHARED_BUFFER) {
          return $length !== undefined ? new Base(data, toOffset($offset, BYTES), $length) : $offset !== undefined ? new Base(data, toOffset($offset, BYTES)) : new Base(data);
        }
        if (TYPED_ARRAY in data) return fromList(TypedArray, data);
        return $from.call(TypedArray, data);
      });
      arrayForEach(TAC !== Function.prototype ? gOPN(Base).concat(gOPN(TAC)) : gOPN(Base), function (key) {
        if (!(key in TypedArray)) hide(TypedArray, key, Base[key]);
      });
      TypedArray[PROTOTYPE] = TypedArrayPrototype;
      if (!LIBRARY) TypedArrayPrototype.constructor = TypedArray;
    }
    var $nativeIterator = TypedArrayPrototype[ITERATOR];
    var CORRECT_ITER_NAME = !!$nativeIterator && ($nativeIterator.name == 'values' || $nativeIterator.name == undefined);
    var $iterator = $iterators.values;
    hide(TypedArray, TYPED_CONSTRUCTOR, true);
    hide(TypedArrayPrototype, TYPED_ARRAY, NAME);
    hide(TypedArrayPrototype, VIEW, true);
    hide(TypedArrayPrototype, DEF_CONSTRUCTOR, TypedArray);
    if (CLAMPED ? new TypedArray(1)[TAG] != NAME : !(TAG in TypedArrayPrototype)) {
      dP(TypedArrayPrototype, TAG, {
        get: function get() {
          return NAME;
        }
      });
    }
    O[NAME] = TypedArray;
    $export($export.G + $export.W + $export.F * (TypedArray != Base), O);
    $export($export.S, NAME, {
      BYTES_PER_ELEMENT: BYTES
    });
    $export($export.S + $export.F * fails(function () {
      Base.of.call(TypedArray, 1);
    }), NAME, {
      from: $from,
      of: $of
    });
    if (!(BYTES_PER_ELEMENT in TypedArrayPrototype)) hide(TypedArrayPrototype, BYTES_PER_ELEMENT, BYTES);
    $export($export.P, NAME, proto);
    setSpecies(NAME);
    $export($export.P + $export.F * FORCED_SET, NAME, {
      set: $set
    });
    $export($export.P + $export.F * !CORRECT_ITER_NAME, NAME, $iterators);
    if (!LIBRARY && TypedArrayPrototype.toString != arrayToString) TypedArrayPrototype.toString = arrayToString;
    $export($export.P + $export.F * fails(function () {
      new TypedArray(1).slice();
    }), NAME, {
      slice: $slice
    });
    $export($export.P + $export.F * (fails(function () {
      return [1, 2].toLocaleString() != new TypedArray([1, 2]).toLocaleString();
    }) || !fails(function () {
      TypedArrayPrototype.toLocaleString.call([1, 2]);
    })), NAME, {
      toLocaleString: $toLocaleString
    });
    Iterators[NAME] = CORRECT_ITER_NAME ? $nativeIterator : $iterator;
    if (!LIBRARY && !CORRECT_ITER_NAME) hide(TypedArrayPrototype, ITERATOR, $iterator);
  };
} else module.exports = function () {/* empty */};

/***/ }),

/***/ 9782:
/***/ ((__unused_webpack_module, exports, __webpack_require__) => {

"use strict";


var global = __webpack_require__(7381);
var DESCRIPTORS = __webpack_require__(4926);
var LIBRARY = __webpack_require__(4219);
var $typed = __webpack_require__(9161);
var hide = __webpack_require__(8012);
var redefineAll = __webpack_require__(7228);
var fails = __webpack_require__(5810);
var anInstance = __webpack_require__(2702);
var toInteger = __webpack_require__(3230);
var toLength = __webpack_require__(8315);
var toIndex = __webpack_require__(3472);
var gOPN = (__webpack_require__(2982).f);
var dP = (__webpack_require__(4835).f);
var arrayFill = __webpack_require__(1132);
var setToStringTag = __webpack_require__(8094);
var ARRAY_BUFFER = 'ArrayBuffer';
var DATA_VIEW = 'DataView';
var PROTOTYPE = 'prototype';
var WRONG_LENGTH = 'Wrong length!';
var WRONG_INDEX = 'Wrong index!';
var $ArrayBuffer = global[ARRAY_BUFFER];
var $DataView = global[DATA_VIEW];
var Math = global.Math;
var RangeError = global.RangeError;
// eslint-disable-next-line no-shadow-restricted-names
var Infinity = global.Infinity;
var BaseBuffer = $ArrayBuffer;
var abs = Math.abs;
var pow = Math.pow;
var floor = Math.floor;
var log = Math.log;
var LN2 = Math.LN2;
var BUFFER = 'buffer';
var BYTE_LENGTH = 'byteLength';
var BYTE_OFFSET = 'byteOffset';
var $BUFFER = DESCRIPTORS ? '_b' : BUFFER;
var $LENGTH = DESCRIPTORS ? '_l' : BYTE_LENGTH;
var $OFFSET = DESCRIPTORS ? '_o' : BYTE_OFFSET;

// IEEE754 conversions based on https://github.com/feross/ieee754
function packIEEE754(value, mLen, nBytes) {
  var buffer = new Array(nBytes);
  var eLen = nBytes * 8 - mLen - 1;
  var eMax = (1 << eLen) - 1;
  var eBias = eMax >> 1;
  var rt = mLen === 23 ? pow(2, -24) - pow(2, -77) : 0;
  var i = 0;
  var s = value < 0 || value === 0 && 1 / value < 0 ? 1 : 0;
  var e, m, c;
  value = abs(value);
  // eslint-disable-next-line no-self-compare
  if (value != value || value === Infinity) {
    // eslint-disable-next-line no-self-compare
    m = value != value ? 1 : 0;
    e = eMax;
  } else {
    e = floor(log(value) / LN2);
    if (value * (c = pow(2, -e)) < 1) {
      e--;
      c *= 2;
    }
    if (e + eBias >= 1) {
      value += rt / c;
    } else {
      value += rt * pow(2, 1 - eBias);
    }
    if (value * c >= 2) {
      e++;
      c /= 2;
    }
    if (e + eBias >= eMax) {
      m = 0;
      e = eMax;
    } else if (e + eBias >= 1) {
      m = (value * c - 1) * pow(2, mLen);
      e = e + eBias;
    } else {
      m = value * pow(2, eBias - 1) * pow(2, mLen);
      e = 0;
    }
  }
  for (; mLen >= 8; buffer[i++] = m & 255, m /= 256, mLen -= 8) {
    ;
  }
  e = e << mLen | m;
  eLen += mLen;
  for (; eLen > 0; buffer[i++] = e & 255, e /= 256, eLen -= 8) {
    ;
  }
  buffer[--i] |= s * 128;
  return buffer;
}
function unpackIEEE754(buffer, mLen, nBytes) {
  var eLen = nBytes * 8 - mLen - 1;
  var eMax = (1 << eLen) - 1;
  var eBias = eMax >> 1;
  var nBits = eLen - 7;
  var i = nBytes - 1;
  var s = buffer[i--];
  var e = s & 127;
  var m;
  s >>= 7;
  for (; nBits > 0; e = e * 256 + buffer[i], i--, nBits -= 8) {
    ;
  }
  m = e & (1 << -nBits) - 1;
  e >>= -nBits;
  nBits += mLen;
  for (; nBits > 0; m = m * 256 + buffer[i], i--, nBits -= 8) {
    ;
  }
  if (e === 0) {
    e = 1 - eBias;
  } else if (e === eMax) {
    return m ? NaN : s ? -Infinity : Infinity;
  } else {
    m = m + pow(2, mLen);
    e = e - eBias;
  }
  return (s ? -1 : 1) * m * pow(2, e - mLen);
}
function unpackI32(bytes) {
  return bytes[3] << 24 | bytes[2] << 16 | bytes[1] << 8 | bytes[0];
}
function packI8(it) {
  return [it & 0xff];
}
function packI16(it) {
  return [it & 0xff, it >> 8 & 0xff];
}
function packI32(it) {
  return [it & 0xff, it >> 8 & 0xff, it >> 16 & 0xff, it >> 24 & 0xff];
}
function packF64(it) {
  return packIEEE754(it, 52, 8);
}
function packF32(it) {
  return packIEEE754(it, 23, 4);
}
function addGetter(C, key, internal) {
  dP(C[PROTOTYPE], key, {
    get: function get() {
      return this[internal];
    }
  });
}
function get(view, bytes, index, isLittleEndian) {
  var numIndex = +index;
  var intIndex = toIndex(numIndex);
  if (intIndex + bytes > view[$LENGTH]) throw RangeError(WRONG_INDEX);
  var store = view[$BUFFER]._b;
  var start = intIndex + view[$OFFSET];
  var pack = store.slice(start, start + bytes);
  return isLittleEndian ? pack : pack.reverse();
}
function set(view, bytes, index, conversion, value, isLittleEndian) {
  var numIndex = +index;
  var intIndex = toIndex(numIndex);
  if (intIndex + bytes > view[$LENGTH]) throw RangeError(WRONG_INDEX);
  var store = view[$BUFFER]._b;
  var start = intIndex + view[$OFFSET];
  var pack = conversion(+value);
  for (var i = 0; i < bytes; i++) {
    store[start + i] = pack[isLittleEndian ? i : bytes - i - 1];
  }
}
if (!$typed.ABV) {
  $ArrayBuffer = function ArrayBuffer(length) {
    anInstance(this, $ArrayBuffer, ARRAY_BUFFER);
    var byteLength = toIndex(length);
    this._b = arrayFill.call(new Array(byteLength), 0);
    this[$LENGTH] = byteLength;
  };
  $DataView = function DataView(buffer, byteOffset, byteLength) {
    anInstance(this, $DataView, DATA_VIEW);
    anInstance(buffer, $ArrayBuffer, DATA_VIEW);
    var bufferLength = buffer[$LENGTH];
    var offset = toInteger(byteOffset);
    if (offset < 0 || offset > bufferLength) throw RangeError('Wrong offset!');
    byteLength = byteLength === undefined ? bufferLength - offset : toLength(byteLength);
    if (offset + byteLength > bufferLength) throw RangeError(WRONG_LENGTH);
    this[$BUFFER] = buffer;
    this[$OFFSET] = offset;
    this[$LENGTH] = byteLength;
  };
  if (DESCRIPTORS) {
    addGetter($ArrayBuffer, BYTE_LENGTH, '_l');
    addGetter($DataView, BUFFER, '_b');
    addGetter($DataView, BYTE_LENGTH, '_l');
    addGetter($DataView, BYTE_OFFSET, '_o');
  }
  redefineAll($DataView[PROTOTYPE], {
    getInt8: function getInt8(byteOffset) {
      return get(this, 1, byteOffset)[0] << 24 >> 24;
    },
    getUint8: function getUint8(byteOffset) {
      return get(this, 1, byteOffset)[0];
    },
    getInt16: function getInt16(byteOffset /* , littleEndian */) {
      var bytes = get(this, 2, byteOffset, arguments[1]);
      return (bytes[1] << 8 | bytes[0]) << 16 >> 16;
    },
    getUint16: function getUint16(byteOffset /* , littleEndian */) {
      var bytes = get(this, 2, byteOffset, arguments[1]);
      return bytes[1] << 8 | bytes[0];
    },
    getInt32: function getInt32(byteOffset /* , littleEndian */) {
      return unpackI32(get(this, 4, byteOffset, arguments[1]));
    },
    getUint32: function getUint32(byteOffset /* , littleEndian */) {
      return unpackI32(get(this, 4, byteOffset, arguments[1])) >>> 0;
    },
    getFloat32: function getFloat32(byteOffset /* , littleEndian */) {
      return unpackIEEE754(get(this, 4, byteOffset, arguments[1]), 23, 4);
    },
    getFloat64: function getFloat64(byteOffset /* , littleEndian */) {
      return unpackIEEE754(get(this, 8, byteOffset, arguments[1]), 52, 8);
    },
    setInt8: function setInt8(byteOffset, value) {
      set(this, 1, byteOffset, packI8, value);
    },
    setUint8: function setUint8(byteOffset, value) {
      set(this, 1, byteOffset, packI8, value);
    },
    setInt16: function setInt16(byteOffset, value /* , littleEndian */) {
      set(this, 2, byteOffset, packI16, value, arguments[2]);
    },
    setUint16: function setUint16(byteOffset, value /* , littleEndian */) {
      set(this, 2, byteOffset, packI16, value, arguments[2]);
    },
    setInt32: function setInt32(byteOffset, value /* , littleEndian */) {
      set(this, 4, byteOffset, packI32, value, arguments[2]);
    },
    setUint32: function setUint32(byteOffset, value /* , littleEndian */) {
      set(this, 4, byteOffset, packI32, value, arguments[2]);
    },
    setFloat32: function setFloat32(byteOffset, value /* , littleEndian */) {
      set(this, 4, byteOffset, packF32, value, arguments[2]);
    },
    setFloat64: function setFloat64(byteOffset, value /* , littleEndian */) {
      set(this, 8, byteOffset, packF64, value, arguments[2]);
    }
  });
} else {
  if (!fails(function () {
    $ArrayBuffer(1);
  }) || !fails(function () {
    new $ArrayBuffer(-1); // eslint-disable-line no-new
  }) || fails(function () {
    new $ArrayBuffer(); // eslint-disable-line no-new
    new $ArrayBuffer(1.5); // eslint-disable-line no-new
    new $ArrayBuffer(NaN); // eslint-disable-line no-new
    return $ArrayBuffer.name != ARRAY_BUFFER;
  })) {
    $ArrayBuffer = function ArrayBuffer(length) {
      anInstance(this, $ArrayBuffer);
      return new BaseBuffer(toIndex(length));
    };
    var ArrayBufferProto = $ArrayBuffer[PROTOTYPE] = BaseBuffer[PROTOTYPE];
    for (var keys = gOPN(BaseBuffer), j = 0, key; keys.length > j;) {
      if (!((key = keys[j++]) in $ArrayBuffer)) hide($ArrayBuffer, key, BaseBuffer[key]);
    }
    if (!LIBRARY) ArrayBufferProto.constructor = $ArrayBuffer;
  }
  // iOS Safari 7.x bug
  var view = new $DataView(new $ArrayBuffer(2));
  var $setInt8 = $DataView[PROTOTYPE].setInt8;
  view.setInt8(0, 2147483648);
  view.setInt8(1, 2147483649);
  if (view.getInt8(0) || !view.getInt8(1)) redefineAll($DataView[PROTOTYPE], {
    setInt8: function setInt8(byteOffset, value) {
      $setInt8.call(this, byteOffset, value << 24 >> 24);
    },
    setUint8: function setUint8(byteOffset, value) {
      $setInt8.call(this, byteOffset, value << 24 >> 24);
    }
  }, true);
}
setToStringTag($ArrayBuffer, ARRAY_BUFFER);
setToStringTag($DataView, DATA_VIEW);
hide($DataView[PROTOTYPE], $typed.VIEW, true);
exports[ARRAY_BUFFER] = $ArrayBuffer;
exports[DATA_VIEW] = $DataView;

/***/ }),

/***/ 9161:
/***/ ((module, __unused_webpack_exports, __webpack_require__) => {

var global = __webpack_require__(7381);
var hide = __webpack_require__(8012);
var uid = __webpack_require__(7936);
var TYPED = uid('typed_array');
var VIEW = uid('view');
var ABV = !!(global.ArrayBuffer && global.DataView);
var CONSTR = ABV;
var i = 0;
var l = 9;
var Typed;
var TypedArrayConstructors = 'Int8Array,Uint8Array,Uint8ClampedArray,Int16Array,Uint16Array,Int32Array,Uint32Array,Float32Array,Float64Array'.split(',');
while (i < l) {
  if (Typed = global[TypedArrayConstructors[i++]]) {
    hide(Typed.prototype, TYPED, true);
    hide(Typed.prototype, VIEW, true);
  } else CONSTR = false;
}
module.exports = {
  ABV: ABV,
  CONSTR: CONSTR,
  TYPED: TYPED,
  VIEW: VIEW
};

/***/ }),

/***/ 7936:
/***/ ((module) => {

var id = 0;
var px = Math.random();
module.exports = function (key) {
  return 'Symbol('.concat(key === undefined ? '' : key, ')_', (++id + px).toString(36));
};

/***/ }),

/***/ 851:
/***/ ((module, __unused_webpack_exports, __webpack_require__) => {

var global = __webpack_require__(7381);
var navigator = global.navigator;
module.exports = navigator && navigator.userAgent || '';

/***/ }),

/***/ 8546:
/***/ ((module, __unused_webpack_exports, __webpack_require__) => {

var isObject = __webpack_require__(7156);
module.exports = function (it, TYPE) {
  if (!isObject(it) || it._t !== TYPE) throw TypeError('Incompatible receiver, ' + TYPE + ' required!');
  return it;
};

/***/ }),

/***/ 5721:
/***/ ((module, __unused_webpack_exports, __webpack_require__) => {

var global = __webpack_require__(7381);
var core = __webpack_require__(8544);
var LIBRARY = __webpack_require__(4219);
var wksExt = __webpack_require__(9078);
var defineProperty = (__webpack_require__(4835).f);
module.exports = function (name) {
  var $Symbol = core.Symbol || (core.Symbol = LIBRARY ? {} : global.Symbol || {});
  if (name.charAt(0) != '_' && !(name in $Symbol)) defineProperty($Symbol, name, {
    value: wksExt.f(name)
  });
};

/***/ }),

/***/ 9078:
/***/ ((__unused_webpack_module, exports, __webpack_require__) => {

exports.f = __webpack_require__(3336);

/***/ }),

/***/ 3336:
/***/ ((module, __unused_webpack_exports, __webpack_require__) => {

var store = __webpack_require__(3192)('wks');
var uid = __webpack_require__(7936);
var _Symbol = (__webpack_require__(7381).Symbol);
var USE_SYMBOL = typeof _Symbol == 'function';
var $exports = module.exports = function (name) {
  return store[name] || (store[name] = USE_SYMBOL && _Symbol[name] || (USE_SYMBOL ? _Symbol : uid)('Symbol.' + name));
};
$exports.store = store;

/***/ }),

/***/ 7637:
/***/ ((module, __unused_webpack_exports, __webpack_require__) => {

var classof = __webpack_require__(2858);
var ITERATOR = __webpack_require__(3336)('iterator');
var Iterators = __webpack_require__(5301);
module.exports = (__webpack_require__(8544).getIteratorMethod) = function (it) {
  if (it != undefined) return it[ITERATOR] || it['@@iterator'] || Iterators[classof(it)];
};

/***/ }),

/***/ 9122:
/***/ ((__unused_webpack_module, __unused_webpack_exports, __webpack_require__) => {

// https://github.com/benjamingr/RexExp.escape
var $export = __webpack_require__(5913);
var $re = __webpack_require__(6813)(/[\\^$*+?.()|[\]{}]/g, '\\$&');
$export($export.S, 'RegExp', {
  escape: function escape(it) {
    return $re(it);
  }
});

/***/ }),

/***/ 4611:
/***/ ((__unused_webpack_module, __unused_webpack_exports, __webpack_require__) => {

// 22.1.3.3 Array.prototype.copyWithin(target, start, end = this.length)
var $export = __webpack_require__(5913);
$export($export.P, 'Array', {
  copyWithin: __webpack_require__(2147)
});
__webpack_require__(4339)('copyWithin');

/***/ }),

/***/ 9892:
/***/ ((__unused_webpack_module, __unused_webpack_exports, __webpack_require__) => {

"use strict";


var $export = __webpack_require__(5913);
var $every = __webpack_require__(3970)(4);
$export($export.P + $export.F * !__webpack_require__(1411)([].every, true), 'Array', {
  // 22.1.3.5 / 15.4.4.16 Array.prototype.every(callbackfn [, thisArg])
  every: function every(callbackfn /* , thisArg */) {
    return $every(this, callbackfn, arguments[1]);
  }
});

/***/ }),

/***/ 9217:
/***/ ((__unused_webpack_module, __unused_webpack_exports, __webpack_require__) => {

// 22.1.3.6 Array.prototype.fill(value, start = 0, end = this.length)
var $export = __webpack_require__(5913);
$export($export.P, 'Array', {
  fill: __webpack_require__(1132)
});
__webpack_require__(4339)('fill');

/***/ }),

/***/ 9355:
/***/ ((__unused_webpack_module, __unused_webpack_exports, __webpack_require__) => {

"use strict";


var $export = __webpack_require__(5913);
var $filter = __webpack_require__(3970)(2);
$export($export.P + $export.F * !__webpack_require__(1411)([].filter, true), 'Array', {
  // 22.1.3.7 / 15.4.4.20 Array.prototype.filter(callbackfn [, thisArg])
  filter: function filter(callbackfn /* , thisArg */) {
    return $filter(this, callbackfn, arguments[1]);
  }
});

/***/ }),

/***/ 109:
/***/ ((__unused_webpack_module, __unused_webpack_exports, __webpack_require__) => {

"use strict";


// 22.1.3.9 Array.prototype.findIndex(predicate, thisArg = undefined)
var $export = __webpack_require__(5913);
var $find = __webpack_require__(3970)(6);
var KEY = 'findIndex';
var forced = true;
// Shouldn't skip holes
if (KEY in []) Array(1)[KEY](function () {
  forced = false;
});
$export($export.P + $export.F * forced, 'Array', {
  findIndex: function findIndex(callbackfn /* , that = undefined */) {
    return $find(this, callbackfn, arguments.length > 1 ? arguments[1] : undefined);
  }
});
__webpack_require__(4339)(KEY);

/***/ }),

/***/ 4138:
/***/ ((__unused_webpack_module, __unused_webpack_exports, __webpack_require__) => {

"use strict";


// 22.1.3.8 Array.prototype.find(predicate, thisArg = undefined)
var $export = __webpack_require__(5913);
var $find = __webpack_require__(3970)(5);
var KEY = 'find';
var forced = true;
// Shouldn't skip holes
if (KEY in []) Array(1)[KEY](function () {
  forced = false;
});
$export($export.P + $export.F * forced, 'Array', {
  find: function find(callbackfn /* , that = undefined */) {
    return $find(this, callbackfn, arguments.length > 1 ? arguments[1] : undefined);
  }
});
__webpack_require__(4339)(KEY);

/***/ }),

/***/ 791:
/***/ ((__unused_webpack_module, __unused_webpack_exports, __webpack_require__) => {

"use strict";


var $export = __webpack_require__(5913);
var $forEach = __webpack_require__(3970)(0);
var STRICT = __webpack_require__(1411)([].forEach, true);
$export($export.P + $export.F * !STRICT, 'Array', {
  // 22.1.3.10 / 15.4.4.18 Array.prototype.forEach(callbackfn [, thisArg])
  forEach: function forEach(callbackfn /* , thisArg */) {
    return $forEach(this, callbackfn, arguments[1]);
  }
});

/***/ }),

/***/ 8671:
/***/ ((__unused_webpack_module, __unused_webpack_exports, __webpack_require__) => {

"use strict";


var ctx = __webpack_require__(566);
var $export = __webpack_require__(5913);
var toObject = __webpack_require__(2515);
var call = __webpack_require__(2471);
var isArrayIter = __webpack_require__(7063);
var toLength = __webpack_require__(8315);
var createProperty = __webpack_require__(1348);
var getIterFn = __webpack_require__(7637);
$export($export.S + $export.F * !__webpack_require__(5508)(function (iter) {
  Array.from(iter);
}), 'Array', {
  // 22.1.2.1 Array.from(arrayLike, mapfn = undefined, thisArg = undefined)
  from: function from(arrayLike /* , mapfn = undefined, thisArg = undefined */) {
    var O = toObject(arrayLike);
    var C = typeof this == 'function' ? this : Array;
    var aLen = arguments.length;
    var mapfn = aLen > 1 ? arguments[1] : undefined;
    var mapping = mapfn !== undefined;
    var index = 0;
    var iterFn = getIterFn(O);
    var length, result, step, iterator;
    if (mapping) mapfn = ctx(mapfn, aLen > 2 ? arguments[2] : undefined, 2);
    // if object isn't iterable or it's array with default iterator - use simple case
    if (iterFn != undefined && !(C == Array && isArrayIter(iterFn))) {
      for (iterator = iterFn.call(O), result = new C(); !(step = iterator.next()).done; index++) {
        createProperty(result, index, mapping ? call(iterator, mapfn, [step.value, index], true) : step.value);
      }
    } else {
      length = toLength(O.length);
      for (result = new C(length); length > index; index++) {
        createProperty(result, index, mapping ? mapfn(O[index], index) : O[index]);
      }
    }
    result.length = index;
    return result;
  }
});

/***/ }),

/***/ 4751:
/***/ ((__unused_webpack_module, __unused_webpack_exports, __webpack_require__) => {

"use strict";


var $export = __webpack_require__(5913);
var $indexOf = __webpack_require__(4687)(false);
var $native = [].indexOf;
var NEGATIVE_ZERO = !!$native && 1 / [1].indexOf(1, -0) < 0;
$export($export.P + $export.F * (NEGATIVE_ZERO || !__webpack_require__(1411)($native)), 'Array', {
  // 22.1.3.11 / 15.4.4.14 Array.prototype.indexOf(searchElement [, fromIndex])
  indexOf: function indexOf(searchElement /* , fromIndex = 0 */) {
    return NEGATIVE_ZERO
    // convert -0 to +0
    ? $native.apply(this, arguments) || 0 : $indexOf(this, searchElement, arguments[1]);
  }
});

/***/ }),

/***/ 1621:
/***/ ((__unused_webpack_module, __unused_webpack_exports, __webpack_require__) => {

// 22.1.2.2 / 15.4.3.2 Array.isArray(arg)
var $export = __webpack_require__(5913);
$export($export.S, 'Array', {
  isArray: __webpack_require__(1320)
});

/***/ }),

/***/ 4806:
/***/ ((module, __unused_webpack_exports, __webpack_require__) => {

"use strict";


var addToUnscopables = __webpack_require__(4339);
var step = __webpack_require__(7218);
var Iterators = __webpack_require__(5301);
var toIObject = __webpack_require__(8499);

// 22.1.3.4 Array.prototype.entries()
// 22.1.3.13 Array.prototype.keys()
// 22.1.3.29 Array.prototype.values()
// 22.1.3.30 Array.prototype[@@iterator]()
module.exports = __webpack_require__(4873)(Array, 'Array', function (iterated, kind) {
  this._t = toIObject(iterated); // target
  this._i = 0; // next index
  this._k = kind; // kind
  // 22.1.5.2.1 %ArrayIteratorPrototype%.next()
}, function () {
  var O = this._t;
  var kind = this._k;
  var index = this._i++;
  if (!O || index >= O.length) {
    this._t = undefined;
    return step(1);
  }
  if (kind == 'keys') return step(0, index);
  if (kind == 'values') return step(0, O[index]);
  return step(0, [index, O[index]]);
}, 'values');

// argumentsList[@@iterator] is %ArrayProto_values% (9.4.4.6, 9.4.4.7)
Iterators.Arguments = Iterators.Array;
addToUnscopables('keys');
addToUnscopables('values');
addToUnscopables('entries');

/***/ }),

/***/ 9437:
/***/ ((__unused_webpack_module, __unused_webpack_exports, __webpack_require__) => {

"use strict";


// 22.1.3.13 Array.prototype.join(separator)
var $export = __webpack_require__(5913);
var toIObject = __webpack_require__(8499);
var arrayJoin = [].join;

// fallback for not array-like strings
$export($export.P + $export.F * (__webpack_require__(331) != Object || !__webpack_require__(1411)(arrayJoin)), 'Array', {
  join: function join(separator) {
    return arrayJoin.call(toIObject(this), separator === undefined ? ',' : separator);
  }
});

/***/ }),

/***/ 9822:
/***/ ((__unused_webpack_module, __unused_webpack_exports, __webpack_require__) => {

"use strict";


var $export = __webpack_require__(5913);
var toIObject = __webpack_require__(8499);
var toInteger = __webpack_require__(3230);
var toLength = __webpack_require__(8315);
var $native = [].lastIndexOf;
var NEGATIVE_ZERO = !!$native && 1 / [1].lastIndexOf(1, -0) < 0;
$export($export.P + $export.F * (NEGATIVE_ZERO || !__webpack_require__(1411)($native)), 'Array', {
  // 22.1.3.14 / 15.4.4.15 Array.prototype.lastIndexOf(searchElement [, fromIndex])
  lastIndexOf: function lastIndexOf(searchElement /* , fromIndex = @[*-1] */) {
    // convert -0 to +0
    if (NEGATIVE_ZERO) return $native.apply(this, arguments) || 0;
    var O = toIObject(this);
    var length = toLength(O.length);
    var index = length - 1;
    if (arguments.length > 1) index = Math.min(index, toInteger(arguments[1]));
    if (index < 0) index = length + index;
    for (; index >= 0; index--) {
      if (index in O) if (O[index] === searchElement) return index || 0;
    }
    return -1;
  }
});

/***/ }),

/***/ 633:
/***/ ((__unused_webpack_module, __unused_webpack_exports, __webpack_require__) => {

"use strict";


var $export = __webpack_require__(5913);
var $map = __webpack_require__(3970)(1);
$export($export.P + $export.F * !__webpack_require__(1411)([].map, true), 'Array', {
  // 22.1.3.15 / 15.4.4.19 Array.prototype.map(callbackfn [, thisArg])
  map: function map(callbackfn /* , thisArg */) {
    return $map(this, callbackfn, arguments[1]);
  }
});

/***/ }),

/***/ 6705:
/***/ ((__unused_webpack_module, __unused_webpack_exports, __webpack_require__) => {

"use strict";


var $export = __webpack_require__(5913);
var createProperty = __webpack_require__(1348);

// WebKit Array.of isn't generic
$export($export.S + $export.F * __webpack_require__(5810)(function () {
  function F() {/* empty */}
  return !(Array.of.call(F) instanceof F);
}), 'Array', {
  // 22.1.2.3 Array.of( ...items)
  of: function of( /* ...args */
  ) {
    var index = 0;
    var aLen = arguments.length;
    var result = new (typeof this == 'function' ? this : Array)(aLen);
    while (aLen > index) {
      createProperty(result, index, arguments[index++]);
    }
    result.length = aLen;
    return result;
  }
});

/***/ }),

/***/ 8738:
/***/ ((__unused_webpack_module, __unused_webpack_exports, __webpack_require__) => {

"use strict";


var $export = __webpack_require__(5913);
var $reduce = __webpack_require__(6419);
$export($export.P + $export.F * !__webpack_require__(1411)([].reduceRight, true), 'Array', {
  // 22.1.3.19 / 15.4.4.22 Array.prototype.reduceRight(callbackfn [, initialValue])
  reduceRight: function reduceRight(callbackfn /* , initialValue */) {
    return $reduce(this, callbackfn, arguments.length, arguments[1], true);
  }
});

/***/ }),

/***/ 9121:
/***/ ((__unused_webpack_module, __unused_webpack_exports, __webpack_require__) => {

"use strict";


var $export = __webpack_require__(5913);
var $reduce = __webpack_require__(6419);
$export($export.P + $export.F * !__webpack_require__(1411)([].reduce, true), 'Array', {
  // 22.1.3.18 / 15.4.4.21 Array.prototype.reduce(callbackfn [, initialValue])
  reduce: function reduce(callbackfn /* , initialValue */) {
    return $reduce(this, callbackfn, arguments.length, arguments[1], false);
  }
});

/***/ }),

/***/ 7263:
/***/ ((__unused_webpack_module, __unused_webpack_exports, __webpack_require__) => {

"use strict";


var $export = __webpack_require__(5913);
var html = __webpack_require__(1225);
var cof = __webpack_require__(3679);
var toAbsoluteIndex = __webpack_require__(6241);
var toLength = __webpack_require__(8315);
var arraySlice = [].slice;

// fallback for not array-like ES3 strings and DOM objects
$export($export.P + $export.F * __webpack_require__(5810)(function () {
  if (html) arraySlice.call(html);
}), 'Array', {
  slice: function slice(begin, end) {
    var len = toLength(this.length);
    var klass = cof(this);
    end = end === undefined ? len : end;
    if (klass == 'Array') return arraySlice.call(this, begin, end);
    var start = toAbsoluteIndex(begin, len);
    var upTo = toAbsoluteIndex(end, len);
    var size = toLength(upTo - start);
    var cloned = new Array(size);
    var i = 0;
    for (; i < size; i++) {
      cloned[i] = klass == 'String' ? this.charAt(start + i) : this[start + i];
    }
    return cloned;
  }
});

/***/ }),

/***/ 9253:
/***/ ((__unused_webpack_module, __unused_webpack_exports, __webpack_require__) => {

"use strict";


var $export = __webpack_require__(5913);
var $some = __webpack_require__(3970)(3);
$export($export.P + $export.F * !__webpack_require__(1411)([].some, true), 'Array', {
  // 22.1.3.23 / 15.4.4.17 Array.prototype.some(callbackfn [, thisArg])
  some: function some(callbackfn /* , thisArg */) {
    return $some(this, callbackfn, arguments[1]);
  }
});

/***/ }),

/***/ 919:
/***/ ((__unused_webpack_module, __unused_webpack_exports, __webpack_require__) => {

"use strict";


var $export = __webpack_require__(5913);
var aFunction = __webpack_require__(6819);
var toObject = __webpack_require__(2515);
var fails = __webpack_require__(5810);
var $sort = [].sort;
var test = [1, 2, 3];
$export($export.P + $export.F * (fails(function () {
  // IE8-
  test.sort(undefined);
}) || !fails(function () {
  // V8 bug
  test.sort(null);
  // Old WebKit
}) || !__webpack_require__(1411)($sort)), 'Array', {
  // 22.1.3.25 Array.prototype.sort(comparefn)
  sort: function sort(comparefn) {
    return comparefn === undefined ? $sort.call(toObject(this)) : $sort.call(toObject(this), aFunction(comparefn));
  }
});

/***/ }),

/***/ 3821:
/***/ ((__unused_webpack_module, __unused_webpack_exports, __webpack_require__) => {

__webpack_require__(4798)('Array');

/***/ }),

/***/ 8384:
/***/ ((__unused_webpack_module, __unused_webpack_exports, __webpack_require__) => {

// 20.3.3.1 / 15.9.4.4 Date.now()
var $export = __webpack_require__(5913);
$export($export.S, 'Date', {
  now: function now() {
    return new Date().getTime();
  }
});

/***/ }),

/***/ 9701:
/***/ ((__unused_webpack_module, __unused_webpack_exports, __webpack_require__) => {

// 20.3.4.36 / 15.9.5.43 Date.prototype.toISOString()
var $export = __webpack_require__(5913);
var toISOString = __webpack_require__(2115);

// PhantomJS / old WebKit has a broken implementations
$export($export.P + $export.F * (Date.prototype.toISOString !== toISOString), 'Date', {
  toISOString: toISOString
});

/***/ }),

/***/ 2334:
/***/ ((__unused_webpack_module, __unused_webpack_exports, __webpack_require__) => {

"use strict";


var $export = __webpack_require__(5913);
var toObject = __webpack_require__(2515);
var toPrimitive = __webpack_require__(8537);
$export($export.P + $export.F * __webpack_require__(5810)(function () {
  return new Date(NaN).toJSON() !== null || Date.prototype.toJSON.call({
    toISOString: function toISOString() {
      return 1;
    }
  }) !== 1;
}), 'Date', {
  // eslint-disable-next-line no-unused-vars
  toJSON: function toJSON(key) {
    var O = toObject(this);
    var pv = toPrimitive(O);
    return typeof pv == 'number' && !isFinite(pv) ? null : O.toISOString();
  }
});

/***/ }),

/***/ 3233:
/***/ ((__unused_webpack_module, __unused_webpack_exports, __webpack_require__) => {

var TO_PRIMITIVE = __webpack_require__(3336)('toPrimitive');
var proto = Date.prototype;
if (!(TO_PRIMITIVE in proto)) __webpack_require__(8012)(proto, TO_PRIMITIVE, __webpack_require__(296));

/***/ }),

/***/ 1325:
/***/ ((__unused_webpack_module, __unused_webpack_exports, __webpack_require__) => {

var DateProto = Date.prototype;
var INVALID_DATE = 'Invalid Date';
var TO_STRING = 'toString';
var $toString = DateProto[TO_STRING];
var getTime = DateProto.getTime;
if (new Date(NaN) + '' != INVALID_DATE) {
  __webpack_require__(7278)(DateProto, TO_STRING, function toString() {
    var value = getTime.call(this);
    // eslint-disable-next-line no-self-compare
    return value === value ? $toString.call(this) : INVALID_DATE;
  });
}

/***/ }),

/***/ 161:
/***/ ((__unused_webpack_module, __unused_webpack_exports, __webpack_require__) => {

// 19.2.3.2 / 15.3.4.5 Function.prototype.bind(thisArg, args...)
var $export = __webpack_require__(5913);
$export($export.P, 'Function', {
  bind: __webpack_require__(8327)
});

/***/ }),

/***/ 15:
/***/ ((__unused_webpack_module, __unused_webpack_exports, __webpack_require__) => {

"use strict";


var isObject = __webpack_require__(7156);
var getPrototypeOf = __webpack_require__(4153);
var HAS_INSTANCE = __webpack_require__(3336)('hasInstance');
var FunctionProto = Function.prototype;
// 19.2.3.6 Function.prototype[@@hasInstance](V)
if (!(HAS_INSTANCE in FunctionProto)) (__webpack_require__(4835).f)(FunctionProto, HAS_INSTANCE, {
  value: function value(O) {
    if (typeof this != 'function' || !isObject(O)) return false;
    if (!isObject(this.prototype)) return O instanceof this;
    // for environment w/o native `@@hasInstance` logic enough `instanceof`, but add this:
    while (O = getPrototypeOf(O)) {
      if (this.prototype === O) return true;
    }
    return false;
  }
});

/***/ }),

/***/ 6042:
/***/ ((__unused_webpack_module, __unused_webpack_exports, __webpack_require__) => {

var dP = (__webpack_require__(4835).f);
var FProto = Function.prototype;
var nameRE = /^\s*function ([^ (]*)/;
var NAME = 'name';

// 19.2.4.2 name
NAME in FProto || __webpack_require__(4926) && dP(FProto, NAME, {
  configurable: true,
  get: function get() {
    try {
      return ('' + this).match(nameRE)[1];
    } catch (e) {
      return '';
    }
  }
});

/***/ }),

/***/ 8969:
/***/ ((module, __unused_webpack_exports, __webpack_require__) => {

"use strict";


var strong = __webpack_require__(4396);
var validate = __webpack_require__(8546);
var MAP = 'Map';

// 23.1 Map Objects
module.exports = __webpack_require__(1966)(MAP, function (get) {
  return function Map() {
    return get(this, arguments.length > 0 ? arguments[0] : undefined);
  };
}, {
  // 23.1.3.6 Map.prototype.get(key)
  get: function get(key) {
    var entry = strong.getEntry(validate(this, MAP), key);
    return entry && entry.v;
  },
  // 23.1.3.9 Map.prototype.set(key, value)
  set: function set(key, value) {
    return strong.def(validate(this, MAP), key === 0 ? 0 : key, value);
  }
}, strong, true);

/***/ }),

/***/ 4717:
/***/ ((__unused_webpack_module, __unused_webpack_exports, __webpack_require__) => {

// 20.2.2.3 Math.acosh(x)
var $export = __webpack_require__(5913);
var log1p = __webpack_require__(5447);
var sqrt = Math.sqrt;
var $acosh = Math.acosh;
$export($export.S + $export.F * !($acosh
// V8 bug: https://code.google.com/p/v8/issues/detail?id=3509
&& Math.floor($acosh(Number.MAX_VALUE)) == 710
// Tor Browser bug: Math.acosh(Infinity) -> NaN
&& $acosh(Infinity) == Infinity), 'Math', {
  acosh: function acosh(x) {
    return (x = +x) < 1 ? NaN : x > 94906265.62425156 ? Math.log(x) + Math.LN2 : log1p(x - 1 + sqrt(x - 1) * sqrt(x + 1));
  }
});

/***/ }),

/***/ 7292:
/***/ ((__unused_webpack_module, __unused_webpack_exports, __webpack_require__) => {

// 20.2.2.5 Math.asinh(x)
var $export = __webpack_require__(5913);
var $asinh = Math.asinh;
function asinh(x) {
  return !isFinite(x = +x) || x == 0 ? x : x < 0 ? -asinh(-x) : Math.log(x + Math.sqrt(x * x + 1));
}

// Tor Browser bug: Math.asinh(0) -> -0
$export($export.S + $export.F * !($asinh && 1 / $asinh(0) > 0), 'Math', {
  asinh: asinh
});

/***/ }),

/***/ 1840:
/***/ ((__unused_webpack_module, __unused_webpack_exports, __webpack_require__) => {

// 20.2.2.7 Math.atanh(x)
var $export = __webpack_require__(5913);
var $atanh = Math.atanh;

// Tor Browser bug: Math.atanh(-0) -> 0
$export($export.S + $export.F * !($atanh && 1 / $atanh(-0) < 0), 'Math', {
  atanh: function atanh(x) {
    return (x = +x) == 0 ? x : Math.log((1 + x) / (1 - x)) / 2;
  }
});

/***/ }),

/***/ 3255:
/***/ ((__unused_webpack_module, __unused_webpack_exports, __webpack_require__) => {

// 20.2.2.9 Math.cbrt(x)
var $export = __webpack_require__(5913);
var sign = __webpack_require__(4012);
$export($export.S, 'Math', {
  cbrt: function cbrt(x) {
    return sign(x = +x) * Math.pow(Math.abs(x), 1 / 3);
  }
});

/***/ }),

/***/ 5728:
/***/ ((__unused_webpack_module, __unused_webpack_exports, __webpack_require__) => {

// 20.2.2.11 Math.clz32(x)
var $export = __webpack_require__(5913);
$export($export.S, 'Math', {
  clz32: function clz32(x) {
    return (x >>>= 0) ? 31 - Math.floor(Math.log(x + 0.5) * Math.LOG2E) : 32;
  }
});

/***/ }),

/***/ 6255:
/***/ ((__unused_webpack_module, __unused_webpack_exports, __webpack_require__) => {

// 20.2.2.12 Math.cosh(x)
var $export = __webpack_require__(5913);
var exp = Math.exp;
$export($export.S, 'Math', {
  cosh: function cosh(x) {
    return (exp(x = +x) + exp(-x)) / 2;
  }
});

/***/ }),

/***/ 2834:
/***/ ((__unused_webpack_module, __unused_webpack_exports, __webpack_require__) => {

// 20.2.2.14 Math.expm1(x)
var $export = __webpack_require__(5913);
var $expm1 = __webpack_require__(4774);
$export($export.S + $export.F * ($expm1 != Math.expm1), 'Math', {
  expm1: $expm1
});

/***/ }),

/***/ 4489:
/***/ ((__unused_webpack_module, __unused_webpack_exports, __webpack_require__) => {

// 20.2.2.16 Math.fround(x)
var $export = __webpack_require__(5913);
$export($export.S, 'Math', {
  fround: __webpack_require__(3800)
});

/***/ }),

/***/ 575:
/***/ ((__unused_webpack_module, __unused_webpack_exports, __webpack_require__) => {

// 20.2.2.17 Math.hypot([value1[, value2[, … ]]])
var $export = __webpack_require__(5913);
var abs = Math.abs;
$export($export.S, 'Math', {
  hypot: function hypot(value1, value2) {
    // eslint-disable-line no-unused-vars
    var sum = 0;
    var i = 0;
    var aLen = arguments.length;
    var larg = 0;
    var arg, div;
    while (i < aLen) {
      arg = abs(arguments[i++]);
      if (larg < arg) {
        div = larg / arg;
        sum = sum * div * div + 1;
        larg = arg;
      } else if (arg > 0) {
        div = arg / larg;
        sum += div * div;
      } else sum += arg;
    }
    return larg === Infinity ? Infinity : larg * Math.sqrt(sum);
  }
});

/***/ }),

/***/ 1369:
/***/ ((__unused_webpack_module, __unused_webpack_exports, __webpack_require__) => {

// 20.2.2.18 Math.imul(x, y)
var $export = __webpack_require__(5913);
var $imul = Math.imul;

// some WebKit versions fails with big numbers, some has wrong arity
$export($export.S + $export.F * __webpack_require__(5810)(function () {
  return $imul(0xffffffff, 5) != -5 || $imul.length != 2;
}), 'Math', {
  imul: function imul(x, y) {
    var UINT16 = 0xffff;
    var xn = +x;
    var yn = +y;
    var xl = UINT16 & xn;
    var yl = UINT16 & yn;
    return 0 | xl * yl + ((UINT16 & xn >>> 16) * yl + xl * (UINT16 & yn >>> 16) << 16 >>> 0);
  }
});

/***/ }),

/***/ 2751:
/***/ ((__unused_webpack_module, __unused_webpack_exports, __webpack_require__) => {

// 20.2.2.21 Math.log10(x)
var $export = __webpack_require__(5913);
$export($export.S, 'Math', {
  log10: function log10(x) {
    return Math.log(x) * Math.LOG10E;
  }
});

/***/ }),

/***/ 9617:
/***/ ((__unused_webpack_module, __unused_webpack_exports, __webpack_require__) => {

// 20.2.2.20 Math.log1p(x)
var $export = __webpack_require__(5913);
$export($export.S, 'Math', {
  log1p: __webpack_require__(5447)
});

/***/ }),

/***/ 3656:
/***/ ((__unused_webpack_module, __unused_webpack_exports, __webpack_require__) => {

// 20.2.2.22 Math.log2(x)
var $export = __webpack_require__(5913);
$export($export.S, 'Math', {
  log2: function log2(x) {
    return Math.log(x) / Math.LN2;
  }
});

/***/ }),

/***/ 1850:
/***/ ((__unused_webpack_module, __unused_webpack_exports, __webpack_require__) => {

// 20.2.2.28 Math.sign(x)
var $export = __webpack_require__(5913);
$export($export.S, 'Math', {
  sign: __webpack_require__(4012)
});

/***/ }),

/***/ 5424:
/***/ ((__unused_webpack_module, __unused_webpack_exports, __webpack_require__) => {

// 20.2.2.30 Math.sinh(x)
var $export = __webpack_require__(5913);
var expm1 = __webpack_require__(4774);
var exp = Math.exp;

// V8 near Chromium 38 has a problem with very small numbers
$export($export.S + $export.F * __webpack_require__(5810)(function () {
  return !Math.sinh(-2e-17) != -2e-17;
}), 'Math', {
  sinh: function sinh(x) {
    return Math.abs(x = +x) < 1 ? (expm1(x) - expm1(-x)) / 2 : (exp(x - 1) - exp(-x - 1)) * (Math.E / 2);
  }
});

/***/ }),

/***/ 230:
/***/ ((__unused_webpack_module, __unused_webpack_exports, __webpack_require__) => {

// 20.2.2.33 Math.tanh(x)
var $export = __webpack_require__(5913);
var expm1 = __webpack_require__(4774);
var exp = Math.exp;
$export($export.S, 'Math', {
  tanh: function tanh(x) {
    var a = expm1(x = +x);
    var b = expm1(-x);
    return a == Infinity ? 1 : b == Infinity ? -1 : (a - b) / (exp(x) + exp(-x));
  }
});

/***/ }),

/***/ 8471:
/***/ ((__unused_webpack_module, __unused_webpack_exports, __webpack_require__) => {

// 20.2.2.34 Math.trunc(x)
var $export = __webpack_require__(5913);
$export($export.S, 'Math', {
  trunc: function trunc(it) {
    return (it > 0 ? Math.floor : Math.ceil)(it);
  }
});

/***/ }),

/***/ 440:
/***/ ((__unused_webpack_module, __unused_webpack_exports, __webpack_require__) => {

"use strict";


var global = __webpack_require__(7381);
var has = __webpack_require__(5389);
var cof = __webpack_require__(3679);
var inheritIfRequired = __webpack_require__(3654);
var toPrimitive = __webpack_require__(8537);
var fails = __webpack_require__(5810);
var gOPN = (__webpack_require__(2982).f);
var gOPD = (__webpack_require__(3299).f);
var dP = (__webpack_require__(4835).f);
var $trim = (__webpack_require__(618).trim);
var NUMBER = 'Number';
var $Number = global[NUMBER];
var Base = $Number;
var proto = $Number.prototype;
// Opera ~12 has broken Object#toString
var BROKEN_COF = cof(__webpack_require__(4275)(proto)) == NUMBER;
var TRIM = ('trim' in String.prototype);

// 7.1.3 ToNumber(argument)
var toNumber = function toNumber(argument) {
  var it = toPrimitive(argument, false);
  if (typeof it == 'string' && it.length > 2) {
    it = TRIM ? it.trim() : $trim(it, 3);
    var first = it.charCodeAt(0);
    var third, radix, maxCode;
    if (first === 43 || first === 45) {
      third = it.charCodeAt(2);
      if (third === 88 || third === 120) return NaN; // Number('+0x1') should be NaN, old V8 fix
    } else if (first === 48) {
      switch (it.charCodeAt(1)) {
        case 66:
        case 98:
          radix = 2;
          maxCode = 49;
          break;
        // fast equal /^0b[01]+$/i
        case 79:
        case 111:
          radix = 8;
          maxCode = 55;
          break;
        // fast equal /^0o[0-7]+$/i
        default:
          return +it;
      }
      for (var digits = it.slice(2), i = 0, l = digits.length, code; i < l; i++) {
        code = digits.charCodeAt(i);
        // parseInt parses a string to a first unavailable symbol
        // but ToNumber should return NaN if a string contains unavailable symbols
        if (code < 48 || code > maxCode) return NaN;
      }
      return parseInt(digits, radix);
    }
  }
  return +it;
};
if (!$Number(' 0o1') || !$Number('0b1') || $Number('+0x1')) {
  $Number = function Number(value) {
    var it = arguments.length < 1 ? 0 : value;
    var that = this;
    return that instanceof $Number
    // check on 1..constructor(foo) case
    && (BROKEN_COF ? fails(function () {
      proto.valueOf.call(that);
    }) : cof(that) != NUMBER) ? inheritIfRequired(new Base(toNumber(it)), that, $Number) : toNumber(it);
  };
  for (var keys = __webpack_require__(4926) ? gOPN(Base) : (
    // ES3:
    'MAX_VALUE,MIN_VALUE,NaN,NEGATIVE_INFINITY,POSITIVE_INFINITY,' +
    // ES6 (in case, if modules with ES6 Number statics required before):
    'EPSILON,isFinite,isInteger,isNaN,isSafeInteger,MAX_SAFE_INTEGER,' + 'MIN_SAFE_INTEGER,parseFloat,parseInt,isInteger').split(','), j = 0, key; keys.length > j; j++) {
    if (has(Base, key = keys[j]) && !has($Number, key)) {
      dP($Number, key, gOPD(Base, key));
    }
  }
  $Number.prototype = proto;
  proto.constructor = $Number;
  __webpack_require__(7278)(global, NUMBER, $Number);
}

/***/ }),

/***/ 1914:
/***/ ((__unused_webpack_module, __unused_webpack_exports, __webpack_require__) => {

// 20.1.2.1 Number.EPSILON
var $export = __webpack_require__(5913);
$export($export.S, 'Number', {
  EPSILON: Math.pow(2, -52)
});

/***/ }),

/***/ 4117:
/***/ ((__unused_webpack_module, __unused_webpack_exports, __webpack_require__) => {

// 20.1.2.2 Number.isFinite(number)
var $export = __webpack_require__(5913);
var _isFinite = (__webpack_require__(7381).isFinite);
$export($export.S, 'Number', {
  isFinite: function isFinite(it) {
    return typeof it == 'number' && _isFinite(it);
  }
});

/***/ }),

/***/ 9619:
/***/ ((__unused_webpack_module, __unused_webpack_exports, __webpack_require__) => {

// 20.1.2.3 Number.isInteger(number)
var $export = __webpack_require__(5913);
$export($export.S, 'Number', {
  isInteger: __webpack_require__(5127)
});

/***/ }),

/***/ 5849:
/***/ ((__unused_webpack_module, __unused_webpack_exports, __webpack_require__) => {

// 20.1.2.4 Number.isNaN(number)
var $export = __webpack_require__(5913);
$export($export.S, 'Number', {
  isNaN: function isNaN(number) {
    // eslint-disable-next-line no-self-compare
    return number != number;
  }
});

/***/ }),

/***/ 4750:
/***/ ((__unused_webpack_module, __unused_webpack_exports, __webpack_require__) => {

// 20.1.2.5 Number.isSafeInteger(number)
var $export = __webpack_require__(5913);
var isInteger = __webpack_require__(5127);
var abs = Math.abs;
$export($export.S, 'Number', {
  isSafeInteger: function isSafeInteger(number) {
    return isInteger(number) && abs(number) <= 0x1fffffffffffff;
  }
});

/***/ }),

/***/ 1550:
/***/ ((__unused_webpack_module, __unused_webpack_exports, __webpack_require__) => {

// 20.1.2.6 Number.MAX_SAFE_INTEGER
var $export = __webpack_require__(5913);
$export($export.S, 'Number', {
  MAX_SAFE_INTEGER: 0x1fffffffffffff
});

/***/ }),

/***/ 3529:
/***/ ((__unused_webpack_module, __unused_webpack_exports, __webpack_require__) => {

// 20.1.2.10 Number.MIN_SAFE_INTEGER
var $export = __webpack_require__(5913);
$export($export.S, 'Number', {
  MIN_SAFE_INTEGER: -0x1fffffffffffff
});

/***/ }),

/***/ 2791:
/***/ ((__unused_webpack_module, __unused_webpack_exports, __webpack_require__) => {

var $export = __webpack_require__(5913);
var $parseFloat = __webpack_require__(5031);
// 20.1.2.12 Number.parseFloat(string)
$export($export.S + $export.F * (Number.parseFloat != $parseFloat), 'Number', {
  parseFloat: $parseFloat
});

/***/ }),

/***/ 6831:
/***/ ((__unused_webpack_module, __unused_webpack_exports, __webpack_require__) => {

var $export = __webpack_require__(5913);
var $parseInt = __webpack_require__(6971);
// 20.1.2.13 Number.parseInt(string, radix)
$export($export.S + $export.F * (Number.parseInt != $parseInt), 'Number', {
  parseInt: $parseInt
});

/***/ }),

/***/ 1077:
/***/ ((__unused_webpack_module, __unused_webpack_exports, __webpack_require__) => {

"use strict";


var $export = __webpack_require__(5913);
var toInteger = __webpack_require__(3230);
var aNumberValue = __webpack_require__(9855);
var repeat = __webpack_require__(1924);
var $toFixed = 1.0.toFixed;
var floor = Math.floor;
var data = [0, 0, 0, 0, 0, 0];
var ERROR = 'Number.toFixed: incorrect invocation!';
var ZERO = '0';
var multiply = function multiply(n, c) {
  var i = -1;
  var c2 = c;
  while (++i < 6) {
    c2 += n * data[i];
    data[i] = c2 % 1e7;
    c2 = floor(c2 / 1e7);
  }
};
var divide = function divide(n) {
  var i = 6;
  var c = 0;
  while (--i >= 0) {
    c += data[i];
    data[i] = floor(c / n);
    c = c % n * 1e7;
  }
};
var numToString = function numToString() {
  var i = 6;
  var s = '';
  while (--i >= 0) {
    if (s !== '' || i === 0 || data[i] !== 0) {
      var t = String(data[i]);
      s = s === '' ? t : s + repeat.call(ZERO, 7 - t.length) + t;
    }
  }
  return s;
};
var pow = function pow(x, n, acc) {
  return n === 0 ? acc : n % 2 === 1 ? pow(x, n - 1, acc * x) : pow(x * x, n / 2, acc);
};
var log = function log(x) {
  var n = 0;
  var x2 = x;
  while (x2 >= 4096) {
    n += 12;
    x2 /= 4096;
  }
  while (x2 >= 2) {
    n += 1;
    x2 /= 2;
  }
  return n;
};
$export($export.P + $export.F * (!!$toFixed && (0.00008.toFixed(3) !== '0.000' || 0.9.toFixed(0) !== '1' || 1.255.toFixed(2) !== '1.25' || 1000000000000000128.0.toFixed(0) !== '1000000000000000128') || !__webpack_require__(5810)(function () {
  // V8 ~ Android 4.3-
  $toFixed.call({});
})), 'Number', {
  toFixed: function toFixed(fractionDigits) {
    var x = aNumberValue(this, ERROR);
    var f = toInteger(fractionDigits);
    var s = '';
    var m = ZERO;
    var e, z, j, k;
    if (f < 0 || f > 20) throw RangeError(ERROR);
    // eslint-disable-next-line no-self-compare
    if (x != x) return 'NaN';
    if (x <= -1e21 || x >= 1e21) return String(x);
    if (x < 0) {
      s = '-';
      x = -x;
    }
    if (x > 1e-21) {
      e = log(x * pow(2, 69, 1)) - 69;
      z = e < 0 ? x * pow(2, -e, 1) : x / pow(2, e, 1);
      z *= 0x10000000000000;
      e = 52 - e;
      if (e > 0) {
        multiply(0, z);
        j = f;
        while (j >= 7) {
          multiply(1e7, 0);
          j -= 7;
        }
        multiply(pow(10, j, 1), 0);
        j = e - 1;
        while (j >= 23) {
          divide(1 << 23);
          j -= 23;
        }
        divide(1 << j);
        multiply(1, 1);
        divide(2);
        m = numToString();
      } else {
        multiply(0, z);
        multiply(1 << -e, 0);
        m = numToString() + repeat.call(ZERO, f);
      }
    }
    if (f > 0) {
      k = m.length;
      m = s + (k <= f ? '0.' + repeat.call(ZERO, f - k) + m : m.slice(0, k - f) + '.' + m.slice(k - f));
    } else {
      m = s + m;
    }
    return m;
  }
});

/***/ }),

/***/ 820:
/***/ ((__unused_webpack_module, __unused_webpack_exports, __webpack_require__) => {

"use strict";


var $export = __webpack_require__(5913);
var $fails = __webpack_require__(5810);
var aNumberValue = __webpack_require__(9855);
var $toPrecision = 1.0.toPrecision;
$export($export.P + $export.F * ($fails(function () {
  // IE7-
  return $toPrecision.call(1, undefined) !== '1';
}) || !$fails(function () {
  // V8 ~ Android 4.3-
  $toPrecision.call({});
})), 'Number', {
  toPrecision: function toPrecision(precision) {
    var that = aNumberValue(this, 'Number#toPrecision: incorrect invocation!');
    return precision === undefined ? $toPrecision.call(that) : $toPrecision.call(that, precision);
  }
});

/***/ }),

/***/ 5331:
/***/ ((__unused_webpack_module, __unused_webpack_exports, __webpack_require__) => {

// 19.1.3.1 Object.assign(target, source)
var $export = __webpack_require__(5913);
$export($export.S + $export.F, 'Object', {
  assign: __webpack_require__(8559)
});

/***/ }),

/***/ 3290:
/***/ ((__unused_webpack_module, __unused_webpack_exports, __webpack_require__) => {

var $export = __webpack_require__(5913);
// 19.1.2.2 / 15.2.3.5 Object.create(O [, Properties])
$export($export.S, 'Object', {
  create: __webpack_require__(4275)
});

/***/ }),

/***/ 8424:
/***/ ((__unused_webpack_module, __unused_webpack_exports, __webpack_require__) => {

var $export = __webpack_require__(5913);
// 19.1.2.3 / 15.2.3.7 Object.defineProperties(O, Properties)
$export($export.S + $export.F * !__webpack_require__(4926), 'Object', {
  defineProperties: __webpack_require__(6447)
});

/***/ }),

/***/ 3690:
/***/ ((__unused_webpack_module, __unused_webpack_exports, __webpack_require__) => {

var $export = __webpack_require__(5913);
// 19.1.2.4 / 15.2.3.6 Object.defineProperty(O, P, Attributes)
$export($export.S + $export.F * !__webpack_require__(4926), 'Object', {
  defineProperty: (__webpack_require__(4835).f)
});

/***/ }),

/***/ 754:
/***/ ((__unused_webpack_module, __unused_webpack_exports, __webpack_require__) => {

// 19.1.2.5 Object.freeze(O)
var isObject = __webpack_require__(7156);
var meta = (__webpack_require__(3763).onFreeze);
__webpack_require__(4057)('freeze', function ($freeze) {
  return function freeze(it) {
    return $freeze && isObject(it) ? $freeze(meta(it)) : it;
  };
});

/***/ }),

/***/ 2357:
/***/ ((__unused_webpack_module, __unused_webpack_exports, __webpack_require__) => {

// 19.1.2.6 Object.getOwnPropertyDescriptor(O, P)
var toIObject = __webpack_require__(8499);
var $getOwnPropertyDescriptor = (__webpack_require__(3299).f);
__webpack_require__(4057)('getOwnPropertyDescriptor', function () {
  return function getOwnPropertyDescriptor(it, key) {
    return $getOwnPropertyDescriptor(toIObject(it), key);
  };
});

/***/ }),

/***/ 6022:
/***/ ((__unused_webpack_module, __unused_webpack_exports, __webpack_require__) => {

// 19.1.2.7 Object.getOwnPropertyNames(O)
__webpack_require__(4057)('getOwnPropertyNames', function () {
  return (__webpack_require__(3136).f);
});

/***/ }),

/***/ 6667:
/***/ ((__unused_webpack_module, __unused_webpack_exports, __webpack_require__) => {

// 19.1.2.9 Object.getPrototypeOf(O)
var toObject = __webpack_require__(2515);
var $getPrototypeOf = __webpack_require__(4153);
__webpack_require__(4057)('getPrototypeOf', function () {
  return function getPrototypeOf(it) {
    return $getPrototypeOf(toObject(it));
  };
});

/***/ }),

/***/ 4919:
/***/ ((__unused_webpack_module, __unused_webpack_exports, __webpack_require__) => {

// 19.1.2.11 Object.isExtensible(O)
var isObject = __webpack_require__(7156);
__webpack_require__(4057)('isExtensible', function ($isExtensible) {
  return function isExtensible(it) {
    return isObject(it) ? $isExtensible ? $isExtensible(it) : true : false;
  };
});

/***/ }),

/***/ 9219:
/***/ ((__unused_webpack_module, __unused_webpack_exports, __webpack_require__) => {

// 19.1.2.12 Object.isFrozen(O)
var isObject = __webpack_require__(7156);
__webpack_require__(4057)('isFrozen', function ($isFrozen) {
  return function isFrozen(it) {
    return isObject(it) ? $isFrozen ? $isFrozen(it) : false : true;
  };
});

/***/ }),

/***/ 3270:
/***/ ((__unused_webpack_module, __unused_webpack_exports, __webpack_require__) => {

// 19.1.2.13 Object.isSealed(O)
var isObject = __webpack_require__(7156);
__webpack_require__(4057)('isSealed', function ($isSealed) {
  return function isSealed(it) {
    return isObject(it) ? $isSealed ? $isSealed(it) : false : true;
  };
});

/***/ }),

/***/ 2456:
/***/ ((__unused_webpack_module, __unused_webpack_exports, __webpack_require__) => {

// 19.1.3.10 Object.is(value1, value2)
var $export = __webpack_require__(5913);
$export($export.S, 'Object', {
  is: __webpack_require__(4261)
});

/***/ }),

/***/ 2506:
/***/ ((__unused_webpack_module, __unused_webpack_exports, __webpack_require__) => {

// 19.1.2.14 Object.keys(O)
var toObject = __webpack_require__(2515);
var $keys = __webpack_require__(9924);
__webpack_require__(4057)('keys', function () {
  return function keys(it) {
    return $keys(toObject(it));
  };
});

/***/ }),

/***/ 6527:
/***/ ((__unused_webpack_module, __unused_webpack_exports, __webpack_require__) => {

// 19.1.2.15 Object.preventExtensions(O)
var isObject = __webpack_require__(7156);
var meta = (__webpack_require__(3763).onFreeze);
__webpack_require__(4057)('preventExtensions', function ($preventExtensions) {
  return function preventExtensions(it) {
    return $preventExtensions && isObject(it) ? $preventExtensions(meta(it)) : it;
  };
});

/***/ }),

/***/ 7571:
/***/ ((__unused_webpack_module, __unused_webpack_exports, __webpack_require__) => {

// 19.1.2.17 Object.seal(O)
var isObject = __webpack_require__(7156);
var meta = (__webpack_require__(3763).onFreeze);
__webpack_require__(4057)('seal', function ($seal) {
  return function seal(it) {
    return $seal && isObject(it) ? $seal(meta(it)) : it;
  };
});

/***/ }),

/***/ 8490:
/***/ ((__unused_webpack_module, __unused_webpack_exports, __webpack_require__) => {

// 19.1.3.19 Object.setPrototypeOf(O, proto)
var $export = __webpack_require__(5913);
$export($export.S, 'Object', {
  setPrototypeOf: (__webpack_require__(6931).set)
});

/***/ }),

/***/ 4554:
/***/ ((__unused_webpack_module, __unused_webpack_exports, __webpack_require__) => {

"use strict";


// 19.1.3.6 Object.prototype.toString()
var classof = __webpack_require__(2858);
var test = {};
test[__webpack_require__(3336)('toStringTag')] = 'z';
if (test + '' != '[object z]') {
  __webpack_require__(7278)(Object.prototype, 'toString', function toString() {
    return '[object ' + classof(this) + ']';
  }, true);
}

/***/ }),

/***/ 3271:
/***/ ((__unused_webpack_module, __unused_webpack_exports, __webpack_require__) => {

var $export = __webpack_require__(5913);
var $parseFloat = __webpack_require__(5031);
// 18.2.4 parseFloat(string)
$export($export.G + $export.F * (parseFloat != $parseFloat), {
  parseFloat: $parseFloat
});

/***/ }),

/***/ 317:
/***/ ((__unused_webpack_module, __unused_webpack_exports, __webpack_require__) => {

var $export = __webpack_require__(5913);
var $parseInt = __webpack_require__(6971);
// 18.2.5 parseInt(string, radix)
$export($export.G + $export.F * (parseInt != $parseInt), {
  parseInt: $parseInt
});

/***/ }),

/***/ 829:
/***/ ((__unused_webpack_module, __unused_webpack_exports, __webpack_require__) => {

"use strict";


var LIBRARY = __webpack_require__(4219);
var global = __webpack_require__(7381);
var ctx = __webpack_require__(566);
var classof = __webpack_require__(2858);
var $export = __webpack_require__(5913);
var isObject = __webpack_require__(7156);
var aFunction = __webpack_require__(6819);
var anInstance = __webpack_require__(2702);
var forOf = __webpack_require__(2734);
var speciesConstructor = __webpack_require__(2035);
var task = (__webpack_require__(8220).set);
var microtask = __webpack_require__(1842)();
var newPromiseCapabilityModule = __webpack_require__(4086);
var perform = __webpack_require__(8228);
var userAgent = __webpack_require__(851);
var promiseResolve = __webpack_require__(3507);
var PROMISE = 'Promise';
var TypeError = global.TypeError;
var process = global.process;
var versions = process && process.versions;
var v8 = versions && versions.v8 || '';
var $Promise = global[PROMISE];
var isNode = classof(process) == 'process';
var empty = function empty() {/* empty */};
var Internal, newGenericPromiseCapability, OwnPromiseCapability, Wrapper;
var newPromiseCapability = newGenericPromiseCapability = newPromiseCapabilityModule.f;
var USE_NATIVE = !!function () {
  try {
    // correct subclassing with @@species support
    var promise = $Promise.resolve(1);
    var FakePromise = (promise.constructor = {})[__webpack_require__(3336)('species')] = function (exec) {
      exec(empty, empty);
    };
    // unhandled rejections tracking support, NodeJS Promise without it fails @@species test
    return (isNode || typeof PromiseRejectionEvent == 'function') && promise.then(empty) instanceof FakePromise
    // v8 6.6 (Node 10 and Chrome 66) have a bug with resolving custom thenables
    // https://bugs.chromium.org/p/chromium/issues/detail?id=830565
    // we can't detect it synchronously, so just check versions
    && v8.indexOf('6.6') !== 0 && userAgent.indexOf('Chrome/66') === -1;
  } catch (e) {/* empty */}
}();

// helpers
var isThenable = function isThenable(it) {
  var then;
  return isObject(it) && typeof (then = it.then) == 'function' ? then : false;
};
var notify = function notify(promise, isReject) {
  if (promise._n) return;
  promise._n = true;
  var chain = promise._c;
  microtask(function () {
    var value = promise._v;
    var ok = promise._s == 1;
    var i = 0;
    var run = function run(reaction) {
      var handler = ok ? reaction.ok : reaction.fail;
      var resolve = reaction.resolve;
      var reject = reaction.reject;
      var domain = reaction.domain;
      var result, then, exited;
      try {
        if (handler) {
          if (!ok) {
            if (promise._h == 2) onHandleUnhandled(promise);
            promise._h = 1;
          }
          if (handler === true) result = value;else {
            if (domain) domain.enter();
            result = handler(value); // may throw
            if (domain) {
              domain.exit();
              exited = true;
            }
          }
          if (result === reaction.promise) {
            reject(TypeError('Promise-chain cycle'));
          } else if (then = isThenable(result)) {
            then.call(result, resolve, reject);
          } else resolve(result);
        } else reject(value);
      } catch (e) {
        if (domain && !exited) domain.exit();
        reject(e);
      }
    };
    while (chain.length > i) {
      run(chain[i++]);
    } // variable length - can't use forEach
    promise._c = [];
    promise._n = false;
    if (isReject && !promise._h) onUnhandled(promise);
  });
};
var onUnhandled = function onUnhandled(promise) {
  task.call(global, function () {
    var value = promise._v;
    var unhandled = isUnhandled(promise);
    var result, handler, console;
    if (unhandled) {
      result = perform(function () {
        if (isNode) {
          process.emit('unhandledRejection', value, promise);
        } else if (handler = global.onunhandledrejection) {
          handler({
            promise: promise,
            reason: value
          });
        } else if ((console = global.console) && console.error) {
          console.error('Unhandled promise rejection', value);
        }
      });
      // Browsers should not trigger `rejectionHandled` event if it was handled here, NodeJS - should
      promise._h = isNode || isUnhandled(promise) ? 2 : 1;
    }
    promise._a = undefined;
    if (unhandled && result.e) throw result.v;
  });
};
var isUnhandled = function isUnhandled(promise) {
  return promise._h !== 1 && (promise._a || promise._c).length === 0;
};
var onHandleUnhandled = function onHandleUnhandled(promise) {
  task.call(global, function () {
    var handler;
    if (isNode) {
      process.emit('rejectionHandled', promise);
    } else if (handler = global.onrejectionhandled) {
      handler({
        promise: promise,
        reason: promise._v
      });
    }
  });
};
var $reject = function $reject(value) {
  var promise = this;
  if (promise._d) return;
  promise._d = true;
  promise = promise._w || promise; // unwrap
  promise._v = value;
  promise._s = 2;
  if (!promise._a) promise._a = promise._c.slice();
  notify(promise, true);
};
var $resolve = function $resolve(value) {
  var promise = this;
  var then;
  if (promise._d) return;
  promise._d = true;
  promise = promise._w || promise; // unwrap
  try {
    if (promise === value) throw TypeError("Promise can't be resolved itself");
    if (then = isThenable(value)) {
      microtask(function () {
        var wrapper = {
          _w: promise,
          _d: false
        }; // wrap
        try {
          then.call(value, ctx($resolve, wrapper, 1), ctx($reject, wrapper, 1));
        } catch (e) {
          $reject.call(wrapper, e);
        }
      });
    } else {
      promise._v = value;
      promise._s = 1;
      notify(promise, false);
    }
  } catch (e) {
    $reject.call({
      _w: promise,
      _d: false
    }, e); // wrap
  }
};

// constructor polyfill
if (!USE_NATIVE) {
  // 25.4.3.1 Promise(executor)
  $Promise = function Promise(executor) {
    anInstance(this, $Promise, PROMISE, '_h');
    aFunction(executor);
    Internal.call(this);
    try {
      executor(ctx($resolve, this, 1), ctx($reject, this, 1));
    } catch (err) {
      $reject.call(this, err);
    }
  };
  // eslint-disable-next-line no-unused-vars
  Internal = function Promise(executor) {
    this._c = []; // <- awaiting reactions
    this._a = undefined; // <- checked in isUnhandled reactions
    this._s = 0; // <- state
    this._d = false; // <- done
    this._v = undefined; // <- value
    this._h = 0; // <- rejection state, 0 - default, 1 - handled, 2 - unhandled
    this._n = false; // <- notify
  };

  Internal.prototype = __webpack_require__(7228)($Promise.prototype, {
    // 25.4.5.3 Promise.prototype.then(onFulfilled, onRejected)
    then: function then(onFulfilled, onRejected) {
      var reaction = newPromiseCapability(speciesConstructor(this, $Promise));
      reaction.ok = typeof onFulfilled == 'function' ? onFulfilled : true;
      reaction.fail = typeof onRejected == 'function' && onRejected;
      reaction.domain = isNode ? process.domain : undefined;
      this._c.push(reaction);
      if (this._a) this._a.push(reaction);
      if (this._s) notify(this, false);
      return reaction.promise;
    },
    // 25.4.5.1 Promise.prototype.catch(onRejected)
    'catch': function _catch(onRejected) {
      return this.then(undefined, onRejected);
    }
  });
  OwnPromiseCapability = function OwnPromiseCapability() {
    var promise = new Internal();
    this.promise = promise;
    this.resolve = ctx($resolve, promise, 1);
    this.reject = ctx($reject, promise, 1);
  };
  newPromiseCapabilityModule.f = newPromiseCapability = function newPromiseCapability(C) {
    return C === $Promise || C === Wrapper ? new OwnPromiseCapability(C) : newGenericPromiseCapability(C);
  };
}
$export($export.G + $export.W + $export.F * !USE_NATIVE, {
  Promise: $Promise
});
__webpack_require__(8094)($Promise, PROMISE);
__webpack_require__(4798)(PROMISE);
Wrapper = __webpack_require__(8544)[PROMISE];

// statics
$export($export.S + $export.F * !USE_NATIVE, PROMISE, {
  // 25.4.4.5 Promise.reject(r)
  reject: function reject(r) {
    var capability = newPromiseCapability(this);
    var $$reject = capability.reject;
    $$reject(r);
    return capability.promise;
  }
});
$export($export.S + $export.F * (LIBRARY || !USE_NATIVE), PROMISE, {
  // 25.4.4.6 Promise.resolve(x)
  resolve: function resolve(x) {
    return promiseResolve(LIBRARY && this === Wrapper ? $Promise : this, x);
  }
});
$export($export.S + $export.F * !(USE_NATIVE && __webpack_require__(5508)(function (iter) {
  $Promise.all(iter)['catch'](empty);
})), PROMISE, {
  // 25.4.4.1 Promise.all(iterable)
  all: function all(iterable) {
    var C = this;
    var capability = newPromiseCapability(C);
    var resolve = capability.resolve;
    var reject = capability.reject;
    var result = perform(function () {
      var values = [];
      var index = 0;
      var remaining = 1;
      forOf(iterable, false, function (promise) {
        var $index = index++;
        var alreadyCalled = false;
        values.push(undefined);
        remaining++;
        C.resolve(promise).then(function (value) {
          if (alreadyCalled) return;
          alreadyCalled = true;
          values[$index] = value;
          --remaining || resolve(values);
        }, reject);
      });
      --remaining || resolve(values);
    });
    if (result.e) reject(result.v);
    return capability.promise;
  },
  // 25.4.4.4 Promise.race(iterable)
  race: function race(iterable) {
    var C = this;
    var capability = newPromiseCapability(C);
    var reject = capability.reject;
    var result = perform(function () {
      forOf(iterable, false, function (promise) {
        C.resolve(promise).then(capability.resolve, reject);
      });
    });
    if (result.e) reject(result.v);
    return capability.promise;
  }
});

/***/ }),

/***/ 1220:
/***/ ((__unused_webpack_module, __unused_webpack_exports, __webpack_require__) => {

// 26.1.1 Reflect.apply(target, thisArgument, argumentsList)
var $export = __webpack_require__(5913);
var aFunction = __webpack_require__(6819);
var anObject = __webpack_require__(6154);
var rApply = ((__webpack_require__(7381).Reflect) || {}).apply;
var fApply = Function.apply;
// MS Edge argumentsList argument is optional
$export($export.S + $export.F * !__webpack_require__(5810)(function () {
  rApply(function () {/* empty */});
}), 'Reflect', {
  apply: function apply(target, thisArgument, argumentsList) {
    var T = aFunction(target);
    var L = anObject(argumentsList);
    return rApply ? rApply(T, thisArgument, L) : fApply.call(T, thisArgument, L);
  }
});

/***/ }),

/***/ 9263:
/***/ ((__unused_webpack_module, __unused_webpack_exports, __webpack_require__) => {

// 26.1.2 Reflect.construct(target, argumentsList [, newTarget])
var $export = __webpack_require__(5913);
var create = __webpack_require__(4275);
var aFunction = __webpack_require__(6819);
var anObject = __webpack_require__(6154);
var isObject = __webpack_require__(7156);
var fails = __webpack_require__(5810);
var bind = __webpack_require__(8327);
var rConstruct = ((__webpack_require__(7381).Reflect) || {}).construct;

// MS Edge supports only 2 arguments and argumentsList argument is optional
// FF Nightly sets third argument as `new.target`, but does not create `this` from it
var NEW_TARGET_BUG = fails(function () {
  function F() {/* empty */}
  return !(rConstruct(function () {/* empty */}, [], F) instanceof F);
});
var ARGS_BUG = !fails(function () {
  rConstruct(function () {/* empty */});
});
$export($export.S + $export.F * (NEW_TARGET_BUG || ARGS_BUG), 'Reflect', {
  construct: function construct(Target, args /* , newTarget */) {
    aFunction(Target);
    anObject(args);
    var newTarget = arguments.length < 3 ? Target : aFunction(arguments[2]);
    if (ARGS_BUG && !NEW_TARGET_BUG) return rConstruct(Target, args, newTarget);
    if (Target == newTarget) {
      // w/o altered newTarget, optimization for 0-4 arguments
      switch (args.length) {
        case 0:
          return new Target();
        case 1:
          return new Target(args[0]);
        case 2:
          return new Target(args[0], args[1]);
        case 3:
          return new Target(args[0], args[1], args[2]);
        case 4:
          return new Target(args[0], args[1], args[2], args[3]);
      }
      // w/o altered newTarget, lot of arguments case
      var $args = [null];
      $args.push.apply($args, args);
      return new (bind.apply(Target, $args))();
    }
    // with altered newTarget, not support built-in constructors
    var proto = newTarget.prototype;
    var instance = create(isObject(proto) ? proto : Object.prototype);
    var result = Function.apply.call(Target, instance, args);
    return isObject(result) ? result : instance;
  }
});

/***/ }),

/***/ 7622:
/***/ ((__unused_webpack_module, __unused_webpack_exports, __webpack_require__) => {

// 26.1.3 Reflect.defineProperty(target, propertyKey, attributes)
var dP = __webpack_require__(4835);
var $export = __webpack_require__(5913);
var anObject = __webpack_require__(6154);
var toPrimitive = __webpack_require__(8537);

// MS Edge has broken Reflect.defineProperty - throwing instead of returning false
$export($export.S + $export.F * __webpack_require__(5810)(function () {
  // eslint-disable-next-line no-undef
  Reflect.defineProperty(dP.f({}, 1, {
    value: 1
  }), 1, {
    value: 2
  });
}), 'Reflect', {
  defineProperty: function defineProperty(target, propertyKey, attributes) {
    anObject(target);
    propertyKey = toPrimitive(propertyKey, true);
    anObject(attributes);
    try {
      dP.f(target, propertyKey, attributes);
      return true;
    } catch (e) {
      return false;
    }
  }
});

/***/ }),

/***/ 9060:
/***/ ((__unused_webpack_module, __unused_webpack_exports, __webpack_require__) => {

// 26.1.4 Reflect.deleteProperty(target, propertyKey)
var $export = __webpack_require__(5913);
var gOPD = (__webpack_require__(3299).f);
var anObject = __webpack_require__(6154);
$export($export.S, 'Reflect', {
  deleteProperty: function deleteProperty(target, propertyKey) {
    var desc = gOPD(anObject(target), propertyKey);
    return desc && !desc.configurable ? false : delete target[propertyKey];
  }
});

/***/ }),

/***/ 980:
/***/ ((__unused_webpack_module, __unused_webpack_exports, __webpack_require__) => {

"use strict";


// 26.1.5 Reflect.enumerate(target)
var $export = __webpack_require__(5913);
var anObject = __webpack_require__(6154);
var Enumerate = function Enumerate(iterated) {
  this._t = anObject(iterated); // target
  this._i = 0; // next index
  var keys = this._k = []; // keys
  var key;
  for (key in iterated) {
    keys.push(key);
  }
};
__webpack_require__(8258)(Enumerate, 'Object', function () {
  var that = this;
  var keys = that._k;
  var key;
  do {
    if (that._i >= keys.length) return {
      value: undefined,
      done: true
    };
  } while (!((key = keys[that._i++]) in that._t));
  return {
    value: key,
    done: false
  };
});
$export($export.S, 'Reflect', {
  enumerate: function enumerate(target) {
    return new Enumerate(target);
  }
});

/***/ }),

/***/ 8484:
/***/ ((__unused_webpack_module, __unused_webpack_exports, __webpack_require__) => {

// 26.1.7 Reflect.getOwnPropertyDescriptor(target, propertyKey)
var gOPD = __webpack_require__(3299);
var $export = __webpack_require__(5913);
var anObject = __webpack_require__(6154);
$export($export.S, 'Reflect', {
  getOwnPropertyDescriptor: function getOwnPropertyDescriptor(target, propertyKey) {
    return gOPD.f(anObject(target), propertyKey);
  }
});

/***/ }),

/***/ 9869:
/***/ ((__unused_webpack_module, __unused_webpack_exports, __webpack_require__) => {

// 26.1.8 Reflect.getPrototypeOf(target)
var $export = __webpack_require__(5913);
var getProto = __webpack_require__(4153);
var anObject = __webpack_require__(6154);
$export($export.S, 'Reflect', {
  getPrototypeOf: function getPrototypeOf(target) {
    return getProto(anObject(target));
  }
});

/***/ }),

/***/ 6175:
/***/ ((__unused_webpack_module, __unused_webpack_exports, __webpack_require__) => {

// 26.1.6 Reflect.get(target, propertyKey [, receiver])
var gOPD = __webpack_require__(3299);
var getPrototypeOf = __webpack_require__(4153);
var has = __webpack_require__(5389);
var $export = __webpack_require__(5913);
var isObject = __webpack_require__(7156);
var anObject = __webpack_require__(6154);
function get(target, propertyKey /* , receiver */) {
  var receiver = arguments.length < 3 ? target : arguments[2];
  var desc, proto;
  if (anObject(target) === receiver) return target[propertyKey];
  if (desc = gOPD.f(target, propertyKey)) return has(desc, 'value') ? desc.value : desc.get !== undefined ? desc.get.call(receiver) : undefined;
  if (isObject(proto = getPrototypeOf(target))) return get(proto, propertyKey, receiver);
}
$export($export.S, 'Reflect', {
  get: get
});

/***/ }),

/***/ 1285:
/***/ ((__unused_webpack_module, __unused_webpack_exports, __webpack_require__) => {

// 26.1.9 Reflect.has(target, propertyKey)
var $export = __webpack_require__(5913);
$export($export.S, 'Reflect', {
  has: function has(target, propertyKey) {
    return propertyKey in target;
  }
});

/***/ }),

/***/ 4854:
/***/ ((__unused_webpack_module, __unused_webpack_exports, __webpack_require__) => {

// 26.1.10 Reflect.isExtensible(target)
var $export = __webpack_require__(5913);
var anObject = __webpack_require__(6154);
var $isExtensible = Object.isExtensible;
$export($export.S, 'Reflect', {
  isExtensible: function isExtensible(target) {
    anObject(target);
    return $isExtensible ? $isExtensible(target) : true;
  }
});

/***/ }),

/***/ 6647:
/***/ ((__unused_webpack_module, __unused_webpack_exports, __webpack_require__) => {

// 26.1.11 Reflect.ownKeys(target)
var $export = __webpack_require__(5913);
$export($export.S, 'Reflect', {
  ownKeys: __webpack_require__(2600)
});

/***/ }),

/***/ 7903:
/***/ ((__unused_webpack_module, __unused_webpack_exports, __webpack_require__) => {

// 26.1.12 Reflect.preventExtensions(target)
var $export = __webpack_require__(5913);
var anObject = __webpack_require__(6154);
var $preventExtensions = Object.preventExtensions;
$export($export.S, 'Reflect', {
  preventExtensions: function preventExtensions(target) {
    anObject(target);
    try {
      if ($preventExtensions) $preventExtensions(target);
      return true;
    } catch (e) {
      return false;
    }
  }
});

/***/ }),

/***/ 3113:
/***/ ((__unused_webpack_module, __unused_webpack_exports, __webpack_require__) => {

// 26.1.14 Reflect.setPrototypeOf(target, proto)
var $export = __webpack_require__(5913);
var setProto = __webpack_require__(6931);
if (setProto) $export($export.S, 'Reflect', {
  setPrototypeOf: function setPrototypeOf(target, proto) {
    setProto.check(target, proto);
    try {
      setProto.set(target, proto);
      return true;
    } catch (e) {
      return false;
    }
  }
});

/***/ }),

/***/ 5197:
/***/ ((__unused_webpack_module, __unused_webpack_exports, __webpack_require__) => {

// 26.1.13 Reflect.set(target, propertyKey, V [, receiver])
var dP = __webpack_require__(4835);
var gOPD = __webpack_require__(3299);
var getPrototypeOf = __webpack_require__(4153);
var has = __webpack_require__(5389);
var $export = __webpack_require__(5913);
var createDesc = __webpack_require__(6256);
var anObject = __webpack_require__(6154);
var isObject = __webpack_require__(7156);
function set(target, propertyKey, V /* , receiver */) {
  var receiver = arguments.length < 4 ? target : arguments[3];
  var ownDesc = gOPD.f(anObject(target), propertyKey);
  var existingDescriptor, proto;
  if (!ownDesc) {
    if (isObject(proto = getPrototypeOf(target))) {
      return set(proto, propertyKey, V, receiver);
    }
    ownDesc = createDesc(0);
  }
  if (has(ownDesc, 'value')) {
    if (ownDesc.writable === false || !isObject(receiver)) return false;
    if (existingDescriptor = gOPD.f(receiver, propertyKey)) {
      if (existingDescriptor.get || existingDescriptor.set || existingDescriptor.writable === false) return false;
      existingDescriptor.value = V;
      dP.f(receiver, propertyKey, existingDescriptor);
    } else dP.f(receiver, propertyKey, createDesc(0, V));
    return true;
  }
  return ownDesc.set === undefined ? false : (ownDesc.set.call(receiver, V), true);
}
$export($export.S, 'Reflect', {
  set: set
});

/***/ }),

/***/ 2566:
/***/ ((__unused_webpack_module, __unused_webpack_exports, __webpack_require__) => {

var global = __webpack_require__(7381);
var inheritIfRequired = __webpack_require__(3654);
var dP = (__webpack_require__(4835).f);
var gOPN = (__webpack_require__(2982).f);
var isRegExp = __webpack_require__(1993);
var $flags = __webpack_require__(2188);
var $RegExp = global.RegExp;
var Base = $RegExp;
var proto = $RegExp.prototype;
var re1 = /a/g;
var re2 = /a/g;
// "new" creates a new object, old webkit buggy here
var CORRECT_NEW = new $RegExp(re1) !== re1;
if (__webpack_require__(4926) && (!CORRECT_NEW || __webpack_require__(5810)(function () {
  re2[__webpack_require__(3336)('match')] = false;
  // RegExp constructor can alter flags and IsRegExp works correct with @@match
  return $RegExp(re1) != re1 || $RegExp(re2) == re2 || $RegExp(re1, 'i') != '/a/i';
}))) {
  $RegExp = function RegExp(p, f) {
    var tiRE = this instanceof $RegExp;
    var piRE = isRegExp(p);
    var fiU = f === undefined;
    return !tiRE && piRE && p.constructor === $RegExp && fiU ? p : inheritIfRequired(CORRECT_NEW ? new Base(piRE && !fiU ? p.source : p, f) : Base((piRE = p instanceof $RegExp) ? p.source : p, piRE && fiU ? $flags.call(p) : f), tiRE ? this : proto, $RegExp);
  };
  var proxy = function proxy(key) {
    key in $RegExp || dP($RegExp, key, {
      configurable: true,
      get: function get() {
        return Base[key];
      },
      set: function set(it) {
        Base[key] = it;
      }
    });
  };
  for (var keys = gOPN(Base), i = 0; keys.length > i;) {
    proxy(keys[i++]);
  }
  proto.constructor = $RegExp;
  $RegExp.prototype = proto;
  __webpack_require__(7278)(global, 'RegExp', $RegExp);
}
__webpack_require__(4798)('RegExp');

/***/ }),

/***/ 5997:
/***/ ((__unused_webpack_module, __unused_webpack_exports, __webpack_require__) => {

"use strict";


var regexpExec = __webpack_require__(6997);
__webpack_require__(5913)({
  target: 'RegExp',
  proto: true,
  forced: regexpExec !== /./.exec
}, {
  exec: regexpExec
});

/***/ }),

/***/ 7181:
/***/ ((__unused_webpack_module, __unused_webpack_exports, __webpack_require__) => {

// 21.2.5.3 get RegExp.prototype.flags()
if (__webpack_require__(4926) && /./g.flags != 'g') (__webpack_require__(4835).f)(RegExp.prototype, 'flags', {
  configurable: true,
  get: __webpack_require__(2188)
});

/***/ }),

/***/ 8682:
/***/ ((__unused_webpack_module, __unused_webpack_exports, __webpack_require__) => {

"use strict";


var anObject = __webpack_require__(6154);
var toLength = __webpack_require__(8315);
var advanceStringIndex = __webpack_require__(1330);
var regExpExec = __webpack_require__(4585);

// @@match logic
__webpack_require__(8644)('match', 1, function (defined, MATCH, $match, maybeCallNative) {
  return [
  // `String.prototype.match` method
  // https://tc39.github.io/ecma262/#sec-string.prototype.match
  function match(regexp) {
    var O = defined(this);
    var fn = regexp == undefined ? undefined : regexp[MATCH];
    return fn !== undefined ? fn.call(regexp, O) : new RegExp(regexp)[MATCH](String(O));
  },
  // `RegExp.prototype[@@match]` method
  // https://tc39.github.io/ecma262/#sec-regexp.prototype-@@match
  function (regexp) {
    var res = maybeCallNative($match, regexp, this);
    if (res.done) return res.value;
    var rx = anObject(regexp);
    var S = String(this);
    if (!rx.global) return regExpExec(rx, S);
    var fullUnicode = rx.unicode;
    rx.lastIndex = 0;
    var A = [];
    var n = 0;
    var result;
    while ((result = regExpExec(rx, S)) !== null) {
      var matchStr = String(result[0]);
      A[n] = matchStr;
      if (matchStr === '') rx.lastIndex = advanceStringIndex(S, toLength(rx.lastIndex), fullUnicode);
      n++;
    }
    return n === 0 ? null : A;
  }];
});

/***/ }),

/***/ 8514:
/***/ ((__unused_webpack_module, __unused_webpack_exports, __webpack_require__) => {

"use strict";


var anObject = __webpack_require__(6154);
var toObject = __webpack_require__(2515);
var toLength = __webpack_require__(8315);
var toInteger = __webpack_require__(3230);
var advanceStringIndex = __webpack_require__(1330);
var regExpExec = __webpack_require__(4585);
var max = Math.max;
var min = Math.min;
var floor = Math.floor;
var SUBSTITUTION_SYMBOLS = /\$([$&`']|\d\d?|<[^>]*>)/g;
var SUBSTITUTION_SYMBOLS_NO_NAMED = /\$([$&`']|\d\d?)/g;
var maybeToString = function maybeToString(it) {
  return it === undefined ? it : String(it);
};

// @@replace logic
__webpack_require__(8644)('replace', 2, function (defined, REPLACE, $replace, maybeCallNative) {
  return [
  // `String.prototype.replace` method
  // https://tc39.github.io/ecma262/#sec-string.prototype.replace
  function replace(searchValue, replaceValue) {
    var O = defined(this);
    var fn = searchValue == undefined ? undefined : searchValue[REPLACE];
    return fn !== undefined ? fn.call(searchValue, O, replaceValue) : $replace.call(String(O), searchValue, replaceValue);
  },
  // `RegExp.prototype[@@replace]` method
  // https://tc39.github.io/ecma262/#sec-regexp.prototype-@@replace
  function (regexp, replaceValue) {
    var res = maybeCallNative($replace, regexp, this, replaceValue);
    if (res.done) return res.value;
    var rx = anObject(regexp);
    var S = String(this);
    var functionalReplace = typeof replaceValue === 'function';
    if (!functionalReplace) replaceValue = String(replaceValue);
    var global = rx.global;
    if (global) {
      var fullUnicode = rx.unicode;
      rx.lastIndex = 0;
    }
    var results = [];
    while (true) {
      var result = regExpExec(rx, S);
      if (result === null) break;
      results.push(result);
      if (!global) break;
      var matchStr = String(result[0]);
      if (matchStr === '') rx.lastIndex = advanceStringIndex(S, toLength(rx.lastIndex), fullUnicode);
    }
    var accumulatedResult = '';
    var nextSourcePosition = 0;
    for (var i = 0; i < results.length; i++) {
      result = results[i];
      var matched = String(result[0]);
      var position = max(min(toInteger(result.index), S.length), 0);
      var captures = [];
      // NOTE: This is equivalent to
      //   captures = result.slice(1).map(maybeToString)
      // but for some reason `nativeSlice.call(result, 1, result.length)` (called in
      // the slice polyfill when slicing native arrays) "doesn't work" in safari 9 and
      // causes a crash (https://pastebin.com/N21QzeQA) when trying to debug it.
      for (var j = 1; j < result.length; j++) {
        captures.push(maybeToString(result[j]));
      }
      var namedCaptures = result.groups;
      if (functionalReplace) {
        var replacerArgs = [matched].concat(captures, position, S);
        if (namedCaptures !== undefined) replacerArgs.push(namedCaptures);
        var replacement = String(replaceValue.apply(undefined, replacerArgs));
      } else {
        replacement = getSubstitution(matched, S, position, captures, namedCaptures, replaceValue);
      }
      if (position >= nextSourcePosition) {
        accumulatedResult += S.slice(nextSourcePosition, position) + replacement;
        nextSourcePosition = position + matched.length;
      }
    }
    return accumulatedResult + S.slice(nextSourcePosition);
  }];

  // https://tc39.github.io/ecma262/#sec-getsubstitution
  function getSubstitution(matched, str, position, captures, namedCaptures, replacement) {
    var tailPos = position + matched.length;
    var m = captures.length;
    var symbols = SUBSTITUTION_SYMBOLS_NO_NAMED;
    if (namedCaptures !== undefined) {
      namedCaptures = toObject(namedCaptures);
      symbols = SUBSTITUTION_SYMBOLS;
    }
    return $replace.call(replacement, symbols, function (match, ch) {
      var capture;
      switch (ch.charAt(0)) {
        case '$':
          return '$';
        case '&':
          return matched;
        case '`':
          return str.slice(0, position);
        case "'":
          return str.slice(tailPos);
        case '<':
          capture = namedCaptures[ch.slice(1, -1)];
          break;
        default:
          // \d\d?
          var n = +ch;
          if (n === 0) return match;
          if (n > m) {
            var f = floor(n / 10);
            if (f === 0) return match;
            if (f <= m) return captures[f - 1] === undefined ? ch.charAt(1) : captures[f - 1] + ch.charAt(1);
            return match;
          }
          capture = captures[n - 1];
      }
      return capture === undefined ? '' : capture;
    });
  }
});

/***/ }),

/***/ 5105:
/***/ ((__unused_webpack_module, __unused_webpack_exports, __webpack_require__) => {

"use strict";


var anObject = __webpack_require__(6154);
var sameValue = __webpack_require__(4261);
var regExpExec = __webpack_require__(4585);

// @@search logic
__webpack_require__(8644)('search', 1, function (defined, SEARCH, $search, maybeCallNative) {
  return [
  // `String.prototype.search` method
  // https://tc39.github.io/ecma262/#sec-string.prototype.search
  function search(regexp) {
    var O = defined(this);
    var fn = regexp == undefined ? undefined : regexp[SEARCH];
    return fn !== undefined ? fn.call(regexp, O) : new RegExp(regexp)[SEARCH](String(O));
  },
  // `RegExp.prototype[@@search]` method
  // https://tc39.github.io/ecma262/#sec-regexp.prototype-@@search
  function (regexp) {
    var res = maybeCallNative($search, regexp, this);
    if (res.done) return res.value;
    var rx = anObject(regexp);
    var S = String(this);
    var previousLastIndex = rx.lastIndex;
    if (!sameValue(previousLastIndex, 0)) rx.lastIndex = 0;
    var result = regExpExec(rx, S);
    if (!sameValue(rx.lastIndex, previousLastIndex)) rx.lastIndex = previousLastIndex;
    return result === null ? -1 : result.index;
  }];
});

/***/ }),

/***/ 5325:
/***/ ((__unused_webpack_module, __unused_webpack_exports, __webpack_require__) => {

"use strict";


var isRegExp = __webpack_require__(1993);
var anObject = __webpack_require__(6154);
var speciesConstructor = __webpack_require__(2035);
var advanceStringIndex = __webpack_require__(1330);
var toLength = __webpack_require__(8315);
var callRegExpExec = __webpack_require__(4585);
var regexpExec = __webpack_require__(6997);
var fails = __webpack_require__(5810);
var $min = Math.min;
var $push = [].push;
var $SPLIT = 'split';
var LENGTH = 'length';
var LAST_INDEX = 'lastIndex';
var MAX_UINT32 = 0xffffffff;

// babel-minify transpiles RegExp('x', 'y') -> /x/y and it causes SyntaxError
var SUPPORTS_Y = !fails(function () {
  RegExp(MAX_UINT32, 'y');
});

// @@split logic
__webpack_require__(8644)('split', 2, function (defined, SPLIT, $split, maybeCallNative) {
  var internalSplit;
  if ('abbc'[$SPLIT](/(b)*/)[1] == 'c' || 'test'[$SPLIT](/(?:)/, -1)[LENGTH] != 4 || 'ab'[$SPLIT](/(?:ab)*/)[LENGTH] != 2 || '.'[$SPLIT](/(.?)(.?)/)[LENGTH] != 4 || '.'[$SPLIT](/()()/)[LENGTH] > 1 || ''[$SPLIT](/.?/)[LENGTH]) {
    // based on es5-shim implementation, need to rework it
    internalSplit = function internalSplit(separator, limit) {
      var string = String(this);
      if (separator === undefined && limit === 0) return [];
      // If `separator` is not a regex, use native split
      if (!isRegExp(separator)) return $split.call(string, separator, limit);
      var output = [];
      var flags = (separator.ignoreCase ? 'i' : '') + (separator.multiline ? 'm' : '') + (separator.unicode ? 'u' : '') + (separator.sticky ? 'y' : '');
      var lastLastIndex = 0;
      var splitLimit = limit === undefined ? MAX_UINT32 : limit >>> 0;
      // Make `global` and avoid `lastIndex` issues by working with a copy
      var separatorCopy = new RegExp(separator.source, flags + 'g');
      var match, lastIndex, lastLength;
      while (match = regexpExec.call(separatorCopy, string)) {
        lastIndex = separatorCopy[LAST_INDEX];
        if (lastIndex > lastLastIndex) {
          output.push(string.slice(lastLastIndex, match.index));
          if (match[LENGTH] > 1 && match.index < string[LENGTH]) $push.apply(output, match.slice(1));
          lastLength = match[0][LENGTH];
          lastLastIndex = lastIndex;
          if (output[LENGTH] >= splitLimit) break;
        }
        if (separatorCopy[LAST_INDEX] === match.index) separatorCopy[LAST_INDEX]++; // Avoid an infinite loop
      }

      if (lastLastIndex === string[LENGTH]) {
        if (lastLength || !separatorCopy.test('')) output.push('');
      } else output.push(string.slice(lastLastIndex));
      return output[LENGTH] > splitLimit ? output.slice(0, splitLimit) : output;
    };
    // Chakra, V8
  } else if ('0'[$SPLIT](undefined, 0)[LENGTH]) {
    internalSplit = function internalSplit(separator, limit) {
      return separator === undefined && limit === 0 ? [] : $split.call(this, separator, limit);
    };
  } else {
    internalSplit = $split;
  }
  return [
  // `String.prototype.split` method
  // https://tc39.github.io/ecma262/#sec-string.prototype.split
  function split(separator, limit) {
    var O = defined(this);
    var splitter = separator == undefined ? undefined : separator[SPLIT];
    return splitter !== undefined ? splitter.call(separator, O, limit) : internalSplit.call(String(O), separator, limit);
  },
  // `RegExp.prototype[@@split]` method
  // https://tc39.github.io/ecma262/#sec-regexp.prototype-@@split
  //
  // NOTE: This cannot be properly polyfilled in engines that don't support
  // the 'y' flag.
  function (regexp, limit) {
    var res = maybeCallNative(internalSplit, regexp, this, limit, internalSplit !== $split);
    if (res.done) return res.value;
    var rx = anObject(regexp);
    var S = String(this);
    var C = speciesConstructor(rx, RegExp);
    var unicodeMatching = rx.unicode;
    var flags = (rx.ignoreCase ? 'i' : '') + (rx.multiline ? 'm' : '') + (rx.unicode ? 'u' : '') + (SUPPORTS_Y ? 'y' : 'g');

    // ^(? + rx + ) is needed, in combination with some S slicing, to
    // simulate the 'y' flag.
    var splitter = new C(SUPPORTS_Y ? rx : '^(?:' + rx.source + ')', flags);
    var lim = limit === undefined ? MAX_UINT32 : limit >>> 0;
    if (lim === 0) return [];
    if (S.length === 0) return callRegExpExec(splitter, S) === null ? [S] : [];
    var p = 0;
    var q = 0;
    var A = [];
    while (q < S.length) {
      splitter.lastIndex = SUPPORTS_Y ? q : 0;
      var z = callRegExpExec(splitter, SUPPORTS_Y ? S : S.slice(q));
      var e;
      if (z === null || (e = $min(toLength(splitter.lastIndex + (SUPPORTS_Y ? 0 : q)), S.length)) === p) {
        q = advanceStringIndex(S, q, unicodeMatching);
      } else {
        A.push(S.slice(p, q));
        if (A.length === lim) return A;
        for (var i = 1; i <= z.length - 1; i++) {
          A.push(z[i]);
          if (A.length === lim) return A;
        }
        q = p = e;
      }
    }
    A.push(S.slice(p));
    return A;
  }];
});

/***/ }),

/***/ 8359:
/***/ ((__unused_webpack_module, __unused_webpack_exports, __webpack_require__) => {

"use strict";


__webpack_require__(7181);
var anObject = __webpack_require__(6154);
var $flags = __webpack_require__(2188);
var DESCRIPTORS = __webpack_require__(4926);
var TO_STRING = 'toString';
var $toString = /./[TO_STRING];
var define = function define(fn) {
  __webpack_require__(7278)(RegExp.prototype, TO_STRING, fn, true);
};

// 21.2.5.14 RegExp.prototype.toString()
if (__webpack_require__(5810)(function () {
  return $toString.call({
    source: 'a',
    flags: 'b'
  }) != '/a/b';
})) {
  define(function toString() {
    var R = anObject(this);
    return '/'.concat(R.source, '/', 'flags' in R ? R.flags : !DESCRIPTORS && R instanceof RegExp ? $flags.call(R) : undefined);
  });
  // FF44- RegExp#toString has a wrong name
} else if ($toString.name != TO_STRING) {
  define(function toString() {
    return $toString.call(this);
  });
}

/***/ }),

/***/ 3940:
/***/ ((module, __unused_webpack_exports, __webpack_require__) => {

"use strict";


var strong = __webpack_require__(4396);
var validate = __webpack_require__(8546);
var SET = 'Set';

// 23.2 Set Objects
module.exports = __webpack_require__(1966)(SET, function (get) {
  return function Set() {
    return get(this, arguments.length > 0 ? arguments[0] : undefined);
  };
}, {
  // 23.2.3.1 Set.prototype.add(value)
  add: function add(value) {
    return strong.def(validate(this, SET), value = value === 0 ? 0 : value, value);
  }
}, strong);

/***/ }),

/***/ 9718:
/***/ ((__unused_webpack_module, __unused_webpack_exports, __webpack_require__) => {

"use strict";


// B.2.3.2 String.prototype.anchor(name)
__webpack_require__(9927)('anchor', function (createHTML) {
  return function anchor(name) {
    return createHTML(this, 'a', 'name', name);
  };
});

/***/ }),

/***/ 3845:
/***/ ((__unused_webpack_module, __unused_webpack_exports, __webpack_require__) => {

"use strict";


// B.2.3.3 String.prototype.big()
__webpack_require__(9927)('big', function (createHTML) {
  return function big() {
    return createHTML(this, 'big', '', '');
  };
});

/***/ }),

/***/ 5803:
/***/ ((__unused_webpack_module, __unused_webpack_exports, __webpack_require__) => {

"use strict";


// B.2.3.4 String.prototype.blink()
__webpack_require__(9927)('blink', function (createHTML) {
  return function blink() {
    return createHTML(this, 'blink', '', '');
  };
});

/***/ }),

/***/ 2222:
/***/ ((__unused_webpack_module, __unused_webpack_exports, __webpack_require__) => {

"use strict";


// B.2.3.5 String.prototype.bold()
__webpack_require__(9927)('bold', function (createHTML) {
  return function bold() {
    return createHTML(this, 'b', '', '');
  };
});

/***/ }),

/***/ 5281:
/***/ ((__unused_webpack_module, __unused_webpack_exports, __webpack_require__) => {

"use strict";


var $export = __webpack_require__(5913);
var $at = __webpack_require__(3593)(false);
$export($export.P, 'String', {
  // 21.1.3.3 String.prototype.codePointAt(pos)
  codePointAt: function codePointAt(pos) {
    return $at(this, pos);
  }
});

/***/ }),

/***/ 3917:
/***/ ((__unused_webpack_module, __unused_webpack_exports, __webpack_require__) => {

"use strict";
// 21.1.3.6 String.prototype.endsWith(searchString [, endPosition])


var $export = __webpack_require__(5913);
var toLength = __webpack_require__(8315);
var context = __webpack_require__(2376);
var ENDS_WITH = 'endsWith';
var $endsWith = ''[ENDS_WITH];
$export($export.P + $export.F * __webpack_require__(3483)(ENDS_WITH), 'String', {
  endsWith: function endsWith(searchString /* , endPosition = @length */) {
    var that = context(this, searchString, ENDS_WITH);
    var endPosition = arguments.length > 1 ? arguments[1] : undefined;
    var len = toLength(that.length);
    var end = endPosition === undefined ? len : Math.min(toLength(endPosition), len);
    var search = String(searchString);
    return $endsWith ? $endsWith.call(that, search, end) : that.slice(end - search.length, end) === search;
  }
});

/***/ }),

/***/ 5036:
/***/ ((__unused_webpack_module, __unused_webpack_exports, __webpack_require__) => {

"use strict";


// B.2.3.6 String.prototype.fixed()
__webpack_require__(9927)('fixed', function (createHTML) {
  return function fixed() {
    return createHTML(this, 'tt', '', '');
  };
});

/***/ }),

/***/ 6131:
/***/ ((__unused_webpack_module, __unused_webpack_exports, __webpack_require__) => {

"use strict";


// B.2.3.7 String.prototype.fontcolor(color)
__webpack_require__(9927)('fontcolor', function (createHTML) {
  return function fontcolor(color) {
    return createHTML(this, 'font', 'color', color);
  };
});

/***/ }),

/***/ 4110:
/***/ ((__unused_webpack_module, __unused_webpack_exports, __webpack_require__) => {

"use strict";


// B.2.3.8 String.prototype.fontsize(size)
__webpack_require__(9927)('fontsize', function (createHTML) {
  return function fontsize(size) {
    return createHTML(this, 'font', 'size', size);
  };
});

/***/ }),

/***/ 8577:
/***/ ((__unused_webpack_module, __unused_webpack_exports, __webpack_require__) => {

var $export = __webpack_require__(5913);
var toAbsoluteIndex = __webpack_require__(6241);
var fromCharCode = String.fromCharCode;
var $fromCodePoint = String.fromCodePoint;

// length should be 1, old FF problem
$export($export.S + $export.F * (!!$fromCodePoint && $fromCodePoint.length != 1), 'String', {
  // 21.1.2.2 String.fromCodePoint(...codePoints)
  fromCodePoint: function fromCodePoint(x) {
    // eslint-disable-line no-unused-vars
    var res = [];
    var aLen = arguments.length;
    var i = 0;
    var code;
    while (aLen > i) {
      code = +arguments[i++];
      if (toAbsoluteIndex(code, 0x10ffff) !== code) throw RangeError(code + ' is not a valid code point');
      res.push(code < 0x10000 ? fromCharCode(code) : fromCharCode(((code -= 0x10000) >> 10) + 0xd800, code % 0x400 + 0xdc00));
    }
    return res.join('');
  }
});

/***/ }),

/***/ 5450:
/***/ ((__unused_webpack_module, __unused_webpack_exports, __webpack_require__) => {

"use strict";
// 21.1.3.7 String.prototype.includes(searchString, position = 0)


var $export = __webpack_require__(5913);
var context = __webpack_require__(2376);
var INCLUDES = 'includes';
$export($export.P + $export.F * __webpack_require__(3483)(INCLUDES), 'String', {
  includes: function includes(searchString /* , position = 0 */) {
    return !!~context(this, searchString, INCLUDES).indexOf(searchString, arguments.length > 1 ? arguments[1] : undefined);
  }
});

/***/ }),

/***/ 6235:
/***/ ((__unused_webpack_module, __unused_webpack_exports, __webpack_require__) => {

"use strict";


// B.2.3.9 String.prototype.italics()
__webpack_require__(9927)('italics', function (createHTML) {
  return function italics() {
    return createHTML(this, 'i', '', '');
  };
});

/***/ }),

/***/ 6575:
/***/ ((__unused_webpack_module, __unused_webpack_exports, __webpack_require__) => {

"use strict";


var $at = __webpack_require__(3593)(true);

// 21.1.3.27 String.prototype[@@iterator]()
__webpack_require__(4873)(String, 'String', function (iterated) {
  this._t = String(iterated); // target
  this._i = 0; // next index
  // 21.1.5.2.1 %StringIteratorPrototype%.next()
}, function () {
  var O = this._t;
  var index = this._i;
  var point;
  if (index >= O.length) return {
    value: undefined,
    done: true
  };
  point = $at(O, index);
  this._i += point.length;
  return {
    value: point,
    done: false
  };
});

/***/ }),

/***/ 6495:
/***/ ((__unused_webpack_module, __unused_webpack_exports, __webpack_require__) => {

"use strict";


// B.2.3.10 String.prototype.link(url)
__webpack_require__(9927)('link', function (createHTML) {
  return function link(url) {
    return createHTML(this, 'a', 'href', url);
  };
});

/***/ }),

/***/ 7906:
/***/ ((__unused_webpack_module, __unused_webpack_exports, __webpack_require__) => {

var $export = __webpack_require__(5913);
var toIObject = __webpack_require__(8499);
var toLength = __webpack_require__(8315);
$export($export.S, 'String', {
  // 21.1.2.4 String.raw(callSite, ...substitutions)
  raw: function raw(callSite) {
    var tpl = toIObject(callSite.raw);
    var len = toLength(tpl.length);
    var aLen = arguments.length;
    var res = [];
    var i = 0;
    while (len > i) {
      res.push(String(tpl[i++]));
      if (i < aLen) res.push(String(arguments[i]));
    }
    return res.join('');
  }
});

/***/ }),

/***/ 9449:
/***/ ((__unused_webpack_module, __unused_webpack_exports, __webpack_require__) => {

var $export = __webpack_require__(5913);
$export($export.P, 'String', {
  // 21.1.3.13 String.prototype.repeat(count)
  repeat: __webpack_require__(1924)
});

/***/ }),

/***/ 4162:
/***/ ((__unused_webpack_module, __unused_webpack_exports, __webpack_require__) => {

"use strict";


// B.2.3.11 String.prototype.small()
__webpack_require__(9927)('small', function (createHTML) {
  return function small() {
    return createHTML(this, 'small', '', '');
  };
});

/***/ }),

/***/ 1616:
/***/ ((__unused_webpack_module, __unused_webpack_exports, __webpack_require__) => {

"use strict";
// 21.1.3.18 String.prototype.startsWith(searchString [, position ])


var $export = __webpack_require__(5913);
var toLength = __webpack_require__(8315);
var context = __webpack_require__(2376);
var STARTS_WITH = 'startsWith';
var $startsWith = ''[STARTS_WITH];
$export($export.P + $export.F * __webpack_require__(3483)(STARTS_WITH), 'String', {
  startsWith: function startsWith(searchString /* , position = 0 */) {
    var that = context(this, searchString, STARTS_WITH);
    var index = toLength(Math.min(arguments.length > 1 ? arguments[1] : undefined, that.length));
    var search = String(searchString);
    return $startsWith ? $startsWith.call(that, search, index) : that.slice(index, index + search.length) === search;
  }
});

/***/ }),

/***/ 5297:
/***/ ((__unused_webpack_module, __unused_webpack_exports, __webpack_require__) => {

"use strict";


// B.2.3.12 String.prototype.strike()
__webpack_require__(9927)('strike', function (createHTML) {
  return function strike() {
    return createHTML(this, 'strike', '', '');
  };
});

/***/ }),

/***/ 1466:
/***/ ((__unused_webpack_module, __unused_webpack_exports, __webpack_require__) => {

"use strict";


// B.2.3.13 String.prototype.sub()
__webpack_require__(9927)('sub', function (createHTML) {
  return function sub() {
    return createHTML(this, 'sub', '', '');
  };
});

/***/ }),

/***/ 2581:
/***/ ((__unused_webpack_module, __unused_webpack_exports, __webpack_require__) => {

"use strict";


// B.2.3.14 String.prototype.sup()
__webpack_require__(9927)('sup', function (createHTML) {
  return function sup() {
    return createHTML(this, 'sup', '', '');
  };
});

/***/ }),

/***/ 8587:
/***/ ((__unused_webpack_module, __unused_webpack_exports, __webpack_require__) => {

"use strict";


// 21.1.3.25 String.prototype.trim()
__webpack_require__(618)('trim', function ($trim) {
  return function trim() {
    return $trim(this, 3);
  };
});

/***/ }),

/***/ 2403:
/***/ ((__unused_webpack_module, __unused_webpack_exports, __webpack_require__) => {

"use strict";


// ECMAScript 6 symbols shim
function _typeof(obj) { "@babel/helpers - typeof"; return _typeof = "function" == typeof Symbol && "symbol" == typeof Symbol.iterator ? function (obj) { return typeof obj; } : function (obj) { return obj && "function" == typeof Symbol && obj.constructor === Symbol && obj !== Symbol.prototype ? "symbol" : typeof obj; }, _typeof(obj); }
var global = __webpack_require__(7381);
var has = __webpack_require__(5389);
var DESCRIPTORS = __webpack_require__(4926);
var $export = __webpack_require__(5913);
var redefine = __webpack_require__(7278);
var META = (__webpack_require__(3763).KEY);
var $fails = __webpack_require__(5810);
var shared = __webpack_require__(3192);
var setToStringTag = __webpack_require__(8094);
var uid = __webpack_require__(7936);
var wks = __webpack_require__(3336);
var wksExt = __webpack_require__(9078);
var wksDefine = __webpack_require__(5721);
var enumKeys = __webpack_require__(8727);
var isArray = __webpack_require__(1320);
var anObject = __webpack_require__(6154);
var isObject = __webpack_require__(7156);
var toObject = __webpack_require__(2515);
var toIObject = __webpack_require__(8499);
var toPrimitive = __webpack_require__(8537);
var createDesc = __webpack_require__(6256);
var _create = __webpack_require__(4275);
var gOPNExt = __webpack_require__(3136);
var $GOPD = __webpack_require__(3299);
var $GOPS = __webpack_require__(5421);
var $DP = __webpack_require__(4835);
var $keys = __webpack_require__(9924);
var gOPD = $GOPD.f;
var dP = $DP.f;
var gOPN = gOPNExt.f;
var $Symbol = global.Symbol;
var $JSON = global.JSON;
var _stringify = $JSON && $JSON.stringify;
var PROTOTYPE = 'prototype';
var HIDDEN = wks('_hidden');
var TO_PRIMITIVE = wks('toPrimitive');
var isEnum = {}.propertyIsEnumerable;
var SymbolRegistry = shared('symbol-registry');
var AllSymbols = shared('symbols');
var OPSymbols = shared('op-symbols');
var ObjectProto = Object[PROTOTYPE];
var USE_NATIVE = typeof $Symbol == 'function' && !!$GOPS.f;
var QObject = global.QObject;
// Don't use setters in Qt Script, https://github.com/zloirock/core-js/issues/173
var setter = !QObject || !QObject[PROTOTYPE] || !QObject[PROTOTYPE].findChild;

// fallback for old Android, https://code.google.com/p/v8/issues/detail?id=687
var setSymbolDesc = DESCRIPTORS && $fails(function () {
  return _create(dP({}, 'a', {
    get: function get() {
      return dP(this, 'a', {
        value: 7
      }).a;
    }
  })).a != 7;
}) ? function (it, key, D) {
  var protoDesc = gOPD(ObjectProto, key);
  if (protoDesc) delete ObjectProto[key];
  dP(it, key, D);
  if (protoDesc && it !== ObjectProto) dP(ObjectProto, key, protoDesc);
} : dP;
var wrap = function wrap(tag) {
  var sym = AllSymbols[tag] = _create($Symbol[PROTOTYPE]);
  sym._k = tag;
  return sym;
};
var isSymbol = USE_NATIVE && _typeof($Symbol.iterator) == 'symbol' ? function (it) {
  return _typeof(it) == 'symbol';
} : function (it) {
  return it instanceof $Symbol;
};
var $defineProperty = function defineProperty(it, key, D) {
  if (it === ObjectProto) $defineProperty(OPSymbols, key, D);
  anObject(it);
  key = toPrimitive(key, true);
  anObject(D);
  if (has(AllSymbols, key)) {
    if (!D.enumerable) {
      if (!has(it, HIDDEN)) dP(it, HIDDEN, createDesc(1, {}));
      it[HIDDEN][key] = true;
    } else {
      if (has(it, HIDDEN) && it[HIDDEN][key]) it[HIDDEN][key] = false;
      D = _create(D, {
        enumerable: createDesc(0, false)
      });
    }
    return setSymbolDesc(it, key, D);
  }
  return dP(it, key, D);
};
var $defineProperties = function defineProperties(it, P) {
  anObject(it);
  var keys = enumKeys(P = toIObject(P));
  var i = 0;
  var l = keys.length;
  var key;
  while (l > i) {
    $defineProperty(it, key = keys[i++], P[key]);
  }
  return it;
};
var $create = function create(it, P) {
  return P === undefined ? _create(it) : $defineProperties(_create(it), P);
};
var $propertyIsEnumerable = function propertyIsEnumerable(key) {
  var E = isEnum.call(this, key = toPrimitive(key, true));
  if (this === ObjectProto && has(AllSymbols, key) && !has(OPSymbols, key)) return false;
  return E || !has(this, key) || !has(AllSymbols, key) || has(this, HIDDEN) && this[HIDDEN][key] ? E : true;
};
var $getOwnPropertyDescriptor = function getOwnPropertyDescriptor(it, key) {
  it = toIObject(it);
  key = toPrimitive(key, true);
  if (it === ObjectProto && has(AllSymbols, key) && !has(OPSymbols, key)) return;
  var D = gOPD(it, key);
  if (D && has(AllSymbols, key) && !(has(it, HIDDEN) && it[HIDDEN][key])) D.enumerable = true;
  return D;
};
var $getOwnPropertyNames = function getOwnPropertyNames(it) {
  var names = gOPN(toIObject(it));
  var result = [];
  var i = 0;
  var key;
  while (names.length > i) {
    if (!has(AllSymbols, key = names[i++]) && key != HIDDEN && key != META) result.push(key);
  }
  return result;
};
var $getOwnPropertySymbols = function getOwnPropertySymbols(it) {
  var IS_OP = it === ObjectProto;
  var names = gOPN(IS_OP ? OPSymbols : toIObject(it));
  var result = [];
  var i = 0;
  var key;
  while (names.length > i) {
    if (has(AllSymbols, key = names[i++]) && (IS_OP ? has(ObjectProto, key) : true)) result.push(AllSymbols[key]);
  }
  return result;
};

// 19.4.1.1 Symbol([description])
if (!USE_NATIVE) {
  $Symbol = function _Symbol() {
    if (this instanceof $Symbol) throw TypeError('Symbol is not a constructor!');
    var tag = uid(arguments.length > 0 ? arguments[0] : undefined);
    var $set = function $set(value) {
      if (this === ObjectProto) $set.call(OPSymbols, value);
      if (has(this, HIDDEN) && has(this[HIDDEN], tag)) this[HIDDEN][tag] = false;
      setSymbolDesc(this, tag, createDesc(1, value));
    };
    if (DESCRIPTORS && setter) setSymbolDesc(ObjectProto, tag, {
      configurable: true,
      set: $set
    });
    return wrap(tag);
  };
  redefine($Symbol[PROTOTYPE], 'toString', function toString() {
    return this._k;
  });
  $GOPD.f = $getOwnPropertyDescriptor;
  $DP.f = $defineProperty;
  (__webpack_require__(2982).f) = gOPNExt.f = $getOwnPropertyNames;
  (__webpack_require__(4616).f) = $propertyIsEnumerable;
  $GOPS.f = $getOwnPropertySymbols;
  if (DESCRIPTORS && !__webpack_require__(4219)) {
    redefine(ObjectProto, 'propertyIsEnumerable', $propertyIsEnumerable, true);
  }
  wksExt.f = function (name) {
    return wrap(wks(name));
  };
}
$export($export.G + $export.W + $export.F * !USE_NATIVE, {
  Symbol: $Symbol
});
for (var es6Symbols =
  // 19.4.2.2, 19.4.2.3, 19.4.2.4, 19.4.2.6, 19.4.2.8, 19.4.2.9, 19.4.2.10, 19.4.2.11, 19.4.2.12, 19.4.2.13, 19.4.2.14
  'hasInstance,isConcatSpreadable,iterator,match,replace,search,species,split,toPrimitive,toStringTag,unscopables'.split(','), j = 0; es6Symbols.length > j;) {
  wks(es6Symbols[j++]);
}
for (var wellKnownSymbols = $keys(wks.store), k = 0; wellKnownSymbols.length > k;) {
  wksDefine(wellKnownSymbols[k++]);
}
$export($export.S + $export.F * !USE_NATIVE, 'Symbol', {
  // 19.4.2.1 Symbol.for(key)
  'for': function _for(key) {
    return has(SymbolRegistry, key += '') ? SymbolRegistry[key] : SymbolRegistry[key] = $Symbol(key);
  },
  // 19.4.2.5 Symbol.keyFor(sym)
  keyFor: function keyFor(sym) {
    if (!isSymbol(sym)) throw TypeError(sym + ' is not a symbol!');
    for (var key in SymbolRegistry) {
      if (SymbolRegistry[key] === sym) return key;
    }
  },
  useSetter: function useSetter() {
    setter = true;
  },
  useSimple: function useSimple() {
    setter = false;
  }
});
$export($export.S + $export.F * !USE_NATIVE, 'Object', {
  // 19.1.2.2 Object.create(O [, Properties])
  create: $create,
  // 19.1.2.4 Object.defineProperty(O, P, Attributes)
  defineProperty: $defineProperty,
  // 19.1.2.3 Object.defineProperties(O, Properties)
  defineProperties: $defineProperties,
  // 19.1.2.6 Object.getOwnPropertyDescriptor(O, P)
  getOwnPropertyDescriptor: $getOwnPropertyDescriptor,
  // 19.1.2.7 Object.getOwnPropertyNames(O)
  getOwnPropertyNames: $getOwnPropertyNames,
  // 19.1.2.8 Object.getOwnPropertySymbols(O)
  getOwnPropertySymbols: $getOwnPropertySymbols
});

// Chrome 38 and 39 `Object.getOwnPropertySymbols` fails on primitives
// https://bugs.chromium.org/p/v8/issues/detail?id=3443
var FAILS_ON_PRIMITIVES = $fails(function () {
  $GOPS.f(1);
});
$export($export.S + $export.F * FAILS_ON_PRIMITIVES, 'Object', {
  getOwnPropertySymbols: function getOwnPropertySymbols(it) {
    return $GOPS.f(toObject(it));
  }
});

// 24.3.2 JSON.stringify(value [, replacer [, space]])
$JSON && $export($export.S + $export.F * (!USE_NATIVE || $fails(function () {
  var S = $Symbol();
  // MS Edge converts symbol values to JSON as {}
  // WebKit converts symbol values to JSON as null
  // V8 throws on boxed symbols
  return _stringify([S]) != '[null]' || _stringify({
    a: S
  }) != '{}' || _stringify(Object(S)) != '{}';
})), 'JSON', {
  stringify: function stringify(it) {
    var args = [it];
    var i = 1;
    var replacer, $replacer;
    while (arguments.length > i) {
      args.push(arguments[i++]);
    }
    $replacer = replacer = args[1];
    if (!isObject(replacer) && it === undefined || isSymbol(it)) return; // IE8 returns string on undefined
    if (!isArray(replacer)) replacer = function replacer(key, value) {
      if (typeof $replacer == 'function') value = $replacer.call(this, key, value);
      if (!isSymbol(value)) return value;
    };
    args[1] = replacer;
    return _stringify.apply($JSON, args);
  }
});

// 19.4.3.4 Symbol.prototype[@@toPrimitive](hint)
$Symbol[PROTOTYPE][TO_PRIMITIVE] || __webpack_require__(8012)($Symbol[PROTOTYPE], TO_PRIMITIVE, $Symbol[PROTOTYPE].valueOf);
// 19.4.3.5 Symbol.prototype[@@toStringTag]
setToStringTag($Symbol, 'Symbol');
// 20.2.1.9 Math[@@toStringTag]
setToStringTag(Math, 'Math', true);
// 24.3.3 JSON[@@toStringTag]
setToStringTag(global.JSON, 'JSON', true);

/***/ }),

/***/ 7195:
/***/ ((__unused_webpack_module, __unused_webpack_exports, __webpack_require__) => {

"use strict";


var $export = __webpack_require__(5913);
var $typed = __webpack_require__(9161);
var buffer = __webpack_require__(9782);
var anObject = __webpack_require__(6154);
var toAbsoluteIndex = __webpack_require__(6241);
var toLength = __webpack_require__(8315);
var isObject = __webpack_require__(7156);
var ArrayBuffer = (__webpack_require__(7381).ArrayBuffer);
var speciesConstructor = __webpack_require__(2035);
var $ArrayBuffer = buffer.ArrayBuffer;
var $DataView = buffer.DataView;
var $isView = $typed.ABV && ArrayBuffer.isView;
var $slice = $ArrayBuffer.prototype.slice;
var VIEW = $typed.VIEW;
var ARRAY_BUFFER = 'ArrayBuffer';
$export($export.G + $export.W + $export.F * (ArrayBuffer !== $ArrayBuffer), {
  ArrayBuffer: $ArrayBuffer
});
$export($export.S + $export.F * !$typed.CONSTR, ARRAY_BUFFER, {
  // 24.1.3.1 ArrayBuffer.isView(arg)
  isView: function isView(it) {
    return $isView && $isView(it) || isObject(it) && VIEW in it;
  }
});
$export($export.P + $export.U + $export.F * __webpack_require__(5810)(function () {
  return !new $ArrayBuffer(2).slice(1, undefined).byteLength;
}), ARRAY_BUFFER, {
  // 24.1.4.3 ArrayBuffer.prototype.slice(start, end)
  slice: function slice(start, end) {
    if ($slice !== undefined && end === undefined) return $slice.call(anObject(this), start); // FF fix
    var len = anObject(this).byteLength;
    var first = toAbsoluteIndex(start, len);
    var fin = toAbsoluteIndex(end === undefined ? len : end, len);
    var result = new (speciesConstructor(this, $ArrayBuffer))(toLength(fin - first));
    var viewS = new $DataView(this);
    var viewT = new $DataView(result);
    var index = 0;
    while (first < fin) {
      viewT.setUint8(index++, viewS.getUint8(first++));
    }
    return result;
  }
});
__webpack_require__(4798)(ARRAY_BUFFER);

/***/ }),

/***/ 5345:
/***/ ((__unused_webpack_module, __unused_webpack_exports, __webpack_require__) => {

var $export = __webpack_require__(5913);
$export($export.G + $export.W + $export.F * !(__webpack_require__(9161).ABV), {
  DataView: (__webpack_require__(9782).DataView)
});

/***/ }),

/***/ 8824:
/***/ ((__unused_webpack_module, __unused_webpack_exports, __webpack_require__) => {

__webpack_require__(431)('Float32', 4, function (init) {
  return function Float32Array(data, byteOffset, length) {
    return init(this, data, byteOffset, length);
  };
});

/***/ }),

/***/ 6472:
/***/ ((__unused_webpack_module, __unused_webpack_exports, __webpack_require__) => {

__webpack_require__(431)('Float64', 8, function (init) {
  return function Float64Array(data, byteOffset, length) {
    return init(this, data, byteOffset, length);
  };
});

/***/ }),

/***/ 7683:
/***/ ((__unused_webpack_module, __unused_webpack_exports, __webpack_require__) => {

__webpack_require__(431)('Int16', 2, function (init) {
  return function Int16Array(data, byteOffset, length) {
    return init(this, data, byteOffset, length);
  };
});

/***/ }),

/***/ 4797:
/***/ ((__unused_webpack_module, __unused_webpack_exports, __webpack_require__) => {

__webpack_require__(431)('Int32', 4, function (init) {
  return function Int32Array(data, byteOffset, length) {
    return init(this, data, byteOffset, length);
  };
});

/***/ }),

/***/ 6670:
/***/ ((__unused_webpack_module, __unused_webpack_exports, __webpack_require__) => {

__webpack_require__(431)('Int8', 1, function (init) {
  return function Int8Array(data, byteOffset, length) {
    return init(this, data, byteOffset, length);
  };
});

/***/ }),

/***/ 1123:
/***/ ((__unused_webpack_module, __unused_webpack_exports, __webpack_require__) => {

__webpack_require__(431)('Uint16', 2, function (init) {
  return function Uint16Array(data, byteOffset, length) {
    return init(this, data, byteOffset, length);
  };
});

/***/ }),

/***/ 4871:
/***/ ((__unused_webpack_module, __unused_webpack_exports, __webpack_require__) => {

__webpack_require__(431)('Uint32', 4, function (init) {
  return function Uint32Array(data, byteOffset, length) {
    return init(this, data, byteOffset, length);
  };
});

/***/ }),

/***/ 7736:
/***/ ((__unused_webpack_module, __unused_webpack_exports, __webpack_require__) => {

__webpack_require__(431)('Uint8', 1, function (init) {
  return function Uint8Array(data, byteOffset, length) {
    return init(this, data, byteOffset, length);
  };
});

/***/ }),

/***/ 4457:
/***/ ((__unused_webpack_module, __unused_webpack_exports, __webpack_require__) => {

__webpack_require__(431)('Uint8', 1, function (init) {
  return function Uint8ClampedArray(data, byteOffset, length) {
    return init(this, data, byteOffset, length);
  };
}, true);

/***/ }),

/***/ 3491:
/***/ ((module, __unused_webpack_exports, __webpack_require__) => {

"use strict";


var global = __webpack_require__(7381);
var each = __webpack_require__(3970)(0);
var redefine = __webpack_require__(7278);
var meta = __webpack_require__(3763);
var assign = __webpack_require__(8559);
var weak = __webpack_require__(4495);
var isObject = __webpack_require__(7156);
var validate = __webpack_require__(8546);
var NATIVE_WEAK_MAP = __webpack_require__(8546);
var IS_IE11 = !global.ActiveXObject && 'ActiveXObject' in global;
var WEAK_MAP = 'WeakMap';
var getWeak = meta.getWeak;
var isExtensible = Object.isExtensible;
var uncaughtFrozenStore = weak.ufstore;
var InternalMap;
var wrapper = function wrapper(get) {
  return function WeakMap() {
    return get(this, arguments.length > 0 ? arguments[0] : undefined);
  };
};
var methods = {
  // 23.3.3.3 WeakMap.prototype.get(key)
  get: function get(key) {
    if (isObject(key)) {
      var data = getWeak(key);
      if (data === true) return uncaughtFrozenStore(validate(this, WEAK_MAP)).get(key);
      return data ? data[this._i] : undefined;
    }
  },
  // 23.3.3.5 WeakMap.prototype.set(key, value)
  set: function set(key, value) {
    return weak.def(validate(this, WEAK_MAP), key, value);
  }
};

// 23.3 WeakMap Objects
var $WeakMap = module.exports = __webpack_require__(1966)(WEAK_MAP, wrapper, methods, weak, true, true);

// IE11 WeakMap frozen keys fix
if (NATIVE_WEAK_MAP && IS_IE11) {
  InternalMap = weak.getConstructor(wrapper, WEAK_MAP);
  assign(InternalMap.prototype, methods);
  meta.NEED = true;
  each(['delete', 'has', 'get', 'set'], function (key) {
    var proto = $WeakMap.prototype;
    var method = proto[key];
    redefine(proto, key, function (a, b) {
      // store frozen objects on internal weakmap shim
      if (isObject(a) && !isExtensible(a)) {
        if (!this._f) this._f = new InternalMap();
        var result = this._f[key](a, b);
        return key == 'set' ? this : result;
        // store all the rest on native weakmap
      }
      return method.call(this, a, b);
    });
  });
}

/***/ }),

/***/ 6332:
/***/ ((__unused_webpack_module, __unused_webpack_exports, __webpack_require__) => {

"use strict";


var weak = __webpack_require__(4495);
var validate = __webpack_require__(8546);
var WEAK_SET = 'WeakSet';

// 23.4 WeakSet Objects
__webpack_require__(1966)(WEAK_SET, function (get) {
  return function WeakSet() {
    return get(this, arguments.length > 0 ? arguments[0] : undefined);
  };
}, {
  // 23.4.3.1 WeakSet.prototype.add(value)
  add: function add(value) {
    return weak.def(validate(this, WEAK_SET), value, true);
  }
}, weak, false, true);

/***/ }),

/***/ 6032:
/***/ ((__unused_webpack_module, __unused_webpack_exports, __webpack_require__) => {

"use strict";


// https://tc39.github.io/proposal-flatMap/#sec-Array.prototype.flatMap
var $export = __webpack_require__(5913);
var flattenIntoArray = __webpack_require__(3120);
var toObject = __webpack_require__(2515);
var toLength = __webpack_require__(8315);
var aFunction = __webpack_require__(6819);
var arraySpeciesCreate = __webpack_require__(5486);
$export($export.P, 'Array', {
  flatMap: function flatMap(callbackfn /* , thisArg */) {
    var O = toObject(this);
    var sourceLen, A;
    aFunction(callbackfn);
    sourceLen = toLength(O.length);
    A = arraySpeciesCreate(O, 0);
    flattenIntoArray(A, O, O, sourceLen, 0, 1, callbackfn, arguments[1]);
    return A;
  }
});
__webpack_require__(4339)('flatMap');

/***/ }),

/***/ 732:
/***/ ((__unused_webpack_module, __unused_webpack_exports, __webpack_require__) => {

"use strict";


// https://tc39.github.io/proposal-flatMap/#sec-Array.prototype.flatten
var $export = __webpack_require__(5913);
var flattenIntoArray = __webpack_require__(3120);
var toObject = __webpack_require__(2515);
var toLength = __webpack_require__(8315);
var toInteger = __webpack_require__(3230);
var arraySpeciesCreate = __webpack_require__(5486);
$export($export.P, 'Array', {
  flatten: function flatten( /* depthArg = 1 */
  ) {
    var depthArg = arguments[0];
    var O = toObject(this);
    var sourceLen = toLength(O.length);
    var A = arraySpeciesCreate(O, 0);
    flattenIntoArray(A, O, O, sourceLen, 0, depthArg === undefined ? 1 : toInteger(depthArg));
    return A;
  }
});
__webpack_require__(4339)('flatten');

/***/ }),

/***/ 2963:
/***/ ((__unused_webpack_module, __unused_webpack_exports, __webpack_require__) => {

"use strict";


// https://github.com/tc39/Array.prototype.includes
var $export = __webpack_require__(5913);
var $includes = __webpack_require__(4687)(true);
$export($export.P, 'Array', {
  includes: function includes(el /* , fromIndex = 0 */) {
    return $includes(this, el, arguments.length > 1 ? arguments[1] : undefined);
  }
});
__webpack_require__(4339)('includes');

/***/ }),

/***/ 6321:
/***/ ((__unused_webpack_module, __unused_webpack_exports, __webpack_require__) => {

// https://github.com/rwaldron/tc39-notes/blob/master/es6/2014-09/sept-25.md#510-globalasap-for-enqueuing-a-microtask
var $export = __webpack_require__(5913);
var microtask = __webpack_require__(1842)();
var process = (__webpack_require__(7381).process);
var isNode = __webpack_require__(3679)(process) == 'process';
$export($export.G, {
  asap: function asap(fn) {
    var domain = isNode && process.domain;
    microtask(domain ? domain.bind(fn) : fn);
  }
});

/***/ }),

/***/ 7469:
/***/ ((__unused_webpack_module, __unused_webpack_exports, __webpack_require__) => {

// https://github.com/ljharb/proposal-is-error
var $export = __webpack_require__(5913);
var cof = __webpack_require__(3679);
$export($export.S, 'Error', {
  isError: function isError(it) {
    return cof(it) === 'Error';
  }
});

/***/ }),

/***/ 6426:
/***/ ((__unused_webpack_module, __unused_webpack_exports, __webpack_require__) => {

// https://github.com/tc39/proposal-global
var $export = __webpack_require__(5913);
$export($export.G, {
  global: __webpack_require__(7381)
});

/***/ }),

/***/ 3591:
/***/ ((__unused_webpack_module, __unused_webpack_exports, __webpack_require__) => {

// https://tc39.github.io/proposal-setmap-offrom/#sec-map.from
__webpack_require__(7598)('Map');

/***/ }),

/***/ 9992:
/***/ ((__unused_webpack_module, __unused_webpack_exports, __webpack_require__) => {

// https://tc39.github.io/proposal-setmap-offrom/#sec-map.of
__webpack_require__(5329)('Map');

/***/ }),

/***/ 8455:
/***/ ((__unused_webpack_module, __unused_webpack_exports, __webpack_require__) => {

// https://github.com/DavidBruant/Map-Set.prototype.toJSON
var $export = __webpack_require__(5913);
$export($export.P + $export.R, 'Map', {
  toJSON: __webpack_require__(1872)('Map')
});

/***/ }),

/***/ 4097:
/***/ ((__unused_webpack_module, __unused_webpack_exports, __webpack_require__) => {

// https://rwaldron.github.io/proposal-math-extensions/
var $export = __webpack_require__(5913);
$export($export.S, 'Math', {
  clamp: function clamp(x, lower, upper) {
    return Math.min(upper, Math.max(lower, x));
  }
});

/***/ }),

/***/ 5813:
/***/ ((__unused_webpack_module, __unused_webpack_exports, __webpack_require__) => {

// https://rwaldron.github.io/proposal-math-extensions/
var $export = __webpack_require__(5913);
$export($export.S, 'Math', {
  DEG_PER_RAD: Math.PI / 180
});

/***/ }),

/***/ 7245:
/***/ ((__unused_webpack_module, __unused_webpack_exports, __webpack_require__) => {

// https://rwaldron.github.io/proposal-math-extensions/
var $export = __webpack_require__(5913);
var RAD_PER_DEG = 180 / Math.PI;
$export($export.S, 'Math', {
  degrees: function degrees(radians) {
    return radians * RAD_PER_DEG;
  }
});

/***/ }),

/***/ 6756:
/***/ ((__unused_webpack_module, __unused_webpack_exports, __webpack_require__) => {

// https://rwaldron.github.io/proposal-math-extensions/
var $export = __webpack_require__(5913);
var scale = __webpack_require__(8124);
var fround = __webpack_require__(3800);
$export($export.S, 'Math', {
  fscale: function fscale(x, inLow, inHigh, outLow, outHigh) {
    return fround(scale(x, inLow, inHigh, outLow, outHigh));
  }
});

/***/ }),

/***/ 8392:
/***/ ((__unused_webpack_module, __unused_webpack_exports, __webpack_require__) => {

// https://gist.github.com/BrendanEich/4294d5c212a6d2254703
var $export = __webpack_require__(5913);
$export($export.S, 'Math', {
  iaddh: function iaddh(x0, x1, y0, y1) {
    var $x0 = x0 >>> 0;
    var $x1 = x1 >>> 0;
    var $y0 = y0 >>> 0;
    return $x1 + (y1 >>> 0) + (($x0 & $y0 | ($x0 | $y0) & ~($x0 + $y0 >>> 0)) >>> 31) | 0;
  }
});

/***/ }),

/***/ 3735:
/***/ ((__unused_webpack_module, __unused_webpack_exports, __webpack_require__) => {

// https://gist.github.com/BrendanEich/4294d5c212a6d2254703
var $export = __webpack_require__(5913);
$export($export.S, 'Math', {
  imulh: function imulh(u, v) {
    var UINT16 = 0xffff;
    var $u = +u;
    var $v = +v;
    var u0 = $u & UINT16;
    var v0 = $v & UINT16;
    var u1 = $u >> 16;
    var v1 = $v >> 16;
    var t = (u1 * v0 >>> 0) + (u0 * v0 >>> 16);
    return u1 * v1 + (t >> 16) + ((u0 * v1 >>> 0) + (t & UINT16) >> 16);
  }
});

/***/ }),

/***/ 1111:
/***/ ((__unused_webpack_module, __unused_webpack_exports, __webpack_require__) => {

// https://gist.github.com/BrendanEich/4294d5c212a6d2254703
var $export = __webpack_require__(5913);
$export($export.S, 'Math', {
  isubh: function isubh(x0, x1, y0, y1) {
    var $x0 = x0 >>> 0;
    var $x1 = x1 >>> 0;
    var $y0 = y0 >>> 0;
    return $x1 - (y1 >>> 0) - ((~$x0 & $y0 | ~($x0 ^ $y0) & $x0 - $y0 >>> 0) >>> 31) | 0;
  }
});

/***/ }),

/***/ 3037:
/***/ ((__unused_webpack_module, __unused_webpack_exports, __webpack_require__) => {

// https://rwaldron.github.io/proposal-math-extensions/
var $export = __webpack_require__(5913);
$export($export.S, 'Math', {
  RAD_PER_DEG: 180 / Math.PI
});

/***/ }),

/***/ 8422:
/***/ ((__unused_webpack_module, __unused_webpack_exports, __webpack_require__) => {

// https://rwaldron.github.io/proposal-math-extensions/
var $export = __webpack_require__(5913);
var DEG_PER_RAD = Math.PI / 180;
$export($export.S, 'Math', {
  radians: function radians(degrees) {
    return degrees * DEG_PER_RAD;
  }
});

/***/ }),

/***/ 1818:
/***/ ((__unused_webpack_module, __unused_webpack_exports, __webpack_require__) => {

// https://rwaldron.github.io/proposal-math-extensions/
var $export = __webpack_require__(5913);
$export($export.S, 'Math', {
  scale: __webpack_require__(8124)
});

/***/ }),

/***/ 7371:
/***/ ((__unused_webpack_module, __unused_webpack_exports, __webpack_require__) => {

// http://jfbastien.github.io/papers/Math.signbit.html
var $export = __webpack_require__(5913);
$export($export.S, 'Math', {
  signbit: function signbit(x) {
    // eslint-disable-next-line no-self-compare
    return (x = +x) != x ? x : x == 0 ? 1 / x == Infinity : x > 0;
  }
});

/***/ }),

/***/ 7883:
/***/ ((__unused_webpack_module, __unused_webpack_exports, __webpack_require__) => {

// https://gist.github.com/BrendanEich/4294d5c212a6d2254703
var $export = __webpack_require__(5913);
$export($export.S, 'Math', {
  umulh: function umulh(u, v) {
    var UINT16 = 0xffff;
    var $u = +u;
    var $v = +v;
    var u0 = $u & UINT16;
    var v0 = $v & UINT16;
    var u1 = $u >>> 16;
    var v1 = $v >>> 16;
    var t = (u1 * v0 >>> 0) + (u0 * v0 >>> 16);
    return u1 * v1 + (t >>> 16) + ((u0 * v1 >>> 0) + (t & UINT16) >>> 16);
  }
});

/***/ }),

/***/ 6792:
/***/ ((__unused_webpack_module, __unused_webpack_exports, __webpack_require__) => {

"use strict";


var $export = __webpack_require__(5913);
var toObject = __webpack_require__(2515);
var aFunction = __webpack_require__(6819);
var $defineProperty = __webpack_require__(4835);

// B.2.2.2 Object.prototype.__defineGetter__(P, getter)
__webpack_require__(4926) && $export($export.P + __webpack_require__(8249), 'Object', {
  __defineGetter__: function __defineGetter__(P, getter) {
    $defineProperty.f(toObject(this), P, {
      get: aFunction(getter),
      enumerable: true,
      configurable: true
    });
  }
});

/***/ }),

/***/ 88:
/***/ ((__unused_webpack_module, __unused_webpack_exports, __webpack_require__) => {

"use strict";


var $export = __webpack_require__(5913);
var toObject = __webpack_require__(2515);
var aFunction = __webpack_require__(6819);
var $defineProperty = __webpack_require__(4835);

// B.2.2.3 Object.prototype.__defineSetter__(P, setter)
__webpack_require__(4926) && $export($export.P + __webpack_require__(8249), 'Object', {
  __defineSetter__: function __defineSetter__(P, setter) {
    $defineProperty.f(toObject(this), P, {
      set: aFunction(setter),
      enumerable: true,
      configurable: true
    });
  }
});

/***/ }),

/***/ 8217:
/***/ ((__unused_webpack_module, __unused_webpack_exports, __webpack_require__) => {

// https://github.com/tc39/proposal-object-values-entries
var $export = __webpack_require__(5913);
var $entries = __webpack_require__(8941)(true);
$export($export.S, 'Object', {
  entries: function entries(it) {
    return $entries(it);
  }
});

/***/ }),

/***/ 9168:
/***/ ((__unused_webpack_module, __unused_webpack_exports, __webpack_require__) => {

// https://github.com/tc39/proposal-object-getownpropertydescriptors
var $export = __webpack_require__(5913);
var ownKeys = __webpack_require__(2600);
var toIObject = __webpack_require__(8499);
var gOPD = __webpack_require__(3299);
var createProperty = __webpack_require__(1348);
$export($export.S, 'Object', {
  getOwnPropertyDescriptors: function getOwnPropertyDescriptors(object) {
    var O = toIObject(object);
    var getDesc = gOPD.f;
    var keys = ownKeys(O);
    var result = {};
    var i = 0;
    var key, desc;
    while (keys.length > i) {
      desc = getDesc(O, key = keys[i++]);
      if (desc !== undefined) createProperty(result, key, desc);
    }
    return result;
  }
});

/***/ }),

/***/ 2095:
/***/ ((__unused_webpack_module, __unused_webpack_exports, __webpack_require__) => {

"use strict";


var $export = __webpack_require__(5913);
var toObject = __webpack_require__(2515);
var toPrimitive = __webpack_require__(8537);
var getPrototypeOf = __webpack_require__(4153);
var getOwnPropertyDescriptor = (__webpack_require__(3299).f);

// B.2.2.4 Object.prototype.__lookupGetter__(P)
__webpack_require__(4926) && $export($export.P + __webpack_require__(8249), 'Object', {
  __lookupGetter__: function __lookupGetter__(P) {
    var O = toObject(this);
    var K = toPrimitive(P, true);
    var D;
    do {
      if (D = getOwnPropertyDescriptor(O, K)) return D.get;
    } while (O = getPrototypeOf(O));
  }
});

/***/ }),

/***/ 2889:
/***/ ((__unused_webpack_module, __unused_webpack_exports, __webpack_require__) => {

"use strict";


var $export = __webpack_require__(5913);
var toObject = __webpack_require__(2515);
var toPrimitive = __webpack_require__(8537);
var getPrototypeOf = __webpack_require__(4153);
var getOwnPropertyDescriptor = (__webpack_require__(3299).f);

// B.2.2.5 Object.prototype.__lookupSetter__(P)
__webpack_require__(4926) && $export($export.P + __webpack_require__(8249), 'Object', {
  __lookupSetter__: function __lookupSetter__(P) {
    var O = toObject(this);
    var K = toPrimitive(P, true);
    var D;
    do {
      if (D = getOwnPropertyDescriptor(O, K)) return D.set;
    } while (O = getPrototypeOf(O));
  }
});

/***/ }),

/***/ 6351:
/***/ ((__unused_webpack_module, __unused_webpack_exports, __webpack_require__) => {

// https://github.com/tc39/proposal-object-values-entries
var $export = __webpack_require__(5913);
var $values = __webpack_require__(8941)(false);
$export($export.S, 'Object', {
  values: function values(it) {
    return $values(it);
  }
});

/***/ }),

/***/ 5613:
/***/ ((__unused_webpack_module, __unused_webpack_exports, __webpack_require__) => {

"use strict";


// https://github.com/zenparsing/es-observable
var $export = __webpack_require__(5913);
var global = __webpack_require__(7381);
var core = __webpack_require__(8544);
var microtask = __webpack_require__(1842)();
var OBSERVABLE = __webpack_require__(3336)('observable');
var aFunction = __webpack_require__(6819);
var anObject = __webpack_require__(6154);
var anInstance = __webpack_require__(2702);
var redefineAll = __webpack_require__(7228);
var hide = __webpack_require__(8012);
var forOf = __webpack_require__(2734);
var RETURN = forOf.RETURN;
var getMethod = function getMethod(fn) {
  return fn == null ? undefined : aFunction(fn);
};
var cleanupSubscription = function cleanupSubscription(subscription) {
  var cleanup = subscription._c;
  if (cleanup) {
    subscription._c = undefined;
    cleanup();
  }
};
var subscriptionClosed = function subscriptionClosed(subscription) {
  return subscription._o === undefined;
};
var closeSubscription = function closeSubscription(subscription) {
  if (!subscriptionClosed(subscription)) {
    subscription._o = undefined;
    cleanupSubscription(subscription);
  }
};
var Subscription = function Subscription(observer, subscriber) {
  anObject(observer);
  this._c = undefined;
  this._o = observer;
  observer = new SubscriptionObserver(this);
  try {
    var cleanup = subscriber(observer);
    var subscription = cleanup;
    if (cleanup != null) {
      if (typeof cleanup.unsubscribe === 'function') cleanup = function cleanup() {
        subscription.unsubscribe();
      };else aFunction(cleanup);
      this._c = cleanup;
    }
  } catch (e) {
    observer.error(e);
    return;
  }
  if (subscriptionClosed(this)) cleanupSubscription(this);
};
Subscription.prototype = redefineAll({}, {
  unsubscribe: function unsubscribe() {
    closeSubscription(this);
  }
});
var SubscriptionObserver = function SubscriptionObserver(subscription) {
  this._s = subscription;
};
SubscriptionObserver.prototype = redefineAll({}, {
  next: function next(value) {
    var subscription = this._s;
    if (!subscriptionClosed(subscription)) {
      var observer = subscription._o;
      try {
        var m = getMethod(observer.next);
        if (m) return m.call(observer, value);
      } catch (e) {
        try {
          closeSubscription(subscription);
        } finally {
          throw e;
        }
      }
    }
  },
  error: function error(value) {
    var subscription = this._s;
    if (subscriptionClosed(subscription)) throw value;
    var observer = subscription._o;
    subscription._o = undefined;
    try {
      var m = getMethod(observer.error);
      if (!m) throw value;
      value = m.call(observer, value);
    } catch (e) {
      try {
        cleanupSubscription(subscription);
      } finally {
        throw e;
      }
    }
    cleanupSubscription(subscription);
    return value;
  },
  complete: function complete(value) {
    var subscription = this._s;
    if (!subscriptionClosed(subscription)) {
      var observer = subscription._o;
      subscription._o = undefined;
      try {
        var m = getMethod(observer.complete);
        value = m ? m.call(observer, value) : undefined;
      } catch (e) {
        try {
          cleanupSubscription(subscription);
        } finally {
          throw e;
        }
      }
      cleanupSubscription(subscription);
      return value;
    }
  }
});
var $Observable = function Observable(subscriber) {
  anInstance(this, $Observable, 'Observable', '_f')._f = aFunction(subscriber);
};
redefineAll($Observable.prototype, {
  subscribe: function subscribe(observer) {
    return new Subscription(observer, this._f);
  },
  forEach: function forEach(fn) {
    var that = this;
    return new (core.Promise || global.Promise)(function (resolve, reject) {
      aFunction(fn);
      var subscription = that.subscribe({
        next: function next(value) {
          try {
            return fn(value);
          } catch (e) {
            reject(e);
            subscription.unsubscribe();
          }
        },
        error: reject,
        complete: resolve
      });
    });
  }
});
redefineAll($Observable, {
  from: function from(x) {
    var C = typeof this === 'function' ? this : $Observable;
    var method = getMethod(anObject(x)[OBSERVABLE]);
    if (method) {
      var observable = anObject(method.call(x));
      return observable.constructor === C ? observable : new C(function (observer) {
        return observable.subscribe(observer);
      });
    }
    return new C(function (observer) {
      var done = false;
      microtask(function () {
        if (!done) {
          try {
            if (forOf(x, false, function (it) {
              observer.next(it);
              if (done) return RETURN;
            }) === RETURN) return;
          } catch (e) {
            if (done) throw e;
            observer.error(e);
            return;
          }
          observer.complete();
        }
      });
      return function () {
        done = true;
      };
    });
  },
  of: function of() {
    for (var i = 0, l = arguments.length, items = new Array(l); i < l;) {
      items[i] = arguments[i++];
    }
    return new (typeof this === 'function' ? this : $Observable)(function (observer) {
      var done = false;
      microtask(function () {
        if (!done) {
          for (var j = 0; j < items.length; ++j) {
            observer.next(items[j]);
            if (done) return;
          }
          observer.complete();
        }
      });
      return function () {
        done = true;
      };
    });
  }
});
hide($Observable.prototype, OBSERVABLE, function () {
  return this;
});
$export($export.G, {
  Observable: $Observable
});
__webpack_require__(4798)('Observable');

/***/ }),

/***/ 8088:
/***/ ((__unused_webpack_module, __unused_webpack_exports, __webpack_require__) => {

"use strict";
// https://github.com/tc39/proposal-promise-finally


var $export = __webpack_require__(5913);
var core = __webpack_require__(8544);
var global = __webpack_require__(7381);
var speciesConstructor = __webpack_require__(2035);
var promiseResolve = __webpack_require__(3507);
$export($export.P + $export.R, 'Promise', {
  'finally': function _finally(onFinally) {
    var C = speciesConstructor(this, core.Promise || global.Promise);
    var isFunction = typeof onFinally == 'function';
    return this.then(isFunction ? function (x) {
      return promiseResolve(C, onFinally()).then(function () {
        return x;
      });
    } : onFinally, isFunction ? function (e) {
      return promiseResolve(C, onFinally()).then(function () {
        throw e;
      });
    } : onFinally);
  }
});

/***/ }),

/***/ 5414:
/***/ ((__unused_webpack_module, __unused_webpack_exports, __webpack_require__) => {

"use strict";


// https://github.com/tc39/proposal-promise-try
var $export = __webpack_require__(5913);
var newPromiseCapability = __webpack_require__(4086);
var perform = __webpack_require__(8228);
$export($export.S, 'Promise', {
  'try': function _try(callbackfn) {
    var promiseCapability = newPromiseCapability.f(this);
    var result = perform(callbackfn);
    (result.e ? promiseCapability.reject : promiseCapability.resolve)(result.v);
    return promiseCapability.promise;
  }
});

/***/ }),

/***/ 2812:
/***/ ((__unused_webpack_module, __unused_webpack_exports, __webpack_require__) => {

var metadata = __webpack_require__(8953);
var anObject = __webpack_require__(6154);
var toMetaKey = metadata.key;
var ordinaryDefineOwnMetadata = metadata.set;
metadata.exp({
  defineMetadata: function defineMetadata(metadataKey, metadataValue, target, targetKey) {
    ordinaryDefineOwnMetadata(metadataKey, metadataValue, anObject(target), toMetaKey(targetKey));
  }
});

/***/ }),

/***/ 2835:
/***/ ((__unused_webpack_module, __unused_webpack_exports, __webpack_require__) => {

var metadata = __webpack_require__(8953);
var anObject = __webpack_require__(6154);
var toMetaKey = metadata.key;
var getOrCreateMetadataMap = metadata.map;
var store = metadata.store;
metadata.exp({
  deleteMetadata: function deleteMetadata(metadataKey, target /* , targetKey */) {
    var targetKey = arguments.length < 3 ? undefined : toMetaKey(arguments[2]);
    var metadataMap = getOrCreateMetadataMap(anObject(target), targetKey, false);
    if (metadataMap === undefined || !metadataMap['delete'](metadataKey)) return false;
    if (metadataMap.size) return true;
    var targetMetadata = store.get(target);
    targetMetadata['delete'](targetKey);
    return !!targetMetadata.size || store['delete'](target);
  }
});

/***/ }),

/***/ 710:
/***/ ((__unused_webpack_module, __unused_webpack_exports, __webpack_require__) => {

var Set = __webpack_require__(3940);
var from = __webpack_require__(5273);
var metadata = __webpack_require__(8953);
var anObject = __webpack_require__(6154);
var getPrototypeOf = __webpack_require__(4153);
var ordinaryOwnMetadataKeys = metadata.keys;
var toMetaKey = metadata.key;
var ordinaryMetadataKeys = function ordinaryMetadataKeys(O, P) {
  var oKeys = ordinaryOwnMetadataKeys(O, P);
  var parent = getPrototypeOf(O);
  if (parent === null) return oKeys;
  var pKeys = ordinaryMetadataKeys(parent, P);
  return pKeys.length ? oKeys.length ? from(new Set(oKeys.concat(pKeys))) : pKeys : oKeys;
};
metadata.exp({
  getMetadataKeys: function getMetadataKeys(target /* , targetKey */) {
    return ordinaryMetadataKeys(anObject(target), arguments.length < 2 ? undefined : toMetaKey(arguments[1]));
  }
});

/***/ }),

/***/ 7415:
/***/ ((__unused_webpack_module, __unused_webpack_exports, __webpack_require__) => {

var metadata = __webpack_require__(8953);
var anObject = __webpack_require__(6154);
var getPrototypeOf = __webpack_require__(4153);
var ordinaryHasOwnMetadata = metadata.has;
var ordinaryGetOwnMetadata = metadata.get;
var toMetaKey = metadata.key;
var ordinaryGetMetadata = function ordinaryGetMetadata(MetadataKey, O, P) {
  var hasOwn = ordinaryHasOwnMetadata(MetadataKey, O, P);
  if (hasOwn) return ordinaryGetOwnMetadata(MetadataKey, O, P);
  var parent = getPrototypeOf(O);
  return parent !== null ? ordinaryGetMetadata(MetadataKey, parent, P) : undefined;
};
metadata.exp({
  getMetadata: function getMetadata(metadataKey, target /* , targetKey */) {
    return ordinaryGetMetadata(metadataKey, anObject(target), arguments.length < 3 ? undefined : toMetaKey(arguments[2]));
  }
});

/***/ }),

/***/ 60:
/***/ ((__unused_webpack_module, __unused_webpack_exports, __webpack_require__) => {

var metadata = __webpack_require__(8953);
var anObject = __webpack_require__(6154);
var ordinaryOwnMetadataKeys = metadata.keys;
var toMetaKey = metadata.key;
metadata.exp({
  getOwnMetadataKeys: function getOwnMetadataKeys(target /* , targetKey */) {
    return ordinaryOwnMetadataKeys(anObject(target), arguments.length < 2 ? undefined : toMetaKey(arguments[1]));
  }
});

/***/ }),

/***/ 3666:
/***/ ((__unused_webpack_module, __unused_webpack_exports, __webpack_require__) => {

var metadata = __webpack_require__(8953);
var anObject = __webpack_require__(6154);
var ordinaryGetOwnMetadata = metadata.get;
var toMetaKey = metadata.key;
metadata.exp({
  getOwnMetadata: function getOwnMetadata(metadataKey, target /* , targetKey */) {
    return ordinaryGetOwnMetadata(metadataKey, anObject(target), arguments.length < 3 ? undefined : toMetaKey(arguments[2]));
  }
});

/***/ }),

/***/ 7216:
/***/ ((__unused_webpack_module, __unused_webpack_exports, __webpack_require__) => {

var metadata = __webpack_require__(8953);
var anObject = __webpack_require__(6154);
var getPrototypeOf = __webpack_require__(4153);
var ordinaryHasOwnMetadata = metadata.has;
var toMetaKey = metadata.key;
var ordinaryHasMetadata = function ordinaryHasMetadata(MetadataKey, O, P) {
  var hasOwn = ordinaryHasOwnMetadata(MetadataKey, O, P);
  if (hasOwn) return true;
  var parent = getPrototypeOf(O);
  return parent !== null ? ordinaryHasMetadata(MetadataKey, parent, P) : false;
};
metadata.exp({
  hasMetadata: function hasMetadata(metadataKey, target /* , targetKey */) {
    return ordinaryHasMetadata(metadataKey, anObject(target), arguments.length < 3 ? undefined : toMetaKey(arguments[2]));
  }
});

/***/ }),

/***/ 3470:
/***/ ((__unused_webpack_module, __unused_webpack_exports, __webpack_require__) => {

var metadata = __webpack_require__(8953);
var anObject = __webpack_require__(6154);
var ordinaryHasOwnMetadata = metadata.has;
var toMetaKey = metadata.key;
metadata.exp({
  hasOwnMetadata: function hasOwnMetadata(metadataKey, target /* , targetKey */) {
    return ordinaryHasOwnMetadata(metadataKey, anObject(target), arguments.length < 3 ? undefined : toMetaKey(arguments[2]));
  }
});

/***/ }),

/***/ 2161:
/***/ ((__unused_webpack_module, __unused_webpack_exports, __webpack_require__) => {

var $metadata = __webpack_require__(8953);
var anObject = __webpack_require__(6154);
var aFunction = __webpack_require__(6819);
var toMetaKey = $metadata.key;
var ordinaryDefineOwnMetadata = $metadata.set;
$metadata.exp({
  metadata: function metadata(metadataKey, metadataValue) {
    return function decorator(target, targetKey) {
      ordinaryDefineOwnMetadata(metadataKey, metadataValue, (targetKey !== undefined ? anObject : aFunction)(target), toMetaKey(targetKey));
    };
  }
});

/***/ }),

/***/ 922:
/***/ ((__unused_webpack_module, __unused_webpack_exports, __webpack_require__) => {

// https://tc39.github.io/proposal-setmap-offrom/#sec-set.from
__webpack_require__(7598)('Set');

/***/ }),

/***/ 3798:
/***/ ((__unused_webpack_module, __unused_webpack_exports, __webpack_require__) => {

// https://tc39.github.io/proposal-setmap-offrom/#sec-set.of
__webpack_require__(5329)('Set');

/***/ }),

/***/ 188:
/***/ ((__unused_webpack_module, __unused_webpack_exports, __webpack_require__) => {

// https://github.com/DavidBruant/Map-Set.prototype.toJSON
var $export = __webpack_require__(5913);
$export($export.P + $export.R, 'Set', {
  toJSON: __webpack_require__(1872)('Set')
});

/***/ }),

/***/ 6696:
/***/ ((__unused_webpack_module, __unused_webpack_exports, __webpack_require__) => {

"use strict";


// https://github.com/mathiasbynens/String.prototype.at
var $export = __webpack_require__(5913);
var $at = __webpack_require__(3593)(true);
var $fails = __webpack_require__(5810);
var FORCED = $fails(function () {
  return '𠮷'.at(0) !== '𠮷';
});
$export($export.P + $export.F * FORCED, 'String', {
  at: function at(pos) {
    return $at(this, pos);
  }
});

/***/ }),

/***/ 7593:
/***/ ((__unused_webpack_module, __unused_webpack_exports, __webpack_require__) => {

"use strict";


// https://tc39.github.io/String.prototype.matchAll/
var $export = __webpack_require__(5913);
var defined = __webpack_require__(408);
var toLength = __webpack_require__(8315);
var isRegExp = __webpack_require__(1993);
var getFlags = __webpack_require__(2188);
var RegExpProto = RegExp.prototype;
var $RegExpStringIterator = function $RegExpStringIterator(regexp, string) {
  this._r = regexp;
  this._s = string;
};
__webpack_require__(8258)($RegExpStringIterator, 'RegExp String', function next() {
  var match = this._r.exec(this._s);
  return {
    value: match,
    done: match === null
  };
});
$export($export.P, 'String', {
  matchAll: function matchAll(regexp) {
    defined(this);
    if (!isRegExp(regexp)) throw TypeError(regexp + ' is not a regexp!');
    var S = String(this);
    var flags = 'flags' in RegExpProto ? String(regexp.flags) : getFlags.call(regexp);
    var rx = new RegExp(regexp.source, ~flags.indexOf('g') ? flags : 'g' + flags);
    rx.lastIndex = toLength(regexp.lastIndex);
    return new $RegExpStringIterator(rx, S);
  }
});

/***/ }),

/***/ 2123:
/***/ ((__unused_webpack_module, __unused_webpack_exports, __webpack_require__) => {

"use strict";


// https://github.com/tc39/proposal-string-pad-start-end
var $export = __webpack_require__(5913);
var $pad = __webpack_require__(1925);
var userAgent = __webpack_require__(851);

// https://github.com/zloirock/core-js/issues/280
var WEBKIT_BUG = /Version\/10\.\d+(\.\d+)?( Mobile\/\w+)? Safari\//.test(userAgent);
$export($export.P + $export.F * WEBKIT_BUG, 'String', {
  padEnd: function padEnd(maxLength /* , fillString = ' ' */) {
    return $pad(this, maxLength, arguments.length > 1 ? arguments[1] : undefined, false);
  }
});

/***/ }),

/***/ 9391:
/***/ ((__unused_webpack_module, __unused_webpack_exports, __webpack_require__) => {

"use strict";


// https://github.com/tc39/proposal-string-pad-start-end
var $export = __webpack_require__(5913);
var $pad = __webpack_require__(1925);
var userAgent = __webpack_require__(851);

// https://github.com/zloirock/core-js/issues/280
var WEBKIT_BUG = /Version\/10\.\d+(\.\d+)?( Mobile\/\w+)? Safari\//.test(userAgent);
$export($export.P + $export.F * WEBKIT_BUG, 'String', {
  padStart: function padStart(maxLength /* , fillString = ' ' */) {
    return $pad(this, maxLength, arguments.length > 1 ? arguments[1] : undefined, true);
  }
});

/***/ }),

/***/ 6541:
/***/ ((__unused_webpack_module, __unused_webpack_exports, __webpack_require__) => {

"use strict";


// https://github.com/sebmarkbage/ecmascript-string-left-right-trim
__webpack_require__(618)('trimLeft', function ($trim) {
  return function trimLeft() {
    return $trim(this, 1);
  };
}, 'trimStart');

/***/ }),

/***/ 1767:
/***/ ((__unused_webpack_module, __unused_webpack_exports, __webpack_require__) => {

"use strict";


// https://github.com/sebmarkbage/ecmascript-string-left-right-trim
__webpack_require__(618)('trimRight', function ($trim) {
  return function trimRight() {
    return $trim(this, 2);
  };
}, 'trimEnd');

/***/ }),

/***/ 4870:
/***/ ((__unused_webpack_module, __unused_webpack_exports, __webpack_require__) => {

__webpack_require__(5721)('asyncIterator');

/***/ }),

/***/ 7937:
/***/ ((__unused_webpack_module, __unused_webpack_exports, __webpack_require__) => {

__webpack_require__(5721)('observable');

/***/ }),

/***/ 3884:
/***/ ((__unused_webpack_module, __unused_webpack_exports, __webpack_require__) => {

// https://github.com/tc39/proposal-global
var $export = __webpack_require__(5913);
$export($export.S, 'System', {
  global: __webpack_require__(7381)
});

/***/ }),

/***/ 2177:
/***/ ((__unused_webpack_module, __unused_webpack_exports, __webpack_require__) => {

// https://tc39.github.io/proposal-setmap-offrom/#sec-weakmap.from
__webpack_require__(7598)('WeakMap');

/***/ }),

/***/ 9737:
/***/ ((__unused_webpack_module, __unused_webpack_exports, __webpack_require__) => {

// https://tc39.github.io/proposal-setmap-offrom/#sec-weakmap.of
__webpack_require__(5329)('WeakMap');

/***/ }),

/***/ 8791:
/***/ ((__unused_webpack_module, __unused_webpack_exports, __webpack_require__) => {

// https://tc39.github.io/proposal-setmap-offrom/#sec-weakset.from
__webpack_require__(7598)('WeakSet');

/***/ }),

/***/ 5704:
/***/ ((__unused_webpack_module, __unused_webpack_exports, __webpack_require__) => {

// https://tc39.github.io/proposal-setmap-offrom/#sec-weakset.of
__webpack_require__(5329)('WeakSet');

/***/ }),

/***/ 1094:
/***/ ((__unused_webpack_module, __unused_webpack_exports, __webpack_require__) => {

var $iterators = __webpack_require__(4806);
var getKeys = __webpack_require__(9924);
var redefine = __webpack_require__(7278);
var global = __webpack_require__(7381);
var hide = __webpack_require__(8012);
var Iterators = __webpack_require__(5301);
var wks = __webpack_require__(3336);
var ITERATOR = wks('iterator');
var TO_STRING_TAG = wks('toStringTag');
var ArrayValues = Iterators.Array;
var DOMIterables = {
  CSSRuleList: true,
  // TODO: Not spec compliant, should be false.
  CSSStyleDeclaration: false,
  CSSValueList: false,
  ClientRectList: false,
  DOMRectList: false,
  DOMStringList: false,
  DOMTokenList: true,
  DataTransferItemList: false,
  FileList: false,
  HTMLAllCollection: false,
  HTMLCollection: false,
  HTMLFormElement: false,
  HTMLSelectElement: false,
  MediaList: true,
  // TODO: Not spec compliant, should be false.
  MimeTypeArray: false,
  NamedNodeMap: false,
  NodeList: true,
  PaintRequestList: false,
  Plugin: false,
  PluginArray: false,
  SVGLengthList: false,
  SVGNumberList: false,
  SVGPathSegList: false,
  SVGPointList: false,
  SVGStringList: false,
  SVGTransformList: false,
  SourceBufferList: false,
  StyleSheetList: true,
  // TODO: Not spec compliant, should be false.
  TextTrackCueList: false,
  TextTrackList: false,
  TouchList: false
};
for (var collections = getKeys(DOMIterables), i = 0; i < collections.length; i++) {
  var NAME = collections[i];
  var explicit = DOMIterables[NAME];
  var Collection = global[NAME];
  var proto = Collection && Collection.prototype;
  var key;
  if (proto) {
    if (!proto[ITERATOR]) hide(proto, ITERATOR, ArrayValues);
    if (!proto[TO_STRING_TAG]) hide(proto, TO_STRING_TAG, NAME);
    Iterators[NAME] = ArrayValues;
    if (explicit) for (key in $iterators) {
      if (!proto[key]) redefine(proto, key, $iterators[key], true);
    }
  }
}

/***/ }),

/***/ 1605:
/***/ ((__unused_webpack_module, __unused_webpack_exports, __webpack_require__) => {

var $export = __webpack_require__(5913);
var $task = __webpack_require__(8220);
$export($export.G + $export.B, {
  setImmediate: $task.set,
  clearImmediate: $task.clear
});

/***/ }),

/***/ 2113:
/***/ ((__unused_webpack_module, __unused_webpack_exports, __webpack_require__) => {

// ie9- setTimeout & setInterval additional parameters fix
var global = __webpack_require__(7381);
var $export = __webpack_require__(5913);
var userAgent = __webpack_require__(851);
var slice = [].slice;
var MSIE = /MSIE .\./.test(userAgent); // <- dirty ie9- check
var wrap = function wrap(set) {
  return function (fn, time /* , ...args */) {
    var boundArgs = arguments.length > 2;
    var args = boundArgs ? slice.call(arguments, 2) : false;
    return set(boundArgs ? function () {
      // eslint-disable-next-line no-new-func
      (typeof fn == 'function' ? fn : Function(fn)).apply(this, args);
    } : fn, time);
  };
};
$export($export.G + $export.B + $export.F * MSIE, {
  setTimeout: wrap(global.setTimeout),
  setInterval: wrap(global.setInterval)
});

/***/ }),

/***/ 2234:
/***/ ((module, __unused_webpack_exports, __webpack_require__) => {

__webpack_require__(2403);
__webpack_require__(3290);
__webpack_require__(3690);
__webpack_require__(8424);
__webpack_require__(2357);
__webpack_require__(6667);
__webpack_require__(2506);
__webpack_require__(6022);
__webpack_require__(754);
__webpack_require__(7571);
__webpack_require__(6527);
__webpack_require__(9219);
__webpack_require__(3270);
__webpack_require__(4919);
__webpack_require__(5331);
__webpack_require__(2456);
__webpack_require__(8490);
__webpack_require__(4554);
__webpack_require__(161);
__webpack_require__(6042);
__webpack_require__(15);
__webpack_require__(317);
__webpack_require__(3271);
__webpack_require__(440);
__webpack_require__(1077);
__webpack_require__(820);
__webpack_require__(1914);
__webpack_require__(4117);
__webpack_require__(9619);
__webpack_require__(5849);
__webpack_require__(4750);
__webpack_require__(1550);
__webpack_require__(3529);
__webpack_require__(2791);
__webpack_require__(6831);
__webpack_require__(4717);
__webpack_require__(7292);
__webpack_require__(1840);
__webpack_require__(3255);
__webpack_require__(5728);
__webpack_require__(6255);
__webpack_require__(2834);
__webpack_require__(4489);
__webpack_require__(575);
__webpack_require__(1369);
__webpack_require__(2751);
__webpack_require__(9617);
__webpack_require__(3656);
__webpack_require__(1850);
__webpack_require__(5424);
__webpack_require__(230);
__webpack_require__(8471);
__webpack_require__(8577);
__webpack_require__(7906);
__webpack_require__(8587);
__webpack_require__(6575);
__webpack_require__(5281);
__webpack_require__(3917);
__webpack_require__(5450);
__webpack_require__(9449);
__webpack_require__(1616);
__webpack_require__(9718);
__webpack_require__(3845);
__webpack_require__(5803);
__webpack_require__(2222);
__webpack_require__(5036);
__webpack_require__(6131);
__webpack_require__(4110);
__webpack_require__(6235);
__webpack_require__(6495);
__webpack_require__(4162);
__webpack_require__(5297);
__webpack_require__(1466);
__webpack_require__(2581);
__webpack_require__(8384);
__webpack_require__(2334);
__webpack_require__(9701);
__webpack_require__(1325);
__webpack_require__(3233);
__webpack_require__(1621);
__webpack_require__(8671);
__webpack_require__(6705);
__webpack_require__(9437);
__webpack_require__(7263);
__webpack_require__(919);
__webpack_require__(791);
__webpack_require__(633);
__webpack_require__(9355);
__webpack_require__(9253);
__webpack_require__(9892);
__webpack_require__(9121);
__webpack_require__(8738);
__webpack_require__(4751);
__webpack_require__(9822);
__webpack_require__(4611);
__webpack_require__(9217);
__webpack_require__(4138);
__webpack_require__(109);
__webpack_require__(3821);
__webpack_require__(4806);
__webpack_require__(2566);
__webpack_require__(5997);
__webpack_require__(8359);
__webpack_require__(7181);
__webpack_require__(8682);
__webpack_require__(8514);
__webpack_require__(5105);
__webpack_require__(5325);
__webpack_require__(829);
__webpack_require__(8969);
__webpack_require__(3940);
__webpack_require__(3491);
__webpack_require__(6332);
__webpack_require__(7195);
__webpack_require__(5345);
__webpack_require__(6670);
__webpack_require__(7736);
__webpack_require__(4457);
__webpack_require__(7683);
__webpack_require__(1123);
__webpack_require__(4797);
__webpack_require__(4871);
__webpack_require__(8824);
__webpack_require__(6472);
__webpack_require__(1220);
__webpack_require__(9263);
__webpack_require__(7622);
__webpack_require__(9060);
__webpack_require__(980);
__webpack_require__(6175);
__webpack_require__(8484);
__webpack_require__(9869);
__webpack_require__(1285);
__webpack_require__(4854);
__webpack_require__(6647);
__webpack_require__(7903);
__webpack_require__(5197);
__webpack_require__(3113);
__webpack_require__(2963);
__webpack_require__(6032);
__webpack_require__(732);
__webpack_require__(6696);
__webpack_require__(9391);
__webpack_require__(2123);
__webpack_require__(6541);
__webpack_require__(1767);
__webpack_require__(7593);
__webpack_require__(4870);
__webpack_require__(7937);
__webpack_require__(9168);
__webpack_require__(6351);
__webpack_require__(8217);
__webpack_require__(6792);
__webpack_require__(88);
__webpack_require__(2095);
__webpack_require__(2889);
__webpack_require__(8455);
__webpack_require__(188);
__webpack_require__(9992);
__webpack_require__(3798);
__webpack_require__(9737);
__webpack_require__(5704);
__webpack_require__(3591);
__webpack_require__(922);
__webpack_require__(2177);
__webpack_require__(8791);
__webpack_require__(6426);
__webpack_require__(3884);
__webpack_require__(7469);
__webpack_require__(4097);
__webpack_require__(5813);
__webpack_require__(7245);
__webpack_require__(6756);
__webpack_require__(8392);
__webpack_require__(1111);
__webpack_require__(3735);
__webpack_require__(3037);
__webpack_require__(8422);
__webpack_require__(1818);
__webpack_require__(7883);
__webpack_require__(7371);
__webpack_require__(8088);
__webpack_require__(5414);
__webpack_require__(2812);
__webpack_require__(2835);
__webpack_require__(7415);
__webpack_require__(710);
__webpack_require__(3666);
__webpack_require__(60);
__webpack_require__(7216);
__webpack_require__(3470);
__webpack_require__(2161);
__webpack_require__(6321);
__webpack_require__(5613);
__webpack_require__(2113);
__webpack_require__(1605);
__webpack_require__(1094);
module.exports = __webpack_require__(8544);

/***/ }),

/***/ 4036:
/***/ ((module) => {

"use strict";


function _typeof(obj) { "@babel/helpers - typeof"; return _typeof = "function" == typeof Symbol && "symbol" == typeof Symbol.iterator ? function (obj) { return typeof obj; } : function (obj) { return obj && "function" == typeof Symbol && obj.constructor === Symbol && obj !== Symbol.prototype ? "symbol" : typeof obj; }, _typeof(obj); }
var isMergeableObject = function isMergeableObject(value) {
  return isNonNullObject(value) && !isSpecial(value);
};
function isNonNullObject(value) {
  return !!value && _typeof(value) === 'object';
}
function isSpecial(value) {
  var stringValue = Object.prototype.toString.call(value);
  return stringValue === '[object RegExp]' || stringValue === '[object Date]' || isReactElement(value);
}

// see https://github.com/facebook/react/blob/b5ac963fb791d1298e7f396236383bc955f916c1/src/isomorphic/classic/element/ReactElement.js#L21-L25
var canUseSymbol = typeof Symbol === 'function' && Symbol["for"];
var REACT_ELEMENT_TYPE = canUseSymbol ? Symbol["for"]('react.element') : 0xeac7;
function isReactElement(value) {
  return value.$$typeof === REACT_ELEMENT_TYPE;
}
function emptyTarget(val) {
  return Array.isArray(val) ? [] : {};
}
function cloneUnlessOtherwiseSpecified(value, options) {
  return options.clone !== false && options.isMergeableObject(value) ? deepmerge(emptyTarget(value), value, options) : value;
}
function defaultArrayMerge(target, source, options) {
  return target.concat(source).map(function (element) {
    return cloneUnlessOtherwiseSpecified(element, options);
  });
}
function getMergeFunction(key, options) {
  if (!options.customMerge) {
    return deepmerge;
  }
  var customMerge = options.customMerge(key);
  return typeof customMerge === 'function' ? customMerge : deepmerge;
}
function getEnumerableOwnPropertySymbols(target) {
  return Object.getOwnPropertySymbols ? Object.getOwnPropertySymbols(target).filter(function (symbol) {
    return target.propertyIsEnumerable(symbol);
  }) : [];
}
function getKeys(target) {
  return Object.keys(target).concat(getEnumerableOwnPropertySymbols(target));
}
function propertyIsOnObject(object, property) {
  try {
    return property in object;
  } catch (_) {
    return false;
  }
}

// Protects from prototype poisoning and unexpected merging up the prototype chain.
function propertyIsUnsafe(target, key) {
  return propertyIsOnObject(target, key) // Properties are safe to merge if they don't exist in the target yet,
  && !(Object.hasOwnProperty.call(target, key) // unsafe if they exist up the prototype chain,
  && Object.propertyIsEnumerable.call(target, key)); // and also unsafe if they're nonenumerable.
}

function mergeObject(target, source, options) {
  var destination = {};
  if (options.isMergeableObject(target)) {
    getKeys(target).forEach(function (key) {
      destination[key] = cloneUnlessOtherwiseSpecified(target[key], options);
    });
  }
  getKeys(source).forEach(function (key) {
    if (propertyIsUnsafe(target, key)) {
      return;
    }
    if (propertyIsOnObject(target, key) && options.isMergeableObject(source[key])) {
      destination[key] = getMergeFunction(key, options)(target[key], source[key], options);
    } else {
      destination[key] = cloneUnlessOtherwiseSpecified(source[key], options);
    }
  });
  return destination;
}
function deepmerge(target, source, options) {
  options = options || {};
  options.arrayMerge = options.arrayMerge || defaultArrayMerge;
  options.isMergeableObject = options.isMergeableObject || isMergeableObject;
  // cloneUnlessOtherwiseSpecified is added to `options` so that custom arrayMerge()
  // implementations can use it. The caller may not replace it.
  options.cloneUnlessOtherwiseSpecified = cloneUnlessOtherwiseSpecified;
  var sourceIsArray = Array.isArray(source);
  var targetIsArray = Array.isArray(target);
  var sourceAndTargetTypesMatch = sourceIsArray === targetIsArray;
  if (!sourceAndTargetTypesMatch) {
    return cloneUnlessOtherwiseSpecified(source, options);
  } else if (sourceIsArray) {
    return options.arrayMerge(target, source, options);
  } else {
    return mergeObject(target, source, options);
  }
}
deepmerge.all = function deepmergeAll(array, options) {
  if (!Array.isArray(array)) {
    throw new Error('first argument should be an array');
  }
  return array.reduce(function (prev, next) {
    return deepmerge(prev, next, options);
  }, {});
};
var deepmerge_1 = deepmerge;
module.exports = deepmerge_1;

/***/ }),

/***/ 3117:
/***/ ((__unused_webpack_module, exports) => {

"use strict";


Object.defineProperty(exports, "__esModule", ({
  value: true
}));
exports.attributeNames = exports.elementNames = void 0;
exports.elementNames = new Map([["altglyph", "altGlyph"], ["altglyphdef", "altGlyphDef"], ["altglyphitem", "altGlyphItem"], ["animatecolor", "animateColor"], ["animatemotion", "animateMotion"], ["animatetransform", "animateTransform"], ["clippath", "clipPath"], ["feblend", "feBlend"], ["fecolormatrix", "feColorMatrix"], ["fecomponenttransfer", "feComponentTransfer"], ["fecomposite", "feComposite"], ["feconvolvematrix", "feConvolveMatrix"], ["fediffuselighting", "feDiffuseLighting"], ["fedisplacementmap", "feDisplacementMap"], ["fedistantlight", "feDistantLight"], ["fedropshadow", "feDropShadow"], ["feflood", "feFlood"], ["fefunca", "feFuncA"], ["fefuncb", "feFuncB"], ["fefuncg", "feFuncG"], ["fefuncr", "feFuncR"], ["fegaussianblur", "feGaussianBlur"], ["feimage", "feImage"], ["femerge", "feMerge"], ["femergenode", "feMergeNode"], ["femorphology", "feMorphology"], ["feoffset", "feOffset"], ["fepointlight", "fePointLight"], ["fespecularlighting", "feSpecularLighting"], ["fespotlight", "feSpotLight"], ["fetile", "feTile"], ["feturbulence", "feTurbulence"], ["foreignobject", "foreignObject"], ["glyphref", "glyphRef"], ["lineargradient", "linearGradient"], ["radialgradient", "radialGradient"], ["textpath", "textPath"]]);
exports.attributeNames = new Map([["definitionurl", "definitionURL"], ["attributename", "attributeName"], ["attributetype", "attributeType"], ["basefrequency", "baseFrequency"], ["baseprofile", "baseProfile"], ["calcmode", "calcMode"], ["clippathunits", "clipPathUnits"], ["diffuseconstant", "diffuseConstant"], ["edgemode", "edgeMode"], ["filterunits", "filterUnits"], ["glyphref", "glyphRef"], ["gradienttransform", "gradientTransform"], ["gradientunits", "gradientUnits"], ["kernelmatrix", "kernelMatrix"], ["kernelunitlength", "kernelUnitLength"], ["keypoints", "keyPoints"], ["keysplines", "keySplines"], ["keytimes", "keyTimes"], ["lengthadjust", "lengthAdjust"], ["limitingconeangle", "limitingConeAngle"], ["markerheight", "markerHeight"], ["markerunits", "markerUnits"], ["markerwidth", "markerWidth"], ["maskcontentunits", "maskContentUnits"], ["maskunits", "maskUnits"], ["numoctaves", "numOctaves"], ["pathlength", "pathLength"], ["patterncontentunits", "patternContentUnits"], ["patterntransform", "patternTransform"], ["patternunits", "patternUnits"], ["pointsatx", "pointsAtX"], ["pointsaty", "pointsAtY"], ["pointsatz", "pointsAtZ"], ["preservealpha", "preserveAlpha"], ["preserveaspectratio", "preserveAspectRatio"], ["primitiveunits", "primitiveUnits"], ["refx", "refX"], ["refy", "refY"], ["repeatcount", "repeatCount"], ["repeatdur", "repeatDur"], ["requiredextensions", "requiredExtensions"], ["requiredfeatures", "requiredFeatures"], ["specularconstant", "specularConstant"], ["specularexponent", "specularExponent"], ["spreadmethod", "spreadMethod"], ["startoffset", "startOffset"], ["stddeviation", "stdDeviation"], ["stitchtiles", "stitchTiles"], ["surfacescale", "surfaceScale"], ["systemlanguage", "systemLanguage"], ["tablevalues", "tableValues"], ["targetx", "targetX"], ["targety", "targetY"], ["textlength", "textLength"], ["viewbox", "viewBox"], ["viewtarget", "viewTarget"], ["xchannelselector", "xChannelSelector"], ["ychannelselector", "yChannelSelector"], ["zoomandpan", "zoomAndPan"]]);

/***/ }),

/***/ 1671:
/***/ (function(__unused_webpack_module, exports, __webpack_require__) {

"use strict";


var __assign = this && this.__assign || function () {
  __assign = Object.assign || function (t) {
    for (var s, i = 1, n = arguments.length; i < n; i++) {
      s = arguments[i];
      for (var p in s) {
        if (Object.prototype.hasOwnProperty.call(s, p)) t[p] = s[p];
      }
    }
    return t;
  };
  return __assign.apply(this, arguments);
};
var __createBinding = this && this.__createBinding || (Object.create ? function (o, m, k, k2) {
  if (k2 === undefined) k2 = k;
  Object.defineProperty(o, k2, {
    enumerable: true,
    get: function get() {
      return m[k];
    }
  });
} : function (o, m, k, k2) {
  if (k2 === undefined) k2 = k;
  o[k2] = m[k];
});
var __setModuleDefault = this && this.__setModuleDefault || (Object.create ? function (o, v) {
  Object.defineProperty(o, "default", {
    enumerable: true,
    value: v
  });
} : function (o, v) {
  o["default"] = v;
});
var __importStar = this && this.__importStar || function (mod) {
  if (mod && mod.__esModule) return mod;
  var result = {};
  if (mod != null) for (var k in mod) {
    if (k !== "default" && Object.prototype.hasOwnProperty.call(mod, k)) __createBinding(result, mod, k);
  }
  __setModuleDefault(result, mod);
  return result;
};
Object.defineProperty(exports, "__esModule", ({
  value: true
}));
/*
 * Module dependencies
 */
var ElementType = __importStar(__webpack_require__(7304));
var entities_1 = __webpack_require__(7531);
/**
 * Mixed-case SVG and MathML tags & attributes
 * recognized by the HTML parser.
 *
 * @see https://html.spec.whatwg.org/multipage/parsing.html#parsing-main-inforeign
 */
var foreignNames_1 = __webpack_require__(3117);
var unencodedElements = new Set(["style", "script", "xmp", "iframe", "noembed", "noframes", "plaintext", "noscript"]);
/**
 * Format attributes
 */
function formatAttributes(attributes, opts) {
  if (!attributes) return;
  return Object.keys(attributes).map(function (key) {
    var _a, _b;
    var value = (_a = attributes[key]) !== null && _a !== void 0 ? _a : "";
    if (opts.xmlMode === "foreign") {
      /* Fix up mixed-case attribute names */
      key = (_b = foreignNames_1.attributeNames.get(key)) !== null && _b !== void 0 ? _b : key;
    }
    if (!opts.emptyAttrs && !opts.xmlMode && value === "") {
      return key;
    }
    return key + "=\"" + (opts.decodeEntities !== false ? entities_1.encodeXML(value) : value.replace(/"/g, "&quot;")) + "\"";
  }).join(" ");
}
/**
 * Self-enclosing tags
 */
var singleTag = new Set(["area", "base", "basefont", "br", "col", "command", "embed", "frame", "hr", "img", "input", "isindex", "keygen", "link", "meta", "param", "source", "track", "wbr"]);
/**
 * Renders a DOM node or an array of DOM nodes to a string.
 *
 * Can be thought of as the equivalent of the `outerHTML` of the passed node(s).
 *
 * @param node Node to be rendered.
 * @param options Changes serialization behavior
 */
function render(node, options) {
  if (options === void 0) {
    options = {};
  }
  var nodes = "length" in node ? node : [node];
  var output = "";
  for (var i = 0; i < nodes.length; i++) {
    output += renderNode(nodes[i], options);
  }
  return output;
}
exports["default"] = render;
function renderNode(node, options) {
  switch (node.type) {
    case ElementType.Root:
      return render(node.children, options);
    case ElementType.Directive:
    case ElementType.Doctype:
      return renderDirective(node);
    case ElementType.Comment:
      return renderComment(node);
    case ElementType.CDATA:
      return renderCdata(node);
    case ElementType.Script:
    case ElementType.Style:
    case ElementType.Tag:
      return renderTag(node, options);
    case ElementType.Text:
      return renderText(node, options);
  }
}
var foreignModeIntegrationPoints = new Set(["mi", "mo", "mn", "ms", "mtext", "annotation-xml", "foreignObject", "desc", "title"]);
var foreignElements = new Set(["svg", "math"]);
function renderTag(elem, opts) {
  var _a;
  // Handle SVG / MathML in HTML
  if (opts.xmlMode === "foreign") {
    /* Fix up mixed-case element names */
    elem.name = (_a = foreignNames_1.elementNames.get(elem.name)) !== null && _a !== void 0 ? _a : elem.name;
    /* Exit foreign mode at integration points */
    if (elem.parent && foreignModeIntegrationPoints.has(elem.parent.name)) {
      opts = __assign(__assign({}, opts), {
        xmlMode: false
      });
    }
  }
  if (!opts.xmlMode && foreignElements.has(elem.name)) {
    opts = __assign(__assign({}, opts), {
      xmlMode: "foreign"
    });
  }
  var tag = "<" + elem.name;
  var attribs = formatAttributes(elem.attribs, opts);
  if (attribs) {
    tag += " " + attribs;
  }
  if (elem.children.length === 0 && (opts.xmlMode ?
  // In XML mode or foreign mode, and user hasn't explicitly turned off self-closing tags
  opts.selfClosingTags !== false :
  // User explicitly asked for self-closing tags, even in HTML mode
  opts.selfClosingTags && singleTag.has(elem.name))) {
    if (!opts.xmlMode) tag += " ";
    tag += "/>";
  } else {
    tag += ">";
    if (elem.children.length > 0) {
      tag += render(elem.children, opts);
    }
    if (opts.xmlMode || !singleTag.has(elem.name)) {
      tag += "</" + elem.name + ">";
    }
  }
  return tag;
}
function renderDirective(elem) {
  return "<" + elem.data + ">";
}
function renderText(elem, opts) {
  var data = elem.data || "";
  // If entities weren't decoded, no need to encode them back
  if (opts.decodeEntities !== false && !(!opts.xmlMode && elem.parent && unencodedElements.has(elem.parent.name))) {
    data = entities_1.encodeXML(data);
  }
  return data;
}
function renderCdata(elem) {
  return "<![CDATA[" + elem.children[0].data + "]]>";
}
function renderComment(elem) {
  return "<!--" + elem.data + "-->";
}

/***/ }),

/***/ 7304:
/***/ ((__unused_webpack_module, exports) => {

"use strict";


Object.defineProperty(exports, "__esModule", ({
  value: true
}));
exports.Doctype = exports.CDATA = exports.Tag = exports.Style = exports.Script = exports.Comment = exports.Directive = exports.Text = exports.Root = exports.isTag = exports.ElementType = void 0;
/** Types of elements found in htmlparser2's DOM */
var ElementType;
(function (ElementType) {
  /** Type for the root element of a document */
  ElementType["Root"] = "root";
  /** Type for Text */
  ElementType["Text"] = "text";
  /** Type for <? ... ?> */
  ElementType["Directive"] = "directive";
  /** Type for <!-- ... --> */
  ElementType["Comment"] = "comment";
  /** Type for <script> tags */
  ElementType["Script"] = "script";
  /** Type for <style> tags */
  ElementType["Style"] = "style";
  /** Type for Any tag */
  ElementType["Tag"] = "tag";
  /** Type for <![CDATA[ ... ]]> */
  ElementType["CDATA"] = "cdata";
  /** Type for <!doctype ...> */
  ElementType["Doctype"] = "doctype";
})(ElementType = exports.ElementType || (exports.ElementType = {}));
/**
 * Tests whether an element is a tag or not.
 *
 * @param elem Element to test
 */
function isTag(elem) {
  return elem.type === ElementType.Tag || elem.type === ElementType.Script || elem.type === ElementType.Style;
}
exports.isTag = isTag;
// Exports for backwards compatibility
/** Type for the root element of a document */
exports.Root = ElementType.Root;
/** Type for Text */
exports.Text = ElementType.Text;
/** Type for <? ... ?> */
exports.Directive = ElementType.Directive;
/** Type for <!-- ... --> */
exports.Comment = ElementType.Comment;
/** Type for <script> tags */
exports.Script = ElementType.Script;
/** Type for <style> tags */
exports.Style = ElementType.Style;
/** Type for Any tag */
exports.Tag = ElementType.Tag;
/** Type for <![CDATA[ ... ]]> */
exports.CDATA = ElementType.CDATA;
/** Type for <!doctype ...> */
exports.Doctype = ElementType.Doctype;

/***/ }),

/***/ 1363:
/***/ (function(__unused_webpack_module, exports, __webpack_require__) {

"use strict";


function _typeof(obj) { "@babel/helpers - typeof"; return _typeof = "function" == typeof Symbol && "symbol" == typeof Symbol.iterator ? function (obj) { return typeof obj; } : function (obj) { return obj && "function" == typeof Symbol && obj.constructor === Symbol && obj !== Symbol.prototype ? "symbol" : typeof obj; }, _typeof(obj); }
var __createBinding = this && this.__createBinding || (Object.create ? function (o, m, k, k2) {
  if (k2 === undefined) k2 = k;
  var desc = Object.getOwnPropertyDescriptor(m, k);
  if (!desc || ("get" in desc ? !m.__esModule : desc.writable || desc.configurable)) {
    desc = {
      enumerable: true,
      get: function get() {
        return m[k];
      }
    };
  }
  Object.defineProperty(o, k2, desc);
} : function (o, m, k, k2) {
  if (k2 === undefined) k2 = k;
  o[k2] = m[k];
});
var __exportStar = this && this.__exportStar || function (m, exports) {
  for (var p in m) {
    if (p !== "default" && !Object.prototype.hasOwnProperty.call(exports, p)) __createBinding(exports, m, p);
  }
};
Object.defineProperty(exports, "__esModule", ({
  value: true
}));
exports.DomHandler = void 0;
var domelementtype_1 = __webpack_require__(7304);
var node_1 = __webpack_require__(5653);
__exportStar(__webpack_require__(5653), exports);
var reWhitespace = /\s+/g;
// Default options
var defaultOpts = {
  normalizeWhitespace: false,
  withStartIndices: false,
  withEndIndices: false,
  xmlMode: false
};
var DomHandler = /** @class */function () {
  /**
   * @param callback Called once parsing has completed.
   * @param options Settings for the handler.
   * @param elementCB Callback whenever a tag is closed.
   */
  function DomHandler(callback, options, elementCB) {
    /** The elements of the DOM */
    this.dom = [];
    /** The root element for the DOM */
    this.root = new node_1.Document(this.dom);
    /** Indicated whether parsing has been completed. */
    this.done = false;
    /** Stack of open tags. */
    this.tagStack = [this.root];
    /** A data node that is still being written to. */
    this.lastNode = null;
    /** Reference to the parser instance. Used for location information. */
    this.parser = null;
    // Make it possible to skip arguments, for backwards-compatibility
    if (typeof options === "function") {
      elementCB = options;
      options = defaultOpts;
    }
    if (_typeof(callback) === "object") {
      options = callback;
      callback = undefined;
    }
    this.callback = callback !== null && callback !== void 0 ? callback : null;
    this.options = options !== null && options !== void 0 ? options : defaultOpts;
    this.elementCB = elementCB !== null && elementCB !== void 0 ? elementCB : null;
  }
  DomHandler.prototype.onparserinit = function (parser) {
    this.parser = parser;
  };
  // Resets the handler back to starting state
  DomHandler.prototype.onreset = function () {
    this.dom = [];
    this.root = new node_1.Document(this.dom);
    this.done = false;
    this.tagStack = [this.root];
    this.lastNode = null;
    this.parser = null;
  };
  // Signals the handler that parsing is done
  DomHandler.prototype.onend = function () {
    if (this.done) return;
    this.done = true;
    this.parser = null;
    this.handleCallback(null);
  };
  DomHandler.prototype.onerror = function (error) {
    this.handleCallback(error);
  };
  DomHandler.prototype.onclosetag = function () {
    this.lastNode = null;
    var elem = this.tagStack.pop();
    if (this.options.withEndIndices) {
      elem.endIndex = this.parser.endIndex;
    }
    if (this.elementCB) this.elementCB(elem);
  };
  DomHandler.prototype.onopentag = function (name, attribs) {
    var type = this.options.xmlMode ? domelementtype_1.ElementType.Tag : undefined;
    var element = new node_1.Element(name, attribs, undefined, type);
    this.addNode(element);
    this.tagStack.push(element);
  };
  DomHandler.prototype.ontext = function (data) {
    var normalizeWhitespace = this.options.normalizeWhitespace;
    var lastNode = this.lastNode;
    if (lastNode && lastNode.type === domelementtype_1.ElementType.Text) {
      if (normalizeWhitespace) {
        lastNode.data = (lastNode.data + data).replace(reWhitespace, " ");
      } else {
        lastNode.data += data;
      }
      if (this.options.withEndIndices) {
        lastNode.endIndex = this.parser.endIndex;
      }
    } else {
      if (normalizeWhitespace) {
        data = data.replace(reWhitespace, " ");
      }
      var node = new node_1.Text(data);
      this.addNode(node);
      this.lastNode = node;
    }
  };
  DomHandler.prototype.oncomment = function (data) {
    if (this.lastNode && this.lastNode.type === domelementtype_1.ElementType.Comment) {
      this.lastNode.data += data;
      return;
    }
    var node = new node_1.Comment(data);
    this.addNode(node);
    this.lastNode = node;
  };
  DomHandler.prototype.oncommentend = function () {
    this.lastNode = null;
  };
  DomHandler.prototype.oncdatastart = function () {
    var text = new node_1.Text("");
    var node = new node_1.NodeWithChildren(domelementtype_1.ElementType.CDATA, [text]);
    this.addNode(node);
    text.parent = node;
    this.lastNode = text;
  };
  DomHandler.prototype.oncdataend = function () {
    this.lastNode = null;
  };
  DomHandler.prototype.onprocessinginstruction = function (name, data) {
    var node = new node_1.ProcessingInstruction(name, data);
    this.addNode(node);
  };
  DomHandler.prototype.handleCallback = function (error) {
    if (typeof this.callback === "function") {
      this.callback(error, this.dom);
    } else if (error) {
      throw error;
    }
  };
  DomHandler.prototype.addNode = function (node) {
    var parent = this.tagStack[this.tagStack.length - 1];
    var previousSibling = parent.children[parent.children.length - 1];
    if (this.options.withStartIndices) {
      node.startIndex = this.parser.startIndex;
    }
    if (this.options.withEndIndices) {
      node.endIndex = this.parser.endIndex;
    }
    parent.children.push(node);
    if (previousSibling) {
      node.prev = previousSibling;
      previousSibling.next = node;
    }
    node.parent = parent;
    this.lastNode = null;
  };
  return DomHandler;
}();
exports.DomHandler = DomHandler;
exports["default"] = DomHandler;

/***/ }),

/***/ 5653:
/***/ (function(__unused_webpack_module, exports, __webpack_require__) {

"use strict";


var __extends = this && this.__extends || function () {
  var _extendStatics = function extendStatics(d, b) {
    _extendStatics = Object.setPrototypeOf || {
      __proto__: []
    } instanceof Array && function (d, b) {
      d.__proto__ = b;
    } || function (d, b) {
      for (var p in b) {
        if (Object.prototype.hasOwnProperty.call(b, p)) d[p] = b[p];
      }
    };
    return _extendStatics(d, b);
  };
  return function (d, b) {
    if (typeof b !== "function" && b !== null) throw new TypeError("Class extends value " + String(b) + " is not a constructor or null");
    _extendStatics(d, b);
    function __() {
      this.constructor = d;
    }
    d.prototype = b === null ? Object.create(b) : (__.prototype = b.prototype, new __());
  };
}();
var __assign = this && this.__assign || function () {
  __assign = Object.assign || function (t) {
    for (var s, i = 1, n = arguments.length; i < n; i++) {
      s = arguments[i];
      for (var p in s) {
        if (Object.prototype.hasOwnProperty.call(s, p)) t[p] = s[p];
      }
    }
    return t;
  };
  return __assign.apply(this, arguments);
};
Object.defineProperty(exports, "__esModule", ({
  value: true
}));
exports.cloneNode = exports.hasChildren = exports.isDocument = exports.isDirective = exports.isComment = exports.isText = exports.isCDATA = exports.isTag = exports.Element = exports.Document = exports.NodeWithChildren = exports.ProcessingInstruction = exports.Comment = exports.Text = exports.DataNode = exports.Node = void 0;
var domelementtype_1 = __webpack_require__(7304);
var nodeTypes = new Map([[domelementtype_1.ElementType.Tag, 1], [domelementtype_1.ElementType.Script, 1], [domelementtype_1.ElementType.Style, 1], [domelementtype_1.ElementType.Directive, 1], [domelementtype_1.ElementType.Text, 3], [domelementtype_1.ElementType.CDATA, 4], [domelementtype_1.ElementType.Comment, 8], [domelementtype_1.ElementType.Root, 9]]);
/**
 * This object will be used as the prototype for Nodes when creating a
 * DOM-Level-1-compliant structure.
 */
var Node = /** @class */function () {
  /**
   *
   * @param type The type of the node.
   */
  function Node(type) {
    this.type = type;
    /** Parent of the node */
    this.parent = null;
    /** Previous sibling */
    this.prev = null;
    /** Next sibling */
    this.next = null;
    /** The start index of the node. Requires `withStartIndices` on the handler to be `true. */
    this.startIndex = null;
    /** The end index of the node. Requires `withEndIndices` on the handler to be `true. */
    this.endIndex = null;
  }
  Object.defineProperty(Node.prototype, "nodeType", {
    // Read-only aliases
    /**
     * [DOM spec](https://dom.spec.whatwg.org/#dom-node-nodetype)-compatible
     * node {@link type}.
     */
    get: function get() {
      var _a;
      return (_a = nodeTypes.get(this.type)) !== null && _a !== void 0 ? _a : 1;
    },
    enumerable: false,
    configurable: true
  });
  Object.defineProperty(Node.prototype, "parentNode", {
    // Read-write aliases for properties
    /**
     * Same as {@link parent}.
     * [DOM spec](https://dom.spec.whatwg.org)-compatible alias.
     */
    get: function get() {
      return this.parent;
    },
    set: function set(parent) {
      this.parent = parent;
    },
    enumerable: false,
    configurable: true
  });
  Object.defineProperty(Node.prototype, "previousSibling", {
    /**
     * Same as {@link prev}.
     * [DOM spec](https://dom.spec.whatwg.org)-compatible alias.
     */
    get: function get() {
      return this.prev;
    },
    set: function set(prev) {
      this.prev = prev;
    },
    enumerable: false,
    configurable: true
  });
  Object.defineProperty(Node.prototype, "nextSibling", {
    /**
     * Same as {@link next}.
     * [DOM spec](https://dom.spec.whatwg.org)-compatible alias.
     */
    get: function get() {
      return this.next;
    },
    set: function set(next) {
      this.next = next;
    },
    enumerable: false,
    configurable: true
  });
  /**
   * Clone this node, and optionally its children.
   *
   * @param recursive Clone child nodes as well.
   * @returns A clone of the node.
   */
  Node.prototype.cloneNode = function (recursive) {
    if (recursive === void 0) {
      recursive = false;
    }
    return cloneNode(this, recursive);
  };
  return Node;
}();
exports.Node = Node;
/**
 * A node that contains some data.
 */
var DataNode = /** @class */function (_super) {
  __extends(DataNode, _super);
  /**
   * @param type The type of the node
   * @param data The content of the data node
   */
  function DataNode(type, data) {
    var _this = _super.call(this, type) || this;
    _this.data = data;
    return _this;
  }
  Object.defineProperty(DataNode.prototype, "nodeValue", {
    /**
     * Same as {@link data}.
     * [DOM spec](https://dom.spec.whatwg.org)-compatible alias.
     */
    get: function get() {
      return this.data;
    },
    set: function set(data) {
      this.data = data;
    },
    enumerable: false,
    configurable: true
  });
  return DataNode;
}(Node);
exports.DataNode = DataNode;
/**
 * Text within the document.
 */
var Text = /** @class */function (_super) {
  __extends(Text, _super);
  function Text(data) {
    return _super.call(this, domelementtype_1.ElementType.Text, data) || this;
  }
  return Text;
}(DataNode);
exports.Text = Text;
/**
 * Comments within the document.
 */
var Comment = /** @class */function (_super) {
  __extends(Comment, _super);
  function Comment(data) {
    return _super.call(this, domelementtype_1.ElementType.Comment, data) || this;
  }
  return Comment;
}(DataNode);
exports.Comment = Comment;
/**
 * Processing instructions, including doc types.
 */
var ProcessingInstruction = /** @class */function (_super) {
  __extends(ProcessingInstruction, _super);
  function ProcessingInstruction(name, data) {
    var _this = _super.call(this, domelementtype_1.ElementType.Directive, data) || this;
    _this.name = name;
    return _this;
  }
  return ProcessingInstruction;
}(DataNode);
exports.ProcessingInstruction = ProcessingInstruction;
/**
 * A `Node` that can have children.
 */
var NodeWithChildren = /** @class */function (_super) {
  __extends(NodeWithChildren, _super);
  /**
   * @param type Type of the node.
   * @param children Children of the node. Only certain node types can have children.
   */
  function NodeWithChildren(type, children) {
    var _this = _super.call(this, type) || this;
    _this.children = children;
    return _this;
  }
  Object.defineProperty(NodeWithChildren.prototype, "firstChild", {
    // Aliases
    /** First child of the node. */
    get: function get() {
      var _a;
      return (_a = this.children[0]) !== null && _a !== void 0 ? _a : null;
    },
    enumerable: false,
    configurable: true
  });
  Object.defineProperty(NodeWithChildren.prototype, "lastChild", {
    /** Last child of the node. */
    get: function get() {
      return this.children.length > 0 ? this.children[this.children.length - 1] : null;
    },
    enumerable: false,
    configurable: true
  });
  Object.defineProperty(NodeWithChildren.prototype, "childNodes", {
    /**
     * Same as {@link children}.
     * [DOM spec](https://dom.spec.whatwg.org)-compatible alias.
     */
    get: function get() {
      return this.children;
    },
    set: function set(children) {
      this.children = children;
    },
    enumerable: false,
    configurable: true
  });
  return NodeWithChildren;
}(Node);
exports.NodeWithChildren = NodeWithChildren;
/**
 * The root node of the document.
 */
var Document = /** @class */function (_super) {
  __extends(Document, _super);
  function Document(children) {
    return _super.call(this, domelementtype_1.ElementType.Root, children) || this;
  }
  return Document;
}(NodeWithChildren);
exports.Document = Document;
/**
 * An element within the DOM.
 */
var Element = /** @class */function (_super) {
  __extends(Element, _super);
  /**
   * @param name Name of the tag, eg. `div`, `span`.
   * @param attribs Object mapping attribute names to attribute values.
   * @param children Children of the node.
   */
  function Element(name, attribs, children, type) {
    if (children === void 0) {
      children = [];
    }
    if (type === void 0) {
      type = name === "script" ? domelementtype_1.ElementType.Script : name === "style" ? domelementtype_1.ElementType.Style : domelementtype_1.ElementType.Tag;
    }
    var _this = _super.call(this, type, children) || this;
    _this.name = name;
    _this.attribs = attribs;
    return _this;
  }
  Object.defineProperty(Element.prototype, "tagName", {
    // DOM Level 1 aliases
    /**
     * Same as {@link name}.
     * [DOM spec](https://dom.spec.whatwg.org)-compatible alias.
     */
    get: function get() {
      return this.name;
    },
    set: function set(name) {
      this.name = name;
    },
    enumerable: false,
    configurable: true
  });
  Object.defineProperty(Element.prototype, "attributes", {
    get: function get() {
      var _this = this;
      return Object.keys(this.attribs).map(function (name) {
        var _a, _b;
        return {
          name: name,
          value: _this.attribs[name],
          namespace: (_a = _this["x-attribsNamespace"]) === null || _a === void 0 ? void 0 : _a[name],
          prefix: (_b = _this["x-attribsPrefix"]) === null || _b === void 0 ? void 0 : _b[name]
        };
      });
    },
    enumerable: false,
    configurable: true
  });
  return Element;
}(NodeWithChildren);
exports.Element = Element;
/**
 * @param node Node to check.
 * @returns `true` if the node is a `Element`, `false` otherwise.
 */
function isTag(node) {
  return (0, domelementtype_1.isTag)(node);
}
exports.isTag = isTag;
/**
 * @param node Node to check.
 * @returns `true` if the node has the type `CDATA`, `false` otherwise.
 */
function isCDATA(node) {
  return node.type === domelementtype_1.ElementType.CDATA;
}
exports.isCDATA = isCDATA;
/**
 * @param node Node to check.
 * @returns `true` if the node has the type `Text`, `false` otherwise.
 */
function isText(node) {
  return node.type === domelementtype_1.ElementType.Text;
}
exports.isText = isText;
/**
 * @param node Node to check.
 * @returns `true` if the node has the type `Comment`, `false` otherwise.
 */
function isComment(node) {
  return node.type === domelementtype_1.ElementType.Comment;
}
exports.isComment = isComment;
/**
 * @param node Node to check.
 * @returns `true` if the node has the type `ProcessingInstruction`, `false` otherwise.
 */
function isDirective(node) {
  return node.type === domelementtype_1.ElementType.Directive;
}
exports.isDirective = isDirective;
/**
 * @param node Node to check.
 * @returns `true` if the node has the type `ProcessingInstruction`, `false` otherwise.
 */
function isDocument(node) {
  return node.type === domelementtype_1.ElementType.Root;
}
exports.isDocument = isDocument;
/**
 * @param node Node to check.
 * @returns `true` if the node is a `NodeWithChildren` (has children), `false` otherwise.
 */
function hasChildren(node) {
  return Object.prototype.hasOwnProperty.call(node, "children");
}
exports.hasChildren = hasChildren;
/**
 * Clone a node, and optionally its children.
 *
 * @param recursive Clone child nodes as well.
 * @returns A clone of the node.
 */
function cloneNode(node, recursive) {
  if (recursive === void 0) {
    recursive = false;
  }
  var result;
  if (isText(node)) {
    result = new Text(node.data);
  } else if (isComment(node)) {
    result = new Comment(node.data);
  } else if (isTag(node)) {
    var children = recursive ? cloneChildren(node.children) : [];
    var clone_1 = new Element(node.name, __assign({}, node.attribs), children);
    children.forEach(function (child) {
      return child.parent = clone_1;
    });
    if (node.namespace != null) {
      clone_1.namespace = node.namespace;
    }
    if (node["x-attribsNamespace"]) {
      clone_1["x-attribsNamespace"] = __assign({}, node["x-attribsNamespace"]);
    }
    if (node["x-attribsPrefix"]) {
      clone_1["x-attribsPrefix"] = __assign({}, node["x-attribsPrefix"]);
    }
    result = clone_1;
  } else if (isCDATA(node)) {
    var children = recursive ? cloneChildren(node.children) : [];
    var clone_2 = new NodeWithChildren(domelementtype_1.ElementType.CDATA, children);
    children.forEach(function (child) {
      return child.parent = clone_2;
    });
    result = clone_2;
  } else if (isDocument(node)) {
    var children = recursive ? cloneChildren(node.children) : [];
    var clone_3 = new Document(children);
    children.forEach(function (child) {
      return child.parent = clone_3;
    });
    if (node["x-mode"]) {
      clone_3["x-mode"] = node["x-mode"];
    }
    result = clone_3;
  } else if (isDirective(node)) {
    var instruction = new ProcessingInstruction(node.name, node.data);
    if (node["x-name"] != null) {
      instruction["x-name"] = node["x-name"];
      instruction["x-publicId"] = node["x-publicId"];
      instruction["x-systemId"] = node["x-systemId"];
    }
    result = instruction;
  } else {
    throw new Error("Not implemented yet: ".concat(node.type));
  }
  result.startIndex = node.startIndex;
  result.endIndex = node.endIndex;
  if (node.sourceCodeLocation != null) {
    result.sourceCodeLocation = node.sourceCodeLocation;
  }
  return result;
}
exports.cloneNode = cloneNode;
function cloneChildren(childs) {
  var children = childs.map(function (child) {
    return cloneNode(child, true);
  });
  for (var i = 1; i < children.length; i++) {
    children[i].prev = children[i - 1];
    children[i - 1].next = children[i];
  }
  return children;
}

/***/ }),

/***/ 3625:
/***/ ((__unused_webpack_module, exports, __webpack_require__) => {

"use strict";


Object.defineProperty(exports, "__esModule", ({
  value: true
}));
exports.getFeed = void 0;
var stringify_1 = __webpack_require__(3633);
var legacy_1 = __webpack_require__(7344);
/**
 * Get the feed object from the root of a DOM tree.
 *
 * @param doc - The DOM to to extract the feed from.
 * @returns The feed.
 */
function getFeed(doc) {
  var feedRoot = getOneElement(isValidFeed, doc);
  return !feedRoot ? null : feedRoot.name === "feed" ? getAtomFeed(feedRoot) : getRssFeed(feedRoot);
}
exports.getFeed = getFeed;
/**
 * Parse an Atom feed.
 *
 * @param feedRoot The root of the feed.
 * @returns The parsed feed.
 */
function getAtomFeed(feedRoot) {
  var _a;
  var childs = feedRoot.children;
  var feed = {
    type: "atom",
    items: (0, legacy_1.getElementsByTagName)("entry", childs).map(function (item) {
      var _a;
      var children = item.children;
      var entry = {
        media: getMediaElements(children)
      };
      addConditionally(entry, "id", "id", children);
      addConditionally(entry, "title", "title", children);
      var href = (_a = getOneElement("link", children)) === null || _a === void 0 ? void 0 : _a.attribs.href;
      if (href) {
        entry.link = href;
      }
      var description = fetch("summary", children) || fetch("content", children);
      if (description) {
        entry.description = description;
      }
      var pubDate = fetch("updated", children);
      if (pubDate) {
        entry.pubDate = new Date(pubDate);
      }
      return entry;
    })
  };
  addConditionally(feed, "id", "id", childs);
  addConditionally(feed, "title", "title", childs);
  var href = (_a = getOneElement("link", childs)) === null || _a === void 0 ? void 0 : _a.attribs.href;
  if (href) {
    feed.link = href;
  }
  addConditionally(feed, "description", "subtitle", childs);
  var updated = fetch("updated", childs);
  if (updated) {
    feed.updated = new Date(updated);
  }
  addConditionally(feed, "author", "email", childs, true);
  return feed;
}
/**
 * Parse a RSS feed.
 *
 * @param feedRoot The root of the feed.
 * @returns The parsed feed.
 */
function getRssFeed(feedRoot) {
  var _a, _b;
  var childs = (_b = (_a = getOneElement("channel", feedRoot.children)) === null || _a === void 0 ? void 0 : _a.children) !== null && _b !== void 0 ? _b : [];
  var feed = {
    type: feedRoot.name.substr(0, 3),
    id: "",
    items: (0, legacy_1.getElementsByTagName)("item", feedRoot.children).map(function (item) {
      var children = item.children;
      var entry = {
        media: getMediaElements(children)
      };
      addConditionally(entry, "id", "guid", children);
      addConditionally(entry, "title", "title", children);
      addConditionally(entry, "link", "link", children);
      addConditionally(entry, "description", "description", children);
      var pubDate = fetch("pubDate", children);
      if (pubDate) entry.pubDate = new Date(pubDate);
      return entry;
    })
  };
  addConditionally(feed, "title", "title", childs);
  addConditionally(feed, "link", "link", childs);
  addConditionally(feed, "description", "description", childs);
  var updated = fetch("lastBuildDate", childs);
  if (updated) {
    feed.updated = new Date(updated);
  }
  addConditionally(feed, "author", "managingEditor", childs, true);
  return feed;
}
var MEDIA_KEYS_STRING = ["url", "type", "lang"];
var MEDIA_KEYS_INT = ["fileSize", "bitrate", "framerate", "samplingrate", "channels", "duration", "height", "width"];
/**
 * Get all media elements of a feed item.
 *
 * @param where Nodes to search in.
 * @returns Media elements.
 */
function getMediaElements(where) {
  return (0, legacy_1.getElementsByTagName)("media:content", where).map(function (elem) {
    var attribs = elem.attribs;
    var media = {
      medium: attribs.medium,
      isDefault: !!attribs.isDefault
    };
    for (var _i = 0, MEDIA_KEYS_STRING_1 = MEDIA_KEYS_STRING; _i < MEDIA_KEYS_STRING_1.length; _i++) {
      var attrib = MEDIA_KEYS_STRING_1[_i];
      if (attribs[attrib]) {
        media[attrib] = attribs[attrib];
      }
    }
    for (var _a = 0, MEDIA_KEYS_INT_1 = MEDIA_KEYS_INT; _a < MEDIA_KEYS_INT_1.length; _a++) {
      var attrib = MEDIA_KEYS_INT_1[_a];
      if (attribs[attrib]) {
        media[attrib] = parseInt(attribs[attrib], 10);
      }
    }
    if (attribs.expression) {
      media.expression = attribs.expression;
    }
    return media;
  });
}
/**
 * Get one element by tag name.
 *
 * @param tagName Tag name to look for
 * @param node Node to search in
 * @returns The element or null
 */
function getOneElement(tagName, node) {
  return (0, legacy_1.getElementsByTagName)(tagName, node, true, 1)[0];
}
/**
 * Get the text content of an element with a certain tag name.
 *
 * @param tagName Tag name to look for.
 * @param where  Node to search in.
 * @param recurse Whether to recurse into child nodes.
 * @returns The text content of the element.
 */
function fetch(tagName, where, recurse) {
  if (recurse === void 0) {
    recurse = false;
  }
  return (0, stringify_1.textContent)((0, legacy_1.getElementsByTagName)(tagName, where, recurse, 1)).trim();
}
/**
 * Adds a property to an object if it has a value.
 *
 * @param obj Object to be extended
 * @param prop Property name
 * @param tagName Tag name that contains the conditionally added property
 * @param where Element to search for the property
 * @param recurse Whether to recurse into child nodes.
 */
function addConditionally(obj, prop, tagName, where, recurse) {
  if (recurse === void 0) {
    recurse = false;
  }
  var val = fetch(tagName, where, recurse);
  if (val) obj[prop] = val;
}
/**
 * Checks if an element is a feed root node.
 *
 * @param value The name of the element to check.
 * @returns Whether an element is a feed root node.
 */
function isValidFeed(value) {
  return value === "rss" || value === "feed" || value === "rdf:RDF";
}

/***/ }),

/***/ 3757:
/***/ ((__unused_webpack_module, exports, __webpack_require__) => {

"use strict";


Object.defineProperty(exports, "__esModule", ({
  value: true
}));
exports.uniqueSort = exports.compareDocumentPosition = exports.removeSubsets = void 0;
var domhandler_1 = __webpack_require__(1363);
/**
 * Given an array of nodes, remove any member that is contained by another.
 *
 * @param nodes Nodes to filter.
 * @returns Remaining nodes that aren't subtrees of each other.
 */
function removeSubsets(nodes) {
  var idx = nodes.length;
  /*
   * Check if each node (or one of its ancestors) is already contained in the
   * array.
   */
  while (--idx >= 0) {
    var node = nodes[idx];
    /*
     * Remove the node if it is not unique.
     * We are going through the array from the end, so we only
     * have to check nodes that preceed the node under consideration in the array.
     */
    if (idx > 0 && nodes.lastIndexOf(node, idx - 1) >= 0) {
      nodes.splice(idx, 1);
      continue;
    }
    for (var ancestor = node.parent; ancestor; ancestor = ancestor.parent) {
      if (nodes.includes(ancestor)) {
        nodes.splice(idx, 1);
        break;
      }
    }
  }
  return nodes;
}
exports.removeSubsets = removeSubsets;
/**
 * Compare the position of one node against another node in any other document.
 * The return value is a bitmask with the following values:
 *
 * Document order:
 * > There is an ordering, document order, defined on all the nodes in the
 * > document corresponding to the order in which the first character of the
 * > XML representation of each node occurs in the XML representation of the
 * > document after expansion of general entities. Thus, the document element
 * > node will be the first node. Element nodes occur before their children.
 * > Thus, document order orders element nodes in order of the occurrence of
 * > their start-tag in the XML (after expansion of entities). The attribute
 * > nodes of an element occur after the element and before its children. The
 * > relative order of attribute nodes is implementation-dependent./
 *
 * Source:
 * http://www.w3.org/TR/DOM-Level-3-Core/glossary.html#dt-document-order
 *
 * @param nodeA The first node to use in the comparison
 * @param nodeB The second node to use in the comparison
 * @returns A bitmask describing the input nodes' relative position.
 *
 * See http://dom.spec.whatwg.org/#dom-node-comparedocumentposition for
 * a description of these values.
 */
function compareDocumentPosition(nodeA, nodeB) {
  var aParents = [];
  var bParents = [];
  if (nodeA === nodeB) {
    return 0;
  }
  var current = (0, domhandler_1.hasChildren)(nodeA) ? nodeA : nodeA.parent;
  while (current) {
    aParents.unshift(current);
    current = current.parent;
  }
  current = (0, domhandler_1.hasChildren)(nodeB) ? nodeB : nodeB.parent;
  while (current) {
    bParents.unshift(current);
    current = current.parent;
  }
  var maxIdx = Math.min(aParents.length, bParents.length);
  var idx = 0;
  while (idx < maxIdx && aParents[idx] === bParents[idx]) {
    idx++;
  }
  if (idx === 0) {
    return 1 /* DISCONNECTED */;
  }

  var sharedParent = aParents[idx - 1];
  var siblings = sharedParent.children;
  var aSibling = aParents[idx];
  var bSibling = bParents[idx];
  if (siblings.indexOf(aSibling) > siblings.indexOf(bSibling)) {
    if (sharedParent === nodeB) {
      return 4 /* FOLLOWING */ | 16 /* CONTAINED_BY */;
    }

    return 4 /* FOLLOWING */;
  }

  if (sharedParent === nodeA) {
    return 2 /* PRECEDING */ | 8 /* CONTAINS */;
  }

  return 2 /* PRECEDING */;
}

exports.compareDocumentPosition = compareDocumentPosition;
/**
 * Sort an array of nodes based on their relative position in the document and
 * remove any duplicate nodes. If the array contains nodes that do not belong
 * to the same document, sort order is unspecified.
 *
 * @param nodes Array of DOM nodes.
 * @returns Collection of unique nodes, sorted in document order.
 */
function uniqueSort(nodes) {
  nodes = nodes.filter(function (node, i, arr) {
    return !arr.includes(node, i + 1);
  });
  nodes.sort(function (a, b) {
    var relative = compareDocumentPosition(a, b);
    if (relative & 2 /* PRECEDING */) {
      return -1;
    } else if (relative & 4 /* FOLLOWING */) {
      return 1;
    }
    return 0;
  });
  return nodes;
}
exports.uniqueSort = uniqueSort;

/***/ }),

/***/ 5511:
/***/ (function(__unused_webpack_module, exports, __webpack_require__) {

"use strict";


var __createBinding = this && this.__createBinding || (Object.create ? function (o, m, k, k2) {
  if (k2 === undefined) k2 = k;
  Object.defineProperty(o, k2, {
    enumerable: true,
    get: function get() {
      return m[k];
    }
  });
} : function (o, m, k, k2) {
  if (k2 === undefined) k2 = k;
  o[k2] = m[k];
});
var __exportStar = this && this.__exportStar || function (m, exports) {
  for (var p in m) {
    if (p !== "default" && !Object.prototype.hasOwnProperty.call(exports, p)) __createBinding(exports, m, p);
  }
};
Object.defineProperty(exports, "__esModule", ({
  value: true
}));
exports.hasChildren = exports.isDocument = exports.isComment = exports.isText = exports.isCDATA = exports.isTag = void 0;
__exportStar(__webpack_require__(3633), exports);
__exportStar(__webpack_require__(6530), exports);
__exportStar(__webpack_require__(1833), exports);
__exportStar(__webpack_require__(7062), exports);
__exportStar(__webpack_require__(7344), exports);
__exportStar(__webpack_require__(3757), exports);
__exportStar(__webpack_require__(3625), exports);
/** @deprecated Use these methods from `domhandler` directly. */
var domhandler_1 = __webpack_require__(1363);
Object.defineProperty(exports, "isTag", ({
  enumerable: true,
  get: function get() {
    return domhandler_1.isTag;
  }
}));
Object.defineProperty(exports, "isCDATA", ({
  enumerable: true,
  get: function get() {
    return domhandler_1.isCDATA;
  }
}));
Object.defineProperty(exports, "isText", ({
  enumerable: true,
  get: function get() {
    return domhandler_1.isText;
  }
}));
Object.defineProperty(exports, "isComment", ({
  enumerable: true,
  get: function get() {
    return domhandler_1.isComment;
  }
}));
Object.defineProperty(exports, "isDocument", ({
  enumerable: true,
  get: function get() {
    return domhandler_1.isDocument;
  }
}));
Object.defineProperty(exports, "hasChildren", ({
  enumerable: true,
  get: function get() {
    return domhandler_1.hasChildren;
  }
}));

/***/ }),

/***/ 7344:
/***/ ((__unused_webpack_module, exports, __webpack_require__) => {

"use strict";


Object.defineProperty(exports, "__esModule", ({
  value: true
}));
exports.getElementsByTagType = exports.getElementsByTagName = exports.getElementById = exports.getElements = exports.testElement = void 0;
var domhandler_1 = __webpack_require__(1363);
var querying_1 = __webpack_require__(7062);
var Checks = {
  tag_name: function tag_name(name) {
    if (typeof name === "function") {
      return function (elem) {
        return (0, domhandler_1.isTag)(elem) && name(elem.name);
      };
    } else if (name === "*") {
      return domhandler_1.isTag;
    }
    return function (elem) {
      return (0, domhandler_1.isTag)(elem) && elem.name === name;
    };
  },
  tag_type: function tag_type(type) {
    if (typeof type === "function") {
      return function (elem) {
        return type(elem.type);
      };
    }
    return function (elem) {
      return elem.type === type;
    };
  },
  tag_contains: function tag_contains(data) {
    if (typeof data === "function") {
      return function (elem) {
        return (0, domhandler_1.isText)(elem) && data(elem.data);
      };
    }
    return function (elem) {
      return (0, domhandler_1.isText)(elem) && elem.data === data;
    };
  }
};
/**
 * @param attrib Attribute to check.
 * @param value Attribute value to look for.
 * @returns A function to check whether the a node has an attribute with a particular value.
 */
function getAttribCheck(attrib, value) {
  if (typeof value === "function") {
    return function (elem) {
      return (0, domhandler_1.isTag)(elem) && value(elem.attribs[attrib]);
    };
  }
  return function (elem) {
    return (0, domhandler_1.isTag)(elem) && elem.attribs[attrib] === value;
  };
}
/**
 * @param a First function to combine.
 * @param b Second function to combine.
 * @returns A function taking a node and returning `true` if either
 * of the input functions returns `true` for the node.
 */
function combineFuncs(a, b) {
  return function (elem) {
    return a(elem) || b(elem);
  };
}
/**
 * @param options An object describing nodes to look for.
 * @returns A function executing all checks in `options` and returning `true`
 * if any of them match a node.
 */
function compileTest(options) {
  var funcs = Object.keys(options).map(function (key) {
    var value = options[key];
    return Object.prototype.hasOwnProperty.call(Checks, key) ? Checks[key](value) : getAttribCheck(key, value);
  });
  return funcs.length === 0 ? null : funcs.reduce(combineFuncs);
}
/**
 * @param options An object describing nodes to look for.
 * @param node The element to test.
 * @returns Whether the element matches the description in `options`.
 */
function testElement(options, node) {
  var test = compileTest(options);
  return test ? test(node) : true;
}
exports.testElement = testElement;
/**
 * @param options An object describing nodes to look for.
 * @param nodes Nodes to search through.
 * @param recurse Also consider child nodes.
 * @param limit Maximum number of nodes to return.
 * @returns All nodes that match `options`.
 */
function getElements(options, nodes, recurse, limit) {
  if (limit === void 0) {
    limit = Infinity;
  }
  var test = compileTest(options);
  return test ? (0, querying_1.filter)(test, nodes, recurse, limit) : [];
}
exports.getElements = getElements;
/**
 * @param id The unique ID attribute value to look for.
 * @param nodes Nodes to search through.
 * @param recurse Also consider child nodes.
 * @returns The node with the supplied ID.
 */
function getElementById(id, nodes, recurse) {
  if (recurse === void 0) {
    recurse = true;
  }
  if (!Array.isArray(nodes)) nodes = [nodes];
  return (0, querying_1.findOne)(getAttribCheck("id", id), nodes, recurse);
}
exports.getElementById = getElementById;
/**
 * @param tagName Tag name to search for.
 * @param nodes Nodes to search through.
 * @param recurse Also consider child nodes.
 * @param limit Maximum number of nodes to return.
 * @returns All nodes with the supplied `tagName`.
 */
function getElementsByTagName(tagName, nodes, recurse, limit) {
  if (recurse === void 0) {
    recurse = true;
  }
  if (limit === void 0) {
    limit = Infinity;
  }
  return (0, querying_1.filter)(Checks.tag_name(tagName), nodes, recurse, limit);
}
exports.getElementsByTagName = getElementsByTagName;
/**
 * @param type Element type to look for.
 * @param nodes Nodes to search through.
 * @param recurse Also consider child nodes.
 * @param limit Maximum number of nodes to return.
 * @returns All nodes with the supplied `type`.
 */
function getElementsByTagType(type, nodes, recurse, limit) {
  if (recurse === void 0) {
    recurse = true;
  }
  if (limit === void 0) {
    limit = Infinity;
  }
  return (0, querying_1.filter)(Checks.tag_type(type), nodes, recurse, limit);
}
exports.getElementsByTagType = getElementsByTagType;

/***/ }),

/***/ 1833:
/***/ ((__unused_webpack_module, exports) => {

"use strict";


Object.defineProperty(exports, "__esModule", ({
  value: true
}));
exports.prepend = exports.prependChild = exports.append = exports.appendChild = exports.replaceElement = exports.removeElement = void 0;
/**
 * Remove an element from the dom
 *
 * @param elem The element to be removed
 */
function removeElement(elem) {
  if (elem.prev) elem.prev.next = elem.next;
  if (elem.next) elem.next.prev = elem.prev;
  if (elem.parent) {
    var childs = elem.parent.children;
    childs.splice(childs.lastIndexOf(elem), 1);
  }
}
exports.removeElement = removeElement;
/**
 * Replace an element in the dom
 *
 * @param elem The element to be replaced
 * @param replacement The element to be added
 */
function replaceElement(elem, replacement) {
  var prev = replacement.prev = elem.prev;
  if (prev) {
    prev.next = replacement;
  }
  var next = replacement.next = elem.next;
  if (next) {
    next.prev = replacement;
  }
  var parent = replacement.parent = elem.parent;
  if (parent) {
    var childs = parent.children;
    childs[childs.lastIndexOf(elem)] = replacement;
  }
}
exports.replaceElement = replaceElement;
/**
 * Append a child to an element.
 *
 * @param elem The element to append to.
 * @param child The element to be added as a child.
 */
function appendChild(elem, child) {
  removeElement(child);
  child.next = null;
  child.parent = elem;
  if (elem.children.push(child) > 1) {
    var sibling = elem.children[elem.children.length - 2];
    sibling.next = child;
    child.prev = sibling;
  } else {
    child.prev = null;
  }
}
exports.appendChild = appendChild;
/**
 * Append an element after another.
 *
 * @param elem The element to append after.
 * @param next The element be added.
 */
function append(elem, next) {
  removeElement(next);
  var parent = elem.parent;
  var currNext = elem.next;
  next.next = currNext;
  next.prev = elem;
  elem.next = next;
  next.parent = parent;
  if (currNext) {
    currNext.prev = next;
    if (parent) {
      var childs = parent.children;
      childs.splice(childs.lastIndexOf(currNext), 0, next);
    }
  } else if (parent) {
    parent.children.push(next);
  }
}
exports.append = append;
/**
 * Prepend a child to an element.
 *
 * @param elem The element to prepend before.
 * @param child The element to be added as a child.
 */
function prependChild(elem, child) {
  removeElement(child);
  child.parent = elem;
  child.prev = null;
  if (elem.children.unshift(child) !== 1) {
    var sibling = elem.children[1];
    sibling.prev = child;
    child.next = sibling;
  } else {
    child.next = null;
  }
}
exports.prependChild = prependChild;
/**
 * Prepend an element before another.
 *
 * @param elem The element to prepend before.
 * @param prev The element be added.
 */
function prepend(elem, prev) {
  removeElement(prev);
  var parent = elem.parent;
  if (parent) {
    var childs = parent.children;
    childs.splice(childs.indexOf(elem), 0, prev);
  }
  if (elem.prev) {
    elem.prev.next = prev;
  }
  prev.parent = parent;
  prev.prev = elem.prev;
  prev.next = elem;
  elem.prev = prev;
}
exports.prepend = prepend;

/***/ }),

/***/ 7062:
/***/ ((__unused_webpack_module, exports, __webpack_require__) => {

"use strict";


Object.defineProperty(exports, "__esModule", ({
  value: true
}));
exports.findAll = exports.existsOne = exports.findOne = exports.findOneChild = exports.find = exports.filter = void 0;
var domhandler_1 = __webpack_require__(1363);
/**
 * Search a node and its children for nodes passing a test function.
 *
 * @param test Function to test nodes on.
 * @param node Node to search. Will be included in the result set if it matches.
 * @param recurse Also consider child nodes.
 * @param limit Maximum number of nodes to return.
 * @returns All nodes passing `test`.
 */
function filter(test, node, recurse, limit) {
  if (recurse === void 0) {
    recurse = true;
  }
  if (limit === void 0) {
    limit = Infinity;
  }
  if (!Array.isArray(node)) node = [node];
  return find(test, node, recurse, limit);
}
exports.filter = filter;
/**
 * Search an array of node and its children for nodes passing a test function.
 *
 * @param test Function to test nodes on.
 * @param nodes Array of nodes to search.
 * @param recurse Also consider child nodes.
 * @param limit Maximum number of nodes to return.
 * @returns All nodes passing `test`.
 */
function find(test, nodes, recurse, limit) {
  var result = [];
  for (var _i = 0, nodes_1 = nodes; _i < nodes_1.length; _i++) {
    var elem = nodes_1[_i];
    if (test(elem)) {
      result.push(elem);
      if (--limit <= 0) break;
    }
    if (recurse && (0, domhandler_1.hasChildren)(elem) && elem.children.length > 0) {
      var children = find(test, elem.children, recurse, limit);
      result.push.apply(result, children);
      limit -= children.length;
      if (limit <= 0) break;
    }
  }
  return result;
}
exports.find = find;
/**
 * Finds the first element inside of an array that matches a test function.
 *
 * @param test Function to test nodes on.
 * @param nodes Array of nodes to search.
 * @returns The first node in the array that passes `test`.
 */
function findOneChild(test, nodes) {
  return nodes.find(test);
}
exports.findOneChild = findOneChild;
/**
 * Finds one element in a tree that passes a test.
 *
 * @param test Function to test nodes on.
 * @param nodes Array of nodes to search.
 * @param recurse Also consider child nodes.
 * @returns The first child node that passes `test`.
 */
function findOne(test, nodes, recurse) {
  if (recurse === void 0) {
    recurse = true;
  }
  var elem = null;
  for (var i = 0; i < nodes.length && !elem; i++) {
    var checked = nodes[i];
    if (!(0, domhandler_1.isTag)(checked)) {
      continue;
    } else if (test(checked)) {
      elem = checked;
    } else if (recurse && checked.children.length > 0) {
      elem = findOne(test, checked.children);
    }
  }
  return elem;
}
exports.findOne = findOne;
/**
 * @param test Function to test nodes on.
 * @param nodes Array of nodes to search.
 * @returns Whether a tree of nodes contains at least one node passing a test.
 */
function existsOne(test, nodes) {
  return nodes.some(function (checked) {
    return (0, domhandler_1.isTag)(checked) && (test(checked) || checked.children.length > 0 && existsOne(test, checked.children));
  });
}
exports.existsOne = existsOne;
/**
 * Search and array of nodes and its children for nodes passing a test function.
 *
 * Same as `find`, only with less options, leading to reduced complexity.
 *
 * @param test Function to test nodes on.
 * @param nodes Array of nodes to search.
 * @returns All nodes passing `test`.
 */
function findAll(test, nodes) {
  var _a;
  var result = [];
  var stack = nodes.filter(domhandler_1.isTag);
  var elem;
  while (elem = stack.shift()) {
    var children = (_a = elem.children) === null || _a === void 0 ? void 0 : _a.filter(domhandler_1.isTag);
    if (children && children.length > 0) {
      stack.unshift.apply(stack, children);
    }
    if (test(elem)) result.push(elem);
  }
  return result;
}
exports.findAll = findAll;

/***/ }),

/***/ 3633:
/***/ (function(__unused_webpack_module, exports, __webpack_require__) {

"use strict";


var __importDefault = this && this.__importDefault || function (mod) {
  return mod && mod.__esModule ? mod : {
    "default": mod
  };
};
Object.defineProperty(exports, "__esModule", ({
  value: true
}));
exports.innerText = exports.textContent = exports.getText = exports.getInnerHTML = exports.getOuterHTML = void 0;
var domhandler_1 = __webpack_require__(1363);
var dom_serializer_1 = __importDefault(__webpack_require__(1671));
var domelementtype_1 = __webpack_require__(7304);
/**
 * @param node Node to get the outer HTML of.
 * @param options Options for serialization.
 * @deprecated Use the `dom-serializer` module directly.
 * @returns `node`'s outer HTML.
 */
function getOuterHTML(node, options) {
  return (0, dom_serializer_1["default"])(node, options);
}
exports.getOuterHTML = getOuterHTML;
/**
 * @param node Node to get the inner HTML of.
 * @param options Options for serialization.
 * @deprecated Use the `dom-serializer` module directly.
 * @returns `node`'s inner HTML.
 */
function getInnerHTML(node, options) {
  return (0, domhandler_1.hasChildren)(node) ? node.children.map(function (node) {
    return getOuterHTML(node, options);
  }).join("") : "";
}
exports.getInnerHTML = getInnerHTML;
/**
 * Get a node's inner text. Same as `textContent`, but inserts newlines for `<br>` tags.
 *
 * @deprecated Use `textContent` instead.
 * @param node Node to get the inner text of.
 * @returns `node`'s inner text.
 */
function getText(node) {
  if (Array.isArray(node)) return node.map(getText).join("");
  if ((0, domhandler_1.isTag)(node)) return node.name === "br" ? "\n" : getText(node.children);
  if ((0, domhandler_1.isCDATA)(node)) return getText(node.children);
  if ((0, domhandler_1.isText)(node)) return node.data;
  return "";
}
exports.getText = getText;
/**
 * Get a node's text content.
 *
 * @param node Node to get the text content of.
 * @returns `node`'s text content.
 * @see {@link https://developer.mozilla.org/en-US/docs/Web/API/Node/textContent}
 */
function textContent(node) {
  if (Array.isArray(node)) return node.map(textContent).join("");
  if ((0, domhandler_1.hasChildren)(node) && !(0, domhandler_1.isComment)(node)) {
    return textContent(node.children);
  }
  if ((0, domhandler_1.isText)(node)) return node.data;
  return "";
}
exports.textContent = textContent;
/**
 * Get a node's inner text.
 *
 * @param node Node to get the inner text of.
 * @returns `node`'s inner text.
 * @see {@link https://developer.mozilla.org/en-US/docs/Web/API/Node/innerText}
 */
function innerText(node) {
  if (Array.isArray(node)) return node.map(innerText).join("");
  if ((0, domhandler_1.hasChildren)(node) && (node.type === domelementtype_1.ElementType.Tag || (0, domhandler_1.isCDATA)(node))) {
    return innerText(node.children);
  }
  if ((0, domhandler_1.isText)(node)) return node.data;
  return "";
}
exports.innerText = innerText;

/***/ }),

/***/ 6530:
/***/ ((__unused_webpack_module, exports, __webpack_require__) => {

"use strict";


Object.defineProperty(exports, "__esModule", ({
  value: true
}));
exports.prevElementSibling = exports.nextElementSibling = exports.getName = exports.hasAttrib = exports.getAttributeValue = exports.getSiblings = exports.getParent = exports.getChildren = void 0;
var domhandler_1 = __webpack_require__(1363);
var emptyArray = [];
/**
 * Get a node's children.
 *
 * @param elem Node to get the children of.
 * @returns `elem`'s children, or an empty array.
 */
function getChildren(elem) {
  var _a;
  return (_a = elem.children) !== null && _a !== void 0 ? _a : emptyArray;
}
exports.getChildren = getChildren;
/**
 * Get a node's parent.
 *
 * @param elem Node to get the parent of.
 * @returns `elem`'s parent node.
 */
function getParent(elem) {
  return elem.parent || null;
}
exports.getParent = getParent;
/**
 * Gets an elements siblings, including the element itself.
 *
 * Attempts to get the children through the element's parent first.
 * If we don't have a parent (the element is a root node),
 * we walk the element's `prev` & `next` to get all remaining nodes.
 *
 * @param elem Element to get the siblings of.
 * @returns `elem`'s siblings.
 */
function getSiblings(elem) {
  var _a, _b;
  var parent = getParent(elem);
  if (parent != null) return getChildren(parent);
  var siblings = [elem];
  var prev = elem.prev,
    next = elem.next;
  while (prev != null) {
    siblings.unshift(prev);
    _a = prev, prev = _a.prev;
  }
  while (next != null) {
    siblings.push(next);
    _b = next, next = _b.next;
  }
  return siblings;
}
exports.getSiblings = getSiblings;
/**
 * Gets an attribute from an element.
 *
 * @param elem Element to check.
 * @param name Attribute name to retrieve.
 * @returns The element's attribute value, or `undefined`.
 */
function getAttributeValue(elem, name) {
  var _a;
  return (_a = elem.attribs) === null || _a === void 0 ? void 0 : _a[name];
}
exports.getAttributeValue = getAttributeValue;
/**
 * Checks whether an element has an attribute.
 *
 * @param elem Element to check.
 * @param name Attribute name to look for.
 * @returns Returns whether `elem` has the attribute `name`.
 */
function hasAttrib(elem, name) {
  return elem.attribs != null && Object.prototype.hasOwnProperty.call(elem.attribs, name) && elem.attribs[name] != null;
}
exports.hasAttrib = hasAttrib;
/**
 * Get the tag name of an element.
 *
 * @param elem The element to get the name for.
 * @returns The tag name of `elem`.
 */
function getName(elem) {
  return elem.name;
}
exports.getName = getName;
/**
 * Returns the next element sibling of a node.
 *
 * @param elem The element to get the next sibling of.
 * @returns `elem`'s next sibling that is a tag.
 */
function nextElementSibling(elem) {
  var _a;
  var next = elem.next;
  while (next !== null && !(0, domhandler_1.isTag)(next)) {
    _a = next, next = _a.next;
  }
  return next;
}
exports.nextElementSibling = nextElementSibling;
/**
 * Returns the previous element sibling of a node.
 *
 * @param elem The element to get the previous sibling of.
 * @returns `elem`'s previous sibling that is a tag.
 */
function prevElementSibling(elem) {
  var _a;
  var prev = elem.prev;
  while (prev !== null && !(0, domhandler_1.isTag)(prev)) {
    _a = prev, prev = _a.prev;
  }
  return prev;
}
exports.prevElementSibling = prevElementSibling;

/***/ }),

/***/ 6347:
/***/ (function(__unused_webpack_module, exports, __webpack_require__) {

"use strict";


var __importDefault = this && this.__importDefault || function (mod) {
  return mod && mod.__esModule ? mod : {
    "default": mod
  };
};
Object.defineProperty(exports, "__esModule", ({
  value: true
}));
exports.decodeHTML = exports.decodeHTMLStrict = exports.decodeXML = void 0;
var entities_json_1 = __importDefault(__webpack_require__(9323));
var legacy_json_1 = __importDefault(__webpack_require__(9591));
var xml_json_1 = __importDefault(__webpack_require__(2586));
var decode_codepoint_1 = __importDefault(__webpack_require__(8271));
var strictEntityRe = /&(?:[a-zA-Z0-9]+|#[xX][\da-fA-F]+|#\d+);/g;
exports.decodeXML = getStrictDecoder(xml_json_1["default"]);
exports.decodeHTMLStrict = getStrictDecoder(entities_json_1["default"]);
function getStrictDecoder(map) {
  var replace = getReplacer(map);
  return function (str) {
    return String(str).replace(strictEntityRe, replace);
  };
}
var sorter = function sorter(a, b) {
  return a < b ? 1 : -1;
};
exports.decodeHTML = function () {
  var legacy = Object.keys(legacy_json_1["default"]).sort(sorter);
  var keys = Object.keys(entities_json_1["default"]).sort(sorter);
  for (var i = 0, j = 0; i < keys.length; i++) {
    if (legacy[j] === keys[i]) {
      keys[i] += ";?";
      j++;
    } else {
      keys[i] += ";";
    }
  }
  var re = new RegExp("&(?:" + keys.join("|") + "|#[xX][\\da-fA-F]+;?|#\\d+;?)", "g");
  var replace = getReplacer(entities_json_1["default"]);
  function replacer(str) {
    if (str.substr(-1) !== ";") str += ";";
    return replace(str);
  }
  // TODO consider creating a merged map
  return function (str) {
    return String(str).replace(re, replacer);
  };
}();
function getReplacer(map) {
  return function replace(str) {
    if (str.charAt(1) === "#") {
      var secondChar = str.charAt(2);
      if (secondChar === "X" || secondChar === "x") {
        return decode_codepoint_1["default"](parseInt(str.substr(3), 16));
      }
      return decode_codepoint_1["default"](parseInt(str.substr(2), 10));
    }
    // eslint-disable-next-line @typescript-eslint/prefer-nullish-coalescing
    return map[str.slice(1, -1)] || str;
  };
}

/***/ }),

/***/ 8271:
/***/ (function(__unused_webpack_module, exports, __webpack_require__) {

"use strict";


var __importDefault = this && this.__importDefault || function (mod) {
  return mod && mod.__esModule ? mod : {
    "default": mod
  };
};
Object.defineProperty(exports, "__esModule", ({
  value: true
}));
var decode_json_1 = __importDefault(__webpack_require__(3600));
// Adapted from https://github.com/mathiasbynens/he/blob/master/src/he.js#L94-L119
var fromCodePoint =
// eslint-disable-next-line @typescript-eslint/no-unnecessary-condition
String.fromCodePoint || function (codePoint) {
  var output = "";
  if (codePoint > 0xffff) {
    codePoint -= 0x10000;
    output += String.fromCharCode(codePoint >>> 10 & 0x3ff | 0xd800);
    codePoint = 0xdc00 | codePoint & 0x3ff;
  }
  output += String.fromCharCode(codePoint);
  return output;
};
function decodeCodePoint(codePoint) {
  if (codePoint >= 0xd800 && codePoint <= 0xdfff || codePoint > 0x10ffff) {
    return "\uFFFD";
  }
  if (codePoint in decode_json_1["default"]) {
    codePoint = decode_json_1["default"][codePoint];
  }
  return fromCodePoint(codePoint);
}
exports["default"] = decodeCodePoint;

/***/ }),

/***/ 3393:
/***/ (function(__unused_webpack_module, exports, __webpack_require__) {

"use strict";


var __importDefault = this && this.__importDefault || function (mod) {
  return mod && mod.__esModule ? mod : {
    "default": mod
  };
};
Object.defineProperty(exports, "__esModule", ({
  value: true
}));
exports.escapeUTF8 = exports.escape = exports.encodeNonAsciiHTML = exports.encodeHTML = exports.encodeXML = void 0;
var xml_json_1 = __importDefault(__webpack_require__(2586));
var inverseXML = getInverseObj(xml_json_1["default"]);
var xmlReplacer = getInverseReplacer(inverseXML);
/**
 * Encodes all non-ASCII characters, as well as characters not valid in XML
 * documents using XML entities.
 *
 * If a character has no equivalent entity, a
 * numeric hexadecimal reference (eg. `&#xfc;`) will be used.
 */
exports.encodeXML = getASCIIEncoder(inverseXML);
var entities_json_1 = __importDefault(__webpack_require__(9323));
var inverseHTML = getInverseObj(entities_json_1["default"]);
var htmlReplacer = getInverseReplacer(inverseHTML);
/**
 * Encodes all entities and non-ASCII characters in the input.
 *
 * This includes characters that are valid ASCII characters in HTML documents.
 * For example `#` will be encoded as `&num;`. To get a more compact output,
 * consider using the `encodeNonAsciiHTML` function.
 *
 * If a character has no equivalent entity, a
 * numeric hexadecimal reference (eg. `&#xfc;`) will be used.
 */
exports.encodeHTML = getInverse(inverseHTML, htmlReplacer);
/**
 * Encodes all non-ASCII characters, as well as characters not valid in HTML
 * documents using HTML entities.
 *
 * If a character has no equivalent entity, a
 * numeric hexadecimal reference (eg. `&#xfc;`) will be used.
 */
exports.encodeNonAsciiHTML = getASCIIEncoder(inverseHTML);
function getInverseObj(obj) {
  return Object.keys(obj).sort().reduce(function (inverse, name) {
    inverse[obj[name]] = "&" + name + ";";
    return inverse;
  }, {});
}
function getInverseReplacer(inverse) {
  var single = [];
  var multiple = [];
  for (var _i = 0, _a = Object.keys(inverse); _i < _a.length; _i++) {
    var k = _a[_i];
    if (k.length === 1) {
      // Add value to single array
      single.push("\\" + k);
    } else {
      // Add value to multiple array
      multiple.push(k);
    }
  }
  // Add ranges to single characters.
  single.sort();
  for (var start = 0; start < single.length - 1; start++) {
    // Find the end of a run of characters
    var end = start;
    while (end < single.length - 1 && single[end].charCodeAt(1) + 1 === single[end + 1].charCodeAt(1)) {
      end += 1;
    }
    var count = 1 + end - start;
    // We want to replace at least three characters
    if (count < 3) continue;
    single.splice(start, count, single[start] + "-" + single[end]);
  }
  multiple.unshift("[" + single.join("") + "]");
  return new RegExp(multiple.join("|"), "g");
}
// /[^\0-\x7F]/gu
var reNonASCII = /(?:[\x80-\uD7FF\uE000-\uFFFF]|[\uD800-\uDBFF][\uDC00-\uDFFF]|[\uD800-\uDBFF](?![\uDC00-\uDFFF])|(?:[^\uD800-\uDBFF]|^)[\uDC00-\uDFFF])/g;
var getCodePoint =
// eslint-disable-next-line @typescript-eslint/no-unnecessary-condition
String.prototype.codePointAt != null ?
// eslint-disable-next-line @typescript-eslint/no-non-null-assertion
function (str) {
  return str.codePointAt(0);
} :
// http://mathiasbynens.be/notes/javascript-encoding#surrogate-formulae
function (c) {
  return (c.charCodeAt(0) - 0xd800) * 0x400 + c.charCodeAt(1) - 0xdc00 + 0x10000;
};
function singleCharReplacer(c) {
  return "&#x" + (c.length > 1 ? getCodePoint(c) : c.charCodeAt(0)).toString(16).toUpperCase() + ";";
}
function getInverse(inverse, re) {
  return function (data) {
    return data.replace(re, function (name) {
      return inverse[name];
    }).replace(reNonASCII, singleCharReplacer);
  };
}
var reEscapeChars = new RegExp(xmlReplacer.source + "|" + reNonASCII.source, "g");
/**
 * Encodes all non-ASCII characters, as well as characters not valid in XML
 * documents using numeric hexadecimal reference (eg. `&#xfc;`).
 *
 * Have a look at `escapeUTF8` if you want a more concise output at the expense
 * of reduced transportability.
 *
 * @param data String to escape.
 */
function escape(data) {
  return data.replace(reEscapeChars, singleCharReplacer);
}
exports.escape = escape;
/**
 * Encodes all characters not valid in XML documents using numeric hexadecimal
 * reference (eg. `&#xfc;`).
 *
 * Note that the output will be character-set dependent.
 *
 * @param data String to escape.
 */
function escapeUTF8(data) {
  return data.replace(xmlReplacer, singleCharReplacer);
}
exports.escapeUTF8 = escapeUTF8;
function getASCIIEncoder(obj) {
  return function (data) {
    return data.replace(reEscapeChars, function (c) {
      return obj[c] || singleCharReplacer(c);
    });
  };
}

/***/ }),

/***/ 7531:
/***/ ((__unused_webpack_module, exports, __webpack_require__) => {

"use strict";


Object.defineProperty(exports, "__esModule", ({
  value: true
}));
exports.decodeXMLStrict = exports.decodeHTML5Strict = exports.decodeHTML4Strict = exports.decodeHTML5 = exports.decodeHTML4 = exports.decodeHTMLStrict = exports.decodeHTML = exports.decodeXML = exports.encodeHTML5 = exports.encodeHTML4 = exports.escapeUTF8 = exports.escape = exports.encodeNonAsciiHTML = exports.encodeHTML = exports.encodeXML = exports.encode = exports.decodeStrict = exports.decode = void 0;
var decode_1 = __webpack_require__(6347);
var encode_1 = __webpack_require__(3393);
/**
 * Decodes a string with entities.
 *
 * @param data String to decode.
 * @param level Optional level to decode at. 0 = XML, 1 = HTML. Default is 0.
 * @deprecated Use `decodeXML` or `decodeHTML` directly.
 */
function decode(data, level) {
  return (!level || level <= 0 ? decode_1.decodeXML : decode_1.decodeHTML)(data);
}
exports.decode = decode;
/**
 * Decodes a string with entities. Does not allow missing trailing semicolons for entities.
 *
 * @param data String to decode.
 * @param level Optional level to decode at. 0 = XML, 1 = HTML. Default is 0.
 * @deprecated Use `decodeHTMLStrict` or `decodeXML` directly.
 */
function decodeStrict(data, level) {
  return (!level || level <= 0 ? decode_1.decodeXML : decode_1.decodeHTMLStrict)(data);
}
exports.decodeStrict = decodeStrict;
/**
 * Encodes a string with entities.
 *
 * @param data String to encode.
 * @param level Optional level to encode at. 0 = XML, 1 = HTML. Default is 0.
 * @deprecated Use `encodeHTML`, `encodeXML` or `encodeNonAsciiHTML` directly.
 */
function encode(data, level) {
  return (!level || level <= 0 ? encode_1.encodeXML : encode_1.encodeHTML)(data);
}
exports.encode = encode;
var encode_2 = __webpack_require__(3393);
Object.defineProperty(exports, "encodeXML", ({
  enumerable: true,
  get: function get() {
    return encode_2.encodeXML;
  }
}));
Object.defineProperty(exports, "encodeHTML", ({
  enumerable: true,
  get: function get() {
    return encode_2.encodeHTML;
  }
}));
Object.defineProperty(exports, "encodeNonAsciiHTML", ({
  enumerable: true,
  get: function get() {
    return encode_2.encodeNonAsciiHTML;
  }
}));
Object.defineProperty(exports, "escape", ({
  enumerable: true,
  get: function get() {
    return encode_2.escape;
  }
}));
Object.defineProperty(exports, "escapeUTF8", ({
  enumerable: true,
  get: function get() {
    return encode_2.escapeUTF8;
  }
}));
// Legacy aliases (deprecated)
Object.defineProperty(exports, "encodeHTML4", ({
  enumerable: true,
  get: function get() {
    return encode_2.encodeHTML;
  }
}));
Object.defineProperty(exports, "encodeHTML5", ({
  enumerable: true,
  get: function get() {
    return encode_2.encodeHTML;
  }
}));
var decode_2 = __webpack_require__(6347);
Object.defineProperty(exports, "decodeXML", ({
  enumerable: true,
  get: function get() {
    return decode_2.decodeXML;
  }
}));
Object.defineProperty(exports, "decodeHTML", ({
  enumerable: true,
  get: function get() {
    return decode_2.decodeHTML;
  }
}));
Object.defineProperty(exports, "decodeHTMLStrict", ({
  enumerable: true,
  get: function get() {
    return decode_2.decodeHTMLStrict;
  }
}));
// Legacy aliases (deprecated)
Object.defineProperty(exports, "decodeHTML4", ({
  enumerable: true,
  get: function get() {
    return decode_2.decodeHTML;
  }
}));
Object.defineProperty(exports, "decodeHTML5", ({
  enumerable: true,
  get: function get() {
    return decode_2.decodeHTML;
  }
}));
Object.defineProperty(exports, "decodeHTML4Strict", ({
  enumerable: true,
  get: function get() {
    return decode_2.decodeHTMLStrict;
  }
}));
Object.defineProperty(exports, "decodeHTML5Strict", ({
  enumerable: true,
  get: function get() {
    return decode_2.decodeHTMLStrict;
  }
}));
Object.defineProperty(exports, "decodeXMLStrict", ({
  enumerable: true,
  get: function get() {
    return decode_2.decodeXML;
  }
}));

/***/ }),

/***/ 2369:
/***/ (function(__unused_webpack_module, exports, __webpack_require__) {

"use strict";


function _typeof(obj) { "@babel/helpers - typeof"; return _typeof = "function" == typeof Symbol && "symbol" == typeof Symbol.iterator ? function (obj) { return typeof obj; } : function (obj) { return obj && "function" == typeof Symbol && obj.constructor === Symbol && obj !== Symbol.prototype ? "symbol" : typeof obj; }, _typeof(obj); }
var __extends = this && this.__extends || function () {
  var _extendStatics = function extendStatics(d, b) {
    _extendStatics = Object.setPrototypeOf || {
      __proto__: []
    } instanceof Array && function (d, b) {
      d.__proto__ = b;
    } || function (d, b) {
      for (var p in b) {
        if (Object.prototype.hasOwnProperty.call(b, p)) d[p] = b[p];
      }
    };
    return _extendStatics(d, b);
  };
  return function (d, b) {
    if (typeof b !== "function" && b !== null) throw new TypeError("Class extends value " + String(b) + " is not a constructor or null");
    _extendStatics(d, b);
    function __() {
      this.constructor = d;
    }
    d.prototype = b === null ? Object.create(b) : (__.prototype = b.prototype, new __());
  };
}();
var __createBinding = this && this.__createBinding || (Object.create ? function (o, m, k, k2) {
  if (k2 === undefined) k2 = k;
  Object.defineProperty(o, k2, {
    enumerable: true,
    get: function get() {
      return m[k];
    }
  });
} : function (o, m, k, k2) {
  if (k2 === undefined) k2 = k;
  o[k2] = m[k];
});
var __setModuleDefault = this && this.__setModuleDefault || (Object.create ? function (o, v) {
  Object.defineProperty(o, "default", {
    enumerable: true,
    value: v
  });
} : function (o, v) {
  o["default"] = v;
});
var __importStar = this && this.__importStar || function (mod) {
  if (mod && mod.__esModule) return mod;
  var result = {};
  if (mod != null) for (var k in mod) {
    if (k !== "default" && Object.prototype.hasOwnProperty.call(mod, k)) __createBinding(result, mod, k);
  }
  __setModuleDefault(result, mod);
  return result;
};
var __importDefault = this && this.__importDefault || function (mod) {
  return mod && mod.__esModule ? mod : {
    "default": mod
  };
};
Object.defineProperty(exports, "__esModule", ({
  value: true
}));
exports.parseFeed = exports.FeedHandler = void 0;
var domhandler_1 = __importDefault(__webpack_require__(1363));
var DomUtils = __importStar(__webpack_require__(5511));
var Parser_1 = __webpack_require__(8168);
var FeedItemMediaMedium;
(function (FeedItemMediaMedium) {
  FeedItemMediaMedium[FeedItemMediaMedium["image"] = 0] = "image";
  FeedItemMediaMedium[FeedItemMediaMedium["audio"] = 1] = "audio";
  FeedItemMediaMedium[FeedItemMediaMedium["video"] = 2] = "video";
  FeedItemMediaMedium[FeedItemMediaMedium["document"] = 3] = "document";
  FeedItemMediaMedium[FeedItemMediaMedium["executable"] = 4] = "executable";
})(FeedItemMediaMedium || (FeedItemMediaMedium = {}));
var FeedItemMediaExpression;
(function (FeedItemMediaExpression) {
  FeedItemMediaExpression[FeedItemMediaExpression["sample"] = 0] = "sample";
  FeedItemMediaExpression[FeedItemMediaExpression["full"] = 1] = "full";
  FeedItemMediaExpression[FeedItemMediaExpression["nonstop"] = 2] = "nonstop";
})(FeedItemMediaExpression || (FeedItemMediaExpression = {}));
// TODO: Consume data as it is coming in
var FeedHandler = /** @class */function (_super) {
  __extends(FeedHandler, _super);
  /**
   *
   * @param callback
   * @param options
   */
  function FeedHandler(callback, options) {
    var _this = this;
    if (_typeof(callback) === "object") {
      callback = undefined;
      options = callback;
    }
    _this = _super.call(this, callback, options) || this;
    return _this;
  }
  FeedHandler.prototype.onend = function () {
    var _a, _b;
    var feedRoot = getOneElement(isValidFeed, this.dom);
    if (!feedRoot) {
      this.handleCallback(new Error("couldn't find root of feed"));
      return;
    }
    var feed = {};
    if (feedRoot.name === "feed") {
      var childs = feedRoot.children;
      feed.type = "atom";
      addConditionally(feed, "id", "id", childs);
      addConditionally(feed, "title", "title", childs);
      var href = getAttribute("href", getOneElement("link", childs));
      if (href) {
        feed.link = href;
      }
      addConditionally(feed, "description", "subtitle", childs);
      var updated = fetch("updated", childs);
      if (updated) {
        feed.updated = new Date(updated);
      }
      addConditionally(feed, "author", "email", childs, true);
      feed.items = getElements("entry", childs).map(function (item) {
        var entry = {};
        var children = item.children;
        addConditionally(entry, "id", "id", children);
        addConditionally(entry, "title", "title", children);
        var href = getAttribute("href", getOneElement("link", children));
        if (href) {
          entry.link = href;
        }
        var description = fetch("summary", children) || fetch("content", children);
        if (description) {
          entry.description = description;
        }
        var pubDate = fetch("updated", children);
        if (pubDate) {
          entry.pubDate = new Date(pubDate);
        }
        entry.media = getMediaElements(children);
        return entry;
      });
    } else {
      var childs = (_b = (_a = getOneElement("channel", feedRoot.children)) === null || _a === void 0 ? void 0 : _a.children) !== null && _b !== void 0 ? _b : [];
      feed.type = feedRoot.name.substr(0, 3);
      feed.id = "";
      addConditionally(feed, "title", "title", childs);
      addConditionally(feed, "link", "link", childs);
      addConditionally(feed, "description", "description", childs);
      var updated = fetch("lastBuildDate", childs);
      if (updated) {
        feed.updated = new Date(updated);
      }
      addConditionally(feed, "author", "managingEditor", childs, true);
      feed.items = getElements("item", feedRoot.children).map(function (item) {
        var entry = {};
        var children = item.children;
        addConditionally(entry, "id", "guid", children);
        addConditionally(entry, "title", "title", children);
        addConditionally(entry, "link", "link", children);
        addConditionally(entry, "description", "description", children);
        var pubDate = fetch("pubDate", children);
        if (pubDate) entry.pubDate = new Date(pubDate);
        entry.media = getMediaElements(children);
        return entry;
      });
    }
    this.feed = feed;
    this.handleCallback(null);
  };
  return FeedHandler;
}(domhandler_1["default"]);
exports.FeedHandler = FeedHandler;
function getMediaElements(where) {
  return getElements("media:content", where).map(function (elem) {
    var media = {
      medium: elem.attribs.medium,
      isDefault: !!elem.attribs.isDefault
    };
    if (elem.attribs.url) {
      media.url = elem.attribs.url;
    }
    if (elem.attribs.fileSize) {
      media.fileSize = parseInt(elem.attribs.fileSize, 10);
    }
    if (elem.attribs.type) {
      media.type = elem.attribs.type;
    }
    if (elem.attribs.expression) {
      media.expression = elem.attribs.expression;
    }
    if (elem.attribs.bitrate) {
      media.bitrate = parseInt(elem.attribs.bitrate, 10);
    }
    if (elem.attribs.framerate) {
      media.framerate = parseInt(elem.attribs.framerate, 10);
    }
    if (elem.attribs.samplingrate) {
      media.samplingrate = parseInt(elem.attribs.samplingrate, 10);
    }
    if (elem.attribs.channels) {
      media.channels = parseInt(elem.attribs.channels, 10);
    }
    if (elem.attribs.duration) {
      media.duration = parseInt(elem.attribs.duration, 10);
    }
    if (elem.attribs.height) {
      media.height = parseInt(elem.attribs.height, 10);
    }
    if (elem.attribs.width) {
      media.width = parseInt(elem.attribs.width, 10);
    }
    if (elem.attribs.lang) {
      media.lang = elem.attribs.lang;
    }
    return media;
  });
}
function getElements(tagName, where) {
  return DomUtils.getElementsByTagName(tagName, where, true);
}
function getOneElement(tagName, node) {
  return DomUtils.getElementsByTagName(tagName, node, true, 1)[0];
}
function fetch(tagName, where, recurse) {
  if (recurse === void 0) {
    recurse = false;
  }
  return DomUtils.getText(DomUtils.getElementsByTagName(tagName, where, recurse, 1)).trim();
}
function getAttribute(name, elem) {
  if (!elem) {
    return null;
  }
  var attribs = elem.attribs;
  return attribs[name];
}
function addConditionally(obj, prop, what, where, recurse) {
  if (recurse === void 0) {
    recurse = false;
  }
  var tmp = fetch(what, where, recurse);
  if (tmp) obj[prop] = tmp;
}
function isValidFeed(value) {
  return value === "rss" || value === "feed" || value === "rdf:RDF";
}
/**
 * Parse a feed.
 *
 * @param feed The feed that should be parsed, as a string.
 * @param options Optionally, options for parsing. When using this option, you should set `xmlMode` to `true`.
 */
function parseFeed(feed, options) {
  if (options === void 0) {
    options = {
      xmlMode: true
    };
  }
  var handler = new FeedHandler(options);
  new Parser_1.Parser(handler, options).end(feed);
  return handler.feed;
}
exports.parseFeed = parseFeed;

/***/ }),

/***/ 8168:
/***/ (function(__unused_webpack_module, exports, __webpack_require__) {

"use strict";


var __importDefault = this && this.__importDefault || function (mod) {
  return mod && mod.__esModule ? mod : {
    "default": mod
  };
};
Object.defineProperty(exports, "__esModule", ({
  value: true
}));
exports.Parser = void 0;
var Tokenizer_1 = __importDefault(__webpack_require__(6506));
var formTags = new Set(["input", "option", "optgroup", "select", "button", "datalist", "textarea"]);
var pTag = new Set(["p"]);
var openImpliesClose = {
  tr: new Set(["tr", "th", "td"]),
  th: new Set(["th"]),
  td: new Set(["thead", "th", "td"]),
  body: new Set(["head", "link", "script"]),
  li: new Set(["li"]),
  p: pTag,
  h1: pTag,
  h2: pTag,
  h3: pTag,
  h4: pTag,
  h5: pTag,
  h6: pTag,
  select: formTags,
  input: formTags,
  output: formTags,
  button: formTags,
  datalist: formTags,
  textarea: formTags,
  option: new Set(["option"]),
  optgroup: new Set(["optgroup", "option"]),
  dd: new Set(["dt", "dd"]),
  dt: new Set(["dt", "dd"]),
  address: pTag,
  article: pTag,
  aside: pTag,
  blockquote: pTag,
  details: pTag,
  div: pTag,
  dl: pTag,
  fieldset: pTag,
  figcaption: pTag,
  figure: pTag,
  footer: pTag,
  form: pTag,
  header: pTag,
  hr: pTag,
  main: pTag,
  nav: pTag,
  ol: pTag,
  pre: pTag,
  section: pTag,
  table: pTag,
  ul: pTag,
  rt: new Set(["rt", "rp"]),
  rp: new Set(["rt", "rp"]),
  tbody: new Set(["thead", "tbody"]),
  tfoot: new Set(["thead", "tbody"])
};
var voidElements = new Set(["area", "base", "basefont", "br", "col", "command", "embed", "frame", "hr", "img", "input", "isindex", "keygen", "link", "meta", "param", "source", "track", "wbr"]);
var foreignContextElements = new Set(["math", "svg"]);
var htmlIntegrationElements = new Set(["mi", "mo", "mn", "ms", "mtext", "annotation-xml", "foreignObject", "desc", "title"]);
var reNameEnd = /\s|\//;
var Parser = /** @class */function () {
  function Parser(cbs, options) {
    if (options === void 0) {
      options = {};
    }
    var _a, _b, _c, _d, _e;
    /** The start index of the last event. */
    this.startIndex = 0;
    /** The end index of the last event. */
    this.endIndex = null;
    this.tagname = "";
    this.attribname = "";
    this.attribvalue = "";
    this.attribs = null;
    this.stack = [];
    this.foreignContext = [];
    this.options = options;
    this.cbs = cbs !== null && cbs !== void 0 ? cbs : {};
    this.lowerCaseTagNames = (_a = options.lowerCaseTags) !== null && _a !== void 0 ? _a : !options.xmlMode;
    this.lowerCaseAttributeNames = (_b = options.lowerCaseAttributeNames) !== null && _b !== void 0 ? _b : !options.xmlMode;
    this.tokenizer = new ((_c = options.Tokenizer) !== null && _c !== void 0 ? _c : Tokenizer_1["default"])(this.options, this);
    (_e = (_d = this.cbs).onparserinit) === null || _e === void 0 ? void 0 : _e.call(_d, this);
  }
  Parser.prototype.updatePosition = function (initialOffset) {
    if (this.endIndex === null) {
      if (this.tokenizer.sectionStart <= initialOffset) {
        this.startIndex = 0;
      } else {
        this.startIndex = this.tokenizer.sectionStart - initialOffset;
      }
    } else {
      this.startIndex = this.endIndex + 1;
    }
    this.endIndex = this.tokenizer.getAbsoluteIndex();
  };
  // Tokenizer event handlers
  Parser.prototype.ontext = function (data) {
    var _a, _b;
    this.updatePosition(1);
    this.endIndex--;
    (_b = (_a = this.cbs).ontext) === null || _b === void 0 ? void 0 : _b.call(_a, data);
  };
  Parser.prototype.onopentagname = function (name) {
    var _a, _b;
    if (this.lowerCaseTagNames) {
      name = name.toLowerCase();
    }
    this.tagname = name;
    if (!this.options.xmlMode && Object.prototype.hasOwnProperty.call(openImpliesClose, name)) {
      var el = void 0;
      while (this.stack.length > 0 && openImpliesClose[name].has(el = this.stack[this.stack.length - 1])) {
        this.onclosetag(el);
      }
    }
    if (this.options.xmlMode || !voidElements.has(name)) {
      this.stack.push(name);
      if (foreignContextElements.has(name)) {
        this.foreignContext.push(true);
      } else if (htmlIntegrationElements.has(name)) {
        this.foreignContext.push(false);
      }
    }
    (_b = (_a = this.cbs).onopentagname) === null || _b === void 0 ? void 0 : _b.call(_a, name);
    if (this.cbs.onopentag) this.attribs = {};
  };
  Parser.prototype.onopentagend = function () {
    var _a, _b;
    this.updatePosition(1);
    if (this.attribs) {
      (_b = (_a = this.cbs).onopentag) === null || _b === void 0 ? void 0 : _b.call(_a, this.tagname, this.attribs);
      this.attribs = null;
    }
    if (!this.options.xmlMode && this.cbs.onclosetag && voidElements.has(this.tagname)) {
      this.cbs.onclosetag(this.tagname);
    }
    this.tagname = "";
  };
  Parser.prototype.onclosetag = function (name) {
    this.updatePosition(1);
    if (this.lowerCaseTagNames) {
      name = name.toLowerCase();
    }
    if (foreignContextElements.has(name) || htmlIntegrationElements.has(name)) {
      this.foreignContext.pop();
    }
    if (this.stack.length && (this.options.xmlMode || !voidElements.has(name))) {
      var pos = this.stack.lastIndexOf(name);
      if (pos !== -1) {
        if (this.cbs.onclosetag) {
          pos = this.stack.length - pos;
          while (pos--) {
            // We know the stack has sufficient elements.
            this.cbs.onclosetag(this.stack.pop());
          }
        } else this.stack.length = pos;
      } else if (name === "p" && !this.options.xmlMode) {
        this.onopentagname(name);
        this.closeCurrentTag();
      }
    } else if (!this.options.xmlMode && (name === "br" || name === "p")) {
      this.onopentagname(name);
      this.closeCurrentTag();
    }
  };
  Parser.prototype.onselfclosingtag = function () {
    if (this.options.xmlMode || this.options.recognizeSelfClosing || this.foreignContext[this.foreignContext.length - 1]) {
      this.closeCurrentTag();
    } else {
      this.onopentagend();
    }
  };
  Parser.prototype.closeCurrentTag = function () {
    var _a, _b;
    var name = this.tagname;
    this.onopentagend();
    /*
     * Self-closing tags will be on the top of the stack
     * (cheaper check than in onclosetag)
     */
    if (this.stack[this.stack.length - 1] === name) {
      (_b = (_a = this.cbs).onclosetag) === null || _b === void 0 ? void 0 : _b.call(_a, name);
      this.stack.pop();
    }
  };
  Parser.prototype.onattribname = function (name) {
    if (this.lowerCaseAttributeNames) {
      name = name.toLowerCase();
    }
    this.attribname = name;
  };
  Parser.prototype.onattribdata = function (value) {
    this.attribvalue += value;
  };
  Parser.prototype.onattribend = function (quote) {
    var _a, _b;
    (_b = (_a = this.cbs).onattribute) === null || _b === void 0 ? void 0 : _b.call(_a, this.attribname, this.attribvalue, quote);
    if (this.attribs && !Object.prototype.hasOwnProperty.call(this.attribs, this.attribname)) {
      this.attribs[this.attribname] = this.attribvalue;
    }
    this.attribname = "";
    this.attribvalue = "";
  };
  Parser.prototype.getInstructionName = function (value) {
    var idx = value.search(reNameEnd);
    var name = idx < 0 ? value : value.substr(0, idx);
    if (this.lowerCaseTagNames) {
      name = name.toLowerCase();
    }
    return name;
  };
  Parser.prototype.ondeclaration = function (value) {
    if (this.cbs.onprocessinginstruction) {
      var name_1 = this.getInstructionName(value);
      this.cbs.onprocessinginstruction("!" + name_1, "!" + value);
    }
  };
  Parser.prototype.onprocessinginstruction = function (value) {
    if (this.cbs.onprocessinginstruction) {
      var name_2 = this.getInstructionName(value);
      this.cbs.onprocessinginstruction("?" + name_2, "?" + value);
    }
  };
  Parser.prototype.oncomment = function (value) {
    var _a, _b, _c, _d;
    this.updatePosition(4);
    (_b = (_a = this.cbs).oncomment) === null || _b === void 0 ? void 0 : _b.call(_a, value);
    (_d = (_c = this.cbs).oncommentend) === null || _d === void 0 ? void 0 : _d.call(_c);
  };
  Parser.prototype.oncdata = function (value) {
    var _a, _b, _c, _d, _e, _f;
    this.updatePosition(1);
    if (this.options.xmlMode || this.options.recognizeCDATA) {
      (_b = (_a = this.cbs).oncdatastart) === null || _b === void 0 ? void 0 : _b.call(_a);
      (_d = (_c = this.cbs).ontext) === null || _d === void 0 ? void 0 : _d.call(_c, value);
      (_f = (_e = this.cbs).oncdataend) === null || _f === void 0 ? void 0 : _f.call(_e);
    } else {
      this.oncomment("[CDATA[" + value + "]]");
    }
  };
  Parser.prototype.onerror = function (err) {
    var _a, _b;
    (_b = (_a = this.cbs).onerror) === null || _b === void 0 ? void 0 : _b.call(_a, err);
  };
  Parser.prototype.onend = function () {
    var _a, _b;
    if (this.cbs.onclosetag) {
      for (var i = this.stack.length; i > 0; this.cbs.onclosetag(this.stack[--i])) {
        ;
      }
    }
    (_b = (_a = this.cbs).onend) === null || _b === void 0 ? void 0 : _b.call(_a);
  };
  /**
   * Resets the parser to a blank state, ready to parse a new HTML document
   */
  Parser.prototype.reset = function () {
    var _a, _b, _c, _d;
    (_b = (_a = this.cbs).onreset) === null || _b === void 0 ? void 0 : _b.call(_a);
    this.tokenizer.reset();
    this.tagname = "";
    this.attribname = "";
    this.attribs = null;
    this.stack = [];
    (_d = (_c = this.cbs).onparserinit) === null || _d === void 0 ? void 0 : _d.call(_c, this);
  };
  /**
   * Resets the parser, then parses a complete document and
   * pushes it to the handler.
   *
   * @param data Document to parse.
   */
  Parser.prototype.parseComplete = function (data) {
    this.reset();
    this.end(data);
  };
  /**
   * Parses a chunk of data and calls the corresponding callbacks.
   *
   * @param chunk Chunk to parse.
   */
  Parser.prototype.write = function (chunk) {
    this.tokenizer.write(chunk);
  };
  /**
   * Parses the end of the buffer and clears the stack, calls onend.
   *
   * @param chunk Optional final chunk to parse.
   */
  Parser.prototype.end = function (chunk) {
    this.tokenizer.end(chunk);
  };
  /**
   * Pauses parsing. The parser won't emit events until `resume` is called.
   */
  Parser.prototype.pause = function () {
    this.tokenizer.pause();
  };
  /**
   * Resumes parsing after `pause` was called.
   */
  Parser.prototype.resume = function () {
    this.tokenizer.resume();
  };
  /**
   * Alias of `write`, for backwards compatibility.
   *
   * @param chunk Chunk to parse.
   * @deprecated
   */
  Parser.prototype.parseChunk = function (chunk) {
    this.write(chunk);
  };
  /**
   * Alias of `end`, for backwards compatibility.
   *
   * @param chunk Optional final chunk to parse.
   * @deprecated
   */
  Parser.prototype.done = function (chunk) {
    this.end(chunk);
  };
  return Parser;
}();
exports.Parser = Parser;

/***/ }),

/***/ 6506:
/***/ (function(__unused_webpack_module, exports, __webpack_require__) {

"use strict";


var __importDefault = this && this.__importDefault || function (mod) {
  return mod && mod.__esModule ? mod : {
    "default": mod
  };
};
Object.defineProperty(exports, "__esModule", ({
  value: true
}));
var decode_codepoint_1 = __importDefault(__webpack_require__(8271));
var entities_json_1 = __importDefault(__webpack_require__(9323));
var legacy_json_1 = __importDefault(__webpack_require__(9591));
var xml_json_1 = __importDefault(__webpack_require__(2586));
function whitespace(c) {
  return c === " " || c === "\n" || c === "\t" || c === "\f" || c === "\r";
}
function isASCIIAlpha(c) {
  return c >= "a" && c <= "z" || c >= "A" && c <= "Z";
}
function ifElseState(upper, SUCCESS, FAILURE) {
  var lower = upper.toLowerCase();
  if (upper === lower) {
    return function (t, c) {
      if (c === lower) {
        t._state = SUCCESS;
      } else {
        t._state = FAILURE;
        t._index--;
      }
    };
  }
  return function (t, c) {
    if (c === lower || c === upper) {
      t._state = SUCCESS;
    } else {
      t._state = FAILURE;
      t._index--;
    }
  };
}
function consumeSpecialNameChar(upper, NEXT_STATE) {
  var lower = upper.toLowerCase();
  return function (t, c) {
    if (c === lower || c === upper) {
      t._state = NEXT_STATE;
    } else {
      t._state = 3 /* InTagName */;
      t._index--; // Consume the token again
    }
  };
}

var stateBeforeCdata1 = ifElseState("C", 24 /* BeforeCdata2 */, 16 /* InDeclaration */);
var stateBeforeCdata2 = ifElseState("D", 25 /* BeforeCdata3 */, 16 /* InDeclaration */);
var stateBeforeCdata3 = ifElseState("A", 26 /* BeforeCdata4 */, 16 /* InDeclaration */);
var stateBeforeCdata4 = ifElseState("T", 27 /* BeforeCdata5 */, 16 /* InDeclaration */);
var stateBeforeCdata5 = ifElseState("A", 28 /* BeforeCdata6 */, 16 /* InDeclaration */);
var stateBeforeScript1 = consumeSpecialNameChar("R", 35 /* BeforeScript2 */);
var stateBeforeScript2 = consumeSpecialNameChar("I", 36 /* BeforeScript3 */);
var stateBeforeScript3 = consumeSpecialNameChar("P", 37 /* BeforeScript4 */);
var stateBeforeScript4 = consumeSpecialNameChar("T", 38 /* BeforeScript5 */);
var stateAfterScript1 = ifElseState("R", 40 /* AfterScript2 */, 1 /* Text */);
var stateAfterScript2 = ifElseState("I", 41 /* AfterScript3 */, 1 /* Text */);
var stateAfterScript3 = ifElseState("P", 42 /* AfterScript4 */, 1 /* Text */);
var stateAfterScript4 = ifElseState("T", 43 /* AfterScript5 */, 1 /* Text */);
var stateBeforeStyle1 = consumeSpecialNameChar("Y", 45 /* BeforeStyle2 */);
var stateBeforeStyle2 = consumeSpecialNameChar("L", 46 /* BeforeStyle3 */);
var stateBeforeStyle3 = consumeSpecialNameChar("E", 47 /* BeforeStyle4 */);
var stateAfterStyle1 = ifElseState("Y", 49 /* AfterStyle2 */, 1 /* Text */);
var stateAfterStyle2 = ifElseState("L", 50 /* AfterStyle3 */, 1 /* Text */);
var stateAfterStyle3 = ifElseState("E", 51 /* AfterStyle4 */, 1 /* Text */);
var stateBeforeSpecialT = consumeSpecialNameChar("I", 54 /* BeforeTitle1 */);
var stateBeforeTitle1 = consumeSpecialNameChar("T", 55 /* BeforeTitle2 */);
var stateBeforeTitle2 = consumeSpecialNameChar("L", 56 /* BeforeTitle3 */);
var stateBeforeTitle3 = consumeSpecialNameChar("E", 57 /* BeforeTitle4 */);
var stateAfterSpecialTEnd = ifElseState("I", 58 /* AfterTitle1 */, 1 /* Text */);
var stateAfterTitle1 = ifElseState("T", 59 /* AfterTitle2 */, 1 /* Text */);
var stateAfterTitle2 = ifElseState("L", 60 /* AfterTitle3 */, 1 /* Text */);
var stateAfterTitle3 = ifElseState("E", 61 /* AfterTitle4 */, 1 /* Text */);
var stateBeforeEntity = ifElseState("#", 63 /* BeforeNumericEntity */, 64 /* InNamedEntity */);
var stateBeforeNumericEntity = ifElseState("X", 66 /* InHexEntity */, 65 /* InNumericEntity */);
var Tokenizer = /** @class */function () {
  function Tokenizer(options, cbs) {
    var _a;
    /** The current state the tokenizer is in. */
    this._state = 1 /* Text */;
    /** The read buffer. */
    this.buffer = "";
    /** The beginning of the section that is currently being read. */
    this.sectionStart = 0;
    /** The index within the buffer that we are currently looking at. */
    this._index = 0;
    /**
     * Data that has already been processed will be removed from the buffer occasionally.
     * `_bufferOffset` keeps track of how many characters have been removed, to make sure position information is accurate.
     */
    this.bufferOffset = 0;
    /** Some behavior, eg. when decoding entities, is done while we are in another state. This keeps track of the other state type. */
    this.baseState = 1 /* Text */;
    /** For special parsing behavior inside of script and style tags. */
    this.special = 1 /* None */;
    /** Indicates whether the tokenizer has been paused. */
    this.running = true;
    /** Indicates whether the tokenizer has finished running / `.end` has been called. */
    this.ended = false;
    this.cbs = cbs;
    this.xmlMode = !!(options === null || options === void 0 ? void 0 : options.xmlMode);
    this.decodeEntities = (_a = options === null || options === void 0 ? void 0 : options.decodeEntities) !== null && _a !== void 0 ? _a : true;
  }
  Tokenizer.prototype.reset = function () {
    this._state = 1 /* Text */;
    this.buffer = "";
    this.sectionStart = 0;
    this._index = 0;
    this.bufferOffset = 0;
    this.baseState = 1 /* Text */;
    this.special = 1 /* None */;
    this.running = true;
    this.ended = false;
  };
  Tokenizer.prototype.write = function (chunk) {
    if (this.ended) this.cbs.onerror(Error(".write() after done!"));
    this.buffer += chunk;
    this.parse();
  };
  Tokenizer.prototype.end = function (chunk) {
    if (this.ended) this.cbs.onerror(Error(".end() after done!"));
    if (chunk) this.write(chunk);
    this.ended = true;
    if (this.running) this.finish();
  };
  Tokenizer.prototype.pause = function () {
    this.running = false;
  };
  Tokenizer.prototype.resume = function () {
    this.running = true;
    if (this._index < this.buffer.length) {
      this.parse();
    }
    if (this.ended) {
      this.finish();
    }
  };
  /**
   * The current index within all of the written data.
   */
  Tokenizer.prototype.getAbsoluteIndex = function () {
    return this.bufferOffset + this._index;
  };
  Tokenizer.prototype.stateText = function (c) {
    if (c === "<") {
      if (this._index > this.sectionStart) {
        this.cbs.ontext(this.getSection());
      }
      this._state = 2 /* BeforeTagName */;
      this.sectionStart = this._index;
    } else if (this.decodeEntities && c === "&" && (this.special === 1 /* None */ || this.special === 4 /* Title */)) {
      if (this._index > this.sectionStart) {
        this.cbs.ontext(this.getSection());
      }
      this.baseState = 1 /* Text */;
      this._state = 62 /* BeforeEntity */;
      this.sectionStart = this._index;
    }
  };
  /**
   * HTML only allows ASCII alpha characters (a-z and A-Z) at the beginning of a tag name.
   *
   * XML allows a lot more characters here (@see https://www.w3.org/TR/REC-xml/#NT-NameStartChar).
   * We allow anything that wouldn't end the tag.
   */
  Tokenizer.prototype.isTagStartChar = function (c) {
    return isASCIIAlpha(c) || this.xmlMode && !whitespace(c) && c !== "/" && c !== ">";
  };
  Tokenizer.prototype.stateBeforeTagName = function (c) {
    if (c === "/") {
      this._state = 5 /* BeforeClosingTagName */;
    } else if (c === "<") {
      this.cbs.ontext(this.getSection());
      this.sectionStart = this._index;
    } else if (c === ">" || this.special !== 1 /* None */ || whitespace(c)) {
      this._state = 1 /* Text */;
    } else if (c === "!") {
      this._state = 15 /* BeforeDeclaration */;
      this.sectionStart = this._index + 1;
    } else if (c === "?") {
      this._state = 17 /* InProcessingInstruction */;
      this.sectionStart = this._index + 1;
    } else if (!this.isTagStartChar(c)) {
      this._state = 1 /* Text */;
    } else {
      this._state = !this.xmlMode && (c === "s" || c === "S") ? 32 /* BeforeSpecialS */ : !this.xmlMode && (c === "t" || c === "T") ? 52 /* BeforeSpecialT */ : 3 /* InTagName */;
      this.sectionStart = this._index;
    }
  };
  Tokenizer.prototype.stateInTagName = function (c) {
    if (c === "/" || c === ">" || whitespace(c)) {
      this.emitToken("onopentagname");
      this._state = 8 /* BeforeAttributeName */;
      this._index--;
    }
  };
  Tokenizer.prototype.stateBeforeClosingTagName = function (c) {
    if (whitespace(c)) {
      // Ignore
    } else if (c === ">") {
      this._state = 1 /* Text */;
    } else if (this.special !== 1 /* None */) {
      if (this.special !== 4 /* Title */ && (c === "s" || c === "S")) {
        this._state = 33 /* BeforeSpecialSEnd */;
      } else if (this.special === 4 /* Title */ && (c === "t" || c === "T")) {
        this._state = 53 /* BeforeSpecialTEnd */;
      } else {
        this._state = 1 /* Text */;
        this._index--;
      }
    } else if (!this.isTagStartChar(c)) {
      this._state = 20 /* InSpecialComment */;
      this.sectionStart = this._index;
    } else {
      this._state = 6 /* InClosingTagName */;
      this.sectionStart = this._index;
    }
  };
  Tokenizer.prototype.stateInClosingTagName = function (c) {
    if (c === ">" || whitespace(c)) {
      this.emitToken("onclosetag");
      this._state = 7 /* AfterClosingTagName */;
      this._index--;
    }
  };
  Tokenizer.prototype.stateAfterClosingTagName = function (c) {
    // Skip everything until ">"
    if (c === ">") {
      this._state = 1 /* Text */;
      this.sectionStart = this._index + 1;
    }
  };
  Tokenizer.prototype.stateBeforeAttributeName = function (c) {
    if (c === ">") {
      this.cbs.onopentagend();
      this._state = 1 /* Text */;
      this.sectionStart = this._index + 1;
    } else if (c === "/") {
      this._state = 4 /* InSelfClosingTag */;
    } else if (!whitespace(c)) {
      this._state = 9 /* InAttributeName */;
      this.sectionStart = this._index;
    }
  };
  Tokenizer.prototype.stateInSelfClosingTag = function (c) {
    if (c === ">") {
      this.cbs.onselfclosingtag();
      this._state = 1 /* Text */;
      this.sectionStart = this._index + 1;
      this.special = 1 /* None */; // Reset special state, in case of self-closing special tags
    } else if (!whitespace(c)) {
      this._state = 8 /* BeforeAttributeName */;
      this._index--;
    }
  };
  Tokenizer.prototype.stateInAttributeName = function (c) {
    if (c === "=" || c === "/" || c === ">" || whitespace(c)) {
      this.cbs.onattribname(this.getSection());
      this.sectionStart = -1;
      this._state = 10 /* AfterAttributeName */;
      this._index--;
    }
  };
  Tokenizer.prototype.stateAfterAttributeName = function (c) {
    if (c === "=") {
      this._state = 11 /* BeforeAttributeValue */;
    } else if (c === "/" || c === ">") {
      this.cbs.onattribend(undefined);
      this._state = 8 /* BeforeAttributeName */;
      this._index--;
    } else if (!whitespace(c)) {
      this.cbs.onattribend(undefined);
      this._state = 9 /* InAttributeName */;
      this.sectionStart = this._index;
    }
  };
  Tokenizer.prototype.stateBeforeAttributeValue = function (c) {
    if (c === '"') {
      this._state = 12 /* InAttributeValueDq */;
      this.sectionStart = this._index + 1;
    } else if (c === "'") {
      this._state = 13 /* InAttributeValueSq */;
      this.sectionStart = this._index + 1;
    } else if (!whitespace(c)) {
      this._state = 14 /* InAttributeValueNq */;
      this.sectionStart = this._index;
      this._index--; // Reconsume token
    }
  };

  Tokenizer.prototype.handleInAttributeValue = function (c, quote) {
    if (c === quote) {
      this.emitToken("onattribdata");
      this.cbs.onattribend(quote);
      this._state = 8 /* BeforeAttributeName */;
    } else if (this.decodeEntities && c === "&") {
      this.emitToken("onattribdata");
      this.baseState = this._state;
      this._state = 62 /* BeforeEntity */;
      this.sectionStart = this._index;
    }
  };
  Tokenizer.prototype.stateInAttributeValueDoubleQuotes = function (c) {
    this.handleInAttributeValue(c, '"');
  };
  Tokenizer.prototype.stateInAttributeValueSingleQuotes = function (c) {
    this.handleInAttributeValue(c, "'");
  };
  Tokenizer.prototype.stateInAttributeValueNoQuotes = function (c) {
    if (whitespace(c) || c === ">") {
      this.emitToken("onattribdata");
      this.cbs.onattribend(null);
      this._state = 8 /* BeforeAttributeName */;
      this._index--;
    } else if (this.decodeEntities && c === "&") {
      this.emitToken("onattribdata");
      this.baseState = this._state;
      this._state = 62 /* BeforeEntity */;
      this.sectionStart = this._index;
    }
  };
  Tokenizer.prototype.stateBeforeDeclaration = function (c) {
    this._state = c === "[" ? 23 /* BeforeCdata1 */ : c === "-" ? 18 /* BeforeComment */ : 16 /* InDeclaration */;
  };

  Tokenizer.prototype.stateInDeclaration = function (c) {
    if (c === ">") {
      this.cbs.ondeclaration(this.getSection());
      this._state = 1 /* Text */;
      this.sectionStart = this._index + 1;
    }
  };
  Tokenizer.prototype.stateInProcessingInstruction = function (c) {
    if (c === ">") {
      this.cbs.onprocessinginstruction(this.getSection());
      this._state = 1 /* Text */;
      this.sectionStart = this._index + 1;
    }
  };
  Tokenizer.prototype.stateBeforeComment = function (c) {
    if (c === "-") {
      this._state = 19 /* InComment */;
      this.sectionStart = this._index + 1;
    } else {
      this._state = 16 /* InDeclaration */;
    }
  };

  Tokenizer.prototype.stateInComment = function (c) {
    if (c === "-") this._state = 21 /* AfterComment1 */;
  };

  Tokenizer.prototype.stateInSpecialComment = function (c) {
    if (c === ">") {
      this.cbs.oncomment(this.buffer.substring(this.sectionStart, this._index));
      this._state = 1 /* Text */;
      this.sectionStart = this._index + 1;
    }
  };
  Tokenizer.prototype.stateAfterComment1 = function (c) {
    if (c === "-") {
      this._state = 22 /* AfterComment2 */;
    } else {
      this._state = 19 /* InComment */;
    }
  };

  Tokenizer.prototype.stateAfterComment2 = function (c) {
    if (c === ">") {
      // Remove 2 trailing chars
      this.cbs.oncomment(this.buffer.substring(this.sectionStart, this._index - 2));
      this._state = 1 /* Text */;
      this.sectionStart = this._index + 1;
    } else if (c !== "-") {
      this._state = 19 /* InComment */;
    }
    // Else: stay in AFTER_COMMENT_2 (`--->`)
  };

  Tokenizer.prototype.stateBeforeCdata6 = function (c) {
    if (c === "[") {
      this._state = 29 /* InCdata */;
      this.sectionStart = this._index + 1;
    } else {
      this._state = 16 /* InDeclaration */;
      this._index--;
    }
  };
  Tokenizer.prototype.stateInCdata = function (c) {
    if (c === "]") this._state = 30 /* AfterCdata1 */;
  };

  Tokenizer.prototype.stateAfterCdata1 = function (c) {
    if (c === "]") this._state = 31 /* AfterCdata2 */;else this._state = 29 /* InCdata */;
  };

  Tokenizer.prototype.stateAfterCdata2 = function (c) {
    if (c === ">") {
      // Remove 2 trailing chars
      this.cbs.oncdata(this.buffer.substring(this.sectionStart, this._index - 2));
      this._state = 1 /* Text */;
      this.sectionStart = this._index + 1;
    } else if (c !== "]") {
      this._state = 29 /* InCdata */;
    }
    // Else: stay in AFTER_CDATA_2 (`]]]>`)
  };

  Tokenizer.prototype.stateBeforeSpecialS = function (c) {
    if (c === "c" || c === "C") {
      this._state = 34 /* BeforeScript1 */;
    } else if (c === "t" || c === "T") {
      this._state = 44 /* BeforeStyle1 */;
    } else {
      this._state = 3 /* InTagName */;
      this._index--; // Consume the token again
    }
  };

  Tokenizer.prototype.stateBeforeSpecialSEnd = function (c) {
    if (this.special === 2 /* Script */ && (c === "c" || c === "C")) {
      this._state = 39 /* AfterScript1 */;
    } else if (this.special === 3 /* Style */ && (c === "t" || c === "T")) {
      this._state = 48 /* AfterStyle1 */;
    } else this._state = 1 /* Text */;
  };

  Tokenizer.prototype.stateBeforeSpecialLast = function (c, special) {
    if (c === "/" || c === ">" || whitespace(c)) {
      this.special = special;
    }
    this._state = 3 /* InTagName */;
    this._index--; // Consume the token again
  };

  Tokenizer.prototype.stateAfterSpecialLast = function (c, sectionStartOffset) {
    if (c === ">" || whitespace(c)) {
      this.special = 1 /* None */;
      this._state = 6 /* InClosingTagName */;
      this.sectionStart = this._index - sectionStartOffset;
      this._index--; // Reconsume the token
    } else this._state = 1 /* Text */;
  };
  // For entities terminated with a semicolon
  Tokenizer.prototype.parseFixedEntity = function (map) {
    if (map === void 0) {
      map = this.xmlMode ? xml_json_1["default"] : entities_json_1["default"];
    }
    // Offset = 1
    if (this.sectionStart + 1 < this._index) {
      var entity = this.buffer.substring(this.sectionStart + 1, this._index);
      if (Object.prototype.hasOwnProperty.call(map, entity)) {
        this.emitPartial(map[entity]);
        this.sectionStart = this._index + 1;
      }
    }
  };
  // Parses legacy entities (without trailing semicolon)
  Tokenizer.prototype.parseLegacyEntity = function () {
    var start = this.sectionStart + 1;
    // The max length of legacy entities is 6
    var limit = Math.min(this._index - start, 6);
    while (limit >= 2) {
      // The min length of legacy entities is 2
      var entity = this.buffer.substr(start, limit);
      if (Object.prototype.hasOwnProperty.call(legacy_json_1["default"], entity)) {
        this.emitPartial(legacy_json_1["default"][entity]);
        this.sectionStart += limit + 1;
        return;
      }
      limit--;
    }
  };
  Tokenizer.prototype.stateInNamedEntity = function (c) {
    if (c === ";") {
      this.parseFixedEntity();
      // Retry as legacy entity if entity wasn't parsed
      if (this.baseState === 1 /* Text */ && this.sectionStart + 1 < this._index && !this.xmlMode) {
        this.parseLegacyEntity();
      }
      this._state = this.baseState;
    } else if ((c < "0" || c > "9") && !isASCIIAlpha(c)) {
      if (this.xmlMode || this.sectionStart + 1 === this._index) {
        // Ignore
      } else if (this.baseState !== 1 /* Text */) {
        if (c !== "=") {
          // Parse as legacy entity, without allowing additional characters.
          this.parseFixedEntity(legacy_json_1["default"]);
        }
      } else {
        this.parseLegacyEntity();
      }
      this._state = this.baseState;
      this._index--;
    }
  };
  Tokenizer.prototype.decodeNumericEntity = function (offset, base, strict) {
    var sectionStart = this.sectionStart + offset;
    if (sectionStart !== this._index) {
      // Parse entity
      var entity = this.buffer.substring(sectionStart, this._index);
      var parsed = parseInt(entity, base);
      this.emitPartial(decode_codepoint_1["default"](parsed));
      this.sectionStart = strict ? this._index + 1 : this._index;
    }
    this._state = this.baseState;
  };
  Tokenizer.prototype.stateInNumericEntity = function (c) {
    if (c === ";") {
      this.decodeNumericEntity(2, 10, true);
    } else if (c < "0" || c > "9") {
      if (!this.xmlMode) {
        this.decodeNumericEntity(2, 10, false);
      } else {
        this._state = this.baseState;
      }
      this._index--;
    }
  };
  Tokenizer.prototype.stateInHexEntity = function (c) {
    if (c === ";") {
      this.decodeNumericEntity(3, 16, true);
    } else if ((c < "a" || c > "f") && (c < "A" || c > "F") && (c < "0" || c > "9")) {
      if (!this.xmlMode) {
        this.decodeNumericEntity(3, 16, false);
      } else {
        this._state = this.baseState;
      }
      this._index--;
    }
  };
  Tokenizer.prototype.cleanup = function () {
    if (this.sectionStart < 0) {
      this.buffer = "";
      this.bufferOffset += this._index;
      this._index = 0;
    } else if (this.running) {
      if (this._state === 1 /* Text */) {
        if (this.sectionStart !== this._index) {
          this.cbs.ontext(this.buffer.substr(this.sectionStart));
        }
        this.buffer = "";
        this.bufferOffset += this._index;
        this._index = 0;
      } else if (this.sectionStart === this._index) {
        // The section just started
        this.buffer = "";
        this.bufferOffset += this._index;
        this._index = 0;
      } else {
        // Remove everything unnecessary
        this.buffer = this.buffer.substr(this.sectionStart);
        this._index -= this.sectionStart;
        this.bufferOffset += this.sectionStart;
      }
      this.sectionStart = 0;
    }
  };
  /**
   * Iterates through the buffer, calling the function corresponding to the current state.
   *
   * States that are more likely to be hit are higher up, as a performance improvement.
   */
  Tokenizer.prototype.parse = function () {
    while (this._index < this.buffer.length && this.running) {
      var c = this.buffer.charAt(this._index);
      if (this._state === 1 /* Text */) {
        this.stateText(c);
      } else if (this._state === 12 /* InAttributeValueDq */) {
        this.stateInAttributeValueDoubleQuotes(c);
      } else if (this._state === 9 /* InAttributeName */) {
        this.stateInAttributeName(c);
      } else if (this._state === 19 /* InComment */) {
        this.stateInComment(c);
      } else if (this._state === 20 /* InSpecialComment */) {
        this.stateInSpecialComment(c);
      } else if (this._state === 8 /* BeforeAttributeName */) {
        this.stateBeforeAttributeName(c);
      } else if (this._state === 3 /* InTagName */) {
        this.stateInTagName(c);
      } else if (this._state === 6 /* InClosingTagName */) {
        this.stateInClosingTagName(c);
      } else if (this._state === 2 /* BeforeTagName */) {
        this.stateBeforeTagName(c);
      } else if (this._state === 10 /* AfterAttributeName */) {
        this.stateAfterAttributeName(c);
      } else if (this._state === 13 /* InAttributeValueSq */) {
        this.stateInAttributeValueSingleQuotes(c);
      } else if (this._state === 11 /* BeforeAttributeValue */) {
        this.stateBeforeAttributeValue(c);
      } else if (this._state === 5 /* BeforeClosingTagName */) {
        this.stateBeforeClosingTagName(c);
      } else if (this._state === 7 /* AfterClosingTagName */) {
        this.stateAfterClosingTagName(c);
      } else if (this._state === 32 /* BeforeSpecialS */) {
        this.stateBeforeSpecialS(c);
      } else if (this._state === 21 /* AfterComment1 */) {
        this.stateAfterComment1(c);
      } else if (this._state === 14 /* InAttributeValueNq */) {
        this.stateInAttributeValueNoQuotes(c);
      } else if (this._state === 4 /* InSelfClosingTag */) {
        this.stateInSelfClosingTag(c);
      } else if (this._state === 16 /* InDeclaration */) {
        this.stateInDeclaration(c);
      } else if (this._state === 15 /* BeforeDeclaration */) {
        this.stateBeforeDeclaration(c);
      } else if (this._state === 22 /* AfterComment2 */) {
        this.stateAfterComment2(c);
      } else if (this._state === 18 /* BeforeComment */) {
        this.stateBeforeComment(c);
      } else if (this._state === 33 /* BeforeSpecialSEnd */) {
        this.stateBeforeSpecialSEnd(c);
      } else if (this._state === 53 /* BeforeSpecialTEnd */) {
        stateAfterSpecialTEnd(this, c);
      } else if (this._state === 39 /* AfterScript1 */) {
        stateAfterScript1(this, c);
      } else if (this._state === 40 /* AfterScript2 */) {
        stateAfterScript2(this, c);
      } else if (this._state === 41 /* AfterScript3 */) {
        stateAfterScript3(this, c);
      } else if (this._state === 34 /* BeforeScript1 */) {
        stateBeforeScript1(this, c);
      } else if (this._state === 35 /* BeforeScript2 */) {
        stateBeforeScript2(this, c);
      } else if (this._state === 36 /* BeforeScript3 */) {
        stateBeforeScript3(this, c);
      } else if (this._state === 37 /* BeforeScript4 */) {
        stateBeforeScript4(this, c);
      } else if (this._state === 38 /* BeforeScript5 */) {
        this.stateBeforeSpecialLast(c, 2 /* Script */);
      } else if (this._state === 42 /* AfterScript4 */) {
        stateAfterScript4(this, c);
      } else if (this._state === 43 /* AfterScript5 */) {
        this.stateAfterSpecialLast(c, 6);
      } else if (this._state === 44 /* BeforeStyle1 */) {
        stateBeforeStyle1(this, c);
      } else if (this._state === 29 /* InCdata */) {
        this.stateInCdata(c);
      } else if (this._state === 45 /* BeforeStyle2 */) {
        stateBeforeStyle2(this, c);
      } else if (this._state === 46 /* BeforeStyle3 */) {
        stateBeforeStyle3(this, c);
      } else if (this._state === 47 /* BeforeStyle4 */) {
        this.stateBeforeSpecialLast(c, 3 /* Style */);
      } else if (this._state === 48 /* AfterStyle1 */) {
        stateAfterStyle1(this, c);
      } else if (this._state === 49 /* AfterStyle2 */) {
        stateAfterStyle2(this, c);
      } else if (this._state === 50 /* AfterStyle3 */) {
        stateAfterStyle3(this, c);
      } else if (this._state === 51 /* AfterStyle4 */) {
        this.stateAfterSpecialLast(c, 5);
      } else if (this._state === 52 /* BeforeSpecialT */) {
        stateBeforeSpecialT(this, c);
      } else if (this._state === 54 /* BeforeTitle1 */) {
        stateBeforeTitle1(this, c);
      } else if (this._state === 55 /* BeforeTitle2 */) {
        stateBeforeTitle2(this, c);
      } else if (this._state === 56 /* BeforeTitle3 */) {
        stateBeforeTitle3(this, c);
      } else if (this._state === 57 /* BeforeTitle4 */) {
        this.stateBeforeSpecialLast(c, 4 /* Title */);
      } else if (this._state === 58 /* AfterTitle1 */) {
        stateAfterTitle1(this, c);
      } else if (this._state === 59 /* AfterTitle2 */) {
        stateAfterTitle2(this, c);
      } else if (this._state === 60 /* AfterTitle3 */) {
        stateAfterTitle3(this, c);
      } else if (this._state === 61 /* AfterTitle4 */) {
        this.stateAfterSpecialLast(c, 5);
      } else if (this._state === 17 /* InProcessingInstruction */) {
        this.stateInProcessingInstruction(c);
      } else if (this._state === 64 /* InNamedEntity */) {
        this.stateInNamedEntity(c);
      } else if (this._state === 23 /* BeforeCdata1 */) {
        stateBeforeCdata1(this, c);
      } else if (this._state === 62 /* BeforeEntity */) {
        stateBeforeEntity(this, c);
      } else if (this._state === 24 /* BeforeCdata2 */) {
        stateBeforeCdata2(this, c);
      } else if (this._state === 25 /* BeforeCdata3 */) {
        stateBeforeCdata3(this, c);
      } else if (this._state === 30 /* AfterCdata1 */) {
        this.stateAfterCdata1(c);
      } else if (this._state === 31 /* AfterCdata2 */) {
        this.stateAfterCdata2(c);
      } else if (this._state === 26 /* BeforeCdata4 */) {
        stateBeforeCdata4(this, c);
      } else if (this._state === 27 /* BeforeCdata5 */) {
        stateBeforeCdata5(this, c);
      } else if (this._state === 28 /* BeforeCdata6 */) {
        this.stateBeforeCdata6(c);
      } else if (this._state === 66 /* InHexEntity */) {
        this.stateInHexEntity(c);
      } else if (this._state === 65 /* InNumericEntity */) {
        this.stateInNumericEntity(c);
        // eslint-disable-next-line @typescript-eslint/no-unnecessary-condition
      } else if (this._state === 63 /* BeforeNumericEntity */) {
        stateBeforeNumericEntity(this, c);
      } else {
        this.cbs.onerror(Error("unknown _state"), this._state);
      }
      this._index++;
    }
    this.cleanup();
  };
  Tokenizer.prototype.finish = function () {
    // If there is remaining data, emit it in a reasonable way
    if (this.sectionStart < this._index) {
      this.handleTrailingData();
    }
    this.cbs.onend();
  };
  Tokenizer.prototype.handleTrailingData = function () {
    var data = this.buffer.substr(this.sectionStart);
    if (this._state === 29 /* InCdata */ || this._state === 30 /* AfterCdata1 */ || this._state === 31 /* AfterCdata2 */) {
      this.cbs.oncdata(data);
    } else if (this._state === 19 /* InComment */ || this._state === 21 /* AfterComment1 */ || this._state === 22 /* AfterComment2 */) {
      this.cbs.oncomment(data);
    } else if (this._state === 64 /* InNamedEntity */ && !this.xmlMode) {
      this.parseLegacyEntity();
      if (this.sectionStart < this._index) {
        this._state = this.baseState;
        this.handleTrailingData();
      }
    } else if (this._state === 65 /* InNumericEntity */ && !this.xmlMode) {
      this.decodeNumericEntity(2, 10, false);
      if (this.sectionStart < this._index) {
        this._state = this.baseState;
        this.handleTrailingData();
      }
    } else if (this._state === 66 /* InHexEntity */ && !this.xmlMode) {
      this.decodeNumericEntity(3, 16, false);
      if (this.sectionStart < this._index) {
        this._state = this.baseState;
        this.handleTrailingData();
      }
    } else if (this._state !== 3 /* InTagName */ && this._state !== 8 /* BeforeAttributeName */ && this._state !== 11 /* BeforeAttributeValue */ && this._state !== 10 /* AfterAttributeName */ && this._state !== 9 /* InAttributeName */ && this._state !== 13 /* InAttributeValueSq */ && this._state !== 12 /* InAttributeValueDq */ && this._state !== 14 /* InAttributeValueNq */ && this._state !== 6 /* InClosingTagName */) {
      this.cbs.ontext(data);
    }
    /*
     * Else, ignore remaining data
     * TODO add a way to remove current tag
     */
  };

  Tokenizer.prototype.getSection = function () {
    return this.buffer.substring(this.sectionStart, this._index);
  };
  Tokenizer.prototype.emitToken = function (name) {
    this.cbs[name](this.getSection());
    this.sectionStart = -1;
  };
  Tokenizer.prototype.emitPartial = function (value) {
    if (this.baseState !== 1 /* Text */) {
      this.cbs.onattribdata(value); // TODO implement the new event
    } else {
      this.cbs.ontext(value);
    }
  };
  return Tokenizer;
}();
exports["default"] = Tokenizer;

/***/ }),

/***/ 6124:
/***/ (function(__unused_webpack_module, exports, __webpack_require__) {

"use strict";


var __createBinding = this && this.__createBinding || (Object.create ? function (o, m, k, k2) {
  if (k2 === undefined) k2 = k;
  Object.defineProperty(o, k2, {
    enumerable: true,
    get: function get() {
      return m[k];
    }
  });
} : function (o, m, k, k2) {
  if (k2 === undefined) k2 = k;
  o[k2] = m[k];
});
var __setModuleDefault = this && this.__setModuleDefault || (Object.create ? function (o, v) {
  Object.defineProperty(o, "default", {
    enumerable: true,
    value: v
  });
} : function (o, v) {
  o["default"] = v;
});
var __importStar = this && this.__importStar || function (mod) {
  if (mod && mod.__esModule) return mod;
  var result = {};
  if (mod != null) for (var k in mod) {
    if (k !== "default" && Object.prototype.hasOwnProperty.call(mod, k)) __createBinding(result, mod, k);
  }
  __setModuleDefault(result, mod);
  return result;
};
var __exportStar = this && this.__exportStar || function (m, exports) {
  for (var p in m) {
    if (p !== "default" && !Object.prototype.hasOwnProperty.call(exports, p)) __createBinding(exports, m, p);
  }
};
var __importDefault = this && this.__importDefault || function (mod) {
  return mod && mod.__esModule ? mod : {
    "default": mod
  };
};
Object.defineProperty(exports, "__esModule", ({
  value: true
}));
exports.RssHandler = exports.DefaultHandler = exports.DomUtils = exports.ElementType = exports.Tokenizer = exports.createDomStream = exports.parseDOM = exports.parseDocument = exports.DomHandler = exports.Parser = void 0;
var Parser_1 = __webpack_require__(8168);
Object.defineProperty(exports, "Parser", ({
  enumerable: true,
  get: function get() {
    return Parser_1.Parser;
  }
}));
var domhandler_1 = __webpack_require__(1363);
Object.defineProperty(exports, "DomHandler", ({
  enumerable: true,
  get: function get() {
    return domhandler_1.DomHandler;
  }
}));
Object.defineProperty(exports, "DefaultHandler", ({
  enumerable: true,
  get: function get() {
    return domhandler_1.DomHandler;
  }
}));
// Helper methods
/**
 * Parses the data, returns the resulting document.
 *
 * @param data The data that should be parsed.
 * @param options Optional options for the parser and DOM builder.
 */
function parseDocument(data, options) {
  var handler = new domhandler_1.DomHandler(undefined, options);
  new Parser_1.Parser(handler, options).end(data);
  return handler.root;
}
exports.parseDocument = parseDocument;
/**
 * Parses data, returns an array of the root nodes.
 *
 * Note that the root nodes still have a `Document` node as their parent.
 * Use `parseDocument` to get the `Document` node instead.
 *
 * @param data The data that should be parsed.
 * @param options Optional options for the parser and DOM builder.
 * @deprecated Use `parseDocument` instead.
 */
function parseDOM(data, options) {
  return parseDocument(data, options).children;
}
exports.parseDOM = parseDOM;
/**
 * Creates a parser instance, with an attached DOM handler.
 *
 * @param cb A callback that will be called once parsing has been completed.
 * @param options Optional options for the parser and DOM builder.
 * @param elementCb An optional callback that will be called every time a tag has been completed inside of the DOM.
 */
function createDomStream(cb, options, elementCb) {
  var handler = new domhandler_1.DomHandler(cb, options, elementCb);
  return new Parser_1.Parser(handler, options);
}
exports.createDomStream = createDomStream;
var Tokenizer_1 = __webpack_require__(6506);
Object.defineProperty(exports, "Tokenizer", ({
  enumerable: true,
  get: function get() {
    return __importDefault(Tokenizer_1)["default"];
  }
}));
var ElementType = __importStar(__webpack_require__(7304));
exports.ElementType = ElementType;
/*
 * All of the following exports exist for backwards-compatibility.
 * They should probably be removed eventually.
 */
__exportStar(__webpack_require__(2369), exports);
exports.DomUtils = __importStar(__webpack_require__(5511));
var FeedHandler_1 = __webpack_require__(2369);
Object.defineProperty(exports, "RssHandler", ({
  enumerable: true,
  get: function get() {
    return FeedHandler_1.FeedHandler;
  }
}));

/***/ }),

/***/ 4281:
/***/ ((__unused_webpack_module, exports) => {

"use strict";


Object.defineProperty(exports, "__esModule", ({
  value: true
}));

/*!
 * is-plain-object <https://github.com/jonschlinkert/is-plain-object>
 *
 * Copyright (c) 2014-2017, Jon Schlinkert.
 * Released under the MIT License.
 */

function isObject(o) {
  return Object.prototype.toString.call(o) === '[object Object]';
}
function isPlainObject(o) {
  var ctor, prot;
  if (isObject(o) === false) return false;

  // If has modified constructor
  ctor = o.constructor;
  if (ctor === undefined) return true;

  // If has modified prototype
  prot = ctor.prototype;
  if (isObject(prot) === false) return false;

  // If constructor does not have an Object-specific method
  if (prot.hasOwnProperty('isPrototypeOf') === false) {
    return false;
  }

  // Most likely a plain Object
  return true;
}
exports.isPlainObject = isPlainObject;

/***/ }),

/***/ 2134:
/***/ (function(module, exports) {

var __WEBPACK_AMD_DEFINE_FACTORY__, __WEBPACK_AMD_DEFINE_ARRAY__, __WEBPACK_AMD_DEFINE_RESULT__;function _typeof(obj) { "@babel/helpers - typeof"; return _typeof = "function" == typeof Symbol && "symbol" == typeof Symbol.iterator ? function (obj) { return typeof obj; } : function (obj) { return obj && "function" == typeof Symbol && obj.constructor === Symbol && obj !== Symbol.prototype ? "symbol" : typeof obj; }, _typeof(obj); }
/**
 * Srcset Parser
 *
 * By Alex Bell |  MIT License
 *
 * JS Parser for the string value that appears in markup <img srcset="here">
 *
 * @returns Array [{url: _, d: _, w: _, h:_}, ...]
 *
 * Based super duper closely on the reference algorithm at:
 * https://html.spec.whatwg.org/multipage/embedded-content.html#parse-a-srcset-attribute
 *
 * Most comments are copied in directly from the spec
 * (except for comments in parens).
 */

(function (root, factory) {
  if (true) {
    // AMD. Register as an anonymous module.
    !(__WEBPACK_AMD_DEFINE_ARRAY__ = [], __WEBPACK_AMD_DEFINE_FACTORY__ = (factory),
		__WEBPACK_AMD_DEFINE_RESULT__ = (typeof __WEBPACK_AMD_DEFINE_FACTORY__ === 'function' ?
		(__WEBPACK_AMD_DEFINE_FACTORY__.apply(exports, __WEBPACK_AMD_DEFINE_ARRAY__)) : __WEBPACK_AMD_DEFINE_FACTORY__),
		__WEBPACK_AMD_DEFINE_RESULT__ !== undefined && (module.exports = __WEBPACK_AMD_DEFINE_RESULT__));
  } else {}
})(this, function () {
  // 1. Let input be the value passed to this algorithm.
  return function (input) {
    // UTILITY FUNCTIONS

    // Manual is faster than RegEx
    // http://bjorn.tipling.com/state-and-regular-expressions-in-javascript
    // http://jsperf.com/whitespace-character/5
    function isSpace(c) {
      return c === " " ||
      // space
      c === "\t" ||
      // horizontal tab
      c === "\n" ||
      // new line
      c === "\f" ||
      // form feed
      c === "\r"; // carriage return
    }

    function collectCharacters(regEx) {
      var chars,
        match = regEx.exec(input.substring(pos));
      if (match) {
        chars = match[0];
        pos += chars.length;
        return chars;
      }
    }
    var inputLength = input.length,
      // (Don't use \s, to avoid matching non-breaking space)
      regexLeadingSpaces = /^[ \t\n\r\u000c]+/,
      regexLeadingCommasOrSpaces = /^[, \t\n\r\u000c]+/,
      regexLeadingNotSpaces = /^[^ \t\n\r\u000c]+/,
      regexTrailingCommas = /[,]+$/,
      regexNonNegativeInteger = /^\d+$/,
      // ( Positive or negative or unsigned integers or decimals, without or without exponents.
      // Must include at least one digit.
      // According to spec tests any decimal point must be followed by a digit.
      // No leading plus sign is allowed.)
      // https://html.spec.whatwg.org/multipage/infrastructure.html#valid-floating-point-number
      regexFloatingPoint = /^-?(?:[0-9]+|[0-9]*\.[0-9]+)(?:[eE][+-]?[0-9]+)?$/,
      url,
      descriptors,
      currentDescriptor,
      state,
      c,
      // 2. Let position be a pointer into input, initially pointing at the start
      //    of the string.
      pos = 0,
      // 3. Let candidates be an initially empty source set.
      candidates = [];

    // 4. Splitting loop: Collect a sequence of characters that are space
    //    characters or U+002C COMMA characters. If any U+002C COMMA characters
    //    were collected, that is a parse error.
    while (true) {
      collectCharacters(regexLeadingCommasOrSpaces);

      // 5. If position is past the end of input, return candidates and abort these steps.
      if (pos >= inputLength) {
        return candidates; // (we're done, this is the sole return path)
      }

      // 6. Collect a sequence of characters that are not space characters,
      //    and let that be url.
      url = collectCharacters(regexLeadingNotSpaces);

      // 7. Let descriptors be a new empty list.
      descriptors = [];

      // 8. If url ends with a U+002C COMMA character (,), follow these substeps:
      //		(1). Remove all trailing U+002C COMMA characters from url. If this removed
      //         more than one character, that is a parse error.
      if (url.slice(-1) === ",") {
        url = url.replace(regexTrailingCommas, "");
        // (Jump ahead to step 9 to skip tokenization and just push the candidate).
        parseDescriptors();

        //	Otherwise, follow these substeps:
      } else {
        tokenize();
      } // (close else of step 8)

      // 16. Return to the step labeled splitting loop.
    } // (Close of big while loop.)

    /**
     * Tokenizes descriptor properties prior to parsing
     * Returns undefined.
     */
    function tokenize() {
      // 8.1. Descriptor tokeniser: Skip whitespace
      collectCharacters(regexLeadingSpaces);

      // 8.2. Let current descriptor be the empty string.
      currentDescriptor = "";

      // 8.3. Let state be in descriptor.
      state = "in descriptor";
      while (true) {
        // 8.4. Let c be the character at position.
        c = input.charAt(pos);

        //  Do the following depending on the value of state.
        //  For the purpose of this step, "EOF" is a special character representing
        //  that position is past the end of input.

        // In descriptor
        if (state === "in descriptor") {
          // Do the following, depending on the value of c:

          // Space character
          // If current descriptor is not empty, append current descriptor to
          // descriptors and let current descriptor be the empty string.
          // Set state to after descriptor.
          if (isSpace(c)) {
            if (currentDescriptor) {
              descriptors.push(currentDescriptor);
              currentDescriptor = "";
              state = "after descriptor";
            }

            // U+002C COMMA (,)
            // Advance position to the next character in input. If current descriptor
            // is not empty, append current descriptor to descriptors. Jump to the step
            // labeled descriptor parser.
          } else if (c === ",") {
            pos += 1;
            if (currentDescriptor) {
              descriptors.push(currentDescriptor);
            }
            parseDescriptors();
            return;

            // U+0028 LEFT PARENTHESIS (()
            // Append c to current descriptor. Set state to in parens.
          } else if (c === "(") {
            currentDescriptor = currentDescriptor + c;
            state = "in parens";

            // EOF
            // If current descriptor is not empty, append current descriptor to
            // descriptors. Jump to the step labeled descriptor parser.
          } else if (c === "") {
            if (currentDescriptor) {
              descriptors.push(currentDescriptor);
            }
            parseDescriptors();
            return;

            // Anything else
            // Append c to current descriptor.
          } else {
            currentDescriptor = currentDescriptor + c;
          }
          // (end "in descriptor"

          // In parens
        } else if (state === "in parens") {
          // U+0029 RIGHT PARENTHESIS ())
          // Append c to current descriptor. Set state to in descriptor.
          if (c === ")") {
            currentDescriptor = currentDescriptor + c;
            state = "in descriptor";

            // EOF
            // Append current descriptor to descriptors. Jump to the step labeled
            // descriptor parser.
          } else if (c === "") {
            descriptors.push(currentDescriptor);
            parseDescriptors();
            return;

            // Anything else
            // Append c to current descriptor.
          } else {
            currentDescriptor = currentDescriptor + c;
          }

          // After descriptor
        } else if (state === "after descriptor") {
          // Do the following, depending on the value of c:
          // Space character: Stay in this state.
          if (isSpace(c)) {

            // EOF: Jump to the step labeled descriptor parser.
          } else if (c === "") {
            parseDescriptors();
            return;

            // Anything else
            // Set state to in descriptor. Set position to the previous character in input.
          } else {
            state = "in descriptor";
            pos -= 1;
          }
        }

        // Advance position to the next character in input.
        pos += 1;

        // Repeat this step.
      } // (close while true loop)
    }

    /**
     * Adds descriptor properties to a candidate, pushes to the candidates array
     * @return undefined
     */
    // Declared outside of the while loop so that it's only created once.
    function parseDescriptors() {
      // 9. Descriptor parser: Let error be no.
      var pError = false,
        // 10. Let width be absent.
        // 11. Let density be absent.
        // 12. Let future-compat-h be absent. (We're implementing it now as h)
        w,
        d,
        h,
        i,
        candidate = {},
        desc,
        lastChar,
        value,
        intVal,
        floatVal;

      // 13. For each descriptor in descriptors, run the appropriate set of steps
      // from the following list:
      for (i = 0; i < descriptors.length; i++) {
        desc = descriptors[i];
        lastChar = desc[desc.length - 1];
        value = desc.substring(0, desc.length - 1);
        intVal = parseInt(value, 10);
        floatVal = parseFloat(value);

        // If the descriptor consists of a valid non-negative integer followed by
        // a U+0077 LATIN SMALL LETTER W character
        if (regexNonNegativeInteger.test(value) && lastChar === "w") {
          // If width and density are not both absent, then let error be yes.
          if (w || d) {
            pError = true;
          }

          // Apply the rules for parsing non-negative integers to the descriptor.
          // If the result is zero, let error be yes.
          // Otherwise, let width be the result.
          if (intVal === 0) {
            pError = true;
          } else {
            w = intVal;
          }

          // If the descriptor consists of a valid floating-point number followed by
          // a U+0078 LATIN SMALL LETTER X character
        } else if (regexFloatingPoint.test(value) && lastChar === "x") {
          // If width, density and future-compat-h are not all absent, then let error
          // be yes.
          if (w || d || h) {
            pError = true;
          }

          // Apply the rules for parsing floating-point number values to the descriptor.
          // If the result is less than zero, let error be yes. Otherwise, let density
          // be the result.
          if (floatVal < 0) {
            pError = true;
          } else {
            d = floatVal;
          }

          // If the descriptor consists of a valid non-negative integer followed by
          // a U+0068 LATIN SMALL LETTER H character
        } else if (regexNonNegativeInteger.test(value) && lastChar === "h") {
          // If height and density are not both absent, then let error be yes.
          if (h || d) {
            pError = true;
          }

          // Apply the rules for parsing non-negative integers to the descriptor.
          // If the result is zero, let error be yes. Otherwise, let future-compat-h
          // be the result.
          if (intVal === 0) {
            pError = true;
          } else {
            h = intVal;
          }

          // Anything else, Let error be yes.
        } else {
          pError = true;
        }
      } // (close step 13 for loop)

      // 15. If error is still no, then append a new image source to candidates whose
      // URL is url, associated with a width width if not absent and a pixel
      // density density if not absent. Otherwise, there is a parse error.
      if (!pError) {
        candidate.url = url;
        if (w) {
          candidate.w = w;
        }
        if (d) {
          candidate.d = d;
        }
        if (h) {
          candidate.h = h;
        }
        candidates.push(candidate);
      } else if (console && console.log) {
        console.log("Invalid srcset descriptor found in '" + input + "' at '" + desc + "'.");
      }
    } // (close parseDescriptors fn)
  };
});

/***/ }),

/***/ 8799:
/***/ ((module) => {

var x = String;
var create = function create() {
  return {
    isColorSupported: false,
    reset: x,
    bold: x,
    dim: x,
    italic: x,
    underline: x,
    inverse: x,
    hidden: x,
    strikethrough: x,
    black: x,
    red: x,
    green: x,
    yellow: x,
    blue: x,
    magenta: x,
    cyan: x,
    white: x,
    gray: x,
    bgBlack: x,
    bgRed: x,
    bgGreen: x,
    bgYellow: x,
    bgBlue: x,
    bgMagenta: x,
    bgCyan: x,
    bgWhite: x
  };
};
module.exports = create();
module.exports.createColors = create;

/***/ }),

/***/ 8940:
/***/ ((module, __unused_webpack_exports, __webpack_require__) => {

"use strict";


function _typeof(obj) { "@babel/helpers - typeof"; return _typeof = "function" == typeof Symbol && "symbol" == typeof Symbol.iterator ? function (obj) { return typeof obj; } : function (obj) { return obj && "function" == typeof Symbol && obj.constructor === Symbol && obj !== Symbol.prototype ? "symbol" : typeof obj; }, _typeof(obj); }
function _classCallCheck(instance, Constructor) { if (!(instance instanceof Constructor)) { throw new TypeError("Cannot call a class as a function"); } }
function _defineProperties(target, props) { for (var i = 0; i < props.length; i++) { var descriptor = props[i]; descriptor.enumerable = descriptor.enumerable || false; descriptor.configurable = true; if ("value" in descriptor) descriptor.writable = true; Object.defineProperty(target, descriptor.key, descriptor); } }
function _createClass(Constructor, protoProps, staticProps) { if (protoProps) _defineProperties(Constructor.prototype, protoProps); if (staticProps) _defineProperties(Constructor, staticProps); Object.defineProperty(Constructor, "prototype", { writable: false }); return Constructor; }
function _get() { if (typeof Reflect !== "undefined" && Reflect.get) { _get = Reflect.get.bind(); } else { _get = function _get(target, property, receiver) { var base = _superPropBase(target, property); if (!base) return; var desc = Object.getOwnPropertyDescriptor(base, property); if (desc.get) { return desc.get.call(arguments.length < 3 ? target : receiver); } return desc.value; }; } return _get.apply(this, arguments); }
function _superPropBase(object, property) { while (!Object.prototype.hasOwnProperty.call(object, property)) { object = _getPrototypeOf(object); if (object === null) break; } return object; }
function _inherits(subClass, superClass) { if (typeof superClass !== "function" && superClass !== null) { throw new TypeError("Super expression must either be null or a function"); } subClass.prototype = Object.create(superClass && superClass.prototype, { constructor: { value: subClass, writable: true, configurable: true } }); Object.defineProperty(subClass, "prototype", { writable: false }); if (superClass) _setPrototypeOf(subClass, superClass); }
function _setPrototypeOf(o, p) { _setPrototypeOf = Object.setPrototypeOf ? Object.setPrototypeOf.bind() : function _setPrototypeOf(o, p) { o.__proto__ = p; return o; }; return _setPrototypeOf(o, p); }
function _createSuper(Derived) { var hasNativeReflectConstruct = _isNativeReflectConstruct(); return function _createSuperInternal() { var Super = _getPrototypeOf(Derived), result; if (hasNativeReflectConstruct) { var NewTarget = _getPrototypeOf(this).constructor; result = Reflect.construct(Super, arguments, NewTarget); } else { result = Super.apply(this, arguments); } return _possibleConstructorReturn(this, result); }; }
function _possibleConstructorReturn(self, call) { if (call && (_typeof(call) === "object" || typeof call === "function")) { return call; } else if (call !== void 0) { throw new TypeError("Derived constructors may only return object or undefined"); } return _assertThisInitialized(self); }
function _assertThisInitialized(self) { if (self === void 0) { throw new ReferenceError("this hasn't been initialised - super() hasn't been called"); } return self; }
function _isNativeReflectConstruct() { if (typeof Reflect === "undefined" || !Reflect.construct) return false; if (Reflect.construct.sham) return false; if (typeof Proxy === "function") return true; try { Boolean.prototype.valueOf.call(Reflect.construct(Boolean, [], function () {})); return true; } catch (e) { return false; } }
function _getPrototypeOf(o) { _getPrototypeOf = Object.setPrototypeOf ? Object.getPrototypeOf.bind() : function _getPrototypeOf(o) { return o.__proto__ || Object.getPrototypeOf(o); }; return _getPrototypeOf(o); }
var Container = __webpack_require__(1204);
var AtRule = /*#__PURE__*/function (_Container) {
  _inherits(AtRule, _Container);
  var _super = _createSuper(AtRule);
  function AtRule(defaults) {
    var _this;
    _classCallCheck(this, AtRule);
    _this = _super.call(this, defaults);
    _this.type = 'atrule';
    return _this;
  }
  _createClass(AtRule, [{
    key: "append",
    value: function append() {
      var _get2;
      if (!this.proxyOf.nodes) this.nodes = [];
      for (var _len = arguments.length, children = new Array(_len), _key = 0; _key < _len; _key++) {
        children[_key] = arguments[_key];
      }
      return (_get2 = _get(_getPrototypeOf(AtRule.prototype), "append", this)).call.apply(_get2, [this].concat(children));
    }
  }, {
    key: "prepend",
    value: function prepend() {
      var _get3;
      if (!this.proxyOf.nodes) this.nodes = [];
      for (var _len2 = arguments.length, children = new Array(_len2), _key2 = 0; _key2 < _len2; _key2++) {
        children[_key2] = arguments[_key2];
      }
      return (_get3 = _get(_getPrototypeOf(AtRule.prototype), "prepend", this)).call.apply(_get3, [this].concat(children));
    }
  }]);
  return AtRule;
}(Container);
module.exports = AtRule;
AtRule["default"] = AtRule;
Container.registerAtRule(AtRule);

/***/ }),

/***/ 3102:
/***/ ((module, __unused_webpack_exports, __webpack_require__) => {

"use strict";


function _typeof(obj) { "@babel/helpers - typeof"; return _typeof = "function" == typeof Symbol && "symbol" == typeof Symbol.iterator ? function (obj) { return typeof obj; } : function (obj) { return obj && "function" == typeof Symbol && obj.constructor === Symbol && obj !== Symbol.prototype ? "symbol" : typeof obj; }, _typeof(obj); }
function _defineProperties(target, props) { for (var i = 0; i < props.length; i++) { var descriptor = props[i]; descriptor.enumerable = descriptor.enumerable || false; descriptor.configurable = true; if ("value" in descriptor) descriptor.writable = true; Object.defineProperty(target, descriptor.key, descriptor); } }
function _createClass(Constructor, protoProps, staticProps) { if (protoProps) _defineProperties(Constructor.prototype, protoProps); if (staticProps) _defineProperties(Constructor, staticProps); Object.defineProperty(Constructor, "prototype", { writable: false }); return Constructor; }
function _classCallCheck(instance, Constructor) { if (!(instance instanceof Constructor)) { throw new TypeError("Cannot call a class as a function"); } }
function _inherits(subClass, superClass) { if (typeof superClass !== "function" && superClass !== null) { throw new TypeError("Super expression must either be null or a function"); } subClass.prototype = Object.create(superClass && superClass.prototype, { constructor: { value: subClass, writable: true, configurable: true } }); Object.defineProperty(subClass, "prototype", { writable: false }); if (superClass) _setPrototypeOf(subClass, superClass); }
function _setPrototypeOf(o, p) { _setPrototypeOf = Object.setPrototypeOf ? Object.setPrototypeOf.bind() : function _setPrototypeOf(o, p) { o.__proto__ = p; return o; }; return _setPrototypeOf(o, p); }
function _createSuper(Derived) { var hasNativeReflectConstruct = _isNativeReflectConstruct(); return function _createSuperInternal() { var Super = _getPrototypeOf(Derived), result; if (hasNativeReflectConstruct) { var NewTarget = _getPrototypeOf(this).constructor; result = Reflect.construct(Super, arguments, NewTarget); } else { result = Super.apply(this, arguments); } return _possibleConstructorReturn(this, result); }; }
function _possibleConstructorReturn(self, call) { if (call && (_typeof(call) === "object" || typeof call === "function")) { return call; } else if (call !== void 0) { throw new TypeError("Derived constructors may only return object or undefined"); } return _assertThisInitialized(self); }
function _assertThisInitialized(self) { if (self === void 0) { throw new ReferenceError("this hasn't been initialised - super() hasn't been called"); } return self; }
function _isNativeReflectConstruct() { if (typeof Reflect === "undefined" || !Reflect.construct) return false; if (Reflect.construct.sham) return false; if (typeof Proxy === "function") return true; try { Boolean.prototype.valueOf.call(Reflect.construct(Boolean, [], function () {})); return true; } catch (e) { return false; } }
function _getPrototypeOf(o) { _getPrototypeOf = Object.setPrototypeOf ? Object.getPrototypeOf.bind() : function _getPrototypeOf(o) { return o.__proto__ || Object.getPrototypeOf(o); }; return _getPrototypeOf(o); }
var Node = __webpack_require__(4343);
var Comment = /*#__PURE__*/function (_Node) {
  _inherits(Comment, _Node);
  var _super = _createSuper(Comment);
  function Comment(defaults) {
    var _this;
    _classCallCheck(this, Comment);
    _this = _super.call(this, defaults);
    _this.type = 'comment';
    return _this;
  }
  return _createClass(Comment);
}(Node);
module.exports = Comment;
Comment["default"] = Comment;

/***/ }),

/***/ 1204:
/***/ ((module, __unused_webpack_exports, __webpack_require__) => {

"use strict";


function _typeof(obj) { "@babel/helpers - typeof"; return _typeof = "function" == typeof Symbol && "symbol" == typeof Symbol.iterator ? function (obj) { return typeof obj; } : function (obj) { return obj && "function" == typeof Symbol && obj.constructor === Symbol && obj !== Symbol.prototype ? "symbol" : typeof obj; }, _typeof(obj); }
function _toConsumableArray(arr) { return _arrayWithoutHoles(arr) || _iterableToArray(arr) || _unsupportedIterableToArray(arr) || _nonIterableSpread(); }
function _nonIterableSpread() { throw new TypeError("Invalid attempt to spread non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method."); }
function _iterableToArray(iter) { if (typeof Symbol !== "undefined" && iter[Symbol.iterator] != null || iter["@@iterator"] != null) return Array.from(iter); }
function _arrayWithoutHoles(arr) { if (Array.isArray(arr)) return _arrayLikeToArray(arr); }
function _classCallCheck(instance, Constructor) { if (!(instance instanceof Constructor)) { throw new TypeError("Cannot call a class as a function"); } }
function _defineProperties(target, props) { for (var i = 0; i < props.length; i++) { var descriptor = props[i]; descriptor.enumerable = descriptor.enumerable || false; descriptor.configurable = true; if ("value" in descriptor) descriptor.writable = true; Object.defineProperty(target, descriptor.key, descriptor); } }
function _createClass(Constructor, protoProps, staticProps) { if (protoProps) _defineProperties(Constructor.prototype, protoProps); if (staticProps) _defineProperties(Constructor, staticProps); Object.defineProperty(Constructor, "prototype", { writable: false }); return Constructor; }
function _get() { if (typeof Reflect !== "undefined" && Reflect.get) { _get = Reflect.get.bind(); } else { _get = function _get(target, property, receiver) { var base = _superPropBase(target, property); if (!base) return; var desc = Object.getOwnPropertyDescriptor(base, property); if (desc.get) { return desc.get.call(arguments.length < 3 ? target : receiver); } return desc.value; }; } return _get.apply(this, arguments); }
function _superPropBase(object, property) { while (!Object.prototype.hasOwnProperty.call(object, property)) { object = _getPrototypeOf(object); if (object === null) break; } return object; }
function _inherits(subClass, superClass) { if (typeof superClass !== "function" && superClass !== null) { throw new TypeError("Super expression must either be null or a function"); } subClass.prototype = Object.create(superClass && superClass.prototype, { constructor: { value: subClass, writable: true, configurable: true } }); Object.defineProperty(subClass, "prototype", { writable: false }); if (superClass) _setPrototypeOf(subClass, superClass); }
function _setPrototypeOf(o, p) { _setPrototypeOf = Object.setPrototypeOf ? Object.setPrototypeOf.bind() : function _setPrototypeOf(o, p) { o.__proto__ = p; return o; }; return _setPrototypeOf(o, p); }
function _createSuper(Derived) { var hasNativeReflectConstruct = _isNativeReflectConstruct(); return function _createSuperInternal() { var Super = _getPrototypeOf(Derived), result; if (hasNativeReflectConstruct) { var NewTarget = _getPrototypeOf(this).constructor; result = Reflect.construct(Super, arguments, NewTarget); } else { result = Super.apply(this, arguments); } return _possibleConstructorReturn(this, result); }; }
function _possibleConstructorReturn(self, call) { if (call && (_typeof(call) === "object" || typeof call === "function")) { return call; } else if (call !== void 0) { throw new TypeError("Derived constructors may only return object or undefined"); } return _assertThisInitialized(self); }
function _assertThisInitialized(self) { if (self === void 0) { throw new ReferenceError("this hasn't been initialised - super() hasn't been called"); } return self; }
function _isNativeReflectConstruct() { if (typeof Reflect === "undefined" || !Reflect.construct) return false; if (Reflect.construct.sham) return false; if (typeof Proxy === "function") return true; try { Boolean.prototype.valueOf.call(Reflect.construct(Boolean, [], function () {})); return true; } catch (e) { return false; } }
function _getPrototypeOf(o) { _getPrototypeOf = Object.setPrototypeOf ? Object.getPrototypeOf.bind() : function _getPrototypeOf(o) { return o.__proto__ || Object.getPrototypeOf(o); }; return _getPrototypeOf(o); }
function _createForOfIteratorHelper(o, allowArrayLike) { var it = typeof Symbol !== "undefined" && o[Symbol.iterator] || o["@@iterator"]; if (!it) { if (Array.isArray(o) || (it = _unsupportedIterableToArray(o)) || allowArrayLike && o && typeof o.length === "number") { if (it) o = it; var i = 0; var F = function F() {}; return { s: F, n: function n() { if (i >= o.length) return { done: true }; return { done: false, value: o[i++] }; }, e: function e(_e) { throw _e; }, f: F }; } throw new TypeError("Invalid attempt to iterate non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method."); } var normalCompletion = true, didErr = false, err; return { s: function s() { it = it.call(o); }, n: function n() { var step = it.next(); normalCompletion = step.done; return step; }, e: function e(_e2) { didErr = true; err = _e2; }, f: function f() { try { if (!normalCompletion && it["return"] != null) it["return"](); } finally { if (didErr) throw err; } } }; }
function _unsupportedIterableToArray(o, minLen) { if (!o) return; if (typeof o === "string") return _arrayLikeToArray(o, minLen); var n = Object.prototype.toString.call(o).slice(8, -1); if (n === "Object" && o.constructor) n = o.constructor.name; if (n === "Map" || n === "Set") return Array.from(o); if (n === "Arguments" || /^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(n)) return _arrayLikeToArray(o, minLen); }
function _arrayLikeToArray(arr, len) { if (len == null || len > arr.length) len = arr.length; for (var i = 0, arr2 = new Array(len); i < len; i++) { arr2[i] = arr[i]; } return arr2; }
var _require = __webpack_require__(5506),
  isClean = _require.isClean,
  my = _require.my;
var Declaration = __webpack_require__(6417);
var Comment = __webpack_require__(3102);
var Node = __webpack_require__(4343);
var parse, Rule, AtRule, Root;
function cleanSource(nodes) {
  return nodes.map(function (i) {
    if (i.nodes) i.nodes = cleanSource(i.nodes);
    delete i.source;
    return i;
  });
}
function markDirtyUp(node) {
  node[isClean] = false;
  if (node.proxyOf.nodes) {
    var _iterator = _createForOfIteratorHelper(node.proxyOf.nodes),
      _step;
    try {
      for (_iterator.s(); !(_step = _iterator.n()).done;) {
        var i = _step.value;
        markDirtyUp(i);
      }
    } catch (err) {
      _iterator.e(err);
    } finally {
      _iterator.f();
    }
  }
}
var Container = /*#__PURE__*/function (_Node) {
  _inherits(Container, _Node);
  var _super = _createSuper(Container);
  function Container() {
    _classCallCheck(this, Container);
    return _super.apply(this, arguments);
  }
  _createClass(Container, [{
    key: "push",
    value: function push(child) {
      child.parent = this;
      this.proxyOf.nodes.push(child);
      return this;
    }
  }, {
    key: "each",
    value: function each(callback) {
      if (!this.proxyOf.nodes) return undefined;
      var iterator = this.getIterator();
      var index, result;
      while (this.indexes[iterator] < this.proxyOf.nodes.length) {
        index = this.indexes[iterator];
        result = callback(this.proxyOf.nodes[index], index);
        if (result === false) break;
        this.indexes[iterator] += 1;
      }
      delete this.indexes[iterator];
      return result;
    }
  }, {
    key: "walk",
    value: function walk(callback) {
      return this.each(function (child, i) {
        var result;
        try {
          result = callback(child, i);
        } catch (e) {
          throw child.addToError(e);
        }
        if (result !== false && child.walk) {
          result = child.walk(callback);
        }
        return result;
      });
    }
  }, {
    key: "walkDecls",
    value: function walkDecls(prop, callback) {
      if (!callback) {
        callback = prop;
        return this.walk(function (child, i) {
          if (child.type === 'decl') {
            return callback(child, i);
          }
        });
      }
      if (prop instanceof RegExp) {
        return this.walk(function (child, i) {
          if (child.type === 'decl' && prop.test(child.prop)) {
            return callback(child, i);
          }
        });
      }
      return this.walk(function (child, i) {
        if (child.type === 'decl' && child.prop === prop) {
          return callback(child, i);
        }
      });
    }
  }, {
    key: "walkRules",
    value: function walkRules(selector, callback) {
      if (!callback) {
        callback = selector;
        return this.walk(function (child, i) {
          if (child.type === 'rule') {
            return callback(child, i);
          }
        });
      }
      if (selector instanceof RegExp) {
        return this.walk(function (child, i) {
          if (child.type === 'rule' && selector.test(child.selector)) {
            return callback(child, i);
          }
        });
      }
      return this.walk(function (child, i) {
        if (child.type === 'rule' && child.selector === selector) {
          return callback(child, i);
        }
      });
    }
  }, {
    key: "walkAtRules",
    value: function walkAtRules(name, callback) {
      if (!callback) {
        callback = name;
        return this.walk(function (child, i) {
          if (child.type === 'atrule') {
            return callback(child, i);
          }
        });
      }
      if (name instanceof RegExp) {
        return this.walk(function (child, i) {
          if (child.type === 'atrule' && name.test(child.name)) {
            return callback(child, i);
          }
        });
      }
      return this.walk(function (child, i) {
        if (child.type === 'atrule' && child.name === name) {
          return callback(child, i);
        }
      });
    }
  }, {
    key: "walkComments",
    value: function walkComments(callback) {
      return this.walk(function (child, i) {
        if (child.type === 'comment') {
          return callback(child, i);
        }
      });
    }
  }, {
    key: "append",
    value: function append() {
      for (var _len = arguments.length, children = new Array(_len), _key = 0; _key < _len; _key++) {
        children[_key] = arguments[_key];
      }
      for (var _i = 0, _children = children; _i < _children.length; _i++) {
        var child = _children[_i];
        var nodes = this.normalize(child, this.last);
        var _iterator2 = _createForOfIteratorHelper(nodes),
          _step2;
        try {
          for (_iterator2.s(); !(_step2 = _iterator2.n()).done;) {
            var node = _step2.value;
            this.proxyOf.nodes.push(node);
          }
        } catch (err) {
          _iterator2.e(err);
        } finally {
          _iterator2.f();
        }
      }
      this.markDirty();
      return this;
    }
  }, {
    key: "prepend",
    value: function prepend() {
      for (var _len2 = arguments.length, children = new Array(_len2), _key2 = 0; _key2 < _len2; _key2++) {
        children[_key2] = arguments[_key2];
      }
      children = children.reverse();
      var _iterator3 = _createForOfIteratorHelper(children),
        _step3;
      try {
        for (_iterator3.s(); !(_step3 = _iterator3.n()).done;) {
          var child = _step3.value;
          var nodes = this.normalize(child, this.first, 'prepend').reverse();
          var _iterator4 = _createForOfIteratorHelper(nodes),
            _step4;
          try {
            for (_iterator4.s(); !(_step4 = _iterator4.n()).done;) {
              var node = _step4.value;
              this.proxyOf.nodes.unshift(node);
            }
          } catch (err) {
            _iterator4.e(err);
          } finally {
            _iterator4.f();
          }
          for (var id in this.indexes) {
            this.indexes[id] = this.indexes[id] + nodes.length;
          }
        }
      } catch (err) {
        _iterator3.e(err);
      } finally {
        _iterator3.f();
      }
      this.markDirty();
      return this;
    }
  }, {
    key: "cleanRaws",
    value: function cleanRaws(keepBetween) {
      _get(_getPrototypeOf(Container.prototype), "cleanRaws", this).call(this, keepBetween);
      if (this.nodes) {
        var _iterator5 = _createForOfIteratorHelper(this.nodes),
          _step5;
        try {
          for (_iterator5.s(); !(_step5 = _iterator5.n()).done;) {
            var node = _step5.value;
            node.cleanRaws(keepBetween);
          }
        } catch (err) {
          _iterator5.e(err);
        } finally {
          _iterator5.f();
        }
      }
    }
  }, {
    key: "insertBefore",
    value: function insertBefore(exist, add) {
      var existIndex = this.index(exist);
      var type = exist === 0 ? 'prepend' : false;
      var nodes = this.normalize(add, this.proxyOf.nodes[existIndex], type).reverse();
      existIndex = this.index(exist);
      var _iterator6 = _createForOfIteratorHelper(nodes),
        _step6;
      try {
        for (_iterator6.s(); !(_step6 = _iterator6.n()).done;) {
          var node = _step6.value;
          this.proxyOf.nodes.splice(existIndex, 0, node);
        }
      } catch (err) {
        _iterator6.e(err);
      } finally {
        _iterator6.f();
      }
      var index;
      for (var id in this.indexes) {
        index = this.indexes[id];
        if (existIndex <= index) {
          this.indexes[id] = index + nodes.length;
        }
      }
      this.markDirty();
      return this;
    }
  }, {
    key: "insertAfter",
    value: function insertAfter(exist, add) {
      var existIndex = this.index(exist);
      var nodes = this.normalize(add, this.proxyOf.nodes[existIndex]).reverse();
      existIndex = this.index(exist);
      var _iterator7 = _createForOfIteratorHelper(nodes),
        _step7;
      try {
        for (_iterator7.s(); !(_step7 = _iterator7.n()).done;) {
          var node = _step7.value;
          this.proxyOf.nodes.splice(existIndex + 1, 0, node);
        }
      } catch (err) {
        _iterator7.e(err);
      } finally {
        _iterator7.f();
      }
      var index;
      for (var id in this.indexes) {
        index = this.indexes[id];
        if (existIndex < index) {
          this.indexes[id] = index + nodes.length;
        }
      }
      this.markDirty();
      return this;
    }
  }, {
    key: "removeChild",
    value: function removeChild(child) {
      child = this.index(child);
      this.proxyOf.nodes[child].parent = undefined;
      this.proxyOf.nodes.splice(child, 1);
      var index;
      for (var id in this.indexes) {
        index = this.indexes[id];
        if (index >= child) {
          this.indexes[id] = index - 1;
        }
      }
      this.markDirty();
      return this;
    }
  }, {
    key: "removeAll",
    value: function removeAll() {
      var _iterator8 = _createForOfIteratorHelper(this.proxyOf.nodes),
        _step8;
      try {
        for (_iterator8.s(); !(_step8 = _iterator8.n()).done;) {
          var node = _step8.value;
          node.parent = undefined;
        }
      } catch (err) {
        _iterator8.e(err);
      } finally {
        _iterator8.f();
      }
      this.proxyOf.nodes = [];
      this.markDirty();
      return this;
    }
  }, {
    key: "replaceValues",
    value: function replaceValues(pattern, opts, callback) {
      if (!callback) {
        callback = opts;
        opts = {};
      }
      this.walkDecls(function (decl) {
        if (opts.props && !opts.props.includes(decl.prop)) return;
        if (opts.fast && !decl.value.includes(opts.fast)) return;
        decl.value = decl.value.replace(pattern, callback);
      });
      this.markDirty();
      return this;
    }
  }, {
    key: "every",
    value: function every(condition) {
      return this.nodes.every(condition);
    }
  }, {
    key: "some",
    value: function some(condition) {
      return this.nodes.some(condition);
    }
  }, {
    key: "index",
    value: function index(child) {
      if (typeof child === 'number') return child;
      if (child.proxyOf) child = child.proxyOf;
      return this.proxyOf.nodes.indexOf(child);
    }
  }, {
    key: "first",
    get: function get() {
      if (!this.proxyOf.nodes) return undefined;
      return this.proxyOf.nodes[0];
    }
  }, {
    key: "last",
    get: function get() {
      if (!this.proxyOf.nodes) return undefined;
      return this.proxyOf.nodes[this.proxyOf.nodes.length - 1];
    }
  }, {
    key: "normalize",
    value: function normalize(nodes, sample) {
      var _this = this;
      if (typeof nodes === 'string') {
        nodes = cleanSource(parse(nodes).nodes);
      } else if (Array.isArray(nodes)) {
        nodes = nodes.slice(0);
        var _iterator9 = _createForOfIteratorHelper(nodes),
          _step9;
        try {
          for (_iterator9.s(); !(_step9 = _iterator9.n()).done;) {
            var i = _step9.value;
            if (i.parent) i.parent.removeChild(i, 'ignore');
          }
        } catch (err) {
          _iterator9.e(err);
        } finally {
          _iterator9.f();
        }
      } else if (nodes.type === 'root' && this.type !== 'document') {
        nodes = nodes.nodes.slice(0);
        var _iterator10 = _createForOfIteratorHelper(nodes),
          _step10;
        try {
          for (_iterator10.s(); !(_step10 = _iterator10.n()).done;) {
            var _i2 = _step10.value;
            if (_i2.parent) _i2.parent.removeChild(_i2, 'ignore');
          }
        } catch (err) {
          _iterator10.e(err);
        } finally {
          _iterator10.f();
        }
      } else if (nodes.type) {
        nodes = [nodes];
      } else if (nodes.prop) {
        if (typeof nodes.value === 'undefined') {
          throw new Error('Value field is missed in node creation');
        } else if (typeof nodes.value !== 'string') {
          nodes.value = String(nodes.value);
        }
        nodes = [new Declaration(nodes)];
      } else if (nodes.selector) {
        nodes = [new Rule(nodes)];
      } else if (nodes.name) {
        nodes = [new AtRule(nodes)];
      } else if (nodes.text) {
        nodes = [new Comment(nodes)];
      } else {
        throw new Error('Unknown node type in node creation');
      }
      var processed = nodes.map(function (i) {
        /* c8 ignore next */
        if (!i[my]) Container.rebuild(i);
        i = i.proxyOf;
        if (i.parent) i.parent.removeChild(i);
        if (i[isClean]) markDirtyUp(i);
        if (typeof i.raws.before === 'undefined') {
          if (sample && typeof sample.raws.before !== 'undefined') {
            i.raws.before = sample.raws.before.replace(/\S/g, '');
          }
        }
        i.parent = _this.proxyOf;
        return i;
      });
      return processed;
    }
  }, {
    key: "getProxyProcessor",
    value: function getProxyProcessor() {
      return {
        set: function set(node, prop, value) {
          if (node[prop] === value) return true;
          node[prop] = value;
          if (prop === 'name' || prop === 'params' || prop === 'selector') {
            node.markDirty();
          }
          return true;
        },
        get: function get(node, prop) {
          if (prop === 'proxyOf') {
            return node;
          } else if (!node[prop]) {
            return node[prop];
          } else if (prop === 'each' || typeof prop === 'string' && prop.startsWith('walk')) {
            return function () {
              for (var _len3 = arguments.length, args = new Array(_len3), _key3 = 0; _key3 < _len3; _key3++) {
                args[_key3] = arguments[_key3];
              }
              return node[prop].apply(node, _toConsumableArray(args.map(function (i) {
                if (typeof i === 'function') {
                  return function (child, index) {
                    return i(child.toProxy(), index);
                  };
                } else {
                  return i;
                }
              })));
            };
          } else if (prop === 'every' || prop === 'some') {
            return function (cb) {
              return node[prop](function (child) {
                for (var _len4 = arguments.length, other = new Array(_len4 > 1 ? _len4 - 1 : 0), _key4 = 1; _key4 < _len4; _key4++) {
                  other[_key4 - 1] = arguments[_key4];
                }
                return cb.apply(void 0, [child.toProxy()].concat(other));
              });
            };
          } else if (prop === 'root') {
            return function () {
              return node.root().toProxy();
            };
          } else if (prop === 'nodes') {
            return node.nodes.map(function (i) {
              return i.toProxy();
            });
          } else if (prop === 'first' || prop === 'last') {
            return node[prop].toProxy();
          } else {
            return node[prop];
          }
        }
      };
    }
  }, {
    key: "getIterator",
    value: function getIterator() {
      if (!this.lastEach) this.lastEach = 0;
      if (!this.indexes) this.indexes = {};
      this.lastEach += 1;
      var iterator = this.lastEach;
      this.indexes[iterator] = 0;
      return iterator;
    }
  }]);
  return Container;
}(Node);
Container.registerParse = function (dependant) {
  parse = dependant;
};
Container.registerRule = function (dependant) {
  Rule = dependant;
};
Container.registerAtRule = function (dependant) {
  AtRule = dependant;
};
Container.registerRoot = function (dependant) {
  Root = dependant;
};
module.exports = Container;
Container["default"] = Container;

/* c8 ignore start */
Container.rebuild = function (node) {
  if (node.type === 'atrule') {
    Object.setPrototypeOf(node, AtRule.prototype);
  } else if (node.type === 'rule') {
    Object.setPrototypeOf(node, Rule.prototype);
  } else if (node.type === 'decl') {
    Object.setPrototypeOf(node, Declaration.prototype);
  } else if (node.type === 'comment') {
    Object.setPrototypeOf(node, Comment.prototype);
  } else if (node.type === 'root') {
    Object.setPrototypeOf(node, Root.prototype);
  }
  node[my] = true;
  if (node.nodes) {
    node.nodes.forEach(function (child) {
      Container.rebuild(child);
    });
  }
};
/* c8 ignore stop */

/***/ }),

/***/ 1667:
/***/ ((module, __unused_webpack_exports, __webpack_require__) => {

"use strict";


function _typeof(obj) { "@babel/helpers - typeof"; return _typeof = "function" == typeof Symbol && "symbol" == typeof Symbol.iterator ? function (obj) { return typeof obj; } : function (obj) { return obj && "function" == typeof Symbol && obj.constructor === Symbol && obj !== Symbol.prototype ? "symbol" : typeof obj; }, _typeof(obj); }
function _classCallCheck(instance, Constructor) { if (!(instance instanceof Constructor)) { throw new TypeError("Cannot call a class as a function"); } }
function _defineProperties(target, props) { for (var i = 0; i < props.length; i++) { var descriptor = props[i]; descriptor.enumerable = descriptor.enumerable || false; descriptor.configurable = true; if ("value" in descriptor) descriptor.writable = true; Object.defineProperty(target, descriptor.key, descriptor); } }
function _createClass(Constructor, protoProps, staticProps) { if (protoProps) _defineProperties(Constructor.prototype, protoProps); if (staticProps) _defineProperties(Constructor, staticProps); Object.defineProperty(Constructor, "prototype", { writable: false }); return Constructor; }
function _inherits(subClass, superClass) { if (typeof superClass !== "function" && superClass !== null) { throw new TypeError("Super expression must either be null or a function"); } subClass.prototype = Object.create(superClass && superClass.prototype, { constructor: { value: subClass, writable: true, configurable: true } }); Object.defineProperty(subClass, "prototype", { writable: false }); if (superClass) _setPrototypeOf(subClass, superClass); }
function _createSuper(Derived) { var hasNativeReflectConstruct = _isNativeReflectConstruct(); return function _createSuperInternal() { var Super = _getPrototypeOf(Derived), result; if (hasNativeReflectConstruct) { var NewTarget = _getPrototypeOf(this).constructor; result = Reflect.construct(Super, arguments, NewTarget); } else { result = Super.apply(this, arguments); } return _possibleConstructorReturn(this, result); }; }
function _possibleConstructorReturn(self, call) { if (call && (_typeof(call) === "object" || typeof call === "function")) { return call; } else if (call !== void 0) { throw new TypeError("Derived constructors may only return object or undefined"); } return _assertThisInitialized(self); }
function _assertThisInitialized(self) { if (self === void 0) { throw new ReferenceError("this hasn't been initialised - super() hasn't been called"); } return self; }
function _wrapNativeSuper(Class) { var _cache = typeof Map === "function" ? new Map() : undefined; _wrapNativeSuper = function _wrapNativeSuper(Class) { if (Class === null || !_isNativeFunction(Class)) return Class; if (typeof Class !== "function") { throw new TypeError("Super expression must either be null or a function"); } if (typeof _cache !== "undefined") { if (_cache.has(Class)) return _cache.get(Class); _cache.set(Class, Wrapper); } function Wrapper() { return _construct(Class, arguments, _getPrototypeOf(this).constructor); } Wrapper.prototype = Object.create(Class.prototype, { constructor: { value: Wrapper, enumerable: false, writable: true, configurable: true } }); return _setPrototypeOf(Wrapper, Class); }; return _wrapNativeSuper(Class); }
function _construct(Parent, args, Class) { if (_isNativeReflectConstruct()) { _construct = Reflect.construct.bind(); } else { _construct = function _construct(Parent, args, Class) { var a = [null]; a.push.apply(a, args); var Constructor = Function.bind.apply(Parent, a); var instance = new Constructor(); if (Class) _setPrototypeOf(instance, Class.prototype); return instance; }; } return _construct.apply(null, arguments); }
function _isNativeReflectConstruct() { if (typeof Reflect === "undefined" || !Reflect.construct) return false; if (Reflect.construct.sham) return false; if (typeof Proxy === "function") return true; try { Boolean.prototype.valueOf.call(Reflect.construct(Boolean, [], function () {})); return true; } catch (e) { return false; } }
function _isNativeFunction(fn) { return Function.toString.call(fn).indexOf("[native code]") !== -1; }
function _setPrototypeOf(o, p) { _setPrototypeOf = Object.setPrototypeOf ? Object.setPrototypeOf.bind() : function _setPrototypeOf(o, p) { o.__proto__ = p; return o; }; return _setPrototypeOf(o, p); }
function _getPrototypeOf(o) { _getPrototypeOf = Object.setPrototypeOf ? Object.getPrototypeOf.bind() : function _getPrototypeOf(o) { return o.__proto__ || Object.getPrototypeOf(o); }; return _getPrototypeOf(o); }
var pico = __webpack_require__(8799);
var terminalHighlight = __webpack_require__(2868);
var CssSyntaxError = /*#__PURE__*/function (_Error) {
  _inherits(CssSyntaxError, _Error);
  var _super = _createSuper(CssSyntaxError);
  function CssSyntaxError(message, line, column, source, file, plugin) {
    var _this;
    _classCallCheck(this, CssSyntaxError);
    _this = _super.call(this, message);
    _this.name = 'CssSyntaxError';
    _this.reason = message;
    if (file) {
      _this.file = file;
    }
    if (source) {
      _this.source = source;
    }
    if (plugin) {
      _this.plugin = plugin;
    }
    if (typeof line !== 'undefined' && typeof column !== 'undefined') {
      if (typeof line === 'number') {
        _this.line = line;
        _this.column = column;
      } else {
        _this.line = line.line;
        _this.column = line.column;
        _this.endLine = column.line;
        _this.endColumn = column.column;
      }
    }
    _this.setMessage();
    if (Error.captureStackTrace) {
      Error.captureStackTrace(_assertThisInitialized(_this), CssSyntaxError);
    }
    return _this;
  }
  _createClass(CssSyntaxError, [{
    key: "setMessage",
    value: function setMessage() {
      this.message = this.plugin ? this.plugin + ': ' : '';
      this.message += this.file ? this.file : '<css input>';
      if (typeof this.line !== 'undefined') {
        this.message += ':' + this.line + ':' + this.column;
      }
      this.message += ': ' + this.reason;
    }
  }, {
    key: "showSourceCode",
    value: function showSourceCode(color) {
      var _this2 = this;
      if (!this.source) return '';
      var css = this.source;
      if (color == null) color = pico.isColorSupported;
      if (terminalHighlight) {
        if (color) css = terminalHighlight(css);
      }
      var lines = css.split(/\r?\n/);
      var start = Math.max(this.line - 3, 0);
      var end = Math.min(this.line + 2, lines.length);
      var maxWidth = String(end).length;
      var mark, aside;
      if (color) {
        var _pico$createColors = pico.createColors(true),
          bold = _pico$createColors.bold,
          red = _pico$createColors.red,
          gray = _pico$createColors.gray;
        mark = function mark(text) {
          return bold(red(text));
        };
        aside = function aside(text) {
          return gray(text);
        };
      } else {
        mark = aside = function aside(str) {
          return str;
        };
      }
      return lines.slice(start, end).map(function (line, index) {
        var number = start + 1 + index;
        var gutter = ' ' + (' ' + number).slice(-maxWidth) + ' | ';
        if (number === _this2.line) {
          var spacing = aside(gutter.replace(/\d/g, ' ')) + line.slice(0, _this2.column - 1).replace(/[^\t]/g, ' ');
          return mark('>') + aside(gutter) + line + '\n ' + spacing + mark('^');
        }
        return ' ' + aside(gutter) + line;
      }).join('\n');
    }
  }, {
    key: "toString",
    value: function toString() {
      var code = this.showSourceCode();
      if (code) {
        code = '\n\n' + code + '\n';
      }
      return this.name + ': ' + this.message + code;
    }
  }]);
  return CssSyntaxError;
}( /*#__PURE__*/_wrapNativeSuper(Error));
module.exports = CssSyntaxError;
CssSyntaxError["default"] = CssSyntaxError;

/***/ }),

/***/ 6417:
/***/ ((module, __unused_webpack_exports, __webpack_require__) => {

"use strict";


function _typeof(obj) { "@babel/helpers - typeof"; return _typeof = "function" == typeof Symbol && "symbol" == typeof Symbol.iterator ? function (obj) { return typeof obj; } : function (obj) { return obj && "function" == typeof Symbol && obj.constructor === Symbol && obj !== Symbol.prototype ? "symbol" : typeof obj; }, _typeof(obj); }
function ownKeys(object, enumerableOnly) { var keys = Object.keys(object); if (Object.getOwnPropertySymbols) { var symbols = Object.getOwnPropertySymbols(object); enumerableOnly && (symbols = symbols.filter(function (sym) { return Object.getOwnPropertyDescriptor(object, sym).enumerable; })), keys.push.apply(keys, symbols); } return keys; }
function _objectSpread(target) { for (var i = 1; i < arguments.length; i++) { var source = null != arguments[i] ? arguments[i] : {}; i % 2 ? ownKeys(Object(source), !0).forEach(function (key) { _defineProperty(target, key, source[key]); }) : Object.getOwnPropertyDescriptors ? Object.defineProperties(target, Object.getOwnPropertyDescriptors(source)) : ownKeys(Object(source)).forEach(function (key) { Object.defineProperty(target, key, Object.getOwnPropertyDescriptor(source, key)); }); } return target; }
function _defineProperty(obj, key, value) { if (key in obj) { Object.defineProperty(obj, key, { value: value, enumerable: true, configurable: true, writable: true }); } else { obj[key] = value; } return obj; }
function _classCallCheck(instance, Constructor) { if (!(instance instanceof Constructor)) { throw new TypeError("Cannot call a class as a function"); } }
function _defineProperties(target, props) { for (var i = 0; i < props.length; i++) { var descriptor = props[i]; descriptor.enumerable = descriptor.enumerable || false; descriptor.configurable = true; if ("value" in descriptor) descriptor.writable = true; Object.defineProperty(target, descriptor.key, descriptor); } }
function _createClass(Constructor, protoProps, staticProps) { if (protoProps) _defineProperties(Constructor.prototype, protoProps); if (staticProps) _defineProperties(Constructor, staticProps); Object.defineProperty(Constructor, "prototype", { writable: false }); return Constructor; }
function _inherits(subClass, superClass) { if (typeof superClass !== "function" && superClass !== null) { throw new TypeError("Super expression must either be null or a function"); } subClass.prototype = Object.create(superClass && superClass.prototype, { constructor: { value: subClass, writable: true, configurable: true } }); Object.defineProperty(subClass, "prototype", { writable: false }); if (superClass) _setPrototypeOf(subClass, superClass); }
function _setPrototypeOf(o, p) { _setPrototypeOf = Object.setPrototypeOf ? Object.setPrototypeOf.bind() : function _setPrototypeOf(o, p) { o.__proto__ = p; return o; }; return _setPrototypeOf(o, p); }
function _createSuper(Derived) { var hasNativeReflectConstruct = _isNativeReflectConstruct(); return function _createSuperInternal() { var Super = _getPrototypeOf(Derived), result; if (hasNativeReflectConstruct) { var NewTarget = _getPrototypeOf(this).constructor; result = Reflect.construct(Super, arguments, NewTarget); } else { result = Super.apply(this, arguments); } return _possibleConstructorReturn(this, result); }; }
function _possibleConstructorReturn(self, call) { if (call && (_typeof(call) === "object" || typeof call === "function")) { return call; } else if (call !== void 0) { throw new TypeError("Derived constructors may only return object or undefined"); } return _assertThisInitialized(self); }
function _assertThisInitialized(self) { if (self === void 0) { throw new ReferenceError("this hasn't been initialised - super() hasn't been called"); } return self; }
function _isNativeReflectConstruct() { if (typeof Reflect === "undefined" || !Reflect.construct) return false; if (Reflect.construct.sham) return false; if (typeof Proxy === "function") return true; try { Boolean.prototype.valueOf.call(Reflect.construct(Boolean, [], function () {})); return true; } catch (e) { return false; } }
function _getPrototypeOf(o) { _getPrototypeOf = Object.setPrototypeOf ? Object.getPrototypeOf.bind() : function _getPrototypeOf(o) { return o.__proto__ || Object.getPrototypeOf(o); }; return _getPrototypeOf(o); }
var Node = __webpack_require__(4343);
var Declaration = /*#__PURE__*/function (_Node) {
  _inherits(Declaration, _Node);
  var _super = _createSuper(Declaration);
  function Declaration(defaults) {
    var _this;
    _classCallCheck(this, Declaration);
    if (defaults && typeof defaults.value !== 'undefined' && typeof defaults.value !== 'string') {
      defaults = _objectSpread(_objectSpread({}, defaults), {}, {
        value: String(defaults.value)
      });
    }
    _this = _super.call(this, defaults);
    _this.type = 'decl';
    return _this;
  }
  _createClass(Declaration, [{
    key: "variable",
    get: function get() {
      return this.prop.startsWith('--') || this.prop[0] === '$';
    }
  }]);
  return Declaration;
}(Node);
module.exports = Declaration;
Declaration["default"] = Declaration;

/***/ }),

/***/ 7083:
/***/ ((module, __unused_webpack_exports, __webpack_require__) => {

"use strict";


function _typeof(obj) { "@babel/helpers - typeof"; return _typeof = "function" == typeof Symbol && "symbol" == typeof Symbol.iterator ? function (obj) { return typeof obj; } : function (obj) { return obj && "function" == typeof Symbol && obj.constructor === Symbol && obj !== Symbol.prototype ? "symbol" : typeof obj; }, _typeof(obj); }
function ownKeys(object, enumerableOnly) { var keys = Object.keys(object); if (Object.getOwnPropertySymbols) { var symbols = Object.getOwnPropertySymbols(object); enumerableOnly && (symbols = symbols.filter(function (sym) { return Object.getOwnPropertyDescriptor(object, sym).enumerable; })), keys.push.apply(keys, symbols); } return keys; }
function _objectSpread(target) { for (var i = 1; i < arguments.length; i++) { var source = null != arguments[i] ? arguments[i] : {}; i % 2 ? ownKeys(Object(source), !0).forEach(function (key) { _defineProperty(target, key, source[key]); }) : Object.getOwnPropertyDescriptors ? Object.defineProperties(target, Object.getOwnPropertyDescriptors(source)) : ownKeys(Object(source)).forEach(function (key) { Object.defineProperty(target, key, Object.getOwnPropertyDescriptor(source, key)); }); } return target; }
function _defineProperty(obj, key, value) { if (key in obj) { Object.defineProperty(obj, key, { value: value, enumerable: true, configurable: true, writable: true }); } else { obj[key] = value; } return obj; }
function _classCallCheck(instance, Constructor) { if (!(instance instanceof Constructor)) { throw new TypeError("Cannot call a class as a function"); } }
function _defineProperties(target, props) { for (var i = 0; i < props.length; i++) { var descriptor = props[i]; descriptor.enumerable = descriptor.enumerable || false; descriptor.configurable = true; if ("value" in descriptor) descriptor.writable = true; Object.defineProperty(target, descriptor.key, descriptor); } }
function _createClass(Constructor, protoProps, staticProps) { if (protoProps) _defineProperties(Constructor.prototype, protoProps); if (staticProps) _defineProperties(Constructor, staticProps); Object.defineProperty(Constructor, "prototype", { writable: false }); return Constructor; }
function _inherits(subClass, superClass) { if (typeof superClass !== "function" && superClass !== null) { throw new TypeError("Super expression must either be null or a function"); } subClass.prototype = Object.create(superClass && superClass.prototype, { constructor: { value: subClass, writable: true, configurable: true } }); Object.defineProperty(subClass, "prototype", { writable: false }); if (superClass) _setPrototypeOf(subClass, superClass); }
function _setPrototypeOf(o, p) { _setPrototypeOf = Object.setPrototypeOf ? Object.setPrototypeOf.bind() : function _setPrototypeOf(o, p) { o.__proto__ = p; return o; }; return _setPrototypeOf(o, p); }
function _createSuper(Derived) { var hasNativeReflectConstruct = _isNativeReflectConstruct(); return function _createSuperInternal() { var Super = _getPrototypeOf(Derived), result; if (hasNativeReflectConstruct) { var NewTarget = _getPrototypeOf(this).constructor; result = Reflect.construct(Super, arguments, NewTarget); } else { result = Super.apply(this, arguments); } return _possibleConstructorReturn(this, result); }; }
function _possibleConstructorReturn(self, call) { if (call && (_typeof(call) === "object" || typeof call === "function")) { return call; } else if (call !== void 0) { throw new TypeError("Derived constructors may only return object or undefined"); } return _assertThisInitialized(self); }
function _assertThisInitialized(self) { if (self === void 0) { throw new ReferenceError("this hasn't been initialised - super() hasn't been called"); } return self; }
function _isNativeReflectConstruct() { if (typeof Reflect === "undefined" || !Reflect.construct) return false; if (Reflect.construct.sham) return false; if (typeof Proxy === "function") return true; try { Boolean.prototype.valueOf.call(Reflect.construct(Boolean, [], function () {})); return true; } catch (e) { return false; } }
function _getPrototypeOf(o) { _getPrototypeOf = Object.setPrototypeOf ? Object.getPrototypeOf.bind() : function _getPrototypeOf(o) { return o.__proto__ || Object.getPrototypeOf(o); }; return _getPrototypeOf(o); }
var Container = __webpack_require__(1204);
var LazyResult, Processor;
var Document = /*#__PURE__*/function (_Container) {
  _inherits(Document, _Container);
  var _super = _createSuper(Document);
  function Document(defaults) {
    var _this;
    _classCallCheck(this, Document);
    // type needs to be passed to super, otherwise child roots won't be normalized correctly
    _this = _super.call(this, _objectSpread({
      type: 'document'
    }, defaults));
    if (!_this.nodes) {
      _this.nodes = [];
    }
    return _this;
  }
  _createClass(Document, [{
    key: "toResult",
    value: function toResult() {
      var opts = arguments.length > 0 && arguments[0] !== undefined ? arguments[0] : {};
      var lazy = new LazyResult(new Processor(), this, opts);
      return lazy.stringify();
    }
  }]);
  return Document;
}(Container);
Document.registerLazyResult = function (dependant) {
  LazyResult = dependant;
};
Document.registerProcessor = function (dependant) {
  Processor = dependant;
};
module.exports = Document;
Document["default"] = Document;

/***/ }),

/***/ 9295:
/***/ ((module, __unused_webpack_exports, __webpack_require__) => {

"use strict";


var _excluded = ["inputs"],
  _excluded2 = ["inputId"];
function ownKeys(object, enumerableOnly) { var keys = Object.keys(object); if (Object.getOwnPropertySymbols) { var symbols = Object.getOwnPropertySymbols(object); enumerableOnly && (symbols = symbols.filter(function (sym) { return Object.getOwnPropertyDescriptor(object, sym).enumerable; })), keys.push.apply(keys, symbols); } return keys; }
function _objectSpread(target) { for (var i = 1; i < arguments.length; i++) { var source = null != arguments[i] ? arguments[i] : {}; i % 2 ? ownKeys(Object(source), !0).forEach(function (key) { _defineProperty(target, key, source[key]); }) : Object.getOwnPropertyDescriptors ? Object.defineProperties(target, Object.getOwnPropertyDescriptors(source)) : ownKeys(Object(source)).forEach(function (key) { Object.defineProperty(target, key, Object.getOwnPropertyDescriptor(source, key)); }); } return target; }
function _defineProperty(obj, key, value) { if (key in obj) { Object.defineProperty(obj, key, { value: value, enumerable: true, configurable: true, writable: true }); } else { obj[key] = value; } return obj; }
function _createForOfIteratorHelper(o, allowArrayLike) { var it = typeof Symbol !== "undefined" && o[Symbol.iterator] || o["@@iterator"]; if (!it) { if (Array.isArray(o) || (it = _unsupportedIterableToArray(o)) || allowArrayLike && o && typeof o.length === "number") { if (it) o = it; var i = 0; var F = function F() {}; return { s: F, n: function n() { if (i >= o.length) return { done: true }; return { done: false, value: o[i++] }; }, e: function e(_e) { throw _e; }, f: F }; } throw new TypeError("Invalid attempt to iterate non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method."); } var normalCompletion = true, didErr = false, err; return { s: function s() { it = it.call(o); }, n: function n() { var step = it.next(); normalCompletion = step.done; return step; }, e: function e(_e2) { didErr = true; err = _e2; }, f: function f() { try { if (!normalCompletion && it["return"] != null) it["return"](); } finally { if (didErr) throw err; } } }; }
function _unsupportedIterableToArray(o, minLen) { if (!o) return; if (typeof o === "string") return _arrayLikeToArray(o, minLen); var n = Object.prototype.toString.call(o).slice(8, -1); if (n === "Object" && o.constructor) n = o.constructor.name; if (n === "Map" || n === "Set") return Array.from(o); if (n === "Arguments" || /^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(n)) return _arrayLikeToArray(o, minLen); }
function _arrayLikeToArray(arr, len) { if (len == null || len > arr.length) len = arr.length; for (var i = 0, arr2 = new Array(len); i < len; i++) { arr2[i] = arr[i]; } return arr2; }
function _objectWithoutProperties(source, excluded) { if (source == null) return {}; var target = _objectWithoutPropertiesLoose(source, excluded); var key, i; if (Object.getOwnPropertySymbols) { var sourceSymbolKeys = Object.getOwnPropertySymbols(source); for (i = 0; i < sourceSymbolKeys.length; i++) { key = sourceSymbolKeys[i]; if (excluded.indexOf(key) >= 0) continue; if (!Object.prototype.propertyIsEnumerable.call(source, key)) continue; target[key] = source[key]; } } return target; }
function _objectWithoutPropertiesLoose(source, excluded) { if (source == null) return {}; var target = {}; var sourceKeys = Object.keys(source); var key, i; for (i = 0; i < sourceKeys.length; i++) { key = sourceKeys[i]; if (excluded.indexOf(key) >= 0) continue; target[key] = source[key]; } return target; }
var Declaration = __webpack_require__(6417);
var PreviousMap = __webpack_require__(3353);
var Comment = __webpack_require__(3102);
var AtRule = __webpack_require__(8940);
var Input = __webpack_require__(2993);
var Root = __webpack_require__(7563);
var Rule = __webpack_require__(6621);
function fromJSON(json, inputs) {
  if (Array.isArray(json)) return json.map(function (n) {
    return fromJSON(n);
  });
  var ownInputs = json.inputs,
    defaults = _objectWithoutProperties(json, _excluded);
  if (ownInputs) {
    inputs = [];
    var _iterator = _createForOfIteratorHelper(ownInputs),
      _step;
    try {
      for (_iterator.s(); !(_step = _iterator.n()).done;) {
        var input = _step.value;
        var inputHydrated = _objectSpread(_objectSpread({}, input), {}, {
          __proto__: Input.prototype
        });
        if (inputHydrated.map) {
          inputHydrated.map = _objectSpread(_objectSpread({}, inputHydrated.map), {}, {
            __proto__: PreviousMap.prototype
          });
        }
        inputs.push(inputHydrated);
      }
    } catch (err) {
      _iterator.e(err);
    } finally {
      _iterator.f();
    }
  }
  if (defaults.nodes) {
    defaults.nodes = json.nodes.map(function (n) {
      return fromJSON(n, inputs);
    });
  }
  if (defaults.source) {
    var _defaults$source = defaults.source,
      inputId = _defaults$source.inputId,
      source = _objectWithoutProperties(_defaults$source, _excluded2);
    defaults.source = source;
    if (inputId != null) {
      defaults.source.input = inputs[inputId];
    }
  }
  if (defaults.type === 'root') {
    return new Root(defaults);
  } else if (defaults.type === 'decl') {
    return new Declaration(defaults);
  } else if (defaults.type === 'rule') {
    return new Rule(defaults);
  } else if (defaults.type === 'comment') {
    return new Comment(defaults);
  } else if (defaults.type === 'atrule') {
    return new AtRule(defaults);
  } else {
    throw new Error('Unknown node type: ' + json.type);
  }
}
module.exports = fromJSON;
fromJSON["default"] = fromJSON;

/***/ }),

/***/ 2993:
/***/ ((module, __unused_webpack_exports, __webpack_require__) => {

"use strict";


function ownKeys(object, enumerableOnly) { var keys = Object.keys(object); if (Object.getOwnPropertySymbols) { var symbols = Object.getOwnPropertySymbols(object); enumerableOnly && (symbols = symbols.filter(function (sym) { return Object.getOwnPropertyDescriptor(object, sym).enumerable; })), keys.push.apply(keys, symbols); } return keys; }
function _objectSpread(target) { for (var i = 1; i < arguments.length; i++) { var source = null != arguments[i] ? arguments[i] : {}; i % 2 ? ownKeys(Object(source), !0).forEach(function (key) { _defineProperty(target, key, source[key]); }) : Object.getOwnPropertyDescriptors ? Object.defineProperties(target, Object.getOwnPropertyDescriptors(source)) : ownKeys(Object(source)).forEach(function (key) { Object.defineProperty(target, key, Object.getOwnPropertyDescriptor(source, key)); }); } return target; }
function _defineProperty(obj, key, value) { if (key in obj) { Object.defineProperty(obj, key, { value: value, enumerable: true, configurable: true, writable: true }); } else { obj[key] = value; } return obj; }
function _typeof(obj) { "@babel/helpers - typeof"; return _typeof = "function" == typeof Symbol && "symbol" == typeof Symbol.iterator ? function (obj) { return typeof obj; } : function (obj) { return obj && "function" == typeof Symbol && obj.constructor === Symbol && obj !== Symbol.prototype ? "symbol" : typeof obj; }, _typeof(obj); }
function _classCallCheck(instance, Constructor) { if (!(instance instanceof Constructor)) { throw new TypeError("Cannot call a class as a function"); } }
function _defineProperties(target, props) { for (var i = 0; i < props.length; i++) { var descriptor = props[i]; descriptor.enumerable = descriptor.enumerable || false; descriptor.configurable = true; if ("value" in descriptor) descriptor.writable = true; Object.defineProperty(target, descriptor.key, descriptor); } }
function _createClass(Constructor, protoProps, staticProps) { if (protoProps) _defineProperties(Constructor.prototype, protoProps); if (staticProps) _defineProperties(Constructor, staticProps); Object.defineProperty(Constructor, "prototype", { writable: false }); return Constructor; }
var _require = __webpack_require__(209),
  SourceMapConsumer = _require.SourceMapConsumer,
  SourceMapGenerator = _require.SourceMapGenerator;
var _require2 = __webpack_require__(7414),
  fileURLToPath = _require2.fileURLToPath,
  pathToFileURL = _require2.pathToFileURL;
var _require3 = __webpack_require__(9830),
  resolve = _require3.resolve,
  isAbsolute = _require3.isAbsolute;
var _require4 = __webpack_require__(2961),
  nanoid = _require4.nanoid;
var terminalHighlight = __webpack_require__(2868);
var CssSyntaxError = __webpack_require__(1667);
var PreviousMap = __webpack_require__(3353);
var fromOffsetCache = Symbol('fromOffsetCache');
var sourceMapAvailable = Boolean(SourceMapConsumer && SourceMapGenerator);
var pathAvailable = Boolean(resolve && isAbsolute);
var Input = /*#__PURE__*/function () {
  function Input(css) {
    var opts = arguments.length > 1 && arguments[1] !== undefined ? arguments[1] : {};
    _classCallCheck(this, Input);
    if (css === null || typeof css === 'undefined' || _typeof(css) === 'object' && !css.toString) {
      throw new Error("PostCSS received ".concat(css, " instead of CSS string"));
    }
    this.css = css.toString();
    if (this.css[0] === "\uFEFF" || this.css[0] === "\uFFFE") {
      this.hasBOM = true;
      this.css = this.css.slice(1);
    } else {
      this.hasBOM = false;
    }
    if (opts.from) {
      if (!pathAvailable || /^\w+:\/\//.test(opts.from) || isAbsolute(opts.from)) {
        this.file = opts.from;
      } else {
        this.file = resolve(opts.from);
      }
    }
    if (pathAvailable && sourceMapAvailable) {
      var map = new PreviousMap(this.css, opts);
      if (map.text) {
        this.map = map;
        var file = map.consumer().file;
        if (!this.file && file) this.file = this.mapResolve(file);
      }
    }
    if (!this.file) {
      this.id = '<input css ' + nanoid(6) + '>';
    }
    if (this.map) this.map.file = this.from;
  }
  _createClass(Input, [{
    key: "fromOffset",
    value: function fromOffset(offset) {
      var lastLine, lineToIndex;
      if (!this[fromOffsetCache]) {
        var lines = this.css.split('\n');
        lineToIndex = new Array(lines.length);
        var prevIndex = 0;
        for (var i = 0, l = lines.length; i < l; i++) {
          lineToIndex[i] = prevIndex;
          prevIndex += lines[i].length + 1;
        }
        this[fromOffsetCache] = lineToIndex;
      } else {
        lineToIndex = this[fromOffsetCache];
      }
      lastLine = lineToIndex[lineToIndex.length - 1];
      var min = 0;
      if (offset >= lastLine) {
        min = lineToIndex.length - 1;
      } else {
        var max = lineToIndex.length - 2;
        var mid;
        while (min < max) {
          mid = min + (max - min >> 1);
          if (offset < lineToIndex[mid]) {
            max = mid - 1;
          } else if (offset >= lineToIndex[mid + 1]) {
            min = mid + 1;
          } else {
            min = mid;
            break;
          }
        }
      }
      return {
        line: min + 1,
        col: offset - lineToIndex[min] + 1
      };
    }
  }, {
    key: "error",
    value: function error(message, line, column) {
      var opts = arguments.length > 3 && arguments[3] !== undefined ? arguments[3] : {};
      var result, endLine, endColumn;
      if (line && _typeof(line) === 'object') {
        var start = line;
        var end = column;
        if (typeof line.offset === 'number') {
          var pos = this.fromOffset(start.offset);
          line = pos.line;
          column = pos.col;
        } else {
          line = start.line;
          column = start.column;
        }
        if (typeof end.offset === 'number') {
          var _pos = this.fromOffset(end.offset);
          endLine = _pos.line;
          endColumn = _pos.col;
        } else {
          endLine = end.line;
          endColumn = end.column;
        }
      } else if (!column) {
        var _pos2 = this.fromOffset(line);
        line = _pos2.line;
        column = _pos2.col;
      }
      var origin = this.origin(line, column, endLine, endColumn);
      if (origin) {
        result = new CssSyntaxError(message, origin.endLine === undefined ? origin.line : {
          line: origin.line,
          column: origin.column
        }, origin.endLine === undefined ? origin.column : {
          line: origin.endLine,
          column: origin.endColumn
        }, origin.source, origin.file, opts.plugin);
      } else {
        result = new CssSyntaxError(message, endLine === undefined ? line : {
          line: line,
          column: column
        }, endLine === undefined ? column : {
          line: endLine,
          column: endColumn
        }, this.css, this.file, opts.plugin);
      }
      result.input = {
        line: line,
        column: column,
        endLine: endLine,
        endColumn: endColumn,
        source: this.css
      };
      if (this.file) {
        if (pathToFileURL) {
          result.input.url = pathToFileURL(this.file).toString();
        }
        result.input.file = this.file;
      }
      return result;
    }
  }, {
    key: "origin",
    value: function origin(line, column, endLine, endColumn) {
      if (!this.map) return false;
      var consumer = this.map.consumer();
      var from = consumer.originalPositionFor({
        line: line,
        column: column
      });
      if (!from.source) return false;
      var to;
      if (typeof endLine === 'number') {
        to = consumer.originalPositionFor({
          line: endLine,
          column: endColumn
        });
      }
      var fromUrl;
      if (isAbsolute(from.source)) {
        fromUrl = pathToFileURL(from.source);
      } else {
        fromUrl = new URL(from.source, this.map.consumer().sourceRoot || pathToFileURL(this.map.mapFile));
      }
      var result = {
        url: fromUrl.toString(),
        line: from.line,
        column: from.column,
        endLine: to && to.line,
        endColumn: to && to.column
      };
      if (fromUrl.protocol === 'file:') {
        if (fileURLToPath) {
          result.file = fileURLToPath(fromUrl);
        } else {
          /* c8 ignore next 2 */
          throw new Error("file: protocol is not available in this PostCSS build");
        }
      }
      var source = consumer.sourceContentFor(from.source);
      if (source) result.source = source;
      return result;
    }
  }, {
    key: "mapResolve",
    value: function mapResolve(file) {
      if (/^\w+:\/\//.test(file)) {
        return file;
      }
      return resolve(this.map.consumer().sourceRoot || this.map.root || '.', file);
    }
  }, {
    key: "from",
    get: function get() {
      return this.file || this.id;
    }
  }, {
    key: "toJSON",
    value: function toJSON() {
      var json = {};
      for (var _i = 0, _arr = ['hasBOM', 'css', 'file', 'id']; _i < _arr.length; _i++) {
        var name = _arr[_i];
        if (this[name] != null) {
          json[name] = this[name];
        }
      }
      if (this.map) {
        json.map = _objectSpread({}, this.map);
        if (json.map.consumerCache) {
          json.map.consumerCache = undefined;
        }
      }
      return json;
    }
  }]);
  return Input;
}();
module.exports = Input;
Input["default"] = Input;
if (terminalHighlight && terminalHighlight.registerInput) {
  terminalHighlight.registerInput(Input);
}

/***/ }),

/***/ 6992:
/***/ ((module, __unused_webpack_exports, __webpack_require__) => {

"use strict";


function _regeneratorRuntime() { "use strict"; /*! regenerator-runtime -- Copyright (c) 2014-present, Facebook, Inc. -- license (MIT): https://github.com/facebook/regenerator/blob/main/LICENSE */ _regeneratorRuntime = function _regeneratorRuntime() { return exports; }; var exports = {}, Op = Object.prototype, hasOwn = Op.hasOwnProperty, defineProperty = Object.defineProperty || function (obj, key, desc) { obj[key] = desc.value; }, $Symbol = "function" == typeof Symbol ? Symbol : {}, iteratorSymbol = $Symbol.iterator || "@@iterator", asyncIteratorSymbol = $Symbol.asyncIterator || "@@asyncIterator", toStringTagSymbol = $Symbol.toStringTag || "@@toStringTag"; function define(obj, key, value) { return Object.defineProperty(obj, key, { value: value, enumerable: !0, configurable: !0, writable: !0 }), obj[key]; } try { define({}, ""); } catch (err) { define = function define(obj, key, value) { return obj[key] = value; }; } function wrap(innerFn, outerFn, self, tryLocsList) { var protoGenerator = outerFn && outerFn.prototype instanceof Generator ? outerFn : Generator, generator = Object.create(protoGenerator.prototype), context = new Context(tryLocsList || []); return defineProperty(generator, "_invoke", { value: makeInvokeMethod(innerFn, self, context) }), generator; } function tryCatch(fn, obj, arg) { try { return { type: "normal", arg: fn.call(obj, arg) }; } catch (err) { return { type: "throw", arg: err }; } } exports.wrap = wrap; var ContinueSentinel = {}; function Generator() {} function GeneratorFunction() {} function GeneratorFunctionPrototype() {} var IteratorPrototype = {}; define(IteratorPrototype, iteratorSymbol, function () { return this; }); var getProto = Object.getPrototypeOf, NativeIteratorPrototype = getProto && getProto(getProto(values([]))); NativeIteratorPrototype && NativeIteratorPrototype !== Op && hasOwn.call(NativeIteratorPrototype, iteratorSymbol) && (IteratorPrototype = NativeIteratorPrototype); var Gp = GeneratorFunctionPrototype.prototype = Generator.prototype = Object.create(IteratorPrototype); function defineIteratorMethods(prototype) { ["next", "throw", "return"].forEach(function (method) { define(prototype, method, function (arg) { return this._invoke(method, arg); }); }); } function AsyncIterator(generator, PromiseImpl) { function invoke(method, arg, resolve, reject) { var record = tryCatch(generator[method], generator, arg); if ("throw" !== record.type) { var result = record.arg, value = result.value; return value && "object" == _typeof(value) && hasOwn.call(value, "__await") ? PromiseImpl.resolve(value.__await).then(function (value) { invoke("next", value, resolve, reject); }, function (err) { invoke("throw", err, resolve, reject); }) : PromiseImpl.resolve(value).then(function (unwrapped) { result.value = unwrapped, resolve(result); }, function (error) { return invoke("throw", error, resolve, reject); }); } reject(record.arg); } var previousPromise; defineProperty(this, "_invoke", { value: function value(method, arg) { function callInvokeWithMethodAndArg() { return new PromiseImpl(function (resolve, reject) { invoke(method, arg, resolve, reject); }); } return previousPromise = previousPromise ? previousPromise.then(callInvokeWithMethodAndArg, callInvokeWithMethodAndArg) : callInvokeWithMethodAndArg(); } }); } function makeInvokeMethod(innerFn, self, context) { var state = "suspendedStart"; return function (method, arg) { if ("executing" === state) throw new Error("Generator is already running"); if ("completed" === state) { if ("throw" === method) throw arg; return doneResult(); } for (context.method = method, context.arg = arg;;) { var delegate = context.delegate; if (delegate) { var delegateResult = maybeInvokeDelegate(delegate, context); if (delegateResult) { if (delegateResult === ContinueSentinel) continue; return delegateResult; } } if ("next" === context.method) context.sent = context._sent = context.arg;else if ("throw" === context.method) { if ("suspendedStart" === state) throw state = "completed", context.arg; context.dispatchException(context.arg); } else "return" === context.method && context.abrupt("return", context.arg); state = "executing"; var record = tryCatch(innerFn, self, context); if ("normal" === record.type) { if (state = context.done ? "completed" : "suspendedYield", record.arg === ContinueSentinel) continue; return { value: record.arg, done: context.done }; } "throw" === record.type && (state = "completed", context.method = "throw", context.arg = record.arg); } }; } function maybeInvokeDelegate(delegate, context) { var method = delegate.iterator[context.method]; if (undefined === method) { if (context.delegate = null, "throw" === context.method) { if (delegate.iterator["return"] && (context.method = "return", context.arg = undefined, maybeInvokeDelegate(delegate, context), "throw" === context.method)) return ContinueSentinel; context.method = "throw", context.arg = new TypeError("The iterator does not provide a 'throw' method"); } return ContinueSentinel; } var record = tryCatch(method, delegate.iterator, context.arg); if ("throw" === record.type) return context.method = "throw", context.arg = record.arg, context.delegate = null, ContinueSentinel; var info = record.arg; return info ? info.done ? (context[delegate.resultName] = info.value, context.next = delegate.nextLoc, "return" !== context.method && (context.method = "next", context.arg = undefined), context.delegate = null, ContinueSentinel) : info : (context.method = "throw", context.arg = new TypeError("iterator result is not an object"), context.delegate = null, ContinueSentinel); } function pushTryEntry(locs) { var entry = { tryLoc: locs[0] }; 1 in locs && (entry.catchLoc = locs[1]), 2 in locs && (entry.finallyLoc = locs[2], entry.afterLoc = locs[3]), this.tryEntries.push(entry); } function resetTryEntry(entry) { var record = entry.completion || {}; record.type = "normal", delete record.arg, entry.completion = record; } function Context(tryLocsList) { this.tryEntries = [{ tryLoc: "root" }], tryLocsList.forEach(pushTryEntry, this), this.reset(!0); } function values(iterable) { if (iterable) { var iteratorMethod = iterable[iteratorSymbol]; if (iteratorMethod) return iteratorMethod.call(iterable); if ("function" == typeof iterable.next) return iterable; if (!isNaN(iterable.length)) { var i = -1, next = function next() { for (; ++i < iterable.length;) { if (hasOwn.call(iterable, i)) return next.value = iterable[i], next.done = !1, next; } return next.value = undefined, next.done = !0, next; }; return next.next = next; } } return { next: doneResult }; } function doneResult() { return { value: undefined, done: !0 }; } return GeneratorFunction.prototype = GeneratorFunctionPrototype, defineProperty(Gp, "constructor", { value: GeneratorFunctionPrototype, configurable: !0 }), defineProperty(GeneratorFunctionPrototype, "constructor", { value: GeneratorFunction, configurable: !0 }), GeneratorFunction.displayName = define(GeneratorFunctionPrototype, toStringTagSymbol, "GeneratorFunction"), exports.isGeneratorFunction = function (genFun) { var ctor = "function" == typeof genFun && genFun.constructor; return !!ctor && (ctor === GeneratorFunction || "GeneratorFunction" === (ctor.displayName || ctor.name)); }, exports.mark = function (genFun) { return Object.setPrototypeOf ? Object.setPrototypeOf(genFun, GeneratorFunctionPrototype) : (genFun.__proto__ = GeneratorFunctionPrototype, define(genFun, toStringTagSymbol, "GeneratorFunction")), genFun.prototype = Object.create(Gp), genFun; }, exports.awrap = function (arg) { return { __await: arg }; }, defineIteratorMethods(AsyncIterator.prototype), define(AsyncIterator.prototype, asyncIteratorSymbol, function () { return this; }), exports.AsyncIterator = AsyncIterator, exports.async = function (innerFn, outerFn, self, tryLocsList, PromiseImpl) { void 0 === PromiseImpl && (PromiseImpl = Promise); var iter = new AsyncIterator(wrap(innerFn, outerFn, self, tryLocsList), PromiseImpl); return exports.isGeneratorFunction(outerFn) ? iter : iter.next().then(function (result) { return result.done ? result.value : iter.next(); }); }, defineIteratorMethods(Gp), define(Gp, toStringTagSymbol, "Generator"), define(Gp, iteratorSymbol, function () { return this; }), define(Gp, "toString", function () { return "[object Generator]"; }), exports.keys = function (val) { var object = Object(val), keys = []; for (var key in object) { keys.push(key); } return keys.reverse(), function next() { for (; keys.length;) { var key = keys.pop(); if (key in object) return next.value = key, next.done = !1, next; } return next.done = !0, next; }; }, exports.values = values, Context.prototype = { constructor: Context, reset: function reset(skipTempReset) { if (this.prev = 0, this.next = 0, this.sent = this._sent = undefined, this.done = !1, this.delegate = null, this.method = "next", this.arg = undefined, this.tryEntries.forEach(resetTryEntry), !skipTempReset) for (var name in this) { "t" === name.charAt(0) && hasOwn.call(this, name) && !isNaN(+name.slice(1)) && (this[name] = undefined); } }, stop: function stop() { this.done = !0; var rootRecord = this.tryEntries[0].completion; if ("throw" === rootRecord.type) throw rootRecord.arg; return this.rval; }, dispatchException: function dispatchException(exception) { if (this.done) throw exception; var context = this; function handle(loc, caught) { return record.type = "throw", record.arg = exception, context.next = loc, caught && (context.method = "next", context.arg = undefined), !!caught; } for (var i = this.tryEntries.length - 1; i >= 0; --i) { var entry = this.tryEntries[i], record = entry.completion; if ("root" === entry.tryLoc) return handle("end"); if (entry.tryLoc <= this.prev) { var hasCatch = hasOwn.call(entry, "catchLoc"), hasFinally = hasOwn.call(entry, "finallyLoc"); if (hasCatch && hasFinally) { if (this.prev < entry.catchLoc) return handle(entry.catchLoc, !0); if (this.prev < entry.finallyLoc) return handle(entry.finallyLoc); } else if (hasCatch) { if (this.prev < entry.catchLoc) return handle(entry.catchLoc, !0); } else { if (!hasFinally) throw new Error("try statement without catch or finally"); if (this.prev < entry.finallyLoc) return handle(entry.finallyLoc); } } } }, abrupt: function abrupt(type, arg) { for (var i = this.tryEntries.length - 1; i >= 0; --i) { var entry = this.tryEntries[i]; if (entry.tryLoc <= this.prev && hasOwn.call(entry, "finallyLoc") && this.prev < entry.finallyLoc) { var finallyEntry = entry; break; } } finallyEntry && ("break" === type || "continue" === type) && finallyEntry.tryLoc <= arg && arg <= finallyEntry.finallyLoc && (finallyEntry = null); var record = finallyEntry ? finallyEntry.completion : {}; return record.type = type, record.arg = arg, finallyEntry ? (this.method = "next", this.next = finallyEntry.finallyLoc, ContinueSentinel) : this.complete(record); }, complete: function complete(record, afterLoc) { if ("throw" === record.type) throw record.arg; return "break" === record.type || "continue" === record.type ? this.next = record.arg : "return" === record.type ? (this.rval = this.arg = record.arg, this.method = "return", this.next = "end") : "normal" === record.type && afterLoc && (this.next = afterLoc), ContinueSentinel; }, finish: function finish(finallyLoc) { for (var i = this.tryEntries.length - 1; i >= 0; --i) { var entry = this.tryEntries[i]; if (entry.finallyLoc === finallyLoc) return this.complete(entry.completion, entry.afterLoc), resetTryEntry(entry), ContinueSentinel; } }, "catch": function _catch(tryLoc) { for (var i = this.tryEntries.length - 1; i >= 0; --i) { var entry = this.tryEntries[i]; if (entry.tryLoc === tryLoc) { var record = entry.completion; if ("throw" === record.type) { var thrown = record.arg; resetTryEntry(entry); } return thrown; } } throw new Error("illegal catch attempt"); }, delegateYield: function delegateYield(iterable, resultName, nextLoc) { return this.delegate = { iterator: values(iterable), resultName: resultName, nextLoc: nextLoc }, "next" === this.method && (this.arg = undefined), ContinueSentinel; } }, exports; }
function asyncGeneratorStep(gen, resolve, reject, _next, _throw, key, arg) { try { var info = gen[key](arg); var value = info.value; } catch (error) { reject(error); return; } if (info.done) { resolve(value); } else { Promise.resolve(value).then(_next, _throw); } }
function _asyncToGenerator(fn) { return function () { var self = this, args = arguments; return new Promise(function (resolve, reject) { var gen = fn.apply(self, args); function _next(value) { asyncGeneratorStep(gen, resolve, reject, _next, _throw, "next", value); } function _throw(err) { asyncGeneratorStep(gen, resolve, reject, _next, _throw, "throw", err); } _next(undefined); }); }; }
function _slicedToArray(arr, i) { return _arrayWithHoles(arr) || _iterableToArrayLimit(arr, i) || _unsupportedIterableToArray(arr, i) || _nonIterableRest(); }
function _nonIterableRest() { throw new TypeError("Invalid attempt to destructure non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method."); }
function _iterableToArrayLimit(arr, i) { var _i = arr == null ? null : typeof Symbol !== "undefined" && arr[Symbol.iterator] || arr["@@iterator"]; if (_i == null) return; var _arr = []; var _n = true; var _d = false; var _s, _e; try { for (_i = _i.call(arr); !(_n = (_s = _i.next()).done); _n = true) { _arr.push(_s.value); if (i && _arr.length === i) break; } } catch (err) { _d = true; _e = err; } finally { try { if (!_n && _i["return"] != null) _i["return"](); } finally { if (_d) throw _e; } } return _arr; }
function _arrayWithHoles(arr) { if (Array.isArray(arr)) return arr; }
function _createForOfIteratorHelper(o, allowArrayLike) { var it = typeof Symbol !== "undefined" && o[Symbol.iterator] || o["@@iterator"]; if (!it) { if (Array.isArray(o) || (it = _unsupportedIterableToArray(o)) || allowArrayLike && o && typeof o.length === "number") { if (it) o = it; var i = 0; var F = function F() {}; return { s: F, n: function n() { if (i >= o.length) return { done: true }; return { done: false, value: o[i++] }; }, e: function e(_e2) { throw _e2; }, f: F }; } throw new TypeError("Invalid attempt to iterate non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method."); } var normalCompletion = true, didErr = false, err; return { s: function s() { it = it.call(o); }, n: function n() { var step = it.next(); normalCompletion = step.done; return step; }, e: function e(_e3) { didErr = true; err = _e3; }, f: function f() { try { if (!normalCompletion && it["return"] != null) it["return"](); } finally { if (didErr) throw err; } } }; }
function _unsupportedIterableToArray(o, minLen) { if (!o) return; if (typeof o === "string") return _arrayLikeToArray(o, minLen); var n = Object.prototype.toString.call(o).slice(8, -1); if (n === "Object" && o.constructor) n = o.constructor.name; if (n === "Map" || n === "Set") return Array.from(o); if (n === "Arguments" || /^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(n)) return _arrayLikeToArray(o, minLen); }
function _arrayLikeToArray(arr, len) { if (len == null || len > arr.length) len = arr.length; for (var i = 0, arr2 = new Array(len); i < len; i++) { arr2[i] = arr[i]; } return arr2; }
function ownKeys(object, enumerableOnly) { var keys = Object.keys(object); if (Object.getOwnPropertySymbols) { var symbols = Object.getOwnPropertySymbols(object); enumerableOnly && (symbols = symbols.filter(function (sym) { return Object.getOwnPropertyDescriptor(object, sym).enumerable; })), keys.push.apply(keys, symbols); } return keys; }
function _objectSpread(target) { for (var i = 1; i < arguments.length; i++) { var source = null != arguments[i] ? arguments[i] : {}; i % 2 ? ownKeys(Object(source), !0).forEach(function (key) { _defineProperty(target, key, source[key]); }) : Object.getOwnPropertyDescriptors ? Object.defineProperties(target, Object.getOwnPropertyDescriptors(source)) : ownKeys(Object(source)).forEach(function (key) { Object.defineProperty(target, key, Object.getOwnPropertyDescriptor(source, key)); }); } return target; }
function _defineProperty(obj, key, value) { if (key in obj) { Object.defineProperty(obj, key, { value: value, enumerable: true, configurable: true, writable: true }); } else { obj[key] = value; } return obj; }
function _classCallCheck(instance, Constructor) { if (!(instance instanceof Constructor)) { throw new TypeError("Cannot call a class as a function"); } }
function _defineProperties(target, props) { for (var i = 0; i < props.length; i++) { var descriptor = props[i]; descriptor.enumerable = descriptor.enumerable || false; descriptor.configurable = true; if ("value" in descriptor) descriptor.writable = true; Object.defineProperty(target, descriptor.key, descriptor); } }
function _createClass(Constructor, protoProps, staticProps) { if (protoProps) _defineProperties(Constructor.prototype, protoProps); if (staticProps) _defineProperties(Constructor, staticProps); Object.defineProperty(Constructor, "prototype", { writable: false }); return Constructor; }
function _typeof(obj) { "@babel/helpers - typeof"; return _typeof = "function" == typeof Symbol && "symbol" == typeof Symbol.iterator ? function (obj) { return typeof obj; } : function (obj) { return obj && "function" == typeof Symbol && obj.constructor === Symbol && obj !== Symbol.prototype ? "symbol" : typeof obj; }, _typeof(obj); }
var _require = __webpack_require__(5506),
  isClean = _require.isClean,
  my = _require.my;
var MapGenerator = __webpack_require__(8991);
var _stringify = __webpack_require__(6157);
var Container = __webpack_require__(1204);
var Document = __webpack_require__(7083);
var warnOnce = __webpack_require__(6574);
var Result = __webpack_require__(6865);
var parse = __webpack_require__(7057);
var Root = __webpack_require__(7563);
var TYPE_TO_CLASS_NAME = {
  document: 'Document',
  root: 'Root',
  atrule: 'AtRule',
  rule: 'Rule',
  decl: 'Declaration',
  comment: 'Comment'
};
var PLUGIN_PROPS = {
  postcssPlugin: true,
  prepare: true,
  Once: true,
  Document: true,
  Root: true,
  Declaration: true,
  Rule: true,
  AtRule: true,
  Comment: true,
  DeclarationExit: true,
  RuleExit: true,
  AtRuleExit: true,
  CommentExit: true,
  RootExit: true,
  DocumentExit: true,
  OnceExit: true
};
var NOT_VISITORS = {
  postcssPlugin: true,
  prepare: true,
  Once: true
};
var CHILDREN = 0;
function isPromise(obj) {
  return _typeof(obj) === 'object' && typeof obj.then === 'function';
}
function getEvents(node) {
  var key = false;
  var type = TYPE_TO_CLASS_NAME[node.type];
  if (node.type === 'decl') {
    key = node.prop.toLowerCase();
  } else if (node.type === 'atrule') {
    key = node.name.toLowerCase();
  }
  if (key && node.append) {
    return [type, type + '-' + key, CHILDREN, type + 'Exit', type + 'Exit-' + key];
  } else if (key) {
    return [type, type + '-' + key, type + 'Exit', type + 'Exit-' + key];
  } else if (node.append) {
    return [type, CHILDREN, type + 'Exit'];
  } else {
    return [type, type + 'Exit'];
  }
}
function toStack(node) {
  var events;
  if (node.type === 'document') {
    events = ['Document', CHILDREN, 'DocumentExit'];
  } else if (node.type === 'root') {
    events = ['Root', CHILDREN, 'RootExit'];
  } else {
    events = getEvents(node);
  }
  return {
    node: node,
    events: events,
    eventIndex: 0,
    visitors: [],
    visitorIndex: 0,
    iterator: 0
  };
}
function cleanMarks(node) {
  node[isClean] = false;
  if (node.nodes) node.nodes.forEach(function (i) {
    return cleanMarks(i);
  });
  return node;
}
var postcss = {};
var LazyResult = /*#__PURE__*/function (_Symbol$toStringTag) {
  function LazyResult(processor, css, opts) {
    var _this = this;
    _classCallCheck(this, LazyResult);
    this.stringified = false;
    this.processed = false;
    var root;
    if (_typeof(css) === 'object' && css !== null && (css.type === 'root' || css.type === 'document')) {
      root = cleanMarks(css);
    } else if (css instanceof LazyResult || css instanceof Result) {
      root = cleanMarks(css.root);
      if (css.map) {
        if (typeof opts.map === 'undefined') opts.map = {};
        if (!opts.map.inline) opts.map.inline = false;
        opts.map.prev = css.map;
      }
    } else {
      var parser = parse;
      if (opts.syntax) parser = opts.syntax.parse;
      if (opts.parser) parser = opts.parser;
      if (parser.parse) parser = parser.parse;
      try {
        root = parser(css, opts);
      } catch (error) {
        this.processed = true;
        this.error = error;
      }
      if (root && !root[my]) {
        /* c8 ignore next 2 */
        Container.rebuild(root);
      }
    }
    this.result = new Result(processor, root, opts);
    this.helpers = _objectSpread(_objectSpread({}, postcss), {}, {
      result: this.result,
      postcss: postcss
    });
    this.plugins = this.processor.plugins.map(function (plugin) {
      if (_typeof(plugin) === 'object' && plugin.prepare) {
        return _objectSpread(_objectSpread({}, plugin), plugin.prepare(_this.result));
      } else {
        return plugin;
      }
    });
  }
  _createClass(LazyResult, [{
    key: _Symbol$toStringTag,
    get: function get() {
      return 'LazyResult';
    }
  }, {
    key: "processor",
    get: function get() {
      return this.result.processor;
    }
  }, {
    key: "opts",
    get: function get() {
      return this.result.opts;
    }
  }, {
    key: "css",
    get: function get() {
      return this.stringify().css;
    }
  }, {
    key: "content",
    get: function get() {
      return this.stringify().content;
    }
  }, {
    key: "map",
    get: function get() {
      return this.stringify().map;
    }
  }, {
    key: "root",
    get: function get() {
      return this.sync().root;
    }
  }, {
    key: "messages",
    get: function get() {
      return this.sync().messages;
    }
  }, {
    key: "warnings",
    value: function warnings() {
      return this.sync().warnings();
    }
  }, {
    key: "toString",
    value: function toString() {
      return this.css;
    }
  }, {
    key: "then",
    value: function then(onFulfilled, onRejected) {
      if (false) {}
      return this.async().then(onFulfilled, onRejected);
    }
  }, {
    key: "catch",
    value: function _catch(onRejected) {
      return this.async()["catch"](onRejected);
    }
  }, {
    key: "finally",
    value: function _finally(onFinally) {
      return this.async().then(onFinally, onFinally);
    }
  }, {
    key: "async",
    value: function async() {
      if (this.error) return Promise.reject(this.error);
      if (this.processed) return Promise.resolve(this.result);
      if (!this.processing) {
        this.processing = this.runAsync();
      }
      return this.processing;
    }
  }, {
    key: "sync",
    value: function sync() {
      if (this.error) throw this.error;
      if (this.processed) return this.result;
      this.processed = true;
      if (this.processing) {
        throw this.getAsyncError();
      }
      var _iterator = _createForOfIteratorHelper(this.plugins),
        _step;
      try {
        for (_iterator.s(); !(_step = _iterator.n()).done;) {
          var plugin = _step.value;
          var promise = this.runOnRoot(plugin);
          if (isPromise(promise)) {
            throw this.getAsyncError();
          }
        }
      } catch (err) {
        _iterator.e(err);
      } finally {
        _iterator.f();
      }
      this.prepareVisitors();
      if (this.hasListener) {
        var root = this.result.root;
        while (!root[isClean]) {
          root[isClean] = true;
          this.walkSync(root);
        }
        if (this.listeners.OnceExit) {
          if (root.type === 'document') {
            var _iterator2 = _createForOfIteratorHelper(root.nodes),
              _step2;
            try {
              for (_iterator2.s(); !(_step2 = _iterator2.n()).done;) {
                var subRoot = _step2.value;
                this.visitSync(this.listeners.OnceExit, subRoot);
              }
            } catch (err) {
              _iterator2.e(err);
            } finally {
              _iterator2.f();
            }
          } else {
            this.visitSync(this.listeners.OnceExit, root);
          }
        }
      }
      return this.result;
    }
  }, {
    key: "stringify",
    value: function stringify() {
      if (this.error) throw this.error;
      if (this.stringified) return this.result;
      this.stringified = true;
      this.sync();
      var opts = this.result.opts;
      var str = _stringify;
      if (opts.syntax) str = opts.syntax.stringify;
      if (opts.stringifier) str = opts.stringifier;
      if (str.stringify) str = str.stringify;
      var map = new MapGenerator(str, this.result.root, this.result.opts);
      var data = map.generate();
      this.result.css = data[0];
      this.result.map = data[1];
      return this.result;
    }
  }, {
    key: "walkSync",
    value: function walkSync(node) {
      var _this2 = this;
      node[isClean] = true;
      var events = getEvents(node);
      var _iterator3 = _createForOfIteratorHelper(events),
        _step3;
      try {
        for (_iterator3.s(); !(_step3 = _iterator3.n()).done;) {
          var event = _step3.value;
          if (event === CHILDREN) {
            if (node.nodes) {
              node.each(function (child) {
                if (!child[isClean]) _this2.walkSync(child);
              });
            }
          } else {
            var visitors = this.listeners[event];
            if (visitors) {
              if (this.visitSync(visitors, node.toProxy())) return;
            }
          }
        }
      } catch (err) {
        _iterator3.e(err);
      } finally {
        _iterator3.f();
      }
    }
  }, {
    key: "visitSync",
    value: function visitSync(visitors, node) {
      var _iterator4 = _createForOfIteratorHelper(visitors),
        _step4;
      try {
        for (_iterator4.s(); !(_step4 = _iterator4.n()).done;) {
          var _step4$value = _slicedToArray(_step4.value, 2),
            plugin = _step4$value[0],
            visitor = _step4$value[1];
          this.result.lastPlugin = plugin;
          var promise = void 0;
          try {
            promise = visitor(node, this.helpers);
          } catch (e) {
            throw this.handleError(e, node.proxyOf);
          }
          if (node.type !== 'root' && node.type !== 'document' && !node.parent) {
            return true;
          }
          if (isPromise(promise)) {
            throw this.getAsyncError();
          }
        }
      } catch (err) {
        _iterator4.e(err);
      } finally {
        _iterator4.f();
      }
    }
  }, {
    key: "runOnRoot",
    value: function runOnRoot(plugin) {
      var _this3 = this;
      this.result.lastPlugin = plugin;
      try {
        if (_typeof(plugin) === 'object' && plugin.Once) {
          if (this.result.root.type === 'document') {
            var roots = this.result.root.nodes.map(function (root) {
              return plugin.Once(root, _this3.helpers);
            });
            if (isPromise(roots[0])) {
              return Promise.all(roots);
            }
            return roots;
          }
          return plugin.Once(this.result.root, this.helpers);
        } else if (typeof plugin === 'function') {
          return plugin(this.result.root, this.result);
        }
      } catch (error) {
        throw this.handleError(error);
      }
    }
  }, {
    key: "getAsyncError",
    value: function getAsyncError() {
      throw new Error('Use process(css).then(cb) to work with async plugins');
    }
  }, {
    key: "handleError",
    value: function handleError(error, node) {
      var plugin = this.result.lastPlugin;
      try {
        if (node) node.addToError(error);
        this.error = error;
        if (error.name === 'CssSyntaxError' && !error.plugin) {
          error.plugin = plugin.postcssPlugin;
          error.setMessage();
        } else if (plugin.postcssVersion) {
          if (false) { var b, a, runtimeVer, pluginVer, pluginName; }
        }
      } catch (err) {
        /* c8 ignore next 3 */
        // eslint-disable-next-line no-console
        if (console && console.error) console.error(err);
      }
      return error;
    }
  }, {
    key: "runAsync",
    value: function () {
      var _runAsync = _asyncToGenerator( /*#__PURE__*/_regeneratorRuntime().mark(function _callee() {
        var _this4 = this;
        var i, plugin, promise, root, stack, _promise, node, _iterator5, _step5, _loop;
        return _regeneratorRuntime().wrap(function _callee$(_context2) {
          while (1) {
            switch (_context2.prev = _context2.next) {
              case 0:
                this.plugin = 0;
                i = 0;
              case 2:
                if (!(i < this.plugins.length)) {
                  _context2.next = 17;
                  break;
                }
                plugin = this.plugins[i];
                promise = this.runOnRoot(plugin);
                if (!isPromise(promise)) {
                  _context2.next = 14;
                  break;
                }
                _context2.prev = 6;
                _context2.next = 9;
                return promise;
              case 9:
                _context2.next = 14;
                break;
              case 11:
                _context2.prev = 11;
                _context2.t0 = _context2["catch"](6);
                throw this.handleError(_context2.t0);
              case 14:
                i++;
                _context2.next = 2;
                break;
              case 17:
                this.prepareVisitors();
                if (!this.hasListener) {
                  _context2.next = 56;
                  break;
                }
                root = this.result.root;
              case 20:
                if (root[isClean]) {
                  _context2.next = 39;
                  break;
                }
                root[isClean] = true;
                stack = [toStack(root)];
              case 23:
                if (!(stack.length > 0)) {
                  _context2.next = 37;
                  break;
                }
                _promise = this.visitTick(stack);
                if (!isPromise(_promise)) {
                  _context2.next = 35;
                  break;
                }
                _context2.prev = 26;
                _context2.next = 29;
                return _promise;
              case 29:
                _context2.next = 35;
                break;
              case 31:
                _context2.prev = 31;
                _context2.t1 = _context2["catch"](26);
                node = stack[stack.length - 1].node;
                throw this.handleError(_context2.t1, node);
              case 35:
                _context2.next = 23;
                break;
              case 37:
                _context2.next = 20;
                break;
              case 39:
                if (!this.listeners.OnceExit) {
                  _context2.next = 56;
                  break;
                }
                _iterator5 = _createForOfIteratorHelper(this.listeners.OnceExit);
                _context2.prev = 41;
                _loop = /*#__PURE__*/_regeneratorRuntime().mark(function _loop() {
                  var _step5$value, plugin, visitor, roots;
                  return _regeneratorRuntime().wrap(function _loop$(_context) {
                    while (1) {
                      switch (_context.prev = _context.next) {
                        case 0:
                          _step5$value = _slicedToArray(_step5.value, 2), plugin = _step5$value[0], visitor = _step5$value[1];
                          _this4.result.lastPlugin = plugin;
                          _context.prev = 2;
                          if (!(root.type === 'document')) {
                            _context.next = 9;
                            break;
                          }
                          roots = root.nodes.map(function (subRoot) {
                            return visitor(subRoot, _this4.helpers);
                          });
                          _context.next = 7;
                          return Promise.all(roots);
                        case 7:
                          _context.next = 11;
                          break;
                        case 9:
                          _context.next = 11;
                          return visitor(root, _this4.helpers);
                        case 11:
                          _context.next = 16;
                          break;
                        case 13:
                          _context.prev = 13;
                          _context.t0 = _context["catch"](2);
                          throw _this4.handleError(_context.t0);
                        case 16:
                        case "end":
                          return _context.stop();
                      }
                    }
                  }, _loop, null, [[2, 13]]);
                });
                _iterator5.s();
              case 44:
                if ((_step5 = _iterator5.n()).done) {
                  _context2.next = 48;
                  break;
                }
                return _context2.delegateYield(_loop(), "t2", 46);
              case 46:
                _context2.next = 44;
                break;
              case 48:
                _context2.next = 53;
                break;
              case 50:
                _context2.prev = 50;
                _context2.t3 = _context2["catch"](41);
                _iterator5.e(_context2.t3);
              case 53:
                _context2.prev = 53;
                _iterator5.f();
                return _context2.finish(53);
              case 56:
                this.processed = true;
                return _context2.abrupt("return", this.stringify());
              case 58:
              case "end":
                return _context2.stop();
            }
          }
        }, _callee, this, [[6, 11], [26, 31], [41, 50, 53, 56]]);
      }));
      function runAsync() {
        return _runAsync.apply(this, arguments);
      }
      return runAsync;
    }()
  }, {
    key: "prepareVisitors",
    value: function prepareVisitors() {
      var _this5 = this;
      this.listeners = {};
      var add = function add(plugin, type, cb) {
        if (!_this5.listeners[type]) _this5.listeners[type] = [];
        _this5.listeners[type].push([plugin, cb]);
      };
      var _iterator6 = _createForOfIteratorHelper(this.plugins),
        _step6;
      try {
        for (_iterator6.s(); !(_step6 = _iterator6.n()).done;) {
          var plugin = _step6.value;
          if (_typeof(plugin) === 'object') {
            for (var event in plugin) {
              if (!PLUGIN_PROPS[event] && /^[A-Z]/.test(event)) {
                throw new Error("Unknown event ".concat(event, " in ").concat(plugin.postcssPlugin, ". ") + "Try to update PostCSS (".concat(this.processor.version, " now)."));
              }
              if (!NOT_VISITORS[event]) {
                if (_typeof(plugin[event]) === 'object') {
                  for (var filter in plugin[event]) {
                    if (filter === '*') {
                      add(plugin, event, plugin[event][filter]);
                    } else {
                      add(plugin, event + '-' + filter.toLowerCase(), plugin[event][filter]);
                    }
                  }
                } else if (typeof plugin[event] === 'function') {
                  add(plugin, event, plugin[event]);
                }
              }
            }
          }
        }
      } catch (err) {
        _iterator6.e(err);
      } finally {
        _iterator6.f();
      }
      this.hasListener = Object.keys(this.listeners).length > 0;
    }
  }, {
    key: "visitTick",
    value: function visitTick(stack) {
      var visit = stack[stack.length - 1];
      var node = visit.node,
        visitors = visit.visitors;
      if (node.type !== 'root' && node.type !== 'document' && !node.parent) {
        stack.pop();
        return;
      }
      if (visitors.length > 0 && visit.visitorIndex < visitors.length) {
        var _visitors$visit$visit = _slicedToArray(visitors[visit.visitorIndex], 2),
          plugin = _visitors$visit$visit[0],
          visitor = _visitors$visit$visit[1];
        visit.visitorIndex += 1;
        if (visit.visitorIndex === visitors.length) {
          visit.visitors = [];
          visit.visitorIndex = 0;
        }
        this.result.lastPlugin = plugin;
        try {
          return visitor(node.toProxy(), this.helpers);
        } catch (e) {
          throw this.handleError(e, node);
        }
      }
      if (visit.iterator !== 0) {
        var iterator = visit.iterator;
        var child;
        while (child = node.nodes[node.indexes[iterator]]) {
          node.indexes[iterator] += 1;
          if (!child[isClean]) {
            child[isClean] = true;
            stack.push(toStack(child));
            return;
          }
        }
        visit.iterator = 0;
        delete node.indexes[iterator];
      }
      var events = visit.events;
      while (visit.eventIndex < events.length) {
        var event = events[visit.eventIndex];
        visit.eventIndex += 1;
        if (event === CHILDREN) {
          if (node.nodes && node.nodes.length) {
            node[isClean] = true;
            visit.iterator = node.getIterator();
          }
          return;
        } else if (this.listeners[event]) {
          visit.visitors = this.listeners[event];
          return;
        }
      }
      stack.pop();
    }
  }]);
  return LazyResult;
}(Symbol.toStringTag);
LazyResult.registerPostcss = function (dependant) {
  postcss = dependant;
};
module.exports = LazyResult;
LazyResult["default"] = LazyResult;
Root.registerLazyResult(LazyResult);
Document.registerLazyResult(LazyResult);

/***/ }),

/***/ 6136:
/***/ ((module) => {

"use strict";


function _createForOfIteratorHelper(o, allowArrayLike) { var it = typeof Symbol !== "undefined" && o[Symbol.iterator] || o["@@iterator"]; if (!it) { if (Array.isArray(o) || (it = _unsupportedIterableToArray(o)) || allowArrayLike && o && typeof o.length === "number") { if (it) o = it; var i = 0; var F = function F() {}; return { s: F, n: function n() { if (i >= o.length) return { done: true }; return { done: false, value: o[i++] }; }, e: function e(_e) { throw _e; }, f: F }; } throw new TypeError("Invalid attempt to iterate non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method."); } var normalCompletion = true, didErr = false, err; return { s: function s() { it = it.call(o); }, n: function n() { var step = it.next(); normalCompletion = step.done; return step; }, e: function e(_e2) { didErr = true; err = _e2; }, f: function f() { try { if (!normalCompletion && it["return"] != null) it["return"](); } finally { if (didErr) throw err; } } }; }
function _unsupportedIterableToArray(o, minLen) { if (!o) return; if (typeof o === "string") return _arrayLikeToArray(o, minLen); var n = Object.prototype.toString.call(o).slice(8, -1); if (n === "Object" && o.constructor) n = o.constructor.name; if (n === "Map" || n === "Set") return Array.from(o); if (n === "Arguments" || /^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(n)) return _arrayLikeToArray(o, minLen); }
function _arrayLikeToArray(arr, len) { if (len == null || len > arr.length) len = arr.length; for (var i = 0, arr2 = new Array(len); i < len; i++) { arr2[i] = arr[i]; } return arr2; }
var list = {
  split: function split(string, separators, last) {
    var array = [];
    var current = '';
    var split = false;
    var func = 0;
    var inQuote = false;
    var prevQuote = '';
    var escape = false;
    var _iterator = _createForOfIteratorHelper(string),
      _step;
    try {
      for (_iterator.s(); !(_step = _iterator.n()).done;) {
        var letter = _step.value;
        if (escape) {
          escape = false;
        } else if (letter === '\\') {
          escape = true;
        } else if (inQuote) {
          if (letter === prevQuote) {
            inQuote = false;
          }
        } else if (letter === '"' || letter === "'") {
          inQuote = true;
          prevQuote = letter;
        } else if (letter === '(') {
          func += 1;
        } else if (letter === ')') {
          if (func > 0) func -= 1;
        } else if (func === 0) {
          if (separators.includes(letter)) split = true;
        }
        if (split) {
          if (current !== '') array.push(current.trim());
          current = '';
          split = false;
        } else {
          current += letter;
        }
      }
    } catch (err) {
      _iterator.e(err);
    } finally {
      _iterator.f();
    }
    if (last || current !== '') array.push(current.trim());
    return array;
  },
  space: function space(string) {
    var spaces = [' ', '\n', '\t'];
    return list.split(string, spaces);
  },
  comma: function comma(string) {
    return list.split(string, [','], true);
  }
};
module.exports = list;
list["default"] = list;

/***/ }),

/***/ 8991:
/***/ ((module, __unused_webpack_exports, __webpack_require__) => {

"use strict";


function _createForOfIteratorHelper(o, allowArrayLike) { var it = typeof Symbol !== "undefined" && o[Symbol.iterator] || o["@@iterator"]; if (!it) { if (Array.isArray(o) || (it = _unsupportedIterableToArray(o)) || allowArrayLike && o && typeof o.length === "number") { if (it) o = it; var i = 0; var F = function F() {}; return { s: F, n: function n() { if (i >= o.length) return { done: true }; return { done: false, value: o[i++] }; }, e: function e(_e) { throw _e; }, f: F }; } throw new TypeError("Invalid attempt to iterate non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method."); } var normalCompletion = true, didErr = false, err; return { s: function s() { it = it.call(o); }, n: function n() { var step = it.next(); normalCompletion = step.done; return step; }, e: function e(_e2) { didErr = true; err = _e2; }, f: function f() { try { if (!normalCompletion && it["return"] != null) it["return"](); } finally { if (didErr) throw err; } } }; }
function _unsupportedIterableToArray(o, minLen) { if (!o) return; if (typeof o === "string") return _arrayLikeToArray(o, minLen); var n = Object.prototype.toString.call(o).slice(8, -1); if (n === "Object" && o.constructor) n = o.constructor.name; if (n === "Map" || n === "Set") return Array.from(o); if (n === "Arguments" || /^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(n)) return _arrayLikeToArray(o, minLen); }
function _arrayLikeToArray(arr, len) { if (len == null || len > arr.length) len = arr.length; for (var i = 0, arr2 = new Array(len); i < len; i++) { arr2[i] = arr[i]; } return arr2; }
function _classCallCheck(instance, Constructor) { if (!(instance instanceof Constructor)) { throw new TypeError("Cannot call a class as a function"); } }
function _defineProperties(target, props) { for (var i = 0; i < props.length; i++) { var descriptor = props[i]; descriptor.enumerable = descriptor.enumerable || false; descriptor.configurable = true; if ("value" in descriptor) descriptor.writable = true; Object.defineProperty(target, descriptor.key, descriptor); } }
function _createClass(Constructor, protoProps, staticProps) { if (protoProps) _defineProperties(Constructor.prototype, protoProps); if (staticProps) _defineProperties(Constructor, staticProps); Object.defineProperty(Constructor, "prototype", { writable: false }); return Constructor; }
var _require = __webpack_require__(209),
  SourceMapConsumer = _require.SourceMapConsumer,
  SourceMapGenerator = _require.SourceMapGenerator;
var _require2 = __webpack_require__(9830),
  dirname = _require2.dirname,
  resolve = _require2.resolve,
  relative = _require2.relative,
  sep = _require2.sep;
var _require3 = __webpack_require__(7414),
  pathToFileURL = _require3.pathToFileURL;
var Input = __webpack_require__(2993);
var sourceMapAvailable = Boolean(SourceMapConsumer && SourceMapGenerator);
var pathAvailable = Boolean(dirname && resolve && relative && sep);
var MapGenerator = /*#__PURE__*/function () {
  function MapGenerator(stringify, root, opts, cssString) {
    _classCallCheck(this, MapGenerator);
    this.stringify = stringify;
    this.mapOpts = opts.map || {};
    this.root = root;
    this.opts = opts;
    this.css = cssString;
    this.usesFileUrls = !this.mapOpts.from && this.mapOpts.absolute;
  }
  _createClass(MapGenerator, [{
    key: "isMap",
    value: function isMap() {
      if (typeof this.opts.map !== 'undefined') {
        return !!this.opts.map;
      }
      return this.previous().length > 0;
    }
  }, {
    key: "previous",
    value: function previous() {
      var _this = this;
      if (!this.previousMaps) {
        this.previousMaps = [];
        if (this.root) {
          this.root.walk(function (node) {
            if (node.source && node.source.input.map) {
              var map = node.source.input.map;
              if (!_this.previousMaps.includes(map)) {
                _this.previousMaps.push(map);
              }
            }
          });
        } else {
          var input = new Input(this.css, this.opts);
          if (input.map) this.previousMaps.push(input.map);
        }
      }
      return this.previousMaps;
    }
  }, {
    key: "isInline",
    value: function isInline() {
      if (typeof this.mapOpts.inline !== 'undefined') {
        return this.mapOpts.inline;
      }
      var annotation = this.mapOpts.annotation;
      if (typeof annotation !== 'undefined' && annotation !== true) {
        return false;
      }
      if (this.previous().length) {
        return this.previous().some(function (i) {
          return i.inline;
        });
      }
      return true;
    }
  }, {
    key: "isSourcesContent",
    value: function isSourcesContent() {
      if (typeof this.mapOpts.sourcesContent !== 'undefined') {
        return this.mapOpts.sourcesContent;
      }
      if (this.previous().length) {
        return this.previous().some(function (i) {
          return i.withContent();
        });
      }
      return true;
    }
  }, {
    key: "clearAnnotation",
    value: function clearAnnotation() {
      if (this.mapOpts.annotation === false) return;
      if (this.root) {
        var node;
        for (var i = this.root.nodes.length - 1; i >= 0; i--) {
          node = this.root.nodes[i];
          if (node.type !== 'comment') continue;
          if (node.text.indexOf('# sourceMappingURL=') === 0) {
            this.root.removeChild(i);
          }
        }
      } else if (this.css) {
        this.css = this.css.replace(/(\n)?\/\*#[\S\s]*?\*\/$/gm, '');
      }
    }
  }, {
    key: "setSourcesContent",
    value: function setSourcesContent() {
      var _this2 = this;
      var already = {};
      if (this.root) {
        this.root.walk(function (node) {
          if (node.source) {
            var from = node.source.input.from;
            if (from && !already[from]) {
              already[from] = true;
              var fromUrl = _this2.usesFileUrls ? _this2.toFileUrl(from) : _this2.toUrl(_this2.path(from));
              _this2.map.setSourceContent(fromUrl, node.source.input.css);
            }
          }
        });
      } else if (this.css) {
        var from = this.opts.from ? this.toUrl(this.path(this.opts.from)) : '<no source>';
        this.map.setSourceContent(from, this.css);
      }
    }
  }, {
    key: "applyPrevMaps",
    value: function applyPrevMaps() {
      var _iterator = _createForOfIteratorHelper(this.previous()),
        _step;
      try {
        for (_iterator.s(); !(_step = _iterator.n()).done;) {
          var prev = _step.value;
          var from = this.toUrl(this.path(prev.file));
          var root = prev.root || dirname(prev.file);
          var map = void 0;
          if (this.mapOpts.sourcesContent === false) {
            map = new SourceMapConsumer(prev.text);
            if (map.sourcesContent) {
              map.sourcesContent = map.sourcesContent.map(function () {
                return null;
              });
            }
          } else {
            map = prev.consumer();
          }
          this.map.applySourceMap(map, from, this.toUrl(this.path(root)));
        }
      } catch (err) {
        _iterator.e(err);
      } finally {
        _iterator.f();
      }
    }
  }, {
    key: "isAnnotation",
    value: function isAnnotation() {
      if (this.isInline()) {
        return true;
      }
      if (typeof this.mapOpts.annotation !== 'undefined') {
        return this.mapOpts.annotation;
      }
      if (this.previous().length) {
        return this.previous().some(function (i) {
          return i.annotation;
        });
      }
      return true;
    }
  }, {
    key: "toBase64",
    value: function toBase64(str) {
      if (Buffer) {
        return Buffer.from(str).toString('base64');
      } else {
        return window.btoa(unescape(encodeURIComponent(str)));
      }
    }
  }, {
    key: "addAnnotation",
    value: function addAnnotation() {
      var content;
      if (this.isInline()) {
        content = 'data:application/json;base64,' + this.toBase64(this.map.toString());
      } else if (typeof this.mapOpts.annotation === 'string') {
        content = this.mapOpts.annotation;
      } else if (typeof this.mapOpts.annotation === 'function') {
        content = this.mapOpts.annotation(this.opts.to, this.root);
      } else {
        content = this.outputFile() + '.map';
      }
      var eol = '\n';
      if (this.css.includes('\r\n')) eol = '\r\n';
      this.css += eol + '/*# sourceMappingURL=' + content + ' */';
    }
  }, {
    key: "outputFile",
    value: function outputFile() {
      if (this.opts.to) {
        return this.path(this.opts.to);
      } else if (this.opts.from) {
        return this.path(this.opts.from);
      } else {
        return 'to.css';
      }
    }
  }, {
    key: "generateMap",
    value: function generateMap() {
      if (this.root) {
        this.generateString();
      } else if (this.previous().length === 1) {
        var prev = this.previous()[0].consumer();
        prev.file = this.outputFile();
        this.map = SourceMapGenerator.fromSourceMap(prev);
      } else {
        this.map = new SourceMapGenerator({
          file: this.outputFile()
        });
        this.map.addMapping({
          source: this.opts.from ? this.toUrl(this.path(this.opts.from)) : '<no source>',
          generated: {
            line: 1,
            column: 0
          },
          original: {
            line: 1,
            column: 0
          }
        });
      }
      if (this.isSourcesContent()) this.setSourcesContent();
      if (this.root && this.previous().length > 0) this.applyPrevMaps();
      if (this.isAnnotation()) this.addAnnotation();
      if (this.isInline()) {
        return [this.css];
      } else {
        return [this.css, this.map];
      }
    }
  }, {
    key: "path",
    value: function path(file) {
      if (file.indexOf('<') === 0) return file;
      if (/^\w+:\/\//.test(file)) return file;
      if (this.mapOpts.absolute) return file;
      var from = this.opts.to ? dirname(this.opts.to) : '.';
      if (typeof this.mapOpts.annotation === 'string') {
        from = dirname(resolve(from, this.mapOpts.annotation));
      }
      file = relative(from, file);
      return file;
    }
  }, {
    key: "toUrl",
    value: function toUrl(path) {
      if (sep === '\\') {
        path = path.replace(/\\/g, '/');
      }
      return encodeURI(path).replace(/[#?]/g, encodeURIComponent);
    }
  }, {
    key: "toFileUrl",
    value: function toFileUrl(path) {
      if (pathToFileURL) {
        return pathToFileURL(path).toString();
      } else {
        throw new Error('`map.absolute` option is not available in this PostCSS build');
      }
    }
  }, {
    key: "sourcePath",
    value: function sourcePath(node) {
      if (this.mapOpts.from) {
        return this.toUrl(this.mapOpts.from);
      } else if (this.usesFileUrls) {
        return this.toFileUrl(node.source.input.from);
      } else {
        return this.toUrl(this.path(node.source.input.from));
      }
    }
  }, {
    key: "generateString",
    value: function generateString() {
      var _this3 = this;
      this.css = '';
      this.map = new SourceMapGenerator({
        file: this.outputFile()
      });
      var line = 1;
      var column = 1;
      var noSource = '<no source>';
      var mapping = {
        source: '',
        generated: {
          line: 0,
          column: 0
        },
        original: {
          line: 0,
          column: 0
        }
      };
      var lines, last;
      this.stringify(this.root, function (str, node, type) {
        _this3.css += str;
        if (node && type !== 'end') {
          mapping.generated.line = line;
          mapping.generated.column = column - 1;
          if (node.source && node.source.start) {
            mapping.source = _this3.sourcePath(node);
            mapping.original.line = node.source.start.line;
            mapping.original.column = node.source.start.column - 1;
            _this3.map.addMapping(mapping);
          } else {
            mapping.source = noSource;
            mapping.original.line = 1;
            mapping.original.column = 0;
            _this3.map.addMapping(mapping);
          }
        }
        lines = str.match(/\n/g);
        if (lines) {
          line += lines.length;
          last = str.lastIndexOf('\n');
          column = str.length - last;
        } else {
          column += str.length;
        }
        if (node && type !== 'start') {
          var p = node.parent || {
            raws: {}
          };
          if (node.type !== 'decl' || node !== p.last || p.raws.semicolon) {
            if (node.source && node.source.end) {
              mapping.source = _this3.sourcePath(node);
              mapping.original.line = node.source.end.line;
              mapping.original.column = node.source.end.column - 1;
              mapping.generated.line = line;
              mapping.generated.column = column - 2;
              _this3.map.addMapping(mapping);
            } else {
              mapping.source = noSource;
              mapping.original.line = 1;
              mapping.original.column = 0;
              mapping.generated.line = line;
              mapping.generated.column = column - 1;
              _this3.map.addMapping(mapping);
            }
          }
        }
      });
    }
  }, {
    key: "generate",
    value: function generate() {
      this.clearAnnotation();
      if (pathAvailable && sourceMapAvailable && this.isMap()) {
        return this.generateMap();
      } else {
        var result = '';
        this.stringify(this.root, function (i) {
          result += i;
        });
        return [result];
      }
    }
  }]);
  return MapGenerator;
}();
module.exports = MapGenerator;

/***/ }),

/***/ 7686:
/***/ ((module, __unused_webpack_exports, __webpack_require__) => {

"use strict";


function _slicedToArray(arr, i) { return _arrayWithHoles(arr) || _iterableToArrayLimit(arr, i) || _unsupportedIterableToArray(arr, i) || _nonIterableRest(); }
function _nonIterableRest() { throw new TypeError("Invalid attempt to destructure non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method."); }
function _unsupportedIterableToArray(o, minLen) { if (!o) return; if (typeof o === "string") return _arrayLikeToArray(o, minLen); var n = Object.prototype.toString.call(o).slice(8, -1); if (n === "Object" && o.constructor) n = o.constructor.name; if (n === "Map" || n === "Set") return Array.from(o); if (n === "Arguments" || /^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(n)) return _arrayLikeToArray(o, minLen); }
function _arrayLikeToArray(arr, len) { if (len == null || len > arr.length) len = arr.length; for (var i = 0, arr2 = new Array(len); i < len; i++) { arr2[i] = arr[i]; } return arr2; }
function _iterableToArrayLimit(arr, i) { var _i = arr == null ? null : typeof Symbol !== "undefined" && arr[Symbol.iterator] || arr["@@iterator"]; if (_i == null) return; var _arr = []; var _n = true; var _d = false; var _s, _e; try { for (_i = _i.call(arr); !(_n = (_s = _i.next()).done); _n = true) { _arr.push(_s.value); if (i && _arr.length === i) break; } } catch (err) { _d = true; _e = err; } finally { try { if (!_n && _i["return"] != null) _i["return"](); } finally { if (_d) throw _e; } } return _arr; }
function _arrayWithHoles(arr) { if (Array.isArray(arr)) return arr; }
function _classCallCheck(instance, Constructor) { if (!(instance instanceof Constructor)) { throw new TypeError("Cannot call a class as a function"); } }
function _defineProperties(target, props) { for (var i = 0; i < props.length; i++) { var descriptor = props[i]; descriptor.enumerable = descriptor.enumerable || false; descriptor.configurable = true; if ("value" in descriptor) descriptor.writable = true; Object.defineProperty(target, descriptor.key, descriptor); } }
function _createClass(Constructor, protoProps, staticProps) { if (protoProps) _defineProperties(Constructor.prototype, protoProps); if (staticProps) _defineProperties(Constructor, staticProps); Object.defineProperty(Constructor, "prototype", { writable: false }); return Constructor; }
var MapGenerator = __webpack_require__(8991);
var stringify = __webpack_require__(6157);
var warnOnce = __webpack_require__(6574);
var parse = __webpack_require__(7057);
var Result = __webpack_require__(6865);
var NoWorkResult = /*#__PURE__*/function (_Symbol$toStringTag) {
  function NoWorkResult(processor, css, opts) {
    _classCallCheck(this, NoWorkResult);
    css = css.toString();
    this.stringified = false;
    this._processor = processor;
    this._css = css;
    this._opts = opts;
    this._map = undefined;
    var root;
    var str = stringify;
    this.result = new Result(this._processor, root, this._opts);
    this.result.css = css;
    var self = this;
    Object.defineProperty(this.result, 'root', {
      get: function get() {
        return self.root;
      }
    });
    var map = new MapGenerator(str, root, this._opts, css);
    if (map.isMap()) {
      var _map$generate = map.generate(),
        _map$generate2 = _slicedToArray(_map$generate, 2),
        generatedCSS = _map$generate2[0],
        generatedMap = _map$generate2[1];
      if (generatedCSS) {
        this.result.css = generatedCSS;
      }
      if (generatedMap) {
        this.result.map = generatedMap;
      }
    }
  }
  _createClass(NoWorkResult, [{
    key: _Symbol$toStringTag,
    get: function get() {
      return 'NoWorkResult';
    }
  }, {
    key: "processor",
    get: function get() {
      return this.result.processor;
    }
  }, {
    key: "opts",
    get: function get() {
      return this.result.opts;
    }
  }, {
    key: "css",
    get: function get() {
      return this.result.css;
    }
  }, {
    key: "content",
    get: function get() {
      return this.result.css;
    }
  }, {
    key: "map",
    get: function get() {
      return this.result.map;
    }
  }, {
    key: "root",
    get: function get() {
      if (this._root) {
        return this._root;
      }
      var root;
      var parser = parse;
      try {
        root = parser(this._css, this._opts);
      } catch (error) {
        this.error = error;
      }
      if (this.error) {
        throw this.error;
      } else {
        this._root = root;
        return root;
      }
    }
  }, {
    key: "messages",
    get: function get() {
      return [];
    }
  }, {
    key: "warnings",
    value: function warnings() {
      return [];
    }
  }, {
    key: "toString",
    value: function toString() {
      return this._css;
    }
  }, {
    key: "then",
    value: function then(onFulfilled, onRejected) {
      if (false) {}
      return this.async().then(onFulfilled, onRejected);
    }
  }, {
    key: "catch",
    value: function _catch(onRejected) {
      return this.async()["catch"](onRejected);
    }
  }, {
    key: "finally",
    value: function _finally(onFinally) {
      return this.async().then(onFinally, onFinally);
    }
  }, {
    key: "async",
    value: function async() {
      if (this.error) return Promise.reject(this.error);
      return Promise.resolve(this.result);
    }
  }, {
    key: "sync",
    value: function sync() {
      if (this.error) throw this.error;
      return this.result;
    }
  }]);
  return NoWorkResult;
}(Symbol.toStringTag);
module.exports = NoWorkResult;
NoWorkResult["default"] = NoWorkResult;

/***/ }),

/***/ 4343:
/***/ ((module, __unused_webpack_exports, __webpack_require__) => {

"use strict";


function _toConsumableArray(arr) { return _arrayWithoutHoles(arr) || _iterableToArray(arr) || _unsupportedIterableToArray(arr) || _nonIterableSpread(); }
function _nonIterableSpread() { throw new TypeError("Invalid attempt to spread non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method."); }
function _iterableToArray(iter) { if (typeof Symbol !== "undefined" && iter[Symbol.iterator] != null || iter["@@iterator"] != null) return Array.from(iter); }
function _arrayWithoutHoles(arr) { if (Array.isArray(arr)) return _arrayLikeToArray(arr); }
function _createForOfIteratorHelper(o, allowArrayLike) { var it = typeof Symbol !== "undefined" && o[Symbol.iterator] || o["@@iterator"]; if (!it) { if (Array.isArray(o) || (it = _unsupportedIterableToArray(o)) || allowArrayLike && o && typeof o.length === "number") { if (it) o = it; var i = 0; var F = function F() {}; return { s: F, n: function n() { if (i >= o.length) return { done: true }; return { done: false, value: o[i++] }; }, e: function e(_e) { throw _e; }, f: F }; } throw new TypeError("Invalid attempt to iterate non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method."); } var normalCompletion = true, didErr = false, err; return { s: function s() { it = it.call(o); }, n: function n() { var step = it.next(); normalCompletion = step.done; return step; }, e: function e(_e2) { didErr = true; err = _e2; }, f: function f() { try { if (!normalCompletion && it["return"] != null) it["return"](); } finally { if (didErr) throw err; } } }; }
function _unsupportedIterableToArray(o, minLen) { if (!o) return; if (typeof o === "string") return _arrayLikeToArray(o, minLen); var n = Object.prototype.toString.call(o).slice(8, -1); if (n === "Object" && o.constructor) n = o.constructor.name; if (n === "Map" || n === "Set") return Array.from(o); if (n === "Arguments" || /^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(n)) return _arrayLikeToArray(o, minLen); }
function _arrayLikeToArray(arr, len) { if (len == null || len > arr.length) len = arr.length; for (var i = 0, arr2 = new Array(len); i < len; i++) { arr2[i] = arr[i]; } return arr2; }
function _classCallCheck(instance, Constructor) { if (!(instance instanceof Constructor)) { throw new TypeError("Cannot call a class as a function"); } }
function _defineProperties(target, props) { for (var i = 0; i < props.length; i++) { var descriptor = props[i]; descriptor.enumerable = descriptor.enumerable || false; descriptor.configurable = true; if ("value" in descriptor) descriptor.writable = true; Object.defineProperty(target, descriptor.key, descriptor); } }
function _createClass(Constructor, protoProps, staticProps) { if (protoProps) _defineProperties(Constructor.prototype, protoProps); if (staticProps) _defineProperties(Constructor, staticProps); Object.defineProperty(Constructor, "prototype", { writable: false }); return Constructor; }
function _typeof(obj) { "@babel/helpers - typeof"; return _typeof = "function" == typeof Symbol && "symbol" == typeof Symbol.iterator ? function (obj) { return typeof obj; } : function (obj) { return obj && "function" == typeof Symbol && obj.constructor === Symbol && obj !== Symbol.prototype ? "symbol" : typeof obj; }, _typeof(obj); }
var _require = __webpack_require__(5506),
  isClean = _require.isClean,
  my = _require.my;
var CssSyntaxError = __webpack_require__(1667);
var Stringifier = __webpack_require__(5701);
var stringify = __webpack_require__(6157);
function cloneNode(obj, parent) {
  var cloned = new obj.constructor();
  for (var i in obj) {
    if (!Object.prototype.hasOwnProperty.call(obj, i)) {
      /* c8 ignore next 2 */
      continue;
    }
    if (i === 'proxyCache') continue;
    var value = obj[i];
    var type = _typeof(value);
    if (i === 'parent' && type === 'object') {
      if (parent) cloned[i] = parent;
    } else if (i === 'source') {
      cloned[i] = value;
    } else if (Array.isArray(value)) {
      cloned[i] = value.map(function (j) {
        return cloneNode(j, cloned);
      });
    } else {
      if (type === 'object' && value !== null) value = cloneNode(value);
      cloned[i] = value;
    }
  }
  return cloned;
}
var Node = /*#__PURE__*/function () {
  function Node() {
    var defaults = arguments.length > 0 && arguments[0] !== undefined ? arguments[0] : {};
    _classCallCheck(this, Node);
    this.raws = {};
    this[isClean] = false;
    this[my] = true;
    for (var name in defaults) {
      if (name === 'nodes') {
        this.nodes = [];
        var _iterator = _createForOfIteratorHelper(defaults[name]),
          _step;
        try {
          for (_iterator.s(); !(_step = _iterator.n()).done;) {
            var node = _step.value;
            if (typeof node.clone === 'function') {
              this.append(node.clone());
            } else {
              this.append(node);
            }
          }
        } catch (err) {
          _iterator.e(err);
        } finally {
          _iterator.f();
        }
      } else {
        this[name] = defaults[name];
      }
    }
  }
  _createClass(Node, [{
    key: "error",
    value: function error(message) {
      var opts = arguments.length > 1 && arguments[1] !== undefined ? arguments[1] : {};
      if (this.source) {
        var _this$rangeBy = this.rangeBy(opts),
          start = _this$rangeBy.start,
          end = _this$rangeBy.end;
        return this.source.input.error(message, {
          line: start.line,
          column: start.column
        }, {
          line: end.line,
          column: end.column
        }, opts);
      }
      return new CssSyntaxError(message);
    }
  }, {
    key: "warn",
    value: function warn(result, text, opts) {
      var data = {
        node: this
      };
      for (var i in opts) {
        data[i] = opts[i];
      }
      return result.warn(text, data);
    }
  }, {
    key: "remove",
    value: function remove() {
      if (this.parent) {
        this.parent.removeChild(this);
      }
      this.parent = undefined;
      return this;
    }
  }, {
    key: "toString",
    value: function toString() {
      var stringifier = arguments.length > 0 && arguments[0] !== undefined ? arguments[0] : stringify;
      if (stringifier.stringify) stringifier = stringifier.stringify;
      var result = '';
      stringifier(this, function (i) {
        result += i;
      });
      return result;
    }
  }, {
    key: "assign",
    value: function assign() {
      var overrides = arguments.length > 0 && arguments[0] !== undefined ? arguments[0] : {};
      for (var name in overrides) {
        this[name] = overrides[name];
      }
      return this;
    }
  }, {
    key: "clone",
    value: function clone() {
      var overrides = arguments.length > 0 && arguments[0] !== undefined ? arguments[0] : {};
      var cloned = cloneNode(this);
      for (var name in overrides) {
        cloned[name] = overrides[name];
      }
      return cloned;
    }
  }, {
    key: "cloneBefore",
    value: function cloneBefore() {
      var overrides = arguments.length > 0 && arguments[0] !== undefined ? arguments[0] : {};
      var cloned = this.clone(overrides);
      this.parent.insertBefore(this, cloned);
      return cloned;
    }
  }, {
    key: "cloneAfter",
    value: function cloneAfter() {
      var overrides = arguments.length > 0 && arguments[0] !== undefined ? arguments[0] : {};
      var cloned = this.clone(overrides);
      this.parent.insertAfter(this, cloned);
      return cloned;
    }
  }, {
    key: "replaceWith",
    value: function replaceWith() {
      if (this.parent) {
        var bookmark = this;
        var foundSelf = false;
        for (var _len = arguments.length, nodes = new Array(_len), _key = 0; _key < _len; _key++) {
          nodes[_key] = arguments[_key];
        }
        for (var _i = 0, _nodes = nodes; _i < _nodes.length; _i++) {
          var node = _nodes[_i];
          if (node === this) {
            foundSelf = true;
          } else if (foundSelf) {
            this.parent.insertAfter(bookmark, node);
            bookmark = node;
          } else {
            this.parent.insertBefore(bookmark, node);
          }
        }
        if (!foundSelf) {
          this.remove();
        }
      }
      return this;
    }
  }, {
    key: "next",
    value: function next() {
      if (!this.parent) return undefined;
      var index = this.parent.index(this);
      return this.parent.nodes[index + 1];
    }
  }, {
    key: "prev",
    value: function prev() {
      if (!this.parent) return undefined;
      var index = this.parent.index(this);
      return this.parent.nodes[index - 1];
    }
  }, {
    key: "before",
    value: function before(add) {
      this.parent.insertBefore(this, add);
      return this;
    }
  }, {
    key: "after",
    value: function after(add) {
      this.parent.insertAfter(this, add);
      return this;
    }
  }, {
    key: "root",
    value: function root() {
      var result = this;
      while (result.parent && result.parent.type !== 'document') {
        result = result.parent;
      }
      return result;
    }
  }, {
    key: "raw",
    value: function raw(prop, defaultType) {
      var str = new Stringifier();
      return str.raw(this, prop, defaultType);
    }
  }, {
    key: "cleanRaws",
    value: function cleanRaws(keepBetween) {
      delete this.raws.before;
      delete this.raws.after;
      if (!keepBetween) delete this.raws.between;
    }
  }, {
    key: "toJSON",
    value: function toJSON(_, inputs) {
      var fixed = {};
      var emitInputs = inputs == null;
      inputs = inputs || new Map();
      var inputsNextIndex = 0;
      for (var name in this) {
        if (!Object.prototype.hasOwnProperty.call(this, name)) {
          /* c8 ignore next 2 */
          continue;
        }
        if (name === 'parent' || name === 'proxyCache') continue;
        var value = this[name];
        if (Array.isArray(value)) {
          fixed[name] = value.map(function (i) {
            if (_typeof(i) === 'object' && i.toJSON) {
              return i.toJSON(null, inputs);
            } else {
              return i;
            }
          });
        } else if (_typeof(value) === 'object' && value.toJSON) {
          fixed[name] = value.toJSON(null, inputs);
        } else if (name === 'source') {
          var inputId = inputs.get(value.input);
          if (inputId == null) {
            inputId = inputsNextIndex;
            inputs.set(value.input, inputsNextIndex);
            inputsNextIndex++;
          }
          fixed[name] = {
            inputId: inputId,
            start: value.start,
            end: value.end
          };
        } else {
          fixed[name] = value;
        }
      }
      if (emitInputs) {
        fixed.inputs = _toConsumableArray(inputs.keys()).map(function (input) {
          return input.toJSON();
        });
      }
      return fixed;
    }
  }, {
    key: "positionInside",
    value: function positionInside(index) {
      var string = this.toString();
      var column = this.source.start.column;
      var line = this.source.start.line;
      for (var i = 0; i < index; i++) {
        if (string[i] === '\n') {
          column = 1;
          line += 1;
        } else {
          column += 1;
        }
      }
      return {
        line: line,
        column: column
      };
    }
  }, {
    key: "positionBy",
    value: function positionBy(opts) {
      var pos = this.source.start;
      if (opts.index) {
        pos = this.positionInside(opts.index);
      } else if (opts.word) {
        var index = this.toString().indexOf(opts.word);
        if (index !== -1) pos = this.positionInside(index);
      }
      return pos;
    }
  }, {
    key: "rangeBy",
    value: function rangeBy(opts) {
      var start = {
        line: this.source.start.line,
        column: this.source.start.column
      };
      var end = this.source.end ? {
        line: this.source.end.line,
        column: this.source.end.column + 1
      } : {
        line: start.line,
        column: start.column + 1
      };
      if (opts.word) {
        var index = this.toString().indexOf(opts.word);
        if (index !== -1) {
          start = this.positionInside(index);
          end = this.positionInside(index + opts.word.length);
        }
      } else {
        if (opts.start) {
          start = {
            line: opts.start.line,
            column: opts.start.column
          };
        } else if (opts.index) {
          start = this.positionInside(opts.index);
        }
        if (opts.end) {
          end = {
            line: opts.end.line,
            column: opts.end.column
          };
        } else if (opts.endIndex) {
          end = this.positionInside(opts.endIndex);
        } else if (opts.index) {
          end = this.positionInside(opts.index + 1);
        }
      }
      if (end.line < start.line || end.line === start.line && end.column <= start.column) {
        end = {
          line: start.line,
          column: start.column + 1
        };
      }
      return {
        start: start,
        end: end
      };
    }
  }, {
    key: "getProxyProcessor",
    value: function getProxyProcessor() {
      return {
        set: function set(node, prop, value) {
          if (node[prop] === value) return true;
          node[prop] = value;
          if (prop === 'prop' || prop === 'value' || prop === 'name' || prop === 'params' || prop === 'important' || /* c8 ignore next */
          prop === 'text') {
            node.markDirty();
          }
          return true;
        },
        get: function get(node, prop) {
          if (prop === 'proxyOf') {
            return node;
          } else if (prop === 'root') {
            return function () {
              return node.root().toProxy();
            };
          } else {
            return node[prop];
          }
        }
      };
    }
  }, {
    key: "toProxy",
    value: function toProxy() {
      if (!this.proxyCache) {
        this.proxyCache = new Proxy(this, this.getProxyProcessor());
      }
      return this.proxyCache;
    }
  }, {
    key: "addToError",
    value: function addToError(error) {
      error.postcssNode = this;
      if (error.stack && this.source && /\n\s{4}at /.test(error.stack)) {
        var s = this.source;
        error.stack = error.stack.replace(/\n\s{4}at /, "$&".concat(s.input.from, ":").concat(s.start.line, ":").concat(s.start.column, "$&"));
      }
      return error;
    }
  }, {
    key: "markDirty",
    value: function markDirty() {
      if (this[isClean]) {
        this[isClean] = false;
        var next = this;
        while (next = next.parent) {
          next[isClean] = false;
        }
      }
    }
  }, {
    key: "proxyOf",
    get: function get() {
      return this;
    }
  }]);
  return Node;
}();
module.exports = Node;
Node["default"] = Node;

/***/ }),

/***/ 7057:
/***/ ((module, __unused_webpack_exports, __webpack_require__) => {

"use strict";


var Container = __webpack_require__(1204);
var Parser = __webpack_require__(7116);
var Input = __webpack_require__(2993);
function parse(css, opts) {
  var input = new Input(css, opts);
  var parser = new Parser(input);
  try {
    parser.parse();
  } catch (e) {
    if (false) {}
    throw e;
  }
  return parser.root;
}
module.exports = parse;
parse["default"] = parse;
Container.registerParse(parse);

/***/ }),

/***/ 7116:
/***/ ((module, __unused_webpack_exports, __webpack_require__) => {

"use strict";


function _slicedToArray(arr, i) { return _arrayWithHoles(arr) || _iterableToArrayLimit(arr, i) || _unsupportedIterableToArray(arr, i) || _nonIterableRest(); }
function _nonIterableRest() { throw new TypeError("Invalid attempt to destructure non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method."); }
function _iterableToArrayLimit(arr, i) { var _i = arr == null ? null : typeof Symbol !== "undefined" && arr[Symbol.iterator] || arr["@@iterator"]; if (_i == null) return; var _arr = []; var _n = true; var _d = false; var _s, _e; try { for (_i = _i.call(arr); !(_n = (_s = _i.next()).done); _n = true) { _arr.push(_s.value); if (i && _arr.length === i) break; } } catch (err) { _d = true; _e = err; } finally { try { if (!_n && _i["return"] != null) _i["return"](); } finally { if (_d) throw _e; } } return _arr; }
function _arrayWithHoles(arr) { if (Array.isArray(arr)) return arr; }
function _createForOfIteratorHelper(o, allowArrayLike) { var it = typeof Symbol !== "undefined" && o[Symbol.iterator] || o["@@iterator"]; if (!it) { if (Array.isArray(o) || (it = _unsupportedIterableToArray(o)) || allowArrayLike && o && typeof o.length === "number") { if (it) o = it; var i = 0; var F = function F() {}; return { s: F, n: function n() { if (i >= o.length) return { done: true }; return { done: false, value: o[i++] }; }, e: function e(_e2) { throw _e2; }, f: F }; } throw new TypeError("Invalid attempt to iterate non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method."); } var normalCompletion = true, didErr = false, err; return { s: function s() { it = it.call(o); }, n: function n() { var step = it.next(); normalCompletion = step.done; return step; }, e: function e(_e3) { didErr = true; err = _e3; }, f: function f() { try { if (!normalCompletion && it["return"] != null) it["return"](); } finally { if (didErr) throw err; } } }; }
function _unsupportedIterableToArray(o, minLen) { if (!o) return; if (typeof o === "string") return _arrayLikeToArray(o, minLen); var n = Object.prototype.toString.call(o).slice(8, -1); if (n === "Object" && o.constructor) n = o.constructor.name; if (n === "Map" || n === "Set") return Array.from(o); if (n === "Arguments" || /^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(n)) return _arrayLikeToArray(o, minLen); }
function _arrayLikeToArray(arr, len) { if (len == null || len > arr.length) len = arr.length; for (var i = 0, arr2 = new Array(len); i < len; i++) { arr2[i] = arr[i]; } return arr2; }
function _classCallCheck(instance, Constructor) { if (!(instance instanceof Constructor)) { throw new TypeError("Cannot call a class as a function"); } }
function _defineProperties(target, props) { for (var i = 0; i < props.length; i++) { var descriptor = props[i]; descriptor.enumerable = descriptor.enumerable || false; descriptor.configurable = true; if ("value" in descriptor) descriptor.writable = true; Object.defineProperty(target, descriptor.key, descriptor); } }
function _createClass(Constructor, protoProps, staticProps) { if (protoProps) _defineProperties(Constructor.prototype, protoProps); if (staticProps) _defineProperties(Constructor, staticProps); Object.defineProperty(Constructor, "prototype", { writable: false }); return Constructor; }
var Declaration = __webpack_require__(6417);
var tokenizer = __webpack_require__(1157);
var Comment = __webpack_require__(3102);
var AtRule = __webpack_require__(8940);
var Root = __webpack_require__(7563);
var Rule = __webpack_require__(6621);
var SAFE_COMMENT_NEIGHBOR = {
  empty: true,
  space: true
};
function findLastWithPosition(tokens) {
  for (var i = tokens.length - 1; i >= 0; i--) {
    var token = tokens[i];
    var pos = token[3] || token[2];
    if (pos) return pos;
  }
}
var Parser = /*#__PURE__*/function () {
  function Parser(input) {
    _classCallCheck(this, Parser);
    this.input = input;
    this.root = new Root();
    this.current = this.root;
    this.spaces = '';
    this.semicolon = false;
    this.customProperty = false;
    this.createTokenizer();
    this.root.source = {
      input: input,
      start: {
        offset: 0,
        line: 1,
        column: 1
      }
    };
  }
  _createClass(Parser, [{
    key: "createTokenizer",
    value: function createTokenizer() {
      this.tokenizer = tokenizer(this.input);
    }
  }, {
    key: "parse",
    value: function parse() {
      var token;
      while (!this.tokenizer.endOfFile()) {
        token = this.tokenizer.nextToken();
        switch (token[0]) {
          case 'space':
            this.spaces += token[1];
            break;
          case ';':
            this.freeSemicolon(token);
            break;
          case '}':
            this.end(token);
            break;
          case 'comment':
            this.comment(token);
            break;
          case 'at-word':
            this.atrule(token);
            break;
          case '{':
            this.emptyRule(token);
            break;
          default:
            this.other(token);
            break;
        }
      }
      this.endFile();
    }
  }, {
    key: "comment",
    value: function comment(token) {
      var node = new Comment();
      this.init(node, token[2]);
      node.source.end = this.getPosition(token[3] || token[2]);
      var text = token[1].slice(2, -2);
      if (/^\s*$/.test(text)) {
        node.text = '';
        node.raws.left = text;
        node.raws.right = '';
      } else {
        var match = text.match(/^(\s*)([^]*\S)(\s*)$/);
        node.text = match[2];
        node.raws.left = match[1];
        node.raws.right = match[3];
      }
    }
  }, {
    key: "emptyRule",
    value: function emptyRule(token) {
      var node = new Rule();
      this.init(node, token[2]);
      node.selector = '';
      node.raws.between = '';
      this.current = node;
    }
  }, {
    key: "other",
    value: function other(start) {
      var end = false;
      var type = null;
      var colon = false;
      var bracket = null;
      var brackets = [];
      var customProperty = start[1].startsWith('--');
      var tokens = [];
      var token = start;
      while (token) {
        type = token[0];
        tokens.push(token);
        if (type === '(' || type === '[') {
          if (!bracket) bracket = token;
          brackets.push(type === '(' ? ')' : ']');
        } else if (customProperty && colon && type === '{') {
          if (!bracket) bracket = token;
          brackets.push('}');
        } else if (brackets.length === 0) {
          if (type === ';') {
            if (colon) {
              this.decl(tokens, customProperty);
              return;
            } else {
              break;
            }
          } else if (type === '{') {
            this.rule(tokens);
            return;
          } else if (type === '}') {
            this.tokenizer.back(tokens.pop());
            end = true;
            break;
          } else if (type === ':') {
            colon = true;
          }
        } else if (type === brackets[brackets.length - 1]) {
          brackets.pop();
          if (brackets.length === 0) bracket = null;
        }
        token = this.tokenizer.nextToken();
      }
      if (this.tokenizer.endOfFile()) end = true;
      if (brackets.length > 0) this.unclosedBracket(bracket);
      if (end && colon) {
        if (!customProperty) {
          while (tokens.length) {
            token = tokens[tokens.length - 1][0];
            if (token !== 'space' && token !== 'comment') break;
            this.tokenizer.back(tokens.pop());
          }
        }
        this.decl(tokens, customProperty);
      } else {
        this.unknownWord(tokens);
      }
    }
  }, {
    key: "rule",
    value: function rule(tokens) {
      tokens.pop();
      var node = new Rule();
      this.init(node, tokens[0][2]);
      node.raws.between = this.spacesAndCommentsFromEnd(tokens);
      this.raw(node, 'selector', tokens);
      this.current = node;
    }
  }, {
    key: "decl",
    value: function decl(tokens, customProperty) {
      var node = new Declaration();
      this.init(node, tokens[0][2]);
      var last = tokens[tokens.length - 1];
      if (last[0] === ';') {
        this.semicolon = true;
        tokens.pop();
      }
      node.source.end = this.getPosition(last[3] || last[2] || findLastWithPosition(tokens));
      while (tokens[0][0] !== 'word') {
        if (tokens.length === 1) this.unknownWord(tokens);
        node.raws.before += tokens.shift()[1];
      }
      node.source.start = this.getPosition(tokens[0][2]);
      node.prop = '';
      while (tokens.length) {
        var type = tokens[0][0];
        if (type === ':' || type === 'space' || type === 'comment') {
          break;
        }
        node.prop += tokens.shift()[1];
      }
      node.raws.between = '';
      var token;
      while (tokens.length) {
        token = tokens.shift();
        if (token[0] === ':') {
          node.raws.between += token[1];
          break;
        } else {
          if (token[0] === 'word' && /\w/.test(token[1])) {
            this.unknownWord([token]);
          }
          node.raws.between += token[1];
        }
      }
      if (node.prop[0] === '_' || node.prop[0] === '*') {
        node.raws.before += node.prop[0];
        node.prop = node.prop.slice(1);
      }
      var firstSpaces = [];
      var next;
      while (tokens.length) {
        next = tokens[0][0];
        if (next !== 'space' && next !== 'comment') break;
        firstSpaces.push(tokens.shift());
      }
      this.precheckMissedSemicolon(tokens);
      for (var i = tokens.length - 1; i >= 0; i--) {
        token = tokens[i];
        if (token[1].toLowerCase() === '!important') {
          node.important = true;
          var string = this.stringFrom(tokens, i);
          string = this.spacesFromEnd(tokens) + string;
          if (string !== ' !important') node.raws.important = string;
          break;
        } else if (token[1].toLowerCase() === 'important') {
          var cache = tokens.slice(0);
          var str = '';
          for (var j = i; j > 0; j--) {
            var _type = cache[j][0];
            if (str.trim().indexOf('!') === 0 && _type !== 'space') {
              break;
            }
            str = cache.pop()[1] + str;
          }
          if (str.trim().indexOf('!') === 0) {
            node.important = true;
            node.raws.important = str;
            tokens = cache;
          }
        }
        if (token[0] !== 'space' && token[0] !== 'comment') {
          break;
        }
      }
      var hasWord = tokens.some(function (i) {
        return i[0] !== 'space' && i[0] !== 'comment';
      });
      if (hasWord) {
        node.raws.between += firstSpaces.map(function (i) {
          return i[1];
        }).join('');
        firstSpaces = [];
      }
      this.raw(node, 'value', firstSpaces.concat(tokens), customProperty);
      if (node.value.includes(':') && !customProperty) {
        this.checkMissedSemicolon(tokens);
      }
    }
  }, {
    key: "atrule",
    value: function atrule(token) {
      var node = new AtRule();
      node.name = token[1].slice(1);
      if (node.name === '') {
        this.unnamedAtrule(node, token);
      }
      this.init(node, token[2]);
      var type;
      var prev;
      var shift;
      var last = false;
      var open = false;
      var params = [];
      var brackets = [];
      while (!this.tokenizer.endOfFile()) {
        token = this.tokenizer.nextToken();
        type = token[0];
        if (type === '(' || type === '[') {
          brackets.push(type === '(' ? ')' : ']');
        } else if (type === '{' && brackets.length > 0) {
          brackets.push('}');
        } else if (type === brackets[brackets.length - 1]) {
          brackets.pop();
        }
        if (brackets.length === 0) {
          if (type === ';') {
            node.source.end = this.getPosition(token[2]);
            this.semicolon = true;
            break;
          } else if (type === '{') {
            open = true;
            break;
          } else if (type === '}') {
            if (params.length > 0) {
              shift = params.length - 1;
              prev = params[shift];
              while (prev && prev[0] === 'space') {
                prev = params[--shift];
              }
              if (prev) {
                node.source.end = this.getPosition(prev[3] || prev[2]);
              }
            }
            this.end(token);
            break;
          } else {
            params.push(token);
          }
        } else {
          params.push(token);
        }
        if (this.tokenizer.endOfFile()) {
          last = true;
          break;
        }
      }
      node.raws.between = this.spacesAndCommentsFromEnd(params);
      if (params.length) {
        node.raws.afterName = this.spacesAndCommentsFromStart(params);
        this.raw(node, 'params', params);
        if (last) {
          token = params[params.length - 1];
          node.source.end = this.getPosition(token[3] || token[2]);
          this.spaces = node.raws.between;
          node.raws.between = '';
        }
      } else {
        node.raws.afterName = '';
        node.params = '';
      }
      if (open) {
        node.nodes = [];
        this.current = node;
      }
    }
  }, {
    key: "end",
    value: function end(token) {
      if (this.current.nodes && this.current.nodes.length) {
        this.current.raws.semicolon = this.semicolon;
      }
      this.semicolon = false;
      this.current.raws.after = (this.current.raws.after || '') + this.spaces;
      this.spaces = '';
      if (this.current.parent) {
        this.current.source.end = this.getPosition(token[2]);
        this.current = this.current.parent;
      } else {
        this.unexpectedClose(token);
      }
    }
  }, {
    key: "endFile",
    value: function endFile() {
      if (this.current.parent) this.unclosedBlock();
      if (this.current.nodes && this.current.nodes.length) {
        this.current.raws.semicolon = this.semicolon;
      }
      this.current.raws.after = (this.current.raws.after || '') + this.spaces;
    }
  }, {
    key: "freeSemicolon",
    value: function freeSemicolon(token) {
      this.spaces += token[1];
      if (this.current.nodes) {
        var prev = this.current.nodes[this.current.nodes.length - 1];
        if (prev && prev.type === 'rule' && !prev.raws.ownSemicolon) {
          prev.raws.ownSemicolon = this.spaces;
          this.spaces = '';
        }
      }
    }

    // Helpers
  }, {
    key: "getPosition",
    value: function getPosition(offset) {
      var pos = this.input.fromOffset(offset);
      return {
        offset: offset,
        line: pos.line,
        column: pos.col
      };
    }
  }, {
    key: "init",
    value: function init(node, offset) {
      this.current.push(node);
      node.source = {
        start: this.getPosition(offset),
        input: this.input
      };
      node.raws.before = this.spaces;
      this.spaces = '';
      if (node.type !== 'comment') this.semicolon = false;
    }
  }, {
    key: "raw",
    value: function raw(node, prop, tokens, customProperty) {
      var token, type;
      var length = tokens.length;
      var value = '';
      var clean = true;
      var next, prev;
      for (var i = 0; i < length; i += 1) {
        token = tokens[i];
        type = token[0];
        if (type === 'space' && i === length - 1 && !customProperty) {
          clean = false;
        } else if (type === 'comment') {
          prev = tokens[i - 1] ? tokens[i - 1][0] : 'empty';
          next = tokens[i + 1] ? tokens[i + 1][0] : 'empty';
          if (!SAFE_COMMENT_NEIGHBOR[prev] && !SAFE_COMMENT_NEIGHBOR[next]) {
            if (value.slice(-1) === ',') {
              clean = false;
            } else {
              value += token[1];
            }
          } else {
            clean = false;
          }
        } else {
          value += token[1];
        }
      }
      if (!clean) {
        var raw = tokens.reduce(function (all, i) {
          return all + i[1];
        }, '');
        node.raws[prop] = {
          value: value,
          raw: raw
        };
      }
      node[prop] = value;
    }
  }, {
    key: "spacesAndCommentsFromEnd",
    value: function spacesAndCommentsFromEnd(tokens) {
      var lastTokenType;
      var spaces = '';
      while (tokens.length) {
        lastTokenType = tokens[tokens.length - 1][0];
        if (lastTokenType !== 'space' && lastTokenType !== 'comment') break;
        spaces = tokens.pop()[1] + spaces;
      }
      return spaces;
    }
  }, {
    key: "spacesAndCommentsFromStart",
    value: function spacesAndCommentsFromStart(tokens) {
      var next;
      var spaces = '';
      while (tokens.length) {
        next = tokens[0][0];
        if (next !== 'space' && next !== 'comment') break;
        spaces += tokens.shift()[1];
      }
      return spaces;
    }
  }, {
    key: "spacesFromEnd",
    value: function spacesFromEnd(tokens) {
      var lastTokenType;
      var spaces = '';
      while (tokens.length) {
        lastTokenType = tokens[tokens.length - 1][0];
        if (lastTokenType !== 'space') break;
        spaces = tokens.pop()[1] + spaces;
      }
      return spaces;
    }
  }, {
    key: "stringFrom",
    value: function stringFrom(tokens, from) {
      var result = '';
      for (var i = from; i < tokens.length; i++) {
        result += tokens[i][1];
      }
      tokens.splice(from, tokens.length - from);
      return result;
    }
  }, {
    key: "colon",
    value: function colon(tokens) {
      var brackets = 0;
      var token, type, prev;
      var _iterator = _createForOfIteratorHelper(tokens.entries()),
        _step;
      try {
        for (_iterator.s(); !(_step = _iterator.n()).done;) {
          var _step$value = _slicedToArray(_step.value, 2),
            i = _step$value[0],
            element = _step$value[1];
          token = element;
          type = token[0];
          if (type === '(') {
            brackets += 1;
          }
          if (type === ')') {
            brackets -= 1;
          }
          if (brackets === 0 && type === ':') {
            if (!prev) {
              this.doubleColon(token);
            } else if (prev[0] === 'word' && prev[1] === 'progid') {
              continue;
            } else {
              return i;
            }
          }
          prev = token;
        }
      } catch (err) {
        _iterator.e(err);
      } finally {
        _iterator.f();
      }
      return false;
    }

    // Errors
  }, {
    key: "unclosedBracket",
    value: function unclosedBracket(bracket) {
      throw this.input.error('Unclosed bracket', {
        offset: bracket[2]
      }, {
        offset: bracket[2] + 1
      });
    }
  }, {
    key: "unknownWord",
    value: function unknownWord(tokens) {
      throw this.input.error('Unknown word', {
        offset: tokens[0][2]
      }, {
        offset: tokens[0][2] + tokens[0][1].length
      });
    }
  }, {
    key: "unexpectedClose",
    value: function unexpectedClose(token) {
      throw this.input.error('Unexpected }', {
        offset: token[2]
      }, {
        offset: token[2] + 1
      });
    }
  }, {
    key: "unclosedBlock",
    value: function unclosedBlock() {
      var pos = this.current.source.start;
      throw this.input.error('Unclosed block', pos.line, pos.column);
    }
  }, {
    key: "doubleColon",
    value: function doubleColon(token) {
      throw this.input.error('Double colon', {
        offset: token[2]
      }, {
        offset: token[2] + token[1].length
      });
    }
  }, {
    key: "unnamedAtrule",
    value: function unnamedAtrule(node, token) {
      throw this.input.error('At-rule without name', {
        offset: token[2]
      }, {
        offset: token[2] + token[1].length
      });
    }
  }, {
    key: "precheckMissedSemicolon",
    value: function precheckMissedSemicolon( /* tokens */
    ) {
      // Hook for Safe Parser
    }
  }, {
    key: "checkMissedSemicolon",
    value: function checkMissedSemicolon(tokens) {
      var colon = this.colon(tokens);
      if (colon === false) return;
      var founded = 0;
      var token;
      for (var j = colon - 1; j >= 0; j--) {
        token = tokens[j];
        if (token[0] !== 'space') {
          founded += 1;
          if (founded === 2) break;
        }
      }
      // If the token is a word, e.g. `!important`, `red` or any other valid property's value.
      // Then we need to return the colon after that word token. [3] is the "end" colon of that word.
      // And because we need it after that one we do +1 to get the next one.
      throw this.input.error('Missed semicolon', token[0] === 'word' ? token[3] + 1 : token[2]);
    }
  }]);
  return Parser;
}();
module.exports = Parser;

/***/ }),

/***/ 7866:
/***/ ((module, __unused_webpack_exports, __webpack_require__) => {

"use strict";


var CssSyntaxError = __webpack_require__(1667);
var Declaration = __webpack_require__(6417);
var LazyResult = __webpack_require__(6992);
var Container = __webpack_require__(1204);
var Processor = __webpack_require__(9429);
var stringify = __webpack_require__(6157);
var fromJSON = __webpack_require__(9295);
var Document = __webpack_require__(7083);
var Warning = __webpack_require__(1662);
var Comment = __webpack_require__(3102);
var AtRule = __webpack_require__(8940);
var Result = __webpack_require__(6865);
var Input = __webpack_require__(2993);
var parse = __webpack_require__(7057);
var list = __webpack_require__(6136);
var Rule = __webpack_require__(6621);
var Root = __webpack_require__(7563);
var Node = __webpack_require__(4343);
function postcss() {
  for (var _len = arguments.length, plugins = new Array(_len), _key = 0; _key < _len; _key++) {
    plugins[_key] = arguments[_key];
  }
  if (plugins.length === 1 && Array.isArray(plugins[0])) {
    plugins = plugins[0];
  }
  return new Processor(plugins);
}
postcss.plugin = function plugin(name, initializer) {
  var warningPrinted = false;
  function creator() {
    // eslint-disable-next-line no-console
    if (console && console.warn && !warningPrinted) {
      warningPrinted = true;
      // eslint-disable-next-line no-console
      console.warn(name + ': postcss.plugin was deprecated. Migration guide:\n' + 'https://evilmartians.com/chronicles/postcss-8-plugin-migration');
      if (process.env.LANG && process.env.LANG.startsWith('cn')) {
        /* c8 ignore next 7 */
        // eslint-disable-next-line no-console
        console.warn(name + ': 里面 postcss.plugin 被弃用. 迁移指南:\n' + 'https://www.w3ctech.com/topic/2226');
      }
    }
    var transformer = initializer.apply(void 0, arguments);
    transformer.postcssPlugin = name;
    transformer.postcssVersion = new Processor().version;
    return transformer;
  }
  var cache;
  Object.defineProperty(creator, 'postcss', {
    get: function get() {
      if (!cache) cache = creator();
      return cache;
    }
  });
  creator.process = function (css, processOpts, pluginOpts) {
    return postcss([creator(pluginOpts)]).process(css, processOpts);
  };
  return creator;
};
postcss.stringify = stringify;
postcss.parse = parse;
postcss.fromJSON = fromJSON;
postcss.list = list;
postcss.comment = function (defaults) {
  return new Comment(defaults);
};
postcss.atRule = function (defaults) {
  return new AtRule(defaults);
};
postcss.decl = function (defaults) {
  return new Declaration(defaults);
};
postcss.rule = function (defaults) {
  return new Rule(defaults);
};
postcss.root = function (defaults) {
  return new Root(defaults);
};
postcss.document = function (defaults) {
  return new Document(defaults);
};
postcss.CssSyntaxError = CssSyntaxError;
postcss.Declaration = Declaration;
postcss.Container = Container;
postcss.Processor = Processor;
postcss.Document = Document;
postcss.Comment = Comment;
postcss.Warning = Warning;
postcss.AtRule = AtRule;
postcss.Result = Result;
postcss.Input = Input;
postcss.Rule = Rule;
postcss.Root = Root;
postcss.Node = Node;
LazyResult.registerPostcss(postcss);
module.exports = postcss;
postcss["default"] = postcss;

/***/ }),

/***/ 3353:
/***/ ((module, __unused_webpack_exports, __webpack_require__) => {

"use strict";


function _typeof(obj) { "@babel/helpers - typeof"; return _typeof = "function" == typeof Symbol && "symbol" == typeof Symbol.iterator ? function (obj) { return typeof obj; } : function (obj) { return obj && "function" == typeof Symbol && obj.constructor === Symbol && obj !== Symbol.prototype ? "symbol" : typeof obj; }, _typeof(obj); }
function _classCallCheck(instance, Constructor) { if (!(instance instanceof Constructor)) { throw new TypeError("Cannot call a class as a function"); } }
function _defineProperties(target, props) { for (var i = 0; i < props.length; i++) { var descriptor = props[i]; descriptor.enumerable = descriptor.enumerable || false; descriptor.configurable = true; if ("value" in descriptor) descriptor.writable = true; Object.defineProperty(target, descriptor.key, descriptor); } }
function _createClass(Constructor, protoProps, staticProps) { if (protoProps) _defineProperties(Constructor.prototype, protoProps); if (staticProps) _defineProperties(Constructor, staticProps); Object.defineProperty(Constructor, "prototype", { writable: false }); return Constructor; }
var _require = __webpack_require__(209),
  SourceMapConsumer = _require.SourceMapConsumer,
  SourceMapGenerator = _require.SourceMapGenerator;
var _require2 = __webpack_require__(4777),
  existsSync = _require2.existsSync,
  readFileSync = _require2.readFileSync;
var _require3 = __webpack_require__(9830),
  dirname = _require3.dirname,
  join = _require3.join;
function fromBase64(str) {
  if (Buffer) {
    return Buffer.from(str, 'base64').toString();
  } else {
    /* c8 ignore next 2 */
    return window.atob(str);
  }
}
var PreviousMap = /*#__PURE__*/function () {
  function PreviousMap(css, opts) {
    _classCallCheck(this, PreviousMap);
    if (opts.map === false) return;
    this.loadAnnotation(css);
    this.inline = this.startWith(this.annotation, 'data:');
    var prev = opts.map ? opts.map.prev : undefined;
    var text = this.loadMap(opts.from, prev);
    if (!this.mapFile && opts.from) {
      this.mapFile = opts.from;
    }
    if (this.mapFile) this.root = dirname(this.mapFile);
    if (text) this.text = text;
  }
  _createClass(PreviousMap, [{
    key: "consumer",
    value: function consumer() {
      if (!this.consumerCache) {
        this.consumerCache = new SourceMapConsumer(this.text);
      }
      return this.consumerCache;
    }
  }, {
    key: "withContent",
    value: function withContent() {
      return !!(this.consumer().sourcesContent && this.consumer().sourcesContent.length > 0);
    }
  }, {
    key: "startWith",
    value: function startWith(string, start) {
      if (!string) return false;
      return string.substr(0, start.length) === start;
    }
  }, {
    key: "getAnnotationURL",
    value: function getAnnotationURL(sourceMapString) {
      return sourceMapString.replace(/^\/\*\s*# sourceMappingURL=/, '').trim();
    }
  }, {
    key: "loadAnnotation",
    value: function loadAnnotation(css) {
      var comments = css.match(/\/\*\s*# sourceMappingURL=/gm);
      if (!comments) return;

      // sourceMappingURLs from comments, strings, etc.
      var start = css.lastIndexOf(comments.pop());
      var end = css.indexOf('*/', start);
      if (start > -1 && end > -1) {
        // Locate the last sourceMappingURL to avoid pickin
        this.annotation = this.getAnnotationURL(css.substring(start, end));
      }
    }
  }, {
    key: "decodeInline",
    value: function decodeInline(text) {
      var baseCharsetUri = /^data:application\/json;charset=utf-?8;base64,/;
      var baseUri = /^data:application\/json;base64,/;
      var charsetUri = /^data:application\/json;charset=utf-?8,/;
      var uri = /^data:application\/json,/;
      if (charsetUri.test(text) || uri.test(text)) {
        return decodeURIComponent(text.substr(RegExp.lastMatch.length));
      }
      if (baseCharsetUri.test(text) || baseUri.test(text)) {
        return fromBase64(text.substr(RegExp.lastMatch.length));
      }
      var encoding = text.match(/data:application\/json;([^,]+),/)[1];
      throw new Error('Unsupported source map encoding ' + encoding);
    }
  }, {
    key: "loadFile",
    value: function loadFile(path) {
      this.root = dirname(path);
      if (existsSync(path)) {
        this.mapFile = path;
        return readFileSync(path, 'utf-8').toString().trim();
      }
    }
  }, {
    key: "loadMap",
    value: function loadMap(file, prev) {
      if (prev === false) return false;
      if (prev) {
        if (typeof prev === 'string') {
          return prev;
        } else if (typeof prev === 'function') {
          var prevPath = prev(file);
          if (prevPath) {
            var map = this.loadFile(prevPath);
            if (!map) {
              throw new Error('Unable to load previous source map: ' + prevPath.toString());
            }
            return map;
          }
        } else if (prev instanceof SourceMapConsumer) {
          return SourceMapGenerator.fromSourceMap(prev).toString();
        } else if (prev instanceof SourceMapGenerator) {
          return prev.toString();
        } else if (this.isMap(prev)) {
          return JSON.stringify(prev);
        } else {
          throw new Error('Unsupported previous source map format: ' + prev.toString());
        }
      } else if (this.inline) {
        return this.decodeInline(this.annotation);
      } else if (this.annotation) {
        var _map = this.annotation;
        if (file) _map = join(dirname(file), _map);
        return this.loadFile(_map);
      }
    }
  }, {
    key: "isMap",
    value: function isMap(map) {
      if (_typeof(map) !== 'object') return false;
      return typeof map.mappings === 'string' || typeof map._mappings === 'string' || Array.isArray(map.sections);
    }
  }]);
  return PreviousMap;
}();
module.exports = PreviousMap;
PreviousMap["default"] = PreviousMap;

/***/ }),

/***/ 9429:
/***/ ((module, __unused_webpack_exports, __webpack_require__) => {

"use strict";


function _typeof(obj) { "@babel/helpers - typeof"; return _typeof = "function" == typeof Symbol && "symbol" == typeof Symbol.iterator ? function (obj) { return typeof obj; } : function (obj) { return obj && "function" == typeof Symbol && obj.constructor === Symbol && obj !== Symbol.prototype ? "symbol" : typeof obj; }, _typeof(obj); }
function _createForOfIteratorHelper(o, allowArrayLike) { var it = typeof Symbol !== "undefined" && o[Symbol.iterator] || o["@@iterator"]; if (!it) { if (Array.isArray(o) || (it = _unsupportedIterableToArray(o)) || allowArrayLike && o && typeof o.length === "number") { if (it) o = it; var i = 0; var F = function F() {}; return { s: F, n: function n() { if (i >= o.length) return { done: true }; return { done: false, value: o[i++] }; }, e: function e(_e) { throw _e; }, f: F }; } throw new TypeError("Invalid attempt to iterate non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method."); } var normalCompletion = true, didErr = false, err; return { s: function s() { it = it.call(o); }, n: function n() { var step = it.next(); normalCompletion = step.done; return step; }, e: function e(_e2) { didErr = true; err = _e2; }, f: function f() { try { if (!normalCompletion && it["return"] != null) it["return"](); } finally { if (didErr) throw err; } } }; }
function _unsupportedIterableToArray(o, minLen) { if (!o) return; if (typeof o === "string") return _arrayLikeToArray(o, minLen); var n = Object.prototype.toString.call(o).slice(8, -1); if (n === "Object" && o.constructor) n = o.constructor.name; if (n === "Map" || n === "Set") return Array.from(o); if (n === "Arguments" || /^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(n)) return _arrayLikeToArray(o, minLen); }
function _arrayLikeToArray(arr, len) { if (len == null || len > arr.length) len = arr.length; for (var i = 0, arr2 = new Array(len); i < len; i++) { arr2[i] = arr[i]; } return arr2; }
function _classCallCheck(instance, Constructor) { if (!(instance instanceof Constructor)) { throw new TypeError("Cannot call a class as a function"); } }
function _defineProperties(target, props) { for (var i = 0; i < props.length; i++) { var descriptor = props[i]; descriptor.enumerable = descriptor.enumerable || false; descriptor.configurable = true; if ("value" in descriptor) descriptor.writable = true; Object.defineProperty(target, descriptor.key, descriptor); } }
function _createClass(Constructor, protoProps, staticProps) { if (protoProps) _defineProperties(Constructor.prototype, protoProps); if (staticProps) _defineProperties(Constructor, staticProps); Object.defineProperty(Constructor, "prototype", { writable: false }); return Constructor; }
var NoWorkResult = __webpack_require__(7686);
var LazyResult = __webpack_require__(6992);
var Document = __webpack_require__(7083);
var Root = __webpack_require__(7563);
var Processor = /*#__PURE__*/function () {
  function Processor() {
    var plugins = arguments.length > 0 && arguments[0] !== undefined ? arguments[0] : [];
    _classCallCheck(this, Processor);
    this.version = '8.4.18';
    this.plugins = this.normalize(plugins);
  }
  _createClass(Processor, [{
    key: "use",
    value: function use(plugin) {
      this.plugins = this.plugins.concat(this.normalize([plugin]));
      return this;
    }
  }, {
    key: "process",
    value: function process(css) {
      var opts = arguments.length > 1 && arguments[1] !== undefined ? arguments[1] : {};
      if (this.plugins.length === 0 && typeof opts.parser === 'undefined' && typeof opts.stringifier === 'undefined' && typeof opts.syntax === 'undefined') {
        return new NoWorkResult(this, css, opts);
      } else {
        return new LazyResult(this, css, opts);
      }
    }
  }, {
    key: "normalize",
    value: function normalize(plugins) {
      var normalized = [];
      var _iterator = _createForOfIteratorHelper(plugins),
        _step;
      try {
        for (_iterator.s(); !(_step = _iterator.n()).done;) {
          var i = _step.value;
          if (i.postcss === true) {
            i = i();
          } else if (i.postcss) {
            i = i.postcss;
          }
          if (_typeof(i) === 'object' && Array.isArray(i.plugins)) {
            normalized = normalized.concat(i.plugins);
          } else if (_typeof(i) === 'object' && i.postcssPlugin) {
            normalized.push(i);
          } else if (typeof i === 'function') {
            normalized.push(i);
          } else if (_typeof(i) === 'object' && (i.parse || i.stringify)) {
            if (false) {}
          } else {
            throw new Error(i + ' is not a PostCSS plugin');
          }
        }
      } catch (err) {
        _iterator.e(err);
      } finally {
        _iterator.f();
      }
      return normalized;
    }
  }]);
  return Processor;
}();
module.exports = Processor;
Processor["default"] = Processor;
Root.registerProcessor(Processor);
Document.registerProcessor(Processor);

/***/ }),

/***/ 6865:
/***/ ((module, __unused_webpack_exports, __webpack_require__) => {

"use strict";


function _classCallCheck(instance, Constructor) { if (!(instance instanceof Constructor)) { throw new TypeError("Cannot call a class as a function"); } }
function _defineProperties(target, props) { for (var i = 0; i < props.length; i++) { var descriptor = props[i]; descriptor.enumerable = descriptor.enumerable || false; descriptor.configurable = true; if ("value" in descriptor) descriptor.writable = true; Object.defineProperty(target, descriptor.key, descriptor); } }
function _createClass(Constructor, protoProps, staticProps) { if (protoProps) _defineProperties(Constructor.prototype, protoProps); if (staticProps) _defineProperties(Constructor, staticProps); Object.defineProperty(Constructor, "prototype", { writable: false }); return Constructor; }
var Warning = __webpack_require__(1662);
var Result = /*#__PURE__*/function () {
  function Result(processor, root, opts) {
    _classCallCheck(this, Result);
    this.processor = processor;
    this.messages = [];
    this.root = root;
    this.opts = opts;
    this.css = undefined;
    this.map = undefined;
  }
  _createClass(Result, [{
    key: "toString",
    value: function toString() {
      return this.css;
    }
  }, {
    key: "warn",
    value: function warn(text) {
      var opts = arguments.length > 1 && arguments[1] !== undefined ? arguments[1] : {};
      if (!opts.plugin) {
        if (this.lastPlugin && this.lastPlugin.postcssPlugin) {
          opts.plugin = this.lastPlugin.postcssPlugin;
        }
      }
      var warning = new Warning(text, opts);
      this.messages.push(warning);
      return warning;
    }
  }, {
    key: "warnings",
    value: function warnings() {
      return this.messages.filter(function (i) {
        return i.type === 'warning';
      });
    }
  }, {
    key: "content",
    get: function get() {
      return this.css;
    }
  }]);
  return Result;
}();
module.exports = Result;
Result["default"] = Result;

/***/ }),

/***/ 7563:
/***/ ((module, __unused_webpack_exports, __webpack_require__) => {

"use strict";


function _typeof(obj) { "@babel/helpers - typeof"; return _typeof = "function" == typeof Symbol && "symbol" == typeof Symbol.iterator ? function (obj) { return typeof obj; } : function (obj) { return obj && "function" == typeof Symbol && obj.constructor === Symbol && obj !== Symbol.prototype ? "symbol" : typeof obj; }, _typeof(obj); }
function _createForOfIteratorHelper(o, allowArrayLike) { var it = typeof Symbol !== "undefined" && o[Symbol.iterator] || o["@@iterator"]; if (!it) { if (Array.isArray(o) || (it = _unsupportedIterableToArray(o)) || allowArrayLike && o && typeof o.length === "number") { if (it) o = it; var i = 0; var F = function F() {}; return { s: F, n: function n() { if (i >= o.length) return { done: true }; return { done: false, value: o[i++] }; }, e: function e(_e) { throw _e; }, f: F }; } throw new TypeError("Invalid attempt to iterate non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method."); } var normalCompletion = true, didErr = false, err; return { s: function s() { it = it.call(o); }, n: function n() { var step = it.next(); normalCompletion = step.done; return step; }, e: function e(_e2) { didErr = true; err = _e2; }, f: function f() { try { if (!normalCompletion && it["return"] != null) it["return"](); } finally { if (didErr) throw err; } } }; }
function _unsupportedIterableToArray(o, minLen) { if (!o) return; if (typeof o === "string") return _arrayLikeToArray(o, minLen); var n = Object.prototype.toString.call(o).slice(8, -1); if (n === "Object" && o.constructor) n = o.constructor.name; if (n === "Map" || n === "Set") return Array.from(o); if (n === "Arguments" || /^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(n)) return _arrayLikeToArray(o, minLen); }
function _arrayLikeToArray(arr, len) { if (len == null || len > arr.length) len = arr.length; for (var i = 0, arr2 = new Array(len); i < len; i++) { arr2[i] = arr[i]; } return arr2; }
function _classCallCheck(instance, Constructor) { if (!(instance instanceof Constructor)) { throw new TypeError("Cannot call a class as a function"); } }
function _defineProperties(target, props) { for (var i = 0; i < props.length; i++) { var descriptor = props[i]; descriptor.enumerable = descriptor.enumerable || false; descriptor.configurable = true; if ("value" in descriptor) descriptor.writable = true; Object.defineProperty(target, descriptor.key, descriptor); } }
function _createClass(Constructor, protoProps, staticProps) { if (protoProps) _defineProperties(Constructor.prototype, protoProps); if (staticProps) _defineProperties(Constructor, staticProps); Object.defineProperty(Constructor, "prototype", { writable: false }); return Constructor; }
function _get() { if (typeof Reflect !== "undefined" && Reflect.get) { _get = Reflect.get.bind(); } else { _get = function _get(target, property, receiver) { var base = _superPropBase(target, property); if (!base) return; var desc = Object.getOwnPropertyDescriptor(base, property); if (desc.get) { return desc.get.call(arguments.length < 3 ? target : receiver); } return desc.value; }; } return _get.apply(this, arguments); }
function _superPropBase(object, property) { while (!Object.prototype.hasOwnProperty.call(object, property)) { object = _getPrototypeOf(object); if (object === null) break; } return object; }
function _inherits(subClass, superClass) { if (typeof superClass !== "function" && superClass !== null) { throw new TypeError("Super expression must either be null or a function"); } subClass.prototype = Object.create(superClass && superClass.prototype, { constructor: { value: subClass, writable: true, configurable: true } }); Object.defineProperty(subClass, "prototype", { writable: false }); if (superClass) _setPrototypeOf(subClass, superClass); }
function _setPrototypeOf(o, p) { _setPrototypeOf = Object.setPrototypeOf ? Object.setPrototypeOf.bind() : function _setPrototypeOf(o, p) { o.__proto__ = p; return o; }; return _setPrototypeOf(o, p); }
function _createSuper(Derived) { var hasNativeReflectConstruct = _isNativeReflectConstruct(); return function _createSuperInternal() { var Super = _getPrototypeOf(Derived), result; if (hasNativeReflectConstruct) { var NewTarget = _getPrototypeOf(this).constructor; result = Reflect.construct(Super, arguments, NewTarget); } else { result = Super.apply(this, arguments); } return _possibleConstructorReturn(this, result); }; }
function _possibleConstructorReturn(self, call) { if (call && (_typeof(call) === "object" || typeof call === "function")) { return call; } else if (call !== void 0) { throw new TypeError("Derived constructors may only return object or undefined"); } return _assertThisInitialized(self); }
function _assertThisInitialized(self) { if (self === void 0) { throw new ReferenceError("this hasn't been initialised - super() hasn't been called"); } return self; }
function _isNativeReflectConstruct() { if (typeof Reflect === "undefined" || !Reflect.construct) return false; if (Reflect.construct.sham) return false; if (typeof Proxy === "function") return true; try { Boolean.prototype.valueOf.call(Reflect.construct(Boolean, [], function () {})); return true; } catch (e) { return false; } }
function _getPrototypeOf(o) { _getPrototypeOf = Object.setPrototypeOf ? Object.getPrototypeOf.bind() : function _getPrototypeOf(o) { return o.__proto__ || Object.getPrototypeOf(o); }; return _getPrototypeOf(o); }
var Container = __webpack_require__(1204);
var LazyResult, Processor;
var Root = /*#__PURE__*/function (_Container) {
  _inherits(Root, _Container);
  var _super = _createSuper(Root);
  function Root(defaults) {
    var _this;
    _classCallCheck(this, Root);
    _this = _super.call(this, defaults);
    _this.type = 'root';
    if (!_this.nodes) _this.nodes = [];
    return _this;
  }
  _createClass(Root, [{
    key: "removeChild",
    value: function removeChild(child, ignore) {
      var index = this.index(child);
      if (!ignore && index === 0 && this.nodes.length > 1) {
        this.nodes[1].raws.before = this.nodes[index].raws.before;
      }
      return _get(_getPrototypeOf(Root.prototype), "removeChild", this).call(this, child);
    }
  }, {
    key: "normalize",
    value: function normalize(child, sample, type) {
      var nodes = _get(_getPrototypeOf(Root.prototype), "normalize", this).call(this, child);
      if (sample) {
        if (type === 'prepend') {
          if (this.nodes.length > 1) {
            sample.raws.before = this.nodes[1].raws.before;
          } else {
            delete sample.raws.before;
          }
        } else if (this.first !== sample) {
          var _iterator = _createForOfIteratorHelper(nodes),
            _step;
          try {
            for (_iterator.s(); !(_step = _iterator.n()).done;) {
              var node = _step.value;
              node.raws.before = sample.raws.before;
            }
          } catch (err) {
            _iterator.e(err);
          } finally {
            _iterator.f();
          }
        }
      }
      return nodes;
    }
  }, {
    key: "toResult",
    value: function toResult() {
      var opts = arguments.length > 0 && arguments[0] !== undefined ? arguments[0] : {};
      var lazy = new LazyResult(new Processor(), this, opts);
      return lazy.stringify();
    }
  }]);
  return Root;
}(Container);
Root.registerLazyResult = function (dependant) {
  LazyResult = dependant;
};
Root.registerProcessor = function (dependant) {
  Processor = dependant;
};
module.exports = Root;
Root["default"] = Root;
Container.registerRoot(Root);

/***/ }),

/***/ 6621:
/***/ ((module, __unused_webpack_exports, __webpack_require__) => {

"use strict";


function _typeof(obj) { "@babel/helpers - typeof"; return _typeof = "function" == typeof Symbol && "symbol" == typeof Symbol.iterator ? function (obj) { return typeof obj; } : function (obj) { return obj && "function" == typeof Symbol && obj.constructor === Symbol && obj !== Symbol.prototype ? "symbol" : typeof obj; }, _typeof(obj); }
function _classCallCheck(instance, Constructor) { if (!(instance instanceof Constructor)) { throw new TypeError("Cannot call a class as a function"); } }
function _defineProperties(target, props) { for (var i = 0; i < props.length; i++) { var descriptor = props[i]; descriptor.enumerable = descriptor.enumerable || false; descriptor.configurable = true; if ("value" in descriptor) descriptor.writable = true; Object.defineProperty(target, descriptor.key, descriptor); } }
function _createClass(Constructor, protoProps, staticProps) { if (protoProps) _defineProperties(Constructor.prototype, protoProps); if (staticProps) _defineProperties(Constructor, staticProps); Object.defineProperty(Constructor, "prototype", { writable: false }); return Constructor; }
function _inherits(subClass, superClass) { if (typeof superClass !== "function" && superClass !== null) { throw new TypeError("Super expression must either be null or a function"); } subClass.prototype = Object.create(superClass && superClass.prototype, { constructor: { value: subClass, writable: true, configurable: true } }); Object.defineProperty(subClass, "prototype", { writable: false }); if (superClass) _setPrototypeOf(subClass, superClass); }
function _setPrototypeOf(o, p) { _setPrototypeOf = Object.setPrototypeOf ? Object.setPrototypeOf.bind() : function _setPrototypeOf(o, p) { o.__proto__ = p; return o; }; return _setPrototypeOf(o, p); }
function _createSuper(Derived) { var hasNativeReflectConstruct = _isNativeReflectConstruct(); return function _createSuperInternal() { var Super = _getPrototypeOf(Derived), result; if (hasNativeReflectConstruct) { var NewTarget = _getPrototypeOf(this).constructor; result = Reflect.construct(Super, arguments, NewTarget); } else { result = Super.apply(this, arguments); } return _possibleConstructorReturn(this, result); }; }
function _possibleConstructorReturn(self, call) { if (call && (_typeof(call) === "object" || typeof call === "function")) { return call; } else if (call !== void 0) { throw new TypeError("Derived constructors may only return object or undefined"); } return _assertThisInitialized(self); }
function _assertThisInitialized(self) { if (self === void 0) { throw new ReferenceError("this hasn't been initialised - super() hasn't been called"); } return self; }
function _isNativeReflectConstruct() { if (typeof Reflect === "undefined" || !Reflect.construct) return false; if (Reflect.construct.sham) return false; if (typeof Proxy === "function") return true; try { Boolean.prototype.valueOf.call(Reflect.construct(Boolean, [], function () {})); return true; } catch (e) { return false; } }
function _getPrototypeOf(o) { _getPrototypeOf = Object.setPrototypeOf ? Object.getPrototypeOf.bind() : function _getPrototypeOf(o) { return o.__proto__ || Object.getPrototypeOf(o); }; return _getPrototypeOf(o); }
var Container = __webpack_require__(1204);
var list = __webpack_require__(6136);
var Rule = /*#__PURE__*/function (_Container) {
  _inherits(Rule, _Container);
  var _super = _createSuper(Rule);
  function Rule(defaults) {
    var _this;
    _classCallCheck(this, Rule);
    _this = _super.call(this, defaults);
    _this.type = 'rule';
    if (!_this.nodes) _this.nodes = [];
    return _this;
  }
  _createClass(Rule, [{
    key: "selectors",
    get: function get() {
      return list.comma(this.selector);
    },
    set: function set(values) {
      var match = this.selector ? this.selector.match(/,\s*/) : null;
      var sep = match ? match[0] : ',' + this.raw('between', 'beforeOpen');
      this.selector = values.join(sep);
    }
  }]);
  return Rule;
}(Container);
module.exports = Rule;
Rule["default"] = Rule;
Container.registerRule(Rule);

/***/ }),

/***/ 5701:
/***/ ((module) => {

"use strict";


function _classCallCheck(instance, Constructor) { if (!(instance instanceof Constructor)) { throw new TypeError("Cannot call a class as a function"); } }
function _defineProperties(target, props) { for (var i = 0; i < props.length; i++) { var descriptor = props[i]; descriptor.enumerable = descriptor.enumerable || false; descriptor.configurable = true; if ("value" in descriptor) descriptor.writable = true; Object.defineProperty(target, descriptor.key, descriptor); } }
function _createClass(Constructor, protoProps, staticProps) { if (protoProps) _defineProperties(Constructor.prototype, protoProps); if (staticProps) _defineProperties(Constructor, staticProps); Object.defineProperty(Constructor, "prototype", { writable: false }); return Constructor; }
var DEFAULT_RAW = {
  colon: ': ',
  indent: '    ',
  beforeDecl: '\n',
  beforeRule: '\n',
  beforeOpen: ' ',
  beforeClose: '\n',
  beforeComment: '\n',
  after: '\n',
  emptyBody: '',
  commentLeft: ' ',
  commentRight: ' ',
  semicolon: false
};
function capitalize(str) {
  return str[0].toUpperCase() + str.slice(1);
}
var Stringifier = /*#__PURE__*/function () {
  function Stringifier(builder) {
    _classCallCheck(this, Stringifier);
    this.builder = builder;
  }
  _createClass(Stringifier, [{
    key: "stringify",
    value: function stringify(node, semicolon) {
      /* c8 ignore start */
      if (!this[node.type]) {
        throw new Error('Unknown AST node type ' + node.type + '. ' + 'Maybe you need to change PostCSS stringifier.');
      }
      /* c8 ignore stop */
      this[node.type](node, semicolon);
    }
  }, {
    key: "document",
    value: function document(node) {
      this.body(node);
    }
  }, {
    key: "root",
    value: function root(node) {
      this.body(node);
      if (node.raws.after) this.builder(node.raws.after);
    }
  }, {
    key: "comment",
    value: function comment(node) {
      var left = this.raw(node, 'left', 'commentLeft');
      var right = this.raw(node, 'right', 'commentRight');
      this.builder('/*' + left + node.text + right + '*/', node);
    }
  }, {
    key: "decl",
    value: function decl(node, semicolon) {
      var between = this.raw(node, 'between', 'colon');
      var string = node.prop + between + this.rawValue(node, 'value');
      if (node.important) {
        string += node.raws.important || ' !important';
      }
      if (semicolon) string += ';';
      this.builder(string, node);
    }
  }, {
    key: "rule",
    value: function rule(node) {
      this.block(node, this.rawValue(node, 'selector'));
      if (node.raws.ownSemicolon) {
        this.builder(node.raws.ownSemicolon, node, 'end');
      }
    }
  }, {
    key: "atrule",
    value: function atrule(node, semicolon) {
      var name = '@' + node.name;
      var params = node.params ? this.rawValue(node, 'params') : '';
      if (typeof node.raws.afterName !== 'undefined') {
        name += node.raws.afterName;
      } else if (params) {
        name += ' ';
      }
      if (node.nodes) {
        this.block(node, name + params);
      } else {
        var end = (node.raws.between || '') + (semicolon ? ';' : '');
        this.builder(name + params + end, node);
      }
    }
  }, {
    key: "body",
    value: function body(node) {
      var last = node.nodes.length - 1;
      while (last > 0) {
        if (node.nodes[last].type !== 'comment') break;
        last -= 1;
      }
      var semicolon = this.raw(node, 'semicolon');
      for (var i = 0; i < node.nodes.length; i++) {
        var child = node.nodes[i];
        var before = this.raw(child, 'before');
        if (before) this.builder(before);
        this.stringify(child, last !== i || semicolon);
      }
    }
  }, {
    key: "block",
    value: function block(node, start) {
      var between = this.raw(node, 'between', 'beforeOpen');
      this.builder(start + between + '{', node, 'start');
      var after;
      if (node.nodes && node.nodes.length) {
        this.body(node);
        after = this.raw(node, 'after');
      } else {
        after = this.raw(node, 'after', 'emptyBody');
      }
      if (after) this.builder(after);
      this.builder('}', node, 'end');
    }
  }, {
    key: "raw",
    value: function raw(node, own, detect) {
      var value;
      if (!detect) detect = own;

      // Already had
      if (own) {
        value = node.raws[own];
        if (typeof value !== 'undefined') return value;
      }
      var parent = node.parent;
      if (detect === 'before') {
        // Hack for first rule in CSS
        if (!parent || parent.type === 'root' && parent.first === node) {
          return '';
        }

        // `root` nodes in `document` should use only their own raws
        if (parent && parent.type === 'document') {
          return '';
        }
      }

      // Floating child without parent
      if (!parent) return DEFAULT_RAW[detect];

      // Detect style by other nodes
      var root = node.root();
      if (!root.rawCache) root.rawCache = {};
      if (typeof root.rawCache[detect] !== 'undefined') {
        return root.rawCache[detect];
      }
      if (detect === 'before' || detect === 'after') {
        return this.beforeAfter(node, detect);
      } else {
        var method = 'raw' + capitalize(detect);
        if (this[method]) {
          value = this[method](root, node);
        } else {
          root.walk(function (i) {
            value = i.raws[own];
            if (typeof value !== 'undefined') return false;
          });
        }
      }
      if (typeof value === 'undefined') value = DEFAULT_RAW[detect];
      root.rawCache[detect] = value;
      return value;
    }
  }, {
    key: "rawSemicolon",
    value: function rawSemicolon(root) {
      var value;
      root.walk(function (i) {
        if (i.nodes && i.nodes.length && i.last.type === 'decl') {
          value = i.raws.semicolon;
          if (typeof value !== 'undefined') return false;
        }
      });
      return value;
    }
  }, {
    key: "rawEmptyBody",
    value: function rawEmptyBody(root) {
      var value;
      root.walk(function (i) {
        if (i.nodes && i.nodes.length === 0) {
          value = i.raws.after;
          if (typeof value !== 'undefined') return false;
        }
      });
      return value;
    }
  }, {
    key: "rawIndent",
    value: function rawIndent(root) {
      if (root.raws.indent) return root.raws.indent;
      var value;
      root.walk(function (i) {
        var p = i.parent;
        if (p && p !== root && p.parent && p.parent === root) {
          if (typeof i.raws.before !== 'undefined') {
            var parts = i.raws.before.split('\n');
            value = parts[parts.length - 1];
            value = value.replace(/\S/g, '');
            return false;
          }
        }
      });
      return value;
    }
  }, {
    key: "rawBeforeComment",
    value: function rawBeforeComment(root, node) {
      var value;
      root.walkComments(function (i) {
        if (typeof i.raws.before !== 'undefined') {
          value = i.raws.before;
          if (value.includes('\n')) {
            value = value.replace(/[^\n]+$/, '');
          }
          return false;
        }
      });
      if (typeof value === 'undefined') {
        value = this.raw(node, null, 'beforeDecl');
      } else if (value) {
        value = value.replace(/\S/g, '');
      }
      return value;
    }
  }, {
    key: "rawBeforeDecl",
    value: function rawBeforeDecl(root, node) {
      var value;
      root.walkDecls(function (i) {
        if (typeof i.raws.before !== 'undefined') {
          value = i.raws.before;
          if (value.includes('\n')) {
            value = value.replace(/[^\n]+$/, '');
          }
          return false;
        }
      });
      if (typeof value === 'undefined') {
        value = this.raw(node, null, 'beforeRule');
      } else if (value) {
        value = value.replace(/\S/g, '');
      }
      return value;
    }
  }, {
    key: "rawBeforeRule",
    value: function rawBeforeRule(root) {
      var value;
      root.walk(function (i) {
        if (i.nodes && (i.parent !== root || root.first !== i)) {
          if (typeof i.raws.before !== 'undefined') {
            value = i.raws.before;
            if (value.includes('\n')) {
              value = value.replace(/[^\n]+$/, '');
            }
            return false;
          }
        }
      });
      if (value) value = value.replace(/\S/g, '');
      return value;
    }
  }, {
    key: "rawBeforeClose",
    value: function rawBeforeClose(root) {
      var value;
      root.walk(function (i) {
        if (i.nodes && i.nodes.length > 0) {
          if (typeof i.raws.after !== 'undefined') {
            value = i.raws.after;
            if (value.includes('\n')) {
              value = value.replace(/[^\n]+$/, '');
            }
            return false;
          }
        }
      });
      if (value) value = value.replace(/\S/g, '');
      return value;
    }
  }, {
    key: "rawBeforeOpen",
    value: function rawBeforeOpen(root) {
      var value;
      root.walk(function (i) {
        if (i.type !== 'decl') {
          value = i.raws.between;
          if (typeof value !== 'undefined') return false;
        }
      });
      return value;
    }
  }, {
    key: "rawColon",
    value: function rawColon(root) {
      var value;
      root.walkDecls(function (i) {
        if (typeof i.raws.between !== 'undefined') {
          value = i.raws.between.replace(/[^\s:]/g, '');
          return false;
        }
      });
      return value;
    }
  }, {
    key: "beforeAfter",
    value: function beforeAfter(node, detect) {
      var value;
      if (node.type === 'decl') {
        value = this.raw(node, null, 'beforeDecl');
      } else if (node.type === 'comment') {
        value = this.raw(node, null, 'beforeComment');
      } else if (detect === 'before') {
        value = this.raw(node, null, 'beforeRule');
      } else {
        value = this.raw(node, null, 'beforeClose');
      }
      var buf = node.parent;
      var depth = 0;
      while (buf && buf.type !== 'root') {
        depth += 1;
        buf = buf.parent;
      }
      if (value.includes('\n')) {
        var indent = this.raw(node, null, 'indent');
        if (indent.length) {
          for (var step = 0; step < depth; step++) {
            value += indent;
          }
        }
      }
      return value;
    }
  }, {
    key: "rawValue",
    value: function rawValue(node, prop) {
      var value = node[prop];
      var raw = node.raws[prop];
      if (raw && raw.value === value) {
        return raw.raw;
      }
      return value;
    }
  }]);
  return Stringifier;
}();
module.exports = Stringifier;
Stringifier["default"] = Stringifier;

/***/ }),

/***/ 6157:
/***/ ((module, __unused_webpack_exports, __webpack_require__) => {

"use strict";


var Stringifier = __webpack_require__(5701);
function stringify(node, builder) {
  var str = new Stringifier(builder);
  str.stringify(node);
}
module.exports = stringify;
stringify["default"] = stringify;

/***/ }),

/***/ 5506:
/***/ ((module) => {

"use strict";


module.exports.isClean = Symbol('isClean');
module.exports.my = Symbol('my');

/***/ }),

/***/ 1157:
/***/ ((module) => {

"use strict";


var SINGLE_QUOTE = "'".charCodeAt(0);
var DOUBLE_QUOTE = '"'.charCodeAt(0);
var BACKSLASH = '\\'.charCodeAt(0);
var SLASH = '/'.charCodeAt(0);
var NEWLINE = '\n'.charCodeAt(0);
var SPACE = ' '.charCodeAt(0);
var FEED = '\f'.charCodeAt(0);
var TAB = '\t'.charCodeAt(0);
var CR = '\r'.charCodeAt(0);
var OPEN_SQUARE = '['.charCodeAt(0);
var CLOSE_SQUARE = ']'.charCodeAt(0);
var OPEN_PARENTHESES = '('.charCodeAt(0);
var CLOSE_PARENTHESES = ')'.charCodeAt(0);
var OPEN_CURLY = '{'.charCodeAt(0);
var CLOSE_CURLY = '}'.charCodeAt(0);
var SEMICOLON = ';'.charCodeAt(0);
var ASTERISK = '*'.charCodeAt(0);
var COLON = ':'.charCodeAt(0);
var AT = '@'.charCodeAt(0);
var RE_AT_END = /[\t\n\f\r "#'()/;[\\\]{}]/g;
var RE_WORD_END = /[\t\n\f\r !"#'():;@[\\\]{}]|\/(?=\*)/g;
var RE_BAD_BRACKET = /.[\n"'(/\\]/;
var RE_HEX_ESCAPE = /[\da-f]/i;
module.exports = function tokenizer(input) {
  var options = arguments.length > 1 && arguments[1] !== undefined ? arguments[1] : {};
  var css = input.css.valueOf();
  var ignore = options.ignoreErrors;
  var code, next, quote, content, escape;
  var escaped, escapePos, prev, n, currentToken;
  var length = css.length;
  var pos = 0;
  var buffer = [];
  var returned = [];
  function position() {
    return pos;
  }
  function unclosed(what) {
    throw input.error('Unclosed ' + what, pos);
  }
  function endOfFile() {
    return returned.length === 0 && pos >= length;
  }
  function nextToken(opts) {
    if (returned.length) return returned.pop();
    if (pos >= length) return;
    var ignoreUnclosed = opts ? opts.ignoreUnclosed : false;
    code = css.charCodeAt(pos);
    switch (code) {
      case NEWLINE:
      case SPACE:
      case TAB:
      case CR:
      case FEED:
        {
          next = pos;
          do {
            next += 1;
            code = css.charCodeAt(next);
          } while (code === SPACE || code === NEWLINE || code === TAB || code === CR || code === FEED);
          currentToken = ['space', css.slice(pos, next)];
          pos = next - 1;
          break;
        }
      case OPEN_SQUARE:
      case CLOSE_SQUARE:
      case OPEN_CURLY:
      case CLOSE_CURLY:
      case COLON:
      case SEMICOLON:
      case CLOSE_PARENTHESES:
        {
          var controlChar = String.fromCharCode(code);
          currentToken = [controlChar, controlChar, pos];
          break;
        }
      case OPEN_PARENTHESES:
        {
          prev = buffer.length ? buffer.pop()[1] : '';
          n = css.charCodeAt(pos + 1);
          if (prev === 'url' && n !== SINGLE_QUOTE && n !== DOUBLE_QUOTE && n !== SPACE && n !== NEWLINE && n !== TAB && n !== FEED && n !== CR) {
            next = pos;
            do {
              escaped = false;
              next = css.indexOf(')', next + 1);
              if (next === -1) {
                if (ignore || ignoreUnclosed) {
                  next = pos;
                  break;
                } else {
                  unclosed('bracket');
                }
              }
              escapePos = next;
              while (css.charCodeAt(escapePos - 1) === BACKSLASH) {
                escapePos -= 1;
                escaped = !escaped;
              }
            } while (escaped);
            currentToken = ['brackets', css.slice(pos, next + 1), pos, next];
            pos = next;
          } else {
            next = css.indexOf(')', pos + 1);
            content = css.slice(pos, next + 1);
            if (next === -1 || RE_BAD_BRACKET.test(content)) {
              currentToken = ['(', '(', pos];
            } else {
              currentToken = ['brackets', content, pos, next];
              pos = next;
            }
          }
          break;
        }
      case SINGLE_QUOTE:
      case DOUBLE_QUOTE:
        {
          quote = code === SINGLE_QUOTE ? "'" : '"';
          next = pos;
          do {
            escaped = false;
            next = css.indexOf(quote, next + 1);
            if (next === -1) {
              if (ignore || ignoreUnclosed) {
                next = pos + 1;
                break;
              } else {
                unclosed('string');
              }
            }
            escapePos = next;
            while (css.charCodeAt(escapePos - 1) === BACKSLASH) {
              escapePos -= 1;
              escaped = !escaped;
            }
          } while (escaped);
          currentToken = ['string', css.slice(pos, next + 1), pos, next];
          pos = next;
          break;
        }
      case AT:
        {
          RE_AT_END.lastIndex = pos + 1;
          RE_AT_END.test(css);
          if (RE_AT_END.lastIndex === 0) {
            next = css.length - 1;
          } else {
            next = RE_AT_END.lastIndex - 2;
          }
          currentToken = ['at-word', css.slice(pos, next + 1), pos, next];
          pos = next;
          break;
        }
      case BACKSLASH:
        {
          next = pos;
          escape = true;
          while (css.charCodeAt(next + 1) === BACKSLASH) {
            next += 1;
            escape = !escape;
          }
          code = css.charCodeAt(next + 1);
          if (escape && code !== SLASH && code !== SPACE && code !== NEWLINE && code !== TAB && code !== CR && code !== FEED) {
            next += 1;
            if (RE_HEX_ESCAPE.test(css.charAt(next))) {
              while (RE_HEX_ESCAPE.test(css.charAt(next + 1))) {
                next += 1;
              }
              if (css.charCodeAt(next + 1) === SPACE) {
                next += 1;
              }
            }
          }
          currentToken = ['word', css.slice(pos, next + 1), pos, next];
          pos = next;
          break;
        }
      default:
        {
          if (code === SLASH && css.charCodeAt(pos + 1) === ASTERISK) {
            next = css.indexOf('*/', pos + 2) + 1;
            if (next === 0) {
              if (ignore || ignoreUnclosed) {
                next = css.length;
              } else {
                unclosed('comment');
              }
            }
            currentToken = ['comment', css.slice(pos, next + 1), pos, next];
            pos = next;
          } else {
            RE_WORD_END.lastIndex = pos + 1;
            RE_WORD_END.test(css);
            if (RE_WORD_END.lastIndex === 0) {
              next = css.length - 1;
            } else {
              next = RE_WORD_END.lastIndex - 2;
            }
            currentToken = ['word', css.slice(pos, next + 1), pos, next];
            buffer.push(currentToken);
            pos = next;
          }
          break;
        }
    }
    pos++;
    return currentToken;
  }
  function back(token) {
    returned.push(token);
  }
  return {
    back: back,
    nextToken: nextToken,
    endOfFile: endOfFile,
    position: position
  };
};

/***/ }),

/***/ 6574:
/***/ ((module) => {

"use strict";
/* eslint-disable no-console */


var printed = {};
module.exports = function warnOnce(message) {
  if (printed[message]) return;
  printed[message] = true;
  if (typeof console !== 'undefined' && console.warn) {
    console.warn(message);
  }
};

/***/ }),

/***/ 1662:
/***/ ((module) => {

"use strict";


function _classCallCheck(instance, Constructor) { if (!(instance instanceof Constructor)) { throw new TypeError("Cannot call a class as a function"); } }
function _defineProperties(target, props) { for (var i = 0; i < props.length; i++) { var descriptor = props[i]; descriptor.enumerable = descriptor.enumerable || false; descriptor.configurable = true; if ("value" in descriptor) descriptor.writable = true; Object.defineProperty(target, descriptor.key, descriptor); } }
function _createClass(Constructor, protoProps, staticProps) { if (protoProps) _defineProperties(Constructor.prototype, protoProps); if (staticProps) _defineProperties(Constructor, staticProps); Object.defineProperty(Constructor, "prototype", { writable: false }); return Constructor; }
var Warning = /*#__PURE__*/function () {
  function Warning(text) {
    var opts = arguments.length > 1 && arguments[1] !== undefined ? arguments[1] : {};
    _classCallCheck(this, Warning);
    this.type = 'warning';
    this.text = text;
    if (opts.node && opts.node.source) {
      var range = opts.node.rangeBy(opts);
      this.line = range.start.line;
      this.column = range.start.column;
      this.endLine = range.end.line;
      this.endColumn = range.end.column;
    }
    for (var opt in opts) {
      this[opt] = opts[opt];
    }
  }
  _createClass(Warning, [{
    key: "toString",
    value: function toString() {
      if (this.node) {
        return this.node.error(this.text, {
          plugin: this.plugin,
          index: this.index,
          word: this.word
        }).message;
      }
      if (this.plugin) {
        return this.plugin + ': ' + this.text;
      }
      return this.text;
    }
  }]);
  return Warning;
}();
module.exports = Warning;
Warning["default"] = Warning;

/***/ }),

/***/ 6760:
/***/ (function(module, __unused_webpack_exports, __webpack_require__) {

/* module decorator */ module = __webpack_require__.nmd(module);
function _typeof(obj) { "@babel/helpers - typeof"; return _typeof = "function" == typeof Symbol && "symbol" == typeof Symbol.iterator ? function (obj) { return typeof obj; } : function (obj) { return obj && "function" == typeof Symbol && obj.constructor === Symbol && obj !== Symbol.prototype ? "symbol" : typeof obj; }, _typeof(obj); }
/**
 * Copyright (c) 2014, Facebook, Inc.
 * All rights reserved.
 *
 * This source code is licensed under the BSD-style license found in the
 * https://raw.github.com/facebook/regenerator/master/LICENSE file. An
 * additional grant of patent rights can be found in the PATENTS file in
 * the same directory.
 */

!function (global) {
  "use strict";

  var Op = Object.prototype;
  var hasOwn = Op.hasOwnProperty;
  var undefined; // More compressible than void 0.
  var $Symbol = typeof Symbol === "function" ? Symbol : {};
  var iteratorSymbol = $Symbol.iterator || "@@iterator";
  var asyncIteratorSymbol = $Symbol.asyncIterator || "@@asyncIterator";
  var toStringTagSymbol = $Symbol.toStringTag || "@@toStringTag";
  var inModule = ( false ? 0 : _typeof(module)) === "object";
  var runtime = global.regeneratorRuntime;
  if (runtime) {
    if (inModule) {
      // If regeneratorRuntime is defined globally and we're in a module,
      // make the exports object identical to regeneratorRuntime.
      module.exports = runtime;
    }
    // Don't bother evaluating the rest of this file if the runtime was
    // already defined globally.
    return;
  }

  // Define the runtime globally (as expected by generated code) as either
  // module.exports (if we're in a module) or a new, empty object.
  runtime = global.regeneratorRuntime = inModule ? module.exports : {};
  function wrap(innerFn, outerFn, self, tryLocsList) {
    // If outerFn provided and outerFn.prototype is a Generator, then outerFn.prototype instanceof Generator.
    var protoGenerator = outerFn && outerFn.prototype instanceof Generator ? outerFn : Generator;
    var generator = Object.create(protoGenerator.prototype);
    var context = new Context(tryLocsList || []);

    // The ._invoke method unifies the implementations of the .next,
    // .throw, and .return methods.
    generator._invoke = makeInvokeMethod(innerFn, self, context);
    return generator;
  }
  runtime.wrap = wrap;

  // Try/catch helper to minimize deoptimizations. Returns a completion
  // record like context.tryEntries[i].completion. This interface could
  // have been (and was previously) designed to take a closure to be
  // invoked without arguments, but in all the cases we care about we
  // already have an existing method we want to call, so there's no need
  // to create a new function object. We can even get away with assuming
  // the method takes exactly one argument, since that happens to be true
  // in every case, so we don't have to touch the arguments object. The
  // only additional allocation required is the completion record, which
  // has a stable shape and so hopefully should be cheap to allocate.
  function tryCatch(fn, obj, arg) {
    try {
      return {
        type: "normal",
        arg: fn.call(obj, arg)
      };
    } catch (err) {
      return {
        type: "throw",
        arg: err
      };
    }
  }
  var GenStateSuspendedStart = "suspendedStart";
  var GenStateSuspendedYield = "suspendedYield";
  var GenStateExecuting = "executing";
  var GenStateCompleted = "completed";

  // Returning this object from the innerFn has the same effect as
  // breaking out of the dispatch switch statement.
  var ContinueSentinel = {};

  // Dummy constructor functions that we use as the .constructor and
  // .constructor.prototype properties for functions that return Generator
  // objects. For full spec compliance, you may wish to configure your
  // minifier not to mangle the names of these two functions.
  function Generator() {}
  function GeneratorFunction() {}
  function GeneratorFunctionPrototype() {}

  // This is a polyfill for %IteratorPrototype% for environments that
  // don't natively support it.
  var IteratorPrototype = {};
  IteratorPrototype[iteratorSymbol] = function () {
    return this;
  };
  var getProto = Object.getPrototypeOf;
  var NativeIteratorPrototype = getProto && getProto(getProto(values([])));
  if (NativeIteratorPrototype && NativeIteratorPrototype !== Op && hasOwn.call(NativeIteratorPrototype, iteratorSymbol)) {
    // This environment has a native %IteratorPrototype%; use it instead
    // of the polyfill.
    IteratorPrototype = NativeIteratorPrototype;
  }
  var Gp = GeneratorFunctionPrototype.prototype = Generator.prototype = Object.create(IteratorPrototype);
  GeneratorFunction.prototype = Gp.constructor = GeneratorFunctionPrototype;
  GeneratorFunctionPrototype.constructor = GeneratorFunction;
  GeneratorFunctionPrototype[toStringTagSymbol] = GeneratorFunction.displayName = "GeneratorFunction";

  // Helper for defining the .next, .throw, and .return methods of the
  // Iterator interface in terms of a single ._invoke method.
  function defineIteratorMethods(prototype) {
    ["next", "throw", "return"].forEach(function (method) {
      prototype[method] = function (arg) {
        return this._invoke(method, arg);
      };
    });
  }
  runtime.isGeneratorFunction = function (genFun) {
    var ctor = typeof genFun === "function" && genFun.constructor;
    return ctor ? ctor === GeneratorFunction ||
    // For the native GeneratorFunction constructor, the best we can
    // do is to check its .name property.
    (ctor.displayName || ctor.name) === "GeneratorFunction" : false;
  };
  runtime.mark = function (genFun) {
    if (Object.setPrototypeOf) {
      Object.setPrototypeOf(genFun, GeneratorFunctionPrototype);
    } else {
      genFun.__proto__ = GeneratorFunctionPrototype;
      if (!(toStringTagSymbol in genFun)) {
        genFun[toStringTagSymbol] = "GeneratorFunction";
      }
    }
    genFun.prototype = Object.create(Gp);
    return genFun;
  };

  // Within the body of any async function, `await x` is transformed to
  // `yield regeneratorRuntime.awrap(x)`, so that the runtime can test
  // `hasOwn.call(value, "__await")` to determine if the yielded value is
  // meant to be awaited.
  runtime.awrap = function (arg) {
    return {
      __await: arg
    };
  };
  function AsyncIterator(generator) {
    function invoke(method, arg, resolve, reject) {
      var record = tryCatch(generator[method], generator, arg);
      if (record.type === "throw") {
        reject(record.arg);
      } else {
        var result = record.arg;
        var value = result.value;
        if (value && _typeof(value) === "object" && hasOwn.call(value, "__await")) {
          return Promise.resolve(value.__await).then(function (value) {
            invoke("next", value, resolve, reject);
          }, function (err) {
            invoke("throw", err, resolve, reject);
          });
        }
        return Promise.resolve(value).then(function (unwrapped) {
          // When a yielded Promise is resolved, its final value becomes
          // the .value of the Promise<{value,done}> result for the
          // current iteration. If the Promise is rejected, however, the
          // result for this iteration will be rejected with the same
          // reason. Note that rejections of yielded Promises are not
          // thrown back into the generator function, as is the case
          // when an awaited Promise is rejected. This difference in
          // behavior between yield and await is important, because it
          // allows the consumer to decide what to do with the yielded
          // rejection (swallow it and continue, manually .throw it back
          // into the generator, abandon iteration, whatever). With
          // await, by contrast, there is no opportunity to examine the
          // rejection reason outside the generator function, so the
          // only option is to throw it from the await expression, and
          // let the generator function handle the exception.
          result.value = unwrapped;
          resolve(result);
        }, reject);
      }
    }
    if (_typeof(global.process) === "object" && global.process.domain) {
      invoke = global.process.domain.bind(invoke);
    }
    var previousPromise;
    function enqueue(method, arg) {
      function callInvokeWithMethodAndArg() {
        return new Promise(function (resolve, reject) {
          invoke(method, arg, resolve, reject);
        });
      }
      return previousPromise =
      // If enqueue has been called before, then we want to wait until
      // all previous Promises have been resolved before calling invoke,
      // so that results are always delivered in the correct order. If
      // enqueue has not been called before, then it is important to
      // call invoke immediately, without waiting on a callback to fire,
      // so that the async generator function has the opportunity to do
      // any necessary setup in a predictable way. This predictability
      // is why the Promise constructor synchronously invokes its
      // executor callback, and why async functions synchronously
      // execute code before the first await. Since we implement simple
      // async functions in terms of async generators, it is especially
      // important to get this right, even though it requires care.
      previousPromise ? previousPromise.then(callInvokeWithMethodAndArg,
      // Avoid propagating failures to Promises returned by later
      // invocations of the iterator.
      callInvokeWithMethodAndArg) : callInvokeWithMethodAndArg();
    }

    // Define the unified helper method that is used to implement .next,
    // .throw, and .return (see defineIteratorMethods).
    this._invoke = enqueue;
  }
  defineIteratorMethods(AsyncIterator.prototype);
  AsyncIterator.prototype[asyncIteratorSymbol] = function () {
    return this;
  };
  runtime.AsyncIterator = AsyncIterator;

  // Note that simple async functions are implemented on top of
  // AsyncIterator objects; they just return a Promise for the value of
  // the final result produced by the iterator.
  runtime.async = function (innerFn, outerFn, self, tryLocsList) {
    var iter = new AsyncIterator(wrap(innerFn, outerFn, self, tryLocsList));
    return runtime.isGeneratorFunction(outerFn) ? iter // If outerFn is a generator, return the full iterator.
    : iter.next().then(function (result) {
      return result.done ? result.value : iter.next();
    });
  };
  function makeInvokeMethod(innerFn, self, context) {
    var state = GenStateSuspendedStart;
    return function invoke(method, arg) {
      if (state === GenStateExecuting) {
        throw new Error("Generator is already running");
      }
      if (state === GenStateCompleted) {
        if (method === "throw") {
          throw arg;
        }

        // Be forgiving, per 25.3.3.3.3 of the spec:
        // https://people.mozilla.org/~jorendorff/es6-draft.html#sec-generatorresume
        return doneResult();
      }
      context.method = method;
      context.arg = arg;
      while (true) {
        var delegate = context.delegate;
        if (delegate) {
          var delegateResult = maybeInvokeDelegate(delegate, context);
          if (delegateResult) {
            if (delegateResult === ContinueSentinel) continue;
            return delegateResult;
          }
        }
        if (context.method === "next") {
          // Setting context._sent for legacy support of Babel's
          // function.sent implementation.
          context.sent = context._sent = context.arg;
        } else if (context.method === "throw") {
          if (state === GenStateSuspendedStart) {
            state = GenStateCompleted;
            throw context.arg;
          }
          context.dispatchException(context.arg);
        } else if (context.method === "return") {
          context.abrupt("return", context.arg);
        }
        state = GenStateExecuting;
        var record = tryCatch(innerFn, self, context);
        if (record.type === "normal") {
          // If an exception is thrown from innerFn, we leave state ===
          // GenStateExecuting and loop back for another invocation.
          state = context.done ? GenStateCompleted : GenStateSuspendedYield;
          if (record.arg === ContinueSentinel) {
            continue;
          }
          return {
            value: record.arg,
            done: context.done
          };
        } else if (record.type === "throw") {
          state = GenStateCompleted;
          // Dispatch the exception by looping back around to the
          // context.dispatchException(context.arg) call above.
          context.method = "throw";
          context.arg = record.arg;
        }
      }
    };
  }

  // Call delegate.iterator[context.method](context.arg) and handle the
  // result, either by returning a { value, done } result from the
  // delegate iterator, or by modifying context.method and context.arg,
  // setting context.delegate to null, and returning the ContinueSentinel.
  function maybeInvokeDelegate(delegate, context) {
    var method = delegate.iterator[context.method];
    if (method === undefined) {
      // A .throw or .return when the delegate iterator has no .throw
      // method always terminates the yield* loop.
      context.delegate = null;
      if (context.method === "throw") {
        if (delegate.iterator["return"]) {
          // If the delegate iterator has a return method, give it a
          // chance to clean up.
          context.method = "return";
          context.arg = undefined;
          maybeInvokeDelegate(delegate, context);
          if (context.method === "throw") {
            // If maybeInvokeDelegate(context) changed context.method from
            // "return" to "throw", let that override the TypeError below.
            return ContinueSentinel;
          }
        }
        context.method = "throw";
        context.arg = new TypeError("The iterator does not provide a 'throw' method");
      }
      return ContinueSentinel;
    }
    var record = tryCatch(method, delegate.iterator, context.arg);
    if (record.type === "throw") {
      context.method = "throw";
      context.arg = record.arg;
      context.delegate = null;
      return ContinueSentinel;
    }
    var info = record.arg;
    if (!info) {
      context.method = "throw";
      context.arg = new TypeError("iterator result is not an object");
      context.delegate = null;
      return ContinueSentinel;
    }
    if (info.done) {
      // Assign the result of the finished delegate to the temporary
      // variable specified by delegate.resultName (see delegateYield).
      context[delegate.resultName] = info.value;

      // Resume execution at the desired location (see delegateYield).
      context.next = delegate.nextLoc;

      // If context.method was "throw" but the delegate handled the
      // exception, let the outer generator proceed normally. If
      // context.method was "next", forget context.arg since it has been
      // "consumed" by the delegate iterator. If context.method was
      // "return", allow the original .return call to continue in the
      // outer generator.
      if (context.method !== "return") {
        context.method = "next";
        context.arg = undefined;
      }
    } else {
      // Re-yield the result returned by the delegate method.
      return info;
    }

    // The delegate iterator is finished, so forget it and continue with
    // the outer generator.
    context.delegate = null;
    return ContinueSentinel;
  }

  // Define Generator.prototype.{next,throw,return} in terms of the
  // unified ._invoke helper method.
  defineIteratorMethods(Gp);
  Gp[toStringTagSymbol] = "Generator";

  // A Generator should always return itself as the iterator object when the
  // @@iterator function is called on it. Some browsers' implementations of the
  // iterator prototype chain incorrectly implement this, causing the Generator
  // object to not be returned from this call. This ensures that doesn't happen.
  // See https://github.com/facebook/regenerator/issues/274 for more details.
  Gp[iteratorSymbol] = function () {
    return this;
  };
  Gp.toString = function () {
    return "[object Generator]";
  };
  function pushTryEntry(locs) {
    var entry = {
      tryLoc: locs[0]
    };
    if (1 in locs) {
      entry.catchLoc = locs[1];
    }
    if (2 in locs) {
      entry.finallyLoc = locs[2];
      entry.afterLoc = locs[3];
    }
    this.tryEntries.push(entry);
  }
  function resetTryEntry(entry) {
    var record = entry.completion || {};
    record.type = "normal";
    delete record.arg;
    entry.completion = record;
  }
  function Context(tryLocsList) {
    // The root entry object (effectively a try statement without a catch
    // or a finally block) gives us a place to store values thrown from
    // locations where there is no enclosing try statement.
    this.tryEntries = [{
      tryLoc: "root"
    }];
    tryLocsList.forEach(pushTryEntry, this);
    this.reset(true);
  }
  runtime.keys = function (object) {
    var keys = [];
    for (var key in object) {
      keys.push(key);
    }
    keys.reverse();

    // Rather than returning an object with a next method, we keep
    // things simple and return the next function itself.
    return function next() {
      while (keys.length) {
        var key = keys.pop();
        if (key in object) {
          next.value = key;
          next.done = false;
          return next;
        }
      }

      // To avoid creating an additional object, we just hang the .value
      // and .done properties off the next function object itself. This
      // also ensures that the minifier will not anonymize the function.
      next.done = true;
      return next;
    };
  };
  function values(iterable) {
    if (iterable) {
      var iteratorMethod = iterable[iteratorSymbol];
      if (iteratorMethod) {
        return iteratorMethod.call(iterable);
      }
      if (typeof iterable.next === "function") {
        return iterable;
      }
      if (!isNaN(iterable.length)) {
        var i = -1,
          next = function next() {
            while (++i < iterable.length) {
              if (hasOwn.call(iterable, i)) {
                next.value = iterable[i];
                next.done = false;
                return next;
              }
            }
            next.value = undefined;
            next.done = true;
            return next;
          };
        return next.next = next;
      }
    }

    // Return an iterator with no values.
    return {
      next: doneResult
    };
  }
  runtime.values = values;
  function doneResult() {
    return {
      value: undefined,
      done: true
    };
  }
  Context.prototype = {
    constructor: Context,
    reset: function reset(skipTempReset) {
      this.prev = 0;
      this.next = 0;
      // Resetting context._sent for legacy support of Babel's
      // function.sent implementation.
      this.sent = this._sent = undefined;
      this.done = false;
      this.delegate = null;
      this.method = "next";
      this.arg = undefined;
      this.tryEntries.forEach(resetTryEntry);
      if (!skipTempReset) {
        for (var name in this) {
          // Not sure about the optimal order of these conditions:
          if (name.charAt(0) === "t" && hasOwn.call(this, name) && !isNaN(+name.slice(1))) {
            this[name] = undefined;
          }
        }
      }
    },
    stop: function stop() {
      this.done = true;
      var rootEntry = this.tryEntries[0];
      var rootRecord = rootEntry.completion;
      if (rootRecord.type === "throw") {
        throw rootRecord.arg;
      }
      return this.rval;
    },
    dispatchException: function dispatchException(exception) {
      if (this.done) {
        throw exception;
      }
      var context = this;
      function handle(loc, caught) {
        record.type = "throw";
        record.arg = exception;
        context.next = loc;
        if (caught) {
          // If the dispatched exception was caught by a catch block,
          // then let that catch block handle the exception normally.
          context.method = "next";
          context.arg = undefined;
        }
        return !!caught;
      }
      for (var i = this.tryEntries.length - 1; i >= 0; --i) {
        var entry = this.tryEntries[i];
        var record = entry.completion;
        if (entry.tryLoc === "root") {
          // Exception thrown outside of any try block that could handle
          // it, so set the completion value of the entire function to
          // throw the exception.
          return handle("end");
        }
        if (entry.tryLoc <= this.prev) {
          var hasCatch = hasOwn.call(entry, "catchLoc");
          var hasFinally = hasOwn.call(entry, "finallyLoc");
          if (hasCatch && hasFinally) {
            if (this.prev < entry.catchLoc) {
              return handle(entry.catchLoc, true);
            } else if (this.prev < entry.finallyLoc) {
              return handle(entry.finallyLoc);
            }
          } else if (hasCatch) {
            if (this.prev < entry.catchLoc) {
              return handle(entry.catchLoc, true);
            }
          } else if (hasFinally) {
            if (this.prev < entry.finallyLoc) {
              return handle(entry.finallyLoc);
            }
          } else {
            throw new Error("try statement without catch or finally");
          }
        }
      }
    },
    abrupt: function abrupt(type, arg) {
      for (var i = this.tryEntries.length - 1; i >= 0; --i) {
        var entry = this.tryEntries[i];
        if (entry.tryLoc <= this.prev && hasOwn.call(entry, "finallyLoc") && this.prev < entry.finallyLoc) {
          var finallyEntry = entry;
          break;
        }
      }
      if (finallyEntry && (type === "break" || type === "continue") && finallyEntry.tryLoc <= arg && arg <= finallyEntry.finallyLoc) {
        // Ignore the finally entry if control is not jumping to a
        // location outside the try/catch block.
        finallyEntry = null;
      }
      var record = finallyEntry ? finallyEntry.completion : {};
      record.type = type;
      record.arg = arg;
      if (finallyEntry) {
        this.method = "next";
        this.next = finallyEntry.finallyLoc;
        return ContinueSentinel;
      }
      return this.complete(record);
    },
    complete: function complete(record, afterLoc) {
      if (record.type === "throw") {
        throw record.arg;
      }
      if (record.type === "break" || record.type === "continue") {
        this.next = record.arg;
      } else if (record.type === "return") {
        this.rval = this.arg = record.arg;
        this.method = "return";
        this.next = "end";
      } else if (record.type === "normal" && afterLoc) {
        this.next = afterLoc;
      }
      return ContinueSentinel;
    },
    finish: function finish(finallyLoc) {
      for (var i = this.tryEntries.length - 1; i >= 0; --i) {
        var entry = this.tryEntries[i];
        if (entry.finallyLoc === finallyLoc) {
          this.complete(entry.completion, entry.afterLoc);
          resetTryEntry(entry);
          return ContinueSentinel;
        }
      }
    },
    "catch": function _catch(tryLoc) {
      for (var i = this.tryEntries.length - 1; i >= 0; --i) {
        var entry = this.tryEntries[i];
        if (entry.tryLoc === tryLoc) {
          var record = entry.completion;
          if (record.type === "throw") {
            var thrown = record.arg;
            resetTryEntry(entry);
          }
          return thrown;
        }
      }

      // The context.catch method must only be called with a location
      // argument that corresponds to a known catch block.
      throw new Error("illegal catch attempt");
    },
    delegateYield: function delegateYield(iterable, resultName, nextLoc) {
      this.delegate = {
        iterator: values(iterable),
        resultName: resultName,
        nextLoc: nextLoc
      };
      if (this.method === "next") {
        // Deliberately forget the last sent value so that we don't
        // accidentally pass it on to the delegate.
        this.arg = undefined;
      }
      return ContinueSentinel;
    }
  };
}(
// Among the various tricks for obtaining a reference to the global
// object, this seems to be the most reliable technique that does not
// use indirect eval (which violates Content Security Policy).
(typeof __webpack_require__.g === "undefined" ? "undefined" : _typeof(__webpack_require__.g)) === "object" ? __webpack_require__.g : (typeof window === "undefined" ? "undefined" : _typeof(window)) === "object" ? window : (typeof self === "undefined" ? "undefined" : _typeof(self)) === "object" ? self : this);

/***/ }),

/***/ 6482:
/***/ ((module, __unused_webpack_exports, __webpack_require__) => {

function _createForOfIteratorHelper(o, allowArrayLike) { var it = typeof Symbol !== "undefined" && o[Symbol.iterator] || o["@@iterator"]; if (!it) { if (Array.isArray(o) || (it = _unsupportedIterableToArray(o)) || allowArrayLike && o && typeof o.length === "number") { if (it) o = it; var i = 0; var F = function F() {}; return { s: F, n: function n() { if (i >= o.length) return { done: true }; return { done: false, value: o[i++] }; }, e: function e(_e) { throw _e; }, f: F }; } throw new TypeError("Invalid attempt to iterate non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method."); } var normalCompletion = true, didErr = false, err; return { s: function s() { it = it.call(o); }, n: function n() { var step = it.next(); normalCompletion = step.done; return step; }, e: function e(_e2) { didErr = true; err = _e2; }, f: function f() { try { if (!normalCompletion && it["return"] != null) it["return"](); } finally { if (didErr) throw err; } } }; }
function _unsupportedIterableToArray(o, minLen) { if (!o) return; if (typeof o === "string") return _arrayLikeToArray(o, minLen); var n = Object.prototype.toString.call(o).slice(8, -1); if (n === "Object" && o.constructor) n = o.constructor.name; if (n === "Map" || n === "Set") return Array.from(o); if (n === "Arguments" || /^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(n)) return _arrayLikeToArray(o, minLen); }
function _arrayLikeToArray(arr, len) { if (len == null || len > arr.length) len = arr.length; for (var i = 0, arr2 = new Array(len); i < len; i++) { arr2[i] = arr[i]; } return arr2; }
var htmlparser = __webpack_require__(6124);
var escapeStringRegexp = __webpack_require__(432);
var _require = __webpack_require__(4281),
  isPlainObject = _require.isPlainObject;
var deepmerge = __webpack_require__(4036);
var parseSrcset = __webpack_require__(2134);
var _require2 = __webpack_require__(7866),
  postcssParse = _require2.parse;
// Tags that can conceivably represent stand-alone media.
var mediaTags = ['img', 'audio', 'video', 'picture', 'svg', 'object', 'map', 'iframe', 'embed'];
// Tags that are inherently vulnerable to being used in XSS attacks.
var vulnerableTags = ['script', 'style'];
function each(obj, cb) {
  if (obj) {
    Object.keys(obj).forEach(function (key) {
      cb(obj[key], key);
    });
  }
}

// Avoid false positives with .__proto__, .hasOwnProperty, etc.
function has(obj, key) {
  return {}.hasOwnProperty.call(obj, key);
}

// Returns those elements of `a` for which `cb(a)` returns truthy
function filter(a, cb) {
  var n = [];
  each(a, function (v) {
    if (cb(v)) {
      n.push(v);
    }
  });
  return n;
}
function isEmptyObject(obj) {
  for (var key in obj) {
    if (has(obj, key)) {
      return false;
    }
  }
  return true;
}
function stringifySrcset(parsedSrcset) {
  return parsedSrcset.map(function (part) {
    if (!part.url) {
      throw new Error('URL missing');
    }
    return part.url + (part.w ? " ".concat(part.w, "w") : '') + (part.h ? " ".concat(part.h, "h") : '') + (part.d ? " ".concat(part.d, "x") : '');
  }).join(', ');
}
module.exports = sanitizeHtml;

// A valid attribute name.
// We use a tolerant definition based on the set of strings defined by
// html.spec.whatwg.org/multipage/parsing.html#before-attribute-name-state
// and html.spec.whatwg.org/multipage/parsing.html#attribute-name-state .
// The characters accepted are ones which can be appended to the attribute
// name buffer without triggering a parse error:
//   * unexpected-equals-sign-before-attribute-name
//   * unexpected-null-character
//   * unexpected-character-in-attribute-name
// We exclude the empty string because it's impossible to get to the after
// attribute name state with an empty attribute name buffer.
var VALID_HTML_ATTRIBUTE_NAME = /^[^\0\t\n\f\r /<=>]+$/;

// Ignore the _recursing flag; it's there for recursive
// invocation as a guard against this exploit:
// https://github.com/fb55/htmlparser2/issues/105

function sanitizeHtml(html, options, _recursing) {
  if (html == null) {
    return '';
  }
  var result = '';
  // Used for hot swapping the result variable with an empty string in order to "capture" the text written to it.
  var tempResult = '';
  function Frame(tag, attribs) {
    var that = this;
    this.tag = tag;
    this.attribs = attribs || {};
    this.tagPosition = result.length;
    this.text = ''; // Node inner text
    this.mediaChildren = [];
    this.updateParentNodeText = function () {
      if (stack.length) {
        var parentFrame = stack[stack.length - 1];
        parentFrame.text += that.text;
      }
    };
    this.updateParentNodeMediaChildren = function () {
      if (stack.length && mediaTags.includes(this.tag)) {
        var parentFrame = stack[stack.length - 1];
        parentFrame.mediaChildren.push(this.tag);
      }
    };
  }
  options = Object.assign({}, sanitizeHtml.defaults, options);
  options.parser = Object.assign({}, htmlParserDefaults, options.parser);

  // vulnerableTags
  vulnerableTags.forEach(function (tag) {
    if (options.allowedTags && options.allowedTags.indexOf(tag) > -1 && !options.allowVulnerableTags) {
      console.warn("\n\n\u26A0\uFE0F Your `allowedTags` option includes, `".concat(tag, "`, which is inherently\nvulnerable to XSS attacks. Please remove it from `allowedTags`.\nOr, to disable this warning, add the `allowVulnerableTags` option\nand ensure you are accounting for this risk.\n\n"));
    }
  });

  // Tags that contain something other than HTML, or where discarding
  // the text when the tag is disallowed makes sense for other reasons.
  // If we are not allowing these tags, we should drop their content too.
  // For other tags you would drop the tag but keep its content.
  var nonTextTagsArray = options.nonTextTags || ['script', 'style', 'textarea', 'option'];
  var allowedAttributesMap;
  var allowedAttributesGlobMap;
  if (options.allowedAttributes) {
    allowedAttributesMap = {};
    allowedAttributesGlobMap = {};
    each(options.allowedAttributes, function (attributes, tag) {
      allowedAttributesMap[tag] = [];
      var globRegex = [];
      attributes.forEach(function (obj) {
        if (typeof obj === 'string' && obj.indexOf('*') >= 0) {
          globRegex.push(escapeStringRegexp(obj).replace(/\\\*/g, '.*'));
        } else {
          allowedAttributesMap[tag].push(obj);
        }
      });
      if (globRegex.length) {
        allowedAttributesGlobMap[tag] = new RegExp('^(' + globRegex.join('|') + ')$');
      }
    });
  }
  var allowedClassesMap = {};
  var allowedClassesGlobMap = {};
  each(options.allowedClasses, function (classes, tag) {
    // Implicitly allows the class attribute
    if (allowedAttributesMap) {
      if (!has(allowedAttributesMap, tag)) {
        allowedAttributesMap[tag] = [];
      }
      allowedAttributesMap[tag].push('class');
    }
    allowedClassesMap[tag] = [];
    var globRegex = [];
    classes.forEach(function (obj) {
      if (typeof obj === 'string' && obj.indexOf('*') >= 0) {
        globRegex.push(escapeStringRegexp(obj).replace(/\\\*/g, '.*'));
      } else {
        allowedClassesMap[tag].push(obj);
      }
    });
    if (globRegex.length) {
      allowedClassesGlobMap[tag] = new RegExp('^(' + globRegex.join('|') + ')$');
    }
  });
  var transformTagsMap = {};
  var transformTagsAll;
  each(options.transformTags, function (transform, tag) {
    var transFun;
    if (typeof transform === 'function') {
      transFun = transform;
    } else if (typeof transform === 'string') {
      transFun = sanitizeHtml.simpleTransform(transform);
    }
    if (tag === '*') {
      transformTagsAll = transFun;
    } else {
      transformTagsMap[tag] = transFun;
    }
  });
  var depth;
  var stack;
  var skipMap;
  var transformMap;
  var skipText;
  var skipTextDepth;
  var addedText = false;
  initializeState();
  var parser = new htmlparser.Parser({
    onopentag: function onopentag(name, attribs) {
      // If `enforceHtmlBoundary` is `true` and this has found the opening
      // `html` tag, reset the state.
      if (options.enforceHtmlBoundary && name === 'html') {
        initializeState();
      }
      if (skipText) {
        skipTextDepth++;
        return;
      }
      var frame = new Frame(name, attribs);
      stack.push(frame);
      var skip = false;
      var hasText = !!frame.text;
      var transformedTag;
      if (has(transformTagsMap, name)) {
        transformedTag = transformTagsMap[name](name, attribs);
        frame.attribs = attribs = transformedTag.attribs;
        if (transformedTag.text !== undefined) {
          frame.innerText = transformedTag.text;
        }
        if (name !== transformedTag.tagName) {
          frame.name = name = transformedTag.tagName;
          transformMap[depth] = transformedTag.tagName;
        }
      }
      if (transformTagsAll) {
        transformedTag = transformTagsAll(name, attribs);
        frame.attribs = attribs = transformedTag.attribs;
        if (name !== transformedTag.tagName) {
          frame.name = name = transformedTag.tagName;
          transformMap[depth] = transformedTag.tagName;
        }
      }
      if (options.allowedTags && options.allowedTags.indexOf(name) === -1 || options.disallowedTagsMode === 'recursiveEscape' && !isEmptyObject(skipMap) || options.nestingLimit != null && depth >= options.nestingLimit) {
        skip = true;
        skipMap[depth] = true;
        if (options.disallowedTagsMode === 'discard') {
          if (nonTextTagsArray.indexOf(name) !== -1) {
            skipText = true;
            skipTextDepth = 1;
          }
        }
        skipMap[depth] = true;
      }
      depth++;
      if (skip) {
        if (options.disallowedTagsMode === 'discard') {
          // We want the contents but not this tag
          return;
        }
        tempResult = result;
        result = '';
      }
      result += '<' + name;
      if (name === 'script') {
        if (options.allowedScriptHostnames || options.allowedScriptDomains) {
          frame.innerText = '';
        }
      }
      if (!allowedAttributesMap || has(allowedAttributesMap, name) || allowedAttributesMap['*']) {
        each(attribs, function (value, a) {
          if (!VALID_HTML_ATTRIBUTE_NAME.test(a)) {
            // This prevents part of an attribute name in the output from being
            // interpreted as the end of an attribute, or end of a tag.
            delete frame.attribs[a];
            return;
          }
          var parsed;
          // check allowedAttributesMap for the element and attribute and modify the value
          // as necessary if there are specific values defined.
          var passedAllowedAttributesMapCheck = false;
          if (!allowedAttributesMap || has(allowedAttributesMap, name) && allowedAttributesMap[name].indexOf(a) !== -1 || allowedAttributesMap['*'] && allowedAttributesMap['*'].indexOf(a) !== -1 || has(allowedAttributesGlobMap, name) && allowedAttributesGlobMap[name].test(a) || allowedAttributesGlobMap['*'] && allowedAttributesGlobMap['*'].test(a)) {
            passedAllowedAttributesMapCheck = true;
          } else if (allowedAttributesMap && allowedAttributesMap[name]) {
            var _iterator = _createForOfIteratorHelper(allowedAttributesMap[name]),
              _step;
            try {
              for (_iterator.s(); !(_step = _iterator.n()).done;) {
                var o = _step.value;
                if (isPlainObject(o) && o.name && o.name === a) {
                  passedAllowedAttributesMapCheck = true;
                  var newValue = '';
                  if (o.multiple === true) {
                    // verify the values that are allowed
                    var splitStrArray = value.split(' ');
                    var _iterator2 = _createForOfIteratorHelper(splitStrArray),
                      _step2;
                    try {
                      for (_iterator2.s(); !(_step2 = _iterator2.n()).done;) {
                        var s = _step2.value;
                        if (o.values.indexOf(s) !== -1) {
                          if (newValue === '') {
                            newValue = s;
                          } else {
                            newValue += ' ' + s;
                          }
                        }
                      }
                    } catch (err) {
                      _iterator2.e(err);
                    } finally {
                      _iterator2.f();
                    }
                  } else if (o.values.indexOf(value) >= 0) {
                    // verified an allowed value matches the entire attribute value
                    newValue = value;
                  }
                  value = newValue;
                }
              }
            } catch (err) {
              _iterator.e(err);
            } finally {
              _iterator.f();
            }
          }
          if (passedAllowedAttributesMapCheck) {
            if (options.allowedSchemesAppliedToAttributes.indexOf(a) !== -1) {
              if (naughtyHref(name, value)) {
                delete frame.attribs[a];
                return;
              }
            }
            if (name === 'script' && a === 'src') {
              var allowed = true;
              try {
                var _parsed = new URL(value);
                if (options.allowedScriptHostnames || options.allowedScriptDomains) {
                  var allowedHostname = (options.allowedScriptHostnames || []).find(function (hostname) {
                    return hostname === _parsed.hostname;
                  });
                  var allowedDomain = (options.allowedScriptDomains || []).find(function (domain) {
                    return _parsed.hostname === domain || _parsed.hostname.endsWith(".".concat(domain));
                  });
                  allowed = allowedHostname || allowedDomain;
                }
              } catch (e) {
                allowed = false;
              }
              if (!allowed) {
                delete frame.attribs[a];
                return;
              }
            }
            if (name === 'iframe' && a === 'src') {
              var _allowed = true;
              try {
                // Chrome accepts \ as a substitute for / in the // at the
                // start of a URL, so rewrite accordingly to prevent exploit.
                // Also drop any whitespace at that point in the URL
                value = value.replace(/^(\w+:)?\s*[\\/]\s*[\\/]/, '$1//');
                if (value.startsWith('relative:')) {
                  // An attempt to exploit our workaround for base URLs being
                  // mandatory for relative URL validation in the WHATWG
                  // URL parser, reject it
                  throw new Error('relative: exploit attempt');
                }
                // naughtyHref is in charge of whether protocol relative URLs
                // are cool. Here we are concerned just with allowed hostnames and
                // whether to allow relative URLs.
                //
                // Build a placeholder "base URL" against which any reasonable
                // relative URL may be parsed successfully
                var base = 'relative://relative-site';
                for (var i = 0; i < 100; i++) {
                  base += "/".concat(i);
                }
                var _parsed2 = new URL(value, base);
                var isRelativeUrl = _parsed2 && _parsed2.hostname === 'relative-site' && _parsed2.protocol === 'relative:';
                if (isRelativeUrl) {
                  // default value of allowIframeRelativeUrls is true
                  // unless allowedIframeHostnames or allowedIframeDomains specified
                  _allowed = has(options, 'allowIframeRelativeUrls') ? options.allowIframeRelativeUrls : !options.allowedIframeHostnames && !options.allowedIframeDomains;
                } else if (options.allowedIframeHostnames || options.allowedIframeDomains) {
                  var _allowedHostname = (options.allowedIframeHostnames || []).find(function (hostname) {
                    return hostname === _parsed2.hostname;
                  });
                  var _allowedDomain = (options.allowedIframeDomains || []).find(function (domain) {
                    return _parsed2.hostname === domain || _parsed2.hostname.endsWith(".".concat(domain));
                  });
                  _allowed = _allowedHostname || _allowedDomain;
                }
              } catch (e) {
                // Unparseable iframe src
                _allowed = false;
              }
              if (!_allowed) {
                delete frame.attribs[a];
                return;
              }
            }
            if (a === 'srcset') {
              try {
                parsed = parseSrcset(value);
                parsed.forEach(function (value) {
                  if (naughtyHref('srcset', value.url)) {
                    value.evil = true;
                  }
                });
                parsed = filter(parsed, function (v) {
                  return !v.evil;
                });
                if (!parsed.length) {
                  delete frame.attribs[a];
                  return;
                } else {
                  value = stringifySrcset(filter(parsed, function (v) {
                    return !v.evil;
                  }));
                  frame.attribs[a] = value;
                }
              } catch (e) {
                // Unparseable srcset
                delete frame.attribs[a];
                return;
              }
            }
            if (a === 'class') {
              var allowedSpecificClasses = allowedClassesMap[name];
              var allowedWildcardClasses = allowedClassesMap['*'];
              var allowedSpecificClassesGlob = allowedClassesGlobMap[name];
              var allowedWildcardClassesGlob = allowedClassesGlobMap['*'];
              var allowedClassesGlobs = [allowedSpecificClassesGlob, allowedWildcardClassesGlob].filter(function (t) {
                return t;
              });
              if (allowedSpecificClasses && allowedWildcardClasses) {
                value = filterClasses(value, deepmerge(allowedSpecificClasses, allowedWildcardClasses), allowedClassesGlobs);
              } else {
                value = filterClasses(value, allowedSpecificClasses || allowedWildcardClasses, allowedClassesGlobs);
              }
              if (!value.length) {
                delete frame.attribs[a];
                return;
              }
            }
            if (a === 'style') {
              try {
                var abstractSyntaxTree = postcssParse(name + ' {' + value + '}');
                var filteredAST = filterCss(abstractSyntaxTree, options.allowedStyles);
                value = stringifyStyleAttributes(filteredAST);
                if (value.length === 0) {
                  delete frame.attribs[a];
                  return;
                }
              } catch (e) {
                delete frame.attribs[a];
                return;
              }
            }
            result += ' ' + a;
            if (value && value.length) {
              result += '="' + escapeHtml(value, true) + '"';
            }
          } else {
            delete frame.attribs[a];
          }
        });
      }
      if (options.selfClosing.indexOf(name) !== -1) {
        result += ' />';
      } else {
        result += '>';
        if (frame.innerText && !hasText && !options.textFilter) {
          result += escapeHtml(frame.innerText);
          addedText = true;
        }
      }
      if (skip) {
        result = tempResult + escapeHtml(result);
        tempResult = '';
      }
    },
    ontext: function ontext(text) {
      if (skipText) {
        return;
      }
      var lastFrame = stack[stack.length - 1];
      var tag;
      if (lastFrame) {
        tag = lastFrame.tag;
        // If inner text was set by transform function then let's use it
        text = lastFrame.innerText !== undefined ? lastFrame.innerText : text;
      }
      if (options.disallowedTagsMode === 'discard' && (tag === 'script' || tag === 'style')) {
        // htmlparser2 gives us these as-is. Escaping them ruins the content. Allowing
        // script tags is, by definition, game over for XSS protection, so if that's
        // your concern, don't allow them. The same is essentially true for style tags
        // which have their own collection of XSS vectors.
        result += text;
      } else {
        var escaped = escapeHtml(text, false);
        if (options.textFilter && !addedText) {
          result += options.textFilter(escaped, tag);
        } else if (!addedText) {
          result += escaped;
        }
      }
      if (stack.length) {
        var frame = stack[stack.length - 1];
        frame.text += text;
      }
    },
    onclosetag: function onclosetag(name) {
      if (skipText) {
        skipTextDepth--;
        if (!skipTextDepth) {
          skipText = false;
        } else {
          return;
        }
      }
      var frame = stack.pop();
      if (!frame) {
        // Do not crash on bad markup
        return;
      }
      skipText = options.enforceHtmlBoundary ? name === 'html' : false;
      depth--;
      var skip = skipMap[depth];
      if (skip) {
        delete skipMap[depth];
        if (options.disallowedTagsMode === 'discard') {
          frame.updateParentNodeText();
          return;
        }
        tempResult = result;
        result = '';
      }
      if (transformMap[depth]) {
        name = transformMap[depth];
        delete transformMap[depth];
      }
      if (options.exclusiveFilter && options.exclusiveFilter(frame)) {
        result = result.substr(0, frame.tagPosition);
        return;
      }
      frame.updateParentNodeMediaChildren();
      frame.updateParentNodeText();
      if (options.selfClosing.indexOf(name) !== -1) {
        // Already output />
        if (skip) {
          result = tempResult;
          tempResult = '';
        }
        return;
      }
      result += '</' + name + '>';
      if (skip) {
        result = tempResult + escapeHtml(result);
        tempResult = '';
      }
    }
  }, options.parser);
  parser.write(html);
  parser.end();
  return result;
  function initializeState() {
    result = '';
    depth = 0;
    stack = [];
    skipMap = {};
    transformMap = {};
    skipText = false;
    skipTextDepth = 0;
  }
  function escapeHtml(s, quote) {
    if (typeof s !== 'string') {
      s = s + '';
    }
    if (options.parser.decodeEntities) {
      s = s.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
      if (quote) {
        s = s.replace(/"/g, '&quot;');
      }
    }
    // TODO: this is inadequate because it will pass `&0;`. This approach
    // will not work, each & must be considered with regard to whether it
    // is followed by a 100% syntactically valid entity or not, and escaped
    // if it is not. If this bothers you, don't set parser.decodeEntities
    // to false. (The default is true.)
    s = s.replace(/&(?![a-zA-Z0-9#]{1,20};)/g, '&amp;') // Match ampersands not part of existing HTML entity
    .replace(/</g, '&lt;').replace(/>/g, '&gt;');
    if (quote) {
      s = s.replace(/"/g, '&quot;');
    }
    return s;
  }
  function naughtyHref(name, href) {
    // Browsers ignore character codes of 32 (space) and below in a surprising
    // number of situations. Start reading here:
    // https://www.owasp.org/index.php/XSS_Filter_Evasion_Cheat_Sheet#Embedded_tab
    // eslint-disable-next-line no-control-regex
    href = href.replace(/[\x00-\x20]+/g, '');
    // Clobber any comments in URLs, which the browser might
    // interpret inside an XML data island, allowing
    // a javascript: URL to be snuck through
    href = href.replace(/<!--.*?-->/g, '');
    // Case insensitive so we don't get faked out by JAVASCRIPT #1
    // Allow more characters after the first so we don't get faked
    // out by certain schemes browsers accept
    var matches = href.match(/^([a-zA-Z][a-zA-Z0-9.\-+]*):/);
    if (!matches) {
      // Protocol-relative URL starting with any combination of '/' and '\'
      if (href.match(/^[/\\]{2}/)) {
        return !options.allowProtocolRelative;
      }

      // No scheme
      return false;
    }
    var scheme = matches[1].toLowerCase();
    if (has(options.allowedSchemesByTag, name)) {
      return options.allowedSchemesByTag[name].indexOf(scheme) === -1;
    }
    return !options.allowedSchemes || options.allowedSchemes.indexOf(scheme) === -1;
  }

  /**
   * Filters user input css properties by allowlisted regex attributes.
   * Modifies the abstractSyntaxTree object.
   *
   * @param {object} abstractSyntaxTree  - Object representation of CSS attributes.
   * @property {array[Declaration]} abstractSyntaxTree.nodes[0] - Each object cointains prop and value key, i.e { prop: 'color', value: 'red' }.
   * @param {object} allowedStyles       - Keys are properties (i.e color), value is list of permitted regex rules (i.e /green/i).
   * @return {object}                    - The modified tree.
   */
  function filterCss(abstractSyntaxTree, allowedStyles) {
    if (!allowedStyles) {
      return abstractSyntaxTree;
    }
    var astRules = abstractSyntaxTree.nodes[0];
    var selectedRule;

    // Merge global and tag-specific styles into new AST.
    if (allowedStyles[astRules.selector] && allowedStyles['*']) {
      selectedRule = deepmerge(allowedStyles[astRules.selector], allowedStyles['*']);
    } else {
      selectedRule = allowedStyles[astRules.selector] || allowedStyles['*'];
    }
    if (selectedRule) {
      abstractSyntaxTree.nodes[0].nodes = astRules.nodes.reduce(filterDeclarations(selectedRule), []);
    }
    return abstractSyntaxTree;
  }

  /**
   * Extracts the style attribues from an AbstractSyntaxTree and formats those
   * values in the inline style attribute format.
   *
   * @param  {AbstractSyntaxTree} filteredAST
   * @return {string}             - Example: "color:yellow;text-align:center;font-family:helvetica;"
   */
  function stringifyStyleAttributes(filteredAST) {
    return filteredAST.nodes[0].nodes.reduce(function (extractedAttributes, attributeObject) {
      extractedAttributes.push(attributeObject.prop + ':' + attributeObject.value);
      return extractedAttributes;
    }, []).join(';');
  }

  /**
    * Filters the existing attributes for the given property. Discards any attributes
    * which don't match the allowlist.
    *
    * @param  {object} selectedRule             - Example: { color: red, font-family: helvetica }
    * @param  {array} allowedDeclarationsList   - List of declarations which pass the allowlist.
    * @param  {object} attributeObject          - Object representing the current css property.
    * @property {string} attributeObject.type   - Typically 'declaration'.
    * @property {string} attributeObject.prop   - The CSS property, i.e 'color'.
    * @property {string} attributeObject.value  - The corresponding value to the css property, i.e 'red'.
    * @return {function}                        - When used in Array.reduce, will return an array of Declaration objects
    */
  function filterDeclarations(selectedRule) {
    return function (allowedDeclarationsList, attributeObject) {
      // If this property is allowlisted...
      if (has(selectedRule, attributeObject.prop)) {
        var matchesRegex = selectedRule[attributeObject.prop].some(function (regularExpression) {
          return regularExpression.test(attributeObject.value);
        });
        if (matchesRegex) {
          allowedDeclarationsList.push(attributeObject);
        }
      }
      return allowedDeclarationsList;
    };
  }
  function filterClasses(classes, allowed, allowedGlobs) {
    if (!allowed) {
      // The class attribute is allowed without filtering on this tag
      return classes;
    }
    classes = classes.split(/\s+/);
    return classes.filter(function (clss) {
      return allowed.indexOf(clss) !== -1 || allowedGlobs.some(function (glob) {
        return glob.test(clss);
      });
    }).join(' ');
  }
}

// Defaults are accessible to you so that you can use them as a starting point
// programmatically if you wish

var htmlParserDefaults = {
  decodeEntities: true
};
sanitizeHtml.defaults = {
  allowedTags: [
  // Sections derived from MDN element categories and limited to the more
  // benign categories.
  // https://developer.mozilla.org/en-US/docs/Web/HTML/Element
  // Content sectioning
  'address', 'article', 'aside', 'footer', 'header', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'hgroup', 'main', 'nav', 'section',
  // Text content
  'blockquote', 'dd', 'div', 'dl', 'dt', 'figcaption', 'figure', 'hr', 'li', 'main', 'ol', 'p', 'pre', 'ul',
  // Inline text semantics
  'a', 'abbr', 'b', 'bdi', 'bdo', 'br', 'cite', 'code', 'data', 'dfn', 'em', 'i', 'kbd', 'mark', 'q', 'rb', 'rp', 'rt', 'rtc', 'ruby', 's', 'samp', 'small', 'span', 'strong', 'sub', 'sup', 'time', 'u', 'var', 'wbr',
  // Table content
  'caption', 'col', 'colgroup', 'table', 'tbody', 'td', 'tfoot', 'th', 'thead', 'tr'],
  disallowedTagsMode: 'discard',
  allowedAttributes: {
    a: ['href', 'name', 'target'],
    // We don't currently allow img itself by default, but this
    // would make sense if we did. You could add srcset here,
    // and if you do the URL is checked for safety
    img: ['src']
  },
  // Lots of these won't come up by default because we don't allow them
  selfClosing: ['img', 'br', 'hr', 'area', 'base', 'basefont', 'input', 'link', 'meta'],
  // URL schemes we permit
  allowedSchemes: ['http', 'https', 'ftp', 'mailto', 'tel'],
  allowedSchemesByTag: {},
  allowedSchemesAppliedToAttributes: ['href', 'src', 'cite'],
  allowProtocolRelative: true,
  enforceHtmlBoundary: false
};
sanitizeHtml.simpleTransform = function (newTagName, newAttribs, merge) {
  merge = merge === undefined ? true : merge;
  newAttribs = newAttribs || {};
  return function (tagName, attribs) {
    var attrib;
    if (merge) {
      for (attrib in newAttribs) {
        attribs[attrib] = newAttribs[attrib];
      }
    } else {
      attribs = newAttribs;
    }
    return {
      tagName: newTagName,
      attribs: attribs
    };
  };
};

/***/ }),

/***/ 432:
/***/ ((module) => {

"use strict";


module.exports = function (string) {
  if (typeof string !== 'string') {
    throw new TypeError('Expected a string');
  }

  // Escape characters with special meaning either inside or outside character sets.
  // Use a simple backslash escape when it’s always valid, and a \unnnn escape when the simpler form would be disallowed by Unicode patterns’ stricter grammar.
  return string.replace(/[|\\{}()[\]^$+*?.]/g, '\\$&').replace(/-/g, '\\x2d');
};

/***/ }),

/***/ 2868:
/***/ (() => {

/* (ignored) */

/***/ }),

/***/ 4777:
/***/ (() => {

/* (ignored) */

/***/ }),

/***/ 9830:
/***/ (() => {

/* (ignored) */

/***/ }),

/***/ 209:
/***/ (() => {

/* (ignored) */

/***/ }),

/***/ 7414:
/***/ (() => {

/* (ignored) */

/***/ }),

/***/ 2961:
/***/ ((module) => {

let urlAlphabet =
  'useandom-26T198340PX75pxJACKVERYMINDBUSHWOLF_GQZbfghjklqvwyzrict'
let customAlphabet = (alphabet, defaultSize = 21) => {
  return (size = defaultSize) => {
    let id = ''
    let i = size
    while (i--) {
      id += alphabet[(Math.random() * alphabet.length) | 0]
    }
    return id
  }
}
let nanoid = (size = 21) => {
  let id = ''
  let i = size
  while (i--) {
    id += urlAlphabet[(Math.random() * 64) | 0]
  }
  return id
}
module.exports = { nanoid, customAlphabet }


/***/ }),

/***/ 3600:
/***/ ((module) => {

"use strict";
module.exports = JSON.parse('{"0":65533,"128":8364,"130":8218,"131":402,"132":8222,"133":8230,"134":8224,"135":8225,"136":710,"137":8240,"138":352,"139":8249,"140":338,"142":381,"145":8216,"146":8217,"147":8220,"148":8221,"149":8226,"150":8211,"151":8212,"152":732,"153":8482,"154":353,"155":8250,"156":339,"158":382,"159":376}');

/***/ }),

/***/ 9323:
/***/ ((module) => {

"use strict";
module.exports = JSON.parse('{"Aacute":"Á","aacute":"á","Abreve":"Ă","abreve":"ă","ac":"∾","acd":"∿","acE":"∾̳","Acirc":"Â","acirc":"â","acute":"´","Acy":"А","acy":"а","AElig":"Æ","aelig":"æ","af":"⁡","Afr":"𝔄","afr":"𝔞","Agrave":"À","agrave":"à","alefsym":"ℵ","aleph":"ℵ","Alpha":"Α","alpha":"α","Amacr":"Ā","amacr":"ā","amalg":"⨿","amp":"&","AMP":"&","andand":"⩕","And":"⩓","and":"∧","andd":"⩜","andslope":"⩘","andv":"⩚","ang":"∠","ange":"⦤","angle":"∠","angmsdaa":"⦨","angmsdab":"⦩","angmsdac":"⦪","angmsdad":"⦫","angmsdae":"⦬","angmsdaf":"⦭","angmsdag":"⦮","angmsdah":"⦯","angmsd":"∡","angrt":"∟","angrtvb":"⊾","angrtvbd":"⦝","angsph":"∢","angst":"Å","angzarr":"⍼","Aogon":"Ą","aogon":"ą","Aopf":"𝔸","aopf":"𝕒","apacir":"⩯","ap":"≈","apE":"⩰","ape":"≊","apid":"≋","apos":"\'","ApplyFunction":"⁡","approx":"≈","approxeq":"≊","Aring":"Å","aring":"å","Ascr":"𝒜","ascr":"𝒶","Assign":"≔","ast":"*","asymp":"≈","asympeq":"≍","Atilde":"Ã","atilde":"ã","Auml":"Ä","auml":"ä","awconint":"∳","awint":"⨑","backcong":"≌","backepsilon":"϶","backprime":"‵","backsim":"∽","backsimeq":"⋍","Backslash":"∖","Barv":"⫧","barvee":"⊽","barwed":"⌅","Barwed":"⌆","barwedge":"⌅","bbrk":"⎵","bbrktbrk":"⎶","bcong":"≌","Bcy":"Б","bcy":"б","bdquo":"„","becaus":"∵","because":"∵","Because":"∵","bemptyv":"⦰","bepsi":"϶","bernou":"ℬ","Bernoullis":"ℬ","Beta":"Β","beta":"β","beth":"ℶ","between":"≬","Bfr":"𝔅","bfr":"𝔟","bigcap":"⋂","bigcirc":"◯","bigcup":"⋃","bigodot":"⨀","bigoplus":"⨁","bigotimes":"⨂","bigsqcup":"⨆","bigstar":"★","bigtriangledown":"▽","bigtriangleup":"△","biguplus":"⨄","bigvee":"⋁","bigwedge":"⋀","bkarow":"⤍","blacklozenge":"⧫","blacksquare":"▪","blacktriangle":"▴","blacktriangledown":"▾","blacktriangleleft":"◂","blacktriangleright":"▸","blank":"␣","blk12":"▒","blk14":"░","blk34":"▓","block":"█","bne":"=⃥","bnequiv":"≡⃥","bNot":"⫭","bnot":"⌐","Bopf":"𝔹","bopf":"𝕓","bot":"⊥","bottom":"⊥","bowtie":"⋈","boxbox":"⧉","boxdl":"┐","boxdL":"╕","boxDl":"╖","boxDL":"╗","boxdr":"┌","boxdR":"╒","boxDr":"╓","boxDR":"╔","boxh":"─","boxH":"═","boxhd":"┬","boxHd":"╤","boxhD":"╥","boxHD":"╦","boxhu":"┴","boxHu":"╧","boxhU":"╨","boxHU":"╩","boxminus":"⊟","boxplus":"⊞","boxtimes":"⊠","boxul":"┘","boxuL":"╛","boxUl":"╜","boxUL":"╝","boxur":"└","boxuR":"╘","boxUr":"╙","boxUR":"╚","boxv":"│","boxV":"║","boxvh":"┼","boxvH":"╪","boxVh":"╫","boxVH":"╬","boxvl":"┤","boxvL":"╡","boxVl":"╢","boxVL":"╣","boxvr":"├","boxvR":"╞","boxVr":"╟","boxVR":"╠","bprime":"‵","breve":"˘","Breve":"˘","brvbar":"¦","bscr":"𝒷","Bscr":"ℬ","bsemi":"⁏","bsim":"∽","bsime":"⋍","bsolb":"⧅","bsol":"\\\\","bsolhsub":"⟈","bull":"•","bullet":"•","bump":"≎","bumpE":"⪮","bumpe":"≏","Bumpeq":"≎","bumpeq":"≏","Cacute":"Ć","cacute":"ć","capand":"⩄","capbrcup":"⩉","capcap":"⩋","cap":"∩","Cap":"⋒","capcup":"⩇","capdot":"⩀","CapitalDifferentialD":"ⅅ","caps":"∩︀","caret":"⁁","caron":"ˇ","Cayleys":"ℭ","ccaps":"⩍","Ccaron":"Č","ccaron":"č","Ccedil":"Ç","ccedil":"ç","Ccirc":"Ĉ","ccirc":"ĉ","Cconint":"∰","ccups":"⩌","ccupssm":"⩐","Cdot":"Ċ","cdot":"ċ","cedil":"¸","Cedilla":"¸","cemptyv":"⦲","cent":"¢","centerdot":"·","CenterDot":"·","cfr":"𝔠","Cfr":"ℭ","CHcy":"Ч","chcy":"ч","check":"✓","checkmark":"✓","Chi":"Χ","chi":"χ","circ":"ˆ","circeq":"≗","circlearrowleft":"↺","circlearrowright":"↻","circledast":"⊛","circledcirc":"⊚","circleddash":"⊝","CircleDot":"⊙","circledR":"®","circledS":"Ⓢ","CircleMinus":"⊖","CirclePlus":"⊕","CircleTimes":"⊗","cir":"○","cirE":"⧃","cire":"≗","cirfnint":"⨐","cirmid":"⫯","cirscir":"⧂","ClockwiseContourIntegral":"∲","CloseCurlyDoubleQuote":"”","CloseCurlyQuote":"’","clubs":"♣","clubsuit":"♣","colon":":","Colon":"∷","Colone":"⩴","colone":"≔","coloneq":"≔","comma":",","commat":"@","comp":"∁","compfn":"∘","complement":"∁","complexes":"ℂ","cong":"≅","congdot":"⩭","Congruent":"≡","conint":"∮","Conint":"∯","ContourIntegral":"∮","copf":"𝕔","Copf":"ℂ","coprod":"∐","Coproduct":"∐","copy":"©","COPY":"©","copysr":"℗","CounterClockwiseContourIntegral":"∳","crarr":"↵","cross":"✗","Cross":"⨯","Cscr":"𝒞","cscr":"𝒸","csub":"⫏","csube":"⫑","csup":"⫐","csupe":"⫒","ctdot":"⋯","cudarrl":"⤸","cudarrr":"⤵","cuepr":"⋞","cuesc":"⋟","cularr":"↶","cularrp":"⤽","cupbrcap":"⩈","cupcap":"⩆","CupCap":"≍","cup":"∪","Cup":"⋓","cupcup":"⩊","cupdot":"⊍","cupor":"⩅","cups":"∪︀","curarr":"↷","curarrm":"⤼","curlyeqprec":"⋞","curlyeqsucc":"⋟","curlyvee":"⋎","curlywedge":"⋏","curren":"¤","curvearrowleft":"↶","curvearrowright":"↷","cuvee":"⋎","cuwed":"⋏","cwconint":"∲","cwint":"∱","cylcty":"⌭","dagger":"†","Dagger":"‡","daleth":"ℸ","darr":"↓","Darr":"↡","dArr":"⇓","dash":"‐","Dashv":"⫤","dashv":"⊣","dbkarow":"⤏","dblac":"˝","Dcaron":"Ď","dcaron":"ď","Dcy":"Д","dcy":"д","ddagger":"‡","ddarr":"⇊","DD":"ⅅ","dd":"ⅆ","DDotrahd":"⤑","ddotseq":"⩷","deg":"°","Del":"∇","Delta":"Δ","delta":"δ","demptyv":"⦱","dfisht":"⥿","Dfr":"𝔇","dfr":"𝔡","dHar":"⥥","dharl":"⇃","dharr":"⇂","DiacriticalAcute":"´","DiacriticalDot":"˙","DiacriticalDoubleAcute":"˝","DiacriticalGrave":"`","DiacriticalTilde":"˜","diam":"⋄","diamond":"⋄","Diamond":"⋄","diamondsuit":"♦","diams":"♦","die":"¨","DifferentialD":"ⅆ","digamma":"ϝ","disin":"⋲","div":"÷","divide":"÷","divideontimes":"⋇","divonx":"⋇","DJcy":"Ђ","djcy":"ђ","dlcorn":"⌞","dlcrop":"⌍","dollar":"$","Dopf":"𝔻","dopf":"𝕕","Dot":"¨","dot":"˙","DotDot":"⃜","doteq":"≐","doteqdot":"≑","DotEqual":"≐","dotminus":"∸","dotplus":"∔","dotsquare":"⊡","doublebarwedge":"⌆","DoubleContourIntegral":"∯","DoubleDot":"¨","DoubleDownArrow":"⇓","DoubleLeftArrow":"⇐","DoubleLeftRightArrow":"⇔","DoubleLeftTee":"⫤","DoubleLongLeftArrow":"⟸","DoubleLongLeftRightArrow":"⟺","DoubleLongRightArrow":"⟹","DoubleRightArrow":"⇒","DoubleRightTee":"⊨","DoubleUpArrow":"⇑","DoubleUpDownArrow":"⇕","DoubleVerticalBar":"∥","DownArrowBar":"⤓","downarrow":"↓","DownArrow":"↓","Downarrow":"⇓","DownArrowUpArrow":"⇵","DownBreve":"̑","downdownarrows":"⇊","downharpoonleft":"⇃","downharpoonright":"⇂","DownLeftRightVector":"⥐","DownLeftTeeVector":"⥞","DownLeftVectorBar":"⥖","DownLeftVector":"↽","DownRightTeeVector":"⥟","DownRightVectorBar":"⥗","DownRightVector":"⇁","DownTeeArrow":"↧","DownTee":"⊤","drbkarow":"⤐","drcorn":"⌟","drcrop":"⌌","Dscr":"𝒟","dscr":"𝒹","DScy":"Ѕ","dscy":"ѕ","dsol":"⧶","Dstrok":"Đ","dstrok":"đ","dtdot":"⋱","dtri":"▿","dtrif":"▾","duarr":"⇵","duhar":"⥯","dwangle":"⦦","DZcy":"Џ","dzcy":"џ","dzigrarr":"⟿","Eacute":"É","eacute":"é","easter":"⩮","Ecaron":"Ě","ecaron":"ě","Ecirc":"Ê","ecirc":"ê","ecir":"≖","ecolon":"≕","Ecy":"Э","ecy":"э","eDDot":"⩷","Edot":"Ė","edot":"ė","eDot":"≑","ee":"ⅇ","efDot":"≒","Efr":"𝔈","efr":"𝔢","eg":"⪚","Egrave":"È","egrave":"è","egs":"⪖","egsdot":"⪘","el":"⪙","Element":"∈","elinters":"⏧","ell":"ℓ","els":"⪕","elsdot":"⪗","Emacr":"Ē","emacr":"ē","empty":"∅","emptyset":"∅","EmptySmallSquare":"◻","emptyv":"∅","EmptyVerySmallSquare":"▫","emsp13":" ","emsp14":" ","emsp":" ","ENG":"Ŋ","eng":"ŋ","ensp":" ","Eogon":"Ę","eogon":"ę","Eopf":"𝔼","eopf":"𝕖","epar":"⋕","eparsl":"⧣","eplus":"⩱","epsi":"ε","Epsilon":"Ε","epsilon":"ε","epsiv":"ϵ","eqcirc":"≖","eqcolon":"≕","eqsim":"≂","eqslantgtr":"⪖","eqslantless":"⪕","Equal":"⩵","equals":"=","EqualTilde":"≂","equest":"≟","Equilibrium":"⇌","equiv":"≡","equivDD":"⩸","eqvparsl":"⧥","erarr":"⥱","erDot":"≓","escr":"ℯ","Escr":"ℰ","esdot":"≐","Esim":"⩳","esim":"≂","Eta":"Η","eta":"η","ETH":"Ð","eth":"ð","Euml":"Ë","euml":"ë","euro":"€","excl":"!","exist":"∃","Exists":"∃","expectation":"ℰ","exponentiale":"ⅇ","ExponentialE":"ⅇ","fallingdotseq":"≒","Fcy":"Ф","fcy":"ф","female":"♀","ffilig":"ﬃ","fflig":"ﬀ","ffllig":"ﬄ","Ffr":"𝔉","ffr":"𝔣","filig":"ﬁ","FilledSmallSquare":"◼","FilledVerySmallSquare":"▪","fjlig":"fj","flat":"♭","fllig":"ﬂ","fltns":"▱","fnof":"ƒ","Fopf":"𝔽","fopf":"𝕗","forall":"∀","ForAll":"∀","fork":"⋔","forkv":"⫙","Fouriertrf":"ℱ","fpartint":"⨍","frac12":"½","frac13":"⅓","frac14":"¼","frac15":"⅕","frac16":"⅙","frac18":"⅛","frac23":"⅔","frac25":"⅖","frac34":"¾","frac35":"⅗","frac38":"⅜","frac45":"⅘","frac56":"⅚","frac58":"⅝","frac78":"⅞","frasl":"⁄","frown":"⌢","fscr":"𝒻","Fscr":"ℱ","gacute":"ǵ","Gamma":"Γ","gamma":"γ","Gammad":"Ϝ","gammad":"ϝ","gap":"⪆","Gbreve":"Ğ","gbreve":"ğ","Gcedil":"Ģ","Gcirc":"Ĝ","gcirc":"ĝ","Gcy":"Г","gcy":"г","Gdot":"Ġ","gdot":"ġ","ge":"≥","gE":"≧","gEl":"⪌","gel":"⋛","geq":"≥","geqq":"≧","geqslant":"⩾","gescc":"⪩","ges":"⩾","gesdot":"⪀","gesdoto":"⪂","gesdotol":"⪄","gesl":"⋛︀","gesles":"⪔","Gfr":"𝔊","gfr":"𝔤","gg":"≫","Gg":"⋙","ggg":"⋙","gimel":"ℷ","GJcy":"Ѓ","gjcy":"ѓ","gla":"⪥","gl":"≷","glE":"⪒","glj":"⪤","gnap":"⪊","gnapprox":"⪊","gne":"⪈","gnE":"≩","gneq":"⪈","gneqq":"≩","gnsim":"⋧","Gopf":"𝔾","gopf":"𝕘","grave":"`","GreaterEqual":"≥","GreaterEqualLess":"⋛","GreaterFullEqual":"≧","GreaterGreater":"⪢","GreaterLess":"≷","GreaterSlantEqual":"⩾","GreaterTilde":"≳","Gscr":"𝒢","gscr":"ℊ","gsim":"≳","gsime":"⪎","gsiml":"⪐","gtcc":"⪧","gtcir":"⩺","gt":">","GT":">","Gt":"≫","gtdot":"⋗","gtlPar":"⦕","gtquest":"⩼","gtrapprox":"⪆","gtrarr":"⥸","gtrdot":"⋗","gtreqless":"⋛","gtreqqless":"⪌","gtrless":"≷","gtrsim":"≳","gvertneqq":"≩︀","gvnE":"≩︀","Hacek":"ˇ","hairsp":" ","half":"½","hamilt":"ℋ","HARDcy":"Ъ","hardcy":"ъ","harrcir":"⥈","harr":"↔","hArr":"⇔","harrw":"↭","Hat":"^","hbar":"ℏ","Hcirc":"Ĥ","hcirc":"ĥ","hearts":"♥","heartsuit":"♥","hellip":"…","hercon":"⊹","hfr":"𝔥","Hfr":"ℌ","HilbertSpace":"ℋ","hksearow":"⤥","hkswarow":"⤦","hoarr":"⇿","homtht":"∻","hookleftarrow":"↩","hookrightarrow":"↪","hopf":"𝕙","Hopf":"ℍ","horbar":"―","HorizontalLine":"─","hscr":"𝒽","Hscr":"ℋ","hslash":"ℏ","Hstrok":"Ħ","hstrok":"ħ","HumpDownHump":"≎","HumpEqual":"≏","hybull":"⁃","hyphen":"‐","Iacute":"Í","iacute":"í","ic":"⁣","Icirc":"Î","icirc":"î","Icy":"И","icy":"и","Idot":"İ","IEcy":"Е","iecy":"е","iexcl":"¡","iff":"⇔","ifr":"𝔦","Ifr":"ℑ","Igrave":"Ì","igrave":"ì","ii":"ⅈ","iiiint":"⨌","iiint":"∭","iinfin":"⧜","iiota":"℩","IJlig":"Ĳ","ijlig":"ĳ","Imacr":"Ī","imacr":"ī","image":"ℑ","ImaginaryI":"ⅈ","imagline":"ℐ","imagpart":"ℑ","imath":"ı","Im":"ℑ","imof":"⊷","imped":"Ƶ","Implies":"⇒","incare":"℅","in":"∈","infin":"∞","infintie":"⧝","inodot":"ı","intcal":"⊺","int":"∫","Int":"∬","integers":"ℤ","Integral":"∫","intercal":"⊺","Intersection":"⋂","intlarhk":"⨗","intprod":"⨼","InvisibleComma":"⁣","InvisibleTimes":"⁢","IOcy":"Ё","iocy":"ё","Iogon":"Į","iogon":"į","Iopf":"𝕀","iopf":"𝕚","Iota":"Ι","iota":"ι","iprod":"⨼","iquest":"¿","iscr":"𝒾","Iscr":"ℐ","isin":"∈","isindot":"⋵","isinE":"⋹","isins":"⋴","isinsv":"⋳","isinv":"∈","it":"⁢","Itilde":"Ĩ","itilde":"ĩ","Iukcy":"І","iukcy":"і","Iuml":"Ï","iuml":"ï","Jcirc":"Ĵ","jcirc":"ĵ","Jcy":"Й","jcy":"й","Jfr":"𝔍","jfr":"𝔧","jmath":"ȷ","Jopf":"𝕁","jopf":"𝕛","Jscr":"𝒥","jscr":"𝒿","Jsercy":"Ј","jsercy":"ј","Jukcy":"Є","jukcy":"є","Kappa":"Κ","kappa":"κ","kappav":"ϰ","Kcedil":"Ķ","kcedil":"ķ","Kcy":"К","kcy":"к","Kfr":"𝔎","kfr":"𝔨","kgreen":"ĸ","KHcy":"Х","khcy":"х","KJcy":"Ќ","kjcy":"ќ","Kopf":"𝕂","kopf":"𝕜","Kscr":"𝒦","kscr":"𝓀","lAarr":"⇚","Lacute":"Ĺ","lacute":"ĺ","laemptyv":"⦴","lagran":"ℒ","Lambda":"Λ","lambda":"λ","lang":"⟨","Lang":"⟪","langd":"⦑","langle":"⟨","lap":"⪅","Laplacetrf":"ℒ","laquo":"«","larrb":"⇤","larrbfs":"⤟","larr":"←","Larr":"↞","lArr":"⇐","larrfs":"⤝","larrhk":"↩","larrlp":"↫","larrpl":"⤹","larrsim":"⥳","larrtl":"↢","latail":"⤙","lAtail":"⤛","lat":"⪫","late":"⪭","lates":"⪭︀","lbarr":"⤌","lBarr":"⤎","lbbrk":"❲","lbrace":"{","lbrack":"[","lbrke":"⦋","lbrksld":"⦏","lbrkslu":"⦍","Lcaron":"Ľ","lcaron":"ľ","Lcedil":"Ļ","lcedil":"ļ","lceil":"⌈","lcub":"{","Lcy":"Л","lcy":"л","ldca":"⤶","ldquo":"“","ldquor":"„","ldrdhar":"⥧","ldrushar":"⥋","ldsh":"↲","le":"≤","lE":"≦","LeftAngleBracket":"⟨","LeftArrowBar":"⇤","leftarrow":"←","LeftArrow":"←","Leftarrow":"⇐","LeftArrowRightArrow":"⇆","leftarrowtail":"↢","LeftCeiling":"⌈","LeftDoubleBracket":"⟦","LeftDownTeeVector":"⥡","LeftDownVectorBar":"⥙","LeftDownVector":"⇃","LeftFloor":"⌊","leftharpoondown":"↽","leftharpoonup":"↼","leftleftarrows":"⇇","leftrightarrow":"↔","LeftRightArrow":"↔","Leftrightarrow":"⇔","leftrightarrows":"⇆","leftrightharpoons":"⇋","leftrightsquigarrow":"↭","LeftRightVector":"⥎","LeftTeeArrow":"↤","LeftTee":"⊣","LeftTeeVector":"⥚","leftthreetimes":"⋋","LeftTriangleBar":"⧏","LeftTriangle":"⊲","LeftTriangleEqual":"⊴","LeftUpDownVector":"⥑","LeftUpTeeVector":"⥠","LeftUpVectorBar":"⥘","LeftUpVector":"↿","LeftVectorBar":"⥒","LeftVector":"↼","lEg":"⪋","leg":"⋚","leq":"≤","leqq":"≦","leqslant":"⩽","lescc":"⪨","les":"⩽","lesdot":"⩿","lesdoto":"⪁","lesdotor":"⪃","lesg":"⋚︀","lesges":"⪓","lessapprox":"⪅","lessdot":"⋖","lesseqgtr":"⋚","lesseqqgtr":"⪋","LessEqualGreater":"⋚","LessFullEqual":"≦","LessGreater":"≶","lessgtr":"≶","LessLess":"⪡","lesssim":"≲","LessSlantEqual":"⩽","LessTilde":"≲","lfisht":"⥼","lfloor":"⌊","Lfr":"𝔏","lfr":"𝔩","lg":"≶","lgE":"⪑","lHar":"⥢","lhard":"↽","lharu":"↼","lharul":"⥪","lhblk":"▄","LJcy":"Љ","ljcy":"љ","llarr":"⇇","ll":"≪","Ll":"⋘","llcorner":"⌞","Lleftarrow":"⇚","llhard":"⥫","lltri":"◺","Lmidot":"Ŀ","lmidot":"ŀ","lmoustache":"⎰","lmoust":"⎰","lnap":"⪉","lnapprox":"⪉","lne":"⪇","lnE":"≨","lneq":"⪇","lneqq":"≨","lnsim":"⋦","loang":"⟬","loarr":"⇽","lobrk":"⟦","longleftarrow":"⟵","LongLeftArrow":"⟵","Longleftarrow":"⟸","longleftrightarrow":"⟷","LongLeftRightArrow":"⟷","Longleftrightarrow":"⟺","longmapsto":"⟼","longrightarrow":"⟶","LongRightArrow":"⟶","Longrightarrow":"⟹","looparrowleft":"↫","looparrowright":"↬","lopar":"⦅","Lopf":"𝕃","lopf":"𝕝","loplus":"⨭","lotimes":"⨴","lowast":"∗","lowbar":"_","LowerLeftArrow":"↙","LowerRightArrow":"↘","loz":"◊","lozenge":"◊","lozf":"⧫","lpar":"(","lparlt":"⦓","lrarr":"⇆","lrcorner":"⌟","lrhar":"⇋","lrhard":"⥭","lrm":"‎","lrtri":"⊿","lsaquo":"‹","lscr":"𝓁","Lscr":"ℒ","lsh":"↰","Lsh":"↰","lsim":"≲","lsime":"⪍","lsimg":"⪏","lsqb":"[","lsquo":"‘","lsquor":"‚","Lstrok":"Ł","lstrok":"ł","ltcc":"⪦","ltcir":"⩹","lt":"<","LT":"<","Lt":"≪","ltdot":"⋖","lthree":"⋋","ltimes":"⋉","ltlarr":"⥶","ltquest":"⩻","ltri":"◃","ltrie":"⊴","ltrif":"◂","ltrPar":"⦖","lurdshar":"⥊","luruhar":"⥦","lvertneqq":"≨︀","lvnE":"≨︀","macr":"¯","male":"♂","malt":"✠","maltese":"✠","Map":"⤅","map":"↦","mapsto":"↦","mapstodown":"↧","mapstoleft":"↤","mapstoup":"↥","marker":"▮","mcomma":"⨩","Mcy":"М","mcy":"м","mdash":"—","mDDot":"∺","measuredangle":"∡","MediumSpace":" ","Mellintrf":"ℳ","Mfr":"𝔐","mfr":"𝔪","mho":"℧","micro":"µ","midast":"*","midcir":"⫰","mid":"∣","middot":"·","minusb":"⊟","minus":"−","minusd":"∸","minusdu":"⨪","MinusPlus":"∓","mlcp":"⫛","mldr":"…","mnplus":"∓","models":"⊧","Mopf":"𝕄","mopf":"𝕞","mp":"∓","mscr":"𝓂","Mscr":"ℳ","mstpos":"∾","Mu":"Μ","mu":"μ","multimap":"⊸","mumap":"⊸","nabla":"∇","Nacute":"Ń","nacute":"ń","nang":"∠⃒","nap":"≉","napE":"⩰̸","napid":"≋̸","napos":"ŉ","napprox":"≉","natural":"♮","naturals":"ℕ","natur":"♮","nbsp":" ","nbump":"≎̸","nbumpe":"≏̸","ncap":"⩃","Ncaron":"Ň","ncaron":"ň","Ncedil":"Ņ","ncedil":"ņ","ncong":"≇","ncongdot":"⩭̸","ncup":"⩂","Ncy":"Н","ncy":"н","ndash":"–","nearhk":"⤤","nearr":"↗","neArr":"⇗","nearrow":"↗","ne":"≠","nedot":"≐̸","NegativeMediumSpace":"​","NegativeThickSpace":"​","NegativeThinSpace":"​","NegativeVeryThinSpace":"​","nequiv":"≢","nesear":"⤨","nesim":"≂̸","NestedGreaterGreater":"≫","NestedLessLess":"≪","NewLine":"\\n","nexist":"∄","nexists":"∄","Nfr":"𝔑","nfr":"𝔫","ngE":"≧̸","nge":"≱","ngeq":"≱","ngeqq":"≧̸","ngeqslant":"⩾̸","nges":"⩾̸","nGg":"⋙̸","ngsim":"≵","nGt":"≫⃒","ngt":"≯","ngtr":"≯","nGtv":"≫̸","nharr":"↮","nhArr":"⇎","nhpar":"⫲","ni":"∋","nis":"⋼","nisd":"⋺","niv":"∋","NJcy":"Њ","njcy":"њ","nlarr":"↚","nlArr":"⇍","nldr":"‥","nlE":"≦̸","nle":"≰","nleftarrow":"↚","nLeftarrow":"⇍","nleftrightarrow":"↮","nLeftrightarrow":"⇎","nleq":"≰","nleqq":"≦̸","nleqslant":"⩽̸","nles":"⩽̸","nless":"≮","nLl":"⋘̸","nlsim":"≴","nLt":"≪⃒","nlt":"≮","nltri":"⋪","nltrie":"⋬","nLtv":"≪̸","nmid":"∤","NoBreak":"⁠","NonBreakingSpace":" ","nopf":"𝕟","Nopf":"ℕ","Not":"⫬","not":"¬","NotCongruent":"≢","NotCupCap":"≭","NotDoubleVerticalBar":"∦","NotElement":"∉","NotEqual":"≠","NotEqualTilde":"≂̸","NotExists":"∄","NotGreater":"≯","NotGreaterEqual":"≱","NotGreaterFullEqual":"≧̸","NotGreaterGreater":"≫̸","NotGreaterLess":"≹","NotGreaterSlantEqual":"⩾̸","NotGreaterTilde":"≵","NotHumpDownHump":"≎̸","NotHumpEqual":"≏̸","notin":"∉","notindot":"⋵̸","notinE":"⋹̸","notinva":"∉","notinvb":"⋷","notinvc":"⋶","NotLeftTriangleBar":"⧏̸","NotLeftTriangle":"⋪","NotLeftTriangleEqual":"⋬","NotLess":"≮","NotLessEqual":"≰","NotLessGreater":"≸","NotLessLess":"≪̸","NotLessSlantEqual":"⩽̸","NotLessTilde":"≴","NotNestedGreaterGreater":"⪢̸","NotNestedLessLess":"⪡̸","notni":"∌","notniva":"∌","notnivb":"⋾","notnivc":"⋽","NotPrecedes":"⊀","NotPrecedesEqual":"⪯̸","NotPrecedesSlantEqual":"⋠","NotReverseElement":"∌","NotRightTriangleBar":"⧐̸","NotRightTriangle":"⋫","NotRightTriangleEqual":"⋭","NotSquareSubset":"⊏̸","NotSquareSubsetEqual":"⋢","NotSquareSuperset":"⊐̸","NotSquareSupersetEqual":"⋣","NotSubset":"⊂⃒","NotSubsetEqual":"⊈","NotSucceeds":"⊁","NotSucceedsEqual":"⪰̸","NotSucceedsSlantEqual":"⋡","NotSucceedsTilde":"≿̸","NotSuperset":"⊃⃒","NotSupersetEqual":"⊉","NotTilde":"≁","NotTildeEqual":"≄","NotTildeFullEqual":"≇","NotTildeTilde":"≉","NotVerticalBar":"∤","nparallel":"∦","npar":"∦","nparsl":"⫽⃥","npart":"∂̸","npolint":"⨔","npr":"⊀","nprcue":"⋠","nprec":"⊀","npreceq":"⪯̸","npre":"⪯̸","nrarrc":"⤳̸","nrarr":"↛","nrArr":"⇏","nrarrw":"↝̸","nrightarrow":"↛","nRightarrow":"⇏","nrtri":"⋫","nrtrie":"⋭","nsc":"⊁","nsccue":"⋡","nsce":"⪰̸","Nscr":"𝒩","nscr":"𝓃","nshortmid":"∤","nshortparallel":"∦","nsim":"≁","nsime":"≄","nsimeq":"≄","nsmid":"∤","nspar":"∦","nsqsube":"⋢","nsqsupe":"⋣","nsub":"⊄","nsubE":"⫅̸","nsube":"⊈","nsubset":"⊂⃒","nsubseteq":"⊈","nsubseteqq":"⫅̸","nsucc":"⊁","nsucceq":"⪰̸","nsup":"⊅","nsupE":"⫆̸","nsupe":"⊉","nsupset":"⊃⃒","nsupseteq":"⊉","nsupseteqq":"⫆̸","ntgl":"≹","Ntilde":"Ñ","ntilde":"ñ","ntlg":"≸","ntriangleleft":"⋪","ntrianglelefteq":"⋬","ntriangleright":"⋫","ntrianglerighteq":"⋭","Nu":"Ν","nu":"ν","num":"#","numero":"№","numsp":" ","nvap":"≍⃒","nvdash":"⊬","nvDash":"⊭","nVdash":"⊮","nVDash":"⊯","nvge":"≥⃒","nvgt":">⃒","nvHarr":"⤄","nvinfin":"⧞","nvlArr":"⤂","nvle":"≤⃒","nvlt":"<⃒","nvltrie":"⊴⃒","nvrArr":"⤃","nvrtrie":"⊵⃒","nvsim":"∼⃒","nwarhk":"⤣","nwarr":"↖","nwArr":"⇖","nwarrow":"↖","nwnear":"⤧","Oacute":"Ó","oacute":"ó","oast":"⊛","Ocirc":"Ô","ocirc":"ô","ocir":"⊚","Ocy":"О","ocy":"о","odash":"⊝","Odblac":"Ő","odblac":"ő","odiv":"⨸","odot":"⊙","odsold":"⦼","OElig":"Œ","oelig":"œ","ofcir":"⦿","Ofr":"𝔒","ofr":"𝔬","ogon":"˛","Ograve":"Ò","ograve":"ò","ogt":"⧁","ohbar":"⦵","ohm":"Ω","oint":"∮","olarr":"↺","olcir":"⦾","olcross":"⦻","oline":"‾","olt":"⧀","Omacr":"Ō","omacr":"ō","Omega":"Ω","omega":"ω","Omicron":"Ο","omicron":"ο","omid":"⦶","ominus":"⊖","Oopf":"𝕆","oopf":"𝕠","opar":"⦷","OpenCurlyDoubleQuote":"“","OpenCurlyQuote":"‘","operp":"⦹","oplus":"⊕","orarr":"↻","Or":"⩔","or":"∨","ord":"⩝","order":"ℴ","orderof":"ℴ","ordf":"ª","ordm":"º","origof":"⊶","oror":"⩖","orslope":"⩗","orv":"⩛","oS":"Ⓢ","Oscr":"𝒪","oscr":"ℴ","Oslash":"Ø","oslash":"ø","osol":"⊘","Otilde":"Õ","otilde":"õ","otimesas":"⨶","Otimes":"⨷","otimes":"⊗","Ouml":"Ö","ouml":"ö","ovbar":"⌽","OverBar":"‾","OverBrace":"⏞","OverBracket":"⎴","OverParenthesis":"⏜","para":"¶","parallel":"∥","par":"∥","parsim":"⫳","parsl":"⫽","part":"∂","PartialD":"∂","Pcy":"П","pcy":"п","percnt":"%","period":".","permil":"‰","perp":"⊥","pertenk":"‱","Pfr":"𝔓","pfr":"𝔭","Phi":"Φ","phi":"φ","phiv":"ϕ","phmmat":"ℳ","phone":"☎","Pi":"Π","pi":"π","pitchfork":"⋔","piv":"ϖ","planck":"ℏ","planckh":"ℎ","plankv":"ℏ","plusacir":"⨣","plusb":"⊞","pluscir":"⨢","plus":"+","plusdo":"∔","plusdu":"⨥","pluse":"⩲","PlusMinus":"±","plusmn":"±","plussim":"⨦","plustwo":"⨧","pm":"±","Poincareplane":"ℌ","pointint":"⨕","popf":"𝕡","Popf":"ℙ","pound":"£","prap":"⪷","Pr":"⪻","pr":"≺","prcue":"≼","precapprox":"⪷","prec":"≺","preccurlyeq":"≼","Precedes":"≺","PrecedesEqual":"⪯","PrecedesSlantEqual":"≼","PrecedesTilde":"≾","preceq":"⪯","precnapprox":"⪹","precneqq":"⪵","precnsim":"⋨","pre":"⪯","prE":"⪳","precsim":"≾","prime":"′","Prime":"″","primes":"ℙ","prnap":"⪹","prnE":"⪵","prnsim":"⋨","prod":"∏","Product":"∏","profalar":"⌮","profline":"⌒","profsurf":"⌓","prop":"∝","Proportional":"∝","Proportion":"∷","propto":"∝","prsim":"≾","prurel":"⊰","Pscr":"𝒫","pscr":"𝓅","Psi":"Ψ","psi":"ψ","puncsp":" ","Qfr":"𝔔","qfr":"𝔮","qint":"⨌","qopf":"𝕢","Qopf":"ℚ","qprime":"⁗","Qscr":"𝒬","qscr":"𝓆","quaternions":"ℍ","quatint":"⨖","quest":"?","questeq":"≟","quot":"\\"","QUOT":"\\"","rAarr":"⇛","race":"∽̱","Racute":"Ŕ","racute":"ŕ","radic":"√","raemptyv":"⦳","rang":"⟩","Rang":"⟫","rangd":"⦒","range":"⦥","rangle":"⟩","raquo":"»","rarrap":"⥵","rarrb":"⇥","rarrbfs":"⤠","rarrc":"⤳","rarr":"→","Rarr":"↠","rArr":"⇒","rarrfs":"⤞","rarrhk":"↪","rarrlp":"↬","rarrpl":"⥅","rarrsim":"⥴","Rarrtl":"⤖","rarrtl":"↣","rarrw":"↝","ratail":"⤚","rAtail":"⤜","ratio":"∶","rationals":"ℚ","rbarr":"⤍","rBarr":"⤏","RBarr":"⤐","rbbrk":"❳","rbrace":"}","rbrack":"]","rbrke":"⦌","rbrksld":"⦎","rbrkslu":"⦐","Rcaron":"Ř","rcaron":"ř","Rcedil":"Ŗ","rcedil":"ŗ","rceil":"⌉","rcub":"}","Rcy":"Р","rcy":"р","rdca":"⤷","rdldhar":"⥩","rdquo":"”","rdquor":"”","rdsh":"↳","real":"ℜ","realine":"ℛ","realpart":"ℜ","reals":"ℝ","Re":"ℜ","rect":"▭","reg":"®","REG":"®","ReverseElement":"∋","ReverseEquilibrium":"⇋","ReverseUpEquilibrium":"⥯","rfisht":"⥽","rfloor":"⌋","rfr":"𝔯","Rfr":"ℜ","rHar":"⥤","rhard":"⇁","rharu":"⇀","rharul":"⥬","Rho":"Ρ","rho":"ρ","rhov":"ϱ","RightAngleBracket":"⟩","RightArrowBar":"⇥","rightarrow":"→","RightArrow":"→","Rightarrow":"⇒","RightArrowLeftArrow":"⇄","rightarrowtail":"↣","RightCeiling":"⌉","RightDoubleBracket":"⟧","RightDownTeeVector":"⥝","RightDownVectorBar":"⥕","RightDownVector":"⇂","RightFloor":"⌋","rightharpoondown":"⇁","rightharpoonup":"⇀","rightleftarrows":"⇄","rightleftharpoons":"⇌","rightrightarrows":"⇉","rightsquigarrow":"↝","RightTeeArrow":"↦","RightTee":"⊢","RightTeeVector":"⥛","rightthreetimes":"⋌","RightTriangleBar":"⧐","RightTriangle":"⊳","RightTriangleEqual":"⊵","RightUpDownVector":"⥏","RightUpTeeVector":"⥜","RightUpVectorBar":"⥔","RightUpVector":"↾","RightVectorBar":"⥓","RightVector":"⇀","ring":"˚","risingdotseq":"≓","rlarr":"⇄","rlhar":"⇌","rlm":"‏","rmoustache":"⎱","rmoust":"⎱","rnmid":"⫮","roang":"⟭","roarr":"⇾","robrk":"⟧","ropar":"⦆","ropf":"𝕣","Ropf":"ℝ","roplus":"⨮","rotimes":"⨵","RoundImplies":"⥰","rpar":")","rpargt":"⦔","rppolint":"⨒","rrarr":"⇉","Rrightarrow":"⇛","rsaquo":"›","rscr":"𝓇","Rscr":"ℛ","rsh":"↱","Rsh":"↱","rsqb":"]","rsquo":"’","rsquor":"’","rthree":"⋌","rtimes":"⋊","rtri":"▹","rtrie":"⊵","rtrif":"▸","rtriltri":"⧎","RuleDelayed":"⧴","ruluhar":"⥨","rx":"℞","Sacute":"Ś","sacute":"ś","sbquo":"‚","scap":"⪸","Scaron":"Š","scaron":"š","Sc":"⪼","sc":"≻","sccue":"≽","sce":"⪰","scE":"⪴","Scedil":"Ş","scedil":"ş","Scirc":"Ŝ","scirc":"ŝ","scnap":"⪺","scnE":"⪶","scnsim":"⋩","scpolint":"⨓","scsim":"≿","Scy":"С","scy":"с","sdotb":"⊡","sdot":"⋅","sdote":"⩦","searhk":"⤥","searr":"↘","seArr":"⇘","searrow":"↘","sect":"§","semi":";","seswar":"⤩","setminus":"∖","setmn":"∖","sext":"✶","Sfr":"𝔖","sfr":"𝔰","sfrown":"⌢","sharp":"♯","SHCHcy":"Щ","shchcy":"щ","SHcy":"Ш","shcy":"ш","ShortDownArrow":"↓","ShortLeftArrow":"←","shortmid":"∣","shortparallel":"∥","ShortRightArrow":"→","ShortUpArrow":"↑","shy":"­","Sigma":"Σ","sigma":"σ","sigmaf":"ς","sigmav":"ς","sim":"∼","simdot":"⩪","sime":"≃","simeq":"≃","simg":"⪞","simgE":"⪠","siml":"⪝","simlE":"⪟","simne":"≆","simplus":"⨤","simrarr":"⥲","slarr":"←","SmallCircle":"∘","smallsetminus":"∖","smashp":"⨳","smeparsl":"⧤","smid":"∣","smile":"⌣","smt":"⪪","smte":"⪬","smtes":"⪬︀","SOFTcy":"Ь","softcy":"ь","solbar":"⌿","solb":"⧄","sol":"/","Sopf":"𝕊","sopf":"𝕤","spades":"♠","spadesuit":"♠","spar":"∥","sqcap":"⊓","sqcaps":"⊓︀","sqcup":"⊔","sqcups":"⊔︀","Sqrt":"√","sqsub":"⊏","sqsube":"⊑","sqsubset":"⊏","sqsubseteq":"⊑","sqsup":"⊐","sqsupe":"⊒","sqsupset":"⊐","sqsupseteq":"⊒","square":"□","Square":"□","SquareIntersection":"⊓","SquareSubset":"⊏","SquareSubsetEqual":"⊑","SquareSuperset":"⊐","SquareSupersetEqual":"⊒","SquareUnion":"⊔","squarf":"▪","squ":"□","squf":"▪","srarr":"→","Sscr":"𝒮","sscr":"𝓈","ssetmn":"∖","ssmile":"⌣","sstarf":"⋆","Star":"⋆","star":"☆","starf":"★","straightepsilon":"ϵ","straightphi":"ϕ","strns":"¯","sub":"⊂","Sub":"⋐","subdot":"⪽","subE":"⫅","sube":"⊆","subedot":"⫃","submult":"⫁","subnE":"⫋","subne":"⊊","subplus":"⪿","subrarr":"⥹","subset":"⊂","Subset":"⋐","subseteq":"⊆","subseteqq":"⫅","SubsetEqual":"⊆","subsetneq":"⊊","subsetneqq":"⫋","subsim":"⫇","subsub":"⫕","subsup":"⫓","succapprox":"⪸","succ":"≻","succcurlyeq":"≽","Succeeds":"≻","SucceedsEqual":"⪰","SucceedsSlantEqual":"≽","SucceedsTilde":"≿","succeq":"⪰","succnapprox":"⪺","succneqq":"⪶","succnsim":"⋩","succsim":"≿","SuchThat":"∋","sum":"∑","Sum":"∑","sung":"♪","sup1":"¹","sup2":"²","sup3":"³","sup":"⊃","Sup":"⋑","supdot":"⪾","supdsub":"⫘","supE":"⫆","supe":"⊇","supedot":"⫄","Superset":"⊃","SupersetEqual":"⊇","suphsol":"⟉","suphsub":"⫗","suplarr":"⥻","supmult":"⫂","supnE":"⫌","supne":"⊋","supplus":"⫀","supset":"⊃","Supset":"⋑","supseteq":"⊇","supseteqq":"⫆","supsetneq":"⊋","supsetneqq":"⫌","supsim":"⫈","supsub":"⫔","supsup":"⫖","swarhk":"⤦","swarr":"↙","swArr":"⇙","swarrow":"↙","swnwar":"⤪","szlig":"ß","Tab":"\\t","target":"⌖","Tau":"Τ","tau":"τ","tbrk":"⎴","Tcaron":"Ť","tcaron":"ť","Tcedil":"Ţ","tcedil":"ţ","Tcy":"Т","tcy":"т","tdot":"⃛","telrec":"⌕","Tfr":"𝔗","tfr":"𝔱","there4":"∴","therefore":"∴","Therefore":"∴","Theta":"Θ","theta":"θ","thetasym":"ϑ","thetav":"ϑ","thickapprox":"≈","thicksim":"∼","ThickSpace":"  ","ThinSpace":" ","thinsp":" ","thkap":"≈","thksim":"∼","THORN":"Þ","thorn":"þ","tilde":"˜","Tilde":"∼","TildeEqual":"≃","TildeFullEqual":"≅","TildeTilde":"≈","timesbar":"⨱","timesb":"⊠","times":"×","timesd":"⨰","tint":"∭","toea":"⤨","topbot":"⌶","topcir":"⫱","top":"⊤","Topf":"𝕋","topf":"𝕥","topfork":"⫚","tosa":"⤩","tprime":"‴","trade":"™","TRADE":"™","triangle":"▵","triangledown":"▿","triangleleft":"◃","trianglelefteq":"⊴","triangleq":"≜","triangleright":"▹","trianglerighteq":"⊵","tridot":"◬","trie":"≜","triminus":"⨺","TripleDot":"⃛","triplus":"⨹","trisb":"⧍","tritime":"⨻","trpezium":"⏢","Tscr":"𝒯","tscr":"𝓉","TScy":"Ц","tscy":"ц","TSHcy":"Ћ","tshcy":"ћ","Tstrok":"Ŧ","tstrok":"ŧ","twixt":"≬","twoheadleftarrow":"↞","twoheadrightarrow":"↠","Uacute":"Ú","uacute":"ú","uarr":"↑","Uarr":"↟","uArr":"⇑","Uarrocir":"⥉","Ubrcy":"Ў","ubrcy":"ў","Ubreve":"Ŭ","ubreve":"ŭ","Ucirc":"Û","ucirc":"û","Ucy":"У","ucy":"у","udarr":"⇅","Udblac":"Ű","udblac":"ű","udhar":"⥮","ufisht":"⥾","Ufr":"𝔘","ufr":"𝔲","Ugrave":"Ù","ugrave":"ù","uHar":"⥣","uharl":"↿","uharr":"↾","uhblk":"▀","ulcorn":"⌜","ulcorner":"⌜","ulcrop":"⌏","ultri":"◸","Umacr":"Ū","umacr":"ū","uml":"¨","UnderBar":"_","UnderBrace":"⏟","UnderBracket":"⎵","UnderParenthesis":"⏝","Union":"⋃","UnionPlus":"⊎","Uogon":"Ų","uogon":"ų","Uopf":"𝕌","uopf":"𝕦","UpArrowBar":"⤒","uparrow":"↑","UpArrow":"↑","Uparrow":"⇑","UpArrowDownArrow":"⇅","updownarrow":"↕","UpDownArrow":"↕","Updownarrow":"⇕","UpEquilibrium":"⥮","upharpoonleft":"↿","upharpoonright":"↾","uplus":"⊎","UpperLeftArrow":"↖","UpperRightArrow":"↗","upsi":"υ","Upsi":"ϒ","upsih":"ϒ","Upsilon":"Υ","upsilon":"υ","UpTeeArrow":"↥","UpTee":"⊥","upuparrows":"⇈","urcorn":"⌝","urcorner":"⌝","urcrop":"⌎","Uring":"Ů","uring":"ů","urtri":"◹","Uscr":"𝒰","uscr":"𝓊","utdot":"⋰","Utilde":"Ũ","utilde":"ũ","utri":"▵","utrif":"▴","uuarr":"⇈","Uuml":"Ü","uuml":"ü","uwangle":"⦧","vangrt":"⦜","varepsilon":"ϵ","varkappa":"ϰ","varnothing":"∅","varphi":"ϕ","varpi":"ϖ","varpropto":"∝","varr":"↕","vArr":"⇕","varrho":"ϱ","varsigma":"ς","varsubsetneq":"⊊︀","varsubsetneqq":"⫋︀","varsupsetneq":"⊋︀","varsupsetneqq":"⫌︀","vartheta":"ϑ","vartriangleleft":"⊲","vartriangleright":"⊳","vBar":"⫨","Vbar":"⫫","vBarv":"⫩","Vcy":"В","vcy":"в","vdash":"⊢","vDash":"⊨","Vdash":"⊩","VDash":"⊫","Vdashl":"⫦","veebar":"⊻","vee":"∨","Vee":"⋁","veeeq":"≚","vellip":"⋮","verbar":"|","Verbar":"‖","vert":"|","Vert":"‖","VerticalBar":"∣","VerticalLine":"|","VerticalSeparator":"❘","VerticalTilde":"≀","VeryThinSpace":" ","Vfr":"𝔙","vfr":"𝔳","vltri":"⊲","vnsub":"⊂⃒","vnsup":"⊃⃒","Vopf":"𝕍","vopf":"𝕧","vprop":"∝","vrtri":"⊳","Vscr":"𝒱","vscr":"𝓋","vsubnE":"⫋︀","vsubne":"⊊︀","vsupnE":"⫌︀","vsupne":"⊋︀","Vvdash":"⊪","vzigzag":"⦚","Wcirc":"Ŵ","wcirc":"ŵ","wedbar":"⩟","wedge":"∧","Wedge":"⋀","wedgeq":"≙","weierp":"℘","Wfr":"𝔚","wfr":"𝔴","Wopf":"𝕎","wopf":"𝕨","wp":"℘","wr":"≀","wreath":"≀","Wscr":"𝒲","wscr":"𝓌","xcap":"⋂","xcirc":"◯","xcup":"⋃","xdtri":"▽","Xfr":"𝔛","xfr":"𝔵","xharr":"⟷","xhArr":"⟺","Xi":"Ξ","xi":"ξ","xlarr":"⟵","xlArr":"⟸","xmap":"⟼","xnis":"⋻","xodot":"⨀","Xopf":"𝕏","xopf":"𝕩","xoplus":"⨁","xotime":"⨂","xrarr":"⟶","xrArr":"⟹","Xscr":"𝒳","xscr":"𝓍","xsqcup":"⨆","xuplus":"⨄","xutri":"△","xvee":"⋁","xwedge":"⋀","Yacute":"Ý","yacute":"ý","YAcy":"Я","yacy":"я","Ycirc":"Ŷ","ycirc":"ŷ","Ycy":"Ы","ycy":"ы","yen":"¥","Yfr":"𝔜","yfr":"𝔶","YIcy":"Ї","yicy":"ї","Yopf":"𝕐","yopf":"𝕪","Yscr":"𝒴","yscr":"𝓎","YUcy":"Ю","yucy":"ю","yuml":"ÿ","Yuml":"Ÿ","Zacute":"Ź","zacute":"ź","Zcaron":"Ž","zcaron":"ž","Zcy":"З","zcy":"з","Zdot":"Ż","zdot":"ż","zeetrf":"ℨ","ZeroWidthSpace":"​","Zeta":"Ζ","zeta":"ζ","zfr":"𝔷","Zfr":"ℨ","ZHcy":"Ж","zhcy":"ж","zigrarr":"⇝","zopf":"𝕫","Zopf":"ℤ","Zscr":"𝒵","zscr":"𝓏","zwj":"‍","zwnj":"‌"}');

/***/ }),

/***/ 9591:
/***/ ((module) => {

"use strict";
module.exports = JSON.parse('{"Aacute":"Á","aacute":"á","Acirc":"Â","acirc":"â","acute":"´","AElig":"Æ","aelig":"æ","Agrave":"À","agrave":"à","amp":"&","AMP":"&","Aring":"Å","aring":"å","Atilde":"Ã","atilde":"ã","Auml":"Ä","auml":"ä","brvbar":"¦","Ccedil":"Ç","ccedil":"ç","cedil":"¸","cent":"¢","copy":"©","COPY":"©","curren":"¤","deg":"°","divide":"÷","Eacute":"É","eacute":"é","Ecirc":"Ê","ecirc":"ê","Egrave":"È","egrave":"è","ETH":"Ð","eth":"ð","Euml":"Ë","euml":"ë","frac12":"½","frac14":"¼","frac34":"¾","gt":">","GT":">","Iacute":"Í","iacute":"í","Icirc":"Î","icirc":"î","iexcl":"¡","Igrave":"Ì","igrave":"ì","iquest":"¿","Iuml":"Ï","iuml":"ï","laquo":"«","lt":"<","LT":"<","macr":"¯","micro":"µ","middot":"·","nbsp":" ","not":"¬","Ntilde":"Ñ","ntilde":"ñ","Oacute":"Ó","oacute":"ó","Ocirc":"Ô","ocirc":"ô","Ograve":"Ò","ograve":"ò","ordf":"ª","ordm":"º","Oslash":"Ø","oslash":"ø","Otilde":"Õ","otilde":"õ","Ouml":"Ö","ouml":"ö","para":"¶","plusmn":"±","pound":"£","quot":"\\"","QUOT":"\\"","raquo":"»","reg":"®","REG":"®","sect":"§","shy":"­","sup1":"¹","sup2":"²","sup3":"³","szlig":"ß","THORN":"Þ","thorn":"þ","times":"×","Uacute":"Ú","uacute":"ú","Ucirc":"Û","ucirc":"û","Ugrave":"Ù","ugrave":"ù","uml":"¨","Uuml":"Ü","uuml":"ü","Yacute":"Ý","yacute":"ý","yen":"¥","yuml":"ÿ"}');

/***/ }),

/***/ 2586:
/***/ ((module) => {

"use strict";
module.exports = JSON.parse('{"amp":"&","apos":"\'","gt":">","lt":"<","quot":"\\""}');

/***/ })

/******/ 	});
/************************************************************************/
/******/ 	// The module cache
/******/ 	var __webpack_module_cache__ = {};
/******/ 	
/******/ 	// The require function
/******/ 	function __webpack_require__(moduleId) {
/******/ 		// Check if module is in cache
/******/ 		var cachedModule = __webpack_module_cache__[moduleId];
/******/ 		if (cachedModule !== undefined) {
/******/ 			return cachedModule.exports;
/******/ 		}
/******/ 		// Create a new module (and put it into the cache)
/******/ 		var module = __webpack_module_cache__[moduleId] = {
/******/ 			id: moduleId,
/******/ 			loaded: false,
/******/ 			exports: {}
/******/ 		};
/******/ 	
/******/ 		// Execute the module function
/******/ 		__webpack_modules__[moduleId].call(module.exports, module, module.exports, __webpack_require__);
/******/ 	
/******/ 		// Flag the module as loaded
/******/ 		module.loaded = true;
/******/ 	
/******/ 		// Return the exports of the module
/******/ 		return module.exports;
/******/ 	}
/******/ 	
/************************************************************************/
/******/ 	/* webpack/runtime/compat get default export */
/******/ 	(() => {
/******/ 		// getDefaultExport function for compatibility with non-harmony modules
/******/ 		__webpack_require__.n = (module) => {
/******/ 			var getter = module && module.__esModule ?
/******/ 				() => (module['default']) :
/******/ 				() => (module);
/******/ 			__webpack_require__.d(getter, { a: getter });
/******/ 			return getter;
/******/ 		};
/******/ 	})();
/******/ 	
/******/ 	/* webpack/runtime/define property getters */
/******/ 	(() => {
/******/ 		// define getter functions for harmony exports
/******/ 		__webpack_require__.d = (exports, definition) => {
/******/ 			for(var key in definition) {
/******/ 				if(__webpack_require__.o(definition, key) && !__webpack_require__.o(exports, key)) {
/******/ 					Object.defineProperty(exports, key, { enumerable: true, get: definition[key] });
/******/ 				}
/******/ 			}
/******/ 		};
/******/ 	})();
/******/ 	
/******/ 	/* webpack/runtime/global */
/******/ 	(() => {
/******/ 		__webpack_require__.g = (function() {
/******/ 			if (typeof globalThis === 'object') return globalThis;
/******/ 			try {
/******/ 				return this || new Function('return this')();
/******/ 			} catch (e) {
/******/ 				if (typeof window === 'object') return window;
/******/ 			}
/******/ 		})();
/******/ 	})();
/******/ 	
/******/ 	/* webpack/runtime/hasOwnProperty shorthand */
/******/ 	(() => {
/******/ 		__webpack_require__.o = (obj, prop) => (Object.prototype.hasOwnProperty.call(obj, prop))
/******/ 	})();
/******/ 	
/******/ 	/* webpack/runtime/make namespace object */
/******/ 	(() => {
/******/ 		// define __esModule on exports
/******/ 		__webpack_require__.r = (exports) => {
/******/ 			if(typeof Symbol !== 'undefined' && Symbol.toStringTag) {
/******/ 				Object.defineProperty(exports, Symbol.toStringTag, { value: 'Module' });
/******/ 			}
/******/ 			Object.defineProperty(exports, '__esModule', { value: true });
/******/ 		};
/******/ 	})();
/******/ 	
/******/ 	/* webpack/runtime/node module decorator */
/******/ 	(() => {
/******/ 		__webpack_require__.nmd = (module) => {
/******/ 			module.paths = [];
/******/ 			if (!module.children) module.children = [];
/******/ 			return module;
/******/ 		};
/******/ 	})();
/******/ 	
/************************************************************************/
var __webpack_exports__ = {};
// This entry need to be wrapped in an IIFE because it need to be in strict mode.
(() => {
"use strict";


__webpack_require__(2234);
__webpack_require__(6760);
__webpack_require__(8299);
if (__webpack_require__.g._babelPolyfill) {
  throw new Error("only one instance of babel-polyfill is allowed");
}
__webpack_require__.g._babelPolyfill = true;
var DEFINE_PROPERTY = "defineProperty";
function define(O, key, value) {
  O[key] || Object[DEFINE_PROPERTY](O, key, {
    writable: true,
    configurable: true,
    value: value
  });
}
define(String.prototype, "padLeft", "".padStart);
define(String.prototype, "padRight", "".padEnd);
"pop,reverse,shift,keys,values,entries,indexOf,every,some,forEach,map,filter,find,findIndex,includes,join,slice,concat,push,splice,unshift,sort,lastIndexOf,reduce,reduceRight,copyWithin,fill".split(",").forEach(function (key) {
  [][key] && define(Array, key, Function.call.bind([][key]));
});
})();

// This entry need to be wrapped in an IIFE because it need to be in strict mode.
(() => {
"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "Sanitizer": () => (/* binding */ Sanitizer),
/* harmony export */   "defaultSanitizer": () => (/* binding */ defaultSanitizer)
/* harmony export */ });
/* harmony import */ var sanitize_html__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(6482);
/* harmony import */ var sanitize_html__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(sanitize_html__WEBPACK_IMPORTED_MODULE_0__);
var _templateObject, _templateObject2, _templateObject3, _templateObject4;
function _taggedTemplateLiteral(strings, raw) { if (!raw) { raw = strings.slice(0); } return Object.freeze(Object.defineProperties(strings, { raw: { value: Object.freeze(raw) } })); }
function _classCallCheck(instance, Constructor) { if (!(instance instanceof Constructor)) { throw new TypeError("Cannot call a class as a function"); } }
function _defineProperties(target, props) { for (var i = 0; i < props.length; i++) { var descriptor = props[i]; descriptor.enumerable = descriptor.enumerable || false; descriptor.configurable = true; if ("value" in descriptor) descriptor.writable = true; Object.defineProperty(target, descriptor.key, descriptor); } }
function _createClass(Constructor, protoProps, staticProps) { if (protoProps) _defineProperties(Constructor.prototype, protoProps); if (staticProps) _defineProperties(Constructor, staticProps); Object.defineProperty(Constructor, "prototype", { writable: false }); return Constructor; }
// Copyright (c) Jupyter Development Team.
// Distributed under the terms of the Modified BSD License.
// sanitize-html uses the url package, so we depend on a standalone version of
// it which acts as a polyfill for browsers.

/**
 * Helper class that contains regular expressions for inline CSS style validation.
 *
 * Which properties (and values) to allow is largely based on the Google Caja project:
 *   https://github.com/google/caja
 *
 * The regular expressions are largly based on the syntax definition found at
 * https://developer.mozilla.org/en-US/docs/Web/CSS.
 */
var CssProp = /*#__PURE__*/function () {
  function CssProp() {
    _classCallCheck(this, CssProp);
  }
  _createClass(CssProp, null, [{
    key: "reg",
    value: function reg(r) {
      return new RegExp('^' + r + '$', 'i');
    }
  }]);
  return CssProp;
}();
/*
 * Numeric base expressions used to help build more complex regular expressions
 */
CssProp.N = {
  integer: "[+-]?[0-9]+",
  integer_pos: "[+]?[0-9]+",
  integer_zero_ff: "([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])",
  number: "[+-]?([0-9]*[.])?[0-9]+(e-?[0-9]*)?",
  number_pos: "[+]?([0-9]*[.])?[0-9]+(e-?[0-9]*)?",
  number_zero_hundred: "[+]?(([0-9]|[1-9][0-9])([.][0-9]+)?|100)",
  number_zero_one: "[+]?(1([.][0]+)?|0?([.][0-9]+)?)"
};
/*
 * Base expressions of common CSS syntax elements
 */
CssProp.B = {
  angle: "(".concat(CssProp.N.number, "(deg|rad|grad|turn)|0)"),
  frequency: "".concat(CssProp.N.number, "(Hz|kHz)"),
  ident: String.raw(_templateObject || (_templateObject = _taggedTemplateLiteral(["-?([_a-z]|[\xA0-\xFF]|\\[0-9a-f]{1,6}(\r\n|[ \t\r\n\f])?|\\[^\r\n\f0-9a-f])([_a-z0-9-]|[\xA0-\xFF]|\\[0-9a-f]{1,6}(\r\n|[ \t\r\n\f])?|\\[^\r\n\f0-9a-f])*"], ["-?([_a-z]|[\\xA0-\\xFF]|\\\\[0-9a-f]{1,6}(\\r\\n|[ \\t\\r\\n\\f])?|\\\\[^\\r\\n\\f0-9a-f])([_a-z0-9-]|[\\xA0-\\xFF]|\\\\[0-9a-f]{1,6}(\\r\\n|[ \\t\\r\\n\\f])?|\\\\[^\\r\\n\\f0-9a-f])*"]))),
  len_or_perc: "(0|".concat(CssProp.N.number, "(px|em|rem|ex|in|cm|mm|pt|pc|%))"),
  length: "(".concat(CssProp.N.number, "(px|em|rem|ex|in|cm|mm|pt|pc)|0)"),
  length_pos: "(".concat(CssProp.N.number_pos, "(px|em|rem|ex|in|cm|mm|pt|pc)|0)"),
  percentage: "".concat(CssProp.N.number, "%"),
  percentage_pos: "".concat(CssProp.N.number_pos, "%"),
  percentage_zero_hundred: "".concat(CssProp.N.number_zero_hundred, "%"),
  string: String.raw(_templateObject2 || (_templateObject2 = _taggedTemplateLiteral(["(\"([^\n\r\f\\\"]|\\\n|\r\n|\r|\f|\\[0-9a-f]{1,6}(\r\n|[ \t\r\n\f])?|\\[^\r\n\f0-9a-f])*\")|('([^\n\r\f\\']|\\\n|\r\n|\r|\f|\\[0-9a-f]{1,6}(\r\n|[ \t\r\n\f])?|\\[^\r\n\f0-9a-f])*')"], ["(\\\"([^\\n\\r\\f\\\\\"]|\\\\\\n|\\r\\n|\\r|\\f|\\\\[0-9a-f]{1,6}(\\r\\n|[ \\t\\r\\n\\f])?|\\\\[^\\r\\n\\f0-9a-f])*\\\")|(\\'([^\\n\\r\\f\\\\']|\\\\\\n|\\r\\n|\\r|\\f|\\\\[0-9a-f]{1,6}(\\r\\n|[ \\t\\r\\n\\f])?|\\\\[^\\r\\n\\f0-9a-f])*\\')"]))),
  time: "".concat(CssProp.N.number, "(s|ms)"),
  url: "url\\(.*?\\)",
  z_index: "[+-]?[0-9]{1,7}"
};
/*
 * Atomic (i.e. not dependant on other regular expressions) sub RegEx segments
 */
CssProp.A = {
  absolute_size: "xx-small|x-small|small|medium|large|x-large|xx-large",
  attachment: "scroll|fixed|local",
  bg_origin: "border-box|padding-box|content-box",
  border_style: "none|hidden|dotted|dashed|solid|double|groove|ridge|inset|outset",
  box: "border-box|padding-box|content-box",
  display_inside: "auto|block|table|flex|grid",
  display_outside: "block-level|inline-level|none|table-row-group|table-header-group|table-footer-group|table-row|table-cell|table-column-group|table-column|table-caption",
  ending_shape: "circle|ellipse",
  generic_family: "serif|sans-serif|cursive|fantasy|monospace",
  generic_voice: "male|female|child",
  relative_size: "smaller|larger",
  repeat_style: "repeat-x|repeat-y|((?:repeat|space|round|no-repeat)(?:\\s*(?:repeat|space|round|no-repeat))?)",
  side_or_corner: "(left|right)?\\s*(top|bottom)?",
  single_animation_direction: "normal|reverse|alternate|alternate-reverse",
  single_animation_fill_mode: "none|forwards|backwards|both",
  single_animation_play_state: "running|paused"
};
/*
 * Color definition sub expressions
 */
CssProp._COLOR = {
  hex: "\\#(0x)?[0-9a-f]+",
  name: "aliceblue|antiquewhite|aqua|aquamarine|azure|beige|bisque|black|blanchedalmond|blue|blueviolet|brown|burlywood|cadetblue|chartreuse|chocolate|coral|cornflowerblue|cornsilk|crimson|cyan|darkblue|darkcyan|darkgoldenrod|darkgray|darkgreen|darkkhaki|darkmagenta|darkolivegreen|darkorange|darkorchid|darkred|darksalmon|darkseagreen|darkslateblue|darkslategray|darkturquoise|darkviolet|deeppink|deepskyblue|dimgray|dodgerblue|firebrick|floralwhite|forestgreen|fuchsia|gainsboro|ghostwhite|gold|goldenrod|gray|green|greenyellow|honeydew|hotpink|indianred|indigo|ivory|khaki|lavender|lavenderblush|lawngreen|lemonchiffon|lightblue|lightcoral|lightcyan|lightgoldenrodyellow|lightgreen|lightgrey|lightpink|lightsalmon|lightseagreen|lightskyblue|lightslategray|lightsteelblue|lightyellow|lime|limegreen|linen|magenta|maroon|mediumaquamarine|mediumblue|mediumorchid|mediumpurple|mediumseagreen|mediumslateblue|mediumspringgreen|mediumturquoise|mediumvioletred|midnightblue|mintcream|mistyrose|moccasin|navajowhite|navy|oldlace|olive|olivedrab|orange|orangered|orchid|palegoldenrod|palegreen|paleturquoise|palevioletred|papayawhip|peachpuff|peru|pink|plum|powderblue|purple|red|rosybrown|royalblue|saddlebrown|salmon|sandybrown|seagreen|seashell|sienna|silver|skyblue|slateblue|slategray|snow|springgreen|steelblue|tan|teal|thistle|tomato|turquoise|transparent|violet|wheat|white|whitesmoke|yellow|yellowgreen",
  rgb: String.raw(_templateObject3 || (_templateObject3 = _taggedTemplateLiteral(["rgb(s*(d{1,3})s*,s*(d{1,3})s*,s*(d{1,3})s*)"], ["rgb\\(\\s*(\\d{1,3})\\s*,\\s*(\\d{1,3})\\s*,\\s*(\\d{1,3})\\s*\\)"]))),
  rgba: String.raw(_templateObject4 || (_templateObject4 = _taggedTemplateLiteral(["rgba(s*(d{1,3})s*,s*(d{1,3})s*,s*(d{1,3})s*,s*(", "|", "|", ")s*)"], ["rgba\\(\\s*(\\d{1,3})\\s*,\\s*(\\d{1,3})\\s*,\\s*(\\d{1,3})\\s*,\\s*(", "|", "|", ")\\s*\\)"])), CssProp.N.integer_zero_ff, CssProp.N.number_zero_one, CssProp.B.percentage_zero_hundred)
};
/*
 * Compound (i.e. dependant on other (sub) regular expressions) sub RegEx segments
 */
CssProp._C = {
  alpha: "".concat(CssProp.N.integer_zero_ff, "|").concat(CssProp.N.number_zero_one, "|").concat(CssProp.B.percentage_zero_hundred),
  alphavalue: CssProp.N.number_zero_one,
  bg_position: "((".concat(CssProp.B.len_or_perc, "|left|center|right|top|bottom)\\s*){1,4}"),
  bg_size: "(".concat(CssProp.B.length_pos, "|").concat(CssProp.B.percentage, "|auto){1,2}|cover|contain"),
  border_width: "thin|medium|thick|".concat(CssProp.B.length),
  bottom: "".concat(CssProp.B.length, "|auto"),
  color: "".concat(CssProp._COLOR.hex, "|").concat(CssProp._COLOR.rgb, "|").concat(CssProp._COLOR.rgba, "|").concat(CssProp._COLOR.name),
  color_stop_length: "(".concat(CssProp.B.len_or_perc, "\\s*){1,2}"),
  linear_color_hint: "".concat(CssProp.B.len_or_perc),
  family_name: "".concat(CssProp.B.string, "|(").concat(CssProp.B.ident, "\\s*)+"),
  image_decl: CssProp.B.url,
  left: "".concat(CssProp.B.length, "|auto"),
  loose_quotable_words: "(".concat(CssProp.B.ident, ")+"),
  margin_width: "".concat(CssProp.B.len_or_perc, "|auto"),
  padding_width: "".concat(CssProp.B.length_pos, "|").concat(CssProp.B.percentage_pos),
  page_url: CssProp.B.url,
  position: "((".concat(CssProp.B.len_or_perc, "|left|center|right|top|bottom)\\s*){1,4}"),
  right: "".concat(CssProp.B.length, "|auto"),
  shadow: '',
  size: "closest-side|farthest-side|closest-corner|farthest-corner|".concat(CssProp.B.length, "|(").concat(CssProp.B.len_or_perc, ")\\s+(").concat(CssProp.B.len_or_perc, ")"),
  top: "".concat(CssProp.B.length, "|auto")
};
CssProp._C1 = {
  image_list: "image\\(\\s*(".concat(CssProp.B.url, ")*\\s*(").concat(CssProp.B.url, "|").concat(CssProp._C.color, ")\\s*\\)"),
  linear_color_stop: "(".concat(CssProp._C.color, ")(\\s*").concat(CssProp._C.color_stop_length, ")?"),
  shadow: "((".concat(CssProp._C.color, ")\\s+((").concat(CssProp.B.length, ")\\s*){2,4}(s+inset)?)|((inset\\s+)?((").concat(CssProp.B.length, ")\\s*){2,4}\\s*(").concat(CssProp._C.color, ")?)")
};
CssProp._C2 = {
  color_stop_list: "((".concat(CssProp._C1.linear_color_stop, ")(\\s*(").concat(CssProp._C.linear_color_hint, "))?\\s*,\\s*)+(").concat(CssProp._C1.linear_color_stop, ")"),
  shape: "rect\\(\\s*(".concat(CssProp._C.top, ")\\s*,\\s*(").concat(CssProp._C.right, ")\\s*,\\s*(").concat(CssProp._C.bottom, ")\\s*,\\s*(").concat(CssProp._C.left, ")\\s*\\)")
};
CssProp._C3 = {
  linear_gradient: "linear-gradient\\((((".concat(CssProp.B.angle, ")|to\\s+(").concat(CssProp.A.side_or_corner, "))\\s*,\\s*)?\\s*(").concat(CssProp._C2.color_stop_list, ")\\s*\\)"),
  radial_gradient: "radial-gradient\\(((((".concat(CssProp.A.ending_shape, ")|(").concat(CssProp._C.size, "))\\s*)*\\s*(at\\s+").concat(CssProp._C.position, ")?\\s*,\\s*)?\\s*(").concat(CssProp._C2.color_stop_list, ")\\s*\\)")
};
CssProp._C4 = {
  image: "".concat(CssProp.B.url, "|").concat(CssProp._C3.linear_gradient, "|").concat(CssProp._C3.radial_gradient, "|").concat(CssProp._C1.image_list),
  bg_image: "(".concat(CssProp.B.url, "|").concat(CssProp._C3.linear_gradient, "|").concat(CssProp._C3.radial_gradient, "|").concat(CssProp._C1.image_list, ")|none")
};
CssProp.C = Object.assign(Object.assign(Object.assign(Object.assign(Object.assign({}, CssProp._C), CssProp._C1), CssProp._C2), CssProp._C3), CssProp._C4);
/*
 * Property value regular expressions not dependant on other sub expressions
 */
CssProp.AP = {
  border_collapse: "collapse|separate",
  box: "normal|none|contents",
  box_sizing: "content-box|padding-box|border-box",
  caption_side: "top|bottom",
  clear: "none|left|right|both",
  direction: "ltr|rtl",
  empty_cells: "show|hide",
  "float": "left|right|none",
  font_stretch: "normal|wider|narrower|ultra-condensed|extra-condensed|condensed|semi-condensed|semi-expanded|expanded|extra-expanded|ultra-expanded",
  font_style: "normal|italic|oblique",
  font_variant: "normal|small-caps",
  font_weight: "normal|bold|bolder|lighter|100|200|300|400|500|600|700|800|900",
  list_style_position: "inside|outside",
  list_style_type: "disc|circle|square|decimal|decimal-leading-zero|lower-roman|upper-roman|lower-greek|lower-latin|upper-latin|armenian|georgian|lower-alpha|upper-alpha|none",
  overflow: "visible|hidden|scroll|auto",
  overflow_wrap: "normal|break-word",
  overflow_x: "visible|hidden|scroll|auto|no-display|no-content",
  page_break_after: "auto|always|avoid|left|right",
  page_break_before: "auto|always|avoid|left|right",
  page_break_inside: "avoid|auto",
  position: "static|relative|absolute",
  resize: "none|both|horizontal|vertical",
  speak: "normal|none|spell-out",
  speak_header: "once|always",
  speak_numeral: "digits|continuous",
  speak_punctuation: "code|none",
  table_layout: "auto|fixed",
  text_align: "left|right|center|justify",
  text_decoration: "none|((underline|overline|line-through|blink)\\s*)+",
  text_transform: "capitalize|uppercase|lowercase|none",
  text_wrap: "normal|unrestricted|none|suppress",
  unicode_bidi: "normal|embed|bidi-override",
  visibility: "visible|hidden|collapse",
  white_space: "normal|pre|nowrap|pre-wrap|pre-line",
  word_break: "normal|keep-all|break-all"
};
/*
 * Compound propertiy value regular expressions (i.e. dependant on other sub expressions)
 */
CssProp._CP = {
  background_attachment: "".concat(CssProp.A.attachment, "(,\\s*").concat(CssProp.A.attachment, ")*"),
  background_color: CssProp.C.color,
  background_origin: "".concat(CssProp.A.box, "(,\\s*").concat(CssProp.A.box, ")*"),
  background_repeat: "".concat(CssProp.A.repeat_style, "(,\\s*").concat(CssProp.A.repeat_style, ")*"),
  border: "((".concat(CssProp.C.border_width, "|").concat(CssProp.A.border_style, "|").concat(CssProp.C.color, ")\\s*){1,3}"),
  border_radius: "((".concat(CssProp.B.len_or_perc, ")\\s*){1,4}(\\/\\s*((").concat(CssProp.B.len_or_perc, ")\\s*){1,4})?"),
  border_spacing: "".concat(CssProp.B.length, "\\s*(").concat(CssProp.B.length, ")?"),
  border_top_color: CssProp.C.color,
  border_top_style: CssProp.A.border_style,
  border_width: "((".concat(CssProp.C.border_width, ")\\s*){1,4}"),
  color: CssProp.C.color,
  cursor: "(".concat(CssProp.B.url, "(\\s*,\\s*)?)*(auto|crosshair|default|pointer|move|e-resize|ne-resize|nw-resize|n-resize|se-resize|sw-resize|s-resize|w-resize|text|wait|help|progress|all-scroll|col-resize|hand|no-drop|not-allowed|row-resize|vertical-text)"),
  display: "inline|block|list-item|run-in|inline-list-item|inline-block|table|inline-table|table-cell|table-caption|flex|inline-flex|grid|inline-grid|".concat(CssProp.A.display_inside, "|").concat(CssProp.A.display_outside, "|inherit|inline-box|inline-stack"),
  display_outside: CssProp.A.display_outside,
  elevation: "".concat(CssProp.B.angle, "|below|level|above|higher|lower"),
  font_family: "(".concat(CssProp.C.family_name, "|").concat(CssProp.A.generic_family, ")(,\\s*(").concat(CssProp.C.family_name, "|").concat(CssProp.A.generic_family, "))*"),
  height: "".concat(CssProp.B.length, "|").concat(CssProp.B.percentage, "|auto"),
  letter_spacing: "normal|".concat(CssProp.B.length),
  list_style_image: "".concat(CssProp.C.image, "|none"),
  margin_right: CssProp.C.margin_width,
  max_height: "".concat(CssProp.B.length_pos, "|").concat(CssProp.B.percentage_pos, "|none|auto"),
  min_height: "".concat(CssProp.B.length_pos, "|").concat(CssProp.B.percentage_pos, "|auto"),
  opacity: CssProp.C.alphavalue,
  outline_color: "".concat(CssProp.C.color, "|invert"),
  outline_width: CssProp.C.border_width,
  padding: "((".concat(CssProp.C.padding_width, ")\\s*){1,4}"),
  padding_top: CssProp.C.padding_width,
  pitch_range: CssProp.N.number,
  right: "".concat(CssProp.B.length, "|").concat(CssProp.B.percentage, "|auto"),
  stress: CssProp.N.number,
  text_indent: "".concat(CssProp.B.length, "|").concat(CssProp.B.percentage),
  text_shadow: "none|".concat(CssProp.C.shadow, "(,\\s*(").concat(CssProp.C.shadow, "))*"),
  volume: "".concat(CssProp.N.number_pos, "|").concat(CssProp.B.percentage_pos, "|silent|x-soft|soft|medium|loud|x-loud"),
  word_wrap: CssProp.AP.overflow_wrap,
  zoom: "normal|".concat(CssProp.N.number_pos, "|").concat(CssProp.B.percentage_pos),
  backface_visibility: CssProp.AP.visibility,
  background_clip: "".concat(CssProp.A.box, "(,\\s*(").concat(CssProp.A.box, "))*"),
  background_position: "".concat(CssProp.C.bg_position, "(,\\s*(").concat(CssProp.C.bg_position, "))*"),
  border_bottom_color: CssProp.C.color,
  border_bottom_style: CssProp.A.border_style,
  border_color: "((".concat(CssProp.C.color, ")\\s*){1,4}"),
  border_left_color: CssProp.C.color,
  border_right_color: CssProp.C.color,
  border_style: "((".concat(CssProp.A.border_style, ")\\s*){1,4}"),
  border_top_left_radius: "(".concat(CssProp.B.length, "|").concat(CssProp.B.percentage, ")(\\s*(").concat(CssProp.B.length, "|").concat(CssProp.B.percentage, "))?"),
  border_top_width: CssProp.C.border_width,
  box_shadow: "none|".concat(CssProp.C.shadow, "(,\\s*(").concat(CssProp.C.shadow, "))*"),
  clip: "".concat(CssProp.C.shape, "|auto"),
  display_inside: CssProp.A.display_inside,
  font_size: "".concat(CssProp.A.absolute_size, "|").concat(CssProp.A.relative_size, "|").concat(CssProp.B.length_pos, "|").concat(CssProp.B.percentage_pos),
  line_height: "normal|".concat(CssProp.N.number_pos, "|").concat(CssProp.B.length_pos, "|").concat(CssProp.B.percentage_pos),
  margin_left: CssProp.C.margin_width,
  max_width: "".concat(CssProp.B.length_pos, "|").concat(CssProp.B.percentage_pos, "|none|auto"),
  outline_style: CssProp.A.border_style,
  padding_bottom: CssProp.C.padding_width,
  padding_right: CssProp.C.padding_width,
  perspective: "none|".concat(CssProp.B.length),
  richness: CssProp.N.number,
  text_overflow: "((clip|ellipsis|".concat(CssProp.B.string, ")\\s*){1,2}"),
  top: "".concat(CssProp.B.length, "|").concat(CssProp.B.percentage, "|auto"),
  width: "".concat(CssProp.B.length_pos, "|").concat(CssProp.B.percentage_pos, "|auto"),
  z_index: "auto|".concat(CssProp.B.z_index),
  // Simplified background
  background: "(((".concat(CssProp.C.bg_position, "\\s*(\\/\\s*").concat(CssProp.C.bg_size, ")?)|(").concat(CssProp.A.repeat_style, ")|(").concat(CssProp.A.attachment, ")|(").concat(CssProp.A.bg_origin, ")|(").concat(CssProp.C.bg_image, ")|(").concat(CssProp.C.color, "))\\s*)+"),
  background_size: "".concat(CssProp.C.bg_size, "(,\\s*").concat(CssProp.C.bg_size, ")*"),
  border_bottom_left_radius: "(".concat(CssProp.B.length, "|").concat(CssProp.B.percentage, ")(\\s*(").concat(CssProp.B.length, "|").concat(CssProp.B.percentage, "))?"),
  border_bottom_width: CssProp.C.border_width,
  border_left_style: CssProp.A.border_style,
  border_right_style: CssProp.A.border_style,
  border_top: "((".concat(CssProp.C.border_width, "|").concat(CssProp.A.border_style, "|").concat(CssProp.C.color, ")\\s*){1,3}"),
  bottom: "".concat(CssProp.B.len_or_perc, "|auto"),
  list_style: "((".concat(CssProp.AP.list_style_type, "|").concat(CssProp.AP.list_style_position, "|").concat(CssProp.C.image, "|none})\\s*){1,3}"),
  margin_top: CssProp.C.margin_width,
  outline: "((".concat(CssProp.C.color, "|invert|").concat(CssProp.A.border_style, "|").concat(CssProp.C.border_width, ")\\s*){1,3}"),
  overflow_y: CssProp.AP.overflow_x,
  pitch: "".concat(CssProp.B.frequency, "|x-low|low|medium|high|x-high"),
  vertical_align: "baseline|sub|super|top|text-top|middle|bottom|text-bottom|".concat(CssProp.B.len_or_perc),
  word_spacing: "normal|".concat(CssProp.B.length),
  background_image: "".concat(CssProp.C.bg_image, "(,\\s*").concat(CssProp.C.bg_image, ")*"),
  border_bottom_right_radius: "(".concat(CssProp.B.length, "|").concat(CssProp.B.percentage, ")(\\s*(").concat(CssProp.B.length, "|").concat(CssProp.B.percentage, "))?"),
  border_left_width: CssProp.C.border_width,
  border_right_width: CssProp.C.border_width,
  left: "".concat(CssProp.B.len_or_perc, "|auto"),
  margin_bottom: CssProp.C.margin_width,
  pause_after: "".concat(CssProp.B.time, "|").concat(CssProp.B.percentage),
  speech_rate: "".concat(CssProp.N.number, "|x-slow|slow|medium|fast|x-fast|faster|slower"),
  transition_duration: "".concat(CssProp.B.time, "(,\\s*").concat(CssProp.B.time, ")*"),
  border_bottom: "((".concat(CssProp.C.border_width, "|").concat(CssProp.A.border_style, "|").concat(CssProp.C.color, ")\\s*){1,3}"),
  border_right: "((".concat(CssProp.C.border_width, "|").concat(CssProp.A.border_style, "|").concat(CssProp.C.color, ")\\s*){1,3}"),
  margin: "((".concat(CssProp.C.margin_width, ")\\s*){1,4}"),
  padding_left: CssProp.C.padding_width,
  border_left: "((".concat(CssProp.C.border_width, "|").concat(CssProp.A.border_style, "|").concat(CssProp.C.color, ")\\s*){1,3}"),
  quotes: "(".concat(CssProp.B.string, "\\s*").concat(CssProp.B.string, ")+|none"),
  border_top_right_radius: "(".concat(CssProp.B.length, "|").concat(CssProp.B.percentage, ")(\\s*(").concat(CssProp.B.length, "|").concat(CssProp.B.percentage, "))?"),
  min_width: "".concat(CssProp.B.length_pos, "|").concat(CssProp.B.percentage_pos, "|auto")
};
CssProp._CP1 = {
  font: "(((((".concat(CssProp.AP.font_style, "|").concat(CssProp.AP.font_variant, "|").concat(CssProp.AP.font_weight, ")\\s*){1,3})?\\s*(").concat(CssProp._CP.font_size, ")\\s*(\\/\\s*(").concat(CssProp._CP.line_height, "))?\\s+(").concat(CssProp._CP.font_family, "))|caption|icon|menu|message-box|small-caption|status-bar)")
};
CssProp.CP = Object.assign(Object.assign({}, CssProp._CP), CssProp._CP1);
// CSS Property value validation regular expressions for use with sanitize-html
CssProp.BORDER_COLLAPSE = CssProp.reg(CssProp.AP.border_collapse);
CssProp.BOX = CssProp.reg(CssProp.AP.box);
CssProp.BOX_SIZING = CssProp.reg(CssProp.AP.box_sizing);
CssProp.CAPTION_SIDE = CssProp.reg(CssProp.AP.caption_side);
CssProp.CLEAR = CssProp.reg(CssProp.AP.clear);
CssProp.DIRECTION = CssProp.reg(CssProp.AP.direction);
CssProp.EMPTY_CELLS = CssProp.reg(CssProp.AP.empty_cells);
CssProp.FLOAT = CssProp.reg(CssProp.AP["float"]);
CssProp.FONT_STRETCH = CssProp.reg(CssProp.AP.font_stretch);
CssProp.FONT_STYLE = CssProp.reg(CssProp.AP.font_style);
CssProp.FONT_VARIANT = CssProp.reg(CssProp.AP.font_variant);
CssProp.FONT_WEIGHT = CssProp.reg(CssProp.AP.font_weight);
CssProp.LIST_STYLE_POSITION = CssProp.reg(CssProp.AP.list_style_position);
CssProp.LIST_STYLE_TYPE = CssProp.reg(CssProp.AP.list_style_type);
CssProp.OVERFLOW = CssProp.reg(CssProp.AP.overflow);
CssProp.OVERFLOW_WRAP = CssProp.reg(CssProp.AP.overflow_wrap);
CssProp.OVERFLOW_X = CssProp.reg(CssProp.AP.overflow_x);
CssProp.PAGE_BREAK_AFTER = CssProp.reg(CssProp.AP.page_break_after);
CssProp.PAGE_BREAK_BEFORE = CssProp.reg(CssProp.AP.page_break_before);
CssProp.PAGE_BREAK_INSIDE = CssProp.reg(CssProp.AP.page_break_inside);
CssProp.POSITION = CssProp.reg(CssProp.AP.position);
CssProp.RESIZE = CssProp.reg(CssProp.AP.resize);
CssProp.SPEAK = CssProp.reg(CssProp.AP.speak);
CssProp.SPEAK_HEADER = CssProp.reg(CssProp.AP.speak_header);
CssProp.SPEAK_NUMERAL = CssProp.reg(CssProp.AP.speak_numeral);
CssProp.SPEAK_PUNCTUATION = CssProp.reg(CssProp.AP.speak_punctuation);
CssProp.TABLE_LAYOUT = CssProp.reg(CssProp.AP.table_layout);
CssProp.TEXT_ALIGN = CssProp.reg(CssProp.AP.text_align);
CssProp.TEXT_DECORATION = CssProp.reg(CssProp.AP.text_decoration);
CssProp.TEXT_TRANSFORM = CssProp.reg(CssProp.AP.text_transform);
CssProp.TEXT_WRAP = CssProp.reg(CssProp.AP.text_wrap);
CssProp.UNICODE_BIDI = CssProp.reg(CssProp.AP.unicode_bidi);
CssProp.VISIBILITY = CssProp.reg(CssProp.AP.visibility);
CssProp.WHITE_SPACE = CssProp.reg(CssProp.AP.white_space);
CssProp.WORD_BREAK = CssProp.reg(CssProp.AP.word_break);
CssProp.BACKGROUND_ATTACHMENT = CssProp.reg(CssProp.CP.background_attachment);
CssProp.BACKGROUND_COLOR = CssProp.reg(CssProp.CP.background_color);
CssProp.BACKGROUND_ORIGIN = CssProp.reg(CssProp.CP.background_origin);
CssProp.BACKGROUND_REPEAT = CssProp.reg(CssProp.CP.background_repeat);
CssProp.BORDER = CssProp.reg(CssProp.CP.border);
CssProp.BORDER_RADIUS = CssProp.reg(CssProp.CP.border_radius);
CssProp.BORDER_SPACING = CssProp.reg(CssProp.CP.border_spacing);
CssProp.BORDER_TOP_COLOR = CssProp.reg(CssProp.CP.border_top_color);
CssProp.BORDER_TOP_STYLE = CssProp.reg(CssProp.CP.border_top_style);
CssProp.BORDER_WIDTH = CssProp.reg(CssProp.CP.border_width);
CssProp.COLOR = CssProp.reg(CssProp.CP.color);
CssProp.CURSOR = CssProp.reg(CssProp.CP.cursor);
CssProp.DISPLAY = CssProp.reg(CssProp.CP.display);
CssProp.DISPLAY_OUTSIDE = CssProp.reg(CssProp.CP.display_outside);
CssProp.ELEVATION = CssProp.reg(CssProp.CP.elevation);
CssProp.FONT_FAMILY = CssProp.reg(CssProp.CP.font_family);
CssProp.HEIGHT = CssProp.reg(CssProp.CP.height);
CssProp.LETTER_SPACING = CssProp.reg(CssProp.CP.letter_spacing);
CssProp.LIST_STYLE_IMAGE = CssProp.reg(CssProp.CP.list_style_image);
CssProp.MARGIN_RIGHT = CssProp.reg(CssProp.CP.margin_right);
CssProp.MAX_HEIGHT = CssProp.reg(CssProp.CP.max_height);
CssProp.MIN_HEIGHT = CssProp.reg(CssProp.CP.min_height);
CssProp.OPACITY = CssProp.reg(CssProp.CP.opacity);
CssProp.OUTLINE_COLOR = CssProp.reg(CssProp.CP.outline_color);
CssProp.OUTLINE_WIDTH = CssProp.reg(CssProp.CP.outline_width);
CssProp.PADDING = CssProp.reg(CssProp.CP.padding);
CssProp.PADDING_TOP = CssProp.reg(CssProp.CP.padding_top);
CssProp.PITCH_RANGE = CssProp.reg(CssProp.CP.pitch_range);
CssProp.RIGHT = CssProp.reg(CssProp.CP.right);
CssProp.STRESS = CssProp.reg(CssProp.CP.stress);
CssProp.TEXT_INDENT = CssProp.reg(CssProp.CP.text_indent);
CssProp.TEXT_SHADOW = CssProp.reg(CssProp.CP.text_shadow);
CssProp.VOLUME = CssProp.reg(CssProp.CP.volume);
CssProp.WORD_WRAP = CssProp.reg(CssProp.CP.word_wrap);
CssProp.ZOOM = CssProp.reg(CssProp.CP.zoom);
CssProp.BACKFACE_VISIBILITY = CssProp.reg(CssProp.CP.backface_visibility);
CssProp.BACKGROUND_CLIP = CssProp.reg(CssProp.CP.background_clip);
CssProp.BACKGROUND_POSITION = CssProp.reg(CssProp.CP.background_position);
CssProp.BORDER_BOTTOM_COLOR = CssProp.reg(CssProp.CP.border_bottom_color);
CssProp.BORDER_BOTTOM_STYLE = CssProp.reg(CssProp.CP.border_bottom_style);
CssProp.BORDER_COLOR = CssProp.reg(CssProp.CP.border_color);
CssProp.BORDER_LEFT_COLOR = CssProp.reg(CssProp.CP.border_left_color);
CssProp.BORDER_RIGHT_COLOR = CssProp.reg(CssProp.CP.border_right_color);
CssProp.BORDER_STYLE = CssProp.reg(CssProp.CP.border_style);
CssProp.BORDER_TOP_LEFT_RADIUS = CssProp.reg(CssProp.CP.border_top_left_radius);
CssProp.BORDER_TOP_WIDTH = CssProp.reg(CssProp.CP.border_top_width);
CssProp.BOX_SHADOW = CssProp.reg(CssProp.CP.box_shadow);
CssProp.CLIP = CssProp.reg(CssProp.CP.clip);
CssProp.DISPLAY_INSIDE = CssProp.reg(CssProp.CP.display_inside);
CssProp.FONT_SIZE = CssProp.reg(CssProp.CP.font_size);
CssProp.LINE_HEIGHT = CssProp.reg(CssProp.CP.line_height);
CssProp.MARGIN_LEFT = CssProp.reg(CssProp.CP.margin_left);
CssProp.MAX_WIDTH = CssProp.reg(CssProp.CP.max_width);
CssProp.OUTLINE_STYLE = CssProp.reg(CssProp.CP.outline_style);
CssProp.PADDING_BOTTOM = CssProp.reg(CssProp.CP.padding_bottom);
CssProp.PADDING_RIGHT = CssProp.reg(CssProp.CP.padding_right);
CssProp.PERSPECTIVE = CssProp.reg(CssProp.CP.perspective);
CssProp.RICHNESS = CssProp.reg(CssProp.CP.richness);
CssProp.TEXT_OVERFLOW = CssProp.reg(CssProp.CP.text_overflow);
CssProp.TOP = CssProp.reg(CssProp.CP.top);
CssProp.WIDTH = CssProp.reg(CssProp.CP.width);
CssProp.Z_INDEX = CssProp.reg(CssProp.CP.z_index);
CssProp.BACKGROUND = CssProp.reg(CssProp.CP.background);
CssProp.BACKGROUND_SIZE = CssProp.reg(CssProp.CP.background_size);
CssProp.BORDER_BOTTOM_LEFT_RADIUS = CssProp.reg(CssProp.CP.border_bottom_left_radius);
CssProp.BORDER_BOTTOM_WIDTH = CssProp.reg(CssProp.CP.border_bottom_width);
CssProp.BORDER_LEFT_STYLE = CssProp.reg(CssProp.CP.border_left_style);
CssProp.BORDER_RIGHT_STYLE = CssProp.reg(CssProp.CP.border_right_style);
CssProp.BORDER_TOP = CssProp.reg(CssProp.CP.border_top);
CssProp.BOTTOM = CssProp.reg(CssProp.CP.bottom);
CssProp.LIST_STYLE = CssProp.reg(CssProp.CP.list_style);
CssProp.MARGIN_TOP = CssProp.reg(CssProp.CP.margin_top);
CssProp.OUTLINE = CssProp.reg(CssProp.CP.outline);
CssProp.OVERFLOW_Y = CssProp.reg(CssProp.CP.overflow_y);
CssProp.PITCH = CssProp.reg(CssProp.CP.pitch);
CssProp.VERTICAL_ALIGN = CssProp.reg(CssProp.CP.vertical_align);
CssProp.WORD_SPACING = CssProp.reg(CssProp.CP.word_spacing);
CssProp.BACKGROUND_IMAGE = CssProp.reg(CssProp.CP.background_image);
CssProp.BORDER_BOTTOM_RIGHT_RADIUS = CssProp.reg(CssProp.CP.border_bottom_right_radius);
CssProp.BORDER_LEFT_WIDTH = CssProp.reg(CssProp.CP.border_left_width);
CssProp.BORDER_RIGHT_WIDTH = CssProp.reg(CssProp.CP.border_right_width);
CssProp.LEFT = CssProp.reg(CssProp.CP.left);
CssProp.MARGIN_BOTTOM = CssProp.reg(CssProp.CP.margin_bottom);
CssProp.PAUSE_AFTER = CssProp.reg(CssProp.CP.pause_after);
CssProp.SPEECH_RATE = CssProp.reg(CssProp.CP.speech_rate);
CssProp.TRANSITION_DURATION = CssProp.reg(CssProp.CP.transition_duration);
CssProp.BORDER_BOTTOM = CssProp.reg(CssProp.CP.border_bottom);
CssProp.BORDER_RIGHT = CssProp.reg(CssProp.CP.border_right);
CssProp.MARGIN = CssProp.reg(CssProp.CP.margin);
CssProp.PADDING_LEFT = CssProp.reg(CssProp.CP.padding_left);
CssProp.BORDER_LEFT = CssProp.reg(CssProp.CP.border_left);
CssProp.FONT = CssProp.reg(CssProp.CP.font);
CssProp.QUOTES = CssProp.reg(CssProp.CP.quotes);
CssProp.BORDER_TOP_RIGHT_RADIUS = CssProp.reg(CssProp.CP.border_top_right_radius);
CssProp.MIN_WIDTH = CssProp.reg(CssProp.CP.min_width);
/**
 * A class to sanitize HTML strings.
 */
var Sanitizer = /*#__PURE__*/function () {
  function Sanitizer() {
    _classCallCheck(this, Sanitizer);
    this._options = {
      // HTML tags that are allowed to be used. Tags were extracted from Google Caja
      allowedTags: ['a', 'abbr', 'acronym', 'address', 'area', 'article', 'aside', 'audio', 'b', 'bdi', 'bdo', 'big', 'blockquote', 'br', 'button', 'canvas', 'caption', 'center', 'cite', 'code', 'col', 'colgroup', 'colspan', 'command', 'data', 'datalist', 'dd', 'del', 'details', 'dfn', 'dir', 'div', 'dl', 'dt', 'em', 'fieldset', 'figcaption', 'figure', 'font', 'footer', 'form', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'header', 'hgroup', 'hr', 'i',
      // 'iframe' is allowed by Google Caja, but disallowed by default by sanitize-html
      // , 'iframe'
      'img', 'input', 'ins', 'kbd', 'label', 'legend', 'li', 'map', 'mark', 'menu', 'meter', 'nav', 'nobr', 'ol', 'optgroup', 'option', 'output', 'p', 'pre', 'progress', 'q', 'rowspan', 's', 'samp', 'section', 'select', 'small', 'source', 'span', 'strike', 'strong', 'sub', 'summary', 'sup', 'table', 'tbody', 'td', 'textarea', 'tfoot', 'th', 'thead', 'time', 'tr', 'track', 'tt', 'u', 'ul', 'var', 'video', 'wbr'],
      // Attributes that HTML tags are allowed to have, extracted from Google Caja.
      // See https://github.com/jupyterlab/jupyterlab/issues/1812#issuecomment-285848435
      allowedAttributes: {
        '*': ['class', 'dir', 'draggable', 'hidden', 'id', 'inert', 'itemprop', 'itemref', 'itemscope', 'lang', 'spellcheck', 'style', 'title', 'translate'],
        // 'rel' and 'target' were *not* allowed by Google Caja
        a: ['accesskey', 'coords', 'href', 'hreflang', 'name', 'rel', 'shape', 'tabindex', 'target', 'type'],
        area: ['accesskey', 'alt', 'coords', 'href', 'nohref', 'shape', 'tabindex'],
        // 'autoplay' was *not* allowed by Google Caja
        audio: ['autoplay', 'controls', 'loop', 'mediagroup', 'muted', 'preload', 'src'],
        bdo: ['dir'],
        blockquote: ['cite'],
        br: ['clear'],
        button: ['accesskey', 'data-commandlinker-args', 'data-commandlinker-command', 'disabled', 'name', 'tabindex', 'type', 'value'],
        canvas: ['height', 'width'],
        caption: ['align'],
        col: ['align', 'char', 'charoff', 'span', 'valign', 'width'],
        colgroup: ['align', 'char', 'charoff', 'span', 'valign', 'width'],
        command: ['checked', 'command', 'disabled', 'icon', 'label', 'radiogroup', 'type'],
        data: ['value'],
        del: ['cite', 'datetime'],
        details: ['open'],
        dir: ['compact'],
        div: ['align'],
        dl: ['compact'],
        fieldset: ['disabled'],
        font: ['color', 'face', 'size'],
        form: ['accept', 'autocomplete', 'enctype', 'method', 'name', 'novalidate'],
        h1: ['align'],
        h2: ['align'],
        h3: ['align'],
        h4: ['align'],
        h5: ['align'],
        h6: ['align'],
        hr: ['align', 'noshade', 'size', 'width'],
        iframe: ['align', 'frameborder', 'height', 'marginheight', 'marginwidth', 'width'],
        img: ['align', 'alt', 'border', 'height', 'hspace', 'ismap', 'name', 'src', 'usemap', 'vspace', 'width'],
        input: ['accept', 'accesskey', 'align', 'alt', 'autocomplete', 'checked', 'disabled', 'inputmode', 'ismap', 'list', 'max', 'maxlength', 'min', 'multiple', 'name', 'placeholder', 'readonly', 'required', 'size', 'src', 'step', 'tabindex', 'type', 'usemap', 'value'],
        ins: ['cite', 'datetime'],
        label: ['accesskey', 'for'],
        legend: ['accesskey', 'align'],
        li: ['type', 'value'],
        map: ['name'],
        menu: ['compact', 'label', 'type'],
        meter: ['high', 'low', 'max', 'min', 'value'],
        ol: ['compact', 'reversed', 'start', 'type'],
        optgroup: ['disabled', 'label'],
        option: ['disabled', 'label', 'selected', 'value'],
        output: ['for', 'name'],
        p: ['align'],
        pre: ['width'],
        progress: ['max', 'min', 'value'],
        q: ['cite'],
        select: ['autocomplete', 'disabled', 'multiple', 'name', 'required', 'size', 'tabindex'],
        source: ['type'],
        table: ['align', 'bgcolor', 'border', 'cellpadding', 'cellspacing', 'frame', 'rules', 'summary', 'width'],
        tbody: ['align', 'char', 'charoff', 'valign'],
        td: ['abbr', 'align', 'axis', 'bgcolor', 'char', 'charoff', 'colspan', 'headers', 'height', 'nowrap', 'rowspan', 'scope', 'valign', 'width'],
        textarea: ['accesskey', 'autocomplete', 'cols', 'disabled', 'inputmode', 'name', 'placeholder', 'readonly', 'required', 'rows', 'tabindex', 'wrap'],
        tfoot: ['align', 'char', 'charoff', 'valign'],
        th: ['abbr', 'align', 'axis', 'bgcolor', 'char', 'charoff', 'colspan', 'headers', 'height', 'nowrap', 'rowspan', 'scope', 'valign', 'width'],
        thead: ['align', 'char', 'charoff', 'valign'],
        tr: ['align', 'bgcolor', 'char', 'charoff', 'valign'],
        track: ['default', 'kind', 'label', 'srclang'],
        ul: ['compact', 'type'],
        video: ['autoplay', 'controls', 'height', 'loop', 'mediagroup', 'muted', 'poster', 'preload', 'src', 'width']
      },
      // Inline CSS styles that HTML tags may have (and their allowed values)
      allowedStyles: {
        // To simplify the data, all styles are allowed on all tags that allow the style attribute
        '*': {
          'backface-visibility': [CssProp.BACKFACE_VISIBILITY],
          background: [CssProp.BACKGROUND],
          'background-attachment': [CssProp.BACKGROUND_ATTACHMENT],
          'background-clip': [CssProp.BACKGROUND_CLIP],
          'background-color': [CssProp.BACKGROUND_COLOR],
          'background-image': [CssProp.BACKGROUND_IMAGE],
          'background-origin': [CssProp.BACKGROUND_ORIGIN],
          'background-position': [CssProp.BACKGROUND_POSITION],
          'background-repeat': [CssProp.BACKGROUND_REPEAT],
          'background-size': [CssProp.BACKGROUND_SIZE],
          border: [CssProp.BORDER],
          'border-bottom': [CssProp.BORDER_BOTTOM],
          'border-bottom-color': [CssProp.BORDER_BOTTOM_COLOR],
          'border-bottom-left-radius': [CssProp.BORDER_BOTTOM_LEFT_RADIUS],
          'border-bottom-right-radius': [CssProp.BORDER_BOTTOM_RIGHT_RADIUS],
          'border-bottom-style': [CssProp.BORDER_BOTTOM_STYLE],
          'border-bottom-width': [CssProp.BORDER_BOTTOM_WIDTH],
          'border-collapse': [CssProp.BORDER_COLLAPSE],
          'border-color': [CssProp.BORDER_COLOR],
          'border-left': [CssProp.BORDER_LEFT],
          'border-left-color': [CssProp.BORDER_LEFT_COLOR],
          'border-left-style': [CssProp.BORDER_LEFT_STYLE],
          'border-left-width': [CssProp.BORDER_LEFT_WIDTH],
          'border-radius': [CssProp.BORDER_RADIUS],
          'border-right': [CssProp.BORDER_RIGHT],
          'border-right-color': [CssProp.BORDER_RIGHT_COLOR],
          'border-right-style': [CssProp.BORDER_RIGHT_STYLE],
          'border-right-width': [CssProp.BORDER_RIGHT_WIDTH],
          'border-spacing': [CssProp.BORDER_SPACING],
          'border-style': [CssProp.BORDER_STYLE],
          'border-top': [CssProp.BORDER_TOP],
          'border-top-color': [CssProp.BORDER_TOP_COLOR],
          'border-top-left-radius': [CssProp.BORDER_TOP_LEFT_RADIUS],
          'border-top-right-radius': [CssProp.BORDER_TOP_RIGHT_RADIUS],
          'border-top-style': [CssProp.BORDER_TOP_STYLE],
          'border-top-width': [CssProp.BORDER_TOP_WIDTH],
          'border-width': [CssProp.BORDER_WIDTH],
          bottom: [CssProp.BOTTOM],
          box: [CssProp.BOX],
          'box-shadow': [CssProp.BOX_SHADOW],
          'box-sizing': [CssProp.BOX_SIZING],
          'caption-side': [CssProp.CAPTION_SIDE],
          clear: [CssProp.CLEAR],
          clip: [CssProp.CLIP],
          color: [CssProp.COLOR],
          cursor: [CssProp.CURSOR],
          direction: [CssProp.DIRECTION],
          display: [CssProp.DISPLAY],
          'display-inside': [CssProp.DISPLAY_INSIDE],
          'display-outside': [CssProp.DISPLAY_OUTSIDE],
          elevation: [CssProp.ELEVATION],
          'empty-cells': [CssProp.EMPTY_CELLS],
          "float": [CssProp.FLOAT],
          font: [CssProp.FONT],
          'font-family': [CssProp.FONT_FAMILY],
          'font-size': [CssProp.FONT_SIZE],
          'font-stretch': [CssProp.FONT_STRETCH],
          'font-style': [CssProp.FONT_STYLE],
          'font-variant': [CssProp.FONT_VARIANT],
          'font-weight': [CssProp.FONT_WEIGHT],
          height: [CssProp.HEIGHT],
          left: [CssProp.LEFT],
          'letter-spacing': [CssProp.LETTER_SPACING],
          'line-height': [CssProp.LINE_HEIGHT],
          'list-style': [CssProp.LIST_STYLE],
          'list-style-image': [CssProp.LIST_STYLE_IMAGE],
          'list-style-position': [CssProp.LIST_STYLE_POSITION],
          'list-style-type': [CssProp.LIST_STYLE_TYPE],
          margin: [CssProp.MARGIN],
          'margin-bottom': [CssProp.MARGIN_BOTTOM],
          'margin-left': [CssProp.MARGIN_LEFT],
          'margin-right': [CssProp.MARGIN_RIGHT],
          'margin-top': [CssProp.MARGIN_TOP],
          'max-height': [CssProp.MAX_HEIGHT],
          'max-width': [CssProp.MAX_WIDTH],
          'min-height': [CssProp.MIN_HEIGHT],
          'min-width': [CssProp.MIN_WIDTH],
          opacity: [CssProp.OPACITY],
          outline: [CssProp.OUTLINE],
          'outline-color': [CssProp.OUTLINE_COLOR],
          'outline-style': [CssProp.OUTLINE_STYLE],
          'outline-width': [CssProp.OUTLINE_WIDTH],
          overflow: [CssProp.OVERFLOW],
          'overflow-wrap': [CssProp.OVERFLOW_WRAP],
          'overflow-x': [CssProp.OVERFLOW_X],
          'overflow-y': [CssProp.OVERFLOW_Y],
          padding: [CssProp.PADDING],
          'padding-bottom': [CssProp.PADDING_BOTTOM],
          'padding-left': [CssProp.PADDING_LEFT],
          'padding-right': [CssProp.PADDING_RIGHT],
          'padding-top': [CssProp.PADDING_TOP],
          'page-break-after': [CssProp.PAGE_BREAK_AFTER],
          'page-break-before': [CssProp.PAGE_BREAK_BEFORE],
          'page-break-inside': [CssProp.PAGE_BREAK_INSIDE],
          'pause-after': [CssProp.PAUSE_AFTER],
          perspective: [CssProp.PERSPECTIVE],
          pitch: [CssProp.PITCH],
          'pitch-range': [CssProp.PITCH_RANGE],
          position: [CssProp.POSITION],
          quotes: [CssProp.QUOTES],
          resize: [CssProp.RESIZE],
          richness: [CssProp.RICHNESS],
          right: [CssProp.RIGHT],
          speak: [CssProp.SPEAK],
          'speak-header': [CssProp.SPEAK_HEADER],
          'speak-numeral': [CssProp.SPEAK_NUMERAL],
          'speak-punctuation': [CssProp.SPEAK_PUNCTUATION],
          'speech-rate': [CssProp.SPEECH_RATE],
          stress: [CssProp.STRESS],
          'table-layout': [CssProp.TABLE_LAYOUT],
          'text-align': [CssProp.TEXT_ALIGN],
          'text-decoration': [CssProp.TEXT_DECORATION],
          'text-indent': [CssProp.TEXT_INDENT],
          'text-overflow': [CssProp.TEXT_OVERFLOW],
          'text-shadow': [CssProp.TEXT_SHADOW],
          'text-transform': [CssProp.TEXT_TRANSFORM],
          'text-wrap': [CssProp.TEXT_WRAP],
          top: [CssProp.TOP],
          'unicode-bidi': [CssProp.UNICODE_BIDI],
          'vertical-align': [CssProp.VERTICAL_ALIGN],
          visibility: [CssProp.VISIBILITY],
          volume: [CssProp.VOLUME],
          'white-space': [CssProp.WHITE_SPACE],
          width: [CssProp.WIDTH],
          'word-break': [CssProp.WORD_BREAK],
          'word-spacing': [CssProp.WORD_SPACING],
          'word-wrap': [CssProp.WORD_WRAP],
          'z-index': [CssProp.Z_INDEX],
          zoom: [CssProp.ZOOM]
        }
      },
      transformTags: {
        // Set the "rel" attribute for <a> tags to "nofollow".
        a: sanitize_html__WEBPACK_IMPORTED_MODULE_0___default().simpleTransform('a', {
          rel: 'nofollow'
        }),
        // Set the "disabled" attribute for <input> tags.
        input: sanitize_html__WEBPACK_IMPORTED_MODULE_0___default().simpleTransform('input', {
          disabled: 'disabled'
        })
      },
      allowedSchemesByTag: {
        // Allow 'attachment:' img src (used for markdown cell attachments).
        img: sanitize_html__WEBPACK_IMPORTED_MODULE_0___default().defaults.allowedSchemes.concat(['attachment'])
      },
      // Override of the default option, so we can skip 'src' attribute validation.
      // 'src' Attributes are validated to be URIs, which does not allow for embedded (image) data.
      // Since embedded data is no longer deemed to be a threat, validation can be skipped.
      // See https://github.com/jupyterlab/jupyterlab/issues/5183
      allowedSchemesAppliedToAttributes: ['href', 'cite']
    };
  }
  /**
   * Sanitize an HTML string.
   *
   * @param dirty - The dirty text.
   *
   * @param options - The optional sanitization options.
   *
   * @returns The sanitized string.
   */
  _createClass(Sanitizer, [{
    key: "sanitize",
    value: function sanitize(dirty, options) {
      return sanitize_html__WEBPACK_IMPORTED_MODULE_0___default()(dirty, Object.assign(Object.assign({}, this._options), options || {}));
    }
  }]);
  return Sanitizer;
}();
/**
 * The default instance of an `ISanitizer` meant for use by user code.
 */
var defaultSanitizer = new Sanitizer();
})();

/******/ 	return __webpack_exports__;
/******/ })()
;
});;