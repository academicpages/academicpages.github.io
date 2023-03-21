
var thunkify = require('..');
var assert = require('assert');
var fs = require('fs');

describe('thunkify(fn)', function(){
  it('should work when sync', function(done){
    function read(file, fn) {
      fn(null, 'file: ' + file);
    }

    read = thunkify(read);

    read('foo.txt')(function(err, res){
      assert(!err);
      assert('file: foo.txt' == res);
      done();
    });
  })

  it('should work when async', function(done){
    function read(file, fn) {
      setTimeout(function(){
        fn(null, 'file: ' + file);
      }, 5);
    }

    read = thunkify(read);

    read('foo.txt')(function(err, res){
      assert(!err);
      assert('file: foo.txt' == res);
      done();
    });
  })

  it('should maintain the receiver', function(done){
    function load(fn) {
      fn(null, this.name);
    }

    var user = {
      name: 'tobi',
      load: thunkify(load)
    };

    user.load()(function(err, name){
      if (err) return done(err);
      assert('tobi' == name);
      done();
    });
  })

  it('should catch errors', function(done){
    function load(fn) {
      throw new Error('boom');
    }

    load = thunkify(load);

    load()(function(err){
      assert(err);
      assert('boom' == err.message);
      done();
    });
  })

  it('should ignore multiple callbacks', function(done){
    function load(fn) {
      fn(null, 1);
      fn(null, 2);
      fn(null, 3);
    }

    load = thunkify(load);

    load()(done);
  })

  it('should pass all results', function(done){
    function read(file, fn) {
      setTimeout(function(){
        fn(null, file[0], file[1]);
      }, 5);
    }

    read = thunkify(read);

    read('foo.txt')(function(err, a, b){
      assert(!err);
      assert('f' == a);
      assert('o' == b);
      done();
    });
  })

  it('should work with node methods', function(done){
    fs.readFile = thunkify(fs.readFile);

    fs.readFile('package.json')(function(err, buf){
      assert(!err);
      assert(Buffer.isBuffer(buf));

      fs.readFile('package.json', 'utf8')(function(err, str){
        assert(!err);
        assert('string' == typeof str);
        done();
      });
    });
  })
})