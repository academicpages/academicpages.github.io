# ----------------------------------------------------------------------------
# Frozen-string-literal: true
# Copyright: 2015-2016 Jordon Bedwell - MIT License
# Encoding: utf-8
# ----------------------------------------------------------------------------

$LOAD_PATH.unshift(File.expand_path("../lib", __FILE__))
require "luna/rubocop/rake/task"
require "rspec/core/rake_task"

task :default => [:spec]
RSpec::Core::RakeTask.new :spec
task :test => :spec
