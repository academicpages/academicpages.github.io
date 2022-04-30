# frozen_string_literal: true

module Jekyll
  module Converters
    class Markdown
      class CommonMark
        class HtmlRenderer < CommonMarker::HtmlRenderer
          def code_block(node)
            block do
              lang = extract_code_lang(node.fence_info)

              out('<div class="')
              out("language-", lang, " ") if lang
              out('highlighter-rouge"><div class="highlight">')
              out("<pre", sourcepos(node), ' class="highlight"')

              if option_enabled?(:GITHUB_PRE_LANG)
                out_data_attr(lang)
                out("><code>")
              else
                out("><code")
                out_data_attr(lang)
                out(">")
              end
              out(render_with_rouge(node.string_content, lang))
              out("</code></pre></div></div>")
            end
          end

          private

          def extract_code_lang(info)
            return unless info.is_a?(String)
            return if info.empty?

            info.split(%r!\s+!)[0]
          end

          def out_data_attr(lang)
            return unless lang

            out(' data-lang="', lang, '"')
          end

          def render_with_rouge(code, lang)
            require "rouge"

            formatter = Rouge::Formatters::HTMLLegacy.new(
              :line_numbers => false,
              :wrap         => false,
              :css_class    => "highlight",
              :gutter_class => "gutter",
              :code_class   => "code"
            )
            lexer = Rouge::Lexer.find_fancy(lang, code) || Rouge::Lexers::PlainText
            formatter.format(lexer.lex(code))
          end
        end
      end
    end
  end
end
