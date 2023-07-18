# coding: utf-8

require File.expand_path('lib/colorator.rb', __dir__)

Gem::Specification.new do |spec|
  spec.name        = "colorator"
  spec.summary     = "Colorize your text in the terminal."
  spec.version     = Colorator::VERSION
  spec.authors     = ["Parker Moore", "Brandon Mathis"]
  spec.email       = ["parkrmoore@gmail.com", "brandon@imathis.com"]
  spec.homepage    = "https://github.com/octopress/colorator"
  spec.licenses    = ["MIT"]

  all                = `git ls-files -z`.split("\x0").reject { |f| f.start_with?(".") }
  spec.files         = all.select { |f| File.basename(f) == f || f =~ %r{^(bin|lib)/} }
  spec.executables   = spec.files.grep(%r{^bin/}) { |f| File.basename(f) }
  spec.require_paths = ["lib"]

  spec.extra_rdoc_files = ["README.markdown", "LICENSE"]
  spec.rdoc_options     = ["--charset=UTF-8"]

  spec.add_development_dependency "rspec", "~> 3.1"
end
