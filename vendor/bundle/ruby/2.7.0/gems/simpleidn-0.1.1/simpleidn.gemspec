lib = File.expand_path('../lib', __FILE__)
$LOAD_PATH.unshift(lib) unless $LOAD_PATH.include?(lib)
require 'simpleidn/version'

Gem::Specification.new do |spec|
  spec.name          = "simpleidn"
  spec.version       = SimpleIDN::VERSION
  spec.authors       = ["Morten Møller Riis"]
  spec.email         = ["mortenmoellerriis _AT_ gmail.com"]

  spec.summary       = %q{Punycode ACE to unicode UTF-8 (and vice-versa) string conversion.}
  spec.description   = %q{This gem allows easy conversion from punycode ACE strings to unicode UTF-8 strings and vice-versa.}
  spec.homepage      = "https://github.com/mmriis/simpleidn"
  spec.license       = "MIT"

  spec.files         = `git ls-files -z`.split("\x0").reject { |f| f.match(%r{^(test|spec|features)/}) }
  spec.require_paths = ["lib"]

  spec.add_runtime_dependency "unf", '~> 0.1.4'

  spec.add_development_dependency "bundler", "~> 1.11"
  spec.add_development_dependency "rake", "~> 10.0"
  spec.add_development_dependency "rspec", "~> 3.0"

  spec.required_ruby_version = '>1.9'
end
