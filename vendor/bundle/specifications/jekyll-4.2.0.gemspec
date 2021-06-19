# -*- encoding: utf-8 -*-
# stub: jekyll 4.2.0 ruby lib

Gem::Specification.new do |s|
  s.name = "jekyll".freeze
  s.version = "4.2.0"

  s.required_rubygems_version = Gem::Requirement.new(">= 2.7.0".freeze) if s.respond_to? :required_rubygems_version=
  s.metadata = { "bug_tracker_uri" => "https://github.com/jekyll/jekyll/issues", "changelog_uri" => "https://github.com/jekyll/jekyll/releases", "homepage_uri" => "https://jekyllrb.com", "source_code_uri" => "https://github.com/jekyll/jekyll" } if s.respond_to? :metadata=
  s.require_paths = ["lib".freeze]
  s.authors = ["Tom Preston-Werner".freeze, "Parker Moore".freeze, "Matt Rogers".freeze]
  s.bindir = "exe".freeze
  s.date = "2020-12-14"
  s.description = "Jekyll is a simple, blog aware, static site generator.".freeze
  s.email = ["maintainers@jekyllrb.com".freeze]
  s.executables = ["jekyll".freeze]
  s.extra_rdoc_files = ["README.markdown".freeze, "LICENSE".freeze]
  s.files = ["LICENSE".freeze, "README.markdown".freeze, "exe/jekyll".freeze]
  s.homepage = "https://jekyllrb.com".freeze
  s.licenses = ["MIT".freeze]
  s.rdoc_options = ["--charset=UTF-8".freeze]
  s.required_ruby_version = Gem::Requirement.new(">= 2.4.0".freeze)
  s.rubygems_version = "3.1.2".freeze
  s.summary = "A simple, blog aware, static site generator.".freeze

  s.installed_by_version = "3.1.2" if s.respond_to? :installed_by_version

  if s.respond_to? :specification_version then
    s.specification_version = 4
  end

  if s.respond_to? :add_runtime_dependency then
    s.add_runtime_dependency(%q<addressable>.freeze, ["~> 2.4"])
    s.add_runtime_dependency(%q<colorator>.freeze, ["~> 1.0"])
    s.add_runtime_dependency(%q<em-websocket>.freeze, ["~> 0.5"])
    s.add_runtime_dependency(%q<i18n>.freeze, ["~> 1.0"])
    s.add_runtime_dependency(%q<jekyll-sass-converter>.freeze, ["~> 2.0"])
    s.add_runtime_dependency(%q<jekyll-watch>.freeze, ["~> 2.0"])
    s.add_runtime_dependency(%q<kramdown>.freeze, ["~> 2.3"])
    s.add_runtime_dependency(%q<kramdown-parser-gfm>.freeze, ["~> 1.0"])
    s.add_runtime_dependency(%q<liquid>.freeze, ["~> 4.0"])
    s.add_runtime_dependency(%q<mercenary>.freeze, ["~> 0.4.0"])
    s.add_runtime_dependency(%q<pathutil>.freeze, ["~> 0.9"])
    s.add_runtime_dependency(%q<rouge>.freeze, ["~> 3.0"])
    s.add_runtime_dependency(%q<safe_yaml>.freeze, ["~> 1.0"])
    s.add_runtime_dependency(%q<terminal-table>.freeze, ["~> 2.0"])
  else
    s.add_dependency(%q<addressable>.freeze, ["~> 2.4"])
    s.add_dependency(%q<colorator>.freeze, ["~> 1.0"])
    s.add_dependency(%q<em-websocket>.freeze, ["~> 0.5"])
    s.add_dependency(%q<i18n>.freeze, ["~> 1.0"])
    s.add_dependency(%q<jekyll-sass-converter>.freeze, ["~> 2.0"])
    s.add_dependency(%q<jekyll-watch>.freeze, ["~> 2.0"])
    s.add_dependency(%q<kramdown>.freeze, ["~> 2.3"])
    s.add_dependency(%q<kramdown-parser-gfm>.freeze, ["~> 1.0"])
    s.add_dependency(%q<liquid>.freeze, ["~> 4.0"])
    s.add_dependency(%q<mercenary>.freeze, ["~> 0.4.0"])
    s.add_dependency(%q<pathutil>.freeze, ["~> 0.9"])
    s.add_dependency(%q<rouge>.freeze, ["~> 3.0"])
    s.add_dependency(%q<safe_yaml>.freeze, ["~> 1.0"])
    s.add_dependency(%q<terminal-table>.freeze, ["~> 2.0"])
  end
end
