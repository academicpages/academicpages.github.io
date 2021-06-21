require 'test_helper'

class BreakTagTest < Minitest::Test
  include Liquid

  # tests that no weird errors are raised if break is called outside of a
  # block
  def test_break_with_no_block
    assigns = { 'i' => 1 }
    markup = '{% break %}'
    expected = ''

    assert_template_result(expected, markup, assigns)
  end
end
