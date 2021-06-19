require 'rubygems'
require 'bibtex'

begin
  require 'citeproc/ruby'
  require 'csl/styles'
rescue LoadError
  puts 'this example depends on the citeproc-ruby and csl-styles gems'
  exit
end

# Open a bibliography file
bib = BibTeX.open File.expand_path('../markdown.bib',__FILE__),
  :include => [:meta_content]

# Replaces all strings in the Bibliography and then
# converts each BibTeX entries to a string using Chicago style
# (all other elements are mapped to simple strings)
bib.replace

cp = CiteProc::Processor.new :style => 'apa',
  :format => 'html', :locale => 'en'

cp.import bib.to_citeproc

content = bib['@entry, @meta_content'].map do |e|
  if e.entry?
    cp.render :bibliography, :id => e.key
  else
    e.to_s
  end
end


begin
  require 'redcarpet'
rescue LoadError
  puts 'this example depends on the redcarpet gem'
  exit
end

puts Redcarpet::Markdown.new(Redcarpet::Render::HTML).render(content.join)
