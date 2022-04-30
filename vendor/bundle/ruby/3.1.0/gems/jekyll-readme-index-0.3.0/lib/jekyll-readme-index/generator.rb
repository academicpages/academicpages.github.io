# frozen_string_literal: true

module JekyllReadmeIndex
  class Generator < Jekyll::Generator
    INDEX_REGEX = %r!$|index\.(html?|xhtml|xml)$!i.freeze

    attr_accessor :site

    safe true
    priority :low

    CONFIG_KEY = "readme_index"
    ENABLED_KEY = "enabled"
    CLEANUP_KEY = "remove_originals"
    FRONTMATTER_KEY = "with_frontmatter"

    def initialize(site)
      @site = site
    end

    def generate(site)
      @site = site
      return if disabled?

      readmes.each do |readme|
        next unless should_be_index?(readme)

        site.pages << readme.to_page
        site.static_files.delete(readme) if cleanup?
      end

      if with_frontmatter?
        readmes_with_frontmatter.each do |readme|
          next unless should_be_index?(readme)

          readme.update_permalink
        end
      end
    end

    private

    # Returns an array of all READMEs as StaticFiles
    def readmes
      site.static_files.select { |file| file.relative_path =~ readme_regex }
    end

    def readmes_with_frontmatter
      site.pages.select { |file| ("/" + file.path) =~ readme_regex }
    end

    # Should the given readme be the containing directory's index?
    def should_be_index?(readme)
      return false unless readme

      !dir_has_index? File.dirname(readme.url)
    end

    # Does the given directory have an index?
    #
    # relative_path - the directory path relative to the site root
    def dir_has_index?(relative_path)
      relative_path << "/" unless relative_path.end_with? "/"
      regex = %r!^#{Regexp.escape(relative_path)}#{INDEX_REGEX}!i
      (site.pages + site.static_files).any? { |file| file.url =~ regex }
    end

    # Regexp to match a file path against to detect if the given file is a README
    def readme_regex
      @readme_regex ||= %r!/readme(#{Regexp.union(markdown_converter.extname_list)})$!i
    end

    def markdown_converter
      @markdown_converter ||= site.find_converter_instance(Jekyll::Converters::Markdown)
    end

    def option(key)
      site.config[CONFIG_KEY] && site.config[CONFIG_KEY][key]
    end

    def disabled?
      option(ENABLED_KEY) == false
    end

    def cleanup?
      option(CLEANUP_KEY) == true
    end

    def with_frontmatter?
      option(FRONTMATTER_KEY) == true
    end
  end
end
