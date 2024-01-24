#! /usr/bin/env node

var ULID = require('../dist/index.umd.js')
process.stdout.write(ULID.ulid())
