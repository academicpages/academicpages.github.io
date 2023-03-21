
/**
 * Module dependencies.
 */

var assert = require('assert');
var weekdayRange = require('../weekdayRange');
var vanillaGetUTCDay = Date.prototype.getUTCDay;
var vanillaGetDay = Date.prototype.getDay;

describe('hooks', function() {

  before(function() {
    Date.prototype.getDay    = function() { return 6; } // Setting local weekday as SAT(6)
    Date.prototype.getUTCDay = function() { return 5; } // Setting UTC weekday as FRI(5)
  });

  after(function() {
    Date.prototype.getUTCDay = vanillaGetUTCDay;
    Date.prototype.getDay    = vanillaGetDay;
  });

  describe('weekdayRange(wd1, wd2, gmt)', function () {

    var tests = [
      ["MON", "FRI", false],
      ["MON", "FRI", "GMT", true],
      ["SAT", true],
      ["SAT", "GMT", false],
      ["FRI", "MON", true],
      ["SAT", "MON", "GMT", false],
      ["SOME", "RANDOM", false],
      ["RANDOM", false],
      ["RANDOM", "VALUE", "IST", false],
    ];

    tests.forEach(function (test) {
      var expected = test.pop();
      it('should return `' + expected +'` for "' + test.join('", "') + '"', function () {
        assert.equal(expected, weekdayRange(test[0], test[1], test[2]));
      });
    });

  });
});
