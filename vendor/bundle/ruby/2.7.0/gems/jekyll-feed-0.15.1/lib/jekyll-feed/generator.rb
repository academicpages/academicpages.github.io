# frozen_string_literal: true

module JekyllFeed
  class Generator < Jekyll::Generator
    safe true
    priority :lowest

    # Main plugin action, called by Jekyll-core
    def generate(site)
      @site = site
      collections.each do |name, meta|
        Jekyll.logger.info "Jekyll Feed:", "Generating feed for #{name}"
        (meta["categories"] + [nil]).each do |category|
          path = feed_path(:collection => name, :category => category)
          next if file_exists?(path)

          @site.pages << make_page(path, :collection => name, :category => category)
        end
      end
      generate_feed_by_tag if config["tags"] && !@site.tags.empty?
    end

    private

    # Matches all whitespace that follows
    #   1. A '>', which closes an XML tag or
    #   2. A '}', which closes a Liquid tag
    # We will strip all of this whitespace to minify the template
    MINIFY_REGEX = %r!(?<=>|})\s+!.freeze

    # Returns the plugin's config or an empty hash if not set
    def config
      @config ||= @site.config["feed"] || {}
    end

    # Determines the destination path of a given feed
    #
    # collection - the name of a collection, e.g., "posts"
    # category - a category within that collection, e.g., "news"
    #
    # Will return "/feed.xml", or the config-specified default feed for posts
    # Will return `/feed/category.xml` for post categories
    # WIll return `/feed/collection.xml` for other collections
    # Will return `/feed/collection/category.xml` for other collection categories
    def feed_path(collection: "posts", category: nil)
      prefix = collection == "posts" ? "/feed" : "/feed/#{collection}"
      return "#{prefix}/#{category}.xml" if category

      collections.dig(collection, "path") || "#{prefix}.xml"
    end

    # Returns a hash representing all collections to be processed and their metadata
    # in the form of { collection_name => { categories = [...], path = "..." } }
    def collections
      return @collections if defined?(@collections)

      @collections = if config["collections"].is_a?(Array)
                       config["collections"].map { |c| [c, {}] }.to_h
                     elsif config["collections"].is_a?(Hash)
                       config["collections"]
                     else
                       {}
                     end

      @collections = normalize_posts_meta(@collections)
      @collections.each_value do |meta|
        meta["categories"] = (meta["categories"] || []).to_set
      end

      @collections
    end

    def generate_feed_by_tag
      tags_config = config["tags"]
      tags_config = {} unless tags_config.is_a?(Hash)

      except    = tags_config["except"] || []
      only      = tags_config["only"] || @site.tags.keys
      tags_pool = only - except
      tags_path = tags_config["path"] || "/feed/by_tag/"

      generate_tag_feed(tags_pool, tags_path)
    end

    def generate_tag_feed(tags_pool, tags_path)
      tags_pool.each do |tag|
        # allow only tags with basic alphanumeric characters and underscore to keep
        # feed path simple.
        next if %r![^a-zA-Z0-9_]!.match?(tag)

        Jekyll.logger.info "Jekyll Feed:", "Generating feed for posts tagged #{tag}"
        path = "#{tags_path}#{tag}.xml"
        next if file_exists?(path)

        @site.pages << make_page(path, :tags => tag)
      end
    end

    # Path to feed.xml template file
    def feed_source_path
      @feed_source_path ||= File.expand_path "feed.xml", __dir__
    end

    def feed_template
      @feed_template ||= File.read(feed_source_path).gsub(MINIFY_REGEX, "")
    end

    # Checks if a file already exists in the site source
    def file_exists?(file_path)
      File.exist? @site.in_source_dir(file_path)
    end

    # Generates contents for a file

    def make_page(file_path, collection: "posts", category: nil, tags: nil)
      PageWithoutAFile.new(@site, __dir__, "", file_path).tap do |file|
        file.content = feed_template
        file.data.merge!(
          "layout"     => nil,
          "sitemap"    => false,
          "xsl"        => file_exists?("feed.xslt.xml"),
          "collection" => collection,
          "category"   => category,
          "tags"       => tags
        )
        file.output
      end
    end

    # Special case the "posts" collection, which, for ease of use and backwards
    # compatability, can be configured via top-level keys or directly as a collection
    def normalize_posts_meta(hash)
      hash["posts"] ||= {}
      hash["posts"]["path"] ||= config["path"]
      hash["posts"]["categories"] ||= config["categories"]
      config["path"] ||= hash["posts"]["path"]
      hash
    end
  end
end
