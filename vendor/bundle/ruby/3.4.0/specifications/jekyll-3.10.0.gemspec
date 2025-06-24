# -*- encoding: utf-8 -*-
# stub: jekyll 3.10.0 ruby lib

Gem::Specification.new do |s|
  s.name = "jekyll".freeze
  s.version = "3.10.0".freeze

  s.required_rubygems_version = Gem::Requirement.new(">= 0".freeze) if s.respond_to? :required_rubygems_version=
  s.require_paths = ["lib".freeze]
  s.authors = ["Tom Preston-Werner".freeze]
  s.bindir = "exe".freeze
  s.date = "2024-06-24"
  s.description = "Jekyll is a simple, blog aware, static site generator.".freeze
  s.email = "tom@mojombo.com".freeze
  s.executables = ["jekyll".freeze]
  s.extra_rdoc_files = ["README.markdown".freeze, "LICENSE".freeze]
  s.files = ["LICENSE".freeze, "README.markdown".freeze, "exe/jekyll".freeze]
  s.homepage = "https://github.com/jekyll/jekyll".freeze
  s.licenses = ["MIT".freeze]
  s.rdoc_options = ["--charset=UTF-8".freeze]
  s.required_ruby_version = Gem::Requirement.new(">= 2.1.0".freeze)
  s.rubygems_version = "3.1.6".freeze
  s.summary = "A simple, blog aware, static site generator.".freeze

  s.installed_by_version = "3.6.9".freeze

  s.specification_version = 2

  s.add_runtime_dependency(%q<addressable>.freeze, ["~> 2.4".freeze])
  s.add_runtime_dependency(%q<colorator>.freeze, ["~> 1.0".freeze])
  s.add_runtime_dependency(%q<csv>.freeze, ["~> 3.0".freeze])
  s.add_runtime_dependency(%q<em-websocket>.freeze, ["~> 0.5".freeze])
  s.add_runtime_dependency(%q<i18n>.freeze, [">= 0.7".freeze, "< 2".freeze])
  s.add_runtime_dependency(%q<jekyll-sass-converter>.freeze, ["~> 1.0".freeze])
  s.add_runtime_dependency(%q<jekyll-watch>.freeze, ["~> 2.0".freeze])
  s.add_runtime_dependency(%q<liquid>.freeze, ["~> 4.0".freeze])
  s.add_runtime_dependency(%q<mercenary>.freeze, ["~> 0.3.3".freeze])
  s.add_runtime_dependency(%q<pathutil>.freeze, ["~> 0.9".freeze])
  s.add_runtime_dependency(%q<rouge>.freeze, [">= 1.7".freeze, "< 4".freeze])
  s.add_runtime_dependency(%q<safe_yaml>.freeze, ["~> 1.0".freeze])
  s.add_runtime_dependency(%q<webrick>.freeze, [">= 1.0".freeze])
  s.add_runtime_dependency(%q<kramdown>.freeze, [">= 1.17".freeze, "< 3".freeze])
end
