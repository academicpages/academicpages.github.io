#--
# BibTeX-Ruby
# Copyright (C) 2010-2015 Sylvester Keil <sylvester.keil.or.at>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#++

module BibTeX

  #
  # The base class for BibTeX objects.
  #
  class Element
    include Comparable

    attr_writer :id
    attr_reader :bibliography

    # Returns an array of BibTeX elements.
    def self.parse(input, options = {})
      case input
      when Element
        [input]
      when Hash
        [Entry.new(input)]
      when Array
        input.inject([]) { |s,a| s.concat(parse(a, options)) }
      when ::String
        Parser.new(options).parse(input).data.each do |e|
          e.parse_names unless !e.respond_to?(:parse_names) || options[:parse_names] == false
          e.parse_month unless !e.respond_to?(:parse_month) || options[:parse_months] == false
        end
      else
        raise ArgumentError, "failed to parse Element from #{input.inspect}"
      end
    end

    # Returns a string containing the object's content.
    def content(options = {})
      ''
    end

    # Returns a string containing the object's content.
    def values_at(*arguments)
      []
    end

    def digest(*arguments)
      [type, content].join('|')
    end

    # Invokes BibTeX string replacement on this element.
    def replace(*arguments); self; end

    # Invokes BibTeX string joining on this element.
    def join; self; end

    # Returns the element's id.
    def id; @id ||= object_id.to_s; end

    # Returns the BibTeX type (if applicable) or the normalized class name.
    def type
      self.class.name.split(/::/).last.gsub(/([[:lower:]])([[:upper:]])/) { "#{$1}_#{$2}" }.downcase.intern
    end

    # Returns a list of names for that Element. All Elements except Entries return an empty list.
    def names
      []
    end

    def has_type?(type)
      self.type == type.intern || defined?(type) == 'constant' && is_a?(type)
    end

    [:entry, :book, :article, :collection, :string, :preamble, :comment].each do |type|
      method_id = "#{type}?"
      define_method(method_id) { has_type?(type) } unless method_defined?(method_id)
    end

    # Returns true if the element matches the given query.
    def matches?(query)
      return true if query.nil? || query.respond_to?(:empty?) && query.empty?

      case query
      when Symbol
        query.to_s == id.to_s
      when Element
        query == self
      when Regexp
        to_s.match(query)
      when /^\/(.+)\/$/
        to_s.match(Regexp.new($1))
      when /@(\*|\w+)(?:\[([^\]]*)\])?/
        query.scan(/(!)?@(\*|\w+)(?:\[([^\]]*)\])?/).any? do |non, type, condition|
          if (non ? !has_type?(type) : has_type?(type))
            if condition.nil? || condition.empty?
              true
            else
              condition.to_s.split(/\s*\|\|\s*/).any? do |conditions|
                meets_all? conditions.split(/\s*(?:,|&&)\s*/)
              end
            end
          end
        end
      else
        id.to_s == query
      end
    end

    alias === matches?
    alias match? matches?

    def meets_all?(*conditions)
      meets? conditions.flatten, :all?
    end
    alias meet_all? meets_all?

    def meets_any?(*conditions)
      meets? conditions.flatten, :any?
    end
    alias meet_any? meets_any?

    # Returns true if the element meets all or any of the given conditions.
    def meets?(conditions, op = :all?)
      conditions.send(op) do |condition|
        meets_condition? condition
      end
    end
    alias meet? meets?

    alias to_s content

    def to_hash(options = {})
      { type => content }
    end

    def to_yaml(options = {})
      require 'yaml'
      to_hash.to_yaml
    end

    def to_json(options = {})
      # Some JSON implementations pass an argument
      # to this method.
      options = {} unless options.is_a?(::Hash)

      ::JSON.dump(to_hash(options))
    end

    def to_xml(options = {})
      require 'rexml/document'
      xml = REXML::Element.new(type)
      xml.text = content
      xml
    end

    # Called when the element was added to a bibliography.
    def added_to_bibliography(bibliography)
      # raise BibTeXError, "failed to add element to Bibliography: already registered with another Bibliography" unless @bibliography.nil?
      @bibliography = bibliography
      self
    end

    # Called when the element was removed from a bibliography.
    def removed_from_bibliography(bibliography)
      @bibliography = nil
      self
    end

    def <=>(other)
      return nil unless other.respond_to? :type and other.respond_to? :to_s
      [type, to_s] <=> [other.type, other.to_s]
    end

    # Returns the Element as a nicely formatted string.
    def inspect
      "#<#{self.class} #{content.gsub(/\n/, ' ')}>"
    end

    private

    def meets_condition?(condition)
      property, operator, value = condition.split(/\s*([!~\/\^<>]?=|!~)\s*/)

      if property.nil?
        true
      else
        property.strip!
        value.strip! unless value.nil?

        if operator.nil? && value.nil?
          respond_to?(:provides?) && provides?(property)
        else

          # Hack: we need to get rid of #type returning the bibtex_type,
          # because type is a valid BibTeX property. This mitigates the
          # issue but is no fix!
          if property == 'type'
            actual = respond_to?(:fields) ? fields[:type] : nil
          else
            actual = respond_to?(property) ? send(property) : nil
          end

          case operator
          when '!=', '/='
            actual.nil? || actual.to_s != value
          when '^='
            !actual.nil? && actual.to_s.match("^#{value}")
          when '~='
            !actual.nil? && actual.to_s.match(value)
          when '!~'
            actual.nil? || !actual.to_s.match(value)
          when '<='
            !actual.nil? && actual.to_i <= value.to_i
          when '>='
            !actual.nil? && actual.to_i >= value.to_i
          else
            !actual.nil? && actual.to_s == value
          end
        end
      end
    end
  end


  #
  # Represents a @string object.
  #
  # In BibTeX @string objects contain a single string constant
  # assignment. For example, @string{ foo = "bar" } defines the
  # constant `foo'; this constant can be used (using BibTeX's
  # string concatenation syntax) in susbsequent
  # @string and @preamble objects, as well as in field values
  # of regular entries.
  #
  class String < Element
    include Replaceable

    attr_reader :key

    # Creates a new instance.
    def initialize(key = nil, value = nil)
      @key, @value = key.to_sym, Value.new(value)
      yield self if block_given?
    end

    # Sets the string's key (i.e., the symbol identifying the constant).
    def key=(key)
      raise(ArgumentError, "keys must be convertible to Symbol; was: #{type.class.name}.") unless type.respond_to?(:to_sym)

      unless bibliography.nil?
        bibliography.strings.delete(@key)
        bibliography.strings[key.to_sym] = self
      end

      @key = key.to_sym
    end

    # Retuns the string's value if parameter matches the key; nil otherwise.
    def [](key)
      @key == key ? @value : nil
    end


    # Called when the element was added to a bibliography.
    def added_to_bibliography(bibliography)
      super
      bibliography.strings[@key] = self
      self
    end

    # Called when the element was removed from a bibliography.
    def removed_from_bibliography(bibliography)
      super
      bibliography.strings[@key] = nil
      self
    end

    # Returns a string representation of the @string's content.
    def content
      "#@key = #{@value.to_s(:quotes => '"')}"
    end

    # Returns a string representation of the @string object.
    def to_s(options = {})
      "@string{ #{content} }\n"
    end

    def to_hash(options = {})
      { :string => { @key => @value.to_s(:quotes => '"') } }
    end

    def to_xml(options = {})
      require 'rexml/document'

      xml = REXML::Element.new(:string)

      k, v = REXML::Element.new(:key), REXML::Element.new(:value)
      k.text = key.to_s
      v.text = value.to_s(:quotes => '"')

      xml.add_elements(k)
      xml.add_elements(v)

      xml
    end
  end

  #
  # Represents a @preamble object.
  #
  # In BibTeX an @preamble object contains a single string literal,
  # a single constant, or a concatenation of string literals and
  # constants.
  class Preamble < Element
    include Replaceable

    # Creates a new instance.
    def initialize(value = '')
      @value = Value.new(value)
    end

    # Returns a string representation of the @preamble's content.
    def content
      @value.to_s(:quotes => '"')
    end

    # Returns a string representation of the @preamble object
    def to_s(options = {})
      "@preamble{ #{content} }\n"
    end
  end

  # Represents a @comment object.
  class Comment < Element
    attr_accessor :content

    def initialize(content = '')
      @content = content
    end

    def to_s(options = {})
      "@comment{ #@content }\n"
    end
  end

  # Represents text in a `.bib' file, but outside of an
  # actual BibTeX object; typically, such text is treated
  # as a comment and is ignored by the parser.
  # BibTeX-Ruby offers this class to allows for
  # post-processing of this type of `meta' content. If you
  # want the parser to include +MetaComment+ objects, you
  # need to add +:meta_content+ to the parser's +:include+
  # option.
  class MetaContent < Element
    attr_accessor :content

    def initialize(content = '')
      @content = content
    end

    def to_s(options = {}); @content; end
  end

end
