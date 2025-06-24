require 'test_helper'

class TokenizerTest < Minitest::Test
  def test_tokenize_strings
    assert_equal [' '], tokenize(' ')
    assert_equal ['hello world'], tokenize('hello world')
  end

  def test_tokenize_variables
    assert_equal ['{{funk}}'], tokenize('{{funk}}')
    assert_equal [' ', '{{funk}}', ' '], tokenize(' {{funk}} ')
    assert_equal [' ', '{{funk}}', ' ', '{{so}}', ' ', '{{brother}}', ' '], tokenize(' {{funk}} {{so}} {{brother}} ')
    assert_equal [' ', '{{  funk  }}', ' '], tokenize(' {{  funk  }} ')
  end

  def test_tokenize_blocks
    assert_equal ['{%comment%}'], tokenize('{%comment%}')
    assert_equal [' ', '{%comment%}', ' '], tokenize(' {%comment%} ')

    assert_equal [' ', '{%comment%}', ' ', '{%endcomment%}', ' '], tokenize(' {%comment%} {%endcomment%} ')
    assert_equal ['  ', '{% comment %}', ' ', '{% endcomment %}', ' '], tokenize("  {% comment %} {% endcomment %} ")
  end

  def test_calculate_line_numbers_per_token_with_profiling
    assert_equal [1],       tokenize_line_numbers("{{funk}}")
    assert_equal [1, 1, 1], tokenize_line_numbers(" {{funk}} ")
    assert_equal [1, 2, 2], tokenize_line_numbers("\n{{funk}}\n")
    assert_equal [1, 1, 3], tokenize_line_numbers(" {{\n funk \n}} ")
  end

  private

  def tokenize(source)
    tokenizer = Liquid::Tokenizer.new(source)
    tokens = []
    while t = tokenizer.shift
      tokens << t
    end
    tokens
  end

  def tokenize_line_numbers(source)
    tokenizer = Liquid::Tokenizer.new(source, true)
    line_numbers = []
    loop do
      line_number = tokenizer.line_number
      if tokenizer.shift
        line_numbers << line_number
      else
        break
      end
    end
    line_numbers
  end
end
