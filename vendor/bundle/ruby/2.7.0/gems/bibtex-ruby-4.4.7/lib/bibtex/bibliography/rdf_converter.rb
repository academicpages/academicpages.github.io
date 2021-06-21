class BibTeX::Bibliography::RDFConverter
  # converts a BibTeX Bibliography to RDF
  # @return [RDF::Graph] the RDF graph of the bibliography
  def self.convert(bibtex)
    new(bibtex).convert!
  end

  # @param [BibTeX::Entry] the bibliography to convert
  def initialize(bibtex, graph = RDF::Graph.new)
    @bibtex = bibtex
    @graph = graph
    @agent = {}
  end

  # @return [RDF::Graph] the RDF graph of this bibliography
  def convert!
    bibtex.q('@entry').each do |entry|
      BibTeX::Entry::RDFConverter.convert(entry, graph, agent)
    end

    graph
  end

  protected

  attr_reader :bibtex, :graph, :agent
end
