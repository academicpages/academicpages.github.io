require 'uri/common'

begin
  require 'rdf/vocab'
rescue LoadError
  ::RDF::Vocab = RDF # support RDF on Ruby 1.9
end

class BibTeX::Entry::RDFConverter
  DEFAULT_REMOVE_FROM_FALLBACK = %w[
    bdsk-file-1
    bdsk-file-2
    bdsk-file-3
    bdsk-file-4
  ].map(&:intern).freeze

  BIBO_TYPES = Hash[*%w[
    article Article
    book Book
    booklet Book
    collection Collection
    conference AcademicArticle
    inbook BookSection
    incollection BookSection
    inproceedings AcademicArticle
    journal Journal
    manual Manual
    mastersthesis Thesis
    online Website
    patent Patent
    periodical Periodical
    phdthesis Thesis
    proceedings Proceedings
    standard Standard
    techreport Report
    thesis Thesis
    unpublished Manuscript
  ].map(&:intern)].freeze

  # converts a BibTeX entry to RDF
  # @return [RDF::Graph] the RDF graph of this entry
  def self.convert(bibtex, graph = RDF::Graph.new, agent = {})
    new(bibtex, graph, agent).convert!
  end

  # @param [BibTeX::Entry] the entry to convert
  def initialize(bibtex, graph = RDF::Graph.new, agent = {})
    @bibtex = bibtex
    @graph = graph
    @agent = agent
  end

  # @return [RDF::Graph] the RDF graph of this entry
  def convert!
    bibtex.parse_names
    bibtex.parse_month

    unless uri_in_graph?(entry)
      methods = self.class.instance_methods(false) - [:convert!]
      methods.each { |m| send(m) }
      run_fallback
    end

    graph
  end

  def abstract
    return unless bibtex.field?(:abstract)

    remove_from_fallback(:abstract)

    graph << [entry, RDF::Vocab::DC.abstract, bibtex[:abstract].to_s]
    graph << [entry, bibo[:abstract], bibtex[:abstract].to_s]
  end

  def annote
    return unless bibtex.field?(:annote)

    remove_from_fallback(:annote)

    pub = RDF::Node.new
    graph << [pub, RDF.type, bibo[:Note]]
    graph << [pub, bibo[:content], bibtex[:annote]]

    graph << [entry, bibo[:annotates], pub]
  end

  def author
    return unless bibtex.field?(:author)

    remove_from_fallback(:author)

    seq = RDF::Node.new

    graph << [seq, RDF.type, RDF[:Seq]]
    graph << [entry, bibo[:authorList], seq]

    bibtex[:author].each do |name|
      node = agent(name) { create_agent(name, :Person) }

      graph << [entry, RDF::Vocab::DC.creator, node]
      graph << [seq, RDF.li, node]
    end
  end

  def bdsk_url
    count = 1
    while bibtex.field?("bdsk-url-#{count}".to_sym)
      field = "bdsk-url-#{count}".to_sym
      remove_from_fallback(field)
      graph << [entry, RDF::Vocab::DC.URI, bibtex[field].to_s]
      graph << [entry, bibo[:uri], bibtex[field].to_s]
      count += 1
    end
  end

  def booktitle
    return unless bibtex.field?(:booktitle)

    remove_from_fallback(:booktitle)
    return if bibtex.has_parent? &&
              bibtex.parent[:title] == bibtex[:booktitle]
    return if bibtex.has_parent? &&
              bibtex.parent[:booktitle] == bibtex[:booktitle]
    return if bibtex.has_parent? &&
              bibtex.parent[:isbn] == bibtex[:isbn]
    return if bibtex[:title] == bibtex[:booktitle]

    series = RDF::Node.new
    graph << [series, RDF.type, bibo[:Document]]
    graph << [series, RDF::Vocab::DC.title, bibtex[:booktitle].to_s]

    graph << [entry, RDF::Vocab::DC.isPartOf, series]
  end

  def chapter
    return unless bibtex.field?(:chapter)

    remove_from_fallback(:chapter)

    graph << [entry, bibo[:chapter], bibtex[:chapter].to_s]
  end

  def children
    return unless bibtex.has_children?

    bibtex.children.each do |child|
      child_id = RDF::URI.new(child.identifier)
      BibTeX::Entry::RDFConverter.new(child, graph, agent).convert! unless uri_in_graph?(child_id)
      graph << [entry, RDF::Vocab::DC.hasPart, child_id]
    end
  end

  def copyright
    return unless bibtex.field?(:copyright)

    remove_from_fallback(:copyright)

    graph << [entry, RDF::Vocab::DC.rightsHolder, bibtex[:copyright].to_s]
  end

  def date_added
    return unless bibtex.field?(:'date-added')

    remove_from_fallback(:'date-added')

    graph << [entry, RDF::Vocab::DC.created, bibtex[:'date-added'].to_s]
  end

  def date_modified
    return unless bibtex.field?(:'date-modified')

    remove_from_fallback(:'date-modified')

    graph << [entry, RDF::Vocab::DC.modified, bibtex[:'date-modified'].to_s]
  end

  def doi
    return unless bibtex.field?(:doi)

    remove_from_fallback(:doi)

    graph << [entry, bibo[:doi], bibtex[:doi].to_s]
    graph << [entry, RDF::Vocab::DC.identifier, "doi:#{bibtex[:doi]}"]
  end

  def edition
    return unless bibtex.field?(:edition)

    remove_from_fallback(:edition)

    graph << [entry, bibo[:edition], bibtex[:edition].to_s]
  end

  def editor
    return unless bibtex.field?(:editor)

    remove_from_fallback(:editor)

    seq = RDF::Node.new

    graph << [seq, RDF.type, RDF[:Seq]]
    graph << [entry, bibo[:editorList], seq]

    bibtex[:editor].each do |name|
      node = agent(name) { create_agent(name, :Person) }

      graph << [entry, bibo.name, node]
      graph << [seq, RDF.li, node]
    end
  end

  def fallback_default
    remove_from_fallback(*DEFAULT_REMOVE_FROM_FALLBACK)
  end

  def howpublished
    return unless bibtex.field?(:howpublished)
    return unless bibtex[:howpublished] =~ /^#{URI::DEFAULT_PARSER.make_regexp}$/

    remove_from_fallback(:howpublished)

    graph << [entry, RDF::Vocab::DC.URI, bibtex[:howpublished].to_s]
    graph << [entry, bibo[:uri], bibtex[:howpublished].to_s]
  end

  def institution
    return unless bibtex.field?(:institution)

    remove_from_fallback(:institution)

    org = agent(bibtex[:institution].to_s) { create_agent(bibtex[:institution].to_s, :Organization) }

    graph << [entry, RDF::Vocab::DC.contributor, org]
  end

  def isbn
    return unless bibtex.field?(:isbn)

    remove_from_fallback(:isbn)

    graph << [entry, bibo[:isbn], bibtex[:isbn].to_s]

    graph << if bibtex.contained?
               [entry, RDF::Vocab::DC.isPartOf, "urn:isbn:#{bibtex[:isbn]}"]
             else
               [entry, RDF::Vocab::DC.identifier, "urn:isbn:#{bibtex[:isbn]}"]
             end
  end

  def issn
    return unless bibtex.field?(:issn)

    remove_from_fallback(:issn)

    graph << [entry, bibo[:issn], bibtex[:issn].to_s]
    graph << if bibtex.contained?
               [entry, RDF::Vocab::DC.isPartOf, "urn:issn:#{bibtex[:issn]}"]
             else
               [entry, RDF::Vocab::DC.identifier, "urn:issn:#{bibtex[:issn]}"]
             end
  end

  def journal_dc_source
    return unless bibtex.field?(:journal)

    remove_from_fallback(:journal)

    source = []
    source << bibtex[:journal].to_s
    source << "Vol. #{bibtex[:volume]}" if bibtex.field?(:volume)
    source << "No. #{bibtex[:number]}" if bibtex.field?(:number)
    pagination = bibtex[:pagination] || 'pp.'
    source << "#{pagination} #{bibtex[:pages]}" if bibtex.field?(:pages)
    graph << [entry, RDF::Vocab::DC.source, source.join(', ')]
  end

  def journal_dc_part_of
    return unless bibtex.field?(:journal)
    return if bibtex.has_parent? && bibtex.parent[:title] == bibtex[:journal]
    return if bibtex.has_parent? && bibtex.parent[:issn] == bibtex[:issn]

    journal = RDF::Node.new
    graph << [journal, RDF.type, bibo[:Journal]]
    graph << [journal, RDF::Vocab::DC.title, bibtex[:journal].to_s]

    graph << [entry, RDF::Vocab::DC.isPartOf, journal]
  end

  def key
    graph << [entry, RDF::Vocab::DC.identifier, "urn:bibtex:#{bibtex.key}"]
  end

  def keywords
    return unless bibtex.field?(:keywords)

    remove_from_fallback(:keywords)

    bibtex[:keywords].to_s.split(/\s*[,;]\s*/).each do |keyword|
      graph << [entry, RDF::Vocab::DC.subject, keyword]
    end
  end

  def language
    return unless bibtex.field?(:language)

    remove_from_fallback(:language)

    bibtex[:language] = 'german' if bibtex[:language] == 'ngerman'

    graph << [entry, RDF::Vocab::DC.language, bibtex[:language].to_s]
  end

  def location
    return unless bibtex.field?(:location)

    remove_from_fallback(:location)

    graph << [entry, RDF::Vocab::DC.Location, bibtex[:location].to_s]
    if %i[proceedings inproceedings conference].include?(bibtex.type)
      event = RDF::Vocabulary.new('http://purl.org/NET/c4dm/event.owl')
      graph << [entry, event[:place], org]
    end
  end

  def lccn
    return unless bibtex.field?(:lccn)

    remove_from_fallback(:lccn)

    graph << [entry, bibo[:lccn], bibtex[:lccn].to_s]
  end

  def note
    return unless bibtex.field?(:note)

    remove_from_fallback(:note)

    pub = RDF::Node.new
    graph << [pub, RDF.type, bibo[:Note]]
    graph << [pub, bibo[:content], bibtex[:note]]

    graph << [entry, bibo[:annotates], pub]
  end

  def number
    return unless bibtex.field?(:number)

    remove_from_fallback(:number)

    graph << case bibtex.type
             when :techreport || :manual || :unpublished
               [entry, bibo[:number], bibtex[:number].to_s]
             else
               [entry, bibo[:issue], bibtex[:number].to_s]
             end
  end

  def organization
    return unless bibtex.field?(:organization)

    remove_from_fallback(:organization)

    org = agent(bibtex[:organization].to_s) { create_agent(bibtex[:organization].to_s, :Organization) }

    graph << [entry, RDF::Vocab::DC.contributor, org]
    graph << [entry, bibo[:organizer], org] if %i[proceedings inproceedings conference].include?(bibtex.type)
  end

  def pages
    return unless bibtex.field?(:pages)

    remove_from_fallback(:pages)

    if bibtex[:pages].to_s =~ /^\s*(\d+)\s*-+\s*(\d+)\s*$/
      graph << [entry, bibo[:pageStart], Regexp.last_match[1]]
      graph << [entry, bibo[:pageEnd], Regexp.last_match[2]]
    else
      graph << [entry, bibo[:pages], bibtex[:pages].to_s]
    end
  end

  def pagetotal
    return unless bibtex.field?(:pagetotal)

    remove_from_fallback(:pagetotal)

    graph << [entry, bibo[:numPages], bibtex[:pagetotal].to_s]
  end

  def parent
    return unless bibtex.has_parent?

    remove_from_fallback(:crossref)

    parent_id = RDF::URI.new(bibtex.parent.identifier)
    BibTeX::Entry::RDFConverter.new(bibtex.parent, graph, agent).convert! unless uri_in_graph?(parent_id)
    graph << [entry, RDF::Vocab::DC.isPartOf, parent_id]
  end

  def publisher
    return unless bibtex.field?(:publisher, :organization, :school, :institution)

    remove_from_fallback(:publisher, :address)

    org =
      if bibtex.field?(:publisher)
        agent(bibtex[:publisher].to_s) { create_agent(bibtex[:publisher].to_s, :Organization) }
      elsif bibtex.field?(:organization)
        agent(bibtex[:organization].to_s) { create_agent(bibtex[:organization].to_s, :Organization) }
      elsif bibtex.field?(:school)
        agent(bibtex[:school].to_s) { create_agent(bibtex[:school].to_s, :Organization) }
      elsif bibtex.field?(:institution)
        agent(bibtex[:institution].to_s) { create_agent(bibtex[:institution].to_s, :Organization) }
      end

    if bibtex.field?(:address)
      address = RDF::Vocabulary.new('http://schemas.talis.com/2005/address/schema#')
      graph << [org, address[:localityName], bibtex[:address]]
    end

    graph << [entry, RDF::Vocab::DC.publisher, org]
    graph << [entry, bibo[:publisher], org]
  end

  def school
    return unless bibtex.field?(:school)

    remove_from_fallback(:school)

    org = agent(bibtex[:school].to_s) { create_agent(bibtex[:school].to_s, :Organization) }

    graph << [entry, RDF::Vocab::DC.contributor, org]
  end

  def series
    return unless bibtex.field?(:series)

    remove_from_fallback(:series)
    return if bibtex.has_parent? && bibtex.parent[:title] == bibtex[:series]
    return if bibtex.has_parent? && bibtex.parent[:series] == bibtex[:series]
    return if bibtex.has_parent? && bibtex.parent[:issn] == bibtex[:issn]

    series = RDF::Node.new
    graph << [series, RDF.type, bibo[:MultiVolumeBook]]
    graph << [series, RDF::Vocab::DC.title, bibtex[:series].to_s]

    graph << [entry, RDF::Vocab::DC.isPartOf, series]
  end

  def thesis_degree
    return unless bibo_class == :Thesis

    degree =
      case bibtex.type
      # ms = masters degree in science
      # Only ma and ms available. We simply chose one.
      when :mastersthesis then bibo['degrees/ms']
      when :phdthesis then bibo['degrees/phd']
      end

    degree =
      case bibtex[:type]
      when 'mathesis' then bibo['degrees/ma']
      when 'phdthesis' then bibo['degrees/phd']
      when /Dissertation/i then bibo['degrees/phd']
      when /Bachelor['s]{0,2} Thesis/i then "Bachelor's Thesis"
      when /Diplomarbeit/i then bibo['degrees/ms']
      when /Magisterarbeit/i then bibo['degrees/ma']
      else degree
      end

    unless degree.nil?
      remove_from_fallback(:type)
      graph << [entry, bibo[:degree], degree]
    end
  end

  def title
    return unless bibtex.field?(:title)

    remove_from_fallback(:title)

    title = [bibtex[:title].to_s, bibtex[:subtitle].to_s]
            .reject { |t| t.nil? || t.empty? }
            .join(': ')
    graph << [entry, RDF::Vocab::DC.title, title]
    graph << [entry, bibo[:shortTitle], bibtex[:title].to_s] if bibtex.field?(:subtitle)
  end

  def translator
    return unless bibtex.field?(:translator)

    remove_from_fallback(:translator)

    node = agent(bibtex[:translator].to_s) do
      create_agent(bibtex[:translator].to_s, :Person)
    end

    graph << [entry, RDF::Vocab::DC.contributor, node]
    graph << [entry, bibo[:translator], node]
  end

  def type
    graph << [entry, RDF.type, bibo[bibo_class]]

    case bibtex.type
    when :proceedings, :journal
      graph << [entry, RDF::Vocab::DC.type, 'Collection']
    else
      graph << [entry, RDF::Vocab::DC.type, 'Text']
    end
  end

  def url
    return unless bibtex.field?(:url)

    remove_from_fallback(:url)

    graph << [entry, RDF::Vocab::DC.URI, bibtex[:url].to_s]
    graph << [entry, bibo[:uri], bibtex[:url].to_s]
  end

  def volume
    return unless bibtex.field?(:volume)

    remove_from_fallback(:volume)

    graph << [entry, bibo[:volume], bibtex[:volume].to_s]
  end

  def volumes
    return unless bibtex.field?(:volumes)

    remove_from_fallback(:volumes)

    graph << [entry, bibo[:numVolumes], bibtex[:volumes].to_s]
  end

  def year
    return unless bibtex.field?(:year)

    remove_from_fallback(:year, :month)

    year = bibtex[:year].to_s
    if bibtex.field?(:month)
      month = BibTeX::Entry::MONTHS.find_index(bibtex[:month].to_s.intern)
      month += 1 unless month.nil?
    end
    date = month.nil? ? year : [year, month].join('-')

    graph << [entry, RDF::Vocab::DC.issued, date]
  end

  protected

  attr_reader :bibtex, :graph

  private

  def bibo
    @bibo ||= RDF::Vocabulary.new('http://purl.org/ontology/bibo/')
  end

  def bibo_class
    BIBO_TYPES[bibtex[:type]] || BIBO_TYPES[bibtex.type] || :Document
  end

  def entry
    @entry ||= RDF::URI.new(bibtex.identifier)
  end

  def agent(key = nil)
    if key.nil?
      @agent
    else
      key = key.respond_to?(:to_hash) ? key.to_hash : key
      @agent[key] ||= yield
    end
  end

  def create_agent(name, type)
    node = RDF::Node.new

    graph << [node, RDF.type, RDF::Vocab::FOAF[type]]
    graph << [node, RDF::Vocab::FOAF.name, name.to_s]

    if name.is_a?(BibTeX::Name)
      %i[given family prefix suffix].each do |part|
        value = name.send(part)
        graph << [node, bibo["#{part}Name"], value.to_s] unless value.nil?
      end
    end

    node
  end

  def uri_in_graph?(uri)
    solutions = RDF::Query.execute(graph) do
      pattern [uri, nil, nil]
    end

    !solutions.empty?
  end

  def fallback
    @fallback ||= bibtex.fields.keys
  end

  def remove_from_fallback(*fields)
    fields.each { |field| fallback.delete(field) }
  end

  def run_fallback
    return if fallback.empty?

    ml = RDF::Vocabulary.new('http://bibtexml.sf.net/')
    fallback.each do |field|
      graph << [entry, ml[field], bibtex[field]]
    end
  end
end
