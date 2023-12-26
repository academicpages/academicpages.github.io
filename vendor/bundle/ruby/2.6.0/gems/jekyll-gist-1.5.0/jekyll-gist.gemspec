# frozen_string_literal: true

lib = File.expand_path("lib", __dir__)

$LOAD_PATH.unshift(lib) unless $LOAD_PATH.include?(lib)
require "jekyll-gist/version"

Gem::Specification.new do |spec|
  spec.name          = "jekyll-gist"
  spec.version       = Jekyll::Gist::VERSION
  spec.authors       = ["Parker Moore"]
  spec.email         = ["parkrmoore@gmail.com"]
  spec.summary       = "Liquid tag for displaying GitHub Gists in Jekyll sites."
  spec.homepage      = "https://github.com/jekyll/jekyll-gist"
  spec.license       = "MIT"

  spec.required_ruby_version = ">= 2.1"

  spec.files         = `git ls-files -z`.split("\x0")
  spec.executables   = spec.files.grep(%r!^bin/!) { |f| File.basename(f) }
  spec.test_files    = spec.files.grep(%r!^(test|spec|features)/!)
  spec.require_paths = ["lib"]

  spec.add_dependency "octokit", "~> 4.2"
  spec.add_development_dependency "bundler", "~> 1.6"
  spec.add_development_dependency "jekyll", ">= 3.0"
  spec.add_development_dependency "rake"
  spec.add_development_dependency "rspec"
  spec.add_development_dependency "rubocop", "~> 0.51"
  spec.add_development_dependency "webmock"
end
