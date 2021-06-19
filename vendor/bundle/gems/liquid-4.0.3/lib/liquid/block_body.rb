module Liquid
  class BlockBody
    FullToken = /\A#{TagStart}#{WhitespaceControl}?\s*(\w+)\s*(.*?)#{WhitespaceControl}?#{TagEnd}\z/om
    ContentOfVariable = /\A#{VariableStart}#{WhitespaceControl}?(.*?)#{WhitespaceControl}?#{VariableEnd}\z/om
    WhitespaceOrNothing = /\A\s*\z/
    TAGSTART = "{%".freeze
    VARSTART = "{{".freeze

    attr_reader :nodelist

    def initialize
      @nodelist = []
      @blank = true
    end

    def parse(tokenizer, parse_context)
      parse_context.line_number = tokenizer.line_number
      while token = tokenizer.shift
        next if token.empty?
        case
        when token.start_with?(TAGSTART)
          whitespace_handler(token, parse_context)
          unless token =~ FullToken
            raise_missing_tag_terminator(token, parse_context)
          end
          tag_name = $1
          markup = $2
          # fetch the tag from registered blocks
          unless tag = registered_tags[tag_name]
            # end parsing if we reach an unknown tag and let the caller decide
            # determine how to proceed
            return yield tag_name, markup
          end
          new_tag = tag.parse(tag_name, markup, tokenizer, parse_context)
          @blank &&= new_tag.blank?
          @nodelist << new_tag
        when token.start_with?(VARSTART)
          whitespace_handler(token, parse_context)
          @nodelist << create_variable(token, parse_context)
          @blank = false
        else
          if parse_context.trim_whitespace
            token.lstrip!
          end
          parse_context.trim_whitespace = false
          @nodelist << token
          @blank &&= !!(token =~ WhitespaceOrNothing)
        end
        parse_context.line_number = tokenizer.line_number
      end

      yield nil, nil
    end

    def whitespace_handler(token, parse_context)
      if token[2] == WhitespaceControl
        previous_token = @nodelist.last
        if previous_token.is_a? String
          previous_token.rstrip!
        end
      end
      parse_context.trim_whitespace = (token[-3] == WhitespaceControl)
    end

    def blank?
      @blank
    end

    def render(context)
      output = []
      context.resource_limits.render_score += @nodelist.length

      idx = 0
      while node = @nodelist[idx]
        case node
        when String
          check_resources(context, node)
          output << node
        when Variable
          render_node_to_output(node, output, context)
        when Block
          render_node_to_output(node, output, context, node.blank?)
          break if context.interrupt? # might have happened in a for-block
        when Continue, Break
          # If we get an Interrupt that means the block must stop processing. An
          # Interrupt is any command that stops block execution such as {% break %}
          # or {% continue %}
          context.push_interrupt(node.interrupt)
          break
        else # Other non-Block tags
          render_node_to_output(node, output, context)
          break if context.interrupt? # might have happened through an include
        end
        idx += 1
      end

      output.join
    end

    private

    def render_node_to_output(node, output, context, skip_output = false)
      node_output = node.render(context)
      node_output = node_output.is_a?(Array) ? node_output.join : node_output.to_s
      check_resources(context, node_output)
      output << node_output unless skip_output
    rescue MemoryError => e
      raise e
    rescue UndefinedVariable, UndefinedDropMethod, UndefinedFilter => e
      context.handle_error(e, node.line_number)
      output << nil
    rescue ::StandardError => e
      line_number = node.is_a?(String) ? nil : node.line_number
      output << context.handle_error(e, line_number)
    end

    def check_resources(context, node_output)
      context.resource_limits.render_length += node_output.length
      return unless context.resource_limits.reached?
      raise MemoryError.new("Memory limits exceeded".freeze)
    end

    def create_variable(token, parse_context)
      token.scan(ContentOfVariable) do |content|
        markup = content.first
        return Variable.new(markup, parse_context)
      end
      raise_missing_variable_terminator(token, parse_context)
    end

    def raise_missing_tag_terminator(token, parse_context)
      raise SyntaxError.new(parse_context.locale.t("errors.syntax.tag_termination".freeze, token: token, tag_end: TagEnd.inspect))
    end

    def raise_missing_variable_terminator(token, parse_context)
      raise SyntaxError.new(parse_context.locale.t("errors.syntax.variable_termination".freeze, token: token, tag_end: VariableEnd.inspect))
    end

    def registered_tags
      Template.tags
    end
  end
end
