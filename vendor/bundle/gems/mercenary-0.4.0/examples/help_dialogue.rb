#!/usr/bin/env ruby
# frozen_string_literal: true

$LOAD_PATH.unshift File.join(__dir__, "..", "lib")

require "mercenary"

# This example sets the logging mode of mercenary to
# debug. Logging messages from "p.logger.debug" will
# be output to STDOUT.

Mercenary.program(:help_dialogue) do |p|
  p.version "2.0.1"
  p.description "An example of the help dialogue in Mercenary"
  p.syntax "help_dialogue <subcommand>"

  p.command(:some_subcommand) do |c|
    c.version "1.4.2"
    c.syntax "some_subcommand <subcommand> [options]"
    c.description "Some subcommand to do something"
    c.option "an_option", "-o", "--option", "Some option"
    c.alias(:blah)

    c.command(:yet_another_sub) do |f|
      f.syntax "yet_another_sub [options]"
      f.description "Do amazing things"
      f.option "blah", "-b", "--blah", "Trigger blah flag"
      f.option "heh", "-H ARG", "--heh ARG", "Give a heh"

      f.action do |args, options|
        print "Args: "
        p args
        print "Opts: "
        p options
      end
    end
  end

  p.command(:another_subcommand) do |c|
    c.syntax "another_subcommand <subcommand> [options]"
    c.description "Another subcommand to do something different."
    c.option "an_option", "-O", "--option", "Some option"
    c.option "another_options", "--pluginzzz", "Set where the plugins should be found from"
  end
end
