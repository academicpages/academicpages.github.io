module Liquid
  class Block < Tag
    MAX_DEPTH = 100

    def initialize(tag_name, markup, options)
      super
      @blank = true
    end

    def parse(tokens)
      @body = BlockBody.new
      while parse_body(@body, tokens)
      end
    end

    def render(context)
      @body.render(context)
    end

    def blank?
      @blank
    end

    def nodelist
      @body.nodelist
    end

    def unknown_tag(tag, _params, _tokens)
      if tag == 'else'.freeze
        raise SyntaxError.new(parse_context.locale.t("errors.syntax.unexpected_else".freeze,
          block_name: block_name))
      elsif tag.start_with?('end'.freeze)
        raise SyntaxError.new(parse_context.locale.t("errors.syntax.invalid_delimiter".freeze,
          tag: tag,
          block_name: block_name,
          block_delimiter: block_delimiter))
      else
        raise SyntaxError.new(parse_context.locale.t("errors.syntax.unknown_tag".freeze, tag: tag))
      end
    end

    def block_name
      @tag_name
    end

    def block_delimiter
      @block_delimiter ||= "end#{block_name}"
    end

    protected

    def parse_body(body, tokens)
      if parse_context.depth >= MAX_DEPTH
        raise StackLevelError, "Nesting too deep".freeze
      end
      parse_context.depth += 1
      begin
        body.parse(tokens, parse_context) do |end_tag_name, end_tag_params|
          @blank &&= body.blank?

          return false if end_tag_name == block_delimiter
          unless end_tag_name
            raise SyntaxError.new(parse_context.locale.t("errors.syntax.tag_never_closed".freeze, block_name: block_name))
          end

          # this tag is not registered with the system
          # pass it to the current block for special handling or error reporting
          unknown_tag(end_tag_name, end_tag_params, tokens)
        end
      ensure
        parse_context.depth -= 1
      end

      true
    end
  end
end
