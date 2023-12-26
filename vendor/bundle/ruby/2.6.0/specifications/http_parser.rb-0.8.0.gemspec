# -*- encoding: utf-8 -*-
# stub: http_parser.rb 0.8.0 ruby lib
# stub: ext/ruby_http_parser/extconf.rb

Gem::Specification.new do |s|
  s.name = "http_parser.rb".freeze
  s.version = "0.8.0"

  s.required_rubygems_version = Gem::Requirement.new(">= 0".freeze) if s.respond_to? :required_rubygems_version=
  s.require_paths = ["lib".freeze]
  s.authors = ["Marc-Andre Cournoyer".freeze, "Aman Gupta".freeze]
  s.date = "2021-09-01"
  s.description = "Ruby bindings to https://github.com/joyent/http-parser and https://github.com/http-parser/http-parser.java".freeze
  s.email = ["macournoyer@gmail.com".freeze, "aman@tmm1.net".freeze]
  s.extensions = ["ext/ruby_http_parser/extconf.rb".freeze]
  s.files = ["ext/ruby_http_parser/extconf.rb".freeze]
  s.homepage = "https://github.com/tmm1/http_parser.rb".freeze
  s.licenses = ["MIT".freeze]
  s.rubygems_version = "3.0.3.1".freeze
  s.summary = "Simple callback-based HTTP request/response parser".freeze

  s.installed_by_version = "3.0.3.1" if s.respond_to? :installed_by_version

  if s.respond_to? :specification_version then
    s.specification_version = 4

    if Gem::Version.new(Gem::VERSION) >= Gem::Version.new('1.2.0') then
      s.add_development_dependency(%q<rake-compiler>.freeze, ["~> 1.0"])
      s.add_development_dependency(%q<rspec>.freeze, ["~> 3"])
      s.add_development_dependency(%q<json>.freeze, ["~> 2.1"])
      s.add_development_dependency(%q<benchmark_suite>.freeze, ["~> 1.0"])
      s.add_development_dependency(%q<ffi>.freeze, ["~> 1.9"])
      s.add_development_dependency(%q<yajl-ruby>.freeze, ["~> 1.3"])
    else
      s.add_dependency(%q<rake-compiler>.freeze, ["~> 1.0"])
      s.add_dependency(%q<rspec>.freeze, ["~> 3"])
      s.add_dependency(%q<json>.freeze, ["~> 2.1"])
      s.add_dependency(%q<benchmark_suite>.freeze, ["~> 1.0"])
      s.add_dependency(%q<ffi>.freeze, ["~> 1.9"])
      s.add_dependency(%q<yajl-ruby>.freeze, ["~> 1.3"])
    end
  else
    s.add_dependency(%q<rake-compiler>.freeze, ["~> 1.0"])
    s.add_dependency(%q<rspec>.freeze, ["~> 3"])
    s.add_dependency(%q<json>.freeze, ["~> 2.1"])
    s.add_dependency(%q<benchmark_suite>.freeze, ["~> 1.0"])
    s.add_dependency(%q<ffi>.freeze, ["~> 1.9"])
    s.add_dependency(%q<yajl-ruby>.freeze, ["~> 1.3"])
  end
end
