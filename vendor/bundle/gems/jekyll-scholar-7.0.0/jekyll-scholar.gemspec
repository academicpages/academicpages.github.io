# -*- encoding: utf-8 -*-
lib = File.expand_path('../lib/', __FILE__)
$:.unshift lib unless $:.include?(lib)

require 'jekyll/scholar/version'

Gem::Specification.new do |s|
  s.name        = 'jekyll-scholar'
  s.version     = Jekyll::Scholar::VERSION.dup
  s.platform    = Gem::Platform::RUBY
  s.authors     = ['Sylvester Keil']
  s.email       = 'http://sylvester.keil.or.at'
  s.homepage    = 'http://github.com/inukshuk/jekyll-scholar'
  s.summary     = 'Jekyll extensions for the academic blogger.'
  s.licenses    = ['MIT']
  s.description = %q{
    Jekyll-Scholar is for all the academic bloggers out there. It is a set of
    extensions for Jekyll the awesome, blog aware, static site generator; it
    formats your BibTeX bibliographies for the web using CSL citation styles
    and generally gives your blog posts citation super-powers.'
  }.gsub(/\s+/, ' ')

  s.date        = Time.now

  s.required_rubygems_version = '>= 1.3.6'

  s.add_runtime_dependency('jekyll', '~> 4.0')
  s.add_runtime_dependency('citeproc-ruby', '~> 1.0')
  s.add_runtime_dependency('csl-styles', '~> 1.0')
  s.add_runtime_dependency('bibtex-ruby', '~> 6.0')

  s.files        = `git ls-files`.split("\n")
  s.test_files   = `git ls-files -- {test,spec,features}/*`.split("\n")
  s.executables  = []
  s.require_path = 'lib'

end

# vim: syntax=ruby
