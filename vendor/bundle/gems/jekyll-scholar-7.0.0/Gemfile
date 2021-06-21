source 'https://rubygems.org'
gemspec

group :development do
  gem 'cucumber'
  gem 'rake'
  gem 'redcarpet'
  gem 'redgreen'
  gem 'shoulda'
  gem 'test-unit'
  gem 'unicode_utils' if RUBY_VERSION < '2.4'
end

group :extra do
  gem 'listen'
end

group :coverage do
  gem 'coveralls', :require => false
  gem 'simplecov', :require => false
end

group :debug do
  gem 'byebug', :require => false, :platform => :mri
end
