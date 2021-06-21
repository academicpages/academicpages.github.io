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
require 'latex/decode/version'


desc 'Run an IRB session with LaTeX-Decode loaded'
task :console, [:script] do |t,args|
  ARGV.clear

  require 'irb'
  require 'latex/decode'

  IRB.conf[:SCRIPT] = args.script
  IRB.start
end

require 'cucumber/rake/task'
Cucumber::Rake::Task.new(:cucumber)

task :release do |t|
  system "gem build latex-decode.gemspec"
  system "git tag #{LaTeX::Decode::VERSION}"
  system "git push --tags"
  system "gem push latex-decode-#{LaTeX::Decode::VERSION}.gem"
  system "rm latex-decode-#{LaTeX::Decode::VERSION}.gem"
  system "jgem build latex-decode.gemspec"
  system "jgem push latex-decode-#{LaTeX::Decode::VERSION}.gem"
  system "rm latex-decode-#{LaTeX::Decode::VERSION}-java.gem"
end

task :default => :cucumber
