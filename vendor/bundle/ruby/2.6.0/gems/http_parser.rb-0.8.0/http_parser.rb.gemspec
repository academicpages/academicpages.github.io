Gem::Specification.new do |s|
  s.name = "http_parser.rb"
  s.version = "0.8.0"
  s.summary = "Simple callback-based HTTP request/response parser"
  s.description = "Ruby bindings to https://github.com/joyent/http-parser and https://github.com/http-parser/http-parser.java"

  s.authors = ["Marc-Andre Cournoyer", "Aman Gupta"]
  s.email   = ["macournoyer@gmail.com", "aman@tmm1.net"]
  s.license = 'MIT'

  s.homepage = "https://github.com/tmm1/http_parser.rb"
  s.files = `git ls-files`.split("\n") + Dir['ext/ruby_http_parser/vendor/**/*']

  s.require_paths = ["lib"]
  s.extensions    = ["ext/ruby_http_parser/extconf.rb"]

  s.add_development_dependency 'rake-compiler', '~> 1.0'
  s.add_development_dependency 'rspec', '~> 3'
  s.add_development_dependency 'json', '~> 2.1'
  s.add_development_dependency 'benchmark_suite', '~> 1.0'
  s.add_development_dependency 'ffi', '~> 1.9'

  if RUBY_PLATFORM =~ /java/
    s.add_development_dependency 'jruby-openssl'
  else
    if Gem::Version.new(RUBY_VERSION) >= Gem::Version.new('2.4.0')
      s.add_development_dependency 'yajl-ruby', '~> 1.3'
    else
      s.add_development_dependency 'yajl-ruby', '= 1.2.1'
    end
  end
end
