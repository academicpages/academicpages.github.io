var fs = require('fs')
var join = require('path').join
var assert = require('assert')
var onchange = require('../')

var FIXTURE_DIR = join(__dirname, '__test__')

// Set up test directory before proceeding.
if (!fs.existsSync(FIXTURE_DIR)) {
  fs.mkdirSync(FIXTURE_DIR)
}

function run (cb) {
  var out = fs.createWriteStream(join(FIXTURE_DIR, 'out.txt'))
  var count = 0

  onchange(['__test__/*'], 'node', ['slow.js', '{{event}}', '{{changed}}'], {
    cwd: __dirname,
    stdout: out
  })

  function write () {
    count++
    fs.writeFileSync(join(FIXTURE_DIR, 'file.txt'), Math.random().toString())

    if (count >= 10) {
      cb(null, count)
      return
    }

    setTimeout(write, 500)
  }

  write()
}

run(function (err, count) {
  var result = fs.readFileSync(join(FIXTURE_DIR, 'out.txt'), 'utf8')
  var lines = result.trim().split('\n').length

  assert.equal(lines, 2)
  assert.equal(count, 10)

  process.exit(0)
})