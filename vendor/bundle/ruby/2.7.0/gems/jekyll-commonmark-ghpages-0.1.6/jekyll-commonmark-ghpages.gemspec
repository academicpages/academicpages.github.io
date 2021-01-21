# coding: utf-8

Gem::Specification.new do |spec|
  spec.name          = "jekyll-commonmark-ghpages"
  spec.summary       = "CommonMark generator for Jekyll"
  spec.version       = "0.1.6"
  spec.authors       = ["Ashe Connor"]
  spec.email         = "kivikakk@github.com"
  spec.homepage      = "https://github.com/github/jekyll-commonmark-ghpages"
  spec.licenses      = ["MIT"]

  spec.files         = `git ls-files -z`.split("\x0")
  spec.executables   = spec.files.grep(%r{^bin/}) { |f| File.basename(f) }
  spec.test_files    = spec.files.grep(%r{^(test|spec|features)/})
  spec.require_paths = ["lib"]

  spec.add_runtime_dependency "jekyll-commonmark", "~> 1.2"
  spec.add_runtime_dependency "commonmarker", "~> 0.17.6"
  spec.add_runtime_dependency "rouge", ">= 2.0", "< 4.0"

  spec.add_development_dependency "rspec", "~> 3.0"
  spec.add_development_dependency "rake"
end
