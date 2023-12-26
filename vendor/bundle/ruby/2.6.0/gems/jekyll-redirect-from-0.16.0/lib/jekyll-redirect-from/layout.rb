# frozen_string_literal: true

module JekyllRedirectFrom
  # A stubbed layout for our default redirect template
  # We cannot use the standard Layout class because of site.in_source_dir
  class Layout < Jekyll::Layout
    def initialize(site)
      @site = site
      @base = __dir__
      @name = "redirect.html"
      @path = File.expand_path(@name, @base)
      @relative_path = "_layouts/redirect.html"

      self.data = {}
      self.ext = "html"
      self.content = File.read(@path)
    end
  end
end
