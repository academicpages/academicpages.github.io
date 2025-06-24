# frozen_string_literal: true

require "jekyll"
require "jekyll-seo-tag/version"

module Jekyll
  class SeoTag < Liquid::Tag
    autoload :JSONLD,     "jekyll-seo-tag/json_ld"
    autoload :AuthorDrop, "jekyll-seo-tag/author_drop"
    autoload :ImageDrop,  "jekyll-seo-tag/image_drop"
    autoload :JSONLDDrop, "jekyll-seo-tag/json_ld_drop"
    autoload :UrlHelper,  "jekyll-seo-tag/url_helper"
    autoload :Drop,       "jekyll-seo-tag/drop"
    autoload :Filters,    "jekyll-seo-tag/filters"

    attr_accessor :context

    # Matches all whitespace that follows either
    #   1. A '}', which closes a Liquid tag
    #   2. A '{', which opens a JSON block
    #   3. A '>' followed by a newline, which closes an XML tag or
    #   4. A ',' followed by a newline, which ends a JSON line
    # We will strip all of this whitespace to minify the template
    # We will not strip any whitespace if the next character is a '-'
    #   so that we do not interfere with the HTML comment at the
    #   very begining
    MINIFY_REGEX = %r!(?<=[{}]|[>,]\n)\s+(?\!-)!.freeze

    def initialize(_tag_name, text, _tokens)
      super
      @text = text
    end

    def render(context)
      @context = context
      SeoTag.template.render!(payload, info)
    end

    private

    def options
      {
        "version" => Jekyll::SeoTag::VERSION,
        "title"   => title?,
      }
    end

    def payload
      # site_payload is an instance of UnifiedPayloadDrop. See https://git.io/v5ajm
      context.registers[:site].site_payload.tap do |site_payload|
        site_payload["page"]      = context.registers[:page]
        site_payload["paginator"] = context["paginator"]
        site_payload["seo_tag"]   = drop
      end
    end

    def drop
      if context.registers[:site].liquid_renderer.respond_to?(:cache)
        Jekyll::SeoTag::Drop.new(@text, @context)
      else
        @drop ||= Jekyll::SeoTag::Drop.new(@text, @context)
      end
    end

    def info
      {
        :registers => context.registers,
        :filters   => [Jekyll::Filters],
      }
    end

    class << self
      def template
        @template ||= Liquid::Template.parse template_contents
      end

      private

      def template_contents
        @template_contents ||= begin
          File.read(template_path).gsub(MINIFY_REGEX, "")
        end
      end

      def template_path
        @template_path ||= begin
          File.expand_path "./template.html", File.dirname(__FILE__)
        end
      end
    end
  end
end

Liquid::Template.register_tag("seo", Jekyll::SeoTag)
