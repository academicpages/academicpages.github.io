
/**
 * Module dependencies.
 */

var assert = require('assert');
var isPlainHostName = require('../isPlainHostName');

describe('isPlainHostName(host)', function () {

  var tests = [
   ["www", true],
   ["www.netscape.com", false]
  ];

  tests.forEach(function (test) {
    var expected = test.pop();
    it('should return `' + expected +'` for "' + test.join('", "') + '"', function () {
      assert.equal(expected, isPlainHostName(test[0]));
    });
  });

});
