module Liquid
  class Comment < Block
    def render(_context)
      ''.freeze
    end

    def unknown_tag(_tag, _markup, _tokens)
    end

    def blank?
      true
    end
  end

  Template.register_tag('comment'.freeze, Comment)
end
