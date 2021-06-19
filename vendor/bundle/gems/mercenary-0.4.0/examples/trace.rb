#!/usr/bin/env ruby
# frozen_string_literal: true

$LOAD_PATH.unshift File.join(__dir__, "..", "lib")

require "mercenary"

# This example sets the logging mode of mercenary to
# debug. Logging messages from "p.logger.debug" will
# be output to STDOUT.

Mercenary.program(:trace) do |p|
  p.version "2.0.1"
  p.description "An example of traces in Mercenary"
  p.syntax "trace <subcommand>"

  p.action do |_, _|
    raise ArgumentError, "YOU DID SOMETHING TERRIBLE YOU BUFFOON"
  end
end
