# frozen_string_literal: true

require 'set'

module HTML
  class Pipeline
    # HTML filter that replaces @user mentions with links. Mentions within <pre>,
    # <code>, and <a> elements are ignored. Mentions that reference users that do
    # not exist are ignored.
    #
    # Context options:
    #   :base_url - Used to construct links to user profile pages for each
    #               mention.
    #   :info_url - Used to link to "more info" when someone mentions @mention
    #               or @mentioned.
    #   :username_pattern - Used to provide a custom regular expression to
    #                       identify usernames
    #
    class MentionFilter < Filter
      # Public: Find user @mentions in text.  See
      # MentionFilter#mention_link_filter.
      #
      #   MentionFilter.mentioned_logins_in(text) do |match, login, is_mentioned|
      #     "<a href=...>#{login}</a>"
      #   end
      #
      # text - String text to search.
      #
      # Yields the String match, the String login name, and a Boolean determining
      # if the match = "@mention[ed]".  The yield's return replaces the match in
      # the original text.
      #
      # Returns a String replaced with the return of the block.
      def self.mentioned_logins_in(text, username_pattern = UsernamePattern)
        text.gsub MentionPatterns[username_pattern] do |match|
          login = Regexp.last_match(1)
          yield match, login, MentionLogins.include?(login.downcase)
        end
      end

      # Hash that contains all of the mention patterns used by the pipeline
      MentionPatterns = Hash.new do |hash, key|
        hash[key] = /
          (?:^|\W)                    # beginning of string or non-word char
          @((?>#{key}))  # @username
          (?!\/)                      # without a trailing slash
          (?=
            \.+[ \t\W]|               # dots followed by space or non-word character
            \.+$|                     # dots at end of line
            [^0-9a-zA-Z_.]|           # non-word character except dot
            $                         # end of line
          )
        /ix
      end

      # Default pattern used to extract usernames from text. The value can be
      # overriden by providing the username_pattern variable in the context.
      UsernamePattern = /[a-z0-9][a-z0-9-]*/

      # List of username logins that, when mentioned, link to the blog post
      # about @mentions instead of triggering a real mention.
      MentionLogins = %w[
        mention
        mentions
        mentioned
        mentioning
      ].freeze

      # Don't look for mentions in text nodes that are children of these elements
      IGNORE_PARENTS = %w(pre code a style script).to_set

      def call
        result[:mentioned_usernames] ||= []

        doc.search('.//text()').each do |node|
          content = node.to_html
          next unless content.include?('@')
          next if has_ancestor?(node, IGNORE_PARENTS)
          html = mention_link_filter(content, base_url, info_url, username_pattern)
          next if html == content
          node.replace(html)
        end
        doc
      end

      # The URL to provide when someone @mentions a "mention" name, such
      # as @mention or @mentioned, that will give them more info on mentions.
      def info_url
        context[:info_url] || nil
      end

      def username_pattern
        context[:username_pattern] || UsernamePattern
      end

      # Replace user @mentions in text with links to the mentioned user's
      # profile page.
      #
      # text      - String text to replace @mention usernames in.
      # base_url  - The base URL used to construct user profile URLs.
      # info_url  - The "more info" URL used to link to more info on @mentions.
      #             If nil we don't link @mention or @mentioned.
      # username_pattern  - Regular expression used to identify usernames in
      #                     text
      #
      # Returns a string with @mentions replaced with links. All links have a
      # 'user-mention' class name attached for styling.
      def mention_link_filter(text, _base_url = '/', info_url = nil, username_pattern = UsernamePattern)
        self.class.mentioned_logins_in(text, username_pattern) do |match, login, is_mentioned|
          link =
            if is_mentioned
              link_to_mention_info(login, info_url)
            else
              link_to_mentioned_user(login)
            end

          link ? match.sub("@#{login}", link) : match
        end
      end

      def link_to_mention_info(text, info_url = nil)
        return "@#{text}" if info_url.nil?
        "<a href='#{info_url}' class='user-mention'>" \
          "@#{text}" \
          '</a>'
      end

      def link_to_mentioned_user(login)
        result[:mentioned_usernames] |= [login]

        url = base_url.dup
        url << '/' unless url =~ /[\/~]\z/

        "<a href='#{url << login}' class='user-mention'>" \
          "@#{login}" \
          '</a>'
      end
    end
  end
end
