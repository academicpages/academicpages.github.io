
/**
 * Module dependencies.
 */

var FTP = require('ftp');
var path = require('path');
var NotFoundError = require('./notfound');
var NotModifiedError = require('./notmodified');
var debug = require('debug')('get-uri:ftp');

/**
 * Module exports.
 */

module.exports = get;

/**
 * Returns a Readable stream from an "ftp:" URI.
 *
 * @api protected
 */

function get (parsed, opts, fn) {
  var cache = opts.cache;
  var client = new FTP();
  var filepath = parsed.pathname;
  var lastModified;

  client.once('error', onerror);
  client.once('ready', onready);
  client.once('greeting', ongreeting);

  function onready () {
    // first we have to figure out the Last Modified date.
    // try the MDTM command first, which is an optional extension command.
    client.lastMod(filepath, onlastmod);
  }

  function ongreeting (greeting) {
    debug('FTP greeting: %o', greeting);
  }

  function onerror (err) {
    client.end();
    fn(err);
  }

  function onfile (err, stream) {
    if (err) return onerror(err);
    stream.once('end', onend);
    stream.lastModified = lastModified;
    fn(null, stream);
  }

  function onend () {
    // close the FTP client socket connection
    client.end();
  }

  function getFile () {
    client.get(filepath, onfile);
  }

  function onlastmod (err, lastmod) {
    // handle the "file not found" error code
    if (err) {
      if (550 == err.code) {
        onerror(new NotFoundError());
      }
      // any other error then we'll try the LIST command instead
    }
    if (lastmod) {
      setLastMod(lastmod);
    } else {
      // try to get the last modified date via the LIST command (uses
      // more bandwidth, but is more compatible with older FTP servers
      var dir = path.dirname(filepath);
      client.list(dir, onlist);
    }
  }

  function setLastMod (lastmod) {
    lastModified = lastmod;
    if (cache && isNotModified()) {
      // file is the same as in the "cache", return a not modified error
      onerror(new NotModifiedError());
    } else {
      // XXX: a small timeout seemed necessary otherwise FTP servers
      // were returning empty sockets for the file occasionally
      setTimeout(client.get.bind(client, filepath, onfile), 10);
    }
  }

  function onlist (err, list) {
    if (err) return onerror(err);
    var name = path.basename(filepath);

    // attempt to find the "entry" with a matching "name"
    var entry;
    for (var i = 0; i < list.length; i++) {
      entry = list[i];
      debug('file %o: %o', i, entry.name);
      if (entry.name == name) {
        break;
      }
      entry = null;
    }

    if (entry) {
      setLastMod(entry.date);
    } else {
      onerror(new NotFoundError());
    }
  }

  // called when `lastModified` is set, and a "cache" stream was provided
  function isNotModified () {
    return +cache.lastModified == +lastModified;
  }

  opts.host = parsed.hostname || parsed.host || 'localhost';
  opts.port = parseInt(parsed.port, 10) || 21;
  if (debug.enabled) opts.debug = debug;

  if (parsed.auth) {
    const [user, password] = parsed.auth.split(":");
    opts.user = user;
    opts.password = password;
  }
  
  client.connect(opts);
}
