
/**
 * Module dependencies.
 */

var isIP = require('net').isIP;
var assert = require('assert');
var myIpAddress = require('../myIpAddress');

describe('myIpAddress()', function () {

  it('should return an IPv4 address', function (done) {
    myIpAddress(function (err, ip) {
      if (err) return done(err);
      assert.equal(4, isIP(ip));
      done();
    });
  });

});
