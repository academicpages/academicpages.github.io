begin
  require 'simplecov'
  require 'coveralls' if ENV['CI']
rescue LoadError
  # ignore
end

begin
  case
  when RUBY_PLATFORM < 'java'
    require 'debug'
    Debugger.start
  when defined?(RUBY_ENGINE) && RUBY_ENGINE == 'rbx'
    require 'rubinius/debugger'
  when defined?(RUBY_VERSION) && RUBY_VERSION < '2.0'
    require 'debugger'
  else
    require 'byebug'
  end
rescue LoadError
  # ignore
end

require 'minitest/autorun'
require 'minitest/ansi'

Minitest::ANSI.use!

require 'tempfile'

require 'bibtex'

module BibTeX
  module Test

    class << self
      def fixtures(name)
        File.expand_path("../fixtures/#{name}.bib", __FILE__)
      end
    end

  end
end
