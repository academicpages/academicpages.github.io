# -*- encoding: utf-8 -*-
# stub: unf_ext 0.0.8.2 ruby lib
# stub: ext/unf_ext/extconf.rb

Gem::Specification.new do |s|
  s.name = "unf_ext".freeze
  s.version = "0.0.8.2"

  s.required_rubygems_version = Gem::Requirement.new(">= 0".freeze) if s.respond_to? :required_rubygems_version=
  s.require_paths = ["lib".freeze]
  s.authors = ["Takeru Ohta".freeze, "Akinori MUSHA".freeze]
  s.date = "2022-05-26"
  s.description = "Unicode Normalization Form support library for CRuby".freeze
  s.email = ["knu@idaemons.org".freeze]
  s.extensions = ["ext/unf_ext/extconf.rb".freeze]
  s.extra_rdoc_files = ["LICENSE.txt".freeze, "README.md".freeze]
  s.files = ["LICENSE.txt".freeze, "README.md".freeze, "ext/unf_ext/extconf.rb".freeze]
  s.homepage = "https://github.com/knu/ruby-unf_ext".freeze
  s.licenses = ["MIT".freeze]
  s.required_ruby_version = Gem::Requirement.new(">= 2.2".freeze)
  s.rubygems_version = "3.0.3.1".freeze
  s.summary = "Unicode Normalization Form support library for CRuby".freeze

  s.installed_by_version = "3.0.3.1" if s.respond_to? :installed_by_version

  if s.respond_to? :specification_version then
    s.specification_version = 4

    if Gem::Version.new(Gem::VERSION) >= Gem::Version.new('1.2.0') then
      s.add_development_dependency(%q<rake>.freeze, [">= 0.9.2.2"])
      s.add_development_dependency(%q<test-unit>.freeze, [">= 0"])
      s.add_development_dependency(%q<rdoc>.freeze, ["> 2.4.2"])
      s.add_development_dependency(%q<bundler>.freeze, [">= 1.2"])
      s.add_development_dependency(%q<rake-compiler>.freeze, [">= 1.1.1"])
      s.add_development_dependency(%q<rake-compiler-dock>.freeze, [">= 1.2.1"])
    else
      s.add_dependency(%q<rake>.freeze, [">= 0.9.2.2"])
      s.add_dependency(%q<test-unit>.freeze, [">= 0"])
      s.add_dependency(%q<rdoc>.freeze, ["> 2.4.2"])
      s.add_dependency(%q<bundler>.freeze, [">= 1.2"])
      s.add_dependency(%q<rake-compiler>.freeze, [">= 1.1.1"])
      s.add_dependency(%q<rake-compiler-dock>.freeze, [">= 1.2.1"])
    end
  else
    s.add_dependency(%q<rake>.freeze, [">= 0.9.2.2"])
    s.add_dependency(%q<test-unit>.freeze, [">= 0"])
    s.add_dependency(%q<rdoc>.freeze, ["> 2.4.2"])
    s.add_dependency(%q<bundler>.freeze, [">= 1.2"])
    s.add_dependency(%q<rake-compiler>.freeze, [">= 1.1.1"])
    s.add_dependency(%q<rake-compiler-dock>.freeze, [">= 1.2.1"])
  end
end
