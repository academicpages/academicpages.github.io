# frozen_string_literal: true

module Jekyll
  # A Jekyll::Page subclass to manage the source map file associated with
  # a given scss / sass page.
  class SourceMapPage < Page
    # Initialize a new SourceMapPage.
    #
    # @param [Jekyll::Page] css_page The Page object that manages the css file.
    def initialize(css_page)
      @site = css_page.site
      @dir  = css_page.dir
      @data = css_page.data
      @name = css_page.basename + ".css.map"

      process(@name)
      Jekyll::Hooks.trigger :pages, :post_init, self
    end

    def source_map(map)
      self.content = map
    end

    def ext
      ".map"
    end

    def asset_file?
      true
    end

    # @return[String] the object as a debug String.
    def inspect
      "#<#{self.class} @name=#{name.inspect}>"
    end
  end
end
