
/**
 * Module dependencies.
 */

var fs = require('fs');
var st = require('st');
var path = require('path');
var http = require('http');
var https = require('https');
var getUri = require('../');
var assert = require('assert');
var streamToArray = require('stream-to-array');

describe('get-uri', function () {

  describe('http/https redirects', function () {

    var httpServer;
    var httpsServer;
    var httpPort;
    var httpsPort;

    before(function(done) {
      httpServer = http.createServer();
      httpServer.listen(function() {
        httpPort = httpServer.address().port;
        done();
      });
    });

    before(function(done) {
      var options = {
        key: fs.readFileSync(__dirname + '/server.key'),
        cert: fs.readFileSync(__dirname + '/server.crt')
      };
      httpsServer = https.createServer(options);
      httpsServer.listen(function() {
        httpsPort = httpsServer.address().port;
        done();
      });
    });

    after(function (done) {
      httpsServer.once('close', function () {
        done();
      });
      httpsServer.close();
    });

    after(function (done) {
      httpServer.once('close', function () {
        done();
      });
      httpServer.close();
    });

    it('should handle http -> https redirect', function (done) {
      httpsServer.once('request', st(__dirname));
      httpServer.once('request', function(req, res) {
        res.writeHead(301, {'Location': 'https://127.0.0.1:' + httpsPort + '/' + path.basename(__filename)});
        res.end('Moved');
      });
      var uri = 'http://127.0.0.1:' + httpPort + '/' + path.basename(__filename);
      fs.readFile(__filename, 'utf8', function (err, real) {
        if (err) return done(err);
        getUri(uri, { rejectUnauthorized: false }, function (err, rs) {
          if (err) return done(err);
          streamToArray(rs, function (err, array) {
            if (err) return done(err);
            var str = Buffer.concat(array).toString('utf8');
            assert.equal(str, real);
            done();
          });
        });
      });
    });

    it('should handle https -> http redirect', function (done) {
      httpServer.once('request', st(__dirname));
      httpsServer.once('request', function(req, res) {
        res.writeHead(301, {'Location': 'http://127.0.0.1:' + httpPort + '/' + path.basename(__filename)});
        res.end('Moved');
      });

      var uri = 'http://127.0.0.1:' + httpPort + '/' + path.basename(__filename);
      fs.readFile(__filename, 'utf8', function (err, real) {
        if (err) return done(err);
        getUri(uri, function (err, rs) {
          if (err) return done(err);
          streamToArray(rs, function (err, array) {
            if (err) return done(err);
            var str = Buffer.concat(array).toString('utf8');
            assert.equal(str, real);
            done();
          });
        });
      });
    });

  });

});
