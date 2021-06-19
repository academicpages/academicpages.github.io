begin
  require 'simplecov'
  require 'coveralls' if ENV['CI']
rescue LoadError
  # ignore
end unless RUBY_VERSION < '1.9'

begin
  case
  when defined?(RUBY_ENGINE) && RUBY_ENGINE == 'rbx'
    require 'rubinius/debugger'
  when RUBY_VERSION > '2.0'
    require 'byebug'
  else
    require 'debugger'
  end
rescue LoadError
  # ignore
end

$LOAD_PATH.unshift(File.dirname(__FILE__) + '/../../lib')
require 'namae'

require 'rspec/expectations'
