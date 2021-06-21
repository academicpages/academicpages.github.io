# frozen_string_literal: true

module Mercenary
  class Presenter
    attr_accessor :command

    # Public: Make a new Presenter
    #
    # command - a Mercenary::Command to present
    #
    # Returns nothing
    def initialize(command)
      @command = command
    end

    # Public: Builds a string representation of the command usage
    #
    # Returns the string representation of the command usage
    def usage_presentation
      "  #{command.syntax}"
    end

    # Public: Builds a string representation of the options
    #
    # Returns the string representation of the options
    def options_presentation
      return nil unless command_options_presentation || parent_command_options_presentation

      [command_options_presentation, parent_command_options_presentation].compact.join("\n")
    end

    def command_options_presentation
      return nil if command.options.empty?

      options = command.options
      options -= command.parent.options if command.parent
      options.map(&:to_s).join("\n")
    end

    # Public: Builds a string representation of the options for parent
    # commands
    #
    # Returns the string representation of the options for parent commands
    def parent_command_options_presentation
      return nil unless command.parent

      Presenter.new(command.parent).options_presentation
    end

    # Public: Builds a string representation of the subcommands
    #
    # Returns the string representation of the subcommands
    def subcommands_presentation
      return nil if command.commands.empty?

      command.commands.values.uniq.map(&:summarize).join("\n")
    end

    # Public: Builds the command header, including the command identity and description
    #
    # Returns the command header as a String
    def command_header
      header = command.identity.to_s
      header << " -- #{command.description}" if command.description
      header
    end

    # Public: Builds a string representation of the whole command
    #
    # Returns the string representation of the whole command
    def command_presentation
      msg = []
      msg << command_header
      msg << "Usage:"
      msg << usage_presentation

      if opts = options_presentation
        msg << "Options:\n#{opts}"
      end
      if subcommands = subcommands_presentation
        msg << "Subcommands:\n#{subcommands_presentation}"
      end
      msg.join("\n\n")
    end

    # Public: Turn a print_* into a *_presentation or freak out
    #
    # meth  - the method being called
    # args  - an array of arguments passed to the missing method
    # block - the block passed to the missing method
    #
    # Returns the value of whatever function is called
    def method_missing(meth, *args, &block)
      if meth.to_s =~ %r!^print_(.+)$!
        send("#{Regexp.last_match(1).downcase}_presentation")
      else
        # You *must* call super if you don't handle the method,
        # otherwise you'll mess up Ruby's method lookup.
        super
      end
    end
  end
end
