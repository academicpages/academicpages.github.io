# frozen_string_literal: true

require 'set'

module HTML
  class Pipeline
    # HTML filter that replaces @org/team mentions with links. Mentions within
    # <pre>, <code>, <a>, <style>, and <script> elements are ignored.
    #
    # Context options:
    #   :base_url - Used to construct links to team profile pages for each
    #               mention.
    #   :team_pattern - Used to provide a custom regular expression to
    #                       identify team names
    #
    class TeamMentionFilter < Filter
      # Public: Find @org/team mentions in text.  See
      # TeamMentionFilter#team_mention_link_filter.
      #
      #   TeamMentionFilter.mentioned_teams_in(text) do |match, org, team|
      #     "<a href=...>#{team}</a>"
      #   end
      #
      # text - String text to search.
      #
      # Yields the String match, org name, and team name.  The yield's
      # return replaces the match in the original text.
      #
      # Returns a String replaced with the return of the block.
      def self.mentioned_teams_in(text, team_pattern = TeamPattern)
        text.gsub team_pattern do |match|
          org = $1
          team = $2
          yield match, org, team
        end
      end

      # Default pattern used to extract team names from text. The value can be
      # overridden by providing the team_pattern variable in the context. To
      # properly link the mention, should be in the format of /@(1)\/(2)/.
      TeamPattern = /
        (?<=^|\W)                  # beginning of string or non-word char
        @([a-z0-9][a-z0-9-]*)      # @organization
          \/                       # dividing slash
          ([a-z0-9][a-z0-9\-_]*)   # team
          \b
      /ix

      # Don't look for mentions in text nodes that are children of these elements
      IGNORE_PARENTS = %w[pre code a style script].to_set

      def call
        result[:mentioned_teams] ||= []

        doc.search('.//text()').each do |node|
          content = node.to_html
          next unless content.include?('@')
          next if has_ancestor?(node, IGNORE_PARENTS)
          html = mention_link_filter(content, base_url, team_pattern)
          next if html == content
          node.replace(html)
        end
        doc
      end

      def team_pattern
        context[:team_pattern] || TeamPattern
      end

      # Replace @org/team mentions in text with links to the mentioned team's
      # page.
      #
      # text      - String text to replace @mention team names in.
      # base_url  - The base URL used to construct team page URLs.
      # team_pattern  - Regular expression used to identify teams in text
      #
      # Returns a string with @team mentions replaced with links. All links have a
      # 'team-mention' class name attached for styling.
      def mention_link_filter(text, _base_url = '/', team_pattern = TeamPattern)
        self.class.mentioned_teams_in(text, team_pattern) do |match, org, team|
          link = link_to_mentioned_team(org, team)

          link ? match.sub("@#{org}/#{team}", link) : match
        end
      end

      def link_to_mentioned_team(org, team)
        result[:mentioned_teams] |= [team]

        url = base_url.dup
        url << '/' unless url =~ /[\/~]\z/
        
        "<a href='#{url << org}/#{team}' class='team-mention'>" \
          "@#{org}/#{team}" \
          '</a>'
      end
    end
  end
end
