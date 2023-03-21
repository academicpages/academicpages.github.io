
/**
 * Module dependencies.
 */

var fs = require('fs');
var st = require('st');
var path = require('path');
var http = require('http');
var getUri = require('../');
var assert = require('assert');
var streamToArray = require('stream-to-array');

describe('get-uri', function () {

  describe('"http:" protocol', function () {

    var port;
    var cache;
    var server;

    before(function (done) {
      // setup target HTTP server
      server = http.createServer(st(__dirname));
      server.listen(function () {
        port = server.address().port;
        done();
      });
    });

    after(function (done) {
      server.once('close', function () { done(); });
      server.close();
    });

    it('should work for HTTP endpoints', function (done) {

      var uri = 'http://127.0.0.1:' + port + '/' + path.basename(__filename);
      fs.readFile(__filename, 'utf8', function (err, real) {
        if (err) return done(err);
        getUri(uri, function (err, rs) {
          if (err) return done(err);
          cache = rs;
          streamToArray(rs, function (err, array) {
            if (err) return done(err);
            var str = Buffer.concat(array).toString('utf8');
            assert.equal(str, real);
            done();
          });
        });
      });
    });

    it('should return ENOTFOUND for bad filenames', function (done) {
      var uri = 'http://127.0.0.1:' + port + '/does-not-exist';
      getUri(uri, function (err, rs) {
        assert(err);
        assert.equal('ENOTFOUND', err.code);
        done();
      });
    });

    it('should return ENOTMODIFIED for the same URI with `cache`', function (done) {
      var uri = 'http://127.0.0.1:' + port + '/' + path.basename(__filename);
      getUri(uri, { cache: cache }, function (err, rs) {
        assert(err);
        assert.equal('ENOTMODIFIED', err.code);
        done();
      });
    });

  });

});
