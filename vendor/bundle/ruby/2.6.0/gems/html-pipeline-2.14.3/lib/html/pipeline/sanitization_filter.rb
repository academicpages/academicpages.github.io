# frozen_string_literal: true

HTML::Pipeline.require_dependency('sanitize', 'SanitizationFilter')

module HTML
  class Pipeline
    # HTML filter with sanization routines and allowlists. This module defines
    # what HTML is allowed in user provided content and fixes up issues with
    # unbalanced tags and whatnot.
    #
    # See the Sanitize docs for more information on the underlying library:
    #
    # https://github.com/rgrove/sanitize/#readme
    #
    # Context options:
    #   :allowlist      - The sanitizer allowlist configuration to use. This
    #                     can be one of the options constants defined in this
    #                     class or a custom sanitize options hash.
    #   :anchor_schemes - The URL schemes to allow in <a href> attributes. The
    #                     default set is provided in the ANCHOR_SCHEMES
    #                     constant in this class. If passed, this overrides any
    #                     schemes specified in the allowlist configuration.
    #
    # This filter does not write additional information to the context.
    class SanitizationFilter < Filter
      LISTS     = Set.new(%w[ul ol].freeze)
      LIST_ITEM = 'li'.freeze

      # List of table child elements. These must be contained by a <table> element
      # or they are not allowed through. Otherwise they can be used to break out
      # of places we're using tables to contain formatted user content (like pull
      # request review comments).
      TABLE_ITEMS = Set.new(%w[tr td th].freeze)
      TABLE = 'table'.freeze
      TABLE_SECTIONS = Set.new(%w[thead tbody tfoot].freeze)

      # These schemes are the only ones allowed in <a href> attributes by default.
      ANCHOR_SCHEMES = ['http', 'https', 'mailto', 'xmpp', :relative, 'github-windows', 'github-mac', 'irc', 'ircs'].freeze

      # The main sanitization allowlist. Only these elements and attributes are
      # allowed through by default.
      ALLOWLIST = {
        elements: %w[
          h1 h2 h3 h4 h5 h6 h7 h8 br b i strong em a pre code img tt
          div ins del sup sub p ol ul table thead tbody tfoot blockquote
          dl dt dd kbd q samp var hr ruby rt rp li tr td th s strike summary
          details caption figure figcaption
          abbr bdo cite dfn mark small span time wbr
        ].freeze,
        remove_contents: ['script'].freeze,
        attributes: {
          'a'          => ['href'].freeze,
          'img'        => %w[src longdesc].freeze,
          'div'        => %w[itemscope itemtype].freeze,
          'blockquote' => ['cite'].freeze,
          'del'        => ['cite'].freeze,
          'ins'        => ['cite'].freeze,
          'q'          => ['cite'].freeze,
          all: %w[abbr accept accept-charset
                  accesskey action align alt
                  aria-describedby aria-hidden aria-label aria-labelledby
                  axis border cellpadding cellspacing char
                  charoff charset checked
                  clear cols colspan color
                  compact coords datetime dir
                  disabled enctype for frame
                  headers height hreflang
                  hspace ismap label lang
                  maxlength media method
                  multiple name nohref noshade
                  nowrap open progress prompt readonly rel rev
                  role rows rowspan rules scope
                  selected shape size span
                  start summary tabindex target
                  title type usemap valign value
                  vspace width itemprop].freeze
        }.freeze,
        protocols: {
          'a'          => { 'href' => ANCHOR_SCHEMES }.freeze,
          'blockquote' => { 'cite' => ['http', 'https', :relative].freeze },
          'del'        => { 'cite' => ['http', 'https', :relative].freeze },
          'ins'        => { 'cite' => ['http', 'https', :relative].freeze },
          'q'          => { 'cite' => ['http', 'https', :relative].freeze },
          'img'        => {
            'src'      => ['http', 'https', :relative].freeze,
            'longdesc' => ['http', 'https', :relative].freeze
          }.freeze
        },
        transformers: [
          # Top-level <li> elements are removed because they can break out of
          # containing markup.
          lambda { |env|
            name = env[:node_name]
            node = env[:node]
            if name == LIST_ITEM && node.ancestors.none? { |n| LISTS.include?(n.name) }
              node.replace(node.children)
            end
          },

          # Table child elements that are not contained by a <table> are removed.
          lambda { |env|
            name = env[:node_name]
            node = env[:node]
            if (TABLE_SECTIONS.include?(name) || TABLE_ITEMS.include?(name)) && node.ancestors.none? { |n| n.name == TABLE }
              node.replace(node.children)
            end
          }
        ].freeze
      }.freeze

      # A more limited sanitization allowlist. This includes all attributes,
      # protocols, and transformers from ALLOWLIST but with a more locked down
      # set of allowed elements.
      LIMITED = ALLOWLIST.merge(
        elements: %w[b i strong em a pre code img ins del sup sub mark abbr p ol ul li]
      )

      # Strip all HTML tags from the document.
      FULL = { elements: [] }.freeze

      # Sanitize markup using the Sanitize library.
      def call
        Sanitize.clean_node!(doc, allowlist)
      end

      def whitelist
        warn "[DEPRECATION] 'whitelist' is deprecated. Please use 'allowlist' instead."
        allowlist
      end

      # The allowlist to use when sanitizing. This can be passed in the context
      # hash to the filter but defaults to ALLOWLIST constant value above.
      def allowlist
        allowlist = context[:allowlist] || context[:whitelist] || ALLOWLIST
        anchor_schemes = context[:anchor_schemes]
        return allowlist unless anchor_schemes
        allowlist = allowlist.dup
        allowlist[:protocols] = (allowlist[:protocols] || {}).dup
        allowlist[:protocols]['a'] = (allowlist[:protocols]['a'] || {}).merge('href' => anchor_schemes)
        allowlist
      end
    end
  end
end
