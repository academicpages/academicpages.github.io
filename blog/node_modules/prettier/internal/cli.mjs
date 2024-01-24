import { createRequire as __prettierCreateRequire } from "module";
import { fileURLToPath as __prettierFileUrlToPath } from "url";
import { dirname as __prettierDirname } from "path";
const require = __prettierCreateRequire(import.meta.url);
const __filename = __prettierFileUrlToPath(import.meta.url);
const __dirname = __prettierDirname(__filename);

var __create = Object.create;
var __defProp = Object.defineProperty;
var __getOwnPropDesc = Object.getOwnPropertyDescriptor;
var __getOwnPropNames = Object.getOwnPropertyNames;
var __getProtoOf = Object.getPrototypeOf;
var __hasOwnProp = Object.prototype.hasOwnProperty;
var __require = /* @__PURE__ */ ((x) => typeof require !== "undefined" ? require : typeof Proxy !== "undefined" ? new Proxy(x, {
  get: (a, b) => (typeof require !== "undefined" ? require : a)[b]
}) : x)(function(x) {
  if (typeof require !== "undefined")
    return require.apply(this, arguments);
  throw Error('Dynamic require of "' + x + '" is not supported');
});
var __commonJS = (cb, mod) => function __require2() {
  return mod || (0, cb[__getOwnPropNames(cb)[0]])((mod = { exports: {} }).exports, mod), mod.exports;
};
var __copyProps = (to, from, except, desc) => {
  if (from && typeof from === "object" || typeof from === "function") {
    for (let key of __getOwnPropNames(from))
      if (!__hasOwnProp.call(to, key) && key !== except)
        __defProp(to, key, { get: () => from[key], enumerable: !(desc = __getOwnPropDesc(from, key)) || desc.enumerable });
  }
  return to;
};
var __toESM = (mod, isNodeMode, target) => (target = mod != null ? __create(__getProtoOf(mod)) : {}, __copyProps(
  // If the importer is in node compatibility mode or this is not an ESM
  // file that has been converted to a CommonJS file using a Babel-
  // compatible transform (i.e. "__esModule" has not been set), then set
  // "default" to the CommonJS "module.exports" for node compatibility.
  isNodeMode || !mod || !mod.__esModule ? __defProp(target, "default", { value: mod, enumerable: true }) : target,
  mod
));
var __accessCheck = (obj, member, msg) => {
  if (!member.has(obj))
    throw TypeError("Cannot " + msg);
};
var __privateGet = (obj, member, getter) => {
  __accessCheck(obj, member, "read from private field");
  return getter ? getter.call(obj) : member.get(obj);
};
var __privateAdd = (obj, member, value) => {
  if (member.has(obj))
    throw TypeError("Cannot add the same private member more than once");
  member instanceof WeakSet ? member.add(obj) : member.set(obj, value);
};
var __privateSet = (obj, member, value, setter) => {
  __accessCheck(obj, member, "write to private field");
  setter ? setter.call(obj, value) : member.set(obj, value);
  return value;
};

// node_modules/dashify/index.js
var require_dashify = __commonJS({
  "node_modules/dashify/index.js"(exports, module) {
    "use strict";
    module.exports = (str, options) => {
      if (typeof str !== "string")
        throw new TypeError("expected a string");
      return str.trim().replace(/([a-z])([A-Z])/g, "$1-$2").replace(/\W/g, (m) => /[À-ž]/.test(m) ? m : "-").replace(/^-+|-+$/g, "").replace(/-{2,}/g, (m) => options && options.condense ? "-" : m).toLowerCase();
    };
  }
});

// node_modules/minimist/index.js
var require_minimist = __commonJS({
  "node_modules/minimist/index.js"(exports, module) {
    "use strict";
    function hasKey(obj, keys) {
      var o = obj;
      keys.slice(0, -1).forEach(function(key2) {
        o = o[key2] || {};
      });
      var key = keys[keys.length - 1];
      return key in o;
    }
    function isNumber(x) {
      if (typeof x === "number") {
        return true;
      }
      if (/^0x[0-9a-f]+$/i.test(x)) {
        return true;
      }
      return /^[-+]?(?:\d+(?:\.\d*)?|\.\d+)(e[-+]?\d+)?$/.test(x);
    }
    function isConstructorOrProto(obj, key) {
      return key === "constructor" && typeof obj[key] === "function" || key === "__proto__";
    }
    module.exports = function(args, opts) {
      if (!opts) {
        opts = {};
      }
      var flags = {
        bools: {},
        strings: {},
        unknownFn: null
      };
      if (typeof opts.unknown === "function") {
        flags.unknownFn = opts.unknown;
      }
      if (typeof opts.boolean === "boolean" && opts.boolean) {
        flags.allBools = true;
      } else {
        [].concat(opts.boolean).filter(Boolean).forEach(function(key2) {
          flags.bools[key2] = true;
        });
      }
      var aliases = {};
      function aliasIsBoolean(key2) {
        return aliases[key2].some(function(x) {
          return flags.bools[x];
        });
      }
      Object.keys(opts.alias || {}).forEach(function(key2) {
        aliases[key2] = [].concat(opts.alias[key2]);
        aliases[key2].forEach(function(x) {
          aliases[x] = [key2].concat(aliases[key2].filter(function(y) {
            return x !== y;
          }));
        });
      });
      [].concat(opts.string).filter(Boolean).forEach(function(key2) {
        flags.strings[key2] = true;
        if (aliases[key2]) {
          [].concat(aliases[key2]).forEach(function(k) {
            flags.strings[k] = true;
          });
        }
      });
      var defaults = opts.default || {};
      var argv = { _: [] };
      function argDefined(key2, arg2) {
        return flags.allBools && /^--[^=]+$/.test(arg2) || flags.strings[key2] || flags.bools[key2] || aliases[key2];
      }
      function setKey(obj, keys, value2) {
        var o = obj;
        for (var i2 = 0; i2 < keys.length - 1; i2++) {
          var key2 = keys[i2];
          if (isConstructorOrProto(o, key2)) {
            return;
          }
          if (o[key2] === void 0) {
            o[key2] = {};
          }
          if (o[key2] === Object.prototype || o[key2] === Number.prototype || o[key2] === String.prototype) {
            o[key2] = {};
          }
          if (o[key2] === Array.prototype) {
            o[key2] = [];
          }
          o = o[key2];
        }
        var lastKey = keys[keys.length - 1];
        if (isConstructorOrProto(o, lastKey)) {
          return;
        }
        if (o === Object.prototype || o === Number.prototype || o === String.prototype) {
          o = {};
        }
        if (o === Array.prototype) {
          o = [];
        }
        if (o[lastKey] === void 0 || flags.bools[lastKey] || typeof o[lastKey] === "boolean") {
          o[lastKey] = value2;
        } else if (Array.isArray(o[lastKey])) {
          o[lastKey].push(value2);
        } else {
          o[lastKey] = [o[lastKey], value2];
        }
      }
      function setArg(key2, val, arg2) {
        if (arg2 && flags.unknownFn && !argDefined(key2, arg2)) {
          if (flags.unknownFn(arg2) === false) {
            return;
          }
        }
        var value2 = !flags.strings[key2] && isNumber(val) ? Number(val) : val;
        setKey(argv, key2.split("."), value2);
        (aliases[key2] || []).forEach(function(x) {
          setKey(argv, x.split("."), value2);
        });
      }
      Object.keys(flags.bools).forEach(function(key2) {
        setArg(key2, defaults[key2] === void 0 ? false : defaults[key2]);
      });
      var notFlags = [];
      if (args.indexOf("--") !== -1) {
        notFlags = args.slice(args.indexOf("--") + 1);
        args = args.slice(0, args.indexOf("--"));
      }
      for (var i = 0; i < args.length; i++) {
        var arg = args[i];
        var key;
        var next;
        if (/^--.+=/.test(arg)) {
          var m = arg.match(/^--([^=]+)=([\s\S]*)$/);
          key = m[1];
          var value = m[2];
          if (flags.bools[key]) {
            value = value !== "false";
          }
          setArg(key, value, arg);
        } else if (/^--no-.+/.test(arg)) {
          key = arg.match(/^--no-(.+)/)[1];
          setArg(key, false, arg);
        } else if (/^--.+/.test(arg)) {
          key = arg.match(/^--(.+)/)[1];
          next = args[i + 1];
          if (next !== void 0 && !/^(-|--)[^-]/.test(next) && !flags.bools[key] && !flags.allBools && (aliases[key] ? !aliasIsBoolean(key) : true)) {
            setArg(key, next, arg);
            i += 1;
          } else if (/^(true|false)$/.test(next)) {
            setArg(key, next === "true", arg);
            i += 1;
          } else {
            setArg(key, flags.strings[key] ? "" : true, arg);
          }
        } else if (/^-[^-]+/.test(arg)) {
          var letters = arg.slice(1, -1).split("");
          var broken = false;
          for (var j = 0; j < letters.length; j++) {
            next = arg.slice(j + 2);
            if (next === "-") {
              setArg(letters[j], next, arg);
              continue;
            }
            if (/[A-Za-z]/.test(letters[j]) && next[0] === "=") {
              setArg(letters[j], next.slice(1), arg);
              broken = true;
              break;
            }
            if (/[A-Za-z]/.test(letters[j]) && /-?\d+(\.\d*)?(e-?\d+)?$/.test(next)) {
              setArg(letters[j], next, arg);
              broken = true;
              break;
            }
            if (letters[j + 1] && letters[j + 1].match(/\W/)) {
              setArg(letters[j], arg.slice(j + 2), arg);
              broken = true;
              break;
            } else {
              setArg(letters[j], flags.strings[letters[j]] ? "" : true, arg);
            }
          }
          key = arg.slice(-1)[0];
          if (!broken && key !== "-") {
            if (args[i + 1] && !/^(-|--)[^-]/.test(args[i + 1]) && !flags.bools[key] && (aliases[key] ? !aliasIsBoolean(key) : true)) {
              setArg(key, args[i + 1], arg);
              i += 1;
            } else if (args[i + 1] && /^(true|false)$/.test(args[i + 1])) {
              setArg(key, args[i + 1] === "true", arg);
              i += 1;
            } else {
              setArg(key, flags.strings[key] ? "" : true, arg);
            }
          }
        } else {
          if (!flags.unknownFn || flags.unknownFn(arg) !== false) {
            argv._.push(flags.strings._ || !isNumber(arg) ? arg : Number(arg));
          }
          if (opts.stopEarly) {
            argv._.push.apply(argv._, args.slice(i + 1));
            break;
          }
        }
      }
      Object.keys(defaults).forEach(function(k) {
        if (!hasKey(argv, k.split("."))) {
          setKey(argv, k.split("."), defaults[k]);
          (aliases[k] || []).forEach(function(x) {
            setKey(argv, x.split("."), defaults[k]);
          });
        }
      });
      if (opts["--"]) {
        argv["--"] = notFlags.slice();
      } else {
        notFlags.forEach(function(k) {
          argv._.push(k);
        });
      }
      return argv;
    };
  }
});

// node_modules/fast-json-stable-stringify/index.js
var require_fast_json_stable_stringify = __commonJS({
  "node_modules/fast-json-stable-stringify/index.js"(exports, module) {
    "use strict";
    module.exports = function(data, opts) {
      if (!opts)
        opts = {};
      if (typeof opts === "function")
        opts = { cmp: opts };
      var cycles = typeof opts.cycles === "boolean" ? opts.cycles : false;
      var cmp = opts.cmp && /* @__PURE__ */ function(f) {
        return function(node) {
          return function(a, b) {
            var aobj = { key: a, value: node[a] };
            var bobj = { key: b, value: node[b] };
            return f(aobj, bobj);
          };
        };
      }(opts.cmp);
      var seen = [];
      return function stringify4(node) {
        if (node && node.toJSON && typeof node.toJSON === "function") {
          node = node.toJSON();
        }
        if (node === void 0)
          return;
        if (typeof node == "number")
          return isFinite(node) ? "" + node : "null";
        if (typeof node !== "object")
          return JSON.stringify(node);
        var i, out;
        if (Array.isArray(node)) {
          out = "[";
          for (i = 0; i < node.length; i++) {
            if (i)
              out += ",";
            out += stringify4(node[i]) || "null";
          }
          return out + "]";
        }
        if (node === null)
          return "null";
        if (seen.indexOf(node) !== -1) {
          if (cycles)
            return JSON.stringify("__cycle__");
          throw new TypeError("Converting circular structure to JSON");
        }
        var seenIndex = seen.push(node) - 1;
        var keys = Object.keys(node).sort(cmp && cmp(node));
        out = "";
        for (i = 0; i < keys.length; i++) {
          var key = keys[i];
          var value = stringify4(node[key]);
          if (!value)
            continue;
          if (out)
            out += ",";
          out += JSON.stringify(key) + ":" + value;
        }
        seen.splice(seenIndex, 1);
        return "{" + out + "}";
      }(data);
    };
  }
});

// node_modules/diff/lib/diff/base.js
var require_base = __commonJS({
  "node_modules/diff/lib/diff/base.js"(exports) {
    "use strict";
    Object.defineProperty(exports, "__esModule", {
      value: true
    });
    exports["default"] = Diff;
    function Diff() {
    }
    Diff.prototype = {
      /*istanbul ignore start*/
      /*istanbul ignore end*/
      diff: function diff2(oldString, newString) {
        var options = arguments.length > 2 && arguments[2] !== void 0 ? arguments[2] : {};
        var callback = options.callback;
        if (typeof options === "function") {
          callback = options;
          options = {};
        }
        this.options = options;
        var self = this;
        function done(value) {
          if (callback) {
            setTimeout(function() {
              callback(void 0, value);
            }, 0);
            return true;
          } else {
            return value;
          }
        }
        oldString = this.castInput(oldString);
        newString = this.castInput(newString);
        oldString = this.removeEmpty(this.tokenize(oldString));
        newString = this.removeEmpty(this.tokenize(newString));
        var newLen = newString.length, oldLen = oldString.length;
        var editLength = 1;
        var maxEditLength = newLen + oldLen;
        if (options.maxEditLength) {
          maxEditLength = Math.min(maxEditLength, options.maxEditLength);
        }
        var bestPath = [{
          newPos: -1,
          components: []
        }];
        var oldPos = this.extractCommon(bestPath[0], newString, oldString, 0);
        if (bestPath[0].newPos + 1 >= newLen && oldPos + 1 >= oldLen) {
          return done([{
            value: this.join(newString),
            count: newString.length
          }]);
        }
        function execEditLength() {
          for (var diagonalPath = -1 * editLength; diagonalPath <= editLength; diagonalPath += 2) {
            var basePath = (
              /*istanbul ignore start*/
              void 0
            );
            var addPath = bestPath[diagonalPath - 1], removePath = bestPath[diagonalPath + 1], _oldPos = (removePath ? removePath.newPos : 0) - diagonalPath;
            if (addPath) {
              bestPath[diagonalPath - 1] = void 0;
            }
            var canAdd = addPath && addPath.newPos + 1 < newLen, canRemove = removePath && 0 <= _oldPos && _oldPos < oldLen;
            if (!canAdd && !canRemove) {
              bestPath[diagonalPath] = void 0;
              continue;
            }
            if (!canAdd || canRemove && addPath.newPos < removePath.newPos) {
              basePath = clonePath(removePath);
              self.pushComponent(basePath.components, void 0, true);
            } else {
              basePath = addPath;
              basePath.newPos++;
              self.pushComponent(basePath.components, true, void 0);
            }
            _oldPos = self.extractCommon(basePath, newString, oldString, diagonalPath);
            if (basePath.newPos + 1 >= newLen && _oldPos + 1 >= oldLen) {
              return done(buildValues(self, basePath.components, newString, oldString, self.useLongestToken));
            } else {
              bestPath[diagonalPath] = basePath;
            }
          }
          editLength++;
        }
        if (callback) {
          (function exec() {
            setTimeout(function() {
              if (editLength > maxEditLength) {
                return callback();
              }
              if (!execEditLength()) {
                exec();
              }
            }, 0);
          })();
        } else {
          while (editLength <= maxEditLength) {
            var ret = execEditLength();
            if (ret) {
              return ret;
            }
          }
        }
      },
      /*istanbul ignore start*/
      /*istanbul ignore end*/
      pushComponent: function pushComponent(components, added, removed) {
        var last = components[components.length - 1];
        if (last && last.added === added && last.removed === removed) {
          components[components.length - 1] = {
            count: last.count + 1,
            added,
            removed
          };
        } else {
          components.push({
            count: 1,
            added,
            removed
          });
        }
      },
      /*istanbul ignore start*/
      /*istanbul ignore end*/
      extractCommon: function extractCommon(basePath, newString, oldString, diagonalPath) {
        var newLen = newString.length, oldLen = oldString.length, newPos = basePath.newPos, oldPos = newPos - diagonalPath, commonCount = 0;
        while (newPos + 1 < newLen && oldPos + 1 < oldLen && this.equals(newString[newPos + 1], oldString[oldPos + 1])) {
          newPos++;
          oldPos++;
          commonCount++;
        }
        if (commonCount) {
          basePath.components.push({
            count: commonCount
          });
        }
        basePath.newPos = newPos;
        return oldPos;
      },
      /*istanbul ignore start*/
      /*istanbul ignore end*/
      equals: function equals(left, right) {
        if (this.options.comparator) {
          return this.options.comparator(left, right);
        } else {
          return left === right || this.options.ignoreCase && left.toLowerCase() === right.toLowerCase();
        }
      },
      /*istanbul ignore start*/
      /*istanbul ignore end*/
      removeEmpty: function removeEmpty(array2) {
        var ret = [];
        for (var i = 0; i < array2.length; i++) {
          if (array2[i]) {
            ret.push(array2[i]);
          }
        }
        return ret;
      },
      /*istanbul ignore start*/
      /*istanbul ignore end*/
      castInput: function castInput(value) {
        return value;
      },
      /*istanbul ignore start*/
      /*istanbul ignore end*/
      tokenize: function tokenize(value) {
        return value.split("");
      },
      /*istanbul ignore start*/
      /*istanbul ignore end*/
      join: function join(chars) {
        return chars.join("");
      }
    };
    function buildValues(diff2, components, newString, oldString, useLongestToken) {
      var componentPos = 0, componentLen = components.length, newPos = 0, oldPos = 0;
      for (; componentPos < componentLen; componentPos++) {
        var component = components[componentPos];
        if (!component.removed) {
          if (!component.added && useLongestToken) {
            var value = newString.slice(newPos, newPos + component.count);
            value = value.map(function(value2, i) {
              var oldValue = oldString[oldPos + i];
              return oldValue.length > value2.length ? oldValue : value2;
            });
            component.value = diff2.join(value);
          } else {
            component.value = diff2.join(newString.slice(newPos, newPos + component.count));
          }
          newPos += component.count;
          if (!component.added) {
            oldPos += component.count;
          }
        } else {
          component.value = diff2.join(oldString.slice(oldPos, oldPos + component.count));
          oldPos += component.count;
          if (componentPos && components[componentPos - 1].added) {
            var tmp = components[componentPos - 1];
            components[componentPos - 1] = components[componentPos];
            components[componentPos] = tmp;
          }
        }
      }
      var lastComponent = components[componentLen - 1];
      if (componentLen > 1 && typeof lastComponent.value === "string" && (lastComponent.added || lastComponent.removed) && diff2.equals("", lastComponent.value)) {
        components[componentLen - 2].value += lastComponent.value;
        components.pop();
      }
      return components;
    }
    function clonePath(path10) {
      return {
        newPos: path10.newPos,
        components: path10.components.slice(0)
      };
    }
  }
});

// node_modules/diff/lib/util/params.js
var require_params = __commonJS({
  "node_modules/diff/lib/util/params.js"(exports) {
    "use strict";
    Object.defineProperty(exports, "__esModule", {
      value: true
    });
    exports.generateOptions = generateOptions;
    function generateOptions(options, defaults) {
      if (typeof options === "function") {
        defaults.callback = options;
      } else if (options) {
        for (var name in options) {
          if (options.hasOwnProperty(name)) {
            defaults[name] = options[name];
          }
        }
      }
      return defaults;
    }
  }
});

// node_modules/diff/lib/diff/line.js
var require_line = __commonJS({
  "node_modules/diff/lib/diff/line.js"(exports) {
    "use strict";
    Object.defineProperty(exports, "__esModule", {
      value: true
    });
    exports.diffLines = diffLines;
    exports.diffTrimmedLines = diffTrimmedLines;
    exports.lineDiff = void 0;
    var _base = _interopRequireDefault(require_base());
    var _params = require_params();
    function _interopRequireDefault(obj) {
      return obj && obj.__esModule ? obj : { "default": obj };
    }
    var lineDiff = new /*istanbul ignore start*/
    _base[
      /*istanbul ignore start*/
      "default"
      /*istanbul ignore end*/
    ]();
    exports.lineDiff = lineDiff;
    lineDiff.tokenize = function(value) {
      var retLines = [], linesAndNewlines = value.split(/(\n|\r\n)/);
      if (!linesAndNewlines[linesAndNewlines.length - 1]) {
        linesAndNewlines.pop();
      }
      for (var i = 0; i < linesAndNewlines.length; i++) {
        var line = linesAndNewlines[i];
        if (i % 2 && !this.options.newlineIsToken) {
          retLines[retLines.length - 1] += line;
        } else {
          if (this.options.ignoreWhitespace) {
            line = line.trim();
          }
          retLines.push(line);
        }
      }
      return retLines;
    };
    function diffLines(oldStr, newStr, callback) {
      return lineDiff.diff(oldStr, newStr, callback);
    }
    function diffTrimmedLines(oldStr, newStr, callback) {
      var options = (
        /*istanbul ignore start*/
        (0, /*istanbul ignore end*/
        /*istanbul ignore start*/
        _params.generateOptions)(callback, {
          ignoreWhitespace: true
        })
      );
      return lineDiff.diff(oldStr, newStr, options);
    }
  }
});

// node_modules/diff/lib/patch/create.js
var require_create = __commonJS({
  "node_modules/diff/lib/patch/create.js"(exports) {
    "use strict";
    Object.defineProperty(exports, "__esModule", {
      value: true
    });
    exports.structuredPatch = structuredPatch;
    exports.formatPatch = formatPatch;
    exports.createTwoFilesPatch = createTwoFilesPatch2;
    exports.createPatch = createPatch;
    var _line = require_line();
    function _toConsumableArray(arr) {
      return _arrayWithoutHoles(arr) || _iterableToArray(arr) || _unsupportedIterableToArray(arr) || _nonIterableSpread();
    }
    function _nonIterableSpread() {
      throw new TypeError("Invalid attempt to spread non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method.");
    }
    function _unsupportedIterableToArray(o, minLen) {
      if (!o)
        return;
      if (typeof o === "string")
        return _arrayLikeToArray(o, minLen);
      var n = Object.prototype.toString.call(o).slice(8, -1);
      if (n === "Object" && o.constructor)
        n = o.constructor.name;
      if (n === "Map" || n === "Set")
        return Array.from(o);
      if (n === "Arguments" || /^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(n))
        return _arrayLikeToArray(o, minLen);
    }
    function _iterableToArray(iter) {
      if (typeof Symbol !== "undefined" && Symbol.iterator in Object(iter))
        return Array.from(iter);
    }
    function _arrayWithoutHoles(arr) {
      if (Array.isArray(arr))
        return _arrayLikeToArray(arr);
    }
    function _arrayLikeToArray(arr, len) {
      if (len == null || len > arr.length)
        len = arr.length;
      for (var i = 0, arr2 = new Array(len); i < len; i++) {
        arr2[i] = arr[i];
      }
      return arr2;
    }
    function structuredPatch(oldFileName, newFileName, oldStr, newStr, oldHeader, newHeader, options) {
      if (!options) {
        options = {};
      }
      if (typeof options.context === "undefined") {
        options.context = 4;
      }
      var diff2 = (
        /*istanbul ignore start*/
        (0, /*istanbul ignore end*/
        /*istanbul ignore start*/
        _line.diffLines)(oldStr, newStr, options)
      );
      if (!diff2) {
        return;
      }
      diff2.push({
        value: "",
        lines: []
      });
      function contextLines(lines) {
        return lines.map(function(entry) {
          return " " + entry;
        });
      }
      var hunks = [];
      var oldRangeStart = 0, newRangeStart = 0, curRange = [], oldLine = 1, newLine = 1;
      var _loop = function _loop2(i2) {
        var current = diff2[i2], lines = current.lines || current.value.replace(/\n$/, "").split("\n");
        current.lines = lines;
        if (current.added || current.removed) {
          var _curRange;
          if (!oldRangeStart) {
            var prev = diff2[i2 - 1];
            oldRangeStart = oldLine;
            newRangeStart = newLine;
            if (prev) {
              curRange = options.context > 0 ? contextLines(prev.lines.slice(-options.context)) : [];
              oldRangeStart -= curRange.length;
              newRangeStart -= curRange.length;
            }
          }
          (_curRange = /*istanbul ignore end*/
          curRange).push.apply(
            /*istanbul ignore start*/
            _curRange,
            /*istanbul ignore start*/
            _toConsumableArray(
              /*istanbul ignore end*/
              lines.map(function(entry) {
                return (current.added ? "+" : "-") + entry;
              })
            )
          );
          if (current.added) {
            newLine += lines.length;
          } else {
            oldLine += lines.length;
          }
        } else {
          if (oldRangeStart) {
            if (lines.length <= options.context * 2 && i2 < diff2.length - 2) {
              var _curRange2;
              (_curRange2 = /*istanbul ignore end*/
              curRange).push.apply(
                /*istanbul ignore start*/
                _curRange2,
                /*istanbul ignore start*/
                _toConsumableArray(
                  /*istanbul ignore end*/
                  contextLines(lines)
                )
              );
            } else {
              var _curRange3;
              var contextSize = Math.min(lines.length, options.context);
              (_curRange3 = /*istanbul ignore end*/
              curRange).push.apply(
                /*istanbul ignore start*/
                _curRange3,
                /*istanbul ignore start*/
                _toConsumableArray(
                  /*istanbul ignore end*/
                  contextLines(lines.slice(0, contextSize))
                )
              );
              var hunk = {
                oldStart: oldRangeStart,
                oldLines: oldLine - oldRangeStart + contextSize,
                newStart: newRangeStart,
                newLines: newLine - newRangeStart + contextSize,
                lines: curRange
              };
              if (i2 >= diff2.length - 2 && lines.length <= options.context) {
                var oldEOFNewline = /\n$/.test(oldStr);
                var newEOFNewline = /\n$/.test(newStr);
                var noNlBeforeAdds = lines.length == 0 && curRange.length > hunk.oldLines;
                if (!oldEOFNewline && noNlBeforeAdds && oldStr.length > 0) {
                  curRange.splice(hunk.oldLines, 0, "\\ No newline at end of file");
                }
                if (!oldEOFNewline && !noNlBeforeAdds || !newEOFNewline) {
                  curRange.push("\\ No newline at end of file");
                }
              }
              hunks.push(hunk);
              oldRangeStart = 0;
              newRangeStart = 0;
              curRange = [];
            }
          }
          oldLine += lines.length;
          newLine += lines.length;
        }
      };
      for (var i = 0; i < diff2.length; i++) {
        _loop(
          /*istanbul ignore end*/
          i
        );
      }
      return {
        oldFileName,
        newFileName,
        oldHeader,
        newHeader,
        hunks
      };
    }
    function formatPatch(diff2) {
      var ret = [];
      if (diff2.oldFileName == diff2.newFileName) {
        ret.push("Index: " + diff2.oldFileName);
      }
      ret.push("===================================================================");
      ret.push("--- " + diff2.oldFileName + (typeof diff2.oldHeader === "undefined" ? "" : "	" + diff2.oldHeader));
      ret.push("+++ " + diff2.newFileName + (typeof diff2.newHeader === "undefined" ? "" : "	" + diff2.newHeader));
      for (var i = 0; i < diff2.hunks.length; i++) {
        var hunk = diff2.hunks[i];
        if (hunk.oldLines === 0) {
          hunk.oldStart -= 1;
        }
        if (hunk.newLines === 0) {
          hunk.newStart -= 1;
        }
        ret.push("@@ -" + hunk.oldStart + "," + hunk.oldLines + " +" + hunk.newStart + "," + hunk.newLines + " @@");
        ret.push.apply(ret, hunk.lines);
      }
      return ret.join("\n") + "\n";
    }
    function createTwoFilesPatch2(oldFileName, newFileName, oldStr, newStr, oldHeader, newHeader, options) {
      return formatPatch(structuredPatch(oldFileName, newFileName, oldStr, newStr, oldHeader, newHeader, options));
    }
    function createPatch(fileName, oldStr, newStr, oldHeader, newHeader, options) {
      return createTwoFilesPatch2(fileName, fileName, oldStr, newStr, oldHeader, newHeader, options);
    }
  }
});

