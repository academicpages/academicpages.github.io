# frozen_string_literal: true

module JekyllTitlesFromHeadings
  class Generator < Jekyll::Generator
    attr_accessor :site
    TITLE_REGEX =
      %r!
        \A\s*                             # Beginning and whitespace
          (?:                             # either
            \#{1,3}\s+(.*)(?:\s+\#{1,3})? # atx-style header
            |                             # or
            (.*)\r?\n[-=]+\s*             # Setex-style header
          )$                              # end of line
      !x.freeze

    CONVERTER_CLASS = Jekyll::Converters::Markdown
    STRIP_MARKUP_FILTERS = [:markdownify, :strip_html, :normalize_whitespace].freeze

    # Regex to strip extra markup still present after markdownify
    # (footnotes at the moment).
    EXTRA_MARKUP_REGEX = %r!\[\^[^\]]*\]!.freeze

    CONFIG_KEY = "titles_from_headings"
    ENABLED_KEY = "enabled"
    STRIP_TITLE_KEY = "strip_title"
    COLLECTIONS_KEY = "collections"

    safe true
    priority :lowest

    def initialize(site)
      @site = site
    end

    def generate(site)
      @site = site
      return if disabled?

      documents = site.pages
      documents = site.pages + site.docs_to_write if collections?

      documents.each do |document|
        next unless should_add_title?(document)
        next if document.is_a?(Jekyll::StaticFile)

        document.data["title"] = title_for(document)
        strip_title!(document) if strip_title?(document)
      end
    end

    def should_add_title?(document)
      markdown?(document) && !title?(document)
    end

    def title?(document)
      !inferred_title?(document) && !document.data["title"].nil?
    end

    def markdown?(document)
      markdown_converter.matches(document.extname)
    end

    def markdown_converter
      @markdown_converter ||= site.find_converter_instance(CONVERTER_CLASS)
    end

    def title_for(document)
      return document.data["title"] if title?(document)

      matches = document.content.to_s.match(TITLE_REGEX)
      return strip_markup(matches[1] || matches[2]) if matches

      document.data["title"] # If we cant match a title, we use the inferred one.
    rescue ArgumentError => e
      raise e unless e.to_s.start_with?("invalid byte sequence in UTF-8")
    end

    private

    def strip_markup(string)
      STRIP_MARKUP_FILTERS.reduce(string) do |memo, method|
        filters.public_send(method, memo)
      end.gsub(EXTRA_MARKUP_REGEX, "")
    end

    def option(key)
      site.config[CONFIG_KEY] && site.config[CONFIG_KEY][key]
    end

    def disabled?
      option(ENABLED_KEY) == false
    end

    def strip_title?(document)
      if document.data.key?(STRIP_TITLE_KEY)
        document.data[STRIP_TITLE_KEY] == true
      else
        option(STRIP_TITLE_KEY) == true
      end
    end

    def strip_title_excerpt?(document)
      document.is_a?(Jekyll::Document) &&
        document.collection.label == "posts" &&
        document.generate_excerpt?
    end

    def collections?
      option(COLLECTIONS_KEY) == true
    end

    # Documents (posts and collection items) have their title inferred from the filename.
    # We want to override these titles, because they were not excplicitly set.
    def inferred_title?(document)
      document.is_a?(Jekyll::Document)
    end

    def strip_title!(document)
      if document.content
        document.content = document.content.gsub(TITLE_REGEX, "").strip
        strip_title_excerpt!(document) if strip_title_excerpt?(document)
      end
    end

    def strip_title_excerpt!(document)
      document.data["excerpt"] = Jekyll::Excerpt.new(document)
    end

    def filters
      @filters ||= JekyllTitlesFromHeadings::Filters.new(site)
    end
  end
end
