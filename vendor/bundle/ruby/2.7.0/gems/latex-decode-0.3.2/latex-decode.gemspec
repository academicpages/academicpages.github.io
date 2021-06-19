# -*- encoding: utf-8 -*-
lib = File.expand_path('../lib/', __FILE__)
$:.unshift lib unless $:.include?(lib)

require 'latex/decode/version'

Gem::Specification.new do |s|
  s.name        = 'latex-decode'
  s.version     = LaTeX::Decode::VERSION.dup
  s.authors     = ['Sylvester Keil']
  s.email       = ['http://sylvester.keil.or.at']
  s.homepage    = 'http://github.com/inukshuk/latex-decode'
  s.summary     = 'Decodes LaTeX to Unicode.'
  s.description = 'Decodes strings formatted in LaTeX to equivalent Unicode strings.'
  s.license     = 'GPL-3.0'

  if RUBY_PLATFORM =~ /java/
    s.platform    = 'java'
  else
    s.platform    = 'ruby'
  end

  s.files        = `git ls-files`.split("\n")
  s.test_files   = `git ls-files -- {test,spec,features}/*`.split("\n")
  s.executables  = []
  s.require_path = 'lib'

  s.rdoc_options     = %w{--line-numbers --inline-source --title "LaTeX-Decode\ Documentation" --main README.md --webcvs=http://github.com/inukshuk/latex-decode/tree/master/}
  s.extra_rdoc_files = %w{README.md LICENSE}
end

# vim: syntax=ruby
