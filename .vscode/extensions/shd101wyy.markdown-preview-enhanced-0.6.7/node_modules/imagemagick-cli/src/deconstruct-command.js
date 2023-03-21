//  An expression to get a command then its parameters.
//  <whitespace><word><whitespace><anything>
const exp = new RegExp(/\s*(\S*)\s*(.*)$/);

function deconstructCommand(command) {
  if (!command) throw new Error('\'command\' is required.');

  //  Split the cli and parameters.
  const [, cli, parameters] = exp.exec(command);
  if (!cli || !parameters) throw new Error('\'command\' should be of the form \'cli parameters\'');

  return {
    cli: cli.toLowerCase(),
    parameters,
  };
}

module.exports = deconstructCommand;
