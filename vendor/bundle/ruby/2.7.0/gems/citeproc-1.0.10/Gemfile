source 'https://rubygems.org'
gemspec

group :debug do
  gem 'byebug', require: false, platforms: :mri
  gem 'ruby-debug', require: false, platforms: :jruby
end

group :optional do
  gem 'nokogiri'
  gem 'chronic', require: false
  gem 'edtf'
  gem 'bibtex-ruby', require: 'bibtex'
  gem 'pry'
  gem 'citeproc-ruby', github: 'inukshuk/citeproc-ruby'
  #gem 'csl', github: 'inukshuk/csl-ruby'
end

group :development do
  gem 'rake'
  gem 'cucumber'
  gem 'rspec'
  gem 'unicode_utils', require: false unless RUBY_VERSION >= '2.4'
  gem 'csl-styles', '~>1.0.1', require: false
end

group :coverage do
  gem 'simplecov', require: false
  gem 'coveralls', require: false if ENV['CI']
end

group :extra do
  gem 'yard'
  gem 'redcarpet', platform: :mri
end
