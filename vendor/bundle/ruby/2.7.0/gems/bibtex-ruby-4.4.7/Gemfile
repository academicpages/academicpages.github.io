source 'https://rubygems.org'
gemspec

gem 'json', '~>1.8', :platforms => [:mri_18, :jruby, :rbx]

if RUBY_VERSION >= '2.0'
  gem 'rdf', '~>2.0.0'
  gem 'rdf-vocab', '~>2.0.0'
else
  gem 'rdf', '~>1.1'
end

gem 'rubysl', '~>2.0', :platforms => :rbx

group :debug do
  if RUBY_VERSION >= '2.0'
    gem 'byebug', :require => false, :platforms => :mri
  else
    gem 'debugger', :require => false, :platforms => :mri
  end

  gem 'ruby-debug', :require => false, :platforms => :jruby

  gem 'rubinius-debugger', :require => false, :platforms => :rbx
  gem 'rubinius-compiler', :require => false, :platforms => :rbx
end

group :test do
	gem 'minitest', '~>4.7', :require => false
  gem 'rubysl-test-unit', '~>2.0', :platforms => :rbx
  gem 'minitest-ansi'
  gem 'cucumber', '~>1.3'
  gem 'unicode', '~>0.4', :platforms => [:rbx, :mswin, :mingw, :mri]
end

group :extra do
  if RUBY_PLATFORM =~ /darwin/i
	  gem 'rb-fsevent', :require => false
  end

	gem 'guard-minitest', :platforms => [:ruby]
	gem 'guard-cucumber', :platforms => [:ruby]
	gem 'redcarpet', :platforms => [:ruby]
end

group :profile do
	gem 'ruby-prof', '~>0.14', :platforms => [:mri]
	gem 'gnuplot', '~>2.4', :platforms => [:mri]
end

group :coverage do
	gem 'simplecov', '~>0.8', :require => false, :platforms => [:ruby]
  gem 'rubinius-coverage', :require => false, :platforms => :rbx
  gem 'coveralls', '~>0.7', :require => false
end

group :development do
  gem 'rake'
  gem 'yard'
  gem 'iconv', :platforms => [:ruby]
end

group :travis do
  # Gem is required at runtime for RBX!
  gem 'racc', :platforms => [:ruby]
end
