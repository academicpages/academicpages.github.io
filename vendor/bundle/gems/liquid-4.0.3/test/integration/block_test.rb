require 'test_helper'

class BlockTest < Minitest::Test
  include Liquid

  def test_unexpected_end_tag
    exc = assert_raises(SyntaxError) do
      Template.parse("{% if true %}{% endunless %}")
    end
    assert_equal exc.message, "Liquid syntax error: 'endunless' is not a valid delimiter for if tags. use endif"
  end
end
