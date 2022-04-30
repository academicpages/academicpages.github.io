require "rspec/expectations"
require File.expand_path("../lib/jekyll-commonmark-ghpages.rb", File.dirname(__FILE__))

RSpec.configure do |config|
  config.run_all_when_everything_filtered = true
  config.order = "random"
end
