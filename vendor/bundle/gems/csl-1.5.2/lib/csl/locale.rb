module CSL
  #
  # CSL::Locales contain locale specific date formatting options, term
  # translations, and a number ordinalizer.
  #
  class Locale < Node
    types << CSL::Info

    include Comparable

    @default = 'en-US'.freeze

    @root = '/usr/local/share/csl/locales'.freeze

    @extension = '.xml'.freeze
    @prefix = 'locales-'.freeze

    @tag_pattern = /^[a-z]{2}(-[A-Z]{2})?|-[A-Z]{2}$/

    # Default languages/regions.
    # Auto-detection is based on these lists.
    @regions = Hash[*%w{
      af ZA bg BG ca AD cs CZ da DK de DE el GR en US es ES et EE fa IR fr FR
      he IL hu HU is IS it IT ja JP km KH ko KR mn MN nb NO nl NL nn NO pl PL
      pt PT ro RO ru RU sk SK sl SI sr RS sv SE th TH tr TR uk UA vi VN zh CN
    }.map(&:to_sym)].freeze

    @languages = @regions.invert.merge(Hash[*%w{
      AT de BR pt CA en CH de GB en TW zh
    }.map(&:to_sym)]).freeze


    class << self
      include Loader

      attr_accessor :default
      attr_reader :languages, :regions

      def load(input = nil)
        input ||= Locale.default
        input = normalize input if input.to_s =~ @tag_pattern
        super(input)
      end

      # Normalizes an IETF tag; adds a language's default region or a
      # region's default language.
      #
      # @example
      #   Locale.normalize("en")  #-> "en-US"
      #   Locale.normalize("-BR") #-> "pt-BR"
      #
      # @raise [ArgumentError] if the passed-in string is no IETF tag
      #
      # @param tag [String] an IETF tag to be normalized
      # @return [String] the normalized IETF tag
      def normalize(tag)
        tag = tag.to_s.strip

        raise ArgumentError, "not a valid IETF tag: #{tag.inspect}" unless
          tag =~ @tag_pattern

        language, region = tag.split(/-/)

        return [language, regions[language.to_sym]].compact.join('-') if region.nil?
        return [languages[region.to_sym], region].join('-') if language.empty?

        tag
      end
    end

    attr_defaults :version => Schema.major_version,
      :xmlns => Schema.namespace

    show_default_attributes!

    attr_struct :xmlns, :version
    attr_children :info, :'style-options', :date, :terms

    has_language

    attr_accessor :region

    alias_child :metadata, :info
    alias_child :dates, :date
    alias_child :options, :style_options

    protected :attributes
    undef_method :[]=

    # @example
    #   Locale.new                                         #-> default
    #   Locale.new('en')                                   #-> American English
    #   Locale.new('en', :'punctuation-in-quote' => false) #-> with style-options
    #   Locale.new(:lang => 'en-GB', :version => '1.0')    #-> British English
    #
    # Returns a new locale. In the first form, the language/regions is set
    # to the default language and region. In the second form the
    # language/region is set by the passed-in IETF tag. The third form
    # additionally accepts a hash of localize style-options. The fourth form
    # is the standard node attribute initialize signature.
    def initialize(*arguments)
      case arguments.length
      when 0
        locale, attributes, options = nil, {}, nil
      when 1
        if arguments[0].is_a?(Hash)
          arguments[0] = arguments[0].symbolize_keys

          locale = arguments[0].delete(:lang) || arguments[0].delete(:'xml:lang')

          attributes, options = arguments
        else
          attributes, locale, options = {}, *arguments
        end
      when 2
        attributes, locale, options = {}, *arguments
      else
        raise ArgumentError, "wrong number of arguments (#{arguments.length} for 0..2)"
      end

      super(attributes, &nil)

      set(locale) unless locale.blank?

      unless options.nil?
        children[:'style-options'] = StyleOptions.new(options)
      end

      yield self if block_given?
    end

    def initialize_copy(other)
      @parent, @ancestors, @descendants, @siblings, @root, @depth = nil
      initialize(other.attributes.to_hash.merge(:lang => other.to_s))
    end

    def added_to(node)
      raise ValidationError, "not allowed to add locale to #{node.nodename}" unless
        node.nodename == 'style'
    end


    def version
      attributes[:version]
    end

    def version=(version)
      raise ArgumentError, "failed to set version to #{version}" unless
        version.respond_to?(:to_s)

      version = version.to_s.strip

      raise ArgumentError, "failed to set version to #{version}: not a version string" unless
        version =~ /^\d[\d\.]+$/

      if version > Schema.version
        warn "setting version to #{version}; latest supported version is #{Schema.version}"
      end

      attributes[:version] = version
    end

    # @return [Boolean] whether or not the Locale's version is less than CSL-Ruby's default version
    def legacy?
      version < Schema.major_version
    end

    # @example
    #   locale.set('en')    #-> sets language to :en, region to :US
    #   locale.set('de-AT') #-> sets language to :de, region to :AT
    #   locale.set('-DE')   #-> sets langauge to :de, region to :DE
    #
    # Sets language and region according to the passed-in locale string. If
    # the region part is not defined by the string, this method will set the
    # region to the default region for the given language.
    #
    # @raise [ArgumentError] if the argument is no valid locale string.
    #   A valid locale string is based on the syntax of IETF language tags;
    #   it consists of either a language or region tag (or both), separated
    #   by a hyphen.
    #
    # @return [self]
    def set(locale)
      @language, @region = Locale.normalize(locale).split(/-/).map(&:to_sym)
      self
    end

    # Sets the locale's language and region to nil.
    # @return [self]
    def clear
      @language, @region = nil
      self
    end

    # @return [String, nil] the term's translation
    def translate(name, options = {})
      return unless has_terms?

      term = terms.lookup name, options
      term && term.to_s(options)
    end
    alias t translate

    # Stores a translation in the locale's term registry.
    # @see Terms#store
    def store(*arguments)
      unless has_terms?
        self << CSL::Locale::Terms.new
      end

      terms.store(*arguments)
      self
    end
    alias learn store

    # Ordinalizes the passed-in number using either the ordinal or
    # long-ordinal forms defined by the locale. If a long-ordinal form is
    # requested but not available, the regular ordinal will be returned
    # instead.
    #
    # @example
    #   Locale.load('en').ordinalize(13)
    #   #-> "13th"
    #
    #   de = Locale.load('de')
    #   de.ordinalize(13)
    #   #-> "13."
    #
    #   de.ordinalize(3, :form => :long, :gender => :feminine)
    #   #-> "dritte"
    #
    # @note
    #   For CSL 1.0 (and older) locales that do not define an "ordinal-00"
    #   term the algorithm specified by CSL 1.0 is used; otherwise uses the
    #   CSL 1.0.1 algorithm with improved support for languages other than
    #   English.
    #
    # @param number [#to_i] the number to ordinalize
    # @param options [Hash] formatting options
    #
    # @option options [:short,:long] :form (:short) which ordinals form to use
    # @option options [:feminine,:masculine,:neutral] :gender (:neutral)
    #   which ordinals gender-form to use
    #
    # @raise [ArgumentError] if number cannot be converted to an integer
    #
    # @return [String] the ordinal for the passed-in number
    def ordinalize(number, options = {})
      raise ArgumentError, "unable to ordinalize #{number}; integer expected" unless
        number.respond_to?(:to_i)

      number = number.to_i
      ordinal = terms.ordinalize number, options

      return number.to_s if ordinal.nil?
      return ordinal.to_s(options) if ordinal.long_ordinal?

      [number, ordinal.to_s(options)].join
    end

    # @return [Boolean] true when the option limit-day-ordinals-to-day-1 is true
    def limit_day_ordinals?
      return false unless has_options? && options.attribute?(:'limit-day-ordinals-to-day-1')
      !!(options[:'limit-day-ordinals-to-day-1'].to_s =~ /^true$/i)
    end

    def limit_day_ordinals!
      unless has_options?
        children[:'style-options'] = StyleOptions.new
      end

      options[:'limit-day-ordinals-to-day-1'] = true
    end

    # @return [Boolean] true when the option punctuation-in-quote is true
    def punctuation_in_quote?
      return false unless has_options? && options.attribute?(:'punctuation-in-quote')
      !!(options[:'punctuation-in-quote'].to_s =~ /^true$/i)
    end
    alias punctuation_in_quotes? punctuation_in_quote?

    def punctuation_in_quote!
      unless has_options?
        children[:'style-options'] = StyleOptions.new
      end

      options[:'punctuation-in-quote'] = true
    end
    alias punctuation_in_quotes! punctuation_in_quote!

    # Puts localized quotes around the passed-in string.
    # @return [String] the quoted string
    def quote(string, escape = false)
      oq, cq = t('open-quote'), t('close-quote')

      return string if oq.nil? || cq.nil? || (oq.empty? && cq.empty?)

      if escape
        oq = CSL.encode_xml_text(oq)
        cq = CSL.encode_xml_text(cq)
      end

      string = replace_with_inner_quotes(string, oq, cq, escape)

      if punctuation_in_quotes?
        "#{oq}#{string}#{cq}"
      else
        string, punctuation = string.split(/([\.,])$/, 2)

        "#{oq}#{string}#{cq}#{punctuation}"
      end
    end

    def replace_with_inner_quotes(string, open, close, escape = false)
      oq, cq = t('open-inner-quote'), t('close-inner-quote')

      return string if oq.nil? || cq.nil? || (oq.empty? && cq.empty?)

      if escape
        oq = CSL.encode_xml_text(oq)
        cq = CSL.encode_xml_text(cq)
      end

      string.gsub(/(#{open}|"\b)/, oq).gsub(/(#{close}|\b")/, cq)
    end

    # @example
    #   locale.each_term { |term| block } #-> locale
    #   locale.each_term                  #-> enumerator
    #
    # Calls block once for each term defined by the locale. If no block is
    # given, an enumerator is returned instead.
    def each_term(&block)
      if block_given?
        terms.each(&block)
        self
      else
        enum_for :each_term
      end
    end

    # @example
    #   locale.each_date { |date_format| block } #-> locale
    #   locale.each_date                         #-> enumerator
    #
    # Calls block once for each date format defined by the locale. If no
    # block is given, an enumerator is returned instead.
    def each_date(&block)
      if block_given?
        if date.is_a? CSL::Node
          yield date
        else
          date.each(&block)
        end
      else
        enum_for :each_date
      end
    end

    # @returns [Boolean] whether or not the Locale is the default locale
    def default?
      to_s == Locale.default
    end

    # @return [Boolean] whehter or not the Locale's region is the default
    #   region for its language
    def default_region?
      region && region == Locale.regions[language]
    end

    # @return [Boolean] whether or not the Locale's language is the default
    #   language for its region
    def default_language?
      language && language == Locale.languages[region]
    end

    def like?(other)
      return false unless other.is_a? Locale
      return true  if other.universal?

      language == other.language
    end

    def universal?
      language.nil?
    end

    def validate
      Schema.validate self
    end

    def valid?
      validate.empty?
    end

    # @return [Locale]
    def merge(*others)
      deep_copy.merge!(*others)
    end

    # @return [self]
    def merge!(*others)
      others.each do |other|
        merge_options other
        merge_dates other
        merge_terms other
      end

      self
    end

    def reverse_merge(other)
      other.merge(self)
    end


    # Locales are sorted first by language, then by region; sort order is
    # alphabetical with the following exceptions: the default locale is
    # prioritised; in case of a language match the default region of that
    # language will be prioritised (e.g., de-DE will come before de-AT even
    # though the alphabetical order would be different).
    #
    # @param other [Locale] the locale used for comparison
    # @return [1,0,-1,nil] the result of the comparison
    def <=>(other)
      case
      when !other.is_a?(Locale)
        nil
      when [language, region] == [other.language, other.region]
        0
      when default?
        -1
      when other.default?
        1
      when language == other.language
        case
        when default_region?
          -1
        when other.default_region?
          1
        else
          region.to_s <=> other.region.to_s
        end
      else
        language.to_s <=> other.language.to_s
      end
    end

    # @return [String] the Locale's IETF tag
    def to_s
      [language, region].compact.join('-')
    end

    # @return [String] a string representation of the Locale
    def inspect
      "#<#{self.class.name} #{to_s}>"
    end

    private

    alias original_locale_attribute_assignments attribute_assignments

    def attribute_assignments
      if root?
        original_locale_attribute_assignments
      else
        'xml:lang="%s"' % to_s
      end
    end

    def preamble
      Schema.preamble.dup
    end

    # @param other [Locale] an other locale whose options should be merged
    # @return [self]
    def merge_options(other)
      return self unless other.has_options?

      if has_options?
        options.attributes.merge! other.options.attributes
      else
        add_child other.options.dup
      end

      self
    end

    # @param other [Locale] an other locale whose date nodes should be merged
    # @return [self]
    def merge_dates(other)
      return self unless other.has_dates?

      if has_dates?
        other.each_date do |date|
          delete_children(*each_date.select { |d| d[:form] == date[:form] })
          add_child date.deep_copy
        end
      else
        other.each_date do |date|
          add_child date.deep_copy
        end
      end

      self
    end

    def merge_terms(other)
      return self unless other.has_terms?

      other.each_term do |term|
        store term.deep_copy
      end

      self
    end
  end

end
