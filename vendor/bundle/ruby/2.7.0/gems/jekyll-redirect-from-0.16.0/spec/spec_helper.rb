# frozen_string_literal: true

require "jekyll"
require File.expand_path("lib/jekyll-redirect-from.rb")

RSpec.configure do |config|
  config.run_all_when_everything_filtered = true
  config.filter_run :focus

  config.expect_with :rspec do |c|
    c.syntax = :expect
  end

  config.before(:each) do
    Jekyll.logger.log_level = :error
    dest_path.rmtree if dest_path.exist?
    site.reset
  end

  config.after(:each) do
    dest_path.rmtree if dest_path.exist?
  end

  def fixtures_path
    Pathname.new(__dir__).join("fixtures")
  end

  def dest_path
    Pathname.new(site.dest)
  end

  def dest_dir(*paths)
    dest_path.join(*paths)
  end

  def config
    Jekyll.configuration(
      "source"      => fixtures_path.to_s,
      "destination" => fixtures_path.join("_site").to_s,
      "collections" => {
        "articles" => { "output" => true },
        "authors"  => {},
      },
      "url"         => "http://jekyllrb.com",
      "plugins"     => [
        "jekyll-redirect-from",
        "jekyll-sitemap",
      ],
      "defaults"    => [{
        "scope"  => { "path" => "" },
        "values" => { "layout" => "layout" },
      }]
    )
  end

  def site
    @site ||= Jekyll::Site.new(config)
  end
end
