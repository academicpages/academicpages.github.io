require 'test_helper'

class ContinueTagTest < Minitest::Test
  include Liquid

  # tests that no weird errors are raised if continue is called outside of a
  # block
  def test_continue_with_no_block
    assigns = {}
    markup = '{% continue %}'
    expected = ''

    assert_template_result(expected, markup, assigns)
  end
end
