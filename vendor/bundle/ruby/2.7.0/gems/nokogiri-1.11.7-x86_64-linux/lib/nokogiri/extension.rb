# frozen_string_literal: true

# load the C or Java extension
begin
  ::RUBY_VERSION =~ /(\d+\.\d+)/
  require "nokogiri/#{Regexp.last_match(1)}/nokogiri"
rescue LoadError => e
  if e.message =~ /GLIBC/
    warn(<<~EOM)

      ERROR: It looks like you're trying to use Nokogiri as a precompiled native gem on a system with glibc < 2.17:

        #{e.message}

        If that's the case, then please install Nokogiri via the `ruby` platform gem:
            gem install nokogiri --platform=ruby
        or:
            bundle config set force_ruby_platform true

        Please visit https://nokogiri.org/tutorials/installing_nokogiri.html for more help.

    EOM
    raise e
  end
  require 'nokogiri/nokogiri'
end
