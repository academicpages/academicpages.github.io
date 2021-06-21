source 'https://rubygems.org'

group :test do
  gem 'rspec', '~> 3.7'
  gem 'rake'
  gem 'cucumber', '~> 3.1'
end

group :development do
  gem 'racc', '~> 1.4', :platform => :ruby
end

group :coverage do
  gem 'simplecov', :require => false, :platforms => :ruby
  gem 'coveralls', :require => false if ENV['CI']
end

group :optional do
  gem 'jeweler'
  gem 'yard'
end

group :debug do
  gem 'debugger', :platform => [:mri_19]
  gem 'byebug', :platform => :mri if RUBY_VERSION > '2.0'
end
