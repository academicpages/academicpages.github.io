source 'https://rubygems.org'

# Specify your gem's dependencies in utopia.gemspec
gemspec

group :maintenance, optional: true do
  gem "bake-gem"
  gem "bake-modernize"
end

group :test do
  gem "rspec", "~> 3.6"

  gem 'simplecov'
  gem 'coveralls', require: false

  gem "bundler"
  gem "rake"
  gem "concurrent-ruby"
end
