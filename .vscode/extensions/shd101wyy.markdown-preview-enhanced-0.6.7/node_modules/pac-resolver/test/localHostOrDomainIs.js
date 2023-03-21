
/**
 * Module dependencies.
 */

var assert = require('assert');
var localHostOrDomainIs = require('../localHostOrDomainIs');

describe('localHostOrDomainIs(host, hostdom)', function () {

  var tests = [
   ["www.netscape.com", "www.netscape.com", true],
   ["www", "www.netscape.com", true],
   ["www.mcom.com", "www.netscape.com", false],
   ["home.netscape.com", "www.netscape.com", false]
  ];

  tests.forEach(function (test) {
    var expected = test.pop();
    it('should return `' + expected +'` for "' + test.join('", "') + '"', function () {
      assert.equal(expected, localHostOrDomainIs(test[0], test[1]));
    });
  });

});
