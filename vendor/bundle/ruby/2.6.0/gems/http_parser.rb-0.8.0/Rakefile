require 'bundler/gem_tasks'

# default task
task :compile => :submodules
task :default => [:compile, :spec]

# load tasks
Dir['tasks/*.rake'].sort.each { |f| load f }
