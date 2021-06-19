require 'test_helper'

class VariableTest < Minitest::Test
  include Liquid

  def test_simple_variable
    template = Template.parse(%({{test}}))
    assert_equal 'worked', template.render!('test' => 'worked')
    assert_equal 'worked wonderfully', template.render!('test' => 'worked wonderfully')
  end

  def test_variable_render_calls_to_liquid
    assert_template_result 'foobar', '{{ foo }}', 'foo' => ThingWithToLiquid.new
  end

  def test_simple_with_whitespaces
    template = Template.parse(%(  {{ test }}  ))
    assert_equal '  worked  ', template.render!('test' => 'worked')
    assert_equal '  worked wonderfully  ', template.render!('test' => 'worked wonderfully')
  end

  def test_ignore_unknown
    template = Template.parse(%({{ test }}))
    assert_equal '', template.render!
  end

  def test_using_blank_as_variable_name
    template = Template.parse("{% assign foo = blank %}{{ foo }}")
    assert_equal '', template.render!
  end

  def test_using_empty_as_variable_name
    template = Template.parse("{% assign foo = empty %}{{ foo }}")
    assert_equal '', template.render!
  end

  def test_hash_scoping
    template = Template.parse(%({{ test.test }}))
    assert_equal 'worked', template.render!('test' => { 'test' => 'worked' })
  end

  def test_false_renders_as_false
    assert_equal 'false', Template.parse("{{ foo }}").render!('foo' => false)
    assert_equal 'false', Template.parse("{{ false }}").render!
  end

  def test_nil_renders_as_empty_string
    assert_equal '', Template.parse("{{ nil }}").render!
    assert_equal 'cat', Template.parse("{{ nil | append: 'cat' }}").render!
  end

  def test_preset_assigns
    template = Template.parse(%({{ test }}))
    template.assigns['test'] = 'worked'
    assert_equal 'worked', template.render!
  end

  def test_reuse_parsed_template
    template = Template.parse(%({{ greeting }} {{ name }}))
    template.assigns['greeting'] = 'Goodbye'
    assert_equal 'Hello Tobi', template.render!('greeting' => 'Hello', 'name' => 'Tobi')
    assert_equal 'Hello ', template.render!('greeting' => 'Hello', 'unknown' => 'Tobi')
    assert_equal 'Hello Brian', template.render!('greeting' => 'Hello', 'name' => 'Brian')
    assert_equal 'Goodbye Brian', template.render!('name' => 'Brian')
    assert_equal({ 'greeting' => 'Goodbye' }, template.assigns)
  end

  def test_assigns_not_polluted_from_template
    template = Template.parse(%({{ test }}{% assign test = 'bar' %}{{ test }}))
    template.assigns['test'] = 'baz'
    assert_equal 'bazbar', template.render!
    assert_equal 'bazbar', template.render!
    assert_equal 'foobar', template.render!('test' => 'foo')
    assert_equal 'bazbar', template.render!
  end

  def test_hash_with_default_proc
    template = Template.parse(%(Hello {{ test }}))
    assigns = Hash.new { |h, k| raise "Unknown variable '#{k}'" }
    assigns['test'] = 'Tobi'
    assert_equal 'Hello Tobi', template.render!(assigns)
    assigns.delete('test')
    e = assert_raises(RuntimeError) do
      template.render!(assigns)
    end
    assert_equal "Unknown variable 'test'", e.message
  end

  def test_multiline_variable
    assert_equal 'worked', Template.parse("{{\ntest\n}}").render!('test' => 'worked')
  end

  def test_render_symbol
    assert_template_result 'bar', '{{ foo }}', 'foo' => :bar
  end
end
