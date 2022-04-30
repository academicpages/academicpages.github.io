# frozen_string_literal: true

module JekyllRedirectFrom
  class Generator < Jekyll::Generator
    safe true
    attr_reader :site, :redirects

    def generate(site)
      @site = site
      @redirects = {}

      # Inject our layout, unless the user has already specified a redirect layout'
      unless site.layouts.key?("redirect")
        site.layouts["redirect"] = JekyllRedirectFrom::Layout.new(site)
      end

      # Must duplicate pages to modify while in loop
      (site.docs_to_write + site.pages.dup).each do |doc|
        next unless redirectable_document?(doc)

        generate_redirect_from(doc)
        generate_redirect_to(doc)
      end

      generate_redirects_json if generate_redirects_json?
    end

    private

    # For every `redirect_from` entry, generate a redirect page
    def generate_redirect_from(doc)
      doc.redirect_from.each do |path|
        page = RedirectPage.redirect_from(doc, path)
        doc.site.pages << page
        redirects[page.redirect_from] = page.redirect_to
      end
    end

    def generate_redirect_to(doc)
      return unless doc.redirect_to

      page = RedirectPage.redirect_to(doc, doc.redirect_to)
      doc.data.merge!(page.data)
      doc.content = doc.output = page.output
      redirects[page.redirect_from] = page.redirect_to
    end

    def generate_redirects_json
      return if File.exist? site.in_source_dir("redirects.json")

      page = PageWithoutAFile.new(site, "", "", "redirects.json")
      page.content = redirects.to_json
      page.data["layout"] = nil
      site.pages << page
    end

    def redirectable_document?(doc)
      doc.is_a?(Jekyll::Document) || doc.is_a?(Jekyll::Page)
    end

    def generate_redirects_json?
      site.config.dig("redirect_from", "json") != false
    end
  end
end
