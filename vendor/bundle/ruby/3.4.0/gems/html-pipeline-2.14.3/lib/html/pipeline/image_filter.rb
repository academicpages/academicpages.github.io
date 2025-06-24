# frozen_string_literal: true

module HTML
  class Pipeline
    # HTML Filter that converts image's url into <img> tag.
    # For example, it will convert
    #   http://example.com/test.jpg
    # into
    #   <img src="http://example.com/test.jpg" alt=""/>.

    class ImageFilter < TextFilter
      def call
        @text.gsub(/(https|http)?:\/\/.+\.(jpg|jpeg|bmp|gif|png)(\?\S+)?/i) do |match|
          %(<img src="#{match}" alt=""/>)
        end
      end
    end
  end
end
