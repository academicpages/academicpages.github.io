module CiteProc

  # A {CitationItem} consititues the main input elements to CiteProc's
  # processing methods. In order to be processed correctly, an item must
  # have a valid {#id} attribute used to retrieve the correpsonding {Item}
  # containing the actual bibliographic data.
  class CitationItem

    extend Forwardable
    include Attributes
    include Comparable

    @labels = [
      :book, :chapter, :column, :figure, :folio, :issue, :line, :note, :opus,
      :page, :paragraph, :part, :section, :'sub-verbo', :verse, :volume
    ].freeze

    class << self
      attr_reader :labels
    end

    # @!attribute id
    # @return [Symbol,String] the id of the corresponding resource

    # @!attribute locator
    # @return [String] a string identifying a page number or similar to mark
    #   a location or range within the resource

    # @!attribute label
    # Labels indicate whether the current locator is to a page, a chapter,
    # or other subdivision of the target resource. Valid labels are defined
    # by {.labels}.
    # @return [Symbol,String] the label type

    # @!attribute suppress_author
    # @return [Boolean] whether or not author names will not be included
    #   in the citation output for this cite

    # @!attribute author_only
    # This optional parameter provides a means for certain demanding styles
    # that require the processor output to be divided between the main text
    # and a footnote.
    # @return [Boolean] whether or not only the author name will be included
    #   in the citation output for this cite

    # @!attribute prefix
    # @return [String] a string to print before cites produced for this item

    # @!attribute suffix
    # @return [String] a string to print after cites produced for this item

    attr_predicates :id, :locator, :page, :label, :'suppress-author',
      :'author-only', :prefix, :suffix

    # Attributes added by processor
    attr_predicates :sortkeys, :postion, :'first-reference-note-number',
      :'near-note', :unsorted

    attr_accessor :data

    def_delegators :@data, :suppressed?, :suppress!,
      :language, :english?, :en?

    def initialize(attributes = nil)
      merge(attributes)
      yield self if block_given?
    end

    def initialize_copy(other)
      @attributes = other.attributes.deep_copy
    end

    def <=>(other)
      return unless other.respond_to?(:data)
      data <=> other.data
    end

    # @return [String] a human-readable representation of the citation item
    def inspect
      "#<CiteProc::CitationItem #{[id, locator].compact.map(&:inspect).join(', ')}>"
    end

  end




  class CitationData

    extend Forwardable
    include Enumerable

    @defaults = {
      :footnote => 0
    }.freeze

    @rb2cp = {
      :id => 'citationID',
      :items => 'citationItems',
      :sorted_items => 'sortedItems',
      :footnote => 'noteIndex',
      :options => 'properties'
    }

    @cp2rb = @rb2cp.invert.freeze
    @rb2cp.freeze

    class << self
      attr_reader :defaults, :cp2rb, :rb2cp
    end

    attr_accessor :id

    attr_reader :items, :options, :sorted_items

    alias properties options

    def_delegators :@items, :length, :empty?, :[]

    # Some delegators should return self
    [:push, :<<, :unshift, :concat].each do |m|
      define_method(m) do |*arguments|
        names.send(m, *arguments)
        self
      end
    end

    def initialize(attributes = nil, options = {})
      @options = CitationData.defaults.merge(options)
      @items, @sorted_items = [], []
      merge(attributes)
    end

    def initialize_copy(other)
      @options = other.options.dup
      @items = other.items.map(&:dup)
      @sorted_items = other.items.map(&:dup)
      @id = other.id.dup if other.processed?
    end

    def merge(other)
      return self if other.nil?

      case other
      when String, /^\s*\{/
        other = JSON.parse(other, :symbolize_names => true)
      when Hash
        # do nothing
      when Array
        other = { :items => other }
      when Attributes
        other = other.to_hash
      else
        raise ParseError, "failed to merge citation data and #{other.inspect}"
      end

      other = convert_from_citeproc(other)

      items.concat(Array(other.delete(:items)).map { |i| CitationItem.create!(i) })
      sorted_items.concat(Array(other.delete(:sorted_items)))

      properties = other.delete(:options)
      options.merge!(convert_from_citeproc(Hash[properties])) unless properties.nil?

      @id = other[:id] if other.has_key?(:id)

      self
    end

    alias update merge

    def each(&block)
      if block_given?
        if sorted?
          sorted_items.each(&block)
        else
          items.each(&block)
        end

        self
      else
        to_enum
      end
    end

    def processed?
      !!id
    end

    def sorted?
      !sorted_items.empty?
    end

    def sort!(&block)
      @sorted_items = items.sort(&block)
      self
    end

    def index
      options[:footnote]
    end

    def footnote?
      options[:footnote] > 0
    end

    def to_citeproc
      cp = {}

      cp[CitationData.rb2cp[:items]] = items.map(&:to_citeproc)
      cp[CitationData.rb2cp[:options]] = { CitationData.rb2cp[:footnote] => index }

      cp[CitationData.rb2cp[:id]] = id if processed?

      cp
    end

    def to_json
      ::JSON.dump(to_citeproc)
    end

    alias to_s to_json

    # @return [String] a human-readable representation of the citation data
    def inspect
      "#<CiteProc::CitationData items=[#{length}]>"
    end

    private

    def convert_from_citeproc(hash)
      hash = hash.symbolize_keys

      CitationData.cp2rb.each do |cp, rb|
        cp = cp.to_sym
        hash[rb] = hash.delete(cp) if hash.has_key?(cp)
      end

      hash
    end

  end

end
