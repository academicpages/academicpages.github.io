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
require 'csl/version'


desc 'Run a Pry session with CSL loaded'
task :console do
  ARGV.clear

  require 'pry'
  require 'csl'

  Pry.start
end

require 'rspec/core'
require 'rspec/core/rake_task'
RSpec::Core::RakeTask.new(:spec) do |spec|
  spec.pattern = FileList['spec/**/*_spec.rb']
end

require 'cucumber/rake/task'
Cucumber::Rake::Task.new(:cucumber) do |t|
  t.profile = 'default'
end

begin
  require 'coveralls/rake/task'
  Coveralls::RakeTask.new
  task :test_with_coveralls => [:spec, :cucumber, 'coveralls:push']
rescue LoadError => e
  # ignore
end if ENV['CI']

task :release do |t|
  system "gem build csl.gemspec"
  system "git tag #{CSL::VERSION}"
  system "git push --tags"
  system "gem push csl-#{CSL::VERSION}.gem"
end

task :default => [:spec, :cucumber]

task :check_warnings do
  $VERBOSE = true
  require 'csl'

  CSL::Style.new
  CSL::Locale.new

  puts CSL::VERSION
end

begin
  require 'yard'
  YARD::Rake::YardocTask.new
rescue LoadError => e
  # ignore
end
