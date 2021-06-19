## 0.4.0 / 2020-01-18

### Major Enhancements

  * Drop Ruby 2.3 support

### Minor Enhancements

  * Remove parent command&#39;s flags from subcommand usage (#44)

### Development Fixes

  * Adopt Jekyll&#39;s rubocop config for consistency

### Documentation

  * fixes the readme (#52)

## 0.3.6 / 2016-04-07

### Bug Fixes

  * Presenter: Options should include those from parent command (#42)

## 0.3.5 / 2014-11-12

### Bug Fixes

  * Capture `OptionsParser::InvalidOption` and show a nice error message (#38)
  * Absolute paths for requires and autoloads (#39)

### Development Fixes

  * Bump to RSpec 3 (#40)

## 0.3.4 / 2014-07-11

### Bug Fixes

  * Use option object as key in the command's `@map` hash (#35)

## 0.3.3 / 2014-05-07

### Bug Fixes

  * The `--version` flag should not exit with code 1, but instead code 0. (#33)

## 0.3.2 / 2014-03-18

### Bug Fixes

  * Remove duplicate commands from help output; show aliases w/command names (#29)

## 0.3.1 / 2014-02-21

### Minor Enhancements

  * Add `-t/--trace` to list of options in help message (#19)

### Bug Fixes

  * `Mercenary::Option` now accepts return values in the form of Class constants (#22)

## 0.3.0 / 2014-02-20

### Major Enhancements

  * Officially drop 1.8.7 support (#14)
  * Allow Commands to set their own versions (#17)
  * Show subcommands, options and usage in help and attach to all commands (#18)
  * Add `-t, --trace` to allow full exception backtrace to print, otherwise print just the error message (#19)

### Minor Enhancements

  * Logging state is maintained throughout process (#12)
  * Tidy up Command#logger output (#21)

### Development Fixes

  * Added specs for `Program` (#13)

## 0.2.1 / 2013-12-25

### Bug Fixes

  * Added missing comma to fix '-v' and '--version' options (#9)

## 0.2.0 / 2013-11-30

### Major Enhancements

  * Add `Command#default_command` to specify a default command if none is given by the user at runtime (#7)

### Minor Enhancements

  * Add `Command#execute` to execute the actions of a command (#6)

### Development Fixes

  * Add standard GitHub bootstrap and cibuild scripts to `script/` (#2)

## 0.1.0 / 2013-11-08

### Major Enhancements

  * It works!

### Minor Enhancements

  * Add a logger to `Command`
  * Add `--version` switch to all programs

### Bug Fixes

  * Fix `Command#syntax` and `Command#description`'s handing of setting vs getting
  * Fix load path problem in `lib/mercenary.rb`

### Development Fixes

  * Add TomDoc to everything
  * Add a couple starter specs
  * Add TravisCI badge
  * Add Travis configuration

## 0.0.1 / 2013-11-06

  * Birthday!
