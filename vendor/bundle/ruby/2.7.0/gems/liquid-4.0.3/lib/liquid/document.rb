module Liquid
  class Document < BlockBody
    def self.parse(tokens, parse_context)
      doc = new
      doc.parse(tokens, parse_context)
      doc
    end

    def parse(tokens, parse_context)
      super do |end_tag_name, end_tag_params|
        unknown_tag(end_tag_name, parse_context) if end_tag_name
      end
    rescue SyntaxError => e
      e.line_number ||= parse_context.line_number
      raise
    end

    def unknown_tag(tag, parse_context)
      case tag
      when 'else'.freeze, 'end'.freeze
        raise SyntaxError.new(parse_context.locale.t("errors.syntax.unexpected_outer_tag".freeze, tag: tag))
      else
        raise SyntaxError.new(parse_context.locale.t("errors.syntax.unknown_tag".freeze, tag: tag))
      end
    end
  end
end
