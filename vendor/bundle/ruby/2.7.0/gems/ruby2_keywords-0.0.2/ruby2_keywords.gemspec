version = IO.popen(%W[git -C #{__dir__} describe --tags --match v[0-9]*], &:read)[/\Av?(\d+(?:\.\d+)*)/, 1]

Gem::Specification.new do |s|
  s.name = "ruby2_keywords"
  s.version = version
  s.summary = "Shim library for Module#ruby2_keywords"
  s.homepage = "https://github.com/ruby/ruby2_keywords"
  s.licenses = ["Ruby"]
  s.authors = ["Nobuyoshi Nakada"]
  s.require_paths = ["lib"]
  s.files = [
    "README.md",
    "lib/ruby2_keywords.rb",
    "ruby2_keywords.gemspec",
  ]
end
