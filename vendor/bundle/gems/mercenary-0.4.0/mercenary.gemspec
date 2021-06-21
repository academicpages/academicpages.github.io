# frozen_string_literal: true

lib = File.expand_path("lib", __dir__)
$LOAD_PATH.unshift(lib) unless $LOAD_PATH.include?(lib)
require "mercenary/version"

Gem::Specification.new do |spec|
  spec.name          = "mercenary"
  spec.version       = Mercenary::VERSION
  spec.authors       = ["Tom Preston-Werner", "Parker Moore"]
  spec.email         = ["tom@mojombo.com", "parkrmoore@gmail.com"]
  spec.description   = "Lightweight and flexible library for writing command-line apps in Ruby."
  spec.summary       = "Lightweight and flexible library for writing command-line apps in Ruby."
  spec.homepage      = "https://github.com/jekyll/mercenary"
  spec.license       = "MIT"

  spec.files         = `git ls-files`.split($INPUT_RECORD_SEPARATOR)
  spec.executables   = spec.files.grep(%r!^bin/!) { |f| File.basename(f) }
  spec.test_files    = spec.files.grep(%r!^(test|spec|features)/!)
  spec.require_paths = ["lib"]

  spec.required_ruby_version = ">= 2.4.0"

  spec.add_development_dependency "bundler"
  spec.add_development_dependency "rake"
  spec.add_development_dependency "rspec", "~> 3.0"
  spec.add_development_dependency "rubocop-jekyll", "~> 0.10.0"
end
