# frozen_string_literal: true

HTML::Pipeline.require_dependency('rinku', 'AutolinkFilter')

module HTML
  class Pipeline
    # HTML Filter for auto_linking urls in HTML.
    #
    # Context options:
    #   :autolink  - boolean whether to autolink urls
    #   :link_mode - :all, :urls or :email_addresses
    #   :link_attr - HTML attributes for the link that will be generated
    #   :skip_tags - HTML tags inside which autolinking will be skipped.
    #                See Rinku.skip_tags
    #   :flags     - additional Rinku flags. See https://github.com/vmg/rinku
    #
    # This filter does not write additional information to the context.
    class AutolinkFilter < Filter
      def call
        return html if context[:autolink] == false

        skip_tags = context[:skip_tags]
        flags = 0
        flags |= context[:flags] if context[:flags]

        Rinku.auto_link(html, link_mode, context[:link_attr], skip_tags, flags)
      end

      def link_mode
        context[:link_mode] || :urls
      end
    end
  end
end
