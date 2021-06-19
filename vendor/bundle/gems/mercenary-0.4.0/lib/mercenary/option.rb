# frozen_string_literal: true

module Mercenary
  class Option
    attr_reader :config_key, :description, :short, :long, :return_type

    # Public: Create a new Option
    #
    # config_key - the key in the config hash to which the value of this option
    #              will map
    # info       - an array containing first the switches, then an optional
    #              return type (e.g. Array), then a description of the option
    #
    # Returns nothing
    def initialize(config_key, info)
      @config_key = config_key
      while arg = info.shift
        begin
          @return_type = Object.const_get(arg.to_s)
          next
        rescue NameError
        end
        if arg.start_with?("-")
          if arg.start_with?("--")
            @long = arg
          else
            @short = arg
          end
          next
        end
        @description = arg
      end
    end

    # Public: Fetch the array containing the info OptionParser is interested in
    #
    # Returns the array which OptionParser#on wants
    def for_option_parser
      [short, long, return_type, description].flatten.reject { |o| o.to_s.empty? }
    end

    # Public: Build a string representation of this option including the
    #   switches and description
    #
    # Returns a string representation of this option
    def to_s
      "#{formatted_switches}  #{description}"
    end

    # Public: Build a beautifully-formatted string representation of the switches
    #
    # Returns a formatted string representation of the switches
    def formatted_switches
      [
        switches.first.rjust(10),
        switches.last.ljust(13),
      ].join(", ").gsub(%r! , !, "   ").gsub(%r!,   !, "    ")
    end

    # Public: Hash based on the hash value of instance variables
    #
    # Returns a Fixnum which is unique to this Option based on the instance variables
    def hash
      instance_variables.map do |var|
        instance_variable_get(var).hash
      end.reduce(:^)
    end

    # Public: Check equivalence of two Options based on equivalence of their
    #   instance variables
    #
    # Returns true if all the instance variables are equal, false otherwise
    def eql?(other)
      return false unless self.class.eql?(other.class)

      instance_variables.map do |var|
        instance_variable_get(var).eql?(other.instance_variable_get(var))
      end.all?
    end

    # Public: Fetch an array of switches, including the short and long versions
    #
    # Returns an array of two strings. An empty string represents no switch in
    # that position.
    def switches
      [short, long].map(&:to_s)
    end
  end
end
