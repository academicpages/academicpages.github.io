# Mercenary

Lightweight and flexible library for writing command-line apps in Ruby.

[![Build Status](https://secure.travis-ci.org/jekyll/mercenary.png)](https://travis-ci.org/jekyll/mercenary)

## Installation

Add this line to your application's Gemfile:

    gem 'mercenary'

And then execute:

    $ bundle

Or install it yourself as:

    $ gem install mercenary

**Note: Mercenary may not work with Ruby < 1.9.3.**

## Usage

Creating programs and commands with Mercenary is easy:

```ruby
Mercenary.program(:jekyll) do |p|
  p.version Jekyll::VERSION
  p.description 'Jekyll is a blog-aware, static site generator in Ruby'
  p.syntax "jekyll <subcommand> [options]"

  p.command(:new) do |c|
    c.syntax "new PATH" # do not include the program name or super commands
    c.description "Creates a new Jekyll site scaffold in PATH"
    c.option 'blank', '--blank', 'Initialize the new site without any content.'

    c.action do |args, options|
      Jekyll::Commands::New.process(args, blank: options['blank'])
    end
  end

  p.command(:build) do |c|
    c.syntax "build [options]"
    c.description "Builds your Jekyll site"

    c.option 'safe', '--safe', 'Run in safe mode'
    c.option 'source', '--source DIR', 'From where to collect the source files'
    c.option 'destination', '--dest DIR', 'To where the compiled files should be written'

    c.action do |_, options|
      Jekyll::Commands::Build.process(options)
    end
  end

  # Bring in command bundled in external gem
  begin
    require "jekyll-import"
    JekyllImport.init_with_program(p)
  rescue LoadError
  end

  p.default_command(:build)
end
```

All commands have the following default options:

- `-h/--help` - show a help message
- `-v/--version` - show the program version
- `-t/--trace` - show the full backtrace when an error occurs

## API

### `Mercenary`

#### `.program`

Creates and executes a program. Accepts two arguments:

- `name` - program name as a Symbol
- `block` - the specification for the program, passed the program instance as an
  argument.

Example is above, under the heading [Usage](#usage).

### `Program`

`Program` is a subclass of `Command`, so it has all of the methods documented
below as well as those for `Command`.

#### `#config`

Fetches the program configuration hash.

### `Command`

#### `#new`

Create a new command. Accepts two arguments:

- `name` - the name of your command, as a symbol
- `parent` - (optional) the parent Command

#### `#version`

Sets or gets the version of the command. Accepts an optional argument:

- `version` - (optional) the version to set for the command. If present, this
  becomes the new version for the command and persists.

#### `#syntax`

Sets or gets the syntax of the command. Built on parent syntaxes if a parent
exists. Accepts one optional argument:

- `syntax` - (optional) the syntax to set for the command. Will inherit from the
  parent commands or program. Usually in the form of
  `"command_name <SUBCOMMAND> [OPTIONS]"`

When a parent command exists, say `supercommand`, with syntax set as
`supercommand <SUBCOMMAND> [OPTIONS]`, the syntax of the command in question
will be `supercommand command_name <SUBCOMMAND> [OPTIONS]` with both
`<SUBCOMMAND>` and `[OPTIONS]` stripped out. Any text between `<` and `>` or
between `[` and `]` will be stripped from parent command syntaxes. The purpose
of this chaining is to reduce redundancy.

#### `#description`

Sets or gets the description of the command. Accepts one optional argument:

- `desc` - (optional) the description to set for the command. If
  provided, will override any previous description set for the command.

#### `#default_command`

Sets or gets the default subcommand of the command to execute in the event no
subcommand is passed during execution. Accepts one optional argument:

- `command_name` - (optional) the `Symbol` name of the subcommand to be
  executed. Raises an `ArgumentError` if the subcommand doesn't exist.
  Overwrites previously-set default commands.

#### `#option`

Adds a new option to the command. Accepts many arguments:

- `config_key` - the configuration key that the value of this option maps to.
- `*options` - all the options, globbed, to be passed to `OptionParser`, namely the
  switches and the option description. Usually in the format
  `"-s", "--switch", "Sets the 'switch' flag"`.

Valid option calls:

```ruby
cmd.option 'config_key', '-c', 'Sets the "config" flag'
cmd.option 'config_key', '--config', 'Sets the "config" flag'
cmd.option 'config_key', '-c', '--config', 'Sets the "config" flag.'
cmd.option 'config_key', '-c FILE', '--config FILE', 'The config file.'
cmd.option 'config_key', '-c FILE1[,FILE2[,FILE3...]]', '--config FILE1[,FILE2[,FILE3...]]', Array, 'The config files.'
```

Notice that you can specify either a short switch, a long switch, or both. If
you want to accept an argument, you have to specify it in the switch strings.
The class of the argument defaults to `String`, but you can optionally set a
different class to create, e.g. `Array`, if you are expecting a particular class
in your code from this option's value. The description is also optional, but
it's highly recommended to include a description.

#### `#alias` 

Specifies an alias for this command such that the alias may be used in place of
the command during execution. Accepts one argument:

- `cmd_name` - the alias name for this command as a `Symbol`

Example:

```ruby
cmd.alias(:my_alias)
# Now `cmd` is now also executable via "my_alias"
```

#### `#action`

Specifies a block to be executed in the event the command is specified at
runtime. The block is given two arguments:

- `args` - the non-switch arguments given from the command-line
- `options` - the options hash built via the switches passed

**Note that actions are additive**, meaning any new call to `#action` will
result in another action to be executed at runtime. Actions will be executed in
the order they are specified in.

Example:

```ruby
cmd.action do |args, options|
  # do something!
end
```

#### `#logger`

Access the logger for this command. Useful for outputting information to STDOUT.
Accepts one optional argument:

- `level` - (optional) the severity threshold at which to begin logging. Uses
  Ruby's built-in
  [`Logger`](http://www.ruby-doc.org/stdlib-2.1.0/libdoc/logger/rdoc/Logger.html)
  levels.

Log level defaults to `Logger::INFO`.

Examples:

```ruby
cmd.logger(Logger::DEBUG)
cmd.logger.debug "My debug message."
cmd.logger.info "My informative message."
cmd.logger.warn "ACHTUNG!!"
cmd.logger.error "Something terrible has happened."
cmd.logger.fatal "I can't continue doing what I'm doing."
```

#### `#command`

Creates a new subcommand for the current command. Accepts two arguments:

- `cmd_name` - the command name, as a Symbol
- `block` -  the specification of the subcommand in a block

Example:

```ruby
my_command.command(:my_subcommand) do |subcmd|
  subcmd.description 'My subcommand'
  subcmd.syntax 'my_subcommand [OPTIONS]'
  # ...
end
```

## Contributing

1. Fork it
2. Create your feature branch (`git checkout -b my-new-feature`)
3. Commit your changes (`git commit -am 'Add some feature'`)
4. Push to the branch (`git push origin my-new-feature`)
5. Create new Pull Request
