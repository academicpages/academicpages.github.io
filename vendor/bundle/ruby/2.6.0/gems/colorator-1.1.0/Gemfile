source "https://rubygems.org"
gemspec

gem "rake"
group :development do
  gem "rspec-helpers", :require => false
  gem "luna-rspec-formatters", :require => false
  gem "pry", :require => false unless ENV[
    "CI"
  ]
end
