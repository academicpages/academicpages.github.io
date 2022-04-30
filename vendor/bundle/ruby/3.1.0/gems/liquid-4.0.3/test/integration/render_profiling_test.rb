require 'test_helper'

class RenderProfilingTest < Minitest::Test
  include Liquid

  class ProfilingFileSystem
    def read_template_file(template_path)
      "Rendering template {% assign template_name = '#{template_path}'%}\n{{ template_name }}"
    end
  end

  def setup
    Liquid::Template.file_system = ProfilingFileSystem.new
  end

  def test_template_allows_flagging_profiling
    t = Template.parse("{{ 'a string' | upcase }}")
    t.render!

    assert_nil t.profiler
  end

  def test_parse_makes_available_simple_profiling
    t = Template.parse("{{ 'a string' | upcase }}", profile: true)
    t.render!

    assert_equal 1, t.profiler.length

    node = t.profiler[0]
    assert_equal " 'a string' | upcase ", node.code
  end

  def test_render_ignores_raw_strings_when_profiling
    t = Template.parse("This is raw string\nstuff\nNewline", profile: true)
    t.render!

    assert_equal 0, t.profiler.length
  end

  def test_profiling_includes_line_numbers_of_liquid_nodes
    t = Template.parse("{{ 'a string' | upcase }}\n{% increment test %}", profile: true)
    t.render!
    assert_equal 2, t.profiler.length

    # {{ 'a string' | upcase }}
    assert_equal 1, t.profiler[0].line_number
    # {{ increment test }}
    assert_equal 2, t.profiler[1].line_number
  end

  def test_profiling_includes_line_numbers_of_included_partials
    t = Template.parse("{% include 'a_template' %}", profile: true)
    t.render!

    included_children = t.profiler[0].children

    # {% assign template_name = 'a_template' %}
    assert_equal 1, included_children[0].line_number
    # {{ template_name }}
    assert_equal 2, included_children[1].line_number
  end

  def test_profiling_times_the_rendering_of_tokens
    t = Template.parse("{% include 'a_template' %}", profile: true)
    t.render!

    node = t.profiler[0]
    refute_nil node.render_time
  end

  def test_profiling_times_the_entire_render
    t = Template.parse("{% include 'a_template' %}", profile: true)
    t.render!

    assert t.profiler.total_render_time >= 0, "Total render time was not calculated"
  end

  def test_profiling_uses_include_to_mark_children
    t = Template.parse("{{ 'a string' | upcase }}\n{% include 'a_template' %}", profile: true)
    t.render!

    include_node = t.profiler[1]
    assert_equal 2, include_node.children.length
  end

  def test_profiling_marks_children_with_the_name_of_included_partial
    t = Template.parse("{{ 'a string' | upcase }}\n{% include 'a_template' %}", profile: true)
    t.render!

    include_node = t.profiler[1]
    include_node.children.each do |child|
      assert_equal "a_template", child.partial
    end
  end

  def test_profiling_supports_multiple_templates
    t = Template.parse("{{ 'a string' | upcase }}\n{% include 'a_template' %}\n{% include 'b_template' %}", profile: true)
    t.render!

    a_template = t.profiler[1]
    a_template.children.each do |child|
      assert_equal "a_template", child.partial
    end

    b_template = t.profiler[2]
    b_template.children.each do |child|
      assert_equal "b_template", child.partial
    end
  end

  def test_profiling_supports_rendering_the_same_partial_multiple_times
    t = Template.parse("{{ 'a string' | upcase }}\n{% include 'a_template' %}\n{% include 'a_template' %}", profile: true)
    t.render!

    a_template1 = t.profiler[1]
    a_template1.children.each do |child|
      assert_equal "a_template", child.partial
    end

    a_template2 = t.profiler[2]
    a_template2.children.each do |child|
      assert_equal "a_template", child.partial
    end
  end

  def test_can_iterate_over_each_profiling_entry
    t = Template.parse("{{ 'a string' | upcase }}\n{% increment test %}", profile: true)
    t.render!

    timing_count = 0
    t.profiler.each do |timing|
      timing_count += 1
    end

    assert_equal 2, timing_count
  end

  def test_profiling_marks_children_of_if_blocks
    t = Template.parse("{% if true %} {% increment test %} {{ test }} {% endif %}", profile: true)
    t.render!

    assert_equal 1, t.profiler.length
    assert_equal 2, t.profiler[0].children.length
  end

  def test_profiling_marks_children_of_for_blocks
    t = Template.parse("{% for item in collection %} {{ item }} {% endfor %}", profile: true)
    t.render!({ "collection" => ["one", "two"] })

    assert_equal 1, t.profiler.length
    # Will profile each invocation of the for block
    assert_equal 2, t.profiler[0].children.length
  end
end