// node_modules/common-path-prefix/index.js
var require_common_path_prefix = __commonJS({
  "node_modules/common-path-prefix/index.js"(exports, module) {
    "use strict";
    var { sep: DEFAULT_SEPARATOR } = __require("path");
    var determineSeparator = (paths) => {
      for (const path10 of paths) {
        const match = /(\/|\\)/.exec(path10);
        if (match !== null)
          return match[0];
      }
      return DEFAULT_SEPARATOR;
    };
    module.exports = function commonPathPrefix2(paths, sep = determineSeparator(paths)) {
      const [first = "", ...remaining] = paths;
      if (first === "" || remaining.length === 0)
        return "";
      const parts = first.split(sep);
      let endOfPrefix = parts.length;
      for (const path10 of remaining) {
        const compare = path10.split(sep);
        for (let i = 0; i < endOfPrefix; i++) {
          if (compare[i] !== parts[i]) {
            endOfPrefix = i;
          }
        }
        if (endOfPrefix === 0)
          return "";
      }
      const prefix = parts.slice(0, endOfPrefix).join(sep);
      return prefix.endsWith(sep) ? prefix : prefix + sep;
    };
  }
});

// node_modules/json-buffer/index.js
var require_json_buffer = __commonJS({
  "node_modules/json-buffer/index.js"(exports) {
    exports.stringify = function stringify4(o) {
      if ("undefined" == typeof o)
        return o;
      if (o && Buffer.isBuffer(o))
        return JSON.stringify(":base64:" + o.toString("base64"));
      if (o && o.toJSON)
        o = o.toJSON();
      if (o && "object" === typeof o) {
        var s = "";
        var array2 = Array.isArray(o);
        s = array2 ? "[" : "{";
        var first = true;
        for (var k in o) {
          var ignore = "function" == typeof o[k] || !array2 && "undefined" === typeof o[k];
          if (Object.hasOwnProperty.call(o, k) && !ignore) {
            if (!first)
              s += ",";
            first = false;
            if (array2) {
              if (o[k] == void 0)
                s += "null";
              else
                s += stringify4(o[k]);
            } else if (o[k] !== void 0) {
              s += stringify4(k) + ":" + stringify4(o[k]);
            }
          }
        }
        s += array2 ? "]" : "}";
        return s;
      } else if ("string" === typeof o) {
        return JSON.stringify(/^:/.test(o) ? ":" + o : o);
      } else if ("undefined" === typeof o) {
        return "null";
      } else
        return JSON.stringify(o);
    };
    exports.parse = function(s) {
      return JSON.parse(s, function(key, value) {
        if ("string" === typeof value) {
          if (/^:base64:/.test(value))
            return Buffer.from(value.substring(8), "base64");
          else
            return /^:/.test(value) ? value.substring(1) : value;
        }
        return value;
      });
    };
  }
});

// node_modules/keyv/src/index.js
var require_src = __commonJS({
  "node_modules/keyv/src/index.js"(exports, module) {
    "use strict";
    var EventEmitter = __require("events");
    var JSONB = require_json_buffer();
    var loadStore = (options) => {
      const adapters = {
        redis: "@keyv/redis",
        rediss: "@keyv/redis",
        mongodb: "@keyv/mongo",
        mongo: "@keyv/mongo",
        sqlite: "@keyv/sqlite",
        postgresql: "@keyv/postgres",
        postgres: "@keyv/postgres",
        mysql: "@keyv/mysql",
        etcd: "@keyv/etcd",
        offline: "@keyv/offline",
        tiered: "@keyv/tiered"
      };
      if (options.adapter || options.uri) {
        const adapter = options.adapter || /^[^:+]*/.exec(options.uri)[0];
        return new (__require(adapters[adapter]))(options);
      }
      return /* @__PURE__ */ new Map();
    };
    var iterableAdapters = [
      "sqlite",
      "postgres",
      "mysql",
      "mongo",
      "redis",
      "tiered"
    ];
    var Keyv = class extends EventEmitter {
      constructor(uri, { emitErrors = true, ...options } = {}) {
        super();
        this.opts = {
          namespace: "keyv",
          serialize: JSONB.stringify,
          deserialize: JSONB.parse,
          ...typeof uri === "string" ? { uri } : uri,
          ...options
        };
        if (!this.opts.store) {
          const adapterOptions = { ...this.opts };
          this.opts.store = loadStore(adapterOptions);
        }
        if (this.opts.compression) {
          const compression = this.opts.compression;
          this.opts.serialize = compression.serialize.bind(compression);
          this.opts.deserialize = compression.deserialize.bind(compression);
        }
        if (typeof this.opts.store.on === "function" && emitErrors) {
          this.opts.store.on("error", (error) => this.emit("error", error));
        }
        this.opts.store.namespace = this.opts.namespace;
        const generateIterator = (iterator) => async function* () {
          for await (const [key, raw] of typeof iterator === "function" ? iterator(this.opts.store.namespace) : iterator) {
            const data = await this.opts.deserialize(raw);
            if (this.opts.store.namespace && !key.includes(this.opts.store.namespace)) {
              continue;
            }
            if (typeof data.expires === "number" && Date.now() > data.expires) {
              this.delete(key);
              continue;
            }
            yield [this._getKeyUnprefix(key), data.value];
          }
        };
        if (typeof this.opts.store[Symbol.iterator] === "function" && this.opts.store instanceof Map) {
          this.iterator = generateIterator(this.opts.store);
        } else if (typeof this.opts.store.iterator === "function" && this.opts.store.opts && this._checkIterableAdaptar()) {
          this.iterator = generateIterator(this.opts.store.iterator.bind(this.opts.store));
        }
      }
      _checkIterableAdaptar() {
        return iterableAdapters.includes(this.opts.store.opts.dialect) || iterableAdapters.findIndex((element) => this.opts.store.opts.url.includes(element)) >= 0;
      }
      _getKeyPrefix(key) {
        return `${this.opts.namespace}:${key}`;
      }
      _getKeyPrefixArray(keys) {
        return keys.map((key) => `${this.opts.namespace}:${key}`);
      }
      _getKeyUnprefix(key) {
        return key.split(":").splice(1).join(":");
      }
      get(key, options) {
        const { store } = this.opts;
        const isArray = Array.isArray(key);
        const keyPrefixed = isArray ? this._getKeyPrefixArray(key) : this._getKeyPrefix(key);
        if (isArray && store.getMany === void 0) {
          const promises = [];
          for (const key2 of keyPrefixed) {
            promises.push(
              Promise.resolve().then(() => store.get(key2)).then((data) => typeof data === "string" ? this.opts.deserialize(data) : this.opts.compression ? this.opts.deserialize(data) : data).then((data) => {
                if (data === void 0 || data === null) {
                  return void 0;
                }
                if (typeof data.expires === "number" && Date.now() > data.expires) {
                  return this.delete(key2).then(() => void 0);
                }
                return options && options.raw ? data : data.value;
              })
            );
          }
          return Promise.allSettled(promises).then((values) => {
            const data = [];
            for (const value of values) {
              data.push(value.value);
            }
            return data;
          });
        }
        return Promise.resolve().then(() => isArray ? store.getMany(keyPrefixed) : store.get(keyPrefixed)).then((data) => typeof data === "string" ? this.opts.deserialize(data) : this.opts.compression ? this.opts.deserialize(data) : data).then((data) => {
          if (data === void 0 || data === null) {
            return void 0;
          }
          if (isArray) {
            return data.map((row, index) => {
              if (typeof row === "string") {
                row = this.opts.deserialize(row);
              }
              if (row === void 0 || row === null) {
                return void 0;
              }
              if (typeof row.expires === "number" && Date.now() > row.expires) {
                this.delete(key[index]).then(() => void 0);
                return void 0;
              }
              return options && options.raw ? row : row.value;
            });
          }
          if (typeof data.expires === "number" && Date.now() > data.expires) {
            return this.delete(key).then(() => void 0);
          }
          return options && options.raw ? data : data.value;
        });
      }
      set(key, value, ttl) {
        const keyPrefixed = this._getKeyPrefix(key);
        if (typeof ttl === "undefined") {
          ttl = this.opts.ttl;
        }
        if (ttl === 0) {
          ttl = void 0;
        }
        const { store } = this.opts;
        return Promise.resolve().then(() => {
          const expires = typeof ttl === "number" ? Date.now() + ttl : null;
          if (typeof value === "symbol") {
            this.emit("error", "symbol cannot be serialized");
          }
          value = { value, expires };
          return this.opts.serialize(value);
        }).then((value2) => store.set(keyPrefixed, value2, ttl)).then(() => true);
      }
      delete(key) {
        const { store } = this.opts;
        if (Array.isArray(key)) {
          const keyPrefixed2 = this._getKeyPrefixArray(key);
          if (store.deleteMany === void 0) {
            const promises = [];
            for (const key2 of keyPrefixed2) {
              promises.push(store.delete(key2));
            }
            return Promise.allSettled(promises).then((values) => values.every((x) => x.value === true));
          }
          return Promise.resolve().then(() => store.deleteMany(keyPrefixed2));
        }
        const keyPrefixed = this._getKeyPrefix(key);
        return Promise.resolve().then(() => store.delete(keyPrefixed));
      }
      clear() {
        const { store } = this.opts;
        return Promise.resolve().then(() => store.clear());
      }
      has(key) {
        const keyPrefixed = this._getKeyPrefix(key);
        const { store } = this.opts;
        return Promise.resolve().then(async () => {
          if (typeof store.has === "function") {
            return store.has(keyPrefixed);
          }
          const value = await store.get(keyPrefixed);
          return value !== void 0;
        });
      }
      disconnect() {
        const { store } = this.opts;
        if (typeof store.disconnect === "function") {
          return store.disconnect();
        }
      }
    };
    module.exports = Keyv;
  }
});

// node_modules/flatted/cjs/index.js
var require_cjs = __commonJS({
  "node_modules/flatted/cjs/index.js"(exports) {
    "use strict";
    var { parse: $parse, stringify: $stringify } = JSON;
    var { keys } = Object;
    var Primitive = String;
    var primitive = "string";
    var ignore = {};
    var object = "object";
    var noop = (_, value) => value;
    var primitives = (value) => value instanceof Primitive ? Primitive(value) : value;
    var Primitives = (_, value) => typeof value === primitive ? new Primitive(value) : value;
    var revive = (input, parsed, output, $) => {
      const lazy = [];
      for (let ke = keys(output), { length } = ke, y = 0; y < length; y++) {
        const k = ke[y];
        const value = output[k];
        if (value instanceof Primitive) {
          const tmp = input[value];
          if (typeof tmp === object && !parsed.has(tmp)) {
            parsed.add(tmp);
            output[k] = ignore;
            lazy.push({ k, a: [input, parsed, tmp, $] });
          } else
            output[k] = $.call(output, k, tmp);
        } else if (output[k] !== ignore)
          output[k] = $.call(output, k, value);
      }
      for (let { length } = lazy, i = 0; i < length; i++) {
        const { k, a } = lazy[i];
        output[k] = $.call(output, k, revive.apply(null, a));
      }
      return output;
    };
    var set = (known, input, value) => {
      const index = Primitive(input.push(value) - 1);
      known.set(value, index);
      return index;
    };
    var parse = (text, reviver) => {
      const input = $parse(text, Primitives).map(primitives);
      const value = input[0];
      const $ = reviver || noop;
      const tmp = typeof value === object && value ? revive(input, /* @__PURE__ */ new Set(), value, $) : value;
      return $.call({ "": tmp }, "", tmp);
    };
    exports.parse = parse;
    var stringify4 = (value, replacer, space) => {
      const $ = replacer && typeof replacer === object ? (k, v) => k === "" || -1 < replacer.indexOf(k) ? v : void 0 : replacer || noop;
      const known = /* @__PURE__ */ new Map();
      const input = [];
      const output = [];
      let i = +set(known, input, $.call({ "": value }, "", value));
      let firstRun = !i;
      while (i < input.length) {
        firstRun = true;
        output[i] = $stringify(input[i++], replace, space);
      }
      return "[" + output.join(",") + "]";
      function replace(key, value2) {
        if (firstRun) {
          firstRun = !firstRun;
          return value2;
        }
        const after = $.call(this, key, value2);
        switch (typeof after) {
          case object:
            if (after === null)
              return after;
          case primitive:
            return known.get(after) || set(known, input, after);
        }
        return after;
      }
    };
    exports.stringify = stringify4;
    var toJSON = (any) => $parse(stringify4(any));
    exports.toJSON = toJSON;
    var fromJSON = (any) => parse($stringify(any));
    exports.fromJSON = fromJSON;
  }
});

// node_modules/flat-cache/src/utils.js
var require_utils = __commonJS({
  "node_modules/flat-cache/src/utils.js"(exports, module) {
    var fs6 = __require("fs");
    var path10 = __require("path");
    var flatted = require_cjs();
    module.exports = {
      tryParse: function(filePath, defaultValue) {
        var result;
        try {
          result = this.readJSON(filePath);
        } catch (ex) {
          result = defaultValue;
        }
        return result;
      },
      /**
       * Read json file synchronously using flatted
       *
       * @method readJSON
       * @param  {String} filePath Json filepath
       * @returns {*} parse result
       */
      readJSON: function(filePath) {
        return flatted.parse(
          fs6.readFileSync(filePath, {
            encoding: "utf8"
          })
        );
      },
      /**
       * Write json file synchronously using circular-json
       *
       * @method writeJSON
       * @param  {String} filePath Json filepath
       * @param  {*} data Object to serialize
       */
      writeJSON: function(filePath, data) {
        fs6.mkdirSync(path10.dirname(filePath), {
          recursive: true
        });
        fs6.writeFileSync(filePath, flatted.stringify(data));
      }
    };
  }
});

// node_modules/fs.realpath/old.js
var require_old = __commonJS({
  "node_modules/fs.realpath/old.js"(exports) {
    var pathModule = __require("path");
    var isWindows = process.platform === "win32";
    var fs6 = __require("fs");
    var DEBUG = process.env.NODE_DEBUG && /fs/.test(process.env.NODE_DEBUG);
    function rethrow() {
      var callback;
      if (DEBUG) {
        var backtrace = new Error();
        callback = debugCallback;
      } else
        callback = missingCallback;
      return callback;
      function debugCallback(err) {
        if (err) {
          backtrace.message = err.message;
          err = backtrace;
          missingCallback(err);
        }
      }
      function missingCallback(err) {
        if (err) {
          if (process.throwDeprecation)
            throw err;
          else if (!process.noDeprecation) {
            var msg = "fs: missing callback " + (err.stack || err.message);
            if (process.traceDeprecation)
              console.trace(msg);
            else
              console.error(msg);
          }
        }
      }
    }
    function maybeCallback(cb) {
      return typeof cb === "function" ? cb : rethrow();
    }
    var normalize = pathModule.normalize;
    if (isWindows) {
      nextPartRe = /(.*?)(?:[\/\\]+|$)/g;
    } else {
      nextPartRe = /(.*?)(?:[\/]+|$)/g;
    }
    var nextPartRe;
    if (isWindows) {
      splitRootRe = /^(?:[a-zA-Z]:|[\\\/]{2}[^\\\/]+[\\\/][^\\\/]+)?[\\\/]*/;
    } else {
      splitRootRe = /^[\/]*/;
    }
    var splitRootRe;
    exports.realpathSync = function realpathSync(p, cache) {
      p = pathModule.resolve(p);
      if (cache && Object.prototype.hasOwnProperty.call(cache, p)) {
        return cache[p];
      }
      var original = p, seenLinks = {}, knownHard = {};
      var pos;
      var current;
      var base;
      var previous;
      start();
      function start() {
        var m = splitRootRe.exec(p);
        pos = m[0].length;
        current = m[0];
        base = m[0];
        previous = "";
        if (isWindows && !knownHard[base]) {
          fs6.lstatSync(base);
          knownHard[base] = true;
        }
      }
      while (pos < p.length) {
        nextPartRe.lastIndex = pos;
        var result = nextPartRe.exec(p);
        previous = current;
        current += result[0];
        base = previous + result[1];
        pos = nextPartRe.lastIndex;
        if (knownHard[base] || cache && cache[base] === base) {
          continue;
        }
        var resolvedLink;
        if (cache && Object.prototype.hasOwnProperty.call(cache, base)) {
          resolvedLink = cache[base];
        } else {
          var stat = fs6.lstatSync(base);
          if (!stat.isSymbolicLink()) {
            knownHard[base] = true;
            if (cache)
              cache[base] = base;
            continue;
          }
          var linkTarget = null;
          if (!isWindows) {
            var id = stat.dev.toString(32) + ":" + stat.ino.toString(32);
            if (seenLinks.hasOwnProperty(id)) {
              linkTarget = seenLinks[id];
            }
          }
          if (linkTarget === null) {
            fs6.statSync(base);
            linkTarget = fs6.readlinkSync(base);
          }
          resolvedLink = pathModule.resolve(previous, linkTarget);
          if (cache)
            cache[base] = resolvedLink;
          if (!isWindows)
            seenLinks[id] = linkTarget;
        }
        p = pathModule.resolve(resolvedLink, p.slice(pos));
        start();
      }
      if (cache)
        cache[original] = p;
      return p;
    };
    exports.realpath = function realpath(p, cache, cb) {
      if (typeof cb !== "function") {
        cb = maybeCallback(cache);
        cache = null;
      }
      p = pathModule.resolve(p);
      if (cache && Object.prototype.hasOwnProperty.call(cache, p)) {
        return process.nextTick(cb.bind(null, null, cache[p]));
      }
      var original = p, seenLinks = {}, knownHard = {};
      var pos;
      var current;
      var base;
      var previous;
      start();
      function start() {
        var m = splitRootRe.exec(p);
        pos = m[0].length;
        current = m[0];
        base = m[0];
        previous = "";
        if (isWindows && !knownHard[base]) {
          fs6.lstat(base, function(err) {
            if (err)
              return cb(err);
            knownHard[base] = true;
            LOOP();
          });
        } else {
          process.nextTick(LOOP);
        }
      }
      function LOOP() {
        if (pos >= p.length) {
          if (cache)
            cache[original] = p;
          return cb(null, p);
        }
        nextPartRe.lastIndex = pos;
        var result = nextPartRe.exec(p);
        previous = current;
        current += result[0];
        base = previous + result[1];
        pos = nextPartRe.lastIndex;
        if (knownHard[base] || cache && cache[base] === base) {
          return process.nextTick(LOOP);
        }
        if (cache && Object.prototype.hasOwnProperty.call(cache, base)) {
          return gotResolvedLink(cache[base]);
        }
        return fs6.lstat(base, gotStat);
      }
      function gotStat(err, stat) {
        if (err)
          return cb(err);
        if (!stat.isSymbolicLink()) {
          knownHard[base] = true;
          if (cache)
            cache[base] = base;
          return process.nextTick(LOOP);
        }
        if (!isWindows) {
          var id = stat.dev.toString(32) + ":" + stat.ino.toString(32);
          if (seenLinks.hasOwnProperty(id)) {
            return gotTarget(null, seenLinks[id], base);
          }
        }
        fs6.stat(base, function(err2) {
          if (err2)
            return cb(err2);
          fs6.readlink(base, function(err3, target) {
            if (!isWindows)
              seenLinks[id] = target;
            gotTarget(err3, target);
          });
        });
      }
      function gotTarget(err, target, base2) {
        if (err)
          return cb(err);
        var resolvedLink = pathModule.resolve(previous, target);
        if (cache)
          cache[base2] = resolvedLink;
        gotResolvedLink(resolvedLink);
      }
      function gotResolvedLink(resolvedLink) {
        p = pathModule.resolve(resolvedLink, p.slice(pos));
        start();
      }
    };
  }
});

// node_modules/fs.realpath/index.js
var require_fs = __commonJS({
  "node_modules/fs.realpath/index.js"(exports, module) {
    module.exports = realpath;
    realpath.realpath = realpath;
    realpath.sync = realpathSync;
    realpath.realpathSync = realpathSync;
    realpath.monkeypatch = monkeypatch;
    realpath.unmonkeypatch = unmonkeypatch;
    var fs6 = __require("fs");
    var origRealpath = fs6.realpath;
    var origRealpathSync = fs6.realpathSync;
    var version2 = process.version;
    var ok = /^v[0-5]\./.test(version2);
    var old = require_old();
    function newError(er) {
      return er && er.syscall === "realpath" && (er.code === "ELOOP" || er.code === "ENOMEM" || er.code === "ENAMETOOLONG");
    }
    function realpath(p, cache, cb) {
      if (ok) {
        return origRealpath(p, cache, cb);
      }
      if (typeof cache === "function") {
        cb = cache;
        cache = null;
      }
      origRealpath(p, cache, function(er, result) {
        if (newError(er)) {
          old.realpath(p, cache, cb);
        } else {
          cb(er, result);
        }
      });
    }
    function realpathSync(p, cache) {
      if (ok) {
        return origRealpathSync(p, cache);
      }
      try {
        return origRealpathSync(p, cache);
      } catch (er) {
        if (newError(er)) {
          return old.realpathSync(p, cache);
        } else {
          throw er;
        }
      }
    }
    function monkeypatch() {
      fs6.realpath = realpath;
      fs6.realpathSync = realpathSync;
    }
    function unmonkeypatch() {
      fs6.realpath = origRealpath;
      fs6.realpathSync = origRealpathSync;
    }
  }
});

// node_modules/concat-map/index.js
var require_concat_map = __commonJS({
  "node_modules/concat-map/index.js"(exports, module) {
    module.exports = function(xs, fn) {
      var res = [];
      for (var i = 0; i < xs.length; i++) {
        var x = fn(xs[i], i);
        if (isArray(x))
          res.push.apply(res, x);
        else
          res.push(x);
      }
      return res;
    };
    var isArray = Array.isArray || function(xs) {
      return Object.prototype.toString.call(xs) === "[object Array]";
    };
  }
});

// node_modules/balanced-match/index.js
var require_balanced_match = __commonJS({
  "node_modules/balanced-match/index.js"(exports, module) {
    "use strict";
    module.exports = balanced;
    function balanced(a, b, str) {
      if (a instanceof RegExp)
        a = maybeMatch(a, str);
      if (b instanceof RegExp)
        b = maybeMatch(b, str);
      var r = range(a, b, str);
      return r && {
        start: r[0],
        end: r[1],
        pre: str.slice(0, r[0]),
        body: str.slice(r[0] + a.length, r[1]),
        post: str.slice(r[1] + b.length)
      };
    }
    function maybeMatch(reg, str) {
      var m = str.match(reg);
      return m ? m[0] : null;
    }
    balanced.range = range;
    function range(a, b, str) {
      var begs, beg, left, right, result;
      var ai = str.indexOf(a);
      var bi = str.indexOf(b, ai + 1);
      var i = ai;
      if (ai >= 0 && bi > 0) {
        if (a === b) {
          return [ai, bi];
        }
        begs = [];
        left = str.length;
        while (i >= 0 && !result) {
          if (i == ai) {
            begs.push(i);
            ai = str.indexOf(a, i + 1);
          } else if (begs.length == 1) {
            result = [begs.pop(), bi];
          } else {
            beg = begs.pop();
            if (beg < left) {
              left = beg;
              right = bi;
            }
            bi = str.indexOf(b, i + 1);
          }
          i = ai < bi && ai >= 0 ? ai : bi;
        }
        if (begs.length) {
          result = [left, right];
        }
      }
      return result;
    }
  }
});

