module Liquid
  # Capture stores the result of a block into a variable without rendering it inplace.
  #
  #   {% capture heading %}
  #     Monkeys!
  #   {% endcapture %}
  #   ...
  #   <h1>{{ heading }}</h1>
  #
  # Capture is useful for saving content for use later in your template, such as
  # in a sidebar or footer.
  #
  class Capture < Block
    Syntax = /(#{VariableSignature}+)/o

    def initialize(tag_name, markup, options)
      super
      if markup =~ Syntax
        @to = $1
      else
        raise SyntaxError.new(options[:locale].t("errors.syntax.capture"))
      end
    end

    def render(context)
      output = super
      context.scopes.last[@to] = output
      context.resource_limits.assign_score += output.length
      ''.freeze
    end

    def blank?
      true
    end
  end

  Template.register_tag('capture'.freeze, Capture)
end
