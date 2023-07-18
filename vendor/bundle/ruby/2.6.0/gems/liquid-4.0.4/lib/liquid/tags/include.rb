module Liquid
  # Include allows templates to relate with other templates
  #
  # Simply include another template:
  #
  #   {% include 'product' %}
  #
  # Include a template with a local variable:
  #
  #   {% include 'product' with products[0] %}
  #
  # Include a template for a collection:
  #
  #   {% include 'product' for products %}
  #
  class Include < Tag
    Syntax = /(#{QuotedFragment}+)(\s+(?:with|for)\s+(#{QuotedFragment}+))?/o

    attr_reader :template_name_expr, :variable_name_expr, :attributes

    def initialize(tag_name, markup, options)
      super

      if markup =~ Syntax

        template_name = $1
        variable_name = $3

        @variable_name_expr = variable_name ? Expression.parse(variable_name) : nil
        @template_name_expr = Expression.parse(template_name)
        @attributes = {}

        markup.scan(TagAttributes) do |key, value|
          @attributes[key] = Expression.parse(value)
        end

      else
        raise SyntaxError.new(options[:locale].t("errors.syntax.include".freeze))
      end
    end

    def parse(_tokens)
    end

    def render(context)
      template_name = context.evaluate(@template_name_expr)
      raise ArgumentError.new(options[:locale].t("errors.argument.include")) unless template_name

      partial = load_cached_partial(template_name, context)
      context_variable_name = template_name.split('/'.freeze).last

      variable = if @variable_name_expr
        context.evaluate(@variable_name_expr)
      else
        context.find_variable(template_name, raise_on_not_found: false)
      end

      old_template_name = context.template_name
      old_partial = context.partial
      begin
        context.template_name = template_name
        context.partial = true
        context.stack do
          @attributes.each do |key, value|
            context[key] = context.evaluate(value)
          end

          if variable.is_a?(Array)
            variable.collect do |var|
              context[context_variable_name] = var
              partial.render(context)
            end
          else
            context[context_variable_name] = variable
            partial.render(context)
          end
        end
      ensure
        context.template_name = old_template_name
        context.partial = old_partial
      end
    end

    private

    alias_method :parse_context, :options
    private :parse_context

    def load_cached_partial(template_name, context)
      cached_partials = context.registers[:cached_partials] || {}

      if cached = cached_partials[template_name]
        return cached
      end
      source = read_template_from_file_system(context)
      begin
        parse_context.partial = true
        partial = Liquid::Template.parse(source, parse_context)
      ensure
        parse_context.partial = false
      end
      cached_partials[template_name] = partial
      context.registers[:cached_partials] = cached_partials
      partial
    end

    def read_template_from_file_system(context)
      file_system = context.registers[:file_system] || Liquid::Template.file_system

      file_system.read_template_file(context.evaluate(@template_name_expr))
    end

    class ParseTreeVisitor < Liquid::ParseTreeVisitor
      def children
        [
          @node.template_name_expr,
          @node.variable_name_expr
        ] + @node.attributes.values
      end
    end
  end

  Template.register_tag('include'.freeze, Include)
end
