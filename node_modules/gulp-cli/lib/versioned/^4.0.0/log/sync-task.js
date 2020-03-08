'use strict';

var log = require('gulplog');
var ansi = require('../../../shared/ansi');

var tasks = {};

function warn() {
  var taskKeys = Object.keys(tasks);

  if (!taskKeys.length) {
    return;
  }

  var taskNames = taskKeys.map(function(key) {
    return tasks[key];
  }).join(', ');

  process.exitCode = 1;

  log.warn(
    ansi.red('The following tasks did not complete:'),
    ansi.cyan(taskNames)
  );
  log.warn(
    ansi.red('Did you forget to signal async completion?')
  );
}

function start(e) {
  tasks[e.uid] = e.name;
}

function clear(e) {
  delete tasks[e.uid];
}

function logSyncTask(gulpInst) {

  process.once('exit', warn);
  gulpInst.on('start', start);
  gulpInst.on('stop', clear);
  gulpInst.on('error', clear);
}

module.exports = logSyncTask;
