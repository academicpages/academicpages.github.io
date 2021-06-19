#!/usr/bin/env ruby

require 'rubygems'
require 'bibtex'
require 'yaml'

if ARGV.length < 1
  puts "Usage: #{$0} <bib> [<yml>]"
else
  out = ARGV.length == 2 ? File.open(ARGV[1], 'w') : STDOUT
  out.puts BibTeX.open(ARGV[0]).to_yaml
end
