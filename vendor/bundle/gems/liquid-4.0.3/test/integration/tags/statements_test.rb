require 'test_helper'

class StatementsTest < Minitest::Test
  include Liquid

  def test_true_eql_true
    text = ' {% if true == true %} true {% else %} false {% endif %} '
    assert_template_result '  true  ', text
  end

  def test_true_not_eql_true
    text = ' {% if true != true %} true {% else %} false {% endif %} '
    assert_template_result '  false  ', text
  end

  def test_true_lq_true
    text = ' {% if 0 > 0 %} true {% else %} false {% endif %} '
    assert_template_result '  false  ', text
  end

  def test_one_lq_zero
    text = ' {% if 1 > 0 %} true {% else %} false {% endif %} '
    assert_template_result '  true  ', text
  end

  def test_zero_lq_one
    text = ' {% if 0 < 1 %} true {% else %} false {% endif %} '
    assert_template_result '  true  ', text
  end

  def test_zero_lq_or_equal_one
    text = ' {% if 0 <= 0 %} true {% else %} false {% endif %} '
    assert_template_result '  true  ', text
  end

  def test_zero_lq_or_equal_one_involving_nil
    text = ' {% if null <= 0 %} true {% else %} false {% endif %} '
    assert_template_result '  false  ', text

    text = ' {% if 0 <= null %} true {% else %} false {% endif %} '
    assert_template_result '  false  ', text
  end

  def test_zero_lqq_or_equal_one
    text = ' {% if 0 >= 0 %} true {% else %} false {% endif %} '
    assert_template_result '  true  ', text
  end

  def test_strings
    text = " {% if 'test' == 'test' %} true {% else %} false {% endif %} "
    assert_template_result '  true  ', text
  end

  def test_strings_not_equal
    text = " {% if 'test' != 'test' %} true {% else %} false {% endif %} "
    assert_template_result '  false  ', text
  end

  def test_var_strings_equal
    text = ' {% if var == "hello there!" %} true {% else %} false {% endif %} '
    assert_template_result '  true  ', text, 'var' => 'hello there!'
  end

  def test_var_strings_are_not_equal
    text = ' {% if "hello there!" == var %} true {% else %} false {% endif %} '
    assert_template_result '  true  ', text, 'var' => 'hello there!'
  end

  def test_var_and_long_string_are_equal
    text = " {% if var == 'hello there!' %} true {% else %} false {% endif %} "
    assert_template_result '  true  ', text, 'var' => 'hello there!'
  end

  def test_var_and_long_string_are_equal_backwards
    text = " {% if 'hello there!' == var %} true {% else %} false {% endif %} "
    assert_template_result '  true  ', text, 'var' => 'hello there!'
  end

  # def test_is_nil
  #  text = %| {% if var != nil %} true {% else %} false {% end %} |
  #  @template.assigns = { 'var' => 'hello there!'}
  #  expected = %|  true  |
  #  assert_equal expected, @template.parse(text)
  # end

  def test_is_collection_empty
    text = ' {% if array == empty %} true {% else %} false {% endif %} '
    assert_template_result '  true  ', text, 'array' => []
  end

  def test_is_not_collection_empty
    text = ' {% if array == empty %} true {% else %} false {% endif %} '
    assert_template_result '  false  ', text, 'array' => [1, 2, 3]
  end

  def test_nil
    text = ' {% if var == nil %} true {% else %} false {% endif %} '
    assert_template_result '  true  ', text, 'var' => nil

    text = ' {% if var == null %} true {% else %} false {% endif %} '
    assert_template_result '  true  ', text, 'var' => nil
  end

  def test_not_nil
    text = ' {% if var != nil %} true {% else %} false {% endif %} '
    assert_template_result '  true  ', text, 'var' => 1

    text = ' {% if var != null %} true {% else %} false {% endif %} '
    assert_template_result '  true  ', text, 'var' => 1
  end
end # StatementsTest
