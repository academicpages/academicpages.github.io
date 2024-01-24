var supportsLargeCharset =
  process.platform !== 'win32' ||
  process.env.CI ||
  process.env.TERM === 'xterm-256color';

exports.getLocation = function (message) {
  var messageNode = message.node;

  var location = {
    line: message.line,
    column: message.column,
  };

  var messageInput = messageNode && messageNode.source && messageNode.source.input;

  if (!messageInput) return location;

  var originLocation =
    messageInput.origin && messageInput.origin(message.line, message.column);
  if (originLocation) return originLocation;

  location.file = messageInput.file || messageInput.id;
  return location;
};

exports.plur = function plur(word, count) {
  return (count === 1 ? word : `${word}s`);
}

exports.warningSymbol = supportsLargeCharset ? '⚠' : '!!';
exports.errorSymbol = supportsLargeCharset ? '✖' : 'xx';
