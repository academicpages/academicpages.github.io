const childProcess = require('child_process');
const debug = require('debug')('imagemagick-cli');
const deconstructCommand = require('./deconstruct-command');
const pickCli = require('./pick-cli');

//  For each command, we'll keep a map of the path to call it with. Example:
//  { convert: 'C:\ProgramData\chocolatey\bin\convert.exe' }
const cliPathsMap = {
};

function mapCli(cli) {
  //  If we have already worked out the path to the CLI, great.
  if (cliPathsMap[cli]) return Promise.resolve(cliPathsMap[cli]);

  //  If we're not on Windows, we just use the cli as-is.
  if (!/^win/.test(process.platform)) {
    cliPathsMap[cli] = cli;
    return Promise.resolve(cliPathsMap[cli]);
  }

  //  On Windows we need to pick the right CLI, internally using the 'where'
  //  command.
  return pickCli(cli)
    .then((mappedCli) => {
      cliPathsMap[cli] = mappedCli;
      return mappedCli;
    });
}

function exec(command) {
  return new Promise((resolve, reject) => {
    //  First, extract the cli and parameters.
    const { cli, parameters } = deconstructCommand(command);

    //  Map the cli to a path.
    mapCli(cli)
      .then((mappedCli) => {
        //  We have the CLI path mapped, which means we can reconstruct the command
        //  with the appropriate path and execute it.
        const reconstructedCommand = `"${mappedCli}" ${parameters}`;
        debug(`Preparing to execute: ${reconstructedCommand}`);

        childProcess.exec(reconstructedCommand, (err, stdout, stderr) => {
          debug(`  err: ${err ? err.toString() : '<null>'}`);
          debug(`  stdout: ${stdout}`);
          debug(`  stderr: ${stderr}`);
          if (err) {
            const errorMessage = `Failed to call '${command}', which was mapped to '${reconstructedCommand}'. Error is '${err.message}'.`;
            const error = new Error(errorMessage);
            error.stdout = stdout;
            error.stderr = stderr;
            return reject(error);
          }

          return resolve({ stdout, stderr });
        });
      })
      .catch(reject);
  });
}

module.exports = exec;
