
/**
 * Module dependencies.
 */

var assert = require('assert');
var isInNet = require('../isInNet');

describe('isInNet(host, pattern, mask)', function () {

  var tests = [
    ["198.95.249.79", "198.95.249.79", "255.255.255.255", true],
    ["198.95.249.78", "198.95.249.79", "255.255.255.255", false],
    ["198.95.1.1", "198.95.0.0", "255.255.0.0", true],
    ["198.94.1.1", "198.95.0.0", "255.255.0.0", false]
  ];

  tests.forEach(function (test) {
    var expected = test.pop();
    it('should return `' + expected +'` for "' + test.join('", "') + '"', function (done) {
      isInNet(test[0], test[1], test[2], function (err, res) {
        if (err) return done(err);
        assert.equal(expected, res);
        done();
      });
    });
  });

});
