module CiteProc

  # Items are similar to a Ruby Hash but pose a number of constraints on their
  # contents: keys are always (implicitly converted to) symbols and values
  # are strictly {Variable Variables}. When Items are constructed
  # from (or merged with) JSON objects or Hashes {Variable} instances are
  # automatically created by passing the variable's key as type to
  # {Variable.create}; this will create the expected {Variable} type for all
  # fields defined in CSL (for example, the `issued' field will become a
  # {Date} object; unknown types will be converted to simple {Variable}
  # instances, which should be fine for numeric or string values but may
  # cause problems for more complex types.
  #
  # Every Item provides accessor methods for all known field names; unknown
  # fields can still be accessed using array accessor syntax.
  #
  #     i = Item.new(:edition => 3, :unknown_field => 42)
  #     i.edition
  #     #-> #<CiteProc::Number "3">
  #
  #     i[:unknown_field]
  #     #-> #<CiteProc::Variable "42">
  #
  # Items can be converted to the CiteProc JSON format via {#to_citeproc}
  # and {#to_json}.
  class Item

    @types = [
      :article, :'article-journal', :'article-magazine', :'article-newspaper',
      :bill, :book, :broadcast, :chapter, :entry, :'entry-dictionary',
      :'entry-encyclopedia', :figure, :graphic, :interview, :legal_case,
      :legislation, :manuscript, :map, :motion_picture, :musical_score,
      :pamphlet, :'paper-conference', :patent, :personal_communication, :post,
      :'post-weblog', :report, :review, :'review-book', :song, :speech,
      :thesis, :treaty, :webpage].freeze

    @bibtex_types = Hash.new { |h,k| :misc }.merge(Hash[*%w{
      pamphlet          booklet
      paper-conference  conference
      chapter           inbook
      chapter           incollection
      paper-conference  inproceedings
      book              manual
      thesis            phdthesis
      paper-conference  proceedings
      report            techreport
      manuscript        unpublished
      article           article
      article-journal   article
      article-magazine  article
    }.map(&:intern)]).freeze

    class << self
      attr_reader :types, :bibtex_types
    end

    extend Forwardable

    include Attributes
    include Enumerable
    include Comparable
    include Observable


    attr_predicates :id, :'short-title', :'journal-abbreviation',
      :type, *Variable.fields[:all]

    def_delegators :attributes, :values_at, :keys, :values

    alias fields keys

    # Hide attributes reader:
    # All access should go through (read|write)_attribute
    protected :attributes


    def initialize(attributes = nil)
      merge(attributes)
      yield self if block_given?
    end

    def initialize_copy(other)
      @attributes = other.attributes.deep_copy
    end


    # Returns a CitationItem with a copy of this item
    # attached as data.
    #
    # If given, number is added as the item's
    # citation-number variable.
    #
    # @param number [Fixnum] the item's citation-number
    # @return [CitationItem] a citation item for this item
    def cite(number = nil)
      CitationItem.new :id => id do |c|
        c.data = dup
        c.data[:'citation-number'] = number unless number.nil?
      end
    end

    def observable_read_attribute(key)
      value = original_read_attribute(key)
      return if suppressed?(key)
      value
    ensure
      changed
      notify_observers :read, key, value
    end

    def simulate_read_attribute(key, value)
      changed
      notify_observers :read, key, value
    end

    alias original_read_attribute read_attribute
    alias unobservable_read_attribute read_attribute

    alias read_attribute observable_read_attribute

    # Update [] alias!
    alias [] read_attribute

    # @param name [Symbol] the name of the variable
    #
    # @param options [Hash]
    # @option options [:short] :form (nil) when given, the variable's
    #   short form will be returned if available.
    #
    # @return [Variable, nil] the matching variable
    def variable(name, options = {})
      if options.key?(:form) && options[:form].to_sym == :short
        var = read_attribute "#{name}-short"
        return var unless var.nil?
      end

      read_attribute name
    end

    def language
      unobservable_read_attribute(:language)
    end

    # An Item is interpreted as being English unless it has
    # an attribute 'language' set to something other than 'en'.
    #
    # @return [Boolean] whether or not this is an English Item
    def english?
      lang = language
      lang.nil? || lang == 'en'
    end
    alias en? english?

    # Calls a block once for each field in the item, passing the field's
    # name-value pair as parameters.
    #
    # If not block is given, an enumerator is returned instead.
    #
    #    item.each { |name, value| block }
    #    #-> item
    #
    #    item.each
    #    #-> an enumerator
    #
    # @yieldparam field [Symbol] the field name
    # @yieldparam value [Variable] the value
    # @return [self,Enumerator] the item or an enumerator if no block is given
    def each(&block)
      if block_given?
        attributes.each_pair(&block)
        self
      else
        to_enum
      end
    end
    alias each_pair each

    # Calls a block once for each field in the item, passing the field's
    # value as parameters.
    #
    # If not block is given, an enumerator is returned instead.
    #
    #    item.each_value { |value| block }
    #    #-> item
    #
    #    item.each_value
    #    #-> an enumerator
    #
    # @yieldparam value [Variable] the value
    # @return [self,Enumerator] the item or an enumerator if no block is given
    def each_value(&block)
      if block_given?
        attributes.each_value(&block)
        self
      else
        enum_for :each_value
      end
    end

    def suppressed?(key)
      suppressed.include?(key.to_s)
    end

    def suppress!(*keys)
      keys.flatten.each do |key|
        suppressed << key.to_s
      end

      suppressed.sort!
      suppressed.uniq!

      self
    end

    def suppressed
      @suppressed ||= []
    end

    def ==(other)
      return false unless other.is_a?(Item)
      id == other.id
    end

    def <=>(other)
      return nil unless other.is_a?(Attributes)
      eql?(other) ? 0 : length <=> other.length
    end

    # Returns a corresponding *BibTeX::Entry* if the bibtex-ruby gem is
    # installed; otherwise returns a BibTeX string.
    def to_bibtex
      # hash = to_hash
      #
      # hash[:type] = Item.bibtex_types[hash[:type]]
      #
      # if hash.has_key?(:issued)
      #   date = hash.delete(:issued)
      #   hash[:year] = date.year
      #   hash[:month] = date.month
      # end
      #
      # Variable.fields[:date].each do |field|
      #   hash[field] = hash[field].to_s if hash.has_key?(field)
      # end
      #
      # Variable.fields[:names].each do |field|
      #   hash[field] = hash[field].to_bibtex
      # end

      raise 'not implemented yet'
    end

    # @return [Symbol,nil] the item's id
    def to_sym
      if id?
        id.to_s.intern
      else
        nil
      end
    end

    # @return [String] a string containing a human-readable
    #   representation of the item
    def inspect
      "#<CiteProc::Item id=#{id.to_s.inspect} attributes={#{attributes.length}}>"
    end

    private

    # @private
    def filter_value(value, key = nil)
      Variable.create!(value, key)
    end
  end

end
