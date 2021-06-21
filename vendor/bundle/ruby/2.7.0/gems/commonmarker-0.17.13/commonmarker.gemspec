# encoding: utf-8
lib = File.expand_path('../lib', __FILE__)
$LOAD_PATH.unshift(lib) unless $LOAD_PATH.include?(lib)
require 'commonmarker/version'

Gem::Specification.new do |s|
  s.name = 'commonmarker'
  s.version = CommonMarker::VERSION
  s.summary = 'CommonMark parser and renderer. Written in C, wrapped in Ruby.'
  s.description = 'A fast, safe, extensible parser for CommonMark. This wraps the official libcmark library.'
  s.authors       = ['Garen Torikian', 'Ashe Connor']
  s.homepage = 'http://github.com/gjtorikian/commonmarker'
  s.license = 'MIT'
  s.required_ruby_version = '>= 2.0.0'

  s.files         = %w(LICENSE.txt README.md Rakefile commonmarker.gemspec bin/commonmarker)
  s.files        += Dir.glob('lib/**/*.rb')
  s.files        += Dir.glob('ext/commonmarker/*.*')
  s.test_files    = Dir.glob('test/**/*')
  s.extensions    = ['ext/commonmarker/extconf.rb']

  s.test_files = s.files.grep(%r{^test/})
  s.executables = ['commonmarker']
  s.require_paths = %w(lib ext)

  s.rdoc_options += ['-x', 'ext/commonmarker/cmark/.*']

  s.add_dependency 'ruby-enum', '~> 0.5'

  s.add_development_dependency 'minitest', '~> 5.6'
  s.add_development_dependency 'rake-compiler', '~> 0.9'
  s.add_development_dependency 'bundler', '~> 1.2'
  s.add_development_dependency 'json', '~> 1.8.1'
  s.add_development_dependency 'awesome_print'
  s.add_development_dependency 'rdoc', '~> 5.1'
end
