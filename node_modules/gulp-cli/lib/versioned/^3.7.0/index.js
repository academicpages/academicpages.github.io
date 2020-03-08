'use strict';

var fs = require('fs');

var log = require('gulplog');
var stdout = require('mute-stdout');

var taskTree = require('./task-tree');
var copyTree = require('../../shared/log/copy-tree');

var tildify = require('../../shared/tildify');
var logTasks = require('../../shared/log/tasks');
var ansi = require('../../shared/ansi');
var logEvents = require('./log/events');
var logTasksSimple = require('./log/tasks-simple');
var registerExports = require('../../shared/register-exports');

function execute(opts, env, config) {
  var tasks = opts._;
  var toRun = tasks.length ? tasks : ['default'];

  if (opts.tasksSimple || opts.tasks || opts.tasksJson) {
    // Mute stdout if we are listing tasks
    stdout.mute();
  }

  // This is what actually loads up the gulpfile
  var exported = require(env.configPath);
  log.info('Using gulpfile', ansi.magenta(tildify(env.configPath)));

  var gulpInst = require(env.modulePath);
  logEvents(gulpInst);

  registerExports(gulpInst, exported);

  // Always unmute stdout after gulpfile is required
  stdout.unmute();

  process.nextTick(function() {
    var tree;

    if (opts.tasksSimple) {
      return logTasksSimple(env, gulpInst);
    }
    if (opts.tasks) {
      tree = taskTree(gulpInst.tasks);
      if (config.description && typeof config.description === 'string') {
        tree.label = config.description;
      } else {
        tree.label = 'Tasks for ' + ansi.magenta(tildify(env.configPath));
      }
      return logTasks(tree, opts, function(task) {
        return gulpInst.tasks[task].fn;
      });
    }
    if (opts.tasksJson) {
      tree = taskTree(gulpInst.tasks);
      if (config.description && typeof config.description === 'string') {
        tree.label = config.description;
      } else {
        tree.label = 'Tasks for ' + tildify(env.configPath);
      }

      var output = JSON.stringify(copyTree(tree, opts));

      if (typeof opts.tasksJson === 'boolean') {
        return console.log(output);
      }

      return fs.writeFileSync(opts.tasksJson, output, 'utf-8');
    }
    gulpInst.start.apply(gulpInst, toRun);
  });
}

module.exports = execute;
