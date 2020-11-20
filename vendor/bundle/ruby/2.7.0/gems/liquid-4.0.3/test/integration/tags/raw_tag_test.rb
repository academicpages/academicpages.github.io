require 'test_helper'

class RawTagTest < Minitest::Test
  include Liquid

  def test_tag_in_raw
    assert_template_result '{% comment %} test {% endcomment %}',
      '{% raw %}{% comment %} test {% endcomment %}{% endraw %}'
  end

  def test_output_in_raw
    assert_template_result '{{ test }}', '{% raw %}{{ test }}{% endraw %}'
  end

  def test_open_tag_in_raw
    assert_template_result ' Foobar {% invalid ', '{% raw %} Foobar {% invalid {% endraw %}'
    assert_template_result ' Foobar invalid %} ', '{% raw %} Foobar invalid %} {% endraw %}'
    assert_template_result ' Foobar {{ invalid ', '{% raw %} Foobar {{ invalid {% endraw %}'
    assert_template_result ' Foobar invalid }} ', '{% raw %} Foobar invalid }} {% endraw %}'
    assert_template_result ' Foobar {% invalid {% {% endraw ', '{% raw %} Foobar {% invalid {% {% endraw {% endraw %}'
    assert_template_result ' Foobar {% {% {% ', '{% raw %} Foobar {% {% {% {% endraw %}'
    assert_template_result ' test {% raw %} {% endraw %}', '{% raw %} test {% raw %} {% {% endraw %}endraw %}'
    assert_template_result ' Foobar {{ invalid 1', '{% raw %} Foobar {{ invalid {% endraw %}{{ 1 }}'
  end

  def test_invalid_raw
    assert_match_syntax_error(/tag was never closed/, '{% raw %} foo')
    assert_match_syntax_error(/Valid syntax/, '{% raw } foo {% endraw %}')
    assert_match_syntax_error(/Valid syntax/, '{% raw } foo %}{% endraw %}')
  end
end
