
/**
 * Module dependencies.
 */

var url = require('url');
var http = require('http');
var https = require('https');
var extend = require('extend');
var NotFoundError = require('./notfound');
var NotModifiedError = require('./notmodified');
var debug = require('debug')('get-uri:http');

/**
 * Module exports.
 */

module.exports = get;

/**
 * Returns a Readable stream from an "http:" URI.
 *
 * @api protected
 */

function get (parsed, opts, fn) {
  debug('GET %o', parsed.href);

  var cache = getCache(parsed, opts.cache);

  // 5 redirects allowed by default
  var maxRedirects = opts.hasOwnProperty('maxRedirects') ? opts.maxRedirects : 5;
  debug('allowing %o max redirects', maxRedirects);

  // first check the previous Expires and/or Cache-Control headers
  // of a previous response if a `cache` was provided
  if (cache && isFresh(cache)) {

    // check for a 3xx "redirect" status code on the previous cache
    var location = cache.headers.location;
    var type = (cache.statusCode / 100 | 0);
    if (3 == type && location) {
      debug('cached redirect');
      fn(new Error('TODO: implement cached redirects!'));
    } else {
      // otherwise we assume that it's the destination endpoint,
      // since there's nowhere else to redirect to
      fn(new NotModifiedError());
    }
    return;
  }

  var mod;
  if (opts.http) {
    // the `https` module passed in from the "http.js" file
    mod = opts.http;
    debug('using secure `https` core module');
  } else {
    mod = http;
    debug('using `http` core module');
  }

  var options = extend({}, opts, parsed);

  // add "cache validation" headers if a `cache` was provided
  if (cache) {
    if (!options.headers) options.headers = {};

    var lastModified = cache.headers['last-modified'];
    if (lastModified != null) {
      options.headers['If-Modified-Since'] = lastModified;
      debug('added "If-Modified-Since" request header: %o', lastModified);
    }

    var etag = cache.headers.etag;
    if (etag != null) {
      options.headers['If-None-Match'] = etag;
      debug('added "If-None-Match" request header: %o', etag);
    }
  }

  var req = mod.get(options);
  req.once('error', onerror);
  req.once('response', onresponse);

  // http.ClientRequest "error" event handler
  function onerror (err) {
    debug('http.ClientRequest "error" event: %o', err.stack || err);
    fn(err);
  }

  // http.ClientRequest "response" event handler
  function onresponse (res) {
    var code = res.statusCode;

    // assign a Date to this response for the "Cache-Control" delta calculation
    res.date = new Date();
    res.parsed = parsed;

    debug('got %o response status code', code);

    // any 2xx response is a "success" code
    var type = (code / 100 | 0);

    // check for a 3xx "redirect" status code
    var location = res.headers.location;
    if (3 == type && location) {
      if (!opts.redirects) opts.redirects = [];
      var redirects = opts.redirects;

      if (redirects.length < maxRedirects) {
        debug('got a "redirect" status code with Location: %o', location);

        // flush this response - we're not going to use it
        res.resume();

        // hang on to this Response object for the "redirects" Array
        redirects.push(res);

        var newUri = url.resolve(parsed, location);
        debug('resolved redirect URL: %o', newUri);

        var left = maxRedirects - redirects.length;
        debug('%o more redirects allowed after this one', left);

        // check if redirecting to a different protocol
        var parsedUrl = url.parse(newUri);
        if (parsedUrl.protocol !== parsed.protocol) {
          opts.http = parsedUrl.protocol === 'https:' ? https : undefined;
        }

        return get(parsedUrl, opts, fn);
      }
    }

    // if we didn't get a 2xx "success" status code, then create an Error object
    if (2 != type) {
      var err;
      if (304 == code) {
        err = new NotModifiedError();
      } else if (404 == code) {
        err = new NotFoundError();
      } else {
        // other HTTP-level error
        var message = http.STATUS_CODES[code];
        err = new Error(message);
        err.statusCode = code;
        err.code = code;
      }

      res.resume();
      return fn(err);
    }

    if (opts.redirects) {
      // store a reference to the "redirects" Array on the Response object so that
      // they can be inspected during a subsequent call to GET the same URI
      res.redirects = opts.redirects;
    }

    fn(null, res);
  }
}

/**
 * Returns `true` if the provided cache's "freshness" is valid. That is, either
 * the Cache-Control header or Expires header values are still within the allowed
 * time period.
 *
 * @return {Boolean}
 * @api private
 */

function isFresh (cache) {
  var cacheControl = cache.headers['cache-control'];
  var expires = cache.headers.expires;
  var fresh;

  if (cacheControl) {
    // for Cache-Control rules, see: http://www.mnot.net/cache_docs/#CACHE-CONTROL
    debug('Cache-Control: %o', cacheControl);

    var parts = cacheControl.split(/,\s*?\b/);
    for (var i = 0; i < parts.length; i++) {
      var part = parts[i];
      var subparts = part.split('=');
      var name = subparts[0];
      switch (name) {
        case 'max-age':
          var val = +subparts[1];
          expires = new Date(+cache.date + (val * 1000));
          fresh = new Date() < expires;
          if (fresh) debug('cache is "fresh" due to previous %o Cache-Control param', part);
          return fresh;
        case 'must-revalidate':
          // XXX: what we supposed to do here?
          break;
        case 'no-cache':
        case 'no-store':
          debug('cache is "stale" due to explicit %o Cache-Control param', name);
          return false;
      }
    }

  } else if (expires) {
    // for Expires rules, see: http://www.mnot.net/cache_docs/#EXPIRES
    debug('Expires: %o', expires);

    fresh = new Date() < new Date(expires);
    if (fresh) debug('cache is "fresh" due to previous Expires response header');
    return fresh;
  }

  return false;
}

/**
 * Attempts to return a previous Response object from a previous GET call to the
 * same URI.
 *
 * @api private
 */

function getCache (parsed, cache) {
  if (!cache) return;
  var href = parsed.href;
  if (cache.parsed.href == href) {
    return cache;
  }
  var redirects = cache.redirects;
  if (redirects) {
    for (var i = 0; i < redirects.length; i++) {
      var c = getCache(parsed, redirects[i]);
      if (c) return c;
    }
  }
}
