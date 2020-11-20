# -*- encoding: utf-8 -*-
# stub: jekyll 3.9.0 ruby lib

Gem::Specification.new do |s|
  s.name = "jekyll".freeze
  s.version = "3.9.0"

  s.required_rubygems_version = Gem::Requirement.new(">= 0".freeze) if s.respond_to? :required_rubygems_version=
  s.require_paths = ["lib".freeze]
  s.authors = ["Tom Preston-Werner".freeze]
  s.bindir = "exe".freeze
  s.date = "2020-08-05"
  s.description = "Jekyll is a simple, blog aware, static site generator.".freeze
  s.email = "tom@mojombo.com".freeze
  s.executables = ["jekyll".freeze]
  s.extra_rdoc_files = ["README.markdown".freeze, "LICENSE".freeze]
  s.files = ["LICENSE".freeze, "README.markdown".freeze, "exe/jekyll".freeze]
  s.homepage = "https://github.com/jekyll/jekyll".freeze
  s.licenses = ["MIT".freeze]
  s.rdoc_options = ["--charset=UTF-8".freeze]
  s.required_ruby_version = Gem::Requirement.new(">= 2.1.0".freeze)
  s.rubygems_version = "3.1.2".freeze
  s.summary = "A simple, blog aware, static site generator.".freeze

  s.installed_by_version = "3.1.2" if s.respond_to? :installed_by_version

  if s.respond_to? :specification_version then
    s.specification_version = 2
  end

  if s.respond_to? :add_runtime_dependency then
    s.add_runtime_dependency(%q<addressable>.freeze, ["~> 2.4"])
    s.add_runtime_dependency(%q<colorator>.freeze, ["~> 1.0"])
    s.add_runtime_dependency(%q<em-websocket>.freeze, ["~> 0.5"])
    s.add_runtime_dependency(%q<i18n>.freeze, ["~> 0.7"])
    s.add_runtime_dependency(%q<jekyll-sass-converter>.freeze, ["~> 1.0"])
    s.add_runtime_dependency(%q<jekyll-watch>.freeze, ["~> 2.0"])
    s.add_runtime_dependency(%q<liquid>.freeze, ["~> 4.0"])
    s.add_runtime_dependency(%q<mercenary>.freeze, ["~> 0.3.3"])
    s.add_runtime_dependency(%q<pathutil>.freeze, ["~> 0.9"])
    s.add_runtime_dependency(%q<rouge>.freeze, [">= 1.7", "< 4"])
    s.add_runtime_dependency(%q<safe_yaml>.freeze, ["~> 1.0"])
    s.add_runtime_dependency(%q<kramdown>.freeze, [">= 1.17", "< 3"])
  else
    s.add_dependency(%q<addressable>.freeze, ["~> 2.4"])
    s.add_dependency(%q<colorator>.freeze, ["~> 1.0"])
    s.add_dependency(%q<em-websocket>.freeze, ["~> 0.5"])
    s.add_dependency(%q<i18n>.freeze, ["~> 0.7"])
    s.add_dependency(%q<jekyll-sass-converter>.freeze, ["~> 1.0"])
    s.add_dependency(%q<jekyll-watch>.freeze, ["~> 2.0"])
    s.add_dependency(%q<liquid>.freeze, ["~> 4.0"])
    s.add_dependency(%q<mercenary>.freeze, ["~> 0.3.3"])
    s.add_dependency(%q<pathutil>.freeze, ["~> 0.9"])
    s.add_dependency(%q<rouge>.freeze, [">= 1.7", "< 4"])
    s.add_dependency(%q<safe_yaml>.freeze, ["~> 1.0"])
    s.add_dependency(%q<kramdown>.freeze, [">= 1.17", "< 3"])
  end
end
