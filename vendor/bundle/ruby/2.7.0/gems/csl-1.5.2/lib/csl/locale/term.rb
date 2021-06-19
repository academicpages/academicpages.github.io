module CSL
  class Locale

    class Terms < Node
      attr_children :term

      alias terms term
      def_delegators :terms, :size, :length

      undef_method :[]=

      def initialize(attributes = {})
        super(attributes)
        children[:term] = []

        @registry = Term::Registry.new
        @ordinals = Term::Registry.new

        yield self if block_given?
      end

      alias each each_child

      # @example
      #   terms.store(term)
      #   terms.store('book', ['book', 'books'])
      #   terms.store('book', 'bk', :form => 'short')
      #
      # Shorthand method to stores a new term translations.
      #
      # @param [Term, String] the term; or the the term's name
      # @param [String] the term's translation
      # @param [Hash] additional term attributes
      #
      # @return [self]
      def store(term, translation = nil, options = nil)
        unless term.is_a?(Term)
          term = Term.new(:name => term)
          term.attributes.merge(options) unless options.nil?
          term.set(*translation)
        end

        self << term
      end

      # If a style uses a term in a form that is undefined, there is a
      # fallback to other forms: "verb-short" first falls back to "verb",
      # "symbol" first falls back to "short", and "verb" and "short" both
      # fall back to "long". If no form fallback is available, nil is
      # returned instead.
      #
      # @return [Term, nil] the term that matches the query
      def lookup(name, options = {})
        options = Term.specialize(options)

        options[:name] = name = name.to_s
        options[:form] = 'long' unless options.key?(:form)

        # NB: currently only ordinals support gender-forms
        options.delete(:'gender-form')

        candidates = registry[name]
        return if candidates.empty?

        # loop terminates when a matching term is found or
        # when there are no more form fallbacks left
        while true do
          term = candidates.detect { |t| t.match?(options) }
          return term unless term.nil?

          fallback = Term.form_fallbacks[options[:form].to_s]
          return if fallback == options[:form]

          options[:form] = fallback
        end
      end
      alias [] lookup

      def ordinalize(number, options = {})
        return unless has_ordinals?

        options = Term.specialize(options)
        number = number.to_i.abs

        # try to match long-ordinals first
        if options.delete(:form).to_s =~ /^long/i
          ordinal = lookup_long_ordinal_for number, options
          return ordinal unless ordinal.nil?
        end

        # select CSL 1.0 or 1.0.1 algorithm
        algorithm = ordinalizer

        ordinal = send algorithm, number, options
        return ordinal unless ordinal.nil?

        # fallback to non-gendered version
        if options.delete(:'gender-form')
          ordinal = send algorithm, number, options
        end

        ordinal
      end

      def ordinalizer
        if has_legacy_ordinals?
          :lookup_legacy_ordinals_for
        else
          :lookup_ordinals_for
        end
      end

      def lookup_long_ordinal_for(number, options = {})
        ordinals[number].detect { |t| t.long_ordinal? && t.match?(options) }
      end

      def lookup_ordinals_for(number, options = {})
        ordinal = lookup_ordinal_for(number, nil, options)
        return ordinal unless ordinal.nil?

        unless number < 100
          ordinal = lookup_ordinal_for(number, 100, options)
          return ordinal unless ordinal.nil?
        end

        unless number < 10
          ordinal = lookup_ordinal_for(number, 10, options)
          return ordinal unless ordinal.nil?
        end

        default_ordinals.detect { |t| t.match?(options) }
      end

      def lookup_ordinal_for(number, divisor, options = {})
        modulus = divisor ? (number % divisor) : number
        ordinals[modulus].detect do |t|
          t.short_ordinal? && t.match?(options) && t.match_modulo?(number)
        end
      end

      def lookup_legacy_ordinals_for(number, options = {})
        case
        when (11..13).include?(number.abs % 100)
          ordinals[4].detect { |t| t.match?(options) }
        when (1..3).include?(number.abs % 10)
          ordinals[number.abs % 10].detect { |t| t.match?(options) }
        else
          ordinals[4].detect { |t| t.match?(options) }
        end
      end

      # @return [Boolean] whether or not regular terms are registered at this node
      def has_terms?
        !registry.empty?
      end

      # @return [Boolean] whether or not ordinal terms are registered at this node
      def has_ordinals?
        !ordinals.empty?
      end

      def has_legacy_ordinals?
        has_ordinals? && !ordinals.key?(:default)
      end

      def default_ordinals
        ordinals[:default]
      end

      def drop_ordinals
        tmp = ordinals.values.flatten(1)
        ordinals.clear
        delete_children tmp
      end

      protected

      # @!attribute [r] registry
      # @return [Hash] a private registry to map term names to the respective
      #   term objects for quick term look-up
      attr_reader :registry

      # @!attribute [r] ordinals
      # @return [Hash] a private registry to map ordinals to the respective
      #   term objects for quick ordinal look-up
      attr_reader :ordinals

      private

      def added_child(term)
        raise ValidationError, "failed to register term #{term.inspect}: name attribute missing" unless
          term.attribute?(:name)

        if term.ordinal?
          store = ordinals[term.ordinal]
        else
          store = registry[term[:name]]
        end

        delete_children store.select { |value| term.exact_match? value }

        store.push(term)

        term
      end

      def deleted_child(term)
        if term.ordinal?
          ordinals[term.ordinal].delete(term)
        else
          registry[term[:name]].delete(term)
        end
      end

    end

    class Term < Node
      attr_struct :name, :form, :gender, :'gender-form', :match
      attr_children :single, :multiple

      attr_defaults :form => 'long'

      attr_accessor :text

      def_delegators :attributes, :hash, :eql?, :name, :form, :gender

      @form_fallbacks = {
        'long'       => 'long',
        'verb'       => 'long',
        'short'      => 'long',
        'verb-short' => 'verb',
        'symbol'     => 'short'
      }.freeze

      class << self

        attr_reader :form_fallbacks

        def specialize(options)
          specialized = {}

          options.each do |key, value|
            key = key.to_sym

            if !value.nil? && Term::Attributes.keys.include?(key)
              specialized[key] = value
            end
          end

          specialized.delete :'gender-form' unless
            specialized[:'gender-form'].to_s =~ /^masculine|feminine$/

          specialized
        end

      end

      # This method returns whether or not the ordinal term matchs the
      # passed-in modulus. This is determined by the ordinal term's match
      # attribute: a value of 'last-two-digits' matches a modulus of 100,
      # 'last-digit' matches a modulus of 10 and 'whole-number' matches
      # only if the number is identical to the ordinal value.
      #
      # If the term is no ordinal term, this methods always returns false.
      #
      # @return [Boolean] whether or not the ordinal term matches the
      #   passed-in number.
      def match_modulo?(number)
        return false unless ordinal?

        case attributes.match
        when 'last-two-digits'
          ordinal == number % 100
        when 'last-digit'
          ordinal == number % 10
        when 'whole-number'
          ordinal == number
        else
          true
        end
      end
      alias matches_modulo? match_modulo?

      # @return [Boolean] whether or not this term is an ordinal term
      def ordinal?
        /^(long-)?ordinal(-\d\d+)?$/ === attributes.name
      end

      # @return [Boolean] whether or not this term is a long-ordinal term
      def long_ordinal?
        /^long-ordinal(-\d\d+)?$/ === attributes.name
      end

      # @return [Boolean] whether or not this term is a regular ordinal term
      def short_ordinal?
        /^ordinal(-\d\d+)?$/ === attributes.name
      end

      def default_ordinal?
        attributes.name == 'ordinal'
      end

      # @return [Fixnum, :default, nil]
      def ordinal
        return unless ordinal?
        return :default if attributes.name == 'ordinal'
        attributes.name[/\d+/].to_i
      end

      def gendered?
        !attributes.gender.blank?
      end

      def neutral?
        !gendered?
      end

      def short?
        attribute?(:form) && attributes.form.to_s =~ /^short$/i
      end

      def verb?
        attribute?(:form) && attributes.form.to_s =~ /^verb$/i
      end

      def verb_short?
        attribute?(:form) && attributes.form.to_s =~ /^verb-short$/i
      end

      def symbol?
        attribute?(:form) && attributes.form.to_s =~ /^symbol$/i
      end

      def long?
        return true unless attribute?(:form)
        attributes.form.to_s =~ /^long$/i
      end

      def textnode?
        !text.blank?
      end

      def singularize
        return text if textnode?
        children.single.to_s
      end

      alias singular singularize

      def pluralize
        return text if textnode?
        children.multiple.to_s
      end

      alias plural pluralize

      alias singular= single=
      alias plural= multiple=

      def set(singular, plural = nil)
        if plural.nil?
          self.text = singular
        else
          self.single = singular
          self.multiple = plural
        end

        self
      end


      # @!method masculine?
      # @return [Boolean] whether or not the term is masculine

      # @!method masculine!
      # @return [self,nil] the term with the gender attribute set to
      #   'masculine', or nil if the term was already masculine

      # @!method feminine?
      # @return [Boolean] whether or not the term is feminie

      # @!method feminine!
      # @return [self,nil] the term with the gender attribute set to
      #   'feminine', or nil if the term was already feminine
      %w{ masculine feminine }.each do |name|
        define_method("#{name}?") do
          attributes.gender.to_s == name
        end

        define_method("#{name}!") do
          return nil if attributes.gender.to_s == name
          attributes.gender = name
          self
        end
      end

      def tags
        if textnode?
          [
            "<#{[nodename, *attribute_assignments].join(' ')}>",
            CSL.encode_xml_text(text),
            "</#{nodename}>"
          ]
        else
          super
        end
      end

      # @param options [Hash,nil] an optional configuration hash
      #
      # @option options [:singular,:plural] :number (:singular) whether to
      #   return the term's singular or plural variant.
      # @option options [Boolean] :plural (false) whether or not to return
      #   the term's plural variant (this option, if set, takes precedence
      #   over :number).
      #
      # @return [String] the term as a string
      def to_s(options = nil)
        if textnode?
          text
        else
          if pluralize?(options)
            pluralize
          else
            singularize
          end
        end
      end

      class Single   < TextNode; end
      class Multiple < TextNode; end

      private

      def pluralize?(options)
        return false if options.nil?

        case
        when options.key?(:plural) || options.key?('plural')
          options[:plural] || options['plural']
        when options.key?(:number) || options.key?('number')
          key = options[:number] || options['number']

          if key.is_a?(Integer) || key.to_s =~ /^[+-]?\d+$/
            key.to_i > 1
          else
            !key.blank? && key.to_s =~ /^plural/i
          end
        else
          false
        end
      end

      class Registry < ::Hash
        def initialize
          super { |h,k| h[k] = [] }
        end
      end
    end

    TextNode.types << Term
  end
end
