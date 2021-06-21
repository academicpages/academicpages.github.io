begin
  require 'simplecov'
  require 'coveralls' if ENV['CI']
rescue LoadError
  # ignore
end

begin
  if RUBY_VERSION > '2.0'
    require 'byebug'
  else
    require 'debugger'
  end
rescue LoadError
  # ignore
end

require 'test/unit'
require 'jekyll/scholar'
require 'tmpdir'

TEST_DIR = File.join(Dir.tmpdir, 'jekyll')

def prepend_test_dir(options, key)
  if options.key?(key)
    if Pathname(options[key]).relative?
      options[key] = File.join(TEST_DIR, options[key])
    end
  else
    options[key] ||= TEST_DIR
  end
end

def run_jekyll(options = {})

  options = Jekyll.configuration(options)

  prepend_test_dir(options, 'source')
  prepend_test_dir(options, 'destination')

  print options['source'] + "\n"
  print options['destination'] + "\n"
  site = Jekyll::Site.new(options)
  site.process

end
