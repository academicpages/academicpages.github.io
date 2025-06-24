begin
  require "bundler/gem_tasks"
rescue LoadError
end

require "rake/testtask"
Rake::TestTask.new(:test) do |t|
  t.libs << "test/lib"
  t.ruby_opts << "-rhelper"
  t.test_files = FileList["test/**/test_*.rb"]
end

require "rdoc/task"
RDoc::Task.new do |doc|
  doc.main   = "README.md"
  doc.title  = "Logger -- Ruby Standard Logger"
  doc.rdoc_files = FileList.new %w[README.md lib BSDL COPYING]
  doc.rdoc_dir = "html"
end

task "gh-pages" => :rdoc do
  %x[git checkout gh-pages]
  require "fileutils"
  FileUtils.rm_rf "/tmp/html"
  FileUtils.mv "html", "/tmp"
  FileUtils.rm_rf "*"
  FileUtils.cp_r Dir.glob("/tmp/html/*"), "."
end

task :default => :test
