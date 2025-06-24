# frozen_string_literal: true

module JekyllDefaultLayout
  # Injects front matter defaults to set default layouts, if they exist
  class Generator < Jekyll::Generator
    attr_accessor :site

    safe true
    priority :lowest

    def initialize(site)
      @site = site
    end

    def generate(site)
      @site = site
      documents.each do |document|
        next unless should_set_layout?(document)

        document.data["layout"] = layout_for(document)
      end
    end

    def should_set_layout?(document)
      markdown?(document) && !layout_specified?(document)
    end

    # Does the given layout exist for the site?
    def layout_exists?(layout)
      !site.layouts[layout].nil?
    end

    # Has the user already specified a default for this layout?
    # Note: We must use `to_liquid`, and not data, to ensure front matter defaults
    def layout_specified?(document)
      document.to_liquid.key? "layout"
    end

    def markdown?(document)
      markdown_converter.matches(document.extname)
    end

    # What layout is appropriate for this document, if any
    # rubocop:disable Metrics/PerceivedComplexity
    def layout_for(document)
      if index?(document) && layout_exists?("home")
        "home"
      elsif page?(document) && layout_exists?("page")
        "page"
      elsif post?(document) && layout_exists?("post")
        "post"
      elsif layout_exists?("default")
        "default"
      end
    end
    # rubocop:enable Metrics/PerceivedComplexity

    def documents
      [site.pages, site.posts.docs].flatten
    end

    def markdown_converter
      @markdown_converter ||= site.find_converter_instance(Jekyll::Converters::Markdown)
    end

    def post?(document)
      document.is_a?(Jekyll::Document) && document.collection.label == "posts"
    end

    def page?(document)
      document.is_a?(Jekyll::Page)
    end

    def index?(document)
      document.url == "/"
    end
  end
end
