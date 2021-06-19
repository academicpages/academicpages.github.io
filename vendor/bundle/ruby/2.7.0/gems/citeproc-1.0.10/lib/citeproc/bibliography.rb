module CiteProc

  # Typically a {Bibliography} is returned by a {Processor} instance. It
  # contains a list of references and formatting options.
  #
  # A Bibliography can be created from (and exported to) CiteProc JSON
  # bibliographies; these consist of a two-element list, composed of a
  # JavaScript array containing certain formatting parameters, and a list of
  # strings representing bibliography entries.
  #
  # See {.defaults} for the default formatting options.
  class Bibliography

    @defaults = {
      :offset => 0,
      :'entry-spacing' => 1,
      :'line-spacing' => 1,
      :'hanging-indent' => false,
      :'second-field-align' => false
    }.freeze


    # citeproc-js and csl attributes are often inconsistent or difficult
    # to use as symbols/method names, so we're using different names at the
    # cost of making conversion to and from the json format more difficult

    @cp2rb = {
      'maxoffset' => :offset,
      'entryspacing' => :'entry-spacing',
      'linespacing' => :'line-spacing',
      'hangingindent' => :'hanging-indent',
      'second-field-align' => :'second-field-align'
    }

    @rb2cp = @cp2rb.invert.freeze
    @cp2rb.freeze

    class << self

      # @!attribute [r] defaults
      # @example Default Formatting Options
      #   {
      #     :offset => 0,
      #     # Some citation styles apply a label (either a number or an
      #     # alphanumeric code) to each bibliography entry, and use this
      #     # label to cite bibliography items in the main text. In the
      #     # bibliography, the labels may either be hung in the margin,
      #     # or they may be set flush to the margin, with the citations
      #     # indented by a uniform amount to the right. In the latter case,
      #     # the amount of indentation needed depends on the  maximum width
      #     # of any label. The :offset option gives the maximum number of
      #     # characters that appear in any label used in the bibliography.
      #     # The client that controls the final rendering of the bibliography
      #     # string should use this value to calculate and apply a suitable
      #     # indentation length.
      #
      #     :'entry-spacing' => 1,
      #     # An integer representing the spacing between entries in the
      #     # bibliography.
      #
      #     :'line-spacing' => 1,
      #     # An integer representing the spacing between the lines within
      #     # each bibliography entry.
      #
      #     :'hanging-indent' => false,
      #
      #     :'second-field-align' => false
      #     # When the second-field-align CSL option is set, this returns
      #     # either "flush" or "margin". The calling application should
      #     # align text in the bibliography output as described by the CSL
      #     # specification. Where second-field-align is not set, this
      #     # return value is set to false.
      #   }
      # @return [Hash] default formatting options
      attr_reader :defaults

      attr_reader :cp2rb, :rb2cp

      # Create a new Bibliography from the passed-in string or array, or nil
      # if the input cannot be parsed.
      def create(input, &block)
        create!(input, &block)
      rescue
        nil
      end

      # Create a new Bibliography from the passed-in string or array. Raises
      # ParseError if the input cannot be parsed.
      def create!(input)
        case
        when input.is_a?(String)
          create!(::JSON.parse(input))

        when input.is_a?(Hash)
          create!([input])

        when input.is_a?(Array) && input.length == 2
          options, references = input

          new do |b|
            b.references.concat(references)
            b.ids.concat(options.fetch('entry_ids', []))
            b.errors.concat(options.fetch('bibliography_errors', []))

            b.header, b.footer = options['bibstart'], options['bibend']

            (options.keys & cp2rb.keys).each do |k|
              b.options[cp2rb[k]] = options[k]
            end

            yield b if block_given?
          end

        else
          raise ParseError, "failed to create Bibliography from #{input.inspect}"
        end
      end

    end

    include Comparable
    include Enumerable

    extend Forwardable

    # @!attribute [r] refrences
    # @return [Array<String>] the list of references
    attr_reader :references

    attr_reader :ids

    # @!attribute [r] options
    # @see .defaults
    # @return [Hash] the current formatting options
    attr_reader :options

    # @!attribute [r] errors
    # @return [Array<String>] a list of errors
    attr_reader :errors

    # @!attribute header
    # @return [String] content included before the reference list
    attr_accessor :header

    # @!attribute footer
    # @return [String] content included after the reference list
    attr_accessor :footer

    # @!attribute prefix
    # @return [String] content included before each reference
    attr_accessor :prefix

    # @!attribute suffix
    # @return [String] content included after each reference
    attr_accessor :suffix

    # Bibliographies quack sorta like an Array
    def_delegators :@references, :length, :empty?

    attr_accessor :connector

    def initialize(options = {})
      @options = Bibliography.defaults.merge(options)
      @errors, @references, @ids, @connector = [], [], [], "\n"

      yield self if block_given?
    end

    def initialize_copy(other)
      @options, @connector = other.options.dup, other.connector.dup
      @errors, @references, @ids = other.errors.dup, other.references.dup, other.ids.dup
    end

    def push(id, reference)
      ids << id
      references << reference
      self
    end
    alias << push

    def has_errors?
      !errors.empty?
    end

    alias errors? has_errors?

    def entry_spacing
      options[:'entry-spacing'].to_f
    end

    def line_spacing
      options[:'line-spacing'].to_f
    end

    def hanging_indent?
      options[:'hanging_indent']
    end

    def join()
      [
        header,

        references.map { |r|
          [prefix, r, suffix].compact.join('')
        }.join(connector),

        footer
      ].compact.join(connector)
    end

    def to_s
      join
    end

    def each(&block)
      if block_given?
        references.each(&block)
        self
      else
        to_enum
      end
    end

    def <=>(other)
      return nil unless other.respond_to?(:references)
      references <=> other.references
    end

    def citeproc_options
      Hash[*options.map { |k,v|
          [Bibliography.rb2cp[k] || k.to_s, v]
        }.flatten]
    end

    def to_citeproc
      [
        citeproc_options.merge({
          'bibstart' => prefix,
          'bibend' => suffix,
          'bibliography_errors' => errors
        }),

        references

      ]
    end

    def to_json
      ::JSON.dump(to_citeproc)
    end

    # @return [String] a human-readable representation of the bibliography
    def inspect
      "#<CiteProc::Bibliography @references=[#{references.length}], @errors=[#{errors.length}]>"
    end

  end

end
