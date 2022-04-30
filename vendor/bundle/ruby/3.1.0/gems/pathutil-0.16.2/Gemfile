# Frozen-string-literal: true
# Copyright: 2015 - 2017 Jordon Bedwell - MIT License
# Encoding: utf-8

source "https://rubygems.org"
gem "rake", :require => false
gemspec

group :test do
  gem "safe_yaml", :require => false
  gem "luna-rspec-formatters", :require => false
  gem "simplecov", :require => false
end

group :development do
  gem "rspec", :require => false
  gem "rspec-helpers", :require => false
  gem "rubocop", :github => "bbatsov/rubocop", :require => false
  gem "benchmark-ips", :require => false
  gem "simple-ansi", :require => false
  gem "pry", :require => false
end
