require 'test_helper'

class TrimModeTest < Minitest::Test
  include Liquid

  # Make sure the trim isn't applied to standard output
  def test_standard_output
    text = <<-END_TEMPLATE
      <div>
        <p>
          {{ 'John' }}
        </p>
      </div>
    END_TEMPLATE
    expected = <<-END_EXPECTED
      <div>
        <p>
          John
        </p>
      </div>
    END_EXPECTED
    assert_template_result(expected, text)
  end

  def test_variable_output_with_multiple_blank_lines
    text = <<-END_TEMPLATE
      <div>
        <p>


          {{- 'John' -}}


        </p>
      </div>
    END_TEMPLATE
    expected = <<-END_EXPECTED
      <div>
        <p>John</p>
      </div>
    END_EXPECTED
    assert_template_result(expected, text)
  end

  def test_tag_output_with_multiple_blank_lines
    text = <<-END_TEMPLATE
      <div>
        <p>


          {%- if true -%}
          yes
          {%- endif -%}


        </p>
      </div>
    END_TEMPLATE
    expected = <<-END_EXPECTED
      <div>
        <p>yes</p>
      </div>
    END_EXPECTED
    assert_template_result(expected, text)
  end

  # Make sure the trim isn't applied to standard tags
  def test_standard_tags
    whitespace = '          '
    text = <<-END_TEMPLATE
      <div>
        <p>
          {% if true %}
          yes
          {% endif %}
        </p>
      </div>
    END_TEMPLATE
    expected = <<-END_EXPECTED
      <div>
        <p>
#{whitespace}
          yes
#{whitespace}
        </p>
      </div>
    END_EXPECTED
    assert_template_result(expected, text)

    text = <<-END_TEMPLATE
      <div>
        <p>
          {% if false %}
          no
          {% endif %}
        </p>
      </div>
    END_TEMPLATE
    expected = <<-END_EXPECTED
      <div>
        <p>
#{whitespace}
        </p>
      </div>
    END_EXPECTED
    assert_template_result(expected, text)
  end

  # Make sure the trim isn't too agressive
  def test_no_trim_output
    text = '<p>{{- \'John\' -}}</p>'
    expected = '<p>John</p>'
    assert_template_result(expected, text)
  end

  # Make sure the trim isn't too agressive
  def test_no_trim_tags
    text = '<p>{%- if true -%}yes{%- endif -%}</p>'
    expected = '<p>yes</p>'
    assert_template_result(expected, text)

    text = '<p>{%- if false -%}no{%- endif -%}</p>'
    expected = '<p></p>'
    assert_template_result(expected, text)
  end

  def test_single_line_outer_tag
    text = '<p> {%- if true %} yes {% endif -%} </p>'
    expected = '<p> yes </p>'
    assert_template_result(expected, text)

    text = '<p> {%- if false %} no {% endif -%} </p>'
    expected = '<p></p>'
    assert_template_result(expected, text)
  end

  def test_single_line_inner_tag
    text = '<p> {% if true -%} yes {%- endif %} </p>'
    expected = '<p> yes </p>'
    assert_template_result(expected, text)

    text = '<p> {% if false -%} no {%- endif %} </p>'
    expected = '<p>  </p>'
    assert_template_result(expected, text)
  end

  def test_single_line_post_tag
    text = '<p> {% if true -%} yes {% endif -%} </p>'
    expected = '<p> yes </p>'
    assert_template_result(expected, text)

    text = '<p> {% if false -%} no {% endif -%} </p>'
    expected = '<p> </p>'
    assert_template_result(expected, text)
  end

  def test_single_line_pre_tag
    text = '<p> {%- if true %} yes {%- endif %} </p>'
    expected = '<p> yes </p>'
    assert_template_result(expected, text)

    text = '<p> {%- if false %} no {%- endif %} </p>'
    expected = '<p> </p>'
    assert_template_result(expected, text)
  end

  def test_pre_trim_output
    text = <<-END_TEMPLATE
      <div>
        <p>
          {{- 'John' }}
        </p>
      </div>
    END_TEMPLATE
    expected = <<-END_EXPECTED
      <div>
        <p>John
        </p>
      </div>
    END_EXPECTED
    assert_template_result(expected, text)
  end

  def test_pre_trim_tags
    text = <<-END_TEMPLATE
      <div>
        <p>
          {%- if true %}
          yes
          {%- endif %}
        </p>
      </div>
    END_TEMPLATE
    expected = <<-END_EXPECTED
      <div>
        <p>
          yes
        </p>
      </div>
    END_EXPECTED
    assert_template_result(expected, text)

    text = <<-END_TEMPLATE
      <div>
        <p>
          {%- if false %}
          no
          {%- endif %}
        </p>
      </div>
    END_TEMPLATE
    expected = <<-END_EXPECTED
      <div>
        <p>
        </p>
      </div>
    END_EXPECTED
    assert_template_result(expected, text)
  end

  def test_post_trim_output
    text = <<-END_TEMPLATE
      <div>
        <p>
          {{ 'John' -}}
        </p>
      </div>
    END_TEMPLATE
    expected = <<-END_EXPECTED
      <div>
        <p>
          John</p>
      </div>
    END_EXPECTED
    assert_template_result(expected, text)
  end

  def test_post_trim_tags
    text = <<-END_TEMPLATE
      <div>
        <p>
          {% if true -%}
          yes
          {% endif -%}
        </p>
      </div>
    END_TEMPLATE
    expected = <<-END_EXPECTED
      <div>
        <p>
          yes
          </p>
      </div>
    END_EXPECTED
    assert_template_result(expected, text)

    text = <<-END_TEMPLATE
      <div>
        <p>
          {% if false -%}
          no
          {% endif -%}
        </p>
      </div>
    END_TEMPLATE
    expected = <<-END_EXPECTED
      <div>
        <p>
          </p>
      </div>
    END_EXPECTED
    assert_template_result(expected, text)
  end

  def test_pre_and_post_trim_tags
    text = <<-END_TEMPLATE
      <div>
        <p>
          {%- if true %}
          yes
          {% endif -%}
        </p>
      </div>
    END_TEMPLATE
    expected = <<-END_EXPECTED
      <div>
        <p>
          yes
          </p>
      </div>
    END_EXPECTED
    assert_template_result(expected, text)

    text = <<-END_TEMPLATE
      <div>
        <p>
          {%- if false %}
          no
          {% endif -%}
        </p>
      </div>
    END_TEMPLATE
    expected = <<-END_EXPECTED
      <div>
        <p></p>
      </div>
    END_EXPECTED
    assert_template_result(expected, text)
  end

  def test_post_and_pre_trim_tags
    text = <<-END_TEMPLATE
      <div>
        <p>
          {% if true -%}
          yes
          {%- endif %}
        </p>
      </div>
    END_TEMPLATE
    expected = <<-END_EXPECTED
      <div>
        <p>
          yes
        </p>
      </div>
    END_EXPECTED
    assert_template_result(expected, text)

    whitespace = '          '
    text = <<-END_TEMPLATE
      <div>
        <p>
          {% if false -%}
          no
          {%- endif %}
        </p>
      </div>
    END_TEMPLATE
    expected = <<-END_EXPECTED
      <div>
        <p>
