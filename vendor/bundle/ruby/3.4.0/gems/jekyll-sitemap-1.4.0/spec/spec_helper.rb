# frozen_string_literal: true

require "jekyll"
require "fileutils"
require File.expand_path("../lib/jekyll-sitemap", __dir__)

Jekyll.logger.log_level = :error

RSpec.configure do |config|
  config.run_all_when_everything_filtered = true
  config.filter_run :focus
  config.order = "random"

  SOURCE_DIR = File.expand_path("fixtures", __dir__)
  DEST_DIR   = File.expand_path("dest", __dir__)
  ROBOT_FIXTURES = File.expand_path("robot-fixtures", __dir__)
  ROBOT_FIXTURE_ITEMS = %w(_posts _layouts _config.yml index.html).freeze

  def source_dir(*files)
    File.join(SOURCE_DIR, *files)
  end

  def dest_dir(*files)
    File.join(DEST_DIR, *files)
  end

  def robot_fixtures(*subdirs)
    File.join(ROBOT_FIXTURES, *subdirs)
  end

  def setup_fixture(directory)
    ROBOT_FIXTURE_ITEMS.each { |item| FileUtils.cp_r(source_dir(item), robot_fixtures(directory)) }
  end

  def cleanup_fixture(directory, dest_dirname = "_site")
    (ROBOT_FIXTURE_ITEMS + [dest_dirname]).each do |item|
      FileUtils.remove_entry(robot_fixtures(directory, item))
    end
  end
end
