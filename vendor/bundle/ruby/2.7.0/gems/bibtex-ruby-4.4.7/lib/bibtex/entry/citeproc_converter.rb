class BibTeX::Entry::CiteProcConverter
  CSL_FILTER = Hash.new { |h, k| k }.merge(Hash[*%w{
    date         issued
    isbn         ISBN
    booktitle    container-title
    journal      container-title
    journaltitle container-title
    series       collection-title
    address      publisher-place
    pages        page
    number       issue
    url          URL
    doi          DOI
    pmid         PMID
    pmcid        PMCID
    year         issued
    type         genre
    school       publisher
    institution  publisher
    organization publisher
    howpublished publisher
    type         genre
  }.map(&:intern)]).freeze

  CSL_FIELDS = %w{
    abstract annote archive archive_location archive-place
    authority call-number chapter-number citation-label citation-number
    collection-title container-title DOI edition event event-place
    first-reference-note-number genre ISBN issue jurisdiction keyword locator
    medium note number number-of-pages number-of-volumes original-publisher
    original-publisher-place original-title page page-first publisher
    publisher-place references section status title URL version volume
    year-suffix accessed container event-date issued original-date
    author editor translator recipient interviewer publisher composer
    original-publisher original-author container-author collection-editor
  }.map(&:intern).freeze

  CSL_TYPES = Hash.new { |h, k| k }.merge(Hash[*%w{
    booklet        pamphlet
    conference     paper-conference
    inbook         chapter
    incollection   chapter
    inproceedings  paper-conference
    manual         book
    mastersthesis  thesis
    phdthesis      thesis
    proceedings    book
    techreport     report
    unpublished    manuscript
    article        article-journal
  }.map(&:intern)]).freeze

  def self.convert(bibtex, options = {})
    new(bibtex, options).convert!
  end

  def initialize(bibtex, options = {})
    @bibtex = bibtex
    @options = { quotes: [] }.merge(options)
  end

  def convert!
    bibtex.parse_names
    bibtex.parse_month

    bibtex.each_pair do |key, value|
      convert key, value
    end

    bibtex.inherited_fields.each do |key|
      convert key, bibtex.parent.provide(key)
    end

    methods = self.class.instance_methods(false) - [:convert!, :hash]
    methods.each { |m| send(m) }

    hash
  end

  def conferences
    return unless [:conference, :proceedings, :inproceedings].include?(bibtex.type)

    if bibtex.field?(:organization) && bibtex.field?(:publisher)
      hash['authority'] = bibtex[:organization]
      hash['publisher'] = bibtex[:publisher]
    end

    if bibtex.field? :address
      hash['event-place'] = bibtex[:address]
    end
  end

  def techreport
    return unless [:techreport, :report].include?(bibtex.type)
    hash['number'] = bibtex[:number].to_s if bibtex.field? :number
  end

  def date
    case
    when bibtex.field?(:date)
      hash['issued'] = {
        'date-parts' => bibtex.date.to_s.split('/').map { |part|
          part.split('-').map(&:to_i)
        }
      }

    when bibtex.field?(:year)
      case bibtex[:year].to_s
      when /^\d+$/
        parts = [bibtex[:year].to_s]

        if bibtex.field?(:month)
          parts.push BibTeX::Entry::MONTHS.find_index(bibtex[:month].to_s.intern)
          parts[1] = parts[1] + 1 unless parts[1].nil?

          if bibtex.field?(:day)
            parts.push bibtex[:day]
          end
        end

        hash['issued'] = { 'date-parts' => [parts.compact.map(&:to_i)] }
      else
        hash['issued'] = { 'literal' => bibtex[:year].to_s }
      end

    else
      # no date present
    end
  end

  def key
    hash['id'] = bibtex.key.to_s
  end

  def type
    hash['type'] = CSL_TYPES[bibtex.type].to_s

    return if hash.key?('genre')
    case bibtex.type
    when :mastersthesis
      hash['genre'] = "Master's thesis"
    when :phdthesis
      hash['genre'] = 'PhD thesis'
    end
  end

  private

  attr_reader :bibtex, :options

  def convert(key, value)
    return if BibTeX::Entry::DATE_FIELDS.include?(key)

    cp_key = CSL_FILTER[key].to_s

    if hash.key?(cp_key)
      hash[key] = value.to_citeproc(options)
    else
      hash[cp_key] = value.to_citeproc(options)
    end
  end

  def hash
    @hash ||= {}
  end
end
