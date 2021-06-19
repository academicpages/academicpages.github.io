module Liquid
  # increment is used in a place where one needs to insert a counter
  #     into a template, and needs the counter to survive across
  #     multiple instantiations of the template.
  #     (To achieve the survival, the application must keep the context)
  #
  #     if the variable does not exist, it is created with value 0.
  #
  #   Hello: {% increment variable %}
  #
  # gives you:
  #
  #    Hello: 0
  #    Hello: 1
  #    Hello: 2
  #
  class Increment < Tag
    def initialize(tag_name, markup, options)
      super
      @variable = markup.strip
    end

    def render(context)
      value = context.environments.first[@variable] ||= 0
      context.environments.first[@variable] = value + 1
      value.to_s
    end
  end

  Template.register_tag('increment'.freeze, Increment)
end