#{whitespace}
        </p>
      </div>
    END_EXPECTED
    assert_template_result(expected, text)
  end

  def test_trim_output
    text = <<-END_TEMPLATE
      <div>
        <p>
          {{- 'John' -}}
        </p>
      </div>
    END_TEMPLATE
    expected = <<-END_EXPECTED
      <div>
        <p>John</p>
      </div>
    END_EXPECTED
    assert_template_result(expected, text)
  end

  def test_trim_tags
    text = <<-END_TEMPLATE
      <div>
        <p>
          {%- if true -%}
          yes
          {%- endif -%}
        </p>
      </div>
    END_TEMPLATE
    expected = <<-END_EXPECTED
      <div>
        <p>yes</p>
      </div>
    END_EXPECTED
    assert_template_result(expected, text)

    text = <<-END_TEMPLATE
      <div>
        <p>
          {%- if false -%}
          no
          {%- endif -%}
        </p>
      </div>
    END_TEMPLATE
    expected = <<-END_EXPECTED
      <div>
        <p></p>
      </div>
    END_EXPECTED
    assert_template_result(expected, text)
  end

  def test_whitespace_trim_output
    text = <<-END_TEMPLATE
      <div>
        <p>
          {{- 'John' -}},
          {{- '30' -}}
        </p>
      </div>
    END_TEMPLATE
    expected = <<-END_EXPECTED
      <div>
        <p>John,30</p>
      </div>
    END_EXPECTED
    assert_template_result(expected, text)
  end

  def test_whitespace_trim_tags
    text = <<-END_TEMPLATE
      <div>
        <p>
          {%- if true -%}
          yes
          {%- endif -%}
        </p>
      </div>
    END_TEMPLATE
    expected = <<-END_EXPECTED
      <div>
        <p>yes</p>
      </div>
    END_EXPECTED
    assert_template_result(expected, text)

    text = <<-END_TEMPLATE
      <div>
        <p>
          {%- if false -%}
          no
          {%- endif -%}
        </p>
      </div>
    END_TEMPLATE
    expected = <<-END_EXPECTED
      <div>
        <p></p>
      </div>
    END_EXPECTED
    assert_template_result(expected, text)
  end

  def test_complex_trim_output
    text = <<-END_TEMPLATE
      <div>
        <p>
          {{- 'John' -}}
          {{- '30' -}}
        </p>
        <b>
          {{ 'John' -}}
          {{- '30' }}
        </b>
        <i>
          {{- 'John' }}
          {{ '30' -}}
        </i>
      </div>
    END_TEMPLATE
    expected = <<-END_EXPECTED
      <div>
        <p>John30</p>
        <b>
          John30
        </b>
        <i>John
          30</i>
      </div>
    END_EXPECTED
    assert_template_result(expected, text)
  end

  def test_complex_trim
    text = <<-END_TEMPLATE
      <div>
        {%- if true -%}
          {%- if true -%}
            <p>
              {{- 'John' -}}
            </p>
          {%- endif -%}
        {%- endif -%}
      </div>
    END_TEMPLATE
    expected = <<-END_EXPECTED
      <div><p>John</p></div>
    END_EXPECTED
    assert_template_result(expected, text)
  end

  def test_right_trim_followed_by_tag
    assert_template_result('ab c', '{{ "a" -}}{{ "b" }} c')
  end

  def test_raw_output
    whitespace = '        '
    text = <<-END_TEMPLATE
      <div>
        {% raw %}
          {%- if true -%}
            <p>
              {{- 'John' -}}
            </p>
          {%- endif -%}
        {% endraw %}
      </div>
    END_TEMPLATE
    expected = <<-END_EXPECTED
      <div>
#{whitespace}
          {%- if true -%}
            <p>
              {{- 'John' -}}
            </p>
          {%- endif -%}
#{whitespace}
      </div>
    END_EXPECTED
    assert_template_result(expected, text)
  end
end # TrimModeTest
