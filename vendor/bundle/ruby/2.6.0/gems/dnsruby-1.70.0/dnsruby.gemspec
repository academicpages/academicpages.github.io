lib = File.expand_path('../lib', __FILE__)
$LOAD_PATH.unshift(lib) unless $LOAD_PATH.include?(lib)
require 'dnsruby/version'

SPEC = Gem::Specification.new do |s|
  s.name = "dnsruby"
  s.version = Dnsruby::VERSION
  s.authors = ["Alex Dalitz"]
  s.email = 'alex@caerkettontech.com'
  s.homepage = "https://github.com/alexdalitz/dnsruby"
  s.platform = Gem::Platform::RUBY
  s.summary = "Ruby DNS(SEC) implementation"
  s.description = \
'Dnsruby is a pure Ruby DNS client library which implements a
stub resolver. It aims to comply with all DNS RFCs, including
DNSSEC NSEC3 support.'
  s.license = "Apache License, Version 2.0"
  
  s.files = `git ls-files -z`.split("\x0")

  s.post_install_message = \
"Installing dnsruby...
  For issues and source code: https://github.com/alexdalitz/dnsruby
  For general discussion (please tell us how you use dnsruby): https://groups.google.com/forum/#!forum/dnsruby"

  s.test_file = "test/ts_offline.rb"
  s.extra_rdoc_files = ["DNSSEC", "EXAMPLES", "README.md", "EVENTMACHINE"]

  s.metadata = {
    'yard.run'          => 'yard',
    'bug_tracker_uri'   => 'https://github.com/alexdalitz/dnsruby/issues',
    'changelog_uri'     => 'https://github.com/alexdalitz/dnsruby/blob/master/RELEASE_NOTES.md',
    'documentation_uri' => 'https://www.rubydoc.info/gems/dnsruby/',
    'homepage_uri'      => 'https://github.com/alexdalitz/dnsruby',
    'source_code_uri'   => 'https://github.com/alexdalitz/dnsruby',
  }

  s.add_development_dependency 'rake', '>= 13.0.6'
  s.add_development_dependency 'minitest', '~> 5.18.0'
  s.add_development_dependency 'rubydns', '>= 2.0.2'
  s.add_development_dependency 'nio4r', '>= 2.5.8'
  s.add_development_dependency 'minitest-display', '>= 0.3.1'
  s.add_development_dependency('yard', '>= 0.9')
  # s.add_development_dependency('io-event', '>=1.1.7')

  if RUBY_VERSION >= "1.9.3"
    s.add_development_dependency 'coveralls', '~> 0.8.23'
  end

  s.add_runtime_dependency 'simpleidn', '~> 0.2.1'
end
