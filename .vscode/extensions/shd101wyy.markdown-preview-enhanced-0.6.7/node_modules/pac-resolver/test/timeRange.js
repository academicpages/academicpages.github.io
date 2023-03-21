
/**
 * Module dependencies.
 */

var assert = require('assert');
var timeRange = require('../timeRange');
var vanillaGetHours = Date.prototype.getHours;
var vanillaGetMinutes = Date.prototype.getMinutes;
var vanillaGetSeconds = Date.prototype.getSeconds;
var vanillaGetUTCHours = Date.prototype.getUTCHours;
var vanillaGetUTCMinutes = Date.prototype.getUTCMinutes;
var vanillaGetUTCSeconds = Date.prototype.getUTCSeconds;

describe('hooks', function() {

  before(function() {
    // Setting local time as 01:24:30
    Date.prototype.getHours = function() { return 1; }
    Date.prototype.getMinutes = function() { return 24; }
    Date.prototype.getSeconds = function() { return 30; }

    // Setting UTC time as 19:54:30
    Date.prototype.getUTCHours = function() { return 19; }
    Date.prototype.getUTCMinutes = function() { return 54; }
    Date.prototype.getUTCSeconds = function() { return 30; }
  });

  after(function() {
    Date.prototype.getHours = vanillaGetHours;
    Date.prototype.getUTCHours = vanillaGetUTCHours;
    Date.prototype.getUTCMinutes = vanillaGetUTCMinutes;
    Date.prototype.getUTCSeconds = vanillaGetUTCSeconds;
  });


  describe('timeRange()', function () {


    var tests = [
      [1, true],
      [1, 2, true],
      [0, 0, 0, 30, false],
      [0, 0, 0, 0, 30, 0, false],
      [0, 0, 0, 0, 30, 0, 'GMT', false],
      [0, 0, 0, 20, 0, 0, 'GMT', true],
    ];

    tests.forEach(function (test) {
      var expected = test.pop();
      it('should return `' + expected +'` for "' + test.join('", "') + '"', function () {
        assert.equal(expected, timeRange.apply(this, test));
      });
    });

  });
});
