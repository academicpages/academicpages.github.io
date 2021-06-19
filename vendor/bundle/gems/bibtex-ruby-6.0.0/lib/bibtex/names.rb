#--
# BibTeX-Ruby
# Copyright (C) 2010-2015  Sylvester Keil <sylvester.keil.or.at>
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

require 'forwardable'

module BibTeX
  # A BibTeX Names value is an ordered list of name values.
  class Names < Value
    include Enumerable

    def_delegators :@tokens, :each, :sort

    def self.parse(string)
      new(NameParser.new.parse(string))
    rescue StandardError => e
      BibTeX.log.info(e.message)
      nil
    end

    def initialize(*arguments)
      @tokens = []
      arguments.flatten.compact.each do |argument|
        add(argument)
      end
    end

    def replace(*_arguments)
      self
    end

    def join
      self
    end

    def value(options = {})
      @tokens.map { |n| n.to_s(options) }.join(' and ')
    end

    def to_s(options = {})
      return value unless options.key?(:quotes)

      q = [options[:quotes]].flatten
      [q[0], value, q[-1]].compact.join
    end

    def name?
      true
    end

    def numeric?
      false
    end

    def atomic?
      true
    end

    alias names? name?
    alias symbol? numeric?

    def to_name
      self
    end

    def to_citeproc(options = {})
      map { |n| n.to_citeproc(options) }
    end

    def strip_braces
      gsub!(/\{|\}/, '')
    end

    def add(name)
      if name.is_a?(Name)
        @tokens << name
      elsif name.respond_to?(:to_s)
        @tokens += Names.parse(name.to_s)
      else
        raise ArgumentError, "failed to add #{name.inspect}: not a name."
      end
      self
    end

    alias << add
    alias push add

    %i[convert! rename_if rename_unless extend_initials].each do |method_id|
      define_method(method_id) do |*arguments|
        tokens.each { |t| t.send(method_id, *arguments) }
        self
      end
    end

    def <=>(other)
      other.respond_to?(:to_a) ? to_a <=> other.to_a : super
    end
  end

  # A Name comprises individual name parts (first, last, prefix and suffix),
  # but behaves almost like an atomic string value.
  class Name < Struct.new(:first, :last, :prefix, :suffix)
    extend Forwardable
    include Comparable

    BibTeXML = {
      first: :first,
      last: :last,
      prefix: :prelast,
      suffix: :lineage
    }.freeze

    def_delegators :to_s, :=~, :===,
                   *String.instance_methods(false).reject { |m| m =~ /^\W|to_s|replace|each|first|last|!$/ }

    class << self
      def parse(string)
        [NameParser.new.parse(string)].flatten[0]
      end

      # Returns true if thing looks like a name.
      # Actually converts thing to a string and tries to parse it.
      def looks_like?(thing)
        thing.respond_to?(:to_s) && [Name.new.parse(string)].flatten.compact.empty?
      end
    end

    def initialize(attributes = {})
      set(attributes)
    end

    def initialize_copy(other)
      other.each_pair do |k, v|
        self[k] = v.dup unless v.nil?
      end
    end

    # Set the name tokens to the values defined in the passed-in hash.
    def set(attributes = {})
      attributes.each_pair do |key, value|
        send("#{key}=", value) if respond_to?(key)
      end

      self
    end

    def blank?
      to_a.compact.empty?
    end

    # Returns the first name (or the passed-in string) as initials.
    def initials(token = first)
      token.to_s.gsub(/([[:upper:]])[^[:upper:]\s-]*\s*/, '\1.')
    end

    def normalize_initials(token = first)
      token = token.dup.to_s
      token.gsub!(/([[:upper:]])([[:upper:]])/, '\1 \2')
      token.gsub!(/\b([[:upper:]])\b[^[:alpha:]-]*/, '\1.')
      token.gsub!(/\b([[:upper:]]\.)([[:upper:]][[:lower:]]+)/, '\1 \2')
      token
    end

    # Returns true if the first name consists solely of initials.
    def initials?
      !(first.nil? || first.empty? || first.to_s =~ /[[:alpha:]]{2,}[^\.]/)
    end

    # Sets the name's first name to the passed-in name if the last name equals
    # for_last and the current first name has the same initials as with_first.
    def extend_initials(with_first, for_last)
      rename_if first: with_first do |name|
        if name.last == for_last
          mine = name.initials.split(/\.[^[:alpha:]]*/)
          other = initials(with_first).split(/\.[^[:alpha:]]*/)

          mine == other || mine.length < other.length && mine == other[0, mine.length]
        end
      end
    end

    # Renames the tokens according to the passed-in attributes if all of the
    # conditions match or if the given block returns true.
    def rename_if(attributes, conditions = {})
      if block_given?
        set(attributes) if yield self
      else
        set(attributes) if conditions.all? do |key, value|
          respond_to?(key) && send(key) == value
        end
      end

      self
    end

    def rename_unless(attributes, conditions = {})
      if block_given?
        set(attributes) unless yield self
      else
        set(attributes) unless conditions.all? do |key, value|
          respond_to?(key) && send(key) == value
        end
      end

      self
    end

    # call-seq:
    #   name.display_order #=> 'Edgar Allen Poe'
    #   name.display_order :initials => true #=> 'E.A. Poe'
    #
    # Returns the name as a string in display order.
    def display_order(options = {})
      [options[:initials] ? initials : first, prefix, last, suffix].compact.join(' ')
    end

    alias display display_order

    # call-seq:
    #   name.sort_order #=> 'Poe, Edgar Allen'
    #   name.sort_order :initials => true #=> 'Poe, E.A.'
    #
    # Returns the name as a string in sort order.
    def sort_order(options = {})
      [[prefix, last].compact.join(' '), suffix, options[:initials] ? initials : first].compact.join(', ')
    end

    alias to_s sort_order

    def <=>(other)
      other.is_a?(Name) ? sort_order <=> other.sort_order : super
    end

    def to_hash
      Hash[each_pair.to_a]
    end

    def to_xml
      require 'rexml/document'
      xml = REXML::Element.new('bibtex:person')

      each_pair do |part, text|
        next if text.nil?

        element = REXML::Element.new("bibtex:#{BibTeXML[part]}")
        element.text = text
        xml.add_element(element)
      end

      xml
    end

    %i[strip! upcase! downcase! sub! gsub! chop! chomp! rstrip!].each do |method_id|
      define_method(method_id) do |*arguments, &block|
        each do |part|
          part&.send(method_id, *arguments, &block)
        end
        self
      end
    end

    def convert(*filters)
      dup.convert!(*filters)
    end

    def convert!(*filters)
      filters.flatten.each do |filter|
        f = Filters.resolve(filter) ||
            raise(ArgumentError, "Failed to load filter #{filter.inspect}")

        each_pair do |k, v|
          self[k] = f.apply(v) unless v.nil?
        end
      end

      self
    end

    def to_citeproc(options = {})
      hash = {}
      hash['family'] = family unless family.nil?
      hash['given'] = given unless given.nil?
      hash['suffix'] = suffix unless suffix.nil?
      hash[options[:particle] || 'non-dropping-particle'] = prefix unless prefix.nil?
      hash
    end

    alias family last
    alias family= last=
    alias given first
    alias given= first=
    alias jr suffix
    alias jr= suffix=
    alias von prefix
    alias von= prefix=
  end
end
