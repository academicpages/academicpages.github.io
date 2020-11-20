# frozen_string_literal: true

require "zlib"

module Jekyll
  class Avatar < Liquid::Tag
    include Jekyll::LiquidExtensions

    SERVERS      = 4
    DEFAULT_SIZE = 40
    API_VERSION  = 3

    def initialize(_tag_name, text, _tokens)
      super
      @text = text
    end

    def render(context)
      @context = context
      @text    = Liquid::Template.parse(@text).render(@context)
      attrs    = attributes.map { |k, v| "#{k}=\"#{v}\"" }.join(" ")
      "<img #{attrs} />"
    end

    private

    def attributes
      result = {
        :class                => classes,
        :alt                  => username,
        :width                => size,
        :height               => size,
        "data-proofer-ignore" => true
      }

      if lazy_load?
        result[:src] = ""
        result["data-src"] = url
        result["data-srcset"] = srcset
      else
        result[:src] = url
        result[:srcset] = srcset
      end

      result
    end

    def lazy_load?
      @text.include?("lazy=true")
    end

    def username
      matches = @text.match(%r!\buser=([\w\.]+)\b!)
      if matches
        lookup_variable(@context, matches[1])
      else
        @text.split(" ").first.sub("@", "")
      end
    end

    def size
      matches = @text.match(%r!\bsize=(\d+)\b!i)
      matches ? matches[1].to_i : DEFAULT_SIZE
    end

    def path(scale = 1)
      "#{username}?v=#{API_VERSION}&s=#{size * scale}"
    end

    def server_number
      Zlib.crc32(path) % SERVERS
    end

    def host
      if ENV["PAGES_AVATARS_URL"].is_a?(String) && !ENV["PAGES_AVATARS_URL"].empty?
        ENV["PAGES_AVATARS_URL"]
      else
        "https://avatars#{server_number}.githubusercontent.com"
      end
    end

    def parsed_host
      @parsed_host ||= {}
      @parsed_host[host] ||= Addressable::URI.parse(host)
    end

    def url(scale = 1)
      uri = parsed_host
      uri.path << "/" unless uri.path.end_with?("/")
      uri = uri.join path(scale)
      uri.to_s
    end

    def srcset
      (1..4).map { |scale| "#{url(scale)} #{scale}x" }.join(", ")
    end

    # See http://primercss.io/avatars/#small-avatars
    def classes
      size < 48 ? "avatar avatar-small" : "avatar"
    end
  end
end

Liquid::Template.register_tag("avatar", Jekyll::Avatar)
