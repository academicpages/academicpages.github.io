
# Namae is a parser for human names. It recognizes personal names of
# various cultural backgrounds and tries to split them into their
# component parts (e.g., given and family names, honorifics etc.).
#
# The main use case of Namae is to use the {Namae.parse .parse} or
# {Namae.parse! .parse!} method to parse a string of names and return
# a list of {Namae::Name Name} objects.
#
# @example Name parsing
#   Namae.parse('Yukihiro "Matz" Matsumoto')
#   #=> [#<Name family="Matsumoto" given="Yukihiro" nick="Matz">]
#
#   Namae.parse('Torvalds, Linus and Cox, Alan')
#   #=> [#<Name family="Torvalds" given="Linus">, #<Name family="Cox" given="Alan">]
#
module Namae

  module_function

  # Parses the passed-in string and returns a list of names. Behaves like
  # parse but returns an empty list for bad input without raising an error.
  #
  # @see parse!
  #
  # @param names [String] the name or names to be parsed
  # @return [Array] the list of parsed names
  def parse(names)
    Parser.instance.parse(names)
  end

  # Parses the passed-in string and returns a list of names.
  #
  # @param names [String] the name or names to be parsed
  # @return [Array] the list of parsed names
  #
  # @raise [ArgumentError] if the string cannot be parsed.
  def parse!(names)
    Parser.instance.parse!(names)
  end

  # @return [Hash] the parser's current configuration.
  def options
    Parser.instance.options
  end

  # @yield [Hash] the parser's default configuration.
  def configure
    yield Parser.defaults
  end
end
