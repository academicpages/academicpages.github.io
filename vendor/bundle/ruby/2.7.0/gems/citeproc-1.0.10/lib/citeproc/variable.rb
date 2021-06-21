
module CiteProc

  # A CiteProc Variable represents the content of a text, numeric, date, or
  # name variable. In its basic form it is thin abstraction that behaves
  # almost like a regular Ruby string; more complex Variables are handled
  # by dedicated sub-classes that make the variable's type more explicit.
  #
  # @abstract
  class Variable

    extend Forwardable
    include Comparable

    @fields = Hash.new { |h,k| h.fetch(k.to_sym, nil) }.merge({
      :date => %w{
        accessed container event-date issued original-date submitted
      },

      :names => %w{
        author collection-editor composer container-author recipient editor
        editorial-director illustrator interviewer original-author translator
        director reviewed-author
      },

      :number => %w{
        chapter-number collection-number edition issue number number-of-pages
        number-of-volumes volume
      },

      :text => %w{
        abstract annote archive archive_location archive-place authority
        call-number citation-label citation-number collection-title
        container-title container-title-short dimensions DOI event event-place
        first-reference-note-number genre ISBN ISSN jurisdiction keyword
        locator medium note original-publisher original-publisher-place
        original-title page page-first PMID PMCID publisher publisher-place
        references reviewed-title scale section source status
        title title-short URL version year-suffix
      }
    })

    @fields.each_value { |v| v.map!(&:to_sym) }

    @types = Hash.new { |h,k| h.fetch(k.to_sym, nil) }.merge(
      Hash[*@fields.keys.map { |k| @fields[k].map { |n| [n,k] } }.flatten]
    ).freeze

    @fields[:name] = @fields[:names]
    @fields[:dates] = @fields[:date]
    @fields[:numbers] = @fields[:number]

    @fields[:all] = @fields[:any] =
      [:date,:names,:text,:number].reduce([]) { |s,a| s.concat(@fields[a]) }.sort

    @fields.freeze

    @markup = /<[^>]*>/.freeze


    class << self

      # @!attribute [r] fields
      # @return [{Symbol => Array<Symbol>}] mapping of variable types to
      #   their respective field names
      attr_reader :fields

      # @!attribute [r] types
      # @return [{Symbol => Symbol}] mapping of field names to variable types
      attr_reader :types

      # @!attribute [r] factories
      # @return [{Symbol => Class}] mapping of field names to their respective
      #   Variable classes
      attr_reader :factories

      # @!attribute markup
      # @return [Regexp] pattern used to strip markup off values
      attr_accessor :markup

      # Creates a new {Variable} instance using the passed-in field name
      # to distinguish which {Variable} class to use as factory. This
      # method returns nil if the creation fails.
      #
      # @see .create!
      #
      # @example
      #   Variable.create('foo')
      #   #-> #<CiteProc::Variable "foo">
      #
      #   Variable.create('foo', :title)
      #   #-> #<CiteProc::Text "foo">
      #
      #   Variable.create(['Matz', 'Flanagan'], :author)
      #   #-> #<CiteProc::Names "Matz & Flanagan">
      #
      #   Variable.create(2009, :issued)
      #   #-> #<CiteProc::Date "2009-01-01">
      #
      # @param value [Object] the variable's value
      # @param field [Symbol] the value's field name
      #
      # @return [Variable] a new {Variable} (or sub-class) instance
      def create(value, field = nil)
        create!(value, field)
      rescue
        nil
      end


      # Creates a new {Variable} instance using the passed-in field name
      # to distinguish which {Variable} class to use as factory.
      #
      # @see .create
      #
      # @raise [TypeError] if no variable can be created for the given value
      #   and type
      #
      # @param value [Object] the variable's value
      # @param field [Symbol] the variable's field name
      #
      # @return [Variable] a new {Variable} (or sub-class) instance
      def create!(value, field = nil)
        factory = factories[field]
        value.is_a?(factory) ? value : factory.new(value)
      end

    end

    # @!attribute value
    # @return [Object] the value wrapped by this variable
    attr_accessor :value

    def_delegators :@value, :to_s,
      *::String.instance_methods(false).select {|m| m.to_s =~ /!$/ }

    def_delegators :to_s, :=~, :===, *String.instance_methods(false).reject { |m|
      m.to_s =~ /^[\W_]|[!=_]$|^(to_s|inspect|replace|first|last|dup|clone|to_f|to_i)$/
    }


    # Creates new Variable for the passed-in value
    def initialize(value = nil)
      replace(value)
    end

    def initialize_copy(other)
      @value = other.value.dup
    end


    # The replace method is typically called by the Variable's constructor. It
    # will try to set the Variable to the passed in value and should accept
    # a wide range of argument types; subclasses (especially Date and Names)
    # override this method.
    #
    # @raise [TypeError] if the variable cannot be set to the passed-in value
    #
    # @param value [Object] the variable's new value
    # @return [self]
    def replace(value)
      raise TypeError, "failed to set value to #{value.inspect}" unless value.respond_to?(:to_s)
      @value = value.to_s
      self
    end

    # @return [Symbol] the variable's type
    def type
      @type ||= self.class.name.split(/::/)[-1].downcase.to_sym
    end

		# @return [Boolean] whether or not the variable holds a plural value
		def plural?
			if numeric?
				Number.pluralize?(to_s)
			else
				false
			end
		end

    # @return [String, nil] roman equivalent of the variable's numeric value
		def romanize
			return unless numeric?
			Number.romanize(to_i)
		end

		# Tokenizes the variable's value according to the rules of CSL number
		# extraction. Note that this method returns an emtpy array unless
		# the variable has numeric content.
		#
		# @see numeric?
		#
		# For numeric variables, this method normalizes delimiters and
		# separators: numbers separated by a hyphen are stripped of intervening
		# spaces ("2 - 4" becomes "2-4"). Numbers separated by a comma receive
		# one space after the comma ("2,3" and "2 , 3" become "2, 3"), while
		# numbers separated by an ampersand receive one space before and one
		# after the ampsersand ("2&3" becomes "2 & 3").
		#
		# The array returned by this method contains all numbers and tokens
		# as separate strings.
		#
		# @example
		#   Variable.new('2,3').tokenize    #-> ['2', ', ', '3']
		#   Variable.new('2  - 4').tokenize #-> ['2', '-', '4']
		#
    # @return [Array<String>] tokenizes the variable's value
    def tokenize
			return [] unless numeric?
      numbers = to_s.dup

      numbers.gsub!(/\s*,\s*/, ', ')
      numbers.gsub!(/\s*-\s*/, '-')
      numbers.gsub!(/\s*&\s*/, ' & ')

      numbers.split(/(\s*[,&-]\s*)/)
    end
		alias extract_numbers tokenize

		# Tests whether the variable contains numeric content. Content is
		# considered numeric if it solely consists of numbers. Numbers may have
		# prefixes and suffixes ("D2", "2b", "L2d"), and may be separated by a
		# comma, hyphen, or ampersand, with or without spaces ("2, 3", "2-4",
		# "2 & 4"). For example, "2nd" tests "true" whereas "second" and
		# "2nd edition" test "false".
		#
    # @return [Boolean] whether or not the variable's value is numeric
    def numeric?
      !!match(/^[\w\.:;]*\d+[\w\.:;]*(\s*[,&-]\s*[\w\.:;]*\d+[\w\.:;]*)*$/i)
    end

    def date?
      false
    end

    # @return [Fixnum] the first (!) numeric data contained in the variable's
    #   value; zero if no numeric data is present
    def to_i
     to_s =~ /([+-]?\d+)/ && $1.to_i || 0
    end

    # @return [Float] the first (!) numeric or floating point data contained
    #   in the variable's value; zero if no numeric data is present
    def to_f
      to_s =~ /([+-]?\d[\d,\.]*)/ && $1.tr(',','.').to_f || 0.0
    end

    # @return [String] the variable's value stripped of markup
    def strip_markup
      gsub(Variable.markup, '')
    end

    # Strips markup off the variable's value.
    # @return [self]
    def strip_markup!
      gsub!(Variable.markup, '')
    end

    # Compares the variable with the passed-in value. If other responds
    # to {#strip_markup} the stripped strings will be compared; otherwise
    # both objects will be converted to and compared as strings.
    #
    # @param other [Object] the object used for comparison
    # @return [Fixnum,nil] -1, 0, or 1 depending on the result of the
    #   comparison; or nil if the two objects cannot be ignored.
    def <=>(other)
      case
      when other.respond_to?(:strip_markup)
        strip_markup <=> other.strip_markup
      when other && other.respond_to?(:to_s)
        to_s <=> other.to_s
      else
        nil
      end
    end

    # @!method to_s
    # @return [String] the variable's value as a string
    alias to_citeproc to_s

    # @return [String] a JSON string representation of the variable
    def to_json
      ::JSON.dump(to_citeproc)
    end

    # @return [String] a human-readable representation of the variable
    def inspect
      "#<#{self.class.name} #{to_s.inspect}>"
    end

  end

  # A CiteProc Variable used for string values.
  class Text < Variable
  end
end