// node_modules/brace-expansion/index.js
var require_brace_expansion = __commonJS({
  "node_modules/brace-expansion/index.js"(exports, module) {
    var concatMap = require_concat_map();
    var balanced = require_balanced_match();
    module.exports = expandTop;
    var escSlash = "\0SLASH" + Math.random() + "\0";
    var escOpen = "\0OPEN" + Math.random() + "\0";
    var escClose = "\0CLOSE" + Math.random() + "\0";
    var escComma = "\0COMMA" + Math.random() + "\0";
    var escPeriod = "\0PERIOD" + Math.random() + "\0";
    function numeric(str) {
      return parseInt(str, 10) == str ? parseInt(str, 10) : str.charCodeAt(0);
    }
    function escapeBraces(str) {
      return str.split("\\\\").join(escSlash).split("\\{").join(escOpen).split("\\}").join(escClose).split("\\,").join(escComma).split("\\.").join(escPeriod);
    }
    function unescapeBraces(str) {
      return str.split(escSlash).join("\\").split(escOpen).join("{").split(escClose).join("}").split(escComma).join(",").split(escPeriod).join(".");
    }
    function parseCommaParts(str) {
      if (!str)
        return [""];
      var parts = [];
      var m = balanced("{", "}", str);
      if (!m)
        return str.split(",");
      var pre = m.pre;
      var body = m.body;
      var post = m.post;
      var p = pre.split(",");
      p[p.length - 1] += "{" + body + "}";
      var postParts = parseCommaParts(post);
      if (post.length) {
        p[p.length - 1] += postParts.shift();
        p.push.apply(p, postParts);
      }
      parts.push.apply(parts, p);
      return parts;
    }
    function expandTop(str) {
      if (!str)
        return [];
      if (str.substr(0, 2) === "{}") {
        str = "\\{\\}" + str.substr(2);
      }
      return expand(escapeBraces(str), true).map(unescapeBraces);
    }
    function embrace(str) {
      return "{" + str + "}";
    }
    function isPadded(el) {
      return /^-?0\d/.test(el);
    }
    function lte(i, y) {
      return i <= y;
    }
    function gte(i, y) {
      return i >= y;
    }
    function expand(str, isTop) {
      var expansions = [];
      var m = balanced("{", "}", str);
      if (!m || /\$$/.test(m.pre))
        return [str];
      var isNumericSequence = /^-?\d+\.\.-?\d+(?:\.\.-?\d+)?$/.test(m.body);
      var isAlphaSequence = /^[a-zA-Z]\.\.[a-zA-Z](?:\.\.-?\d+)?$/.test(m.body);
      var isSequence = isNumericSequence || isAlphaSequence;
      var isOptions = m.body.indexOf(",") >= 0;
      if (!isSequence && !isOptions) {
        if (m.post.match(/,.*\}/)) {
          str = m.pre + "{" + m.body + escClose + m.post;
          return expand(str);
        }
        return [str];
      }
      var n;
      if (isSequence) {
        n = m.body.split(/\.\./);
      } else {
        n = parseCommaParts(m.body);
        if (n.length === 1) {
          n = expand(n[0], false).map(embrace);
          if (n.length === 1) {
            var post = m.post.length ? expand(m.post, false) : [""];
            return post.map(function(p) {
              return m.pre + n[0] + p;
            });
          }
        }
      }
      var pre = m.pre;
      var post = m.post.length ? expand(m.post, false) : [""];
      var N;
      if (isSequence) {
        var x = numeric(n[0]);
        var y = numeric(n[1]);
        var width = Math.max(n[0].length, n[1].length);
        var incr = n.length == 3 ? Math.abs(numeric(n[2])) : 1;
        var test = lte;
        var reverse = y < x;
        if (reverse) {
          incr *= -1;
          test = gte;
        }
        var pad = n.some(isPadded);
        N = [];
        for (var i = x; test(i, y); i += incr) {
          var c;
          if (isAlphaSequence) {
            c = String.fromCharCode(i);
            if (c === "\\")
              c = "";
          } else {
            c = String(i);
            if (pad) {
              var need = width - c.length;
              if (need > 0) {
                var z = new Array(need + 1).join("0");
                if (i < 0)
                  c = "-" + z + c.slice(1);
                else
                  c = z + c;
              }
            }
          }
          N.push(c);
        }
      } else {
        N = concatMap(n, function(el) {
          return expand(el, false);
        });
      }
      for (var j = 0; j < N.length; j++) {
        for (var k = 0; k < post.length; k++) {
          var expansion = pre + N[j] + post[k];
          if (!isTop || isSequence || expansion)
            expansions.push(expansion);
        }
      }
      return expansions;
    }
  }
});

