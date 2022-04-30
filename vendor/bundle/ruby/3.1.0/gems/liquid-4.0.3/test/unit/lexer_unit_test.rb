require 'test_helper'

class LexerUnitTest < Minitest::Test
  include Liquid

  def test_strings
    tokens = Lexer.new(%( 'this is a test""' "wat 'lol'")).tokenize
    assert_equal [[:string, %('this is a test""')], [:string, %("wat 'lol'")], [:end_of_string]], tokens
  end

  def test_integer
    tokens = Lexer.new('hi 50').tokenize
    assert_equal [[:id, 'hi'], [:number, '50'], [:end_of_string]], tokens
  end

  def test_float
    tokens = Lexer.new('hi 5.0').tokenize
    assert_equal [[:id, 'hi'], [:number, '5.0'], [:end_of_string]], tokens
  end

  def test_comparison
    tokens = Lexer.new('== <> contains ').tokenize
    assert_equal [[:comparison, '=='], [:comparison, '<>'], [:comparison, 'contains'], [:end_of_string]], tokens
  end

  def test_specials
    tokens = Lexer.new('| .:').tokenize
    assert_equal [[:pipe, '|'], [:dot, '.'], [:colon, ':'], [:end_of_string]], tokens
    tokens = Lexer.new('[,]').tokenize
    assert_equal [[:open_square, '['], [:comma, ','], [:close_square, ']'], [:end_of_string]], tokens
  end

  def test_fancy_identifiers
    tokens = Lexer.new('hi five?').tokenize
    assert_equal [[:id, 'hi'], [:id, 'five?'], [:end_of_string]], tokens

    tokens = Lexer.new('2foo').tokenize
    assert_equal [[:number, '2'], [:id, 'foo'], [:end_of_string]], tokens
  end

  def test_whitespace
    tokens = Lexer.new("five|\n\t ==").tokenize
    assert_equal [[:id, 'five'], [:pipe, '|'], [:comparison, '=='], [:end_of_string]], tokens
  end

  def test_unexpected_character
    assert_raises(SyntaxError) do
      Lexer.new("%").tokenize
    end
  end
end
