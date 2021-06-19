# frozen_string_literal: true

module Jekyll
  module Commands
    module Watch
      extend self

      def init_with_program(prog); end

      # Build your jekyll site
      # Continuously watch if `watch` is set to true in the config.
      def process(options)
        Jekyll.logger.log_level = :error if options["quiet"]
        Jekyll::Watcher.watch(options) if options["watch"]
      end
    end
  end
end
