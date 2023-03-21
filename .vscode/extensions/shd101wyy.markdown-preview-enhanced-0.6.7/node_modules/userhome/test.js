var test = require('tape');
var userhome = require('./');

test('returns some kind of path', function(t) {
  t.plan(2);
  t.ok(userhome().length > 2);
  t.ok(userhome('test').indexOf('test') !== -1);
});

test('throws an error if we cant find a valid home', function(t) {
  t.plan(1);
  var homevar = (process.platform === 'win32') ? 'USERPROFILE' : 'HOME';
  var oldhome = process.env[homevar];
  delete process.env[homevar];
  t.throws(function() {
    userhome('what');
    process.env[homevar] = oldhome;
  }, /Could not find a valid user home path./g);
});
