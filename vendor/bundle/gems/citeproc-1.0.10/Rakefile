# encoding: utf-8

require 'bundler'
begin
  Bundler.setup
rescue Bundler::BundlerError => e
  $stderr.puts e.message
  $stderr.puts "Run `bundle install` to install missing gems"
  exit e.status_code
end

$:.unshift(File.join(File.dirname(__FILE__), './lib'))
require 'citeproc/version'


desc 'Run an IRB session with CiteProc loaded'
task :console do
  require 'pry'
  require 'citeproc'

  Pry.start
end

task :check_warnings do
  $VERBOSE = true
  require 'citeproc'

  puts CiteProc::VERSION
end

require 'rspec/core'
require 'rspec/core/rake_task'
RSpec::Core::RakeTask.new(:spec) do |spec|
  spec.pattern = FileList['spec/**/*_spec.rb']
end

require 'cucumber/rake/task'
Cucumber::Rake::Task.new(:cucumber)

begin
  require 'coveralls/rake/task'
  Coveralls::RakeTask.new
  task :test_with_coveralls => [:spec, 'coveralls:push']
rescue LoadError => e
  # ignore
end

task :release do |t|
  system "gem build citeproc.gemspec"
  system "git tag #{CiteProc::VERSION}"
  system "git push --tags"
  system "gem push citeproc-#{CiteProc::VERSION}.gem"
end

task :default => :spec

begin
  require 'yard'
  YARD::Rake::YardocTask.new
rescue LoadError => e
  # ignore
end

require './tasks/testsuite'
