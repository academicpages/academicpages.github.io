var osx   = process.platform === 'darwin'
var win   = process.platform === 'win32'
var other = !osx && !win
var fs    = require('fs')

if (other) {
  try {
    module.exports = require('which').sync('google-chrome')
  } catch(e) {
    module.exports = null
  }
} else
if (osx) {
  var regPath = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'
  var altPath = require('userhome')(regPath.slice(1))

  module.exports = fs.existsSync(regPath)
    ? regPath
    : altPath
} else {
  var suffix = '\\Google\\Chrome\\Application\\chrome.exe';
  var prefixes = [
      process.env.LOCALAPPDATA
    , process.env.PROGRAMFILES
    , process.env['PROGRAMFILES(X86)']
  ]

  for (var i = 0; i < prefixes.length; i++) {
    var exe = prefixes[i] + suffix
    if (fs.existsSync(exe)) {
      module.exports = exe
      break
    }
  }
}

module.exports = module.exports || null
