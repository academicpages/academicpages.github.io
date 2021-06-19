require "rspec/core/rake_task"

desc "Run specs"
task :spec => ['spec:app', 'spec:lib']

namespace :spec do
  desc "Run only specs tagged 'solo'"
  RSpec::Core::RakeTask.new(:solo) do |t|
    t.verbose = false
    t.rspec_opts = %w(--color --tag solo)
  end

  desc "Run only specs tagged NOT tagged 'libraries' (for applications)"
  RSpec::Core::RakeTask.new(:app) do |t|
    t.verbose = false
    ENV["MONKEYPATCH_YAML"] = "true"
    t.rspec_opts = %w(--color --tag ~libraries)
  end

  desc "Run only specs tagged 'libraries'"
  RSpec::Core::RakeTask.new(:lib) do |t|
    t.verbose = false
    ENV["MONKEYPATCH_YAML"] = "false"
    t.rspec_opts = %w(--color --tag libraries)
  end
end
