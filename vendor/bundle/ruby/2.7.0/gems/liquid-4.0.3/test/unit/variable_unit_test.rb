require 'test_helper'

class VariableUnitTest < Minitest::Test
  include Liquid

  def test_variable
    var = create_variable('hello')
    assert_equal VariableLookup.new('hello'), var.name
  end

  def test_filters
    var = create_variable('hello | textileze')
    assert_equal VariableLookup.new('hello'), var.name
    assert_equal [['textileze', []]], var.filters

    var = create_variable('hello | textileze | paragraph')
    assert_equal VariableLookup.new('hello'), var.name
    assert_equal [['textileze', []], ['paragraph', []]], var.filters

    var = create_variable(%( hello | strftime: '%Y'))
    assert_equal VariableLookup.new('hello'), var.name
    assert_equal [['strftime', ['%Y']]], var.filters

    var = create_variable(%( 'typo' | link_to: 'Typo', true ))
    assert_equal 'typo', var.name
    assert_equal [['link_to', ['Typo', true]]], var.filters

    var = create_variable(%( 'typo' | link_to: 'Typo', false ))
    assert_equal 'typo', var.name
    assert_equal [['link_to', ['Typo', false]]], var.filters

    var = create_variable(%( 'foo' | repeat: 3 ))
    assert_equal 'foo', var.name
    assert_equal [['repeat', [3]]], var.filters

    var = create_variable(%( 'foo' | repeat: 3, 3 ))
    assert_equal 'foo', var.name
    assert_equal [['repeat', [3, 3]]], var.filters

    var = create_variable(%( 'foo' | repeat: 3, 3, 3 ))
    assert_equal 'foo', var.name
    assert_equal [['repeat', [3, 3, 3]]], var.filters

    var = create_variable(%( hello | strftime: '%Y, okay?'))
    assert_equal VariableLookup.new('hello'), var.name
    assert_equal [['strftime', ['%Y, okay?']]], var.filters

    var = create_variable(%( hello | things: "%Y, okay?", 'the other one'))
    assert_equal VariableLookup.new('hello'), var.name
    assert_equal [['things', ['%Y, okay?', 'the other one']]], var.filters
  end

  def test_filter_with_date_parameter
    var = create_variable(%( '2006-06-06' | date: "%m/%d/%Y"))
    assert_equal '2006-06-06', var.name
    assert_equal [['date', ['%m/%d/%Y']]], var.filters
  end

  def test_filters_without_whitespace
    var = create_variable('hello | textileze | paragraph')
    assert_equal VariableLookup.new('hello'), var.name
    assert_equal [['textileze', []], ['paragraph', []]], var.filters

    var = create_variable('hello|textileze|paragraph')
    assert_equal VariableLookup.new('hello'), var.name
    assert_equal [['textileze', []], ['paragraph', []]], var.filters

    var = create_variable("hello|replace:'foo','bar'|textileze")
    assert_equal VariableLookup.new('hello'), var.name
    assert_equal [['replace', ['foo', 'bar']], ['textileze', []]], var.filters
  end

  def test_symbol
    var = create_variable("http://disney.com/logo.gif | image: 'med' ", error_mode: :lax)
    assert_equal VariableLookup.new('http://disney.com/logo.gif'), var.name
    assert_equal [['image', ['med']]], var.filters
  end

  def test_string_to_filter
    var = create_variable("'http://disney.com/logo.gif' | image: 'med' ")
    assert_equal 'http://disney.com/logo.gif', var.name
    assert_equal [['image', ['med']]], var.filters
  end

  def test_string_single_quoted
    var = create_variable(%( "hello" ))
    assert_equal 'hello', var.name
  end

  def test_string_double_quoted
    var = create_variable(%( 'hello' ))
    assert_equal 'hello', var.name
  end

  def test_integer
    var = create_variable(%( 1000 ))
    assert_equal 1000, var.name
  end

  def test_float
    var = create_variable(%( 1000.01 ))
    assert_equal 1000.01, var.name
  end

  def test_dashes
    assert_equal VariableLookup.new('foo-bar'), create_variable('foo-bar').name
    assert_equal VariableLookup.new('foo-bar-2'), create_variable('foo-bar-2').name

    with_error_mode :strict do
      assert_raises(Liquid::SyntaxError) { create_variable('foo - bar') }
      assert_raises(Liquid::SyntaxError) { create_variable('-foo') }
      assert_raises(Liquid::SyntaxError) { create_variable('2foo') }
    end
  end

  def test_string_with_special_chars
    var = create_variable(%( 'hello! $!@.;"ddasd" ' ))
    assert_equal 'hello! $!@.;"ddasd" ', var.name
  end

  def test_string_dot
    var = create_variable(%( test.test ))
    assert_equal VariableLookup.new('test.test'), var.name
  end

  def test_filter_with_keyword_arguments
    var = create_variable(%( hello | things: greeting: "world", farewell: 'goodbye'))
    assert_equal VariableLookup.new('hello'), var.name
    assert_equal [['things', [], { 'greeting' => 'world', 'farewell' => 'goodbye' }]], var.filters
  end

  def test_lax_filter_argument_parsing
    var = create_variable(%( number_of_comments | pluralize: 'comment': 'comments' ), error_mode: :lax)
    assert_equal VariableLookup.new('number_of_comments'), var.name
    assert_equal [['pluralize', ['comment', 'comments']]], var.filters
  end

  def test_strict_filter_argument_parsing
    with_error_mode(:strict) do
      assert_raises(SyntaxError) do
        create_variable(%( number_of_comments | pluralize: 'comment': 'comments' ))
      end
    end
  end

  def test_output_raw_source_of_variable
    var = create_variable(%( name_of_variable | upcase ))
    assert_equal " name_of_variable | upcase ", var.raw
  end

  def test_variable_lookup_interface
    lookup = VariableLookup.new('a.b.c')
    assert_equal 'a', lookup.name
    assert_equal ['b', 'c'], lookup.lookups
  end

  private

  def create_variable(markup, options = {})
    Variable.new(markup, ParseContext.new(options))
  end
end
