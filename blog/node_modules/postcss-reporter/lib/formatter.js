var pico = require('picocolors');
var path = require('path');
var firstBy = require('thenby');
var util = require('./util');

function createSortFunction(positionless, sortByPosition) {
  var positionValue = 0

  if (positionless === 'any') { positionValue = 1; }
  if (positionless === 'first') { positionValue = 2; }
  if (positionless === 'last') { positionValue = 0; }

  var sortFunction = firstBy((m) => {
    if (!m.line) return 1;
    return positionValue;
  })

  if (sortByPosition) {
    sortFunction = sortFunction.thenBy('line').thenBy('column');
  }

  return sortFunction;
}

module.exports = function (opts) {
  var options = opts || {};
  var sortByPosition =
    typeof options.sortByPosition !== 'undefined'
      ? options.sortByPosition
      : true;
  var positionless = options.positionless || 'first';

  var sortFunction = createSortFunction(positionless, sortByPosition);

  return function (input) {
    var messages = input.messages.filter(function (message) {
      return typeof message.text === 'string';
    });
    var source = input.source;

    if (!messages.length) return '';

    var orderedMessages = messages.sort(sortFunction);

    var output = '\n';

    if (source) {
      output += pico.bold(pico.underline(logFrom(source))) + '\n';
    }

    orderedMessages.forEach(function (w) {
      output += messageToString(w) + '\n';
    });

    return output;

    function messageToString(message) {
      var location = util.getLocation(message);
      var str = '';

      if (location.line) {
        str += pico.bold(location.line);
      }

      if (location.column) {
        str += pico.bold(':' + location.column);
      }

      if (location.line || location.column) {
        str += '\t';
      }

      if (!options.noIcon) {
        if (message.type === 'warning') {
          str += pico.yellow(util.warningSymbol + '  ');
        } else if (message.type === 'error') {
          str += pico.red(util.errorSymbol + '  ');
        }
      }

      str += message.text;
      if (!options.noPlugin) {
        str += pico.yellow(' [' + message.plugin + ']');
      }
      return str;
    }

    function logFrom(fromValue) {
      if (fromValue.charAt(0) === '<') return fromValue;
      return path.relative(process.cwd(), fromValue).split(path.sep).join('/');
    }
  };
};
