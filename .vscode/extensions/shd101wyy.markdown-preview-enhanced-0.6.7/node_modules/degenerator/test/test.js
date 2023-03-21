
/**
 * Module dependencies.
 */

var fs = require('fs');
var path = require('path');
var assert = require('assert');
var degenerator = require('../');

describe('degenerator()', function () {

  describe('"expected" fixture tests', function () {

    fs.readdirSync(__dirname).forEach(function (n) {
      if ('test.js' == n) return;
      if (/\.expected\.js$/.test(n)) return;
      var expectedName = path.basename(n, '.js') + '.expected.js';

      it(n + ' → ' + expectedName, function () {
        var sourceName = path.resolve(__dirname, n);
        var compiledName = path.resolve(__dirname, expectedName);
        var js = fs.readFileSync(sourceName, 'utf8');
        var expected = fs.readFileSync(compiledName, 'utf8');

        // the test case can define the `names` to use as a
        // comment on the first line of the file
        var names = js.match(/\/\/\s*(.*)/);
        if (names) {
          // the comment should be a comma-separated list of function names
          names = names[1].split(/,\s*/);
        } else {
          // if no function names were passed in then convert them all
          names = [ /.*/ ];
        }

        var compiled = degenerator(js, names);
        assert.equal(expected.trim(), compiled.trim());
      });
    });

  });

});
