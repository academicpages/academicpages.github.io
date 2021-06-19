require 'test_helper'

module MoneyFilter
  def money(input)
    sprintf(' %d$ ', input)
  end

  def money_with_underscore(input)
    sprintf(' %d$ ', input)
  end
end

module CanadianMoneyFilter
  def money(input)
    sprintf(' %d$ CAD ', input)
  end
end

module SubstituteFilter
  def substitute(input, params = {})
    input.gsub(/%\{(\w+)\}/) { |match| params[$1] }
  end
end

class FiltersTest < Minitest::Test
  include Liquid

  module OverrideObjectMethodFilter
    def tap(input)
      "tap overridden"
    end
  end

  def setup
    @context = Context.new
  end

  def test_local_filter
    @context['var'] = 1000
    @context.add_filters(MoneyFilter)

    assert_equal ' 1000$ ', Template.parse("{{var | money}}").render(@context)
  end

  def test_underscore_in_filter_name
    @context['var'] = 1000
    @context.add_filters(MoneyFilter)
    assert_equal ' 1000$ ', Template.parse("{{var | money_with_underscore}}").render(@context)
  end

  def test_second_filter_overwrites_first
    @context['var'] = 1000
    @context.add_filters(MoneyFilter)
    @context.add_filters(CanadianMoneyFilter)

    assert_equal ' 1000$ CAD ', Template.parse("{{var | money}}").render(@context)
  end

  def test_size
    @context['var'] = 'abcd'
    @context.add_filters(MoneyFilter)

    assert_equal '4', Template.parse("{{var | size}}").render(@context)
  end

  def test_join
    @context['var'] = [1, 2, 3, 4]

    assert_equal "1 2 3 4", Template.parse("{{var | join}}").render(@context)
  end

  def test_sort
    @context['value'] = 3
    @context['numbers'] = [2, 1, 4, 3]
    @context['words'] = ['expected', 'as', 'alphabetic']
    @context['arrays'] = ['flower', 'are']
    @context['case_sensitive'] = ['sensitive', 'Expected', 'case']

    assert_equal '1 2 3 4', Template.parse("{{numbers | sort | join}}").render(@context)
    assert_equal 'alphabetic as expected', Template.parse("{{words | sort | join}}").render(@context)
    assert_equal '3', Template.parse("{{value | sort}}").render(@context)
    assert_equal 'are flower', Template.parse("{{arrays | sort | join}}").render(@context)
    assert_equal 'Expected case sensitive', Template.parse("{{case_sensitive | sort | join}}").render(@context)
  end

  def test_sort_natural
    @context['words'] = ['case', 'Assert', 'Insensitive']
    @context['hashes'] = [{ 'a' => 'A' }, { 'a' => 'b' }, { 'a' => 'C' }]
    @context['objects'] = [TestObject.new('A'), TestObject.new('b'), TestObject.new('C')]

    # Test strings
    assert_equal 'Assert case Insensitive', Template.parse("{{words | sort_natural | join}}").render(@context)

    # Test hashes
    assert_equal 'A b C', Template.parse("{{hashes | sort_natural: 'a' | map: 'a' | join}}").render(@context)

    # Test objects
    assert_equal 'A b C', Template.parse("{{objects | sort_natural: 'a' | map: 'a' | join}}").render(@context)
  end

  def test_compact
    @context['words'] = ['a', nil, 'b', nil, 'c']
    @context['hashes'] = [{ 'a' => 'A' }, { 'a' => nil }, { 'a' => 'C' }]
    @context['objects'] = [TestObject.new('A'), TestObject.new(nil), TestObject.new('C')]

    # Test strings
    assert_equal 'a b c', Template.parse("{{words | compact | join}}").render(@context)

    # Test hashes
    assert_equal 'A C', Template.parse("{{hashes | compact: 'a' | map: 'a' | join}}").render(@context)

    # Test objects
    assert_equal 'A C', Template.parse("{{objects | compact: 'a' | map: 'a' | join}}").render(@context)
  end

  def test_strip_html
    @context['var'] = "<b>bla blub</a>"

    assert_equal "bla blub", Template.parse("{{ var | strip_html }}").render(@context)
  end

  def test_strip_html_ignore_comments_with_html
    @context['var'] = "<!-- split and some <ul> tag --><b>bla blub</a>"

    assert_equal "bla blub", Template.parse("{{ var | strip_html }}").render(@context)
  end

  def test_capitalize
    @context['var'] = "blub"

    assert_equal "Blub", Template.parse("{{ var | capitalize }}").render(@context)
  end

  def test_nonexistent_filter_is_ignored
    @context['var'] = 1000

    assert_equal '1000', Template.parse("{{ var | xyzzy }}").render(@context)
  end

  def test_filter_with_keyword_arguments
    @context['surname'] = 'john'
    @context['input'] = 'hello %{first_name}, %{last_name}'
    @context.add_filters(SubstituteFilter)
    output = Template.parse(%({{ input | substitute: first_name: surname, last_name: 'doe' }})).render(@context)
    assert_equal 'hello john, doe', output
  end

  def test_override_object_method_in_filter
    assert_equal "tap overridden", Template.parse("{{var | tap}}").render!({ 'var' => 1000 }, filters: [OverrideObjectMethodFilter])

    # tap still treated as a non-existent filter
    assert_equal "1000", Template.parse("{{var | tap}}").render!({ 'var' => 1000 })
  end
end

class FiltersInTemplate < Minitest::Test
  include Liquid

  def test_local_global
    with_global_filter(MoneyFilter) do
      assert_equal " 1000$ ", Template.parse("{{1000 | money}}").render!(nil, nil)
      assert_equal " 1000$ CAD ", Template.parse("{{1000 | money}}").render!(nil, filters: CanadianMoneyFilter)
      assert_equal " 1000$ CAD ", Template.parse("{{1000 | money}}").render!(nil, filters: [CanadianMoneyFilter])
    end
  end

  def test_local_filter_with_deprecated_syntax
    assert_equal " 1000$ CAD ", Template.parse("{{1000 | money}}").render!(nil, CanadianMoneyFilter)
    assert_equal " 1000$ CAD ", Template.parse("{{1000 | money}}").render!(nil, [CanadianMoneyFilter])
  end
end # FiltersTest

class TestObject < Liquid::Drop
  attr_accessor :a
  def initialize(a)
    @a = a
  end
end
