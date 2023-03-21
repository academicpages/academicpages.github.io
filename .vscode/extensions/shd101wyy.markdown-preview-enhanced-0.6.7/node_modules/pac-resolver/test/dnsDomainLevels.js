
/**
 * Module dependencies.
 */

var assert = require('assert');
var dnsDomainLevels = require('../dnsDomainLevels');

describe('dnsDomainLevels(host)', function () {

  var tests = [
    ["www", 0],
    ["www.netscape", 1],
    ["www.netscape.com", 2]
  ];

  tests.forEach(function (test) {
    var expected = test.pop();
    it('should return `' + expected +'` for "' + test.join('", "') + '"', function () {
      assert.equal(expected, dnsDomainLevels(test[0]));
    });
  });

});
