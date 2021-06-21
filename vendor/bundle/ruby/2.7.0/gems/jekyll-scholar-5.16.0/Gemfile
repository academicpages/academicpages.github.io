source 'https://rubygems.org'
gemspec

group :development do
  gem 'test-unit'
  gem 'rake'
  gem 'redgreen'
  gem 'shoulda'
  gem 'cucumber', '1.3.11'
  gem 'redcarpet'
  gem 'unicode_utils' if RUBY_VERSION < '2.4'
end

group :extra do
    gem 'listen'
end

group :coverage do
  gem 'simplecov', :require => false
  gem 'coveralls', :require => false
end

group :debug do
  gem 'byebug', :require => false, :platform => :mri
end