// node_modules/minimatch/minimatch.js
var require_minimatch = __commonJS({
  "node_modules/minimatch/minimatch.js"(exports, module) {
    module.exports = minimatch;
    minimatch.Minimatch = Minimatch;
    var path10 = function() {
      try {
        return __require("path");
      } catch (e) {
      }
    }() || {
      sep: "/"
    };
    minimatch.sep = path10.sep;
    var GLOBSTAR = minimatch.GLOBSTAR = Minimatch.GLOBSTAR = {};
    var expand = require_brace_expansion();
    var plTypes = {
      "!": { open: "(?:(?!(?:", close: "))[^/]*?)" },
      "?": { open: "(?:", close: ")?" },
      "+": { open: "(?:", close: ")+" },
      "*": { open: "(?:", close: ")*" },
      "@": { open: "(?:", close: ")" }
    };
    var qmark = "[^/]";
    var star = qmark + "*?";
    var twoStarDot = "(?:(?!(?:\\/|^)(?:\\.{1,2})($|\\/)).)*?";
    var twoStarNoDot = "(?:(?!(?:\\/|^)\\.).)*?";
    var reSpecials = charSet("().*{}+?[]^$\\!");
    function charSet(s) {
      return s.split("").reduce(function(set, c) {
        set[c] = true;
        return set;
      }, {});
    }
    var slashSplit = /\/+/;
    minimatch.filter = filter;
    function filter(pattern, options) {
      options = options || {};
      return function(p, i, list) {
        return minimatch(p, pattern, options);
      };
    }
    function ext(a, b) {
      b = b || {};
      var t = {};
      Object.keys(a).forEach(function(k) {
        t[k] = a[k];
      });
      Object.keys(b).forEach(function(k) {
        t[k] = b[k];
      });
      return t;
    }
    minimatch.defaults = function(def) {
      if (!def || typeof def !== "object" || !Object.keys(def).length) {
        return minimatch;
      }
      var orig = minimatch;
      var m = function minimatch2(p, pattern, options) {
        return orig(p, pattern, ext(def, options));
      };
      m.Minimatch = function Minimatch2(pattern, options) {
        return new orig.Minimatch(pattern, ext(def, options));
      };
      m.Minimatch.defaults = function defaults(options) {
        return orig.defaults(ext(def, options)).Minimatch;
      };
      m.filter = function filter2(pattern, options) {
        return orig.filter(pattern, ext(def, options));
      };
      m.defaults = function defaults(options) {
        return orig.defaults(ext(def, options));
      };
      m.makeRe = function makeRe2(pattern, options) {
        return orig.makeRe(pattern, ext(def, options));
      };
      m.braceExpand = function braceExpand2(pattern, options) {
        return orig.braceExpand(pattern, ext(def, options));
      };
      m.match = function(list, pattern, options) {
        return orig.match(list, pattern, ext(def, options));
      };
      return m;
    };
    Minimatch.defaults = function(def) {
      return minimatch.defaults(def).Minimatch;
    };
    function minimatch(p, pattern, options) {
      assertValidPattern(pattern);
      if (!options)
        options = {};
      if (!options.nocomment && pattern.charAt(0) === "#") {
        return false;
      }
      return new Minimatch(pattern, options).match(p);
    }
    function Minimatch(pattern, options) {
      if (!(this instanceof Minimatch)) {
        return new Minimatch(pattern, options);
      }
      assertValidPattern(pattern);
      if (!options)
        options = {};
      pattern = pattern.trim();
      if (!options.allowWindowsEscape && path10.sep !== "/") {
        pattern = pattern.split(path10.sep).join("/");
      }
      this.options = options;
      this.set = [];
      this.pattern = pattern;
      this.regexp = null;
      this.negate = false;
      this.comment = false;
      this.empty = false;
      this.partial = !!options.partial;
      this.make();
    }
    Minimatch.prototype.debug = function() {
    };
    Minimatch.prototype.make = make;
    function make() {
      var pattern = this.pattern;
      var options = this.options;
      if (!options.nocomment && pattern.charAt(0) === "#") {
        this.comment = true;
        return;
      }
      if (!pattern) {
        this.empty = true;
        return;
      }
      this.parseNegate();
      var set = this.globSet = this.braceExpand();
      if (options.debug)
        this.debug = function debug() {
          console.error.apply(console, arguments);
        };
      this.debug(this.pattern, set);
      set = this.globParts = set.map(function(s) {
        return s.split(slashSplit);
      });
      this.debug(this.pattern, set);
      set = set.map(function(s, si, set2) {
        return s.map(this.parse, this);
      }, this);
      this.debug(this.pattern, set);
      set = set.filter(function(s) {
        return s.indexOf(false) === -1;
      });
      this.debug(this.pattern, set);
      this.set = set;
    }
    Minimatch.prototype.parseNegate = parseNegate;
    function parseNegate() {
      var pattern = this.pattern;
      var negate = false;
      var options = this.options;
      var negateOffset = 0;
      if (options.nonegate)
        return;
      for (var i = 0, l = pattern.length; i < l && pattern.charAt(i) === "!"; i++) {
        negate = !negate;
        negateOffset++;
      }
      if (negateOffset)
        this.pattern = pattern.substr(negateOffset);
      this.negate = negate;
    }
    minimatch.braceExpand = function(pattern, options) {
      return braceExpand(pattern, options);
    };
    Minimatch.prototype.braceExpand = braceExpand;
    function braceExpand(pattern, options) {
      if (!options) {
        if (this instanceof Minimatch) {
          options = this.options;
        } else {
          options = {};
        }
      }
      pattern = typeof pattern === "undefined" ? this.pattern : pattern;
      assertValidPattern(pattern);
      if (options.nobrace || !/\{(?:(?!\{).)*\}/.test(pattern)) {
        return [pattern];
      }
      return expand(pattern);
    }
    var MAX_PATTERN_LENGTH = 1024 * 64;
    var assertValidPattern = function(pattern) {
      if (typeof pattern !== "string") {
        throw new TypeError("invalid pattern");
      }
      if (pattern.length > MAX_PATTERN_LENGTH) {
        throw new TypeError("pattern is too long");
      }
    };
    Minimatch.prototype.parse = parse;
    var SUBPARSE = {};
    function parse(pattern, isSub) {
      assertValidPattern(pattern);
      var options = this.options;
      if (pattern === "**") {
        if (!options.noglobstar)
          return GLOBSTAR;
        else
          pattern = "*";
      }
      if (pattern === "")
        return "";
      var re = "";
      var hasMagic = !!options.nocase;
      var escaping = false;
      var patternListStack = [];
      var negativeLists = [];
      var stateChar;
      var inClass = false;
      var reClassStart = -1;
      var classStart = -1;
      var patternStart = pattern.charAt(0) === "." ? "" : options.dot ? "(?!(?:^|\\/)\\.{1,2}(?:$|\\/))" : "(?!\\.)";
      var self = this;
      function clearStateChar() {
        if (stateChar) {
          switch (stateChar) {
            case "*":
              re += star;
              hasMagic = true;
              break;
            case "?":
              re += qmark;
              hasMagic = true;
              break;
            default:
              re += "\\" + stateChar;
              break;
          }
          self.debug("clearStateChar %j %j", stateChar, re);
          stateChar = false;
        }
      }
      for (var i = 0, len = pattern.length, c; i < len && (c = pattern.charAt(i)); i++) {
        this.debug("%s	%s %s %j", pattern, i, re, c);
        if (escaping && reSpecials[c]) {
          re += "\\" + c;
          escaping = false;
          continue;
        }
        switch (c) {
          case "/": {
            return false;
          }
          case "\\":
            clearStateChar();
            escaping = true;
            continue;
          case "?":
          case "*":
          case "+":
          case "@":
          case "!":
            this.debug("%s	%s %s %j <-- stateChar", pattern, i, re, c);
            if (inClass) {
              this.debug("  in class");
              if (c === "!" && i === classStart + 1)
                c = "^";
              re += c;
              continue;
            }
            self.debug("call clearStateChar %j", stateChar);
            clearStateChar();
            stateChar = c;
            if (options.noext)
              clearStateChar();
            continue;
          case "(":
            if (inClass) {
              re += "(";
              continue;
            }
            if (!stateChar) {
              re += "\\(";
              continue;
            }
            patternListStack.push({
              type: stateChar,
              start: i - 1,
              reStart: re.length,
              open: plTypes[stateChar].open,
              close: plTypes[stateChar].close
            });
            re += stateChar === "!" ? "(?:(?!(?:" : "(?:";
            this.debug("plType %j %j", stateChar, re);
            stateChar = false;
            continue;
          case ")":
            if (inClass || !patternListStack.length) {
              re += "\\)";
              continue;
            }
            clearStateChar();
            hasMagic = true;
            var pl = patternListStack.pop();
            re += pl.close;
            if (pl.type === "!") {
              negativeLists.push(pl);
            }
            pl.reEnd = re.length;
            continue;
          case "|":
            if (inClass || !patternListStack.length || escaping) {
              re += "\\|";
              escaping = false;
              continue;
            }
            clearStateChar();
            re += "|";
            continue;
          case "[":
            clearStateChar();
            if (inClass) {
              re += "\\" + c;
              continue;
            }
            inClass = true;
            classStart = i;
            reClassStart = re.length;
            re += c;
            continue;
          case "]":
            if (i === classStart + 1 || !inClass) {
              re += "\\" + c;
              escaping = false;
              continue;
            }
            var cs = pattern.substring(classStart + 1, i);
            try {
              RegExp("[" + cs + "]");
            } catch (er) {
              var sp = this.parse(cs, SUBPARSE);
              re = re.substr(0, reClassStart) + "\\[" + sp[0] + "\\]";
              hasMagic = hasMagic || sp[1];
              inClass = false;
              continue;
            }
            hasMagic = true;
            inClass = false;
            re += c;
            continue;
          default:
            clearStateChar();
            if (escaping) {
              escaping = false;
            } else if (reSpecials[c] && !(c === "^" && inClass)) {
              re += "\\";
            }
            re += c;
        }
      }
      if (inClass) {
        cs = pattern.substr(classStart + 1);
        sp = this.parse(cs, SUBPARSE);
        re = re.substr(0, reClassStart) + "\\[" + sp[0];
        hasMagic = hasMagic || sp[1];
      }
      for (pl = patternListStack.pop(); pl; pl = patternListStack.pop()) {
        var tail = re.slice(pl.reStart + pl.open.length);
        this.debug("setting tail", re, pl);
        tail = tail.replace(/((?:\\{2}){0,64})(\\?)\|/g, function(_, $1, $2) {
          if (!$2) {
            $2 = "\\";
          }
          return $1 + $1 + $2 + "|";
        });
        this.debug("tail=%j\n   %s", tail, tail, pl, re);
        var t = pl.type === "*" ? star : pl.type === "?" ? qmark : "\\" + pl.type;
        hasMagic = true;
        re = re.slice(0, pl.reStart) + t + "\\(" + tail;
      }
      clearStateChar();
      if (escaping) {
        re += "\\\\";
      }
      var addPatternStart = false;
      switch (re.charAt(0)) {
        case "[":
        case ".":
        case "(":
          addPatternStart = true;
      }
      for (var n = negativeLists.length - 1; n > -1; n--) {
        var nl = negativeLists[n];
        var nlBefore = re.slice(0, nl.reStart);
        var nlFirst = re.slice(nl.reStart, nl.reEnd - 8);
        var nlLast = re.slice(nl.reEnd - 8, nl.reEnd);
        var nlAfter = re.slice(nl.reEnd);
        nlLast += nlAfter;
        var openParensBefore = nlBefore.split("(").length - 1;
        var cleanAfter = nlAfter;
        for (i = 0; i < openParensBefore; i++) {
          cleanAfter = cleanAfter.replace(/\)[+*?]?/, "");
        }
        nlAfter = cleanAfter;
        var dollar = "";
        if (nlAfter === "" && isSub !== SUBPARSE) {
          dollar = "$";
        }
        var newRe = nlBefore + nlFirst + nlAfter + dollar + nlLast;
        re = newRe;
      }
      if (re !== "" && hasMagic) {
        re = "(?=.)" + re;
      }
      if (addPatternStart) {
        re = patternStart + re;
      }
      if (isSub === SUBPARSE) {
        return [re, hasMagic];
      }
      if (!hasMagic) {
        return globUnescape(pattern);
      }
      var flags = options.nocase ? "i" : "";
      try {
        var regExp = new RegExp("^" + re + "$", flags);
      } catch (er) {
        return new RegExp("$.");
      }
      regExp._glob = pattern;
      regExp._src = re;
      return regExp;
    }
    minimatch.makeRe = function(pattern, options) {
      return new Minimatch(pattern, options || {}).makeRe();
    };
    Minimatch.prototype.makeRe = makeRe;
    function makeRe() {
      if (this.regexp || this.regexp === false)
        return this.regexp;
      var set = this.set;
      if (!set.length) {
        this.regexp = false;
        return this.regexp;
      }
      var options = this.options;
      var twoStar = options.noglobstar ? star : options.dot ? twoStarDot : twoStarNoDot;
      var flags = options.nocase ? "i" : "";
      var re = set.map(function(pattern) {
        return pattern.map(function(p) {
          return p === GLOBSTAR ? twoStar : typeof p === "string" ? regExpEscape(p) : p._src;
        }).join("\\/");
      }).join("|");
      re = "^(?:" + re + ")$";
      if (this.negate)
        re = "^(?!" + re + ").*$";
      try {
        this.regexp = new RegExp(re, flags);
      } catch (ex) {
        this.regexp = false;
      }
      return this.regexp;
    }
    minimatch.match = function(list, pattern, options) {
      options = options || {};
      var mm = new Minimatch(pattern, options);
      list = list.filter(function(f) {
        return mm.match(f);
      });
      if (mm.options.nonull && !list.length) {
        list.push(pattern);
      }
      return list;
    };
    Minimatch.prototype.match = function match(f, partial) {
      if (typeof partial === "undefined")
        partial = this.partial;
      this.debug("match", f, this.pattern);
      if (this.comment)
        return false;
      if (this.empty)
        return f === "";
      if (f === "/" && partial)
        return true;
      var options = this.options;
      if (path10.sep !== "/") {
        f = f.split(path10.sep).join("/");
      }
      f = f.split(slashSplit);
      this.debug(this.pattern, "split", f);
      var set = this.set;
      this.debug(this.pattern, "set", set);
      var filename;
      var i;
      for (i = f.length - 1; i >= 0; i--) {
        filename = f[i];
        if (filename)
          break;
      }
      for (i = 0; i < set.length; i++) {
        var pattern = set[i];
        var file = f;
        if (options.matchBase && pattern.length === 1) {
          file = [filename];
        }
        var hit = this.matchOne(file, pattern, partial);
        if (hit) {
          if (options.flipNegate)
            return true;
          return !this.negate;
        }
      }
      if (options.flipNegate)
        return false;
      return this.negate;
    };
    Minimatch.prototype.matchOne = function(file, pattern, partial) {
      var options = this.options;
      this.debug(
        "matchOne",
        { "this": this, file, pattern }
      );
      this.debug("matchOne", file.length, pattern.length);
      for (var fi = 0, pi = 0, fl = file.length, pl = pattern.length; fi < fl && pi < pl; fi++, pi++) {
        this.debug("matchOne loop");
        var p = pattern[pi];
        var f = file[fi];
        this.debug(pattern, p, f);
        if (p === false)
          return false;
        if (p === GLOBSTAR) {
          this.debug("GLOBSTAR", [pattern, p, f]);
          var fr = fi;
          var pr = pi + 1;
          if (pr === pl) {
            this.debug("** at the end");
            for (; fi < fl; fi++) {
              if (file[fi] === "." || file[fi] === ".." || !options.dot && file[fi].charAt(0) === ".")
                return false;
            }
            return true;
          }
          while (fr < fl) {
            var swallowee = file[fr];
            this.debug("\nglobstar while", file, fr, pattern, pr, swallowee);
            if (this.matchOne(file.slice(fr), pattern.slice(pr), partial)) {
              this.debug("globstar found match!", fr, fl, swallowee);
              return true;
            } else {
              if (swallowee === "." || swallowee === ".." || !options.dot && swallowee.charAt(0) === ".") {
                this.debug("dot detected!", file, fr, pattern, pr);
                break;
              }
              this.debug("globstar swallow a segment, and continue");
              fr++;
            }
          }
          if (partial) {
            this.debug("\n>>> no match, partial?", file, fr, pattern, pr);
            if (fr === fl)
              return true;
          }
          return false;
        }
        var hit;
        if (typeof p === "string") {
          hit = f === p;
          this.debug("string match", p, f, hit);
        } else {
          hit = f.match(p);
          this.debug("pattern match", p, f, hit);
        }
        if (!hit)
          return false;
      }
      if (fi === fl && pi === pl) {
        return true;
      } else if (fi === fl) {
        return partial;
      } else if (pi === pl) {
        return fi === fl - 1 && file[fi] === "";
      }
      throw new Error("wtf?");
    };
    function globUnescape(s) {
      return s.replace(/\\(.)/g, "$1");
    }
    function regExpEscape(s) {
      return s.replace(/[-[\]{}()*+?.,\\^$|#\s]/g, "\\$&");
    }
  }
});

// node_modules/inherits/inherits_browser.js
var require_inherits_browser = __commonJS({
  "node_modules/inherits/inherits_browser.js"(exports, module) {
    if (typeof Object.create === "function") {
      module.exports = function inherits(ctor, superCtor) {
        if (superCtor) {
          ctor.super_ = superCtor;
          ctor.prototype = Object.create(superCtor.prototype, {
            constructor: {
              value: ctor,
              enumerable: false,
              writable: true,
              configurable: true
            }
          });
        }
      };
    } else {
      module.exports = function inherits(ctor, superCtor) {
        if (superCtor) {
          ctor.super_ = superCtor;
          var TempCtor = function() {
          };
          TempCtor.prototype = superCtor.prototype;
          ctor.prototype = new TempCtor();
          ctor.prototype.constructor = ctor;
        }
      };
    }
  }
});

// node_modules/inherits/inherits.js
var require_inherits = __commonJS({
  "node_modules/inherits/inherits.js"(exports, module) {
    try {
      util = __require("util");
      if (typeof util.inherits !== "function")
        throw "";
      module.exports = util.inherits;
    } catch (e) {
      module.exports = require_inherits_browser();
    }
    var util;
  }
});

// node_modules/path-is-absolute/index.js
var require_path_is_absolute = __commonJS({
  "node_modules/path-is-absolute/index.js"(exports, module) {
    "use strict";
    function posix(path10) {
      return path10.charAt(0) === "/";
    }
    function win32(path10) {
      var splitDeviceRe = /^([a-zA-Z]:|[\\\/]{2}[^\\\/]+[\\\/]+[^\\\/]+)?([\\\/])?([\s\S]*?)$/;
      var result = splitDeviceRe.exec(path10);
      var device = result[1] || "";
      var isUnc = Boolean(device && device.charAt(1) !== ":");
      return Boolean(result[2] || isUnc);
    }
    module.exports = process.platform === "win32" ? win32 : posix;
    module.exports.posix = posix;
    module.exports.win32 = win32;
  }
});

// node_modules/glob/common.js
var require_common = __commonJS({
  "node_modules/glob/common.js"(exports) {
    exports.setopts = setopts;
    exports.ownProp = ownProp;
    exports.makeAbs = makeAbs;
    exports.finish = finish;
    exports.mark = mark;
    exports.isIgnored = isIgnored;
    exports.childrenIgnored = childrenIgnored;
    function ownProp(obj, field) {
      return Object.prototype.hasOwnProperty.call(obj, field);
    }
    var fs6 = __require("fs");
    var path10 = __require("path");
    var minimatch = require_minimatch();
    var isAbsolute = require_path_is_absolute();
    var Minimatch = minimatch.Minimatch;
    function alphasort(a, b) {
      return a.localeCompare(b, "en");
    }
    function setupIgnores(self, options) {
      self.ignore = options.ignore || [];
      if (!Array.isArray(self.ignore))
        self.ignore = [self.ignore];
      if (self.ignore.length) {
        self.ignore = self.ignore.map(ignoreMap);
      }
    }
    function ignoreMap(pattern) {
      var gmatcher = null;
      if (pattern.slice(-3) === "/**") {
        var gpattern = pattern.replace(/(\/\*\*)+$/, "");
        gmatcher = new Minimatch(gpattern, { dot: true });
      }
      return {
        matcher: new Minimatch(pattern, { dot: true }),
        gmatcher
      };
    }
    function setopts(self, pattern, options) {
      if (!options)
        options = {};
      if (options.matchBase && -1 === pattern.indexOf("/")) {
        if (options.noglobstar) {
          throw new Error("base matching requires globstar");
        }
        pattern = "**/" + pattern;
      }
      self.silent = !!options.silent;
      self.pattern = pattern;
      self.strict = options.strict !== false;
      self.realpath = !!options.realpath;
      self.realpathCache = options.realpathCache || /* @__PURE__ */ Object.create(null);
      self.follow = !!options.follow;
      self.dot = !!options.dot;
      self.mark = !!options.mark;
      self.nodir = !!options.nodir;
      if (self.nodir)
        self.mark = true;
      self.sync = !!options.sync;
      self.nounique = !!options.nounique;
      self.nonull = !!options.nonull;
      self.nosort = !!options.nosort;
      self.nocase = !!options.nocase;
      self.stat = !!options.stat;
      self.noprocess = !!options.noprocess;
      self.absolute = !!options.absolute;
      self.fs = options.fs || fs6;
      self.maxLength = options.maxLength || Infinity;
      self.cache = options.cache || /* @__PURE__ */ Object.create(null);
      self.statCache = options.statCache || /* @__PURE__ */ Object.create(null);
      self.symlinks = options.symlinks || /* @__PURE__ */ Object.create(null);
      setupIgnores(self, options);
      self.changedCwd = false;
      var cwd2 = process.cwd();
      if (!ownProp(options, "cwd"))
        self.cwd = cwd2;
      else {
        self.cwd = path10.resolve(options.cwd);
        self.changedCwd = self.cwd !== cwd2;
      }
      self.root = options.root || path10.resolve(self.cwd, "/");
      self.root = path10.resolve(self.root);
      if (process.platform === "win32")
        self.root = self.root.replace(/\\/g, "/");
      self.cwdAbs = isAbsolute(self.cwd) ? self.cwd : makeAbs(self, self.cwd);
      if (process.platform === "win32")
        self.cwdAbs = self.cwdAbs.replace(/\\/g, "/");
      self.nomount = !!options.nomount;
      options.nonegate = true;
      options.nocomment = true;
      options.allowWindowsEscape = false;
      self.minimatch = new Minimatch(pattern, options);
      self.options = self.minimatch.options;
    }
    function finish(self) {
      var nou = self.nounique;
      var all = nou ? [] : /* @__PURE__ */ Object.create(null);
      for (var i = 0, l = self.matches.length; i < l; i++) {
        var matches = self.matches[i];
        if (!matches || Object.keys(matches).length === 0) {
          if (self.nonull) {
            var literal = self.minimatch.globSet[i];
            if (nou)
              all.push(literal);
            else
              all[literal] = true;
          }
        } else {
          var m = Object.keys(matches);
          if (nou)
            all.push.apply(all, m);
          else
            m.forEach(function(m2) {
              all[m2] = true;
            });
        }
      }
      if (!nou)
        all = Object.keys(all);
      if (!self.nosort)
        all = all.sort(alphasort);
      if (self.mark) {
        for (var i = 0; i < all.length; i++) {
          all[i] = self._mark(all[i]);
        }
        if (self.nodir) {
          all = all.filter(function(e) {
            var notDir = !/\/$/.test(e);
            var c = self.cache[e] || self.cache[makeAbs(self, e)];
            if (notDir && c)
              notDir = c !== "DIR" && !Array.isArray(c);
            return notDir;
          });
        }
      }
      if (self.ignore.length)
        all = all.filter(function(m2) {
          return !isIgnored(self, m2);
        });
      self.found = all;
    }
    function mark(self, p) {
      var abs = makeAbs(self, p);
      var c = self.cache[abs];
      var m = p;
      if (c) {
        var isDir = c === "DIR" || Array.isArray(c);
        var slash = p.slice(-1) === "/";
        if (isDir && !slash)
          m += "/";
        else if (!isDir && slash)
          m = m.slice(0, -1);
        if (m !== p) {
          var mabs = makeAbs(self, m);
          self.statCache[mabs] = self.statCache[abs];
          self.cache[mabs] = self.cache[abs];
        }
      }
      return m;
    }
    function makeAbs(self, f) {
      var abs = f;
      if (f.charAt(0) === "/") {
        abs = path10.join(self.root, f);
      } else if (isAbsolute(f) || f === "") {
        abs = f;
      } else if (self.changedCwd) {
        abs = path10.resolve(self.cwd, f);
      } else {
        abs = path10.resolve(f);
      }
      if (process.platform === "win32")
        abs = abs.replace(/\\/g, "/");
      return abs;
    }
    function isIgnored(self, path11) {
      if (!self.ignore.length)
        return false;
      return self.ignore.some(function(item) {
        return item.matcher.match(path11) || !!(item.gmatcher && item.gmatcher.match(path11));
      });
    }
    function childrenIgnored(self, path11) {
      if (!self.ignore.length)
        return false;
      return self.ignore.some(function(item) {
        return !!(item.gmatcher && item.gmatcher.match(path11));
      });
    }
  }
});

// node_modules/glob/sync.js
var require_sync = __commonJS({
  "node_modules/glob/sync.js"(exports, module) {
    module.exports = globSync;
    globSync.GlobSync = GlobSync;
    var rp = require_fs();
    var minimatch = require_minimatch();
    var Minimatch = minimatch.Minimatch;
    var Glob = require_glob().Glob;
    var util = __require("util");
    var path10 = __require("path");
    var assert = __require("assert");
    var isAbsolute = require_path_is_absolute();
    var common = require_common();
    var setopts = common.setopts;
    var ownProp = common.ownProp;
    var childrenIgnored = common.childrenIgnored;
    var isIgnored = common.isIgnored;
    function globSync(pattern, options) {
      if (typeof options === "function" || arguments.length === 3)
        throw new TypeError("callback provided to sync glob\nSee: https://github.com/isaacs/node-glob/issues/167");
      return new GlobSync(pattern, options).found;
    }
    function GlobSync(pattern, options) {
      if (!pattern)
        throw new Error("must provide pattern");
      if (typeof options === "function" || arguments.length === 3)
        throw new TypeError("callback provided to sync glob\nSee: https://github.com/isaacs/node-glob/issues/167");
      if (!(this instanceof GlobSync))
        return new GlobSync(pattern, options);
      setopts(this, pattern, options);
      if (this.noprocess)
        return this;
      var n = this.minimatch.set.length;
      this.matches = new Array(n);
      for (var i = 0; i < n; i++) {
        this._process(this.minimatch.set[i], i, false);
      }
      this._finish();
    }
    GlobSync.prototype._finish = function() {
      assert.ok(this instanceof GlobSync);
      if (this.realpath) {
        var self = this;
        this.matches.forEach(function(matchset, index) {
          var set = self.matches[index] = /* @__PURE__ */ Object.create(null);
          for (var p in matchset) {
            try {
              p = self._makeAbs(p);
              var real = rp.realpathSync(p, self.realpathCache);
              set[real] = true;
            } catch (er) {
              if (er.syscall === "stat")
                set[self._makeAbs(p)] = true;
              else
                throw er;
            }
          }
        });
      }
      common.finish(this);
    };
    GlobSync.prototype._process = function(pattern, index, inGlobStar) {
      assert.ok(this instanceof GlobSync);
      var n = 0;
      while (typeof pattern[n] === "string") {
        n++;
      }
      var prefix;
      switch (n) {
        case pattern.length:
          this._processSimple(pattern.join("/"), index);
          return;
        case 0:
          prefix = null;
          break;
        default:
          prefix = pattern.slice(0, n).join("/");
          break;
      }
      var remain = pattern.slice(n);
      var read;
      if (prefix === null)
        read = ".";
      else if (isAbsolute(prefix) || isAbsolute(pattern.map(function(p) {
        return typeof p === "string" ? p : "[*]";
      }).join("/"))) {
        if (!prefix || !isAbsolute(prefix))
          prefix = "/" + prefix;
        read = prefix;
      } else
        read = prefix;
      var abs = this._makeAbs(read);
      if (childrenIgnored(this, read))
        return;
      var isGlobStar = remain[0] === minimatch.GLOBSTAR;
      if (isGlobStar)
        this._processGlobStar(prefix, read, abs, remain, index, inGlobStar);
      else
        this._processReaddir(prefix, read, abs, remain, index, inGlobStar);
    };
    GlobSync.prototype._processReaddir = function(prefix, read, abs, remain, index, inGlobStar) {
      var entries = this._readdir(abs, inGlobStar);
      if (!entries)
        return;
      var pn = remain[0];
      var negate = !!this.minimatch.negate;
      var rawGlob = pn._glob;
      var dotOk = this.dot || rawGlob.charAt(0) === ".";
      var matchedEntries = [];
      for (var i = 0; i < entries.length; i++) {
        var e = entries[i];
        if (e.charAt(0) !== "." || dotOk) {
          var m;
          if (negate && !prefix) {
            m = !e.match(pn);
          } else {
            m = e.match(pn);
          }
          if (m)
            matchedEntries.push(e);
        }
      }
      var len = matchedEntries.length;
      if (len === 0)
        return;
      if (remain.length === 1 && !this.mark && !this.stat) {
        if (!this.matches[index])
          this.matches[index] = /* @__PURE__ */ Object.create(null);
        for (var i = 0; i < len; i++) {
          var e = matchedEntries[i];
          if (prefix) {
            if (prefix.slice(-1) !== "/")
              e = prefix + "/" + e;
            else
              e = prefix + e;
          }
          if (e.charAt(0) === "/" && !this.nomount) {
            e = path10.join(this.root, e);
          }
          this._emitMatch(index, e);
        }
        return;
      }
      remain.shift();
      for (var i = 0; i < len; i++) {
        var e = matchedEntries[i];
        var newPattern;
        if (prefix)
          newPattern = [prefix, e];
        else
          newPattern = [e];
        this._process(newPattern.concat(remain), index, inGlobStar);
      }
    };
    GlobSync.prototype._emitMatch = function(index, e) {
      if (isIgnored(this, e))
        return;
      var abs = this._makeAbs(e);
      if (this.mark)
        e = this._mark(e);
      if (this.absolute) {
        e = abs;
      }
      if (this.matches[index][e])
        return;
      if (this.nodir) {
        var c = this.cache[abs];
        if (c === "DIR" || Array.isArray(c))
          return;
      }
      this.matches[index][e] = true;
      if (this.stat)
        this._stat(e);
    };
    GlobSync.prototype._readdirInGlobStar = function(abs) {
      if (this.follow)
        return this._readdir(abs, false);
      var entries;
      var lstat;
      var stat;
      try {
        lstat = this.fs.lstatSync(abs);
      } catch (er) {
        if (er.code === "ENOENT") {
          return null;
        }
      }
      var isSym = lstat && lstat.isSymbolicLink();
      this.symlinks[abs] = isSym;
      if (!isSym && lstat && !lstat.isDirectory())
        this.cache[abs] = "FILE";
      else
        entries = this._readdir(abs, false);
      return entries;
    };
    GlobSync.prototype._readdir = function(abs, inGlobStar) {
      var entries;
      if (inGlobStar && !ownProp(this.symlinks, abs))
        return this._readdirInGlobStar(abs);
      if (ownProp(this.cache, abs)) {
        var c = this.cache[abs];
        if (!c || c === "FILE")
          return null;
        if (Array.isArray(c))
          return c;
      }
      try {
        return this._readdirEntries(abs, this.fs.readdirSync(abs));
      } catch (er) {
        this._readdirError(abs, er);
        return null;
      }
    };
    GlobSync.prototype._readdirEntries = function(abs, entries) {
      if (!this.mark && !this.stat) {
        for (var i = 0; i < entries.length; i++) {
          var e = entries[i];
          if (abs === "/")
            e = abs + e;
          else
            e = abs + "/" + e;
          this.cache[e] = true;
        }
      }
      this.cache[abs] = entries;
      return entries;
    };
    GlobSync.prototype._readdirError = function(f, er) {
      switch (er.code) {
        case "ENOTSUP":
        case "ENOTDIR":
          var abs = this._makeAbs(f);
          this.cache[abs] = "FILE";
          if (abs === this.cwdAbs) {
            var error = new Error(er.code + " invalid cwd " + this.cwd);
            error.path = this.cwd;
            error.code = er.code;
            throw error;
          }
          break;
        case "ENOENT":
        case "ELOOP":
        case "ENAMETOOLONG":
        case "UNKNOWN":
          this.cache[this._makeAbs(f)] = false;
          break;
        default:
          this.cache[this._makeAbs(f)] = false;
          if (this.strict)
            throw er;
          if (!this.silent)
            console.error("glob error", er);
          break;
      }
    };
    GlobSync.prototype._processGlobStar = function(prefix, read, abs, remain, index, inGlobStar) {
      var entries = this._readdir(abs, inGlobStar);
      if (!entries)
        return;
      var remainWithoutGlobStar = remain.slice(1);
      var gspref = prefix ? [prefix] : [];
      var noGlobStar = gspref.concat(remainWithoutGlobStar);
      this._process(noGlobStar, index, false);
      var len = entries.length;
      var isSym = this.symlinks[abs];
      if (isSym && inGlobStar)
        return;
      for (var i = 0; i < len; i++) {
        var e = entries[i];
        if (e.charAt(0) === "." && !this.dot)
          continue;
        var instead = gspref.concat(entries[i], remainWithoutGlobStar);
        this._process(instead, index, true);
        var below = gspref.concat(entries[i], remain);
        this._process(below, index, true);
      }
    };
    GlobSync.prototype._processSimple = function(prefix, index) {
      var exists = this._stat(prefix);
      if (!this.matches[index])
        this.matches[index] = /* @__PURE__ */ Object.create(null);
      if (!exists)
        return;
      if (prefix && isAbsolute(prefix) && !this.nomount) {
        var trail = /[\/\\]$/.test(prefix);
        if (prefix.charAt(0) === "/") {
          prefix = path10.join(this.root, prefix);
        } else {
          prefix = path10.resolve(this.root, prefix);
          if (trail)
            prefix += "/";
        }
      }
      if (process.platform === "win32")
        prefix = prefix.replace(/\\/g, "/");
      this._emitMatch(index, prefix);
    };
    GlobSync.prototype._stat = function(f) {
      var abs = this._makeAbs(f);
      var needDir = f.slice(-1) === "/";
      if (f.length > this.maxLength)
        return false;
      if (!this.stat && ownProp(this.cache, abs)) {
        var c = this.cache[abs];
        if (Array.isArray(c))
          c = "DIR";
        if (!needDir || c === "DIR")
          return c;
        if (needDir && c === "FILE")
          return false;
      }
      var exists;
      var stat = this.statCache[abs];
      if (!stat) {
        var lstat;
        try {
          lstat = this.fs.lstatSync(abs);
        } catch (er) {
          if (er && (er.code === "ENOENT" || er.code === "ENOTDIR")) {
            this.statCache[abs] = false;
            return false;
          }
        }
        if (lstat && lstat.isSymbolicLink()) {
          try {
            stat = this.fs.statSync(abs);
          } catch (er) {
            stat = lstat;
          }
        } else {
          stat = lstat;
        }
      }
      this.statCache[abs] = stat;
      var c = true;
      if (stat)
        c = stat.isDirectory() ? "DIR" : "FILE";
      this.cache[abs] = this.cache[abs] || c;
      if (needDir && c === "FILE")
        return false;
      return c;
    };
    GlobSync.prototype._mark = function(p) {
      return common.mark(this, p);
    };
    GlobSync.prototype._makeAbs = function(f) {
      return common.makeAbs(this, f);
    };
  }
});

// node_modules/wrappy/wrappy.js
var require_wrappy = __commonJS({
  "node_modules/wrappy/wrappy.js"(exports, module) {
    module.exports = wrappy;
    function wrappy(fn, cb) {
      if (fn && cb)
        return wrappy(fn)(cb);
      if (typeof fn !== "function")
        throw new TypeError("need wrapper function");
      Object.keys(fn).forEach(function(k) {
        wrapper[k] = fn[k];
      });
      return wrapper;
      function wrapper() {
        var args = new Array(arguments.length);
        for (var i = 0; i < args.length; i++) {
          args[i] = arguments[i];
        }
        var ret = fn.apply(this, args);
        var cb2 = args[args.length - 1];
        if (typeof ret === "function" && ret !== cb2) {
          Object.keys(cb2).forEach(function(k) {
            ret[k] = cb2[k];
          });
        }
        return ret;
      }
    }
  }
});

// node_modules/once/once.js
var require_once = __commonJS({
  "node_modules/once/once.js"(exports, module) {
    var wrappy = require_wrappy();
    module.exports = wrappy(once);
    module.exports.strict = wrappy(onceStrict);
    once.proto = once(function() {
      Object.defineProperty(Function.prototype, "once", {
        value: function() {
          return once(this);
        },
        configurable: true
      });
      Object.defineProperty(Function.prototype, "onceStrict", {
        value: function() {
          return onceStrict(this);
        },
        configurable: true
      });
    });
    function once(fn) {
      var f = function() {
        if (f.called)
          return f.value;
        f.called = true;
        return f.value = fn.apply(this, arguments);
      };
      f.called = false;
      return f;
    }
    function onceStrict(fn) {
      var f = function() {
        if (f.called)
          throw new Error(f.onceError);
        f.called = true;
        return f.value = fn.apply(this, arguments);
      };
      var name = fn.name || "Function wrapped with `once`";
      f.onceError = name + " shouldn't be called more than once";
      f.called = false;
      return f;
    }
  }
});

// node_modules/inflight/inflight.js
var require_inflight = __commonJS({
  "node_modules/inflight/inflight.js"(exports, module) {
    var wrappy = require_wrappy();
    var reqs = /* @__PURE__ */ Object.create(null);
    var once = require_once();
    module.exports = wrappy(inflight);
    function inflight(key, cb) {
      if (reqs[key]) {
        reqs[key].push(cb);
        return null;
      } else {
        reqs[key] = [cb];
        return makeres(key);
      }
    }
    function makeres(key) {
      return once(function RES() {
        var cbs = reqs[key];
        var len = cbs.length;
        var args = slice(arguments);
        try {
          for (var i = 0; i < len; i++) {
            cbs[i].apply(null, args);
          }
        } finally {
          if (cbs.length > len) {
            cbs.splice(0, len);
            process.nextTick(function() {
              RES.apply(null, args);
            });
          } else {
            delete reqs[key];
          }
        }
      });
    }
    function slice(args) {
      var length = args.length;
      var array2 = [];
      for (var i = 0; i < length; i++)
        array2[i] = args[i];
      return array2;
    }
  }
});

// node_modules/glob/glob.js
var require_glob = __commonJS({
  "node_modules/glob/glob.js"(exports, module) {
    module.exports = glob;
    var rp = require_fs();
    var minimatch = require_minimatch();
    var Minimatch = minimatch.Minimatch;
    var inherits = require_inherits();
    var EE = __require("events").EventEmitter;
    var path10 = __require("path");
    var assert = __require("assert");
    var isAbsolute = require_path_is_absolute();
    var globSync = require_sync();
    var common = require_common();
    var setopts = common.setopts;
    var ownProp = common.ownProp;
    var inflight = require_inflight();
    var util = __require("util");
    var childrenIgnored = common.childrenIgnored;
    var isIgnored = common.isIgnored;
    var once = require_once();
    function glob(pattern, options, cb) {
      if (typeof options === "function")
        cb = options, options = {};
      if (!options)
        options = {};
      if (options.sync) {
        if (cb)
          throw new TypeError("callback provided to sync glob");
        return globSync(pattern, options);
      }
      return new Glob(pattern, options, cb);
    }
    glob.sync = globSync;
    var GlobSync = glob.GlobSync = globSync.GlobSync;
    glob.glob = glob;
    function extend(origin, add) {
      if (add === null || typeof add !== "object") {
        return origin;
      }
      var keys = Object.keys(add);
      var i = keys.length;
      while (i--) {
        origin[keys[i]] = add[keys[i]];
      }
      return origin;
    }
    glob.hasMagic = function(pattern, options_) {
      var options = extend({}, options_);
      options.noprocess = true;
      var g = new Glob(pattern, options);
      var set = g.minimatch.set;
      if (!pattern)
        return false;
      if (set.length > 1)
        return true;
      for (var j = 0; j < set[0].length; j++) {
        if (typeof set[0][j] !== "string")
          return true;
      }
      return false;
    };
    glob.Glob = Glob;
    inherits(Glob, EE);
    function Glob(pattern, options, cb) {
      if (typeof options === "function") {
        cb = options;
        options = null;
      }
      if (options && options.sync) {
        if (cb)
          throw new TypeError("callback provided to sync glob");
        return new GlobSync(pattern, options);
      }
      if (!(this instanceof Glob))
        return new Glob(pattern, options, cb);
      setopts(this, pattern, options);
      this._didRealPath = false;
      var n = this.minimatch.set.length;
      this.matches = new Array(n);
      if (typeof cb === "function") {
        cb = once(cb);
        this.on("error", cb);
        this.on("end", function(matches) {
          cb(null, matches);
        });
      }
      var self = this;
      this._processing = 0;
      this._emitQueue = [];
      this._processQueue = [];
      this.paused = false;
      if (this.noprocess)
        return this;
      if (n === 0)
        return done();
      var sync = true;
      for (var i = 0; i < n; i++) {
        this._process(this.minimatch.set[i], i, false, done);
      }
      sync = false;
      function done() {
        --self._processing;
        if (self._processing <= 0) {
          if (sync) {
            process.nextTick(function() {
              self._finish();
            });
          } else {
            self._finish();
          }
        }
      }
    }
    Glob.prototype._finish = function() {
      assert(this instanceof Glob);
      if (this.aborted)
        return;
      if (this.realpath && !this._didRealpath)
        return this._realpath();
      common.finish(this);
      this.emit("end", this.found);
    };
    Glob.prototype._realpath = function() {
      if (this._didRealpath)
        return;
      this._didRealpath = true;
      var n = this.matches.length;
      if (n === 0)
        return this._finish();
      var self = this;
      for (var i = 0; i < this.matches.length; i++)
        this._realpathSet(i, next);
      function next() {
        if (--n === 0)
          self._finish();
      }
    };
    Glob.prototype._realpathSet = function(index, cb) {
      var matchset = this.matches[index];
      if (!matchset)
        return cb();
      var found = Object.keys(matchset);
      var self = this;
      var n = found.length;
      if (n === 0)
        return cb();
      var set = this.matches[index] = /* @__PURE__ */ Object.create(null);
      found.forEach(function(p, i) {
        p = self._makeAbs(p);
        rp.realpath(p, self.realpathCache, function(er, real) {
          if (!er)
            set[real] = true;
          else if (er.syscall === "stat")
            set[p] = true;
          else
            self.emit("error", er);
          if (--n === 0) {
            self.matches[index] = set;
            cb();
          }
        });
      });
    };
    Glob.prototype._mark = function(p) {
      return common.mark(this, p);
    };
    Glob.prototype._makeAbs = function(f) {
      return common.makeAbs(this, f);
    };
    Glob.prototype.abort = function() {
      this.aborted = true;
      this.emit("abort");
    };
    Glob.prototype.pause = function() {
      if (!this.paused) {
        this.paused = true;
        this.emit("pause");
      }
    };
    Glob.prototype.resume = function() {
      if (this.paused) {
        this.emit("resume");
        this.paused = false;
        if (this._emitQueue.length) {
          var eq = this._emitQueue.slice(0);
          this._emitQueue.length = 0;
          for (var i = 0; i < eq.length; i++) {
            var e = eq[i];
            this._emitMatch(e[0], e[1]);
          }
        }
        if (this._processQueue.length) {
          var pq = this._processQueue.slice(0);
          this._processQueue.length = 0;
          for (var i = 0; i < pq.length; i++) {
            var p = pq[i];
            this._processing--;
            this._process(p[0], p[1], p[2], p[3]);
          }
        }
      }
    };
    Glob.prototype._process = function(pattern, index, inGlobStar, cb) {
      assert(this instanceof Glob);
      assert(typeof cb === "function");
      if (this.aborted)
        return;
      this._processing++;
      if (this.paused) {
        this._processQueue.push([pattern, index, inGlobStar, cb]);
        return;
      }
      var n = 0;
      while (typeof pattern[n] === "string") {
        n++;
      }
      var prefix;
      switch (n) {
        case pattern.length:
          this._processSimple(pattern.join("/"), index, cb);
          return;
        case 0:
          prefix = null;
          break;
        default:
          prefix = pattern.slice(0, n).join("/");
          break;
      }
      var remain = pattern.slice(n);
      var read;
      if (prefix === null)
        read = ".";
      else if (isAbsolute(prefix) || isAbsolute(pattern.map(function(p) {
        return typeof p === "string" ? p : "[*]";
      }).join("/"))) {
        if (!prefix || !isAbsolute(prefix))
          prefix = "/" + prefix;
        read = prefix;
      } else
        read = prefix;
      var abs = this._makeAbs(read);
      if (childrenIgnored(this, read))
        return cb();
      var isGlobStar = remain[0] === minimatch.GLOBSTAR;
      if (isGlobStar)
        this._processGlobStar(prefix, read, abs, remain, index, inGlobStar, cb);
      else
        this._processReaddir(prefix, read, abs, remain, index, inGlobStar, cb);
    };
    Glob.prototype._processReaddir = function(prefix, read, abs, remain, index, inGlobStar, cb) {
      var self = this;
      this._readdir(abs, inGlobStar, function(er, entries) {
        return self._processReaddir2(prefix, read, abs, remain, index, inGlobStar, entries, cb);
      });
    };
    Glob.prototype._processReaddir2 = function(prefix, read, abs, remain, index, inGlobStar, entries, cb) {
      if (!entries)
        return cb();
      var pn = remain[0];
      var negate = !!this.minimatch.negate;
      var rawGlob = pn._glob;
      var dotOk = this.dot || rawGlob.charAt(0) === ".";
      var matchedEntries = [];
      for (var i = 0; i < entries.length; i++) {
        var e = entries[i];
        if (e.charAt(0) !== "." || dotOk) {
          var m;
          if (negate && !prefix) {
            m = !e.match(pn);
          } else {
            m = e.match(pn);
          }
          if (m)
            matchedEntries.push(e);
        }
      }
      var len = matchedEntries.length;
      if (len === 0)
        return cb();
      if (remain.length === 1 && !this.mark && !this.stat) {
        if (!this.matches[index])
          this.matches[index] = /* @__PURE__ */ Object.create(null);
        for (var i = 0; i < len; i++) {
          var e = matchedEntries[i];
          if (prefix) {
            if (prefix !== "/")
              e = prefix + "/" + e;
            else
              e = prefix + e;
          }
          if (e.charAt(0) === "/" && !this.nomount) {
            e = path10.join(this.root, e);
          }
          this._emitMatch(index, e);
        }
        return cb();
      }
      remain.shift();
      for (var i = 0; i < len; i++) {
        var e = matchedEntries[i];
        var newPattern;
        if (prefix) {
          if (prefix !== "/")
            e = prefix + "/" + e;
          else
            e = prefix + e;
        }
        this._process([e].concat(remain), index, inGlobStar, cb);
      }
      cb();
    };
    Glob.prototype._emitMatch = function(index, e) {
      if (this.aborted)
        return;
      if (isIgnored(this, e))
        return;
      if (this.paused) {
        this._emitQueue.push([index, e]);
        return;
      }
      var abs = isAbsolute(e) ? e : this._makeAbs(e);
      if (this.mark)
        e = this._mark(e);
      if (this.absolute)
        e = abs;
      if (this.matches[index][e])
        return;
      if (this.nodir) {
        var c = this.cache[abs];
        if (c === "DIR" || Array.isArray(c))
          return;
      }
      this.matches[index][e] = true;
      var st = this.statCache[abs];
      if (st)
        this.emit("stat", e, st);
      this.emit("match", e);
    };
    Glob.prototype._readdirInGlobStar = function(abs, cb) {
      if (this.aborted)
        return;
      if (this.follow)
        return this._readdir(abs, false, cb);
      var lstatkey = "lstat\0" + abs;
      var self = this;
      var lstatcb = inflight(lstatkey, lstatcb_);
      if (lstatcb)
        self.fs.lstat(abs, lstatcb);
      function lstatcb_(er, lstat) {
        if (er && er.code === "ENOENT")
          return cb();
        var isSym = lstat && lstat.isSymbolicLink();
        self.symlinks[abs] = isSym;
        if (!isSym && lstat && !lstat.isDirectory()) {
          self.cache[abs] = "FILE";
          cb();
        } else
          self._readdir(abs, false, cb);
      }
    };
    Glob.prototype._readdir = function(abs, inGlobStar, cb) {
      if (this.aborted)
        return;
      cb = inflight("readdir\0" + abs + "\0" + inGlobStar, cb);
      if (!cb)
        return;
      if (inGlobStar && !ownProp(this.symlinks, abs))
        return this._readdirInGlobStar(abs, cb);
      if (ownProp(this.cache, abs)) {
        var c = this.cache[abs];
        if (!c || c === "FILE")
          return cb();
        if (Array.isArray(c))
          return cb(null, c);
      }
      var self = this;
      self.fs.readdir(abs, readdirCb(this, abs, cb));
    };
    function readdirCb(self, abs, cb) {
      return function(er, entries) {
        if (er)
          self._readdirError(abs, er, cb);
        else
          self._readdirEntries(abs, entries, cb);
      };
    }
    Glob.prototype._readdirEntries = function(abs, entries, cb) {
      if (this.aborted)
        return;
      if (!this.mark && !this.stat) {
        for (var i = 0; i < entries.length; i++) {
          var e = entries[i];
          if (abs === "/")
            e = abs + e;
          else
            e = abs + "/" + e;
          this.cache[e] = true;
        }
      }
      this.cache[abs] = entries;
      return cb(null, entries);
    };
    Glob.prototype._readdirError = function(f, er, cb) {
      if (this.aborted)
        return;
      switch (er.code) {
        case "ENOTSUP":
        case "ENOTDIR":
          var abs = this._makeAbs(f);
          this.cache[abs] = "FILE";
          if (abs === this.cwdAbs) {
            var error = new Error(er.code + " invalid cwd " + this.cwd);
            error.path = this.cwd;
            error.code = er.code;
            this.emit("error", error);
            this.abort();
          }
          break;
        case "ENOENT":
        case "ELOOP":
        case "ENAMETOOLONG":
        case "UNKNOWN":
          this.cache[this._makeAbs(f)] = false;
          break;
        default:
          this.cache[this._makeAbs(f)] = false;
          if (this.strict) {
            this.emit("error", er);
            this.abort();
          }
          if (!this.silent)
            console.error("glob error", er);
          break;
      }
      return cb();
    };
    Glob.prototype._processGlobStar = function(prefix, read, abs, remain, index, inGlobStar, cb) {
      var self = this;
      this._readdir(abs, inGlobStar, function(er, entries) {
        self._processGlobStar2(prefix, read, abs, remain, index, inGlobStar, entries, cb);
      });
    };
    Glob.prototype._processGlobStar2 = function(prefix, read, abs, remain, index, inGlobStar, entries, cb) {
      if (!entries)
        return cb();
      var remainWithoutGlobStar = remain.slice(1);
      var gspref = prefix ? [prefix] : [];
      var noGlobStar = gspref.concat(remainWithoutGlobStar);
      this._process(noGlobStar, index, false, cb);
      var isSym = this.symlinks[abs];
      var len = entries.length;
      if (isSym && inGlobStar)
        return cb();
      for (var i = 0; i < len; i++) {
        var e = entries[i];
        if (e.charAt(0) === "." && !this.dot)
          continue;
        var instead = gspref.concat(entries[i], remainWithoutGlobStar);
        this._process(instead, index, true, cb);
        var below = gspref.concat(entries[i], remain);
        this._process(below, index, true, cb);
      }
      cb();
    };
    Glob.prototype._processSimple = function(prefix, index, cb) {
      var self = this;
      this._stat(prefix, function(er, exists) {
        self._processSimple2(prefix, index, er, exists, cb);
      });
    };
    Glob.prototype._processSimple2 = function(prefix, index, er, exists, cb) {
      if (!this.matches[index])
        this.matches[index] = /* @__PURE__ */ Object.create(null);
      if (!exists)
        return cb();
      if (prefix && isAbsolute(prefix) && !this.nomount) {
        var trail = /[\/\\]$/.test(prefix);
        if (prefix.charAt(0) === "/") {
          prefix = path10.join(this.root, prefix);
        } else {
          prefix = path10.resolve(this.root, prefix);
          if (trail)
            prefix += "/";
        }
      }
      if (process.platform === "win32")
        prefix = prefix.replace(/\\/g, "/");
      this._emitMatch(index, prefix);
      cb();
    };
    Glob.prototype._stat = function(f, cb) {
      var abs = this._makeAbs(f);
      var needDir = f.slice(-1) === "/";
      if (f.length > this.maxLength)
        return cb();
      if (!this.stat && ownProp(this.cache, abs)) {
        var c = this.cache[abs];
        if (Array.isArray(c))
          c = "DIR";
        if (!needDir || c === "DIR")
          return cb(null, c);
        if (needDir && c === "FILE")
          return cb();
      }
      var exists;
      var stat = this.statCache[abs];
      if (stat !== void 0) {
        if (stat === false)
          return cb(null, stat);
        else {
          var type = stat.isDirectory() ? "DIR" : "FILE";
          if (needDir && type === "FILE")
            return cb();
          else
            return cb(null, type, stat);
        }
      }
      var self = this;
      var statcb = inflight("stat\0" + abs, lstatcb_);
      if (statcb)
        self.fs.lstat(abs, statcb);
      function lstatcb_(er, lstat) {
        if (lstat && lstat.isSymbolicLink()) {
          return self.fs.stat(abs, function(er2, stat2) {
            if (er2)
              self._stat2(f, abs, null, lstat, cb);
            else
              self._stat2(f, abs, er2, stat2, cb);
          });
        } else {
          self._stat2(f, abs, er, lstat, cb);
        }
      }
    };
    Glob.prototype._stat2 = function(f, abs, er, stat, cb) {
      if (er && (er.code === "ENOENT" || er.code === "ENOTDIR")) {
        this.statCache[abs] = false;
        return cb();
      }
      var needDir = f.slice(-1) === "/";
      this.statCache[abs] = stat;
      if (abs.slice(-1) === "/" && stat && !stat.isDirectory())
        return cb(null, false, stat);
      var c = true;
      if (stat)
        c = stat.isDirectory() ? "DIR" : "FILE";
      this.cache[abs] = this.cache[abs] || c;
      if (needDir && c === "FILE")
        return cb();
      return cb(null, c, stat);
    };
  }
});

// node_modules/flat-cache/node_modules/rimraf/rimraf.js
var require_rimraf = __commonJS({
  "node_modules/flat-cache/node_modules/rimraf/rimraf.js"(exports, module) {
    var assert = __require("assert");
    var path10 = __require("path");
    var fs6 = __require("fs");
    var glob = void 0;
    try {
      glob = require_glob();
    } catch (_err) {
    }
    var defaultGlobOpts = {
      nosort: true,
      silent: true
    };
    var timeout = 0;
    var isWindows = process.platform === "win32";
    var defaults = (options) => {
      const methods = [
        "unlink",
        "chmod",
        "stat",
        "lstat",
        "rmdir",
        "readdir"
      ];
      methods.forEach((m) => {
        options[m] = options[m] || fs6[m];
        m = m + "Sync";
        options[m] = options[m] || fs6[m];
      });
      options.maxBusyTries = options.maxBusyTries || 3;
      options.emfileWait = options.emfileWait || 1e3;
      if (options.glob === false) {
        options.disableGlob = true;
      }
      if (options.disableGlob !== true && glob === void 0) {
        throw Error("glob dependency not found, set `options.disableGlob = true` if intentional");
      }
      options.disableGlob = options.disableGlob || false;
      options.glob = options.glob || defaultGlobOpts;
    };
    var rimraf = (p, options, cb) => {
      if (typeof options === "function") {
        cb = options;
        options = {};
      }
      assert(p, "rimraf: missing path");
      assert.equal(typeof p, "string", "rimraf: path should be a string");
      assert.equal(typeof cb, "function", "rimraf: callback function required");
      assert(options, "rimraf: invalid options argument provided");
      assert.equal(typeof options, "object", "rimraf: options should be object");
      defaults(options);
      let busyTries = 0;
      let errState = null;
      let n = 0;
      const next = (er) => {
        errState = errState || er;
        if (--n === 0)
          cb(errState);
      };
      const afterGlob = (er, results) => {
        if (er)
          return cb(er);
        n = results.length;
        if (n === 0)
          return cb();
        results.forEach((p2) => {
          const CB = (er2) => {
            if (er2) {
              if ((er2.code === "EBUSY" || er2.code === "ENOTEMPTY" || er2.code === "EPERM") && busyTries < options.maxBusyTries) {
                busyTries++;
                return setTimeout(() => rimraf_(p2, options, CB), busyTries * 100);
              }
              if (er2.code === "EMFILE" && timeout < options.emfileWait) {
                return setTimeout(() => rimraf_(p2, options, CB), timeout++);
              }
              if (er2.code === "ENOENT")
                er2 = null;
            }
            timeout = 0;
            next(er2);
          };
          rimraf_(p2, options, CB);
        });
      };
      if (options.disableGlob || !glob.hasMagic(p))
        return afterGlob(null, [p]);
      options.lstat(p, (er, stat) => {
        if (!er)
          return afterGlob(null, [p]);
        glob(p, options.glob, afterGlob);
      });
    };
    var rimraf_ = (p, options, cb) => {
      assert(p);
      assert(options);
      assert(typeof cb === "function");
      options.lstat(p, (er, st) => {
        if (er && er.code === "ENOENT")
          return cb(null);
        if (er && er.code === "EPERM" && isWindows)
          fixWinEPERM(p, options, er, cb);
        if (st && st.isDirectory())
          return rmdir(p, options, er, cb);
        options.unlink(p, (er2) => {
          if (er2) {
            if (er2.code === "ENOENT")
              return cb(null);
            if (er2.code === "EPERM")
              return isWindows ? fixWinEPERM(p, options, er2, cb) : rmdir(p, options, er2, cb);
            if (er2.code === "EISDIR")
              return rmdir(p, options, er2, cb);
          }
          return cb(er2);
        });
      });
    };
    var fixWinEPERM = (p, options, er, cb) => {
      assert(p);
      assert(options);
      assert(typeof cb === "function");
      options.chmod(p, 438, (er2) => {
        if (er2)
          cb(er2.code === "ENOENT" ? null : er);
        else
          options.stat(p, (er3, stats) => {
            if (er3)
              cb(er3.code === "ENOENT" ? null : er);
            else if (stats.isDirectory())
              rmdir(p, options, er, cb);
            else
              options.unlink(p, cb);
          });
      });
    };
    var fixWinEPERMSync = (p, options, er) => {
      assert(p);
      assert(options);
      try {
        options.chmodSync(p, 438);
      } catch (er2) {
        if (er2.code === "ENOENT")
          return;
        else
          throw er;
      }
      let stats;
      try {
        stats = options.statSync(p);
      } catch (er3) {
        if (er3.code === "ENOENT")
          return;
        else
          throw er;
      }
      if (stats.isDirectory())
        rmdirSync(p, options, er);
      else
        options.unlinkSync(p);
    };
    var rmdir = (p, options, originalEr, cb) => {
      assert(p);
      assert(options);
      assert(typeof cb === "function");
      options.rmdir(p, (er) => {
        if (er && (er.code === "ENOTEMPTY" || er.code === "EEXIST" || er.code === "EPERM"))
          rmkids(p, options, cb);
        else if (er && er.code === "ENOTDIR")
          cb(originalEr);
        else
          cb(er);
      });
    };
    var rmkids = (p, options, cb) => {
      assert(p);
      assert(options);
      assert(typeof cb === "function");
      options.readdir(p, (er, files) => {
        if (er)
          return cb(er);
        let n = files.length;
        if (n === 0)
          return options.rmdir(p, cb);
        let errState;
        files.forEach((f) => {
          rimraf(path10.join(p, f), options, (er2) => {
            if (errState)
              return;
            if (er2)
              return cb(errState = er2);
            if (--n === 0)
              options.rmdir(p, cb);
          });
        });
      });
    };
    var rimrafSync = (p, options) => {
      options = options || {};
      defaults(options);
      assert(p, "rimraf: missing path");
      assert.equal(typeof p, "string", "rimraf: path should be a string");
      assert(options, "rimraf: missing options");
      assert.equal(typeof options, "object", "rimraf: options should be object");
      let results;
      if (options.disableGlob || !glob.hasMagic(p)) {
        results = [p];
      } else {
        try {
          options.lstatSync(p);
          results = [p];
        } catch (er) {
          results = glob.sync(p, options.glob);
        }
      }
      if (!results.length)
        return;
      for (let i = 0; i < results.length; i++) {
        const p2 = results[i];
        let st;
        try {
          st = options.lstatSync(p2);
        } catch (er) {
          if (er.code === "ENOENT")
            return;
          if (er.code === "EPERM" && isWindows)
            fixWinEPERMSync(p2, options, er);
        }
        try {
          if (st && st.isDirectory())
            rmdirSync(p2, options, null);
          else
            options.unlinkSync(p2);
        } catch (er) {
          if (er.code === "ENOENT")
            return;
          if (er.code === "EPERM")
            return isWindows ? fixWinEPERMSync(p2, options, er) : rmdirSync(p2, options, er);
          if (er.code !== "EISDIR")
            throw er;
          rmdirSync(p2, options, er);
        }
      }
    };
    var rmdirSync = (p, options, originalEr) => {
      assert(p);
      assert(options);
      try {
        options.rmdirSync(p);
      } catch (er) {
        if (er.code === "ENOENT")
          return;
        if (er.code === "ENOTDIR")
          throw originalEr;
        if (er.code === "ENOTEMPTY" || er.code === "EEXIST" || er.code === "EPERM")
          rmkidsSync(p, options);
      }
    };
    var rmkidsSync = (p, options) => {
      assert(p);
      assert(options);
      options.readdirSync(p).forEach((f) => rimrafSync(path10.join(p, f), options));
      const retries = isWindows ? 100 : 1;
      let i = 0;
      do {
        let threw = true;
        try {
          const ret = options.rmdirSync(p, options);
          threw = false;
          return ret;
        } finally {
          if (++i < retries && threw)
            continue;
        }
      } while (true);
    };
    module.exports = rimraf;
    rimraf.sync = rimrafSync;
  }
});

// node_modules/flat-cache/src/del.js
var require_del = __commonJS({
  "node_modules/flat-cache/src/del.js"(exports, module) {
    var rimraf = require_rimraf().sync;
    var fs6 = __require("fs");
    module.exports = function del(file) {
      if (fs6.existsSync(file)) {
        rimraf(file, {
          glob: false
        });
        return true;
      }
      return false;
    };
  }
});

// node_modules/flat-cache/src/cache.js
var require_cache = __commonJS({
  "node_modules/flat-cache/src/cache.js"(exports, module) {
    var path10 = __require("path");
    var fs6 = __require("fs");
    var Keyv = require_src();
    var utils = require_utils();
    var del = require_del();
    var writeJSON = utils.writeJSON;
    var cache = {
      /**
       * Load a cache identified by the given Id. If the element does not exists, then initialize an empty
       * cache storage. If specified `cacheDir` will be used as the directory to persist the data to. If omitted
       * then the cache module directory `./cache` will be used instead
       *
       * @method load
       * @param docId {String} the id of the cache, would also be used as the name of the file cache
       * @param [cacheDir] {String} directory for the cache entry
       */
      load: function(docId, cacheDir) {
        var me = this;
        me.keyv = new Keyv();
        me.__visited = {};
        me.__persisted = {};
        me._pathToFile = cacheDir ? path10.resolve(cacheDir, docId) : path10.resolve(__dirname, "../.cache/", docId);
        if (fs6.existsSync(me._pathToFile)) {
          me._persisted = utils.tryParse(me._pathToFile, {});
        }
      },
      get _persisted() {
        return this.__persisted;
      },
      set _persisted(value) {
        this.__persisted = value;
        this.keyv.set("persisted", value);
      },
      get _visited() {
        return this.__visited;
      },
      set _visited(value) {
        this.__visited = value;
        this.keyv.set("visited", value);
      },
      /**
       * Load the cache from the provided file
       * @method loadFile
       * @param  {String} pathToFile the path to the file containing the info for the cache
       */
      loadFile: function(pathToFile) {
        var me = this;
        var dir = path10.dirname(pathToFile);
        var fName = path10.basename(pathToFile);
        me.load(fName, dir);
      },
      /**
       * Returns the entire persisted object
       * @method all
       * @returns {*}
       */
      all: function() {
        return this._persisted;
      },
      keys: function() {
        return Object.keys(this._persisted);
      },
      /**
       * sets a key to a given value
       * @method setKey
       * @param key {string} the key to set
       * @param value {object} the value of the key. Could be any object that can be serialized with JSON.stringify
       */
      setKey: function(key, value) {
        this._visited[key] = true;
        this._persisted[key] = value;
      },
      /**
       * remove a given key from the cache
       * @method removeKey
       * @param key {String} the key to remove from the object
       */
      removeKey: function(key) {
        delete this._visited[key];
        delete this._persisted[key];
      },
      /**
       * Return the value of the provided key
       * @method getKey
       * @param key {String} the name of the key to retrieve
       * @returns {*} the value from the key
       */
      getKey: function(key) {
        this._visited[key] = true;
        return this._persisted[key];
      },
      /**
       * Remove keys that were not accessed/set since the
       * last time the `prune` method was called.
       * @method _prune
       * @private
       */
      _prune: function() {
        var me = this;
        var obj = {};
        var keys = Object.keys(me._visited);
        if (keys.length === 0) {
          return;
        }
        keys.forEach(function(key) {
          obj[key] = me._persisted[key];
        });
        me._visited = {};
        me._persisted = obj;
      },
      /**
       * Save the state of the cache identified by the docId to disk
       * as a JSON structure
       * @param [noPrune=false] {Boolean} whether to remove from cache the non visited files
       * @method save
       */
      save: function(noPrune) {
        var me = this;
        !noPrune && me._prune();
        writeJSON(me._pathToFile, me._persisted);
      },
      /**
       * remove the file where the cache is persisted
       * @method removeCacheFile
       * @return {Boolean} true or false if the file was successfully deleted
       */
      removeCacheFile: function() {
        return del(this._pathToFile);
      },
      /**
       * Destroy the file cache and cache content.
       * @method destroy
       */
      destroy: function() {
        var me = this;
        me._visited = {};
        me._persisted = {};
        me.removeCacheFile();
      }
    };
    module.exports = {
      /**
       * Alias for create. Should be considered depreacted. Will be removed in next releases
       *
       * @method load
       * @param docId {String} the id of the cache, would also be used as the name of the file cache
       * @param [cacheDir] {String} directory for the cache entry
       * @returns {cache} cache instance
       */
      load: function(docId, cacheDir) {
        return this.create(docId, cacheDir);
      },
      /**
       * Load a cache identified by the given Id. If the element does not exists, then initialize an empty
       * cache storage.
       *
       * @method create
       * @param docId {String} the id of the cache, would also be used as the name of the file cache
       * @param [cacheDir] {String} directory for the cache entry
       * @returns {cache} cache instance
       */
      create: function(docId, cacheDir) {
        var obj = Object.create(cache);
        obj.load(docId, cacheDir);
        return obj;
      },
      createFromFile: function(filePath) {
        var obj = Object.create(cache);
        obj.loadFile(filePath);
        return obj;
      },
      /**
       * Clear the cache identified by the given id. Caches stored in a different cache directory can be deleted directly
       *
       * @method clearCache
       * @param docId {String} the id of the cache, would also be used as the name of the file cache
       * @param cacheDir {String} the directory where the cache file was written
       * @returns {Boolean} true if the cache folder was deleted. False otherwise
       */
      clearCacheById: function(docId, cacheDir) {
        var filePath = cacheDir ? path10.resolve(cacheDir, docId) : path10.resolve(__dirname, "../.cache/", docId);
        return del(filePath);
      },
      /**
       * Remove all cache stored in the cache directory
       * @method clearAll
       * @returns {Boolean} true if the cache folder was deleted. False otherwise
       */
      clearAll: function(cacheDir) {
        var filePath = cacheDir ? path10.resolve(cacheDir) : path10.resolve(__dirname, "../.cache/");
        return del(filePath);
      }
    };
  }
});

// node_modules/file-entry-cache/cache.js
var require_cache2 = __commonJS({
  "node_modules/file-entry-cache/cache.js"(exports, module) {
    var path10 = __require("path");
    var crypto = __require("crypto");
    module.exports = {
      createFromFile: function(filePath, useChecksum) {
        var fname = path10.basename(filePath);
        var dir = path10.dirname(filePath);
        return this.create(fname, dir, useChecksum);
      },
      create: function(cacheId, _path, useChecksum) {
        var fs6 = __require("fs");
        var flatCache = require_cache();
        var cache = flatCache.load(cacheId, _path);
        var normalizedEntries = {};
        var removeNotFoundFiles = function removeNotFoundFiles2() {
          const cachedEntries = cache.keys();
          cachedEntries.forEach(function remover(fPath) {
            try {
              fs6.statSync(fPath);
            } catch (err) {
              if (err.code === "ENOENT") {
                cache.removeKey(fPath);
              }
            }
          });
        };
        removeNotFoundFiles();
        return {
          /**
           * the flat cache storage used to persist the metadata of the `files
           * @type {Object}
           */
          cache,
          /**
           * Given a buffer, calculate md5 hash of its content.
           * @method getHash
           * @param  {Buffer} buffer   buffer to calculate hash on
           * @return {String}          content hash digest
           */
          getHash: function(buffer) {
            return crypto.createHash("md5").update(buffer).digest("hex");
          },
          /**
           * Return whether or not a file has changed since last time reconcile was called.
           * @method hasFileChanged
           * @param  {String}  file  the filepath to check
           * @return {Boolean}       wheter or not the file has changed
           */
          hasFileChanged: function(file) {
            return this.getFileDescriptor(file).changed;
          },
          /**
           * given an array of file paths it return and object with three arrays:
           *  - changedFiles: Files that changed since previous run
           *  - notChangedFiles: Files that haven't change
           *  - notFoundFiles: Files that were not found, probably deleted
           *
           * @param  {Array} files the files to analyze and compare to the previous seen files
           * @return {[type]}       [description]
           */
          analyzeFiles: function(files) {
            var me = this;
            files = files || [];
            var res = {
              changedFiles: [],
              notFoundFiles: [],
              notChangedFiles: []
            };
            me.normalizeEntries(files).forEach(function(entry) {
              if (entry.changed) {
                res.changedFiles.push(entry.key);
                return;
              }
              if (entry.notFound) {
                res.notFoundFiles.push(entry.key);
                return;
              }
              res.notChangedFiles.push(entry.key);
            });
            return res;
          },
          getFileDescriptor: function(file) {
            var fstat;
            try {
              fstat = fs6.statSync(file);
            } catch (ex) {
              this.removeEntry(file);
              return { key: file, notFound: true, err: ex };
            }
            if (useChecksum) {
              return this._getFileDescriptorUsingChecksum(file);
            }
            return this._getFileDescriptorUsingMtimeAndSize(file, fstat);
          },
          _getFileDescriptorUsingMtimeAndSize: function(file, fstat) {
            var meta = cache.getKey(file);
            var cacheExists = !!meta;
            var cSize = fstat.size;
            var cTime = fstat.mtime.getTime();
            var isDifferentDate;
            var isDifferentSize;
            if (!meta) {
              meta = { size: cSize, mtime: cTime };
            } else {
              isDifferentDate = cTime !== meta.mtime;
              isDifferentSize = cSize !== meta.size;
            }
            var nEntry = normalizedEntries[file] = {
              key: file,
              changed: !cacheExists || isDifferentDate || isDifferentSize,
              meta
            };
            return nEntry;
          },
          _getFileDescriptorUsingChecksum: function(file) {
            var meta = cache.getKey(file);
            var cacheExists = !!meta;
            var contentBuffer;
            try {
              contentBuffer = fs6.readFileSync(file);
            } catch (ex) {
              contentBuffer = "";
            }
            var isDifferent = true;
            var hash = this.getHash(contentBuffer);
            if (!meta) {
              meta = { hash };
            } else {
              isDifferent = hash !== meta.hash;
            }
            var nEntry = normalizedEntries[file] = {
              key: file,
              changed: !cacheExists || isDifferent,
              meta
            };
            return nEntry;
          },
          /**
           * Return the list o the files that changed compared
           * against the ones stored in the cache
           *
           * @method getUpdated
           * @param files {Array} the array of files to compare against the ones in the cache
           * @returns {Array}
           */
          getUpdatedFiles: function(files) {
            var me = this;
            files = files || [];
            return me.normalizeEntries(files).filter(function(entry) {
              return entry.changed;
            }).map(function(entry) {
              return entry.key;
            });
          },
          /**
           * return the list of files
           * @method normalizeEntries
           * @param files
           * @returns {*}
           */
          normalizeEntries: function(files) {
            files = files || [];
            var me = this;
            var nEntries = files.map(function(file) {
              return me.getFileDescriptor(file);
            });
            return nEntries;
          },
          /**
           * Remove an entry from the file-entry-cache. Useful to force the file to still be considered
           * modified the next time the process is run
           *
           * @method removeEntry
           * @param entryName
           */
          removeEntry: function(entryName) {
            delete normalizedEntries[entryName];
            cache.removeKey(entryName);
          },
          /**
           * Delete the cache file from the disk
           * @method deleteCacheFile
           */
          deleteCacheFile: function() {
            cache.removeCacheFile();
          },
          /**
           * remove the cache from the file and clear the memory cache
           */
          destroy: function() {
            normalizedEntries = {};
            cache.destroy();
          },
          _getMetaForFileUsingCheckSum: function(cacheEntry) {
            var contentBuffer = fs6.readFileSync(cacheEntry.key);
            var hash = this.getHash(contentBuffer);
            var meta = Object.assign(cacheEntry.meta, { hash });
            delete meta.size;
            delete meta.mtime;
            return meta;
          },
          _getMetaForFileUsingMtimeAndSize: function(cacheEntry) {
            var stat = fs6.statSync(cacheEntry.key);
            var meta = Object.assign(cacheEntry.meta, {
              size: stat.size,
              mtime: stat.mtime.getTime()
            });
            delete meta.hash;
            return meta;
          },
          /**
           * Sync the files and persist them to the cache
           * @method reconcile
           */
          reconcile: function(noPrune) {
            removeNotFoundFiles();
            noPrune = typeof noPrune === "undefined" ? true : noPrune;
            var entries = normalizedEntries;
            var keys = Object.keys(entries);
            if (keys.length === 0) {
              return;
            }
            var me = this;
            keys.forEach(function(entryName) {
              var cacheEntry = entries[entryName];
              try {
                var meta = useChecksum ? me._getMetaForFileUsingCheckSum(cacheEntry) : me._getMetaForFileUsingMtimeAndSize(cacheEntry);
                cache.setKey(entryName, meta);
              } catch (err) {
                if (err.code !== "ENOENT") {
                  throw err;
                }
              }
            });
            cache.save(noPrune);
          }
        };
      }
    };
  }
});

// node_modules/wcwidth.js/combining.js
var require_combining = __commonJS({
  "node_modules/wcwidth.js/combining.js"(exports, module) {
    module.exports = [
      [768, 879],
      [1155, 1158],
      [1160, 1161],
      [1425, 1469],
      [1471, 1471],
      [1473, 1474],
      [1476, 1477],
      [1479, 1479],
      [1536, 1539],
      [1552, 1557],
      [1611, 1630],
      [1648, 1648],
      [1750, 1764],
      [1767, 1768],
      [1770, 1773],
      [1807, 1807],
      [1809, 1809],
      [1840, 1866],
      [1958, 1968],
      [2027, 2035],
      [2305, 2306],
      [2364, 2364],
      [2369, 2376],
      [2381, 2381],
      [2385, 2388],
      [2402, 2403],
      [2433, 2433],
      [2492, 2492],
      [2497, 2500],
      [2509, 2509],
      [2530, 2531],
      [2561, 2562],
      [2620, 2620],
      [2625, 2626],
      [2631, 2632],
      [2635, 2637],
      [2672, 2673],
      [2689, 2690],
      [2748, 2748],
      [2753, 2757],
      [2759, 2760],
      [2765, 2765],
      [2786, 2787],
      [2817, 2817],
      [2876, 2876],
      [2879, 2879],
      [2881, 2883],
      [2893, 2893],
      [2902, 2902],
      [2946, 2946],
      [3008, 3008],
      [3021, 3021],
      [3134, 3136],
      [3142, 3144],
      [3146, 3149],
      [3157, 3158],
      [3260, 3260],
      [3263, 3263],
      [3270, 3270],
      [3276, 3277],
      [3298, 3299],
      [3393, 3395],
      [3405, 3405],
      [3530, 3530],
      [3538, 3540],
      [3542, 3542],
      [3633, 3633],
      [3636, 3642],
      [3655, 3662],
      [3761, 3761],
      [3764, 3769],
      [3771, 3772],
      [3784, 3789],
      [3864, 3865],
      [3893, 3893],
      [3895, 3895],
      [3897, 3897],
      [3953, 3966],
      [3968, 3972],
      [3974, 3975],
      [3984, 3991],
      [3993, 4028],
      [4038, 4038],
      [4141, 4144],
      [4146, 4146],
      [4150, 4151],
      [4153, 4153],
      [4184, 4185],
      [4448, 4607],
      [4959, 4959],
      [5906, 5908],
      [5938, 5940],
      [5970, 5971],
      [6002, 6003],
      [6068, 6069],
      [6071, 6077],
      [6086, 6086],
      [6089, 6099],
      [6109, 6109],
      [6155, 6157],
      [6313, 6313],
      [6432, 6434],
      [6439, 6440],
      [6450, 6450],
      [6457, 6459],
      [6679, 6680],
      [6912, 6915],
      [6964, 6964],
      [6966, 6970],
      [6972, 6972],
      [6978, 6978],
      [7019, 7027],
      [7616, 7626],
      [7678, 7679],
      [8203, 8207],
      [8234, 8238],
      [8288, 8291],
      [8298, 8303],
      [8400, 8431],
      [12330, 12335],
      [12441, 12442],
      [43014, 43014],
      [43019, 43019],
      [43045, 43046],
      [64286, 64286],
      [65024, 65039],
      [65056, 65059],
      [65279, 65279],
      [65529, 65531],
      [68097, 68099],
      [68101, 68102],
      [68108, 68111],
      [68152, 68154],
      [68159, 68159],
      [119143, 119145],
      [119155, 119170],
      [119173, 119179],
      [119210, 119213],
      [119362, 119364],
      [917505, 917505],
      [917536, 917631],
      [917760, 917999]
    ];
  }
});

// node_modules/wcwidth.js/index.js
var require_wcwidth = __commonJS({
  "node_modules/wcwidth.js/index.js"(exports, module) {
    var combining = require_combining();
    var DEFAULTS = {
      nul: 0,
      control: 0
    };
    function bisearch(ucs) {
      let min = 0;
      let max = combining.length - 1;
      let mid;
      if (ucs < combining[0][0] || ucs > combining[max][1])
        return false;
      while (max >= min) {
        mid = Math.floor((min + max) / 2);
        if (ucs > combining[mid][1])
          min = mid + 1;
        else if (ucs < combining[mid][0])
          max = mid - 1;
        else
          return true;
      }
      return false;
    }
    function wcwidth2(ucs, opts) {
      if (ucs === 0)
        return opts.nul;
      if (ucs < 32 || ucs >= 127 && ucs < 160)
        return opts.control;
      if (bisearch(ucs))
        return 0;
      return 1 + (ucs >= 4352 && (ucs <= 4447 || // Hangul Jamo init. consonants
      ucs == 9001 || ucs == 9002 || ucs >= 11904 && ucs <= 42191 && ucs != 12351 || // CJK ... Yi
      ucs >= 44032 && ucs <= 55203 || // Hangul Syllables
      ucs >= 63744 && ucs <= 64255 || // CJK Compatibility Ideographs
      ucs >= 65040 && ucs <= 65049 || // Vertical forms
      ucs >= 65072 && ucs <= 65135 || // CJK Compatibility Forms
      ucs >= 65280 && ucs <= 65376 || // Fullwidth Forms
      ucs >= 65504 && ucs <= 65510 || ucs >= 131072 && ucs <= 196605 || ucs >= 196608 && ucs <= 262141));
    }
    function wcswidth(str, opts) {
      let h;
      let l;
      let s = 0;
      let n;
      if (typeof str !== "string")
        return wcwidth2(str, opts);
      for (let i = 0; i < str.length; i++) {
        h = str.charCodeAt(i);
        if (h >= 55296 && h <= 56319) {
          l = str.charCodeAt(++i);
          if (l >= 56320 && l <= 57343) {
            h = (h - 55296) * 1024 + (l - 56320) + 65536;
          } else {
            i--;
          }
        }
        n = wcwidth2(h, opts);
        if (n < 0)
          return -1;
        s += n;
      }
      return s;
    }
    module.exports = (str) => wcswidth(str, DEFAULTS);
    module.exports.config = (opts = {}) => {
      opts = {
        ...DEFAULTS,
        ...opts
      };
      return (str) => wcswidth(str, opts);
    };
  }
});

// src/cli/index.js
import * as prettier2 from "../index.mjs";

// scripts/build/shims/at.js
var at = (isOptionalObject, object, index) => {
  if (isOptionalObject && (object === void 0 || object === null)) {
    return;
  }
  if (Array.isArray(object) || typeof object === "string") {
    return object[index < 0 ? object.length + index : index];
  }
  return object.at(index);
};
var at_default = at;

// src/cli/options/get-context-options.js
var import_dashify = __toESM(require_dashify(), 1);
import { getSupportInfo } from "../index.mjs";

// src/cli/cli-options.evaluate.js
var cli_options_evaluate_default = {
  "cache": {
    "default": false,
    "description": "Only format changed files. Cannot use with --stdin-filepath.",
    "type": "boolean"
  },
  "cacheLocation": {
    "description": "Path to the cache file.",
    "type": "path"
  },
  "cacheStrategy": {
    "choices": [
      {
        "description": "Use the file metadata such as timestamps as cache keys",
        "value": "metadata"
      },
      {
        "description": "Use the file content as cache keys",
        "value": "content"
      }
    ],
    "description": "Strategy for the cache to use for detecting changed files.",
    "type": "choice"
  },
  "check": {
    "alias": "c",
    "category": "Output",
    "description": "Check if the given files are formatted, print a human-friendly summary\nmessage and paths to unformatted files (see also --list-different).",
    "type": "boolean"
  },
  "color": {
    "default": true,
    "description": "Colorize error messages.",
    "oppositeDescription": "Do not colorize error messages.",
    "type": "boolean"
  },
  "config": {
    "category": "Config",
    "description": "Path to a Prettier configuration file (.prettierrc, package.json, prettier.config.js).",
    "exception": (value) => value === false,
    "oppositeDescription": "Do not look for a configuration file.",
    "type": "path"
  },
  "configPrecedence": {
    "category": "Config",
    "choices": [
      {
        "description": "CLI options take precedence over config file",
        "value": "cli-override"
      },
      {
        "description": "Config file take precedence over CLI options",
        "value": "file-override"
      },
      {
        "description": "If a config file is found will evaluate it and ignore other CLI options.\nIf no config file is found CLI options will evaluate as normal.",
        "value": "prefer-file"
      }
    ],
    "default": "cli-override",
    "description": "Define in which order config files and CLI options should be evaluated.",
    "type": "choice"
  },
  "debugBenchmark": {
    "type": "boolean"
  },
  "debugCheck": {
    "type": "boolean"
  },
  "debugPrintAst": {
    "type": "boolean"
  },
  "debugPrintComments": {
    "type": "boolean"
  },
  "debugPrintDoc": {
    "type": "boolean"
  },
  "debugRepeat": {
    "default": 0,
    "type": "int"
  },
  "editorconfig": {
    "category": "Config",
    "default": true,
    "description": "Take .editorconfig into account when parsing configuration.",
    "oppositeDescription": "Don't take .editorconfig into account when parsing configuration.",
    "type": "boolean"
  },
  "errorOnUnmatchedPattern": {
    "oppositeDescription": "Prevent errors when pattern is unmatched.",
    "type": "boolean"
  },
  "fileInfo": {
    "description": "Extract the following info (as JSON) for a given file path. Reported fields:\n* ignored (boolean) - true if file path is filtered by --ignore-path\n* inferredParser (string | null) - name of parser inferred from file path",
    "type": "path"
  },
  "findConfigPath": {
    "category": "Config",
    "description": "Find and print the path to a configuration file for the given input file.",
    "type": "path"
  },
  "help": {
    "alias": "h",
    "description": "Show CLI usage, or details about the given flag.\nExample: --help write",
    "exception": (value) => value === "",
    "type": "flag"
  },
  "ignorePath": {
    "array": true,
    "category": "Config",
    "default": [
      {
        "value": [
          ".gitignore",
          ".prettierignore"
        ]
      }
    ],
    "description": "Path to a file with patterns describing files to ignore.\nMultiple values are accepted.",
    "type": "path"
  },
  "ignoreUnknown": {
    "alias": "u",
    "description": "Ignore unknown files.",
    "type": "boolean"
  },
  "listDifferent": {
    "alias": "l",
    "category": "Output",
    "description": "Print the names of files that are different from Prettier's formatting (see also --check).",
    "type": "boolean"
  },
  "logLevel": {
    "choices": [
      "silent",
      "error",
      "warn",
      "log",
      "debug"
    ],
    "default": "log",
    "description": "What level of logs to report.",
    "type": "choice"
  },
  "supportInfo": {
    "description": "Print support information as JSON.",
    "type": "boolean"
  },
  "version": {
    "alias": "v",
    "description": "Print Prettier version.",
    "type": "boolean"
  },
  "withNodeModules": {
    "category": "Config",
    "description": "Process files inside 'node_modules' directory.",
    "type": "boolean"
  },
  "write": {
    "alias": "w",
    "category": "Output",
    "description": "Edit files in-place. (Beware!)",
    "type": "boolean"
  }
};

// src/cli/prettier-internal.js
import { __internal as sharedWithCli } from "../index.mjs";
var {
  errors,
  optionCategories,
  createIsIgnoredFunction,
  formatOptionsHiddenDefaults,
  normalizeOptions,
  getSupportInfoWithoutPlugins,
  normalizeOptionSettings,
  vnopts,
  fastGlob,
  mockable
} = sharedWithCli;

// src/cli/options/get-context-options.js
var detailedCliOptions = normalizeOptionSettings(cli_options_evaluate_default).map(
  (option) => normalizeDetailedOption(option)
);
function apiOptionToCliOption(apiOption) {
  const cliOption = {
    ...apiOption,
    description: apiOption.cliDescription ?? apiOption.description,
    category: apiOption.cliCategory ?? optionCategories.CATEGORY_FORMAT,
    forwardToApi: apiOption.name
  };
  if (apiOption.deprecated) {
    delete cliOption.forwardToApi;
    delete cliOption.description;
    delete cliOption.oppositeDescription;
    cliOption.deprecated = true;
  }
  return normalizeDetailedOption(cliOption);
}
function normalizeDetailedOption(option) {
  var _a;
  return {
    category: optionCategories.CATEGORY_OTHER,
    ...option,
    name: option.cliName ?? (0, import_dashify.default)(option.name),
    choices: (_a = option.choices) == null ? void 0 : _a.map((choice) => {
      const newChoice = {
        description: "",
        deprecated: false,
        ...typeof choice === "object" ? choice : { value: choice }
      };
      if (newChoice.value === true) {
        newChoice.value = "";
      }
      return newChoice;
    })
  };
}
function supportInfoToContextOptions({ options: supportOptions, languages }) {
  const detailedOptions = [
    ...detailedCliOptions,
    ...supportOptions.map((apiOption) => apiOptionToCliOption(apiOption))
  ];
  return {
    supportOptions,
    languages,
    detailedOptions
  };
}
async function getContextOptions(plugins) {
  const supportInfo = await getSupportInfo({
    showDeprecated: true,
    plugins
  });
  return supportInfoToContextOptions(supportInfo);
}
function getContextOptionsWithoutPlugins() {
  const supportInfo = getSupportInfoWithoutPlugins();
  return supportInfoToContextOptions(supportInfo);
}

// scripts/build/shims/string-replace-all.js
var stringReplaceAll = (isOptionalObject, original, pattern, replacement) => {
  if (isOptionalObject && (original === void 0 || original === null)) {
    return;
  }
  if (original.replaceAll) {
    return original.replaceAll(pattern, replacement);
  }
  if (pattern.global) {
    return original.replace(pattern, replacement);
  }
  return original.split(pattern).join(replacement);
};
var string_replace_all_default = stringReplaceAll;

// node_modules/camelcase/index.js
var UPPERCASE = /[\p{Lu}]/u;
var LOWERCASE = /[\p{Ll}]/u;
var LEADING_CAPITAL = /^[\p{Lu}](?![\p{Lu}])/gu;
var IDENTIFIER = /([\p{Alpha}\p{N}_]|$)/u;
var SEPARATORS = /[_.\- ]+/;
var LEADING_SEPARATORS = new RegExp("^" + SEPARATORS.source);
var SEPARATORS_AND_IDENTIFIER = new RegExp(SEPARATORS.source + IDENTIFIER.source, "gu");
var NUMBERS_AND_IDENTIFIER = new RegExp("\\d+" + IDENTIFIER.source, "gu");
var preserveCamelCase = (string, toLowerCase, toUpperCase, preserveConsecutiveUppercase2) => {
  let isLastCharLower = false;
  let isLastCharUpper = false;
  let isLastLastCharUpper = false;
  let isLastLastCharPreserved = false;
  for (let index = 0; index < string.length; index++) {
    const character = string[index];
    isLastLastCharPreserved = index > 2 ? string[index - 3] === "-" : true;
    if (isLastCharLower && UPPERCASE.test(character)) {
      string = string.slice(0, index) + "-" + string.slice(index);
      isLastCharLower = false;
      isLastLastCharUpper = isLastCharUpper;
      isLastCharUpper = true;
      index++;
    } else if (isLastCharUpper && isLastLastCharUpper && LOWERCASE.test(character) && (!isLastLastCharPreserved || preserveConsecutiveUppercase2)) {
      string = string.slice(0, index - 1) + "-" + string.slice(index - 1);
      isLastLastCharUpper = isLastCharUpper;
      isLastCharUpper = false;
      isLastCharLower = true;
    } else {
      isLastCharLower = toLowerCase(character) === character && toUpperCase(character) !== character;
      isLastLastCharUpper = isLastCharUpper;
      isLastCharUpper = toUpperCase(character) === character && toLowerCase(character) !== character;
    }
  }
  return string;
};
var preserveConsecutiveUppercase = (input, toLowerCase) => {
  LEADING_CAPITAL.lastIndex = 0;
  return string_replace_all_default(
    /* isOptionalObject*/
    false,
    input,
    LEADING_CAPITAL,
    (match) => toLowerCase(match)
  );
};
var postProcess = (input, toUpperCase) => {
  SEPARATORS_AND_IDENTIFIER.lastIndex = 0;
  NUMBERS_AND_IDENTIFIER.lastIndex = 0;
  return string_replace_all_default(
    /* isOptionalObject*/
    false,
    string_replace_all_default(
      /* isOptionalObject*/
      false,
      input,
      NUMBERS_AND_IDENTIFIER,
      (match, pattern, offset) => ["_", "-"].includes(input.charAt(offset + match.length)) ? match : toUpperCase(match)
    ),
    SEPARATORS_AND_IDENTIFIER,
    (_, identifier) => toUpperCase(identifier)
  );
};
function camelCase(input, options) {
  if (!(typeof input === "string" || Array.isArray(input))) {
    throw new TypeError("Expected the input to be `string | string[]`");
  }
  options = {
    pascalCase: false,
    preserveConsecutiveUppercase: false,
    ...options
  };
  if (Array.isArray(input)) {
    input = input.map((x) => x.trim()).filter((x) => x.length).join("-");
  } else {
    input = input.trim();
  }
  if (input.length === 0) {
    return "";
  }
  const toLowerCase = options.locale === false ? (string) => string.toLowerCase() : (string) => string.toLocaleLowerCase(options.locale);
  const toUpperCase = options.locale === false ? (string) => string.toUpperCase() : (string) => string.toLocaleUpperCase(options.locale);
  if (input.length === 1) {
    if (SEPARATORS.test(input)) {
      return "";
    }
    return options.pascalCase ? toUpperCase(input) : toLowerCase(input);
  }
  const hasUpperCase = input !== toLowerCase(input);
  if (hasUpperCase) {
    input = preserveCamelCase(input, toLowerCase, toUpperCase, options.preserveConsecutiveUppercase);
  }
  input = input.replace(LEADING_SEPARATORS, "");
  input = options.preserveConsecutiveUppercase ? preserveConsecutiveUppercase(input, toLowerCase) : toLowerCase(input);
  if (options.pascalCase) {
    input = toUpperCase(input.charAt(0)) + input.slice(1);
  }
  return postProcess(input, toUpperCase);
}

// src/cli/utils.js
import fs from "fs/promises";
import path from "path";

// node_modules/sdbm/index.js
function sdbm(string) {
  let hash = 0;
  for (let i = 0; i < string.length; i++) {
    hash = string.charCodeAt(i) + (hash << 6) + (hash << 16) - hash;
  }
  return hash >>> 0;
}

// src/cli/utils.js
import { __internal as sharedWithCli2 } from "../index.mjs";
var printToScreen = console.log.bind(console);
function groupBy(array2, iteratee) {
  const result = /* @__PURE__ */ Object.create(null);
  for (const value of array2) {
    const key = iteratee(value);
    if (Array.isArray(result[key])) {
      result[key].push(value);
    } else {
      result[key] = [value];
    }
  }
  return result;
}
function pick(object, keys) {
  const entries = keys.map((key) => [key, object[key]]);
  return Object.fromEntries(entries);
}
function createHash(source) {
  return String(sdbm(source));
}
async function statSafe(filePath) {
  try {
    return await fs.stat(filePath);
  } catch (error) {
    if (error.code !== "ENOENT") {
      throw error;
    }
  }
}
async function lstatSafe(filePath) {
  try {
    return await fs.lstat(filePath);
  } catch (error) {
    if (error.code !== "ENOENT") {
      throw error;
    }
  }
}
function isJson(value) {
  try {
    JSON.parse(value);
    return true;
  } catch {
    return false;
  }
}
var normalizeToPosix = path.sep === "\\" ? (filepath) => string_replace_all_default(
  /* isOptionalObject*/
  false,
  filepath,
  "\\",
  "/"
) : (filepath) => filepath;
var {
  isNonEmptyArray,
  partition,
  omit
} = sharedWithCli2.utils;

// src/cli/options/create-minimist-options.js
function createMinimistOptions(detailedOptions) {
  const booleanNames = [];
  const stringNames = [];
  const defaultValues = {};
  for (const option of detailedOptions) {
    const { name, alias, type } = option;
    const names = type === "boolean" ? booleanNames : stringNames;
    names.push(name);
    if (alias) {
      names.push(alias);
    }
    if (!option.deprecated && (!option.forwardToApi || name === "plugin") && option.default !== void 0) {
      defaultValues[option.name] = option.default;
    }
  }
  return {
    // we use vnopts' AliasSchema to handle aliases for better error messages
    alias: {},
    boolean: booleanNames,
    string: stringNames,
    default: defaultValues
  };
}

// src/cli/options/minimist.js
var import_minimist = __toESM(require_minimist(), 1);
var PLACEHOLDER = null;
function minimistParse(args, options) {
  const boolean = options.boolean ?? [];
  const defaults = options.default ?? {};
  const booleanWithoutDefault = boolean.filter((key) => !(key in defaults));
  const newDefaults = {
    ...defaults,
    ...Object.fromEntries(
      booleanWithoutDefault.map((key) => [key, PLACEHOLDER])
    )
  };
  const parsed = (0, import_minimist.default)(args, { ...options, default: newDefaults });
  return Object.fromEntries(
    Object.entries(parsed).filter(([, value]) => value !== PLACEHOLDER)
  );
}

// node_modules/chalk/source/vendor/ansi-styles/index.js
var ANSI_BACKGROUND_OFFSET = 10;
var wrapAnsi16 = (offset = 0) => (code) => `\x1B[${code + offset}m`;
var wrapAnsi256 = (offset = 0) => (code) => `\x1B[${38 + offset};5;${code}m`;
var wrapAnsi16m = (offset = 0) => (red, green, blue) => `\x1B[${38 + offset};2;${red};${green};${blue}m`;
var styles = {
  modifier: {
    reset: [0, 0],
    // 21 isn't widely supported and 22 does the same thing
    bold: [1, 22],
    dim: [2, 22],
    italic: [3, 23],
    underline: [4, 24],
    overline: [53, 55],
    inverse: [7, 27],
    hidden: [8, 28],
    strikethrough: [9, 29]
  },
  color: {
    black: [30, 39],
    red: [31, 39],
    green: [32, 39],
    yellow: [33, 39],
    blue: [34, 39],
    magenta: [35, 39],
    cyan: [36, 39],
    white: [37, 39],
    // Bright color
    blackBright: [90, 39],
    gray: [90, 39],
    // Alias of `blackBright`
    grey: [90, 39],
    // Alias of `blackBright`
    redBright: [91, 39],
    greenBright: [92, 39],
    yellowBright: [93, 39],
    blueBright: [94, 39],
    magentaBright: [95, 39],
    cyanBright: [96, 39],
    whiteBright: [97, 39]
  },
  bgColor: {
    bgBlack: [40, 49],
    bgRed: [41, 49],
    bgGreen: [42, 49],
    bgYellow: [43, 49],
    bgBlue: [44, 49],
    bgMagenta: [45, 49],
    bgCyan: [46, 49],
    bgWhite: [47, 49],
    // Bright color
    bgBlackBright: [100, 49],
    bgGray: [100, 49],
    // Alias of `bgBlackBright`
    bgGrey: [100, 49],
    // Alias of `bgBlackBright`
    bgRedBright: [101, 49],
    bgGreenBright: [102, 49],
    bgYellowBright: [103, 49],
    bgBlueBright: [104, 49],
    bgMagentaBright: [105, 49],
    bgCyanBright: [106, 49],
    bgWhiteBright: [107, 49]
  }
};
var modifierNames = Object.keys(styles.modifier);
var foregroundColorNames = Object.keys(styles.color);
var backgroundColorNames = Object.keys(styles.bgColor);
var colorNames = [...foregroundColorNames, ...backgroundColorNames];
function assembleStyles() {
  const codes = /* @__PURE__ */ new Map();
  for (const [groupName, group] of Object.entries(styles)) {
    for (const [styleName, style] of Object.entries(group)) {
      styles[styleName] = {
        open: `\x1B[${style[0]}m`,
        close: `\x1B[${style[1]}m`
      };
      group[styleName] = styles[styleName];
      codes.set(style[0], style[1]);
    }
    Object.defineProperty(styles, groupName, {
      value: group,
      enumerable: false
    });
  }
  Object.defineProperty(styles, "codes", {
    value: codes,
    enumerable: false
  });
  styles.color.close = "\x1B[39m";
  styles.bgColor.close = "\x1B[49m";
  styles.color.ansi = wrapAnsi16();
  styles.color.ansi256 = wrapAnsi256();
  styles.color.ansi16m = wrapAnsi16m();
  styles.bgColor.ansi = wrapAnsi16(ANSI_BACKGROUND_OFFSET);
  styles.bgColor.ansi256 = wrapAnsi256(ANSI_BACKGROUND_OFFSET);
  styles.bgColor.ansi16m = wrapAnsi16m(ANSI_BACKGROUND_OFFSET);
  Object.defineProperties(styles, {
    rgbToAnsi256: {
      value(red, green, blue) {
        if (red === green && green === blue) {
          if (red < 8) {
            return 16;
          }
          if (red > 248) {
            return 231;
          }
          return Math.round((red - 8) / 247 * 24) + 232;
        }
        return 16 + 36 * Math.round(red / 255 * 5) + 6 * Math.round(green / 255 * 5) + Math.round(blue / 255 * 5);
      },
      enumerable: false
    },
    hexToRgb: {
      value(hex) {
        const matches = /[a-f\d]{6}|[a-f\d]{3}/i.exec(hex.toString(16));
        if (!matches) {
          return [0, 0, 0];
        }
        let [colorString] = matches;
        if (colorString.length === 3) {
          colorString = [...colorString].map((character) => character + character).join("");
        }
        const integer = Number.parseInt(colorString, 16);
        return [
          /* eslint-disable no-bitwise */
          integer >> 16 & 255,
          integer >> 8 & 255,
          integer & 255
          /* eslint-enable no-bitwise */
        ];
      },
      enumerable: false
    },
    hexToAnsi256: {
      value: (hex) => styles.rgbToAnsi256(...styles.hexToRgb(hex)),
      enumerable: false
    },
    ansi256ToAnsi: {
      value(code) {
        if (code < 8) {
          return 30 + code;
        }
        if (code < 16) {
          return 90 + (code - 8);
        }
        let red;
        let green;
        let blue;
        if (code >= 232) {
          red = ((code - 232) * 10 + 8) / 255;
          green = red;
          blue = red;
        } else {
          code -= 16;
          const remainder = code % 36;
          red = Math.floor(code / 36) / 5;
          green = Math.floor(remainder / 6) / 5;
          blue = remainder % 6 / 5;
        }
        const value = Math.max(red, green, blue) * 2;
        if (value === 0) {
          return 30;
        }
        let result = 30 + (Math.round(blue) << 2 | Math.round(green) << 1 | Math.round(red));
        if (value === 2) {
          result += 60;
        }
        return result;
      },
      enumerable: false
    },
    rgbToAnsi: {
      value: (red, green, blue) => styles.ansi256ToAnsi(styles.rgbToAnsi256(red, green, blue)),
      enumerable: false
    },
    hexToAnsi: {
      value: (hex) => styles.ansi256ToAnsi(styles.hexToAnsi256(hex)),
      enumerable: false
    }
  });
  return styles;
}
var ansiStyles = assembleStyles();
var ansi_styles_default = ansiStyles;

// node_modules/chalk/source/vendor/supports-color/index.js
import process2 from "process";
import os from "os";
import tty from "tty";
function hasFlag(flag, argv = globalThis.Deno ? globalThis.Deno.args : process2.argv) {
  const prefix = flag.startsWith("-") ? "" : flag.length === 1 ? "-" : "--";
  const position = argv.indexOf(prefix + flag);
  const terminatorPosition = argv.indexOf("--");
  return position !== -1 && (terminatorPosition === -1 || position < terminatorPosition);
}
var { env } = process2;
var flagForceColor;
if (hasFlag("no-color") || hasFlag("no-colors") || hasFlag("color=false") || hasFlag("color=never")) {
  flagForceColor = 0;
} else if (hasFlag("color") || hasFlag("colors") || hasFlag("color=true") || hasFlag("color=always")) {
  flagForceColor = 1;
}
function envForceColor() {
  if ("FORCE_COLOR" in env) {
    if (env.FORCE_COLOR === "true") {
      return 1;
    }
    if (env.FORCE_COLOR === "false") {
      return 0;
    }
    return env.FORCE_COLOR.length === 0 ? 1 : Math.min(Number.parseInt(env.FORCE_COLOR, 10), 3);
  }
}
function translateLevel(level) {
  if (level === 0) {
    return false;
  }
  return {
    level,
    hasBasic: true,
    has256: level >= 2,
    has16m: level >= 3
  };
}
function _supportsColor(haveStream, { streamIsTTY, sniffFlags = true } = {}) {
  const noFlagForceColor = envForceColor();
  if (noFlagForceColor !== void 0) {
    flagForceColor = noFlagForceColor;
  }
  const forceColor = sniffFlags ? flagForceColor : noFlagForceColor;
  if (forceColor === 0) {
    return 0;
  }
  if (sniffFlags) {
    if (hasFlag("color=16m") || hasFlag("color=full") || hasFlag("color=truecolor")) {
      return 3;
    }
    if (hasFlag("color=256")) {
      return 2;
    }
  }
  if ("TF_BUILD" in env && "AGENT_NAME" in env) {
    return 1;
  }
  if (haveStream && !streamIsTTY && forceColor === void 0) {
    return 0;
  }
  const min = forceColor || 0;
  if (env.TERM === "dumb") {
    return min;
  }
  if (process2.platform === "win32") {
    const osRelease = os.release().split(".");
    if (Number(osRelease[0]) >= 10 && Number(osRelease[2]) >= 10586) {
      return Number(osRelease[2]) >= 14931 ? 3 : 2;
    }
    return 1;
  }
  if ("CI" in env) {
    if ("GITHUB_ACTIONS" in env || "GITEA_ACTIONS" in env) {
      return 3;
    }
    if (["TRAVIS", "CIRCLECI", "APPVEYOR", "GITLAB_CI", "BUILDKITE", "DRONE"].some((sign) => sign in env) || env.CI_NAME === "codeship") {
      return 1;
    }
    return min;
  }
  if ("TEAMCITY_VERSION" in env) {
    return /^(9\.(0*[1-9]\d*)\.|\d{2,}\.)/.test(env.TEAMCITY_VERSION) ? 1 : 0;
  }
  if (env.COLORTERM === "truecolor") {
    return 3;
  }
  if (env.TERM === "xterm-kitty") {
    return 3;
  }
  if ("TERM_PROGRAM" in env) {
    const version2 = Number.parseInt((env.TERM_PROGRAM_VERSION || "").split(".")[0], 10);
    switch (env.TERM_PROGRAM) {
      case "iTerm.app": {
        return version2 >= 3 ? 3 : 2;
      }
      case "Apple_Terminal": {
        return 2;
      }
    }
  }
  if (/-256(color)?$/i.test(env.TERM)) {
    return 2;
  }
  if (/^screen|^xterm|^vt100|^vt220|^rxvt|color|ansi|cygwin|linux/i.test(env.TERM)) {
    return 1;
  }
  if ("COLORTERM" in env) {
    return 1;
  }
  return min;
}
function createSupportsColor(stream, options = {}) {
  const level = _supportsColor(stream, {
    streamIsTTY: stream && stream.isTTY,
    ...options
  });
  return translateLevel(level);
}
var supportsColor = {
  stdout: createSupportsColor({ isTTY: tty.isatty(1) }),
  stderr: createSupportsColor({ isTTY: tty.isatty(2) })
};
var supports_color_default = supportsColor;

// node_modules/chalk/source/utilities.js
function stringReplaceAll2(string, substring, replacer) {
  let index = string.indexOf(substring);
  if (index === -1) {
    return string;
  }
  const substringLength = substring.length;
  let endIndex = 0;
  let returnValue = "";
  do {
    returnValue += string.slice(endIndex, index) + substring + replacer;
    endIndex = index + substringLength;
    index = string.indexOf(substring, endIndex);
  } while (index !== -1);
  returnValue += string.slice(endIndex);
  return returnValue;
}
function stringEncaseCRLFWithFirstIndex(string, prefix, postfix, index) {
  let endIndex = 0;
  let returnValue = "";
  do {
    const gotCR = string[index - 1] === "\r";
    returnValue += string.slice(endIndex, gotCR ? index - 1 : index) + prefix + (gotCR ? "\r\n" : "\n") + postfix;
    endIndex = index + 1;
    index = string.indexOf("\n", endIndex);
  } while (index !== -1);
  returnValue += string.slice(endIndex);
  return returnValue;
}

// node_modules/chalk/source/index.js
var { stdout: stdoutColor, stderr: stderrColor } = supports_color_default;
var GENERATOR = Symbol("GENERATOR");
var STYLER = Symbol("STYLER");
var IS_EMPTY = Symbol("IS_EMPTY");
var levelMapping = [
  "ansi",
  "ansi",
  "ansi256",
  "ansi16m"
];
var styles2 = /* @__PURE__ */ Object.create(null);
var applyOptions = (object, options = {}) => {
  if (options.level && !(Number.isInteger(options.level) && options.level >= 0 && options.level <= 3)) {
    throw new Error("The `level` option should be an integer from 0 to 3");
  }
  const colorLevel = stdoutColor ? stdoutColor.level : 0;
  object.level = options.level === void 0 ? colorLevel : options.level;
};
var chalkFactory = (options) => {
  const chalk2 = (...strings) => strings.join(" ");
  applyOptions(chalk2, options);
  Object.setPrototypeOf(chalk2, createChalk.prototype);
  return chalk2;
};
function createChalk(options) {
  return chalkFactory(options);
}
Object.setPrototypeOf(createChalk.prototype, Function.prototype);
for (const [styleName, style] of Object.entries(ansi_styles_default)) {
  styles2[styleName] = {
    get() {
      const builder = createBuilder(this, createStyler(style.open, style.close, this[STYLER]), this[IS_EMPTY]);
      Object.defineProperty(this, styleName, { value: builder });
      return builder;
    }
  };
}
styles2.visible = {
  get() {
    const builder = createBuilder(this, this[STYLER], true);
    Object.defineProperty(this, "visible", { value: builder });
    return builder;
  }
};
var getModelAnsi = (model, level, type, ...arguments_) => {
  if (model === "rgb") {
    if (level === "ansi16m") {
      return ansi_styles_default[type].ansi16m(...arguments_);
    }
    if (level === "ansi256") {
      return ansi_styles_default[type].ansi256(ansi_styles_default.rgbToAnsi256(...arguments_));
    }
    return ansi_styles_default[type].ansi(ansi_styles_default.rgbToAnsi(...arguments_));
  }
  if (model === "hex") {
    return getModelAnsi("rgb", level, type, ...ansi_styles_default.hexToRgb(...arguments_));
  }
  return ansi_styles_default[type][model](...arguments_);
};
var usedModels = ["rgb", "hex", "ansi256"];
for (const model of usedModels) {
  styles2[model] = {
    get() {
      const { level } = this;
      return function(...arguments_) {
        const styler = createStyler(getModelAnsi(model, levelMapping[level], "color", ...arguments_), ansi_styles_default.color.close, this[STYLER]);
        return createBuilder(this, styler, this[IS_EMPTY]);
      };
    }
  };
  const bgModel = "bg" + model[0].toUpperCase() + model.slice(1);
  styles2[bgModel] = {
    get() {
      const { level } = this;
      return function(...arguments_) {
        const styler = createStyler(getModelAnsi(model, levelMapping[level], "bgColor", ...arguments_), ansi_styles_default.bgColor.close, this[STYLER]);
        return createBuilder(this, styler, this[IS_EMPTY]);
      };
    }
  };
}
var proto = Object.defineProperties(() => {
}, {
  ...styles2,
  level: {
    enumerable: true,
    get() {
      return this[GENERATOR].level;
    },
    set(level) {
      this[GENERATOR].level = level;
    }
  }
});
var createStyler = (open, close, parent) => {
  let openAll;
  let closeAll;
  if (parent === void 0) {
    openAll = open;
    closeAll = close;
  } else {
    openAll = parent.openAll + open;
    closeAll = close + parent.closeAll;
  }
  return {
    open,
    close,
    openAll,
    closeAll,
    parent
  };
};
var createBuilder = (self, _styler, _isEmpty) => {
  const builder = (...arguments_) => applyStyle(builder, arguments_.length === 1 ? "" + arguments_[0] : arguments_.join(" "));
  Object.setPrototypeOf(builder, proto);
  builder[GENERATOR] = self;
  builder[STYLER] = _styler;
  builder[IS_EMPTY] = _isEmpty;
  return builder;
};
var applyStyle = (self, string) => {
  if (self.level <= 0 || !string) {
    return self[IS_EMPTY] ? "" : string;
  }
  let styler = self[STYLER];
  if (styler === void 0) {
    return string;
  }
  const { openAll, closeAll } = styler;
  if (string.includes("\x1B")) {
    while (styler !== void 0) {
      string = stringReplaceAll2(string, styler.close, styler.open);
      styler = styler.parent;
    }
  }
  const lfIndex = string.indexOf("\n");
  if (lfIndex !== -1) {
    string = stringEncaseCRLFWithFirstIndex(string, closeAll, openAll, lfIndex);
  }
  return openAll + string + closeAll;
};
Object.defineProperties(createChalk.prototype, styles2);
var chalk = createChalk();
var chalkStderr = createChalk({ level: stderrColor ? stderrColor.level : 0 });
var source_default = chalk;

// node_modules/leven/index.js
var array = [];
var characterCodeCache = [];
function leven(first, second) {
  if (first === second) {
    return 0;
  }
  const swap = first;
  if (first.length > second.length) {
    first = second;
    second = swap;
  }
  let firstLength = first.length;
  let secondLength = second.length;
  while (firstLength > 0 && first.charCodeAt(~-firstLength) === second.charCodeAt(~-secondLength)) {
    firstLength--;
    secondLength--;
  }
  let start = 0;
  while (start < firstLength && first.charCodeAt(start) === second.charCodeAt(start)) {
    start++;
  }
  firstLength -= start;
  secondLength -= start;
  if (firstLength === 0) {
    return secondLength;
  }
  let bCharacterCode;
  let result;
  let temporary;
  let temporary2;
  let index = 0;
  let index2 = 0;
  while (index < firstLength) {
    characterCodeCache[index] = first.charCodeAt(start + index);
    array[index] = ++index;
  }
  while (index2 < secondLength) {
    bCharacterCode = second.charCodeAt(start + index2);
    temporary = index2++;
    result = index2;
    for (index = 0; index < firstLength; index++) {
      temporary2 = bCharacterCode === characterCodeCache[index] ? temporary : temporary + 1;
      temporary = array[index];
      result = array[index] = temporary > result ? temporary2 > result ? result + 1 : temporary2 : temporary2 > temporary ? temporary + 1 : temporary2;
    }
  }
  return result;
}

// src/cli/options/normalize-cli-options.js
var descriptor = {
  key: (key) => key.length === 1 ? `-${key}` : `--${key}`,
  value: (value) => vnopts.apiDescriptor.value(value),
  pair: ({ key, value }) => value === false ? `--no-${key}` : value === true ? descriptor.key(key) : value === "" ? `${descriptor.key(key)} without an argument` : `${descriptor.key(key)}=${value}`
};
var _flags;
var FlagSchema = class extends vnopts.ChoiceSchema {
  constructor({ name, flags }) {
    super({ name, choices: flags });
    __privateAdd(this, _flags, []);
    __privateSet(this, _flags, [...flags].sort());
  }
  preprocess(value, utils) {
    if (typeof value === "string" && value.length > 0 && !__privateGet(this, _flags).includes(value)) {
      const suggestion = __privateGet(this, _flags).find((flag) => leven(flag, value) < 3);
      if (suggestion) {
        utils.logger.warn(
          [
            `Unknown flag ${source_default.yellow(utils.descriptor.value(value))},`,
            `did you mean ${source_default.blue(utils.descriptor.value(suggestion))}?`
          ].join(" ")
        );
        return suggestion;
      }
    }
    return value;
  }
  expected() {
    return "a flag";
  }
};
_flags = new WeakMap();
function normalizeCliOptions(options, optionInfos, opts) {
  return normalizeOptions(options, optionInfos, {
    ...opts,
    isCLI: true,
    FlagSchema,
    descriptor
  });
}
var normalize_cli_options_default = normalizeCliOptions;

// src/cli/options/parse-cli-arguments.js
function parseArgv(rawArguments, detailedOptions, logger, keys) {
  var _a;
  const minimistOptions = createMinimistOptions(detailedOptions);
  let argv = minimistParse(rawArguments, minimistOptions);
  if (keys) {
    detailedOptions = detailedOptions.filter(
      (option) => keys.includes(option.name)
    );
    argv = pick(argv, keys);
  }
  const normalized = normalize_cli_options_default(argv, detailedOptions, { logger });
  return {
    ...Object.fromEntries(
      Object.entries(normalized).map(([key, value]) => {
        const option = detailedOptions.find(({ name }) => name === key) || {};
        return [option.forwardToApi || camelCase(key), value];
      })
    ),
    _: (_a = normalized._) == null ? void 0 : _a.map(String),
    get __raw() {
      return argv;
    }
  };
}
var { detailedOptions: detailedOptionsWithoutPlugins } = getContextOptionsWithoutPlugins();
function parseArgvWithoutPlugins(rawArguments, logger, keys) {
  return parseArgv(
    rawArguments,
    detailedOptionsWithoutPlugins,
    logger,
    typeof keys === "string" ? [keys] : keys
  );
}

// src/cli/context.js
var _stack;
var Context = class {
  constructor({
    rawArguments,
    logger
  }) {
    __privateAdd(this, _stack, []);
    this.rawArguments = rawArguments;
    this.logger = logger;
  }
  async init() {
    const {
      rawArguments,
      logger
    } = this;
    const {
      plugins
    } = parseArgvWithoutPlugins(rawArguments, logger, ["plugin"]);
    await this.pushContextPlugins(plugins);
    const argv = parseArgv(rawArguments, this.detailedOptions, logger);
    this.argv = argv;
    this.filePatterns = argv._;
  }
  /**
   * @param {string[]} plugins
   */
  async pushContextPlugins(plugins) {
    const options = await getContextOptions(plugins);
    __privateGet(this, _stack).push(options);
    Object.assign(this, options);
  }
  popContextPlugins() {
    __privateGet(this, _stack).pop();
    Object.assign(this, at_default(
      /* isOptionalObject*/
      false,
      __privateGet(this, _stack),
      -1
    ));
  }
  // eslint-disable-next-line getter-return
  get performanceTestFlag() {
    const {
      debugBenchmark,
      debugRepeat
    } = this.argv;
    if (debugBenchmark) {
      return {
        name: "--debug-benchmark",
        debugBenchmark: true
      };
    }
    if (debugRepeat > 0) {
      return {
        name: "--debug-repeat",
        debugRepeat
      };
    }
    const {
      PRETTIER_PERF_REPEAT
    } = process.env;
    if (PRETTIER_PERF_REPEAT && /^\d+$/.test(PRETTIER_PERF_REPEAT)) {
      return {
        name: "PRETTIER_PERF_REPEAT (environment variable)",
        debugRepeat: Number(PRETTIER_PERF_REPEAT)
      };
    }
  }
};
_stack = new WeakMap();
var context_default = Context;

// src/cli/file-info.js
var import_fast_json_stable_stringify = __toESM(require_fast_json_stable_stringify(), 1);
import { format, getFileInfo } from "../index.mjs";
async function logFileInfoOrDie(context) {
  const {
    fileInfo: file,
    ignorePath,
    withNodeModules,
    plugins,
    config
  } = context.argv;
  const fileInfo = await getFileInfo(file, {
    ignorePath,
    withNodeModules,
    plugins,
    resolveConfig: config !== false
  });
  printToScreen(await format((0, import_fast_json_stable_stringify.default)(fileInfo), { parser: "json" }));
}
var file_info_default = logFileInfoOrDie;

// src/cli/find-config-path.js
import path2 from "path";
import { resolveConfigFile } from "../index.mjs";
async function logResolvedConfigPathOrDie(context) {
  const file = context.argv.findConfigPath;
  const configFile = await resolveConfigFile(file);
  if (configFile) {
    printToScreen(normalizeToPosix(path2.relative(process.cwd(), configFile)));
  } else {
    throw new Error(`Can not find configure file for "${file}".`);
  }
}
var find_config_path_default = logResolvedConfigPathOrDie;

// src/cli/format.js
import fs5 from "fs/promises";
import path9 from "path";
var import_diff = __toESM(require_create(), 1);
import * as prettier from "../index.mjs";

// src/cli/expand-patterns.js
import path3 from "path";
async function* expandPatterns(context) {
  const seen = /* @__PURE__ */ new Set();
  let noResults = true;
  for await (const {
    filePath,
    ignoreUnknown,
    error
  } of expandPatternsInternal(context)) {
    noResults = false;
    if (error) {
      yield {
        error
      };
      continue;
    }
    const filename = path3.resolve(filePath);
    if (seen.has(filename)) {
      continue;
    }
    seen.add(filename);
    yield {
      filename,
      ignoreUnknown
    };
  }
  if (noResults && context.argv.errorOnUnmatchedPattern !== false) {
    yield {
      error: `No matching files. Patterns: ${context.filePatterns.join(" ")}`
    };
  }
}
async function* expandPatternsInternal(context) {
  const silentlyIgnoredDirs = [".git", ".sl", ".svn", ".hg"];
  if (context.argv.withNodeModules !== true) {
    silentlyIgnoredDirs.push("node_modules");
  }
  const globOptions = {
    dot: true,
    ignore: silentlyIgnoredDirs.map((dir) => "**/" + dir),
    followSymbolicLinks: false
  };
  const cwd2 = process.cwd();
  const entries = [];
  for (const pattern of context.filePatterns) {
    const absolutePath = path3.resolve(cwd2, pattern);
    if (containsIgnoredPathSegment(absolutePath, cwd2, silentlyIgnoredDirs)) {
      continue;
    }
    const stat = await lstatSafe(absolutePath);
    if (stat) {
      if (stat.isSymbolicLink()) {
        if (context.argv.errorOnUnmatchedPattern !== false) {
          yield {
            error: `Explicitly specified pattern "${pattern}" is a symbolic link.`
          };
        } else {
          context.logger.debug(`Skipping pattern "${pattern}", as it is a symbolic link.`);
        }
      } else if (stat.isFile()) {
        entries.push({
          type: "file",
          glob: escapePathForGlob(fixWindowsSlashes(pattern)),
          input: pattern
        });
      } else if (stat.isDirectory()) {
        const relativePath = path3.relative(cwd2, absolutePath) || ".";
        const prefix = escapePathForGlob(fixWindowsSlashes(relativePath));
        entries.push({
          type: "dir",
          glob: `${prefix}/**/*`,
          input: pattern,
          ignoreUnknown: true
        });
      }
    } else if (pattern[0] === "!") {
      globOptions.ignore.push(fixWindowsSlashes(pattern.slice(1)));
    } else {
      entries.push({
        type: "glob",
        glob: fixWindowsSlashes(pattern),
        input: pattern
      });
    }
  }
  for (const {
    type,
    glob,
    input,
    ignoreUnknown
  } of entries) {
    let result;
    try {
      result = await fastGlob(glob, globOptions);
    } catch ({
      message
    }) {
      yield {
        error: `${errorMessages.globError[type]}: "${input}".
${message}`
      };
      continue;
    }
    if (result.length === 0) {
      if (context.argv.errorOnUnmatchedPattern !== false) {
        yield {
          error: `${errorMessages.emptyResults[type]}: "${input}".`
        };
      }
    } else {
      yield* sortPaths(result).map((filePath) => ({
        filePath,
        ignoreUnknown
      }));
    }
  }
}
var errorMessages = {
  globError: {
    file: "Unable to resolve file",
    dir: "Unable to expand directory",
    glob: "Unable to expand glob pattern"
  },
  emptyResults: {
    file: "Explicitly specified file was ignored due to negative glob patterns",
    dir: "No supported files were found in the directory",
    glob: "No files matching the pattern were found"
  }
};
function containsIgnoredPathSegment(absolutePath, cwd2, ignoredDirectories) {
  return path3.relative(cwd2, absolutePath).split(path3.sep).some((dir) => ignoredDirectories.includes(dir));
}
function sortPaths(paths) {
  return paths.sort((a, b) => a.localeCompare(b));
}
function escapePathForGlob(path10) {
  return string_replace_all_default(
    /* isOptionalObject*/
    false,
    string_replace_all_default(
      /* isOptionalObject*/
      false,
      fastGlob.escapePath(
        string_replace_all_default(
          /* isOptionalObject*/
          false,
          path10,
          "\\",
          "\0"
        )
        // Workaround for fast-glob#262 (part 1)
      ),
      "\\!",
      "@(!)"
    ),
    "\0",
    "@(\\\\)"
  );
}
var fixWindowsSlashes = normalizeToPosix;

// src/cli/find-cache-file.js
import fs4 from "fs/promises";
import os2 from "os";
import path8 from "path";

// node_modules/find-cache-dir/index.js
var import_common_path_prefix = __toESM(require_common_path_prefix(), 1);
import process4 from "process";
import path7 from "path";
import fs3 from "fs";

// node_modules/pkg-dir/index.js
import path6 from "path";

// node_modules/pkg-dir/node_modules/find-up/index.js
import path5 from "path";
import { fileURLToPath as fileURLToPath2 } from "url";

// node_modules/pkg-dir/node_modules/locate-path/index.js
import process3 from "process";
import path4 from "path";
import fs2, { promises as fsPromises } from "fs";
import { fileURLToPath } from "url";
var typeMappings = {
  directory: "isDirectory",
  file: "isFile"
};
function checkType(type) {
  if (Object.hasOwnProperty.call(typeMappings, type)) {
    return;
  }
  throw new Error(`Invalid type specified: ${type}`);
}
var matchType = (type, stat) => stat[typeMappings[type]]();
var toPath = (urlOrPath) => urlOrPath instanceof URL ? fileURLToPath(urlOrPath) : urlOrPath;
function locatePathSync(paths, {
  cwd: cwd2 = process3.cwd(),
  type = "file",
  allowSymlinks = true
} = {}) {
  checkType(type);
  cwd2 = toPath(cwd2);
  const statFunction = allowSymlinks ? fs2.statSync : fs2.lstatSync;
  for (const path_ of paths) {
    try {
      const stat = statFunction(path4.resolve(cwd2, path_), {
        throwIfNoEntry: false
      });
      if (!stat) {
        continue;
      }
      if (matchType(type, stat)) {
        return path_;
      }
    } catch {
    }
  }
}

// node_modules/pkg-dir/node_modules/find-up/index.js
var toPath2 = (urlOrPath) => urlOrPath instanceof URL ? fileURLToPath2(urlOrPath) : urlOrPath;
var findUpStop = Symbol("findUpStop");
function findUpMultipleSync(name, options = {}) {
  let directory = path5.resolve(toPath2(options.cwd) || "");
  const { root } = path5.parse(directory);
  const stopAt = options.stopAt || root;
  const limit = options.limit || Number.POSITIVE_INFINITY;
  const paths = [name].flat();
  const runMatcher = (locateOptions) => {
    if (typeof name !== "function") {
      return locatePathSync(paths, locateOptions);
    }
    const foundPath = name(locateOptions.cwd);
    if (typeof foundPath === "string") {
      return locatePathSync([foundPath], locateOptions);
    }
    return foundPath;
  };
  const matches = [];
  while (true) {
    const foundPath = runMatcher({ ...options, cwd: directory });
    if (foundPath === findUpStop) {
      break;
    }
    if (foundPath) {
      matches.push(path5.resolve(directory, foundPath));
    }
    if (directory === stopAt || matches.length >= limit) {
      break;
    }
    directory = path5.dirname(directory);
  }
  return matches;
}
function findUpSync(name, options = {}) {
  const matches = findUpMultipleSync(name, { ...options, limit: 1 });
  return matches[0];
}

// node_modules/pkg-dir/index.js
function packageDirectorySync({ cwd: cwd2 } = {}) {
  const filePath = findUpSync("package.json", { cwd: cwd2 });
  return filePath && path6.dirname(filePath);
}

// node_modules/find-cache-dir/index.js
var { env: env2, cwd } = process4;
var isWritable = (path10) => {
  try {
    fs3.accessSync(path10, fs3.constants.W_OK);
    return true;
  } catch {
    return false;
  }
};
function useDirectory(directory, options) {
  if (options.create) {
    fs3.mkdirSync(directory, { recursive: true });
  }
  return directory;
}
function getNodeModuleDirectory(directory) {
  const nodeModules = path7.join(directory, "node_modules");
  if (!isWritable(nodeModules) && (fs3.existsSync(nodeModules) || !isWritable(path7.join(directory)))) {
    return;
  }
  return nodeModules;
}
function findCacheDirectory(options = {}) {
  if (env2.CACHE_DIR && !["true", "false", "1", "0"].includes(env2.CACHE_DIR)) {
    return useDirectory(path7.join(env2.CACHE_DIR, options.name), options);
  }
  let { cwd: directory = cwd(), files } = options;
  if (files) {
    if (!Array.isArray(files)) {
      throw new TypeError(`Expected \`files\` option to be an array, got \`${typeof files}\`.`);
    }
    directory = (0, import_common_path_prefix.default)(files.map((file) => path7.resolve(directory, file)));
  }
  directory = packageDirectorySync({ cwd: directory });
  if (!directory) {
    return;
  }
  const nodeModules = getNodeModuleDirectory(directory);
  if (!nodeModules) {
    return;
  }
  return useDirectory(path7.join(directory, "node_modules", ".cache", options.name), options);
}

// src/cli/find-cache-file.js
function findDefaultCacheFile() {
  const cacheDir = findCacheDirectory({ name: "prettier", create: true }) || os2.tmpdir();
  const cacheFilePath = path8.join(cacheDir, ".prettier-cache");
  return cacheFilePath;
}
async function findCacheFileFromOption(cacheLocation) {
  const cacheFile = path8.resolve(cacheLocation);
  const stat = await statSafe(cacheFile);
  if (stat) {
    if (stat.isDirectory()) {
      throw new Error(
        `Resolved --cache-location '${cacheFile}' is a directory`
      );
    }
    const data = await fs4.readFile(cacheFile, "utf8");
    if (!isJson(data)) {
      throw new Error(`'${cacheFile}' isn't a valid JSON file`);
    }
  }
  return cacheFile;
}
async function findCacheFile(cacheLocation) {
  if (!cacheLocation) {
    return findDefaultCacheFile();
  }
  const cacheFile = await findCacheFileFromOption(cacheLocation);
  return cacheFile;
}
var find_cache_file_default = findCacheFile;

// src/cli/format-results-cache.js
var import_fast_json_stable_stringify2 = __toESM(require_fast_json_stable_stringify(), 1);
var import_file_entry_cache = __toESM(require_cache2(), 1);
import { version as prettierVersion } from "../index.mjs";
var optionsHashCache = /* @__PURE__ */ new WeakMap();
var nodeVersion = process.version;
function getHashOfOptions(options) {
  if (optionsHashCache.has(options)) {
    return optionsHashCache.get(options);
  }
  const hash = createHash(
    `${prettierVersion}_${nodeVersion}_${(0, import_fast_json_stable_stringify2.default)(options)}`
  );
  optionsHashCache.set(options, hash);
  return hash;
}
function getMetadataFromFileDescriptor(fileDescriptor) {
  return fileDescriptor.meta;
}
var _fileEntryCache;
var FormatResultsCache = class {
  /**
   * @param {string} cacheFileLocation The path of cache file location. (default: `node_modules/.cache/prettier/.prettier-cache`)
   * @param {string} cacheStrategy
   */
  constructor(cacheFileLocation, cacheStrategy) {
    __privateAdd(this, _fileEntryCache, void 0);
    const useChecksum = cacheStrategy === "content";
    __privateSet(this, _fileEntryCache, import_file_entry_cache.default.create(
      /* cacheId */
      cacheFileLocation,
      /* directory */
      void 0,
      useChecksum
    ));
  }
  /**
   * @param {string} filePath
   * @param {any} options
   */
  existsAvailableFormatResultsCache(filePath, options) {
    const fileDescriptor = __privateGet(this, _fileEntryCache).getFileDescriptor(filePath);
    if (fileDescriptor.notFound) {
      return false;
    }
    const hashOfOptions = getHashOfOptions(options);
    const meta = getMetadataFromFileDescriptor(fileDescriptor);
    const changed = fileDescriptor.changed || meta.hashOfOptions !== hashOfOptions;
    return !changed;
  }
  /**
   * @param {string} filePath
   * @param {any} options
   */
  setFormatResultsCache(filePath, options) {
    const fileDescriptor = __privateGet(this, _fileEntryCache).getFileDescriptor(filePath);
    const meta = getMetadataFromFileDescriptor(fileDescriptor);
    if (fileDescriptor && !fileDescriptor.notFound) {
      meta.hashOfOptions = getHashOfOptions(options);
    }
  }
  /**
   * @param {string} filePath
   */
  removeFormatResultsCache(filePath) {
    __privateGet(this, _fileEntryCache).removeEntry(filePath);
  }
  reconcile() {
    __privateGet(this, _fileEntryCache).reconcile();
  }
};
_fileEntryCache = new WeakMap();
var format_results_cache_default = FormatResultsCache;

// src/cli/is-tty.js
function isTTY() {
  return process.stdout.isTTY && !mockable.isCI();
}

// src/cli/options/get-options-for-file.js
var import_dashify2 = __toESM(require_dashify(), 1);
import { resolveConfig } from "../index.mjs";
function getOptions(argv, detailedOptions) {
  return Object.fromEntries(
    detailedOptions.filter(({ forwardToApi }) => forwardToApi).map(({ forwardToApi, name }) => [forwardToApi, argv[name]])
  );
}
function cliifyOptions(object, apiDetailedOptionMap) {
  return Object.fromEntries(
    Object.entries(object || {}).map(([key, value]) => {
      const apiOption = apiDetailedOptionMap[key];
      const cliKey = apiOption ? apiOption.name : key;
      return [(0, import_dashify2.default)(cliKey), value];
    })
  );
}
function createApiDetailedOptionMap(detailedOptions) {
  return Object.fromEntries(
    detailedOptions.filter(
      (option) => option.forwardToApi && option.forwardToApi !== option.name
    ).map((option) => [option.forwardToApi, option])
  );
}
function parseArgsToOptions(context, overrideDefaults) {
  const minimistOptions = createMinimistOptions(context.detailedOptions);
  const apiDetailedOptionMap = createApiDetailedOptionMap(
    context.detailedOptions
  );
  return getOptions(
    normalize_cli_options_default(
      minimistParse(context.rawArguments, {
        string: minimistOptions.string,
        boolean: minimistOptions.boolean,
        default: cliifyOptions(overrideDefaults, apiDetailedOptionMap)
      }),
      context.detailedOptions,
      { logger: false }
    ),
    context.detailedOptions
  );
}
async function getOptionsOrDie(context, filePath) {
  try {
    if (context.argv.config === false) {
      context.logger.debug(
        "'--no-config' option found, skip loading config file."
      );
      return null;
    }
    context.logger.debug(
      context.argv.config ? `load config file from '${context.argv.config}'` : `resolve config from '${filePath}'`
    );
    const options = await resolveConfig(filePath, {
      editorconfig: context.argv.editorconfig,
      config: context.argv.config
    });
    context.logger.debug("loaded options `" + JSON.stringify(options) + "`");
    return options;
  } catch (error) {
    context.logger.error(
      `Invalid configuration${filePath ? ` for file "${filePath}"` : ""}:
` + error.message
    );
    process.exit(2);
  }
}
function applyConfigPrecedence(context, options) {
  try {
    switch (context.argv.configPrecedence) {
      case "cli-override":
        return parseArgsToOptions(context, options);
      case "file-override":
        return { ...parseArgsToOptions(context), ...options };
      case "prefer-file":
        return options || parseArgsToOptions(context);
    }
  } catch (error) {
    context.logger.error(error.toString());
    process.exit(2);
  }
}
async function getOptionsForFile(context, filepath) {
  const options = await getOptionsOrDie(context, filepath);
  const hasPlugins = options == null ? void 0 : options.plugins;
  if (hasPlugins) {
    await context.pushContextPlugins(options.plugins);
  }
  const appliedOptions = {
    filepath,
    ...applyConfigPrecedence(
      context,
      options && normalizeOptions(options, context.supportOptions, {
        logger: context.logger
      })
    )
  };
  context.logger.debug(
    `applied config-precedence (${context.argv.configPrecedence}): ${JSON.stringify(appliedOptions)}`
  );
  if (hasPlugins) {
    context.popContextPlugins();
  }
  return appliedOptions;
}
var get_options_for_file_default = getOptionsForFile;

// src/cli/format.js
var { getStdin, writeFormattedFile } = mockable;
function diff(a, b) {
  return (0, import_diff.createTwoFilesPatch)("", "", a, b, "", "", { context: 2 });
}
var DebugError = class extends Error {
  name = "DebugError";
};
function handleError(context, filename, error, printedFilename, ignoreUnknown) {
  ignoreUnknown || (ignoreUnknown = context.argv.ignoreUnknown);
  const errorIsUndefinedParseError = error instanceof errors.UndefinedParserError;
  if (printedFilename) {
    if ((context.argv.write || ignoreUnknown) && errorIsUndefinedParseError) {
      printedFilename.clear();
    } else {
      process.stdout.write("\n");
    }
  }
  if (errorIsUndefinedParseError) {
    if (ignoreUnknown) {
      return;
    }
    if (!context.argv.check && !context.argv.listDifferent) {
      process.exitCode = 2;
    }
    context.logger.error(error.message);
    return;
  }
  const isParseError = Boolean(error == null ? void 0 : error.loc);
  const isValidationError = /^Invalid \S+ value\./.test(error == null ? void 0 : error.message);
  if (isParseError) {
    context.logger.error(`${filename}: ${String(error)}`);
  } else if (isValidationError || error instanceof errors.ConfigError) {
    context.logger.error(error.message);
    process.exit(1);
  } else if (error instanceof DebugError) {
    context.logger.error(`${filename}: ${error.message}`);
  } else {
    context.logger.error(filename + ": " + (error.stack || error));
  }
  process.exitCode = 2;
}
function writeOutput(context, result, options) {
  process.stdout.write(
    context.argv.debugCheck ? result.filepath : result.formatted
  );
  if (options && options.cursorOffset >= 0) {
    process.stderr.write(result.cursorOffset + "\n");
  }
}
async function listDifferent(context, input, options, filename) {
  if (!context.argv.check && !context.argv.listDifferent) {
    return;
  }
  try {
    if (!await prettier.check(input, options) && !context.argv.write) {
      context.logger.log(filename);
      process.exitCode = 1;
    }
  } catch (error) {
    context.logger.error(error.message);
  }
  return true;
}
async function format3(context, input, opt) {
  if (context.argv.debugPrintDoc) {
    const doc = await prettier.__debug.printToDoc(input, opt);
    return { formatted: await prettier.__debug.formatDoc(doc) + "\n" };
  }
  if (context.argv.debugPrintComments) {
    return {
      formatted: await prettier.format(
        JSON.stringify(
          (await prettier.formatWithCursor(input, opt)).comments || []
        ),
        { parser: "json" }
      )
    };
  }
  if (context.argv.debugPrintAst) {
    const { ast } = await prettier.__debug.parse(input, opt);
    return {
      formatted: JSON.stringify(ast)
    };
  }
  if (context.argv.debugCheck) {
    const pp = await prettier.format(input, opt);
    const pppp = await prettier.format(pp, opt);
    if (pp !== pppp) {
      throw new DebugError(
        "prettier(input) !== prettier(prettier(input))\n" + diff(pp, pppp)
      );
    } else {
      const stringify4 = (obj) => JSON.stringify(obj, null, 2);
      const ast = stringify4(
        (await prettier.__debug.parse(input, opt, { massage: true })).ast
      );
      const past = stringify4(
        (await prettier.__debug.parse(pp, opt, { massage: true })).ast
      );
      if (ast !== past) {
        const MAX_AST_SIZE = 2097152;
        const astDiff = ast.length > MAX_AST_SIZE || past.length > MAX_AST_SIZE ? "AST diff too large to render" : diff(ast, past);
        throw new DebugError(
          "ast(input) !== ast(prettier(input))\n" + astDiff + "\n" + diff(input, pp)
        );
      }
    }
    return { formatted: pp, filepath: opt.filepath || "(stdin)\n" };
  }
  const { performanceTestFlag } = context;
  if (performanceTestFlag == null ? void 0 : performanceTestFlag.debugBenchmark) {
    let benchmark;
    try {
      ({ default: benchmark } = await import("benchmark"));
    } catch {
      context.logger.debug(
        "'--debug-benchmark' requires the 'benchmark' package to be installed."
      );
      process.exit(2);
    }
    context.logger.debug(
      "'--debug-benchmark' option found, measuring formatWithCursor with 'benchmark' module."
    );
    const suite = new benchmark.Suite();
    suite.add("format", {
      defer: true,
      async fn(deferred) {
        await prettier.formatWithCursor(input, opt);
        deferred.resolve();
      }
    });
    const result = await new Promise((resolve) => {
      suite.on("complete", (event) => {
        resolve({
          benchmark: String(event.target),
          hz: event.target.hz,
          ms: event.target.times.cycle * 1e3
        });
      }).run({ async: false });
    });
    context.logger.debug(
      "'--debug-benchmark' measurements for formatWithCursor: " + JSON.stringify(result, null, 2)
    );
  } else if (performanceTestFlag == null ? void 0 : performanceTestFlag.debugRepeat) {
    const repeat = performanceTestFlag.debugRepeat;
    context.logger.debug(
      `'${performanceTestFlag.name}' found, running formatWithCursor ${repeat} times.`
    );
    let totalMs = 0;
    for (let i = 0; i < repeat; ++i) {
      const startMs = Date.now();
      await prettier.formatWithCursor(input, opt);
      totalMs += Date.now() - startMs;
    }
    const averageMs = totalMs / repeat;
    const results = {
      repeat,
      hz: 1e3 / averageMs,
      ms: averageMs
    };
    context.logger.debug(
      `'${performanceTestFlag.name}' measurements for formatWithCursor: ${JSON.stringify(
        results,
        null,
        2
      )}`
    );
  }
  return prettier.formatWithCursor(input, opt);
}
async function createIsIgnoredFromContextOrDie(context) {
  try {
    return await createIsIgnoredFunction(
      context.argv.ignorePath,
      context.argv.withNodeModules
    );
  } catch (e) {
    context.logger.error(e.message);
    process.exit(2);
  }
}
async function formatStdin(context) {
  const { filepath } = context.argv;
  try {
    const input = await getStdin();
    let isFileIgnored = false;
    if (filepath) {
      const isIgnored = await createIsIgnoredFromContextOrDie(context);
      isFileIgnored = isIgnored(filepath);
    }
    if (isFileIgnored) {
      writeOutput(context, { formatted: input });
      return;
    }
    const options = await get_options_for_file_default(
      context,
      filepath ? path9.resolve(filepath) : void 0
    );
    if (await listDifferent(context, input, options, "(stdin)")) {
      return;
    }
    const formatted = await format3(context, input, options);
    const { performanceTestFlag } = context;
    if (performanceTestFlag) {
      context.logger.log(
        `'${performanceTestFlag.name}' option found, skipped print code to screen.`
      );
      return;
    }
    writeOutput(context, formatted, options);
  } catch (error) {
    handleError(context, filepath || "stdin", error);
  }
}
async function formatFiles(context) {
  const isIgnored = await createIsIgnoredFromContextOrDie(context);
  const cwd2 = process.cwd();
  let numberOfUnformattedFilesFound = 0;
  const { performanceTestFlag } = context;
  if (context.argv.check && !performanceTestFlag) {
    context.logger.log("Checking formatting...");
  }
  let formatResultsCache;
  const cacheFilePath = await find_cache_file_default(context.argv.cacheLocation);
  if (context.argv.cache) {
    formatResultsCache = new format_results_cache_default(
      cacheFilePath,
      context.argv.cacheStrategy || "content"
    );
  } else if (!context.argv.cacheLocation) {
    const stat = await statSafe(cacheFilePath);
    if (stat) {
      await fs5.unlink(cacheFilePath);
    }
  }
  for await (const { error, filename, ignoreUnknown } of expandPatterns(
    context
  )) {
    if (error) {
      context.logger.error(error);
      process.exitCode = 2;
      continue;
    }
    const isFileIgnored = isIgnored(filename);
    if (isFileIgnored && (context.argv.debugCheck || context.argv.write || context.argv.check || context.argv.listDifferent)) {
      continue;
    }
    const options = {
      ...await get_options_for_file_default(context, filename),
      filepath: filename
    };
    const fileNameToDisplay = normalizeToPosix(path9.relative(cwd2, filename));
    let printedFilename;
    if (isTTY()) {
      printedFilename = context.logger.log(fileNameToDisplay, {
        newline: false,
        clearable: true
      });
    }
    let input;
    try {
      input = await fs5.readFile(filename, "utf8");
    } catch (error2) {
      context.logger.log("");
      context.logger.error(
        `Unable to read file "${fileNameToDisplay}":
${error2.message}`
      );
      process.exitCode = 2;
      continue;
    }
    if (isFileIgnored) {
      printedFilename == null ? void 0 : printedFilename.clear();
      writeOutput(context, { formatted: input }, options);
      continue;
    }
    const start = Date.now();
    const isCacheExists = formatResultsCache == null ? void 0 : formatResultsCache.existsAvailableFormatResultsCache(
      filename,
      options
    );
    let result;
    let output;
    try {
      if (isCacheExists) {
        result = { formatted: input };
      } else {
        result = await format3(context, input, options);
      }
      output = result.formatted;
    } catch (error2) {
      handleError(
        context,
        fileNameToDisplay,
        error2,
        printedFilename,
        ignoreUnknown
      );
      continue;
    }
    const isDifferent = output !== input;
    let shouldSetCache = !isDifferent;
    printedFilename == null ? void 0 : printedFilename.clear();
    if (performanceTestFlag) {
      context.logger.log(
        `'${performanceTestFlag.name}' option found, skipped print code or write files.`
      );
      return;
    }
    if (context.argv.write) {
      if (isDifferent) {
        if (!context.argv.check && !context.argv.listDifferent) {
          context.logger.log(`${fileNameToDisplay} ${Date.now() - start}ms`);
        }
        try {
          await writeFormattedFile(filename, output);
          shouldSetCache = true;
        } catch (error2) {
          context.logger.error(
            `Unable to write file "${fileNameToDisplay}":
${error2.message}`
          );
          process.exitCode = 2;
        }
      } else if (!context.argv.check && !context.argv.listDifferent) {
        const message = `${source_default.grey(fileNameToDisplay)} ${Date.now() - start}ms (unchanged)`;
        if (isCacheExists) {
          context.logger.log(`${message} (cached)`);
        } else {
          context.logger.log(message);
        }
      }
    } else if (context.argv.debugCheck) {
      if (result.filepath) {
        context.logger.log(fileNameToDisplay);
      } else {
        process.exitCode = 2;
      }
    } else if (!context.argv.check && !context.argv.listDifferent) {
      writeOutput(context, result, options);
    }
    if (shouldSetCache) {
      formatResultsCache == null ? void 0 : formatResultsCache.setFormatResultsCache(filename, options);
    } else {
      formatResultsCache == null ? void 0 : formatResultsCache.removeFormatResultsCache(filename);
    }
    if (isDifferent) {
      if (context.argv.check) {
        context.logger.warn(fileNameToDisplay);
      } else if (context.argv.listDifferent) {
        context.logger.log(fileNameToDisplay);
      }
      numberOfUnformattedFilesFound += 1;
    }
  }
  formatResultsCache == null ? void 0 : formatResultsCache.reconcile();
  if (context.argv.check) {
    if (numberOfUnformattedFilesFound === 0) {
      context.logger.log("All matched files use Prettier code style!");
    } else {
      const files = numberOfUnformattedFilesFound === 1 ? "the above file" : `${numberOfUnformattedFilesFound} files`;
      context.logger.warn(
        context.argv.write ? `Code style issues fixed in ${files}.` : `Code style issues found in ${files}. Run Prettier to fix.`
      );
    }
  }
  if ((context.argv.check || context.argv.listDifferent) && numberOfUnformattedFilesFound > 0 && !process.exitCode && !context.argv.write) {
    process.exitCode = 1;
  }
}

// src/cli/logger.js
import readline from "readline";

// node_modules/ansi-regex/index.js
function ansiRegex({ onlyFirst = false } = {}) {
  const pattern = [
    "[\\u001B\\u009B][[\\]()#;?]*(?:(?:(?:(?:;[-a-zA-Z\\d\\/#&.:=?%@~_]+)*|[a-zA-Z\\d]+(?:;[-a-zA-Z\\d\\/#&.:=?%@~_]*)*)?\\u0007)",
    "(?:(?:\\d{1,4}(?:;\\d{0,4})*)?[\\dA-PR-TZcf-ntqry=><~]))"
  ].join("|");
  return new RegExp(pattern, onlyFirst ? void 0 : "g");
}

// node_modules/strip-ansi/index.js
var regex = ansiRegex();
function stripAnsi(string) {
  if (typeof string !== "string") {
    throw new TypeError(`Expected a \`string\`, got \`${typeof string}\``);
  }
  return string.replace(regex, "");
}

// src/cli/logger.js
var import_wcwidth = __toESM(require_wcwidth(), 1);
var countLines = (stream, text) => {
  const columns = stream.columns || 80;
  let lineCount = 0;
  for (const line of stripAnsi(text).split("\n")) {
    lineCount += Math.max(1, Math.ceil((0, import_wcwidth.default)(line) / columns));
  }
  return lineCount;
};
var clear = (stream, text) => () => {
  const lineCount = countLines(stream, text);
  for (let line = 0; line < lineCount; line++) {
    if (line > 0) {
      readline.moveCursor(stream, 0, -1);
    }
    readline.clearLine(stream, 0);
    readline.cursorTo(stream, 0);
  }
};
var emptyLogResult = {
  clear() {
  }
};
function createLogger(logLevel = "log") {
  return {
    logLevel,
    warn: createLogFunc("warn", "yellow"),
    error: createLogFunc("error", "red"),
    debug: createLogFunc("debug", "blue"),
    log: createLogFunc("log")
  };
  function createLogFunc(loggerName, color) {
    if (!shouldLog(loggerName)) {
      return () => emptyLogResult;
    }
    const stream = process[loggerName === "log" ? "stdout" : "stderr"];
    const chalkInstance = loggerName === "log" ? source_default : chalkStderr;
    const prefix = color ? `[${chalkInstance[color](loggerName)}] ` : "";
    return (message, options) => {
      options = {
        newline: true,
        clearable: false,
        ...options
      };
      message = string_replace_all_default(
        /* isOptionalObject*/
        false,
        message,
        /^/gm,
        prefix
      ) + (options.newline ? "\n" : "");
      stream.write(message);
      if (options.clearable) {
        return {
          clear: clear(stream, message)
        };
      }
    };
  }
  function shouldLog(loggerName) {
    switch (logLevel) {
      case "silent":
        return false;
      case "debug":
        if (loggerName === "debug") {
          return true;
        }
      case "log":
        if (loggerName === "log") {
          return true;
        }
      case "warn":
        if (loggerName === "warn") {
          return true;
        }
      case "error":
        return loggerName === "error";
    }
  }
}
var logger_default = createLogger;

// src/cli/print-support-info.js
var import_fast_json_stable_stringify3 = __toESM(require_fast_json_stable_stringify(), 1);
import { format as format4, getSupportInfo as getSupportInfo2 } from "../index.mjs";
var sortByName = (array2) => array2.sort((a, b) => a.name.localeCompare(b.name));
async function printSupportInfo() {
  const { languages, options } = await getSupportInfo2();
  const supportInfo = {
    languages: sortByName(languages),
    options: sortByName(options).map(
      (option) => omit(option, ["cliName", "cliCategory", "cliDescription"])
    )
  };
  printToScreen(await format4((0, import_fast_json_stable_stringify3.default)(supportInfo), { parser: "json" }));
}
var print_support_info_default = printSupportInfo;

// src/cli/constants.evaluate.js
var categoryOrder = [
  "Output",
  "Format",
  "Config",
  "Editor",
  "Other"
];
var usageSummary = "Usage: prettier [options] [file/dir/glob ...]\n\nBy default, output is written to stdout.\nStdin is read if it is piped to Prettier and no files are given.";

// src/cli/usage.js
var OPTION_USAGE_THRESHOLD = 25;
var CHOICE_USAGE_MARGIN = 3;
var CHOICE_USAGE_INDENTATION = 2;
function indent(str, spaces) {
  return string_replace_all_default(
    /* isOptionalObject*/
    false,
    str,
    /^/gm,
    " ".repeat(spaces)
  );
}
function createDefaultValueDisplay(value) {
  return Array.isArray(value) ? `[${value.map(createDefaultValueDisplay).join(", ")}]` : value;
}
function getOptionDefaultValue(context, optionName) {
  var _a;
  const option = context.detailedOptions.find(({
    name
  }) => name === optionName);
  if ((option == null ? void 0 : option.default) !== void 0) {
    return option.default;
  }
  const optionCamelName = camelCase(optionName);
  return formatOptionsHiddenDefaults[optionCamelName] ?? ((_a = context.supportOptions.find((option2) => !option2.deprecated && option2.name === optionCamelName)) == null ? void 0 : _a.default);
}
function createOptionUsageHeader(option) {
  const name = `--${option.name}`;
  const alias = option.alias ? `-${option.alias},` : null;
  const type = createOptionUsageType(option);
  return [alias, name, type].filter(Boolean).join(" ");
}
function createOptionUsageRow(header, content, threshold) {
  const separator = header.length >= threshold ? `
${" ".repeat(threshold)}` : " ".repeat(threshold - header.length);
  const description = string_replace_all_default(
    /* isOptionalObject*/
    false,
    content,
    "\n",
    `
${" ".repeat(threshold)}`
  );
  return `${header}${separator}${description}`;
}
function createOptionUsageType(option) {
  switch (option.type) {
    case "boolean":
      return null;
    case "choice":
      return `<${option.choices.filter((choice) => !choice.deprecated).map((choice) => choice.value).join("|")}>`;
    default:
      return `<${option.type}>`;
  }
}
function createChoiceUsages(choices, margin, indentation) {
  const activeChoices = choices.filter((choice) => !choice.deprecated);
  const threshold = Math.max(0, ...activeChoices.map((choice) => choice.value.length)) + margin;
  return activeChoices.map((choice) => indent(createOptionUsageRow(choice.value, choice.description, threshold), indentation));
}
function createOptionUsage(context, option, threshold) {
  const header = createOptionUsageHeader(option);
  const optionDefaultValue = getOptionDefaultValue(context, option.name);
  return createOptionUsageRow(header, `${option.description}${optionDefaultValue === void 0 ? "" : `
Defaults to ${createDefaultValueDisplay(optionDefaultValue)}.`}`, threshold);
}
function getOptionsWithOpposites(options) {
  const optionsWithOpposites = options.map((option) => [option.description ? option : null, option.oppositeDescription ? {
    ...option,
    name: `no-${option.name}`,
    type: "boolean",
    description: option.oppositeDescription
  } : null]);
  return optionsWithOpposites.flat().filter(Boolean);
}
function createUsage(context) {
  const sortedOptions = context.detailedOptions.sort((optionA, optionB) => optionA.name.localeCompare(optionB.name));
  const options = getOptionsWithOpposites(sortedOptions).filter(
    // remove unnecessary option (e.g. `semi`, `color`, etc.), which is only used for --help <flag>
    (option) => !(option.type === "boolean" && option.oppositeDescription && !option.name.startsWith("no-"))
  );
  const groupedOptions = groupBy(options, (option) => option.category);
  const firstCategories = categoryOrder.slice(0, -1);
  const lastCategories = categoryOrder.slice(-1);
  const restCategories = Object.keys(groupedOptions).filter((category) => !categoryOrder.includes(category));
  const allCategories = [...firstCategories, ...restCategories, ...lastCategories];
  const optionsUsage = allCategories.map((category) => {
    const categoryOptions = groupedOptions[category].map((option) => createOptionUsage(context, option, OPTION_USAGE_THRESHOLD)).join("\n");
    return `${category} options:

${indent(categoryOptions, 2)}`;
  });
  return [usageSummary, ...optionsUsage, ""].join("\n\n");
}
function createPluginDefaults(pluginDefaults) {
  if (!pluginDefaults || Object.keys(pluginDefaults).length === 0) {
    return "";
  }
  const defaults = Object.entries(pluginDefaults).sort(([pluginNameA], [pluginNameB]) => pluginNameA.localeCompare(pluginNameB)).map(([plugin, value]) => `* ${plugin}: ${createDefaultValueDisplay(value)}`).join("\n");
  return `
Plugin defaults:
${defaults}`;
}
function createDetailedUsage(context, flag) {
  const option = getOptionsWithOpposites(context.detailedOptions).find((option2) => option2.name === flag || option2.alias === flag);
  const header = createOptionUsageHeader(option);
  const description = `

${indent(option.description, 2)}`;
  const choices = option.type !== "choice" ? "" : `

Valid options:

${createChoiceUsages(option.choices, CHOICE_USAGE_MARGIN, CHOICE_USAGE_INDENTATION).join("\n")}`;
  const optionDefaultValue = getOptionDefaultValue(context, option.name);
  const defaults = optionDefaultValue !== void 0 ? `

Default: ${createDefaultValueDisplay(optionDefaultValue)}` : "";
  const pluginDefaults = createPluginDefaults(option.pluginDefaults);
  return `${header}${description}${choices}${defaults}${pluginDefaults}`;
}

// src/cli/index.js
async function run(rawArguments = process.argv.slice(2)) {
  let logger = logger_default();
  try {
    const { logLevel } = parseArgvWithoutPlugins(
      rawArguments,
      logger,
      "log-level"
    );
    if (logLevel !== logger.logLevel) {
      logger = logger_default(logLevel);
    }
    const context = new context_default({ rawArguments, logger });
    await context.init();
    if (logger.logLevel !== "debug" && context.performanceTestFlag) {
      context.logger = logger_default("debug");
    }
    await main(context);
  } catch (error) {
    logger.error(error.message);
    process.exitCode = 1;
  }
}
async function main(context) {
  context.logger.debug(`normalized argv: ${JSON.stringify(context.argv)}`);
  if (context.argv.check && context.argv.listDifferent) {
    throw new Error("Cannot use --check and --list-different together.");
  }
  if (context.argv.write && context.argv.debugCheck) {
    throw new Error("Cannot use --write and --debug-check together.");
  }
  if (context.argv.findConfigPath && context.filePatterns.length > 0) {
    throw new Error("Cannot use --find-config-path with multiple files");
  }
  if (context.argv.fileInfo && context.filePatterns.length > 0) {
    throw new Error("Cannot use --file-info with multiple files");
  }
  if (!context.argv.cache && context.argv.cacheStrategy) {
    throw new Error("`--cache-strategy` cannot be used without `--cache`.");
  }
  if (context.argv.version) {
    printToScreen(prettier2.version);
    return;
  }
  if (context.argv.help !== void 0) {
    printToScreen(
      typeof context.argv.help === "string" && context.argv.help !== "" ? createDetailedUsage(context, context.argv.help) : createUsage(context)
    );
    return;
  }
  if (context.argv.supportInfo) {
    return print_support_info_default();
  }
  if (context.argv.findConfigPath) {
    await find_config_path_default(context);
    return;
  }
  if (context.argv.fileInfo) {
    await file_info_default(context);
    return;
  }
  const hasFilePatterns = context.filePatterns.length > 0;
  const useStdin = !hasFilePatterns && (!process.stdin.isTTY || context.argv.filepath);
  if (useStdin) {
    if (context.argv.cache) {
      throw new Error("`--cache` cannot be used when formatting stdin.");
    }
    await formatStdin(context);
    return;
  }
  if (hasFilePatterns) {
    await formatFiles(context);
    return;
  }
  process.exitCode = 1;
  printToScreen(createUsage(context));
}
export {
  run
};
