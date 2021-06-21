# frozen_string_literal: false

module Mercenary
  class Command
    attr_reader :name
    attr_reader :description
    attr_reader :syntax
    attr_accessor :options
    attr_accessor :commands
    attr_accessor :actions
    attr_reader :map
    attr_accessor :parent
    attr_reader :trace
    attr_reader :aliases

    # Public: Creates a new Command
    #
    # name - the name of the command
    # parent - (optional) the instancce of Mercenary::Command which you wish to
    #          be the parent of this command
    #
    # Returns nothing
    def initialize(name, parent = nil)
      @name     = name
      @options  = []
      @commands = {}
      @actions  = []
      @map      = {}
      @parent   = parent
      @trace    = false
      @aliases  = []
    end

    # Public: Sets or gets the command version
    #
    # version - the command version (optional)
    #
    # Returns the version and sets it if an argument is non-nil
    def version(version = nil)
      @version = version if version
      @version
    end

    # Public: Sets or gets the syntax string
    #
    # syntax - the string which describes this command's usage syntax (optional)
    #
    # Returns the syntax string and sets it if an argument is present
    def syntax(syntax = nil)
      @syntax = syntax if syntax
      syntax_list = []
      syntax_list << parent.syntax.to_s.gsub(%r!<[\w\s-]+>!, "").gsub(%r!\[[\w\s-]+\]!, "").strip if parent
      syntax_list << (@syntax || name.to_s)
      syntax_list.join(" ")
    end

    # Public: Sets or gets the command description
    #
    # description - the description of what the command does (optional)
    #
    # Returns the description and sets it if an argument is present
    def description(desc = nil)
      @description = desc if desc
      @description
    end

    # Public: Sets the default command
    #
    # command_name - the command name to be executed in the event no args are
    #                present
    #
    # Returns the default command if there is one, `nil` otherwise
    def default_command(command_name = nil)
      if command_name
        if commands.key?(command_name)
          @default_command = commands[command_name] if command_name
          @default_command
        else
          raise ArgumentError, "'#{command_name}' couldn't be found in this command's list of commands."
        end
      else
        @default_command
      end
    end

    # Public: Adds an option switch
    #
    # sym - the variable key which is used to identify the value of the switch
    #       at runtime in the options hash
    #
    # Returns nothing
    def option(sym, *options)
      new_option = Option.new(sym, options)
      @options << new_option
      @map[new_option] = sym
    end

    # Public: Adds a subcommand
    #
    # cmd_name - the name of the command
    # block    - a block accepting the new instance of Mercenary::Command to be
    #            modified (optional)
    #
    # Returns nothing
    def command(cmd_name)
      cmd = Command.new(cmd_name, self)
      yield cmd
      @commands[cmd_name] = cmd
    end

    # Public: Add an alias for this command's name to be attached to the parent
    #
    # cmd_name - the name of the alias
    #
    # Returns nothing
    def alias(cmd_name)
      logger.debug "adding alias to parent for self: '#{cmd_name}'"
      aliases << cmd_name
      @parent.commands[cmd_name] = self
    end

    # Public: Add an action Proc to be executed at runtime
    #
    # block - the Proc to be executed at runtime
    #
    # Returns nothing
    def action(&block)
      @actions << block
    end

    # Public: Fetch a Logger (stdlib)
    #
    # level - the logger level (a Logger constant, see docs for more info)
    #
    # Returns the instance of Logger

    def logger(level = nil)
      unless @logger
        @logger = Logger.new(STDOUT)
        @logger.level = level || Logger::INFO
        @logger.formatter = proc do |severity, _datetime, _progname, msg|
          "#{identity} | " << "#{severity.downcase.capitalize}:".ljust(7) << " #{msg}\n"
        end
      end

      @logger.level = level unless level.nil?
      @logger
    end

    # Public: Run the command
    #
    # argv   - an array of string args
    # opts   - the instance of OptionParser
    # config - the output config hash
    #
    # Returns the command to be executed
    def go(argv, opts, config)
      opts.banner = "Usage: #{syntax}"
      process_options(opts, config)
      add_default_options(opts)

      if argv[0] && cmd = commands[argv[0].to_sym]
        logger.debug "Found subcommand '#{cmd.name}'"
        argv.shift
        cmd.go(argv, opts, config)
      else
        logger.debug "No additional command found, time to exec"
        self
      end
    end

    # Public: Add this command's options to OptionParser and set a default
    #         action of setting the value of the option to the inputted hash
    #
    # opts - instance of OptionParser
    # config - the Hash in which the option values should be placed
    #
    # Returns nothing
    def process_options(opts, config)
      options.each do |option|
        opts.on(*option.for_option_parser) do |x|
          config[map[option]] = x
        end
      end
    end

    # Public: Add version and help options to the command
    #
    # opts - instance of OptionParser
    #
    # Returns nothing
    def add_default_options(opts)
      option "show_help", "-h", "--help", "Show this message"
      option "show_version", "-v", "--version", "Print the name and version"
      option "show_backtrace", "-t", "--trace", "Show the full backtrace when an error occurs"
      opts.on("-v", "--version", "Print the version") do
        puts "#{name} #{version}"
        exit(0)
      end

      opts.on("-t", "--trace", "Show full backtrace if an error occurs") do
        @trace = true
      end

      opts.on_tail("-h", "--help", "Show this message") do
        puts self
        exit
      end
    end

    # Public: Execute all actions given the inputted args and options
    #
    # argv - (optional) command-line args (sans opts)
    # config - (optional) the Hash configuration of string key to value
    #
    # Returns nothing
    def execute(argv = [], config = {})
      if actions.empty? && !default_command.nil?
        default_command.execute
      else
        actions.each { |a| a.call(argv, config) }
      end
    end

    # Public: Check if this command has a subcommand
    #
    # sub_command - the name of the subcommand
    #
    # Returns true if this command is the parent of a command of name
    # 'sub_command' and false otherwise
    def has_command?(sub_command)
      commands.key?(sub_command)
    end

    # Public: Identify this command
    #
    # Returns a string which identifies this command
    def ident
      "<Command name=#{identity}>"
    end

    # Public: Get the full identity (name & version) of this command
    #
    # Returns a string containing the name and version if it exists
    def identity
      "#{full_name} #{version}".strip
    end

    # Public: Get the name of the current command plus that of
    #   its parent commands
    #
    # Returns the full name of the command
    def full_name
      the_name = []
      the_name << parent.full_name if parent&.full_name
      the_name << name
      the_name.join(" ")
    end

    # Public: Return all the names and aliases for this command.
    #
    # Returns a comma-separated String list of the name followed by its aliases
    def names_and_aliases
      ([name.to_s] + aliases).compact.join(", ")
    end

    # Public: Build a string containing a summary of the command
    #
    # Returns a one-line summary of the command.
    def summarize
      "  #{names_and_aliases.ljust(20)}  #{description}"
    end

    # Public: Build a string containing the command name, options and any subcommands
    #
    # Returns the string identifying this command, its options and its subcommands
    def to_s
      Presenter.new(self).print_command
    end
  end
end
