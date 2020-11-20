require 'simplecov'

module SimpleCov
  module Configuration
    def clean_filters
      @filters = []
    end
  end
end

SimpleCov.configure do
  clean_filters
  load_profile 'test_frameworks'
end

ENV["COVERAGE"] && SimpleCov.start do
  add_filter "/.rvm/"
end
require 'rubygems'
require 'bundler'
begin
  Bundler.setup(:default, :development)
rescue Bundler::BundlerError => e
  $stderr.puts e.message
  $stderr.puts "Run `bundle install` to install missing gems"
  exit e.status_code
end

$LOAD_PATH.unshift(File.dirname(__FILE__))
$LOAD_PATH.unshift(File.join(File.dirname(__FILE__), '..', 'lib'))
require 'hawkins'
require 'stringio'

module SpecUtils
  # Copied from Minitest.  The Rspec output matcher doesn't work very will with
  # blocks that are throwing exceptions.
  def capture_io
    orig_stdout = $stdout
    captured_stdout = StringIO.new
    $stdout = captured_stdout

    orig_stderr = $stderr
    captured_stderr = StringIO.new
    $stderr = captured_stderr

    yield

    return captured_stdout.string, captured_stderr.string
  ensure
    $stdout = orig_stdout
    $stderr = orig_stderr
  end
end

RSpec.configure do |config|
  config.color = true
  config.expect_with :rspec do |c|
    c.syntax = :expect
  end
  config.formatter = 'Fuubar'
  config.include SpecUtils
end
