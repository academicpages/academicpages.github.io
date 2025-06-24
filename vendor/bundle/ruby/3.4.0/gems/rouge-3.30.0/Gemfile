# frozen_string_literal: true

source 'http://rubygems.org'

gemspec

gem 'rake'

gem 'minitest', '>= 5.0'
gem 'minitest-power_assert'
gem 'power_assert', '~> 1.2'

gem 'parallel', '~> 1.13.0' if RUBY_VERSION < '2.2.0'
gem 'rubocop', '~> 1.0', '<= 1.11'
gem 'rubocop-performance'

# don't try to install redcarpet under jruby
gem 'redcarpet', :platforms => :ruby

# Profiling
if RUBY_VERSION >= '2.3.0'
  gem 'memory_profiler', :require => false
end

# Needed for a Rake task
gem 'git'
gem 'yard'

group :development do
  gem 'pry'

  # docs
  gem 'github-markup'

  # for visual tests
  if RUBY_VERSION < '2.2.0'
    gem 'sinatra', '~> 1.4.8'
  else
    gem 'sinatra'
  end

  # Ruby 3 no longer ships with a web server
  gem 'puma' if RUBY_VERSION >= '3'
  gem 'shotgun'
end
