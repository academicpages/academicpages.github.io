#!/usr/bin/env rake
# frozen_string_literal: true

require 'rubygems'
require 'bundler/setup'

require 'bundler/gem_tasks'
require 'rake/testtask'

Rake::TestTask.new do |t|
  t.libs << 'test'
  t.test_files = FileList['test/**/*_test.rb']
  t.verbose = true
  t.warning = false
end

task default: :test
