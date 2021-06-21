module Liquid
  # Continue tag to be used to break out of a for loop.
  #
  # == Basic Usage:
  #    {% for item in collection %}
  #      {% if item.condition %}
  #        {% continue %}
  #      {% endif %}
  #    {% endfor %}
  #
  class Continue < Tag
    def interrupt
      ContinueInterrupt.new
    end
  end

  Template.register_tag('continue'.freeze, Continue)
end
