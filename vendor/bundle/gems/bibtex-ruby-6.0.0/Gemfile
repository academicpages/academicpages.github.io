source 'https://rubygems.org'
gemspec

gem 'json', '~>2.0', platforms: %i[mri_18 jruby]

gem 'rdf', '~>3.0'
gem 'rdf-vocab', '~>3.0'

gem 'rexml', '~>3.0'

group :debug do
  gem 'byebug', require: false, platforms: :mri
  gem 'ruby-debug', require: false, platforms: :jruby
end

group :test do
  gem 'cucumber'
  gem 'minitest', require: false
  gem 'unicode', '~>0.4', platforms: %i[mswin mingw mri]
end

group :extra do
  gem 'redcarpet', platforms: [:ruby]
end

group :profile do
  gem 'gnuplot', platforms: [:mri]
  gem 'ruby-prof', platforms: [:mri]
end

group :coverage do
  gem 'simplecov', require: false, platforms: [:ruby]
end

group :development do
  gem 'iconv', platforms: [:ruby]
  gem 'racc'
  gem 'rake'
  gem 'yard'
end
