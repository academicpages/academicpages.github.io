const childProcess = require('child_process');

const regexes = [
  //  Most intalls will be in an ImageMagick folder...
  new RegExp(/ImageMagick/, 'i'),

  //  ...if the user uses 'choco' to install, it'll be in a chocolatey folder.
  new RegExp(/chocolatey/, 'i'),
];

function pickCli(cli) {
  return new Promise((resolve, reject) => {
    //  If we are not on Windows, then just return the original cli.
    if (/^win/.test(process.platform) === false) return resolve(cli);

    //  We're on windows, so we need to see the available options with 'where'.
    return childProcess.exec(`where ${cli}`, (err, stdout) => {
      if (err) return reject(err);

      const options = stdout.split('\r\n');

      //  The first regex to pass wins.
      for (let i = 0; i < regexes.length; i += 1) {
        for (let j = 0; j < options.length; j += 1) {
          const result = regexes[i].test(options[j]);
          if (result) return resolve(options[j]);
        }
      }

      //  Nothing matches, bad luck. We'll go for the first option.
      return resolve(options[0]);
    });
  });
}

module.exports = pickCli;
