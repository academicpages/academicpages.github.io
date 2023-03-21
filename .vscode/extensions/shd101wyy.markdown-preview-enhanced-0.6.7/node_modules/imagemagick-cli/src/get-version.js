const exec = require('./exec');

function getVersion() {
  return exec('convert -version')
    .then(({ stdout }) => {
      const result = /Version: ImageMagick ([\S]+)/.exec(stdout);
      return result[1];
    })
    //  Any errors means a null version.
    .catch(() => null);
}

module.exports = getVersion;
