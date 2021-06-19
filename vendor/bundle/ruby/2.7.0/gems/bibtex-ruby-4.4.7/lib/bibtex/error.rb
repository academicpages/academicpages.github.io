module BibTeX

	class BibTeXError < StandardError
		attr_reader :original

		def initialize(message = nil, original = $!)
			super(message)
			@original = original
		end
	end

  class ParseError < BibTeXError; end
  class ArgumentError < BibTeXError; end

  #
  # Represents a lexical or syntactical error.
  #
  class Error < Element

    attr_reader :trace

    def initialize(trace=[])
      @trace = trace
    end

    def trace=(trace)
      raise(ArgumentError, "BibTeX::Error trace must be of type Array; was: #{trace.class.name}.") unless trace.kind_of?(Array)
      @trace = trace
    end

    def content
      @trace.map { |e| e[1] }.join
    end

    # Called when the element was added to a bibliography.
    def added_to_bibliography(bibliography)
      super(bibliography)
      bibliography.errors << self
      self
    end

    # Called when the element was removed from a bibliography.
    def removed_from_bibliography(bibliography)
      super(bibliography)
      bibliography.errors.delete(self)
      self
    end
  end
end
