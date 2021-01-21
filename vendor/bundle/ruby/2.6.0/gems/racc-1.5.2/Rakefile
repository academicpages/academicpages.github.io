# -*- ruby -*-

require "bundler/gem_tasks"

require 'rdoc/task'

RDoc::Task.new(:docs) do |rd|
  spec = Gem::Specification.load("racc.gemspec")
  rd.main = "README.en.rdoc"
  rd.rdoc_files.include(spec.files.find_all { |file_name|
    file_name =~ /^(bin|lib|ext)/ || file_name !~ /\//
  })

  title = "#{spec.name}-#{spec.version} Documentation"

  rd.options << "-t #{title}"
end

require 'rake/testtask'

Rake::TestTask.new(:test) do |t|
  t.test_files = FileList["test/**/test_*.rb"]
  if RUBY_VERSION >= "2.6"
    t.ruby_opts = %w[--enable-frozen-string-literal --debug=frozen-string-literal]
  end
end
gem 'rake-compiler', '>= 0.4.1'

def java?
  /java/ === RUBY_PLATFORM
end
def jruby?
  Object.const_defined?(:RUBY_ENGINE) and 'jruby' == RUBY_ENGINE
end

file 'lib/racc/parser-text.rb' => ['lib/racc/parser.rb'] do |t|
  source = 'lib/racc/parser.rb'

  open(t.name, 'wb') { |io|
    io.write(<<-eorb)
module Racc
  PARSER_TEXT = <<'__end_of_file__'
#{File.read(source)}
__end_of_file__
end
    eorb
  }
end

if jruby?
  # JRUBY
  require "rake/javaextensiontask"
  Rake::JavaExtensionTask.new("cparse") do |ext|
    jruby_home = RbConfig::CONFIG['prefix']
    ext.lib_dir = File.join 'lib', 'racc'
    ext.ext_dir = File.join 'ext', 'racc'
    # source/target jvm
    ext.source_version = '1.6'
    ext.target_version = '1.6'
    jars = ["#{jruby_home}/lib/jruby.jar"] + FileList['lib/*.jar']
    ext.classpath = jars.map { |x| File.expand_path x }.join( ':' )
    ext.name = 'cparse-jruby'
  end

  task :compile => ['lib/racc/parser-text.rb']
else
  # MRI
  require "rake/extensiontask"
  Rake::ExtensionTask.new "cparse" do |ext|
    ext.lib_dir = File.join 'lib', 'racc'
    ext.ext_dir = File.join 'ext', 'racc', 'cparse'
  end

  task :compile => 'lib/racc/parser-text.rb'
end

task :build => "lib/racc/parser-text.rb"

task :test => :compile
