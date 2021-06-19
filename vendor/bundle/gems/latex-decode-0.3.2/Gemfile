source 'https://rubygems.org'
gemspec

group :test do
  gem 'rake'
  gem 'rspec', '~> 3.0'
  gem 'cucumber', '~> 1.3'
end

group :debug do
	gem 'debugger', :platforms => :mri_19
	gem 'byebug', :platforms => :mri if RUBY_VERSION > '2.0'

  gem 'rubinius-debugger', :require => false, :platforms => :rbx
  gem 'rubinius-compiler', :require => false, :platforms => :rbx
end

gem 'unicode', '~> 0.4', :platforms => [:mri, :rbx, :mswin, :mingw] if RUBY_VERSION < '2.4'
gem 'ritex', '~> 1.0.1'

gem 'rubysl', '~> 2.0', :platforms => :rbx
