require 'rexml/document'

class BibTeX::Entry::BibTeXMLConverter
  def self.convert(bibtex, options = {})
    new(bibtex, options).convert!
  end

  def initialize(bibtex, options = {})
    @bibtex = bibtex
    @options = options
  end

  def convert!
    xml = REXML::Element.new('bibtex:entry')
    xml.attributes['id'] = bibtex.key

    fields

    xml.add_element(entry)
    xml
  end

  def fields
    bibtex.fields.each do |key, value|
      field = REXML::Element.new("bibtex:#{key}")

      if options[:extended] && value.name?
        value.each { |n| field.add_element(n.to_xml) }
      else
        field.text = value.to_s(options)
      end

      entry.add_element(field)
    end
  end

  protected

  attr_reader :bibtex, :options

  def entry
    @entry ||= REXML::Element.new("bibtex:#{bibtex.type}")
  end
end
