#!/usr/bin/env node
var onchange = require('./')
var arrify = require('arrify')

// Parse argv with minimist...it's easier this way.
var argv = require('minimist')(process.argv.slice(2), {
  '--': true,
  boolean: ['v', 'i', 'w'],
  string: ['e', 'c'],
  alias: {
    verbose: ['v'],
    initial: ['i'],
    exclude: ['e'],
    wait: ['w'],
    cwd: ['c']
  }
})

// Print usage info
if (!argv._.length || argv.help) {
  console.log('Usage: onchange [...file] -- <command> [...args]')
  process.exit()
}

// Setup some storage variables
var matches = argv._.slice()

// Build exclusion list
var exclude = arrify(argv.exclude)

// Ignore node_modules folders, as they eat CPU like crazy
if (exclude.length === 0) {
  exclude.push('**/node_modules/**')
}

// Shift first thing after to command and use the rest as args
var args = argv['--'].slice()
var command = args.shift()

var options = {
  exclude: exclude,
  verbose: argv.verbose,
  initial: argv.initial,
  wait: argv.wait,
  cwd: argv.cwd
}

if (!command) {
  console.error('Remember to pass the command after "--":')
  console.error('  onchange \'**/*.js\' -- echo \'{{changed}}\'')
  process.exit(1)
}

// Start watcher
onchange(matches, command, args, options)
