require File.expand_path("../mercenary/version", __FILE__)
require "optparse"
require "logger"

module Mercenary
  autoload :Command,   File.expand_path("../mercenary/command", __FILE__)
  autoload :Option,    File.expand_path("../mercenary/option", __FILE__)
  autoload :Presenter, File.expand_path("../mercenary/presenter", __FILE__)
  autoload :Program,   File.expand_path("../mercenary/program", __FILE__)

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
