# Contributed by @mfenner
# See https://github.com/inukshuk/jekyll-scholar/issues/30

require 'uri'

URL_PATTERN = Regexp.compile([
  '\\\\href\\\\{([^\\\\}]+)\\\\}\\\\{([^\\\\}]+)\\\\}',
  URI.regexp(['http', 'https', 'ftp'])
].join('|'))

module Jekyll
  class Scholar
    class Markdown < BibTeX::Filter
      def apply(value)
        value.to_s.gsub(URL_PATTERN) {
          if $1
            "[#{$2}](#{$1})"
          else
            "[#{$&}](#{$&})"
          end
        }
      end
    end
  end
end
