# frozen-string-literal: true

module Jekyll
  module Converters
    class Markdown
      class CommonMark
        autoload :HtmlRenderer, "jekyll-commonmark/html_renderer"

        def initialize(config)
          Jekyll::External.require_with_graceful_fail "commonmarker"

          parse_keys  = CommonMarker::Config::OPTS[:parse].keys
          render_keys = CommonMarker::Config::OPTS[:render].keys

          options = setup_options(config, parse_keys, render_keys)
          options_set = Set.new(options)

          @extensions = setup_extensions(config)

          @parse_options  = (options_set & parse_keys).to_a
          @render_options = (options_set & render_keys).to_a

          @parse_options  = :DEFAULT if @parse_options.empty?
          @render_options = :DEFAULT if @render_options.empty?
        end

        def convert(content)
          HtmlRenderer.new(
            :options    => @render_options,
            :extensions => @extensions
          ).render(
            CommonMarker.render_doc(content, @parse_options, @extensions)
          )
        end

        private

        def validate(list, bucket, type)
          list.reject do |item|
            next if bucket.include?(item)

            Jekyll.logger.warn "CommonMark:", "#{item} is not a valid #{type}"
            Jekyll.logger.info "Valid #{type}s:", bucket.join(", ")
            true
          end
        end

        def setup_options(config, parse_keys, render_keys)
          options    = config["commonmark"]["options"].collect { |e| e.upcase.to_sym }
          valid_opts = Set.new(parse_keys + render_keys).to_a
          validate(options, valid_opts, "option")
        rescue NoMethodError
          []
        end

        def setup_extensions(config)
          extensions       = config["commonmark"]["extensions"].collect(&:to_sym)
          valid_extensions = CommonMarker.extensions.collect(&:to_sym)
          validate(extensions, valid_extensions, "extension")
        rescue NoMethodError
          []
        end
      end
    end
  end
end
