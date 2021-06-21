# -*- coding: utf-8 -*-
module CiteProc

  # Names consist of several dependent parts of strings. Simple personal names
  # are composed of family and given elements, containing respectively the
  # family and given name of the individual.
  #
  #     Name.new(:family => 'Doe', :given => 'Jane')
  #
  # Institutional and other names that should always be presented literally
  # (such as "The Artist Formerly Known as Prince", "Banksy", or "Ramses IV")
  # should be delivered as a single :literal element:
  #
  #     Name.new(:literal => 'Banksy')
  #
  # Name particles, such as the "von" in "Alexander von Humboldt", can be
  # delivered separately from the family and given name, as :dropping-particle
  # and :non-dropping-particle elements.
  #
  # Name suffixes such as the "Jr." in "Frank Bennett, Jr." and the "III" in
  # "Horatio Ramses III" can be delivered as a suffix element.
  #
  #      Name.new do |n|
  #        n.family, n.given, n.suffix = 'Ramses', 'Horatio', 'III'
  #      end
  #
  # Names not written in the Latin or Cyrillic scripts are always displayed
  # with the family name first. Sometimes it might be desired to handle a
  # Latin or Cyrillic transliteration as if it were a fixed (non-Byzantine)
  # name (e.g., for Hungarian names). This behavior can be prompted by
  # including activating static-ordering:
  #
  #     Name.new(:family => 'Murakami', :given => 'Haruki').to_s
  #     #-> "Haruki Murakami"
  #
  #     Name.new(:family => 'Murakami', :given => 'Haruki').static_order!.to_s
  #     #-> "Murakami Haruki"
  class Name

    extend Forwardable

    include Attributes
    include Comparable

    # Class instance variables

    @romanesque =
      /^[\p{Latin}\p{Greek}\p{Cyrillic}\p{Hebrew}\p{Armenian}\p{Georgian}\p{Common}]*$/

    # Default formatting options
    @defaults = {
      :form => 'long',
      :'name-as-sort-order' => false,
      :'demote-non-dropping-particle' => :never,
      :'sort-separator' => ', ',
      :initialize => true,
      :'initialize-with-hyphen' => true,
      :'initialize-with' => nil
    }.freeze

    @parts = [:family, :given,:literal, :suffix, :'dropping-particle',
      :'non-dropping-particle'].freeze

    class << self
      attr_reader :defaults, :parts, :romanesque
    end



    # Method generators

    # @!attribute [r] options
    # @return the name's formatting options
    attr_reader :options

    attr_reader :sort_prefix

    attr_predicates :'comma-suffix', :'static-ordering', :multi, *@parts

    # Aliases
    [[:particle, :'non_dropping_particle']].each do |a, m|
      alias_method(a, m) if method_defined?(m)

      wa, wm = "#{a}=", "#{m}="
      alias_method(wa, wm) if method_defined?(wm)

      pa, pm = "#{a}?", "#{m}?"
      alias_method(pa, pm) if method_defined?(pm)

      pa, pm = "has_#{a}?", "has_#{m}?"
      alias_method(pa, pm) if method_defined?(pm)
    end

    # Names quack sorta like a String
    def_delegators :to_s, :=~, :===, *String.instance_methods(false).reject { |m|
      m.to_s =~ /^[\W_]|[!=_]$|^(to_s|inspect|replace|first|last|dup|clone)$/
    }

    # Delegate bang! methods to each field's value
    String.instance_methods(false).each do |m|
      if m.to_s.end_with?('!')
        define_method(m) do |*arguments, &block|
          Name.parts.each do |part|
            p = attributes[part]
            p.send(m, *arguments, &block) if p.respond_to?(m)
          end
          self
        end
      end
    end


    # Instance methods

    def initialize(attributes = {}, options = {})
      @options = Name.defaults.merge(options)
      @sort_prefix = (/^(the|an?|der|die|das|eine?|l[ae])\s+|^l\W/i).freeze

      merge(attributes)

      yield self if block_given?
    end

    def initialize_copy(other)
      @attributes = other.attributes.deep_copy
      @options = other.options.dup
    end


    # Resets the object's options to the default settings.
    # @return [self]
    def reset!
      @options = Name.defaults.dup
    end

    # Returns a copy of the name object with all options
    # reset to their default settings.
    # @return [Name] a copy of the name with default options
    def reset
      dup.reset!
    end

    # @return [Boolean] whether or not the Name looks like it belongs to a person
    def personal?
      !empty? && !literal?
    end

    # A name is `romanesque' if it contains only romanesque characters. This
    # should be the case for the majority of names written in latin- or
    # greek-based script. It will be false, for example, for names written
    # in Chinese, Japanese, Arabic or Hebrew.
    #
    # @return [Boolean] whether or not the name is romanesque
    def romanesque?
      !!([given, family].join.gsub(Variable.markup, '') =~ Name.romanesque)
    end

    alias byzantine? romanesque?

    # @return [Boolean] whether or not the name should be printed in static order
    def static_order?
      static_ordering? || !romanesque?
    end

    # Set the name to use static order for printing, i.e., print the family
    # name before the given name as is customary, for example, in Hungarian
    # and many Asian languages.
    #
    # @return [self]
    def static_order!
      self.static_ordering = true
      self
    end

    alias static_order static_ordering
    alias static_order= static_ordering=

    # @return [Boolean] whether or not the name will be printed in sort-order
    def sort_order?
      !!(options[:'name-as-sort-order'].to_s =~ /^(y(es)?|always|t(rue)?)$/i)
    end

    def display_order?
      !sort_order?
    end

    # Sets the name to use sort-order. The reverse of {#display_order!}.
    # @return [self]
    def sort_order!(toggle = true)
      options[:'name-as-sort-order'] = !!toggle
      self
    end

    # Sets the name to use display-order. The reverse of {#sort_order!}.
    # @return [self]
    def display_order!(toggle = true)
      options[:'name-as-sort-order'] = !toggle
      self
    end

    # @return [String] the current sort separator
    def sort_separator
      options[:'sort-separator']
    end

    alias comma sort_separator

    # @return [Boolean] whether or not the short form will be used for printing
    def short_form?
      options[:form].to_s =~ /short/i
    end

    # Use short form for printing the name
    # @return [self]
    def short_form!
      options[:form] = 'short'
      self
    end

    # @return [Boolean] whether or not the long form will be used for printing
    def long_form?
      !short_form?
    end

    # Use long form for printing the name
    # @return [self]
    def long_form!
      options[:form] = 'long'
      self
    end

    # @return [Boolean] whether or not initials will be used for printing
    def initials?
      !!options[:'initialize-with'] && personal? && romanesque?
    end

    def initialize_with
      options[:'initialize-with'].to_s
    end

    def initialize_existing_only?
      options[:initialize].to_s == 'false'
    end

    def initialize_without_hyphen?
      !options[:'initialize-with-hyphen']
    end

    def initialize_without_hyphen!
      options[:'initialize-with-hyphen'] = false
    end

    def initials
      case
      when !initials?
        given
      when initialize_existing_only?
        existing_initials_of given
      else
        initials_of given
      end
    end

    def demote_non_dropping_particle?
      always_demote_non_dropping_particle? ||
        !!(sort_order? && options[:'demote-non-dropping-particle'] =~ /^sort(-only)?$/i)
    end

    alias demote_particle? demote_non_dropping_particle?

    def never_demote_non_dropping_particle?
      !!(options[:'demote-non-dropping-particle'] =~ /^never$/i)
    end

    def never_demote_non_dropping_particle!
      options[:'demote-non-dropping-particle'] = 'never'
      self
    end

    alias never_demote_particle? never_demote_non_dropping_particle?
    alias never_demote_particle! never_demote_non_dropping_particle!

    def always_demote_non_dropping_particle?
      !!(options[:'demote-non-dropping-particle'] =~ /^(display-and-sort|always)$/i)
    end

    def always_demote_non_dropping_particle!
      options[:'demote-non-dropping-particle'] = 'display-and-sort'
      self
    end

    alias always_demote_particle? always_demote_non_dropping_particle?
    alias always_demote_particle! always_demote_non_dropping_particle!

    alias demote_particle! always_demote_non_dropping_particle!

    # Compares two names. The comparison is based on #sort_order_downcase
    #
    # @see #sort_order_downcase
    #
    # @param other [#sort_order_downcase] the other name
    # @return [Fixnum,nil] -1, 0, or 1 depending on the result of the
    #   comparison; nil if the name cannot be compared to the passed-in object
    def <=>(other)
      return nil unless other.respond_to?(:sort_order_downcase)
      sort_order_downcase <=> other.sort_order_downcase
    end

    def to_s
      [given, family].compact_join(' ')
    end

    # @return [String] the name formatted according to the current options
    def format
      case
      when literal?
        literal.to_s
      when static_order?
        [family, initials].compact.join(' ')
      when !short_form?
        case
        when !sort_order?
          [[initials, dropping_particle, particle, family].compact_join(' '),
            suffix].compact_join(comma_suffix? ? comma : ' ')

        when !demote_particle?
          [[particle, family].compact_join(' '), [initials,
            dropping_particle].compact_join(' '), suffix].compact_join(comma)

        else
          [family, [initials, dropping_particle, particle].compact_join(' '),
            suffix].compact_join(comma)
        end
      else
        [particle, family].compact_join(' ')
      end
    end
    alias print format

    # @return [Array<String>] an ordered array of formatted name parts to be used for sorting
    def sort_order
      case
      when literal?
        [literal.to_s.sub(sort_prefix, '')]
      when never_demote_particle?
        [[particle, family].compact_join(' '), dropping_particle, given, suffix].map(&:to_s)
      else
        [family, [particle, dropping_particle].compact_join(' '), given, suffix].map(&:to_s)
      end
    end

    # @return [String] the name as a string stripped off all markup
    def strip_markup
      gsub(Variable.markup, '')
    end

    # @return [self] the name with all parts stripped off markup
    def strip_markup!
      gsub!(Variable.markup, '')
    end

    # @return [Array<String>] the sort order array stripped off markup and downcased
    def sort_order_downcase
      sort_order.map { |s| s.downcase.gsub(Variable.markup, '') }
    end

    # @return [String] a human-readable representation of the name object
    def inspect
      "#<CiteProc::Name #{to_s.inspect}>"
    end

    private

    def filter_key(key)
      key = key.to_s.tr('_', '-')
      key = 'non-dropping-particle' if key == 'particle'
      super key
    end

    def initials_of(string)
      return unless string
      string = string.dup

      string.gsub!(/([[:upper:]])[^[:upper:]\s-]*\s*/, "\\1#{initialize_with}")

      initialize_hyphen!(string)

      string.strip!
      string
    end

    def initialize_hyphen!(string)
      if initialize_without_hyphen?
        string.tr!('-', '')
      else
        string.gsub!(/\s*-/, '-')
      end
    end

    def existing_initials_of(string)
      return unless string
      string = string.dup

      string.gsub!(/([[:upper:]])([[:upper:]])/, '\1 \2')
      string.gsub!(/\b([[:upper:]])\b[^[:alpha:]-]*/, "\\1#{initialize_with}")

      initialize_hyphen!(string)

      string.strip!
      string
    end
  end




  # Represents a {Variable} containing an ordered list of {Name}
  # objects. The names can be formatted using CSL formatting options (see
  # {Names.defaults} for details).
  class Names < Variable

    @defaults = {
      :and => ' & ',
      :delimiter => ', ',
      :'delimiter-precedes-last' => :contextual,
      :'et-al' => 'et al.',
      :'et-al-min' => 5,
      :'et-al-use-first' => 3,
      :'et-al-subsequent-min' => 5,
      :'et-al-subsequent-use-first' => 3
    }.freeze

    class << self

      # @!attribute [r] defaults
      # @example
      #    {
      #      :and => '&',
      #      # The delimiter between the penultimate and last name
      #
      #      :delimiter => ', ',
      #      # The delimiter between the other names
      #
      #      :'delimiter-precedes-last' => :contextual,
      #      # Determines in which cases the delimiter used to delimit names
      #      # is also used to separate the second to last and the last name
      #      # in name lists. The possible values are: 'contextual' (default,
      #      # the delimiter is only included for name lists with three or
      #      # more names), 'always', and 'never'
      #
      #      :'et-al' => 'et al.',
      #      # The string used for the phrase 'and others'
      #
      #      :'et-al-min' => 5,
      #      :'et-al-use-first' => 3,
      #      # Together, these attributes control et-al abbreviation. When
      #      # the number of names in a name variable matches or exceeds
      #      # the number set on et-al-min, the rendered name list is truncated
      #      # at the number of names set on et-al-use-first. If truncation
      #      # occurs, the "et-al" term is appended to the names rendered.
      #      # With a single name (et-al-use-first="1"), the "et-al" term is
      #      # preceded by a space (e.g. "Doe et al."). With multiple names,
      #      # the "et-al" term is preceded by the name delimiter (e.g.
      #      # "Doe, Smith, et al.")
      #
      #      :'et-al-subsequent-min' => 5,
      #      :'et-al-subsequent-use-first' => 3
      #      # See above. Abbreviation rules for subsequent cites (cites
      #      # referencing earlier cited items)
      #    }
      #
      # @return [Hash] the Names' default formatting options
      attr_reader :defaults

      # Parses the passed-in string and returns a Names object. Behaves like
      # parse but returns nil for bad input without raising an error.
      #
      # @see .parse!
      #
      # @param names [String] the name or names to be parsed
      # @return [Names,nil] the parsed names
      def parse(names)
        parse!(names)
      rescue ParseError
        nil
      end

      # Parses the passed-in string and returns a Names object.
      #
      # @param names [String] the name or names to be parsed
      # @return [Names] the parsed names
      #
      # @raise [ParseError] if the string cannot be parsed.
      def parse!(names)
        new Namae.parse!(names)
      rescue
        raise ParseError, $!.message
      end

    end

    include Enumerable

    # @!attribute [r] options
    # @return [Hash] the current formatting options

    attr_reader :options

    alias names value

    # Don't expose value/names writer
    undef_method :value=

    # Delegate bang! methods to each name
    Name.instance_methods(false).each do |m|
      if m.to_s.end_with?('!')
        define_method(m) do |*arguments, &block|
          names.each do |name|
            name.send(m, *arguments, &block)
          end
          self
        end
      end
    end

    # Names quack sorta like an Array
    def_delegators :names, :length, :empty?, :[], :join


    # Some delegators should return self

    # @!method push(name)
    #    Appends the given name to the list of names.
    #    @param name [Name] a name
    #    @return [self]
    # @!method unshift(name)
    #    Inserts the given name at the beginning of the list of names.
    #    @param name [Name] a name
    #    @return [self]
    [:<<, :push, :unshift].each do |m|
      define_method(m) do |*arguments, &block|
        names.send(m, *arguments, &block)
        self
      end
    end

    def initialize(*arguments)
      @options = Names.defaults.dup
      super(arguments.flatten(1))
    end

    def initialize_copy(other)
      @options, @value = other.options.dup, other.value.map(&:dup)
    end

    def replace(values)
      @value = []

      [*values].each do |value|
        case
        when value.is_a?(Name)
          @value << value
        when value.respond_to?(:each_pair), value.respond_to?(:to_hash)
          @value << Name.new(value)
        when value.respond_to?(:to_s)
          begin
            @value.concat Namae.parse!(value.to_s).map { |n| Name.new n }
          rescue
            raise TypeError, $!.message
          end
        else
          raise TypeError, "failed to create names from #{value.inspect}"
        end
      end

      self
    end

    # @return [Fixnum] the maximum number of names that should be printed
    def max_names
      [length, options[:'et-al-use-first'].to_i.abs].min
    end

    # @return [Boolean] whether or not the Names should be truncate
    def truncate?
      length >= options[:'et-al-min'].to_i.abs
    end

    # @return [Boolean] whether ot not the Names, if printed on subsequent
    #   cites, should be truncated
    def truncate_subsequent?
      length >= options[:'et-al-subsequent-min'].to_i
    end

    # @return [String] the delimiter between names
    def delimiter
      options[:delimiter]
    end

    # @return [String] the delimiter between the penultimate and last name
    # @see #connector
    # @see #delimiter_precedes_last?
    def last_delimiter
      if delimiter_precedes_last?
        [delimiter, connector].compact.join.squeeze(' ')
      else
        connector
      end
    end

    # @return [String] the delimiter between the last name printed name and
    #   the 'and others' term
    def truncated_delimiter
      max_names > 1 ? delimiter : ' '
    end

    # @return [Boolean] whether or not the delimiter will be inserted between
    #   the penultimate and the last name
    def delimiter_precedes_last?
      case
      when delimiter_never_precedes_last?
        false
      when delimiter_always_precedes_last?
        true
      else
        length > 2
      end
    end

    # @return [Boolean] whether or not the should always be inserted between
    #   the penultimate and the last name
    def delimiter_always_precedes_last?
      !!(options[:'delimiter-precedes-last'].to_s =~ /^always$/i)
    end

    # Set the :'delimiter-precedes-last' option to :always
    # @return [self] self
    def delimiter_always_precedes_last!
      options[:'delimiter-precedes-last'] = :always
      self
    end

    alias delimiter_precedes_last! delimiter_always_precedes_last!


    # @return [Boolean] whether or not the should never be inserted between
    #   the penultimate and the last name
    def delimiter_never_precedes_last?
      !!(options[:'delimiter-precedes-last'].to_s =~ /^never$/i)
    end

    # Set the :'delimiter-precedes-last' option to :never
    # @return [self] self
    def delimiter_never_precedes_last!
      options[:'delimiter-precedes-last'] = :never
      self
    end

    # @return [Boolean] whether or not the should be inserted between the
    #   penultimate and the last name depending on the number of names
    def delimiter_contextually_precedes_last?
      !!(options[:'delimiter-precedes-last'].to_s =~ /^contextual/i)
    end

    # Set the :'delimiter-precedes-last' option to :contextual
    # @return [self] self
    def delimiter_contextually_precedes_last!
      options[:'delimiter-precedes-last'] = :contextual
      self
    end

    # @return [String] the connector between the penultimate and the last name
    def connector
      options[:and]
    end

    # @return [false] Names are non-numeric Variables
    def numeric?
      false
    end

    # @return [Boolean] whether or not the variable holds more than one Name
		def plural?
			length > 1
		end

    # Calls a block once for each name. If no block is given, an enumerator
    # is returned instead.
    #
    # @yieldparam name [Name] a name in the list
    # @return [self,Enumerator] self or an enumerator if no block is given
    def each(&block)
      if block_given?
        names.each(&block)
        self
      else
        to_enum
      end
    end

    # Compares two lists of Names.
    # @param other [(Name)] a list of names
    # @return [Fixnum,nil] -1, 0, or 1 depending on the result of the
    #   comparison; or nil if the two objects cannot be compared
    def <=>(other)
      return nil unless other.respond_to?(:to_a)
      to_a <=> other.to_a
    end

		alias to_i length

    # Converts the list of names into a formatted string depending on the
    # current formatting options.
    # @return [String] the formatted list of names
    def to_s
      case
      when truncate?
        [names[0...max_names].join(delimiter), options[:'et-al']].join(truncated_delimiter)
      when length < 3
        names.join(last_delimiter)
      else
        [names[0...-1].join(delimiter), names[-1]].join(last_delimiter)
      end
    end

    # @return [String] the names in a BibTeX-compatible format
    def to_bibtex
      map { |n| n.dup.sort_order!.format }.join(' and ')
    end

    # @return [Array<Hash>] the list of names converted to hash objects
    def to_citeproc
      map(&:to_citeproc)
    end

    # @return [String] a human-readable representation of the Names object
    def inspect
      "#<CiteProc::Names #{to_s.inspect}>"
    end

  end

end
