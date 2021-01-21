require 'test_helper'

class IncrementTagTest < Minitest::Test
  include Liquid

  def test_inc
    assert_template_result('0', '{%increment port %}', {})
    assert_template_result('0 1', '{%increment port %} {%increment port%}', {})
    assert_template_result('0 0 1 2 1',
      '{%increment port %} {%increment starboard%} ' \
      '{%increment port %} {%increment port%} ' \
      '{%increment starboard %}', {})
  end

  def test_dec
    assert_template_result('9', '{%decrement port %}', { 'port' => 10 })
    assert_template_result('-1 -2', '{%decrement port %} {%decrement port%}', {})
    assert_template_result('1 5 2 2 5',
      '{%increment port %} {%increment starboard%} ' \
      '{%increment port %} {%decrement port%} ' \
      '{%decrement starboard %}', { 'port' => 1, 'starboard' => 5 })
  end
end
