'use strict';

Object.defineProperty(exports, "__esModule", {
  value: true
});
exports.TypeName = undefined;
exports.parse = parse;
exports.toCodePoints = toCodePoints;

var _regex = require('./lib/regex');

var _regex2 = _interopRequireDefault(_regex);

function _interopRequireDefault(obj) { return obj && obj.__esModule ? obj : { default: obj }; }

var TypeName = exports.TypeName = 'emoji';
// Copyright Twitter Inc. Licensed under MIT
// https://github.com/twitter/twemoji-parser/blob/master/LICENSE.md
function parse(text, options) {
  var assetType = options && options.assetType ? options.assetType : 'svg';
  var getTwemojiUrl = options && options.buildUrl ? options.buildUrl : function (codepoints, assetType) {
    return assetType === 'png' ? 'https://twemoji.maxcdn.com/v/latest/72x72/' + codepoints + '.png' : 'https://twemoji.maxcdn.com/v/latest/svg/' + codepoints + '.svg';
  };

  var entities = [];

  _regex2.default.lastIndex = 0;
  while (true) {
    var result = _regex2.default.exec(text);
    if (!result) {
      break;
    }

    var emojiText = result[0];
    var codepoints = toCodePoints(removeVS16s(emojiText)).join('-');

    entities.push({
      url: codepoints ? getTwemojiUrl(codepoints, assetType) : '',
      indices: [result.index, _regex2.default.lastIndex],
      text: emojiText,
      type: TypeName
    });
  }
  return entities;
}

var vs16RegExp = /\uFE0F/g;
// avoid using a string literal like '\u200D' here because minifiers expand it inline
var zeroWidthJoiner = String.fromCharCode(0x200d);

var removeVS16s = function removeVS16s(rawEmoji) {
  return rawEmoji.indexOf(zeroWidthJoiner) < 0 ? rawEmoji.replace(vs16RegExp, '') : rawEmoji;
};

function toCodePoints(unicodeSurrogates) {
  var points = [];
  var char = 0;
  var previous = 0;
  var i = 0;
  while (i < unicodeSurrogates.length) {
    char = unicodeSurrogates.charCodeAt(i++);
    if (previous) {
      points.push((0x10000 + (previous - 0xd800 << 10) + (char - 0xdc00)).toString(16));
      previous = 0;
    } else if (char > 0xd800 && char <= 0xdbff) {
      previous = char;
    } else {
      points.push(char.toString(16));
    }
  }
  return points;
}