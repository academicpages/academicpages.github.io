# -*- encoding: utf-8 -*-
# stub: rubyzip 2.3.2 ruby lib

Gem::Specification.new do |s|
  s.name = "rubyzip".freeze
  s.version = "2.3.2"

  s.required_rubygems_version = Gem::Requirement.new(">= 0".freeze) if s.respond_to? :required_rubygems_version=
  s.metadata = { "bug_tracker_uri" => "https://github.com/rubyzip/rubyzip/issues", "changelog_uri" => "https://github.com/rubyzip/rubyzip/blob/v2.3.2/Changelog.md", "documentation_uri" => "https://www.rubydoc.info/gems/rubyzip/2.3.2", "source_code_uri" => "https://github.com/rubyzip/rubyzip/tree/v2.3.2", "wiki_uri" => "https://github.com/rubyzip/rubyzip/wiki" } if s.respond_to? :metadata=
  s.require_paths = ["lib".freeze]
  s.authors = ["Alexander Simonov".freeze]
  s.date = "2021-07-05"
  s.email = ["alex@simonov.me".freeze]
  s.homepage = "http://github.com/rubyzip/rubyzip".freeze
  s.licenses = ["BSD 2-Clause".freeze]
  s.post_install_message = "RubyZip 3.0 is coming!\n**********************\n\nThe public API of some Rubyzip classes has been modernized to use named\nparameters for optional arguments. Please check your usage of the\nfollowing classes:\n  * `Zip::File`\n  * `Zip::Entry`\n  * `Zip::InputStream`\n  * `Zip::OutputStream`\n\nPlease ensure that your Gemfiles and .gemspecs are suitably restrictive\nto avoid an unexpected breakage when 3.0 is released (e.g. ~> 2.3.0).\nSee https://github.com/rubyzip/rubyzip for details. The Changelog also\nlists other enhancements and bugfixes that have been implemented since\nversion 2.3.0.\n".freeze
  s.required_ruby_version = Gem::Requirement.new(">= 2.4".freeze)
  s.rubygems_version = "3.0.3.1".freeze
  s.summary = "rubyzip is a ruby module for reading and writing zip files".freeze

  s.installed_by_version = "3.0.3.1" if s.respond_to? :installed_by_version

  if s.respond_to? :specification_version then
    s.specification_version = 4

    if Gem::Version.new(Gem::VERSION) >= Gem::Version.new('1.2.0') then
      s.add_development_dependency(%q<coveralls>.freeze, ["~> 0.7"])
      s.add_development_dependency(%q<minitest>.freeze, ["~> 5.4"])
      s.add_development_dependency(%q<pry>.freeze, ["~> 0.10"])
      s.add_development_dependency(%q<rake>.freeze, ["~> 12.3", ">= 12.3.3"])
      s.add_development_dependency(%q<rubocop>.freeze, ["~> 0.79"])
    else
      s.add_dependency(%q<coveralls>.freeze, ["~> 0.7"])
      s.add_dependency(%q<minitest>.freeze, ["~> 5.4"])
      s.add_dependency(%q<pry>.freeze, ["~> 0.10"])
      s.add_dependency(%q<rake>.freeze, ["~> 12.3", ">= 12.3.3"])
      s.add_dependency(%q<rubocop>.freeze, ["~> 0.79"])
    end
  else
    s.add_dependency(%q<coveralls>.freeze, ["~> 0.7"])
    s.add_dependency(%q<minitest>.freeze, ["~> 5.4"])
    s.add_dependency(%q<pry>.freeze, ["~> 0.10"])
    s.add_dependency(%q<rake>.freeze, ["~> 12.3", ">= 12.3.3"])
    s.add_dependency(%q<rubocop>.freeze, ["~> 0.79"])
  end
end
