
/**
 * Module dependencies.
 */

var isIP = require('net').isIP;
var assert = require('assert');
var dnsResolve = require('../dnsResolve');

describe('dnsResolve(host)', function () {

  var tests = [
   ["www.netscape.com", true],
   ["bogus.domain.foobar", false]
  ];

  tests.forEach(function (test) {
    var expected = test.pop();
    if (expected) {
      it('should resolve an IPv4 address for "' + test.join('", "') + '"', function (done) {
        dnsResolve(test[0], function (err, res) {
          if (err) return done(err);
          assert.equal('string', typeof res);
          assert.equal(4, isIP(res));
          done();
        });
      });
    } else {
      it('should throw a not found Error for "' + test.join('", "') + '"', function (done) {
        dnsResolve(test[0], function (err, res) {
          assert(err);
          done();
        });
      });
    }
  });

});
