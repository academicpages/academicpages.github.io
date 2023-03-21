
/**
 * Module dependencies.
 */

var fs = require('fs');
var ftpd = require('ftpd');
var path = require('path');
var getUri = require('../');
var assert = require('assert');
var streamToArray = require('stream-to-array');

describe('get-uri', function () {

  describe('"ftp:" protocol', function () {

    var port;
    var cache;
    var server;

    before(function (done) {
      var options = {
        logLevel: -1,
        getInitialCwd: function (socket, fn) {
          fn(null, '/');
        },
        getRoot: function (socket) {
          return __dirname;
        }
      };

      var host = '127.0.0.1';
      server = new ftpd.FtpServer(host, options);

      server.on('client:connected', function(conn){
        var username;
        conn.on('command:user', function(user, success, failure) {
          username = user;
          success();
        });
        conn.on('command:pass', function(pass, success, failure){
          success(username);
        });
      });

      server.listen(0, function () {
        port = server.server.address().port;
        done();
      });
    });

    after(function (done) {
      server.server.once('close', function () {
        done();
      });
      server.server.close();
    });

    it('should work for ftp endpoints', function (done) {
      var uri = 'ftp://127.0.0.1:' + port + '/' + path.basename(__filename);
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
      var uri = 'ftp://127.0.0.1:' + port + '/does-not-exist';
      getUri(uri, function (err, rs) {
        assert(err);
        assert.equal('ENOTFOUND', err.code);
        done();
      });
    });

    it('should return ENOTMODIFIED for the same URI with `cache`', function (done) {
      var uri = 'ftp://127.0.0.1:' + port + '/' + path.basename(__filename);
      getUri(uri, { cache: cache }, function (err, rs) {
        assert(err);
        assert.equal('ENOTMODIFIED', err.code);
        done();
      });
    });

  });

});
