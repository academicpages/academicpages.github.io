/**
 * Module dependencies.
 */

var fs = require('fs');
var url = require('url');
var http = require('http');
var https = require('https');
var assert = require('assert');
var getRawBody = require('raw-body');
var Proxy = require('proxy');
var socks = require('socksv5');
var PacProxyAgent = require('../');

describe('PacProxyAgent', function () {
  // target servers
  var httpServer, httpPort;
  var httpsServer, httpsPort;

  // proxy servers
  var socksServer, socksPort;
  var proxyServer, proxyPort;
  var proxyHttpsServer, proxyHttpsPort;

  before(function (done) {
    // setup target HTTP server
    httpServer = http.createServer();
    httpServer.listen(function () {
      httpPort = httpServer.address().port;
      done();
    });
  });

  before(function (done) {
    // setup target SSL HTTPS server
    var options = {
      key: fs.readFileSync(__dirname + '/ssl-cert-snakeoil.key'),
      cert: fs.readFileSync(__dirname + '/ssl-cert-snakeoil.pem')
    };
    httpsServer = https.createServer(options);
    httpsServer.listen(function () {
      httpsPort = httpsServer.address().port;
      done();
    });
  });

  before(function (done) {
    // setup SOCKS proxy server
    socksServer = socks.createServer(function(info, accept, deny) {
      accept();
    });
    socksServer.listen(function() {
      socksPort = socksServer.address().port;
      done();
    });
    socksServer.useAuth(socks.auth.None());
  });

  before(function (done) {
    // setup HTTP proxy server
    proxyServer = Proxy();
    proxyServer.listen(function () {
      proxyPort = proxyServer.address().port;
      done();
    });
  });

  before(function (done) {
    // setup SSL HTTPS proxy server
    var options = {
      key: fs.readFileSync(__dirname + '/ssl-cert-snakeoil.key'),
      cert: fs.readFileSync(__dirname + '/ssl-cert-snakeoil.pem')
    };
    proxyHttpsServer = Proxy(https.createServer(options));
    proxyHttpsServer.listen(function () {
      proxyHttpsPort = proxyHttpsServer.address().port;
      done();
    });
  });


  after(function (done) {
    //socksServer.once('close', function () { done(); });
    socksServer.close();
    done();
  });

  after(function (done) {
    //httpServer.once('close', function () { done(); });
    httpServer.close();
    done();
  });

  after(function (done) {
    //httpsServer.once('close', function () { done(); });
    httpsServer.close();
    done();
  });

  after(function (done) {
    //proxyServer.once('close', function () { done(); });
    proxyServer.close();
    done();
  });

  after(function (done) {
    //proxyHttpsServer.once('close', function () { done(); });
    proxyHttpsServer.close();
    done();
  });

  it('should allow a `sandbox` to be passed in', function (done) {
    this.slow(1000);

    function FindProxyForURL(url, host) {
      throw new Error(foo() + bar());
    }

    function foo () {
      return 'hi';
    }

    function asyncBar(fn) {
      setTimeout(function () {
        fn(null, 'fooooo');
      }, 200);
    }
    asyncBar.async = true;

    var uri = 'data:,' + encodeURIComponent(FindProxyForURL.toString());
    var agent = new PacProxyAgent(uri, {
      sandbox: {
        foo: foo,
        bar: asyncBar
      }
    });

    var opts = url.parse('http://localhost:' + httpPort + '/test');
    opts.agent = agent;

    var req = http.get(opts);
    req.once('error', function (err) {
      assert.equal(err.message, 'hifooooo');
      done();
    });
  });

  describe('constructor', function () {
    it('should throw an Error if no "proxy" argument is given', function () {
      assert.throws(function () {
        new PacProxyAgent();
      });
    });
    it('should accept a "string" proxy argument', function () {
      var agent = new PacProxyAgent('pac+ftp://example.com/proxy.pac');
      assert.equal('ftp://example.com/proxy.pac', agent.uri);
    });
    it('should accept a `url.parse()` result object argument', function () {
      var opts = url.parse('pac+ftp://example.com/proxy.pac');
      var agent = new PacProxyAgent(opts);
      assert.equal('ftp://example.com/proxy.pac', agent.uri);
    });
    it('should accept a `uri` on the options object', function () {
      var agent = new PacProxyAgent({ uri: 'pac+ftp://example.com/proxy.pac' });
      assert.equal('ftp://example.com/proxy.pac', agent.uri);
    });
  });

  describe('"http" module', function () {
    it('should work over an HTTP proxy', function (done) {
      httpServer.once('request', function (req, res) {
        res.end(JSON.stringify(req.headers));
      });

      function FindProxyForURL(url, host) {
        return "PROXY localhost:PORT;"
      }

      var uri = 'data:,' + encodeURIComponent(FindProxyForURL.toString().replace('PORT', proxyPort));
      var agent = new PacProxyAgent(uri);

      var opts = url.parse('http://localhost:' + httpPort + '/test');
      opts.agent = agent;

      var req = http.get(opts, function (res) {
        getRawBody(res, 'utf8', function (err, buf) {
          if (err) return done(err);
          var data = JSON.parse(buf);
          assert.equal('localhost:' + httpPort, data.host);
          assert('via' in data);
          done();
        });
      });
      req.once('error', done);
    });

    it('should work over an HTTPS proxy', function (done) {
      httpServer.once('request', function (req, res) {
        res.end(JSON.stringify(req.headers));
      });

      function FindProxyForURL(url, host) {
        return "HTTPS localhost:PORT;"
      }

      var uri = 'data:,' + encodeURIComponent(FindProxyForURL.toString().replace('PORT', proxyHttpsPort));
      var proxy = url.parse(uri);
      proxy.rejectUnauthorized = false;
      var agent = new PacProxyAgent(proxy);

      var opts = url.parse('http://localhost:' + httpPort + '/test');
      opts.agent = agent;

      var req = http.get(opts, function (res) {
        getRawBody(res, 'utf8', function (err, buf) {
          if (err) return done(err);
          var data = JSON.parse(buf);
          assert.equal('localhost:' + httpPort, data.host);
          assert('via' in data);
          done();
        });
      });
      req.once('error', done);
    });

    it('should work over a SOCKS proxy', function (done) {
      httpServer.once('request', function (req, res) {
        res.end(JSON.stringify(req.headers));
      });

      function FindProxyForURL(url, host) {
        return "SOCKS localhost:PORT;"
      }

      var uri = 'data:,' + encodeURIComponent(FindProxyForURL.toString().replace('PORT', socksPort));
      var agent = new PacProxyAgent(uri);

      var opts = url.parse('http://localhost:' + httpPort + '/test');
      opts.agent = agent;

      var req = http.get(opts, function (res) {
        getRawBody(res, 'utf8', function (err, buf) {
          if (err) return done(err);
          var data = JSON.parse(buf);
          assert.equal('localhost:' + httpPort, data.host);
          done();
        });
      });
      req.once('error', done);
    });

  });


  describe('"https" module', function () {
    it('should work over an HTTP proxy', function (done) {
      httpsServer.once('request', function (req, res) {
        res.end(JSON.stringify(req.headers));
      });

      function FindProxyForURL(url, host) {
        return "PROXY localhost:PORT;"
      }

      var uri = 'data:,' + encodeURIComponent(FindProxyForURL.toString().replace('PORT', proxyPort));
      var agent = new PacProxyAgent(uri);

      var opts = url.parse('https://localhost:' + httpsPort + '/test');
      opts.agent = agent;
      opts.rejectUnauthorized = false;

      var req = https.get(opts, function (res) {
        getRawBody(res, 'utf8', function (err, buf) {
          if (err) return done(err);
          var data = JSON.parse(buf);
          assert.equal('localhost:' + httpsPort, data.host);
          done();
        });
      });
      req.once('error', done);
    });

    it('should work over an HTTPS proxy', function (done) {
      var gotReq = false;
      httpsServer.once('request', function (req, res) {
        gotReq = true;
        res.end(JSON.stringify(req.headers));
      });

      function FindProxyForURL(url, host) {
        return "HTTPS localhost:PORT;"
      }

      var uri = 'data:,' + encodeURIComponent(FindProxyForURL.toString().replace('PORT', proxyHttpsPort));
      var agent = new PacProxyAgent(uri, {
        rejectUnauthorized: false
      });

      var opts = url.parse('https://localhost:' + httpsPort + '/test');
      opts.agent = agent;
      opts.rejectUnauthorized = false;

      var req = https.get(opts, function (res) {
        getRawBody(res, 'utf8', function (err, buf) {
          if (err) return done(err);
          var data = JSON.parse(buf);
          assert.equal('localhost:' + httpsPort, data.host);
          assert(gotReq);
          done();
        });
      });
      req.once('error', done);
    });

    it('should work over a SOCKS proxy', function (done) {
      var gotReq = false;
      httpsServer.once('request', function (req, res) {
        gotReq = true;
        res.end(JSON.stringify(req.headers));
      });

      function FindProxyForURL(url, host) {
        return "SOCKS localhost:PORT;"
      }

      var uri = 'data:,' + encodeURIComponent(FindProxyForURL.toString().replace('PORT', socksPort));
      var agent = new PacProxyAgent(uri);

      var opts = url.parse('https://localhost:' + httpsPort + '/test');
      opts.agent = agent;
      opts.rejectUnauthorized = false;

      var req = https.get(opts, function (res) {
        getRawBody(res, 'utf8', function (err, buf) {
          if (err) return done(err);
          var data = JSON.parse(buf);
          assert.equal('localhost:' + httpsPort, data.host);
          assert(gotReq);
          done();
        });
      });
      req.once('error', done);
    });
  });

});
