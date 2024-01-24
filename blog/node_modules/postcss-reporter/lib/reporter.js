var defaultFormatter = require('./formatter');
var pico = require('picocolors');
var util = require('./util');

module.exports = function (opts = {}) {
  var formatter =
    opts.formatter ||
    defaultFormatter({
      noIcon: opts.noIcon,
      noPlugin: opts.noPlugin,
    });

  var pluginFilter;
  if (!opts.plugins) {
    // Every plugin
    pluginFilter = function () {
      return true;
    };
  } else if (
    opts.plugins.every(function (plugin) {
      return plugin[0] === '!';
    })
  ) {
    // Deny list
    pluginFilter = function (message) {
      return opts.plugins.indexOf('!' + message.plugin) === -1;
    };
  } else {
    // Allow list
    pluginFilter = function (message) {
      return opts.plugins.indexOf(message.plugin) !== -1;
    };
  }

  var messageFilter = opts.filter || ((message) => message.type === 'warning' || message.type === 'error');

  return {
    postcssPlugin: 'postcss-reporter',
    OnceExit(css, { result }) {
      var messagesToLog = result.messages
        .filter(pluginFilter)
        .filter(messageFilter);

      var resultSource = !result.root.source
        ? ''
        : result.root.source.input.file || result.root.source.input.id;

      let errorCount = 0;
      let warningCount = 0;

      var sourceGroupedMessages = messagesToLog.reduce((grouped, message) => {
        const key = util.getLocation(message).file || resultSource;

        if (!grouped.hasOwnProperty(key)) {
          grouped[key] = [];
        }

        if (message.type === 'error') {
          errorCount++;
        } else if (message.type === 'warning') {
          warningCount++;
        }

        grouped[key].push(message);

        return grouped;
      }, {});

      var report = '';
      for (const source in sourceGroupedMessages) {
        if (sourceGroupedMessages.hasOwnProperty(source)) {
          report += formatter({
            messages: sourceGroupedMessages[source],
            source: source,
          });
        }
      }

      if (opts.clearReportedMessages) {
        result.messages = result.messages.filter(message => !messagesToLog.includes(message));
      }

      if (opts.clearAllMessages) {
        var messagesToClear = result.messages.filter(pluginFilter);
        result.messages = result.messages.filter(message => !messagesToClear.includes(message));
      }

      if (!report) return;

      const summaryColor = errorCount > 0 ? 'red' : 'yellow';
      const summarySymbol = errorCount > 0 ? util.errorSymbol : util.warningSymbol;
      const summary = `${summarySymbol} ${messagesToLog.length} ${util.plur('problem', messagesToLog.length)} (${errorCount} ${util.plur('error')}, ${warningCount} ${util.plur('warning')})`

      report += `\n ${pico[summaryColor](pico.bold(summary))}\n`;

      console.log(report);

      if (shouldThrowError()) {
        throw new Error(
          pico.red(
            pico.bold('\n** postcss-reporter: warnings or errors were found **')
          )
        );
      }

      function shouldThrowError() {
        return opts.throwError || errorCount > 0;
      }
    },
  };
};
