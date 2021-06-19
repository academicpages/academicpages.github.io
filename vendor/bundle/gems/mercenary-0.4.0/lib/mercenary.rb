# frozen_string_literal: true

require File.expand_path("mercenary/version", __dir__)
require "optparse"
require "logger"

module Mercenary
  autoload :Command,   File.expand_path("mercenary/command", __dir__)
  autoload :Option,    File.expand_path("mercenary/option", __dir__)
  autoload :Presenter, File.expand_path("mercenary/presenter", __dir__)
  autoload :Program,   File.expand_path("mercenary/program", __dir__)

  # Public: Instantiate a new program and execute.
  #
  # name - the name of your program
  #
  # Returns nothing.
  def self.program(name)
    program = Program.new(name)
    yield program
    program.go(ARGV)
  end
end
