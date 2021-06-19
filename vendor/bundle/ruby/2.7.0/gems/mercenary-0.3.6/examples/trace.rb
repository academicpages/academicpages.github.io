#!/usr/bin/env ruby

$:.unshift File.join(File.dirname(__FILE__), *%w{ .. lib })

require "mercenary"

# This example sets the logging mode of mercenary to
# debug. Logging messages from "p.logger.debug" will
# be output to STDOUT.

Mercenary.program(:trace) do |p|

  p.version "2.0.1"
  p.description 'An example of traces in Mercenary'
  p.syntax 'trace <subcommand>'

  p.action do |_, _|
    raise ArgumentError.new("YOU DID SOMETHING TERRIBLE YOU BUFFOON")
  end

end
