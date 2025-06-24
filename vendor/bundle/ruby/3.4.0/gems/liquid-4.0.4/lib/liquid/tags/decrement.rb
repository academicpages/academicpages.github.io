module Liquid
  # decrement is used in a place where one needs to insert a counter
  #     into a template, and needs the counter to survive across
  #     multiple instantiations of the template.
  #     NOTE: decrement is a pre-decrement, --i,
  #           while increment is post:      i++.
  #
  #     (To achieve the survival, the application must keep the context)
  #
  #     if the variable does not exist, it is created with value 0.

  #   Hello: {% decrement variable %}
  #
  # gives you:
  #
  #    Hello: -1
  #    Hello: -2
  #    Hello: -3
  #
  class Decrement < Tag
    def initialize(tag_name, markup, options)
      super
      @variable = markup.strip
    end

    def render(context)
      value = context.environments.first[@variable] ||= 0
      value -= 1
      context.environments.first[@variable] = value
      value.to_s
    end
  end

  Template.register_tag('decrement'.freeze, Decrement)
end
