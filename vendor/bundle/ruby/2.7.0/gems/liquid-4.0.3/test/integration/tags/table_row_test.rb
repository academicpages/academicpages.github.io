require 'test_helper'

class TableRowTest < Minitest::Test
  include Liquid

  class ArrayDrop < Liquid::Drop
    include Enumerable

    def initialize(array)
      @array = array
    end

    def each(&block)
      @array.each(&block)
    end
  end

  def test_table_row
    assert_template_result("<tr class=\"row1\">\n<td class=\"col1\"> 1 </td><td class=\"col2\"> 2 </td><td class=\"col3\"> 3 </td></tr>\n<tr class=\"row2\"><td class=\"col1\"> 4 </td><td class=\"col2\"> 5 </td><td class=\"col3\"> 6 </td></tr>\n",
      '{% tablerow n in numbers cols:3%} {{n}} {% endtablerow %}',
      'numbers' => [1, 2, 3, 4, 5, 6])

    assert_template_result("<tr class=\"row1\">\n</tr>\n",
      '{% tablerow n in numbers cols:3%} {{n}} {% endtablerow %}',
      'numbers' => [])
  end

  def test_table_row_with_different_cols
    assert_template_result("<tr class=\"row1\">\n<td class=\"col1\"> 1 </td><td class=\"col2\"> 2 </td><td class=\"col3\"> 3 </td><td class=\"col4\"> 4 </td><td class=\"col5\"> 5 </td></tr>\n<tr class=\"row2\"><td class=\"col1\"> 6 </td></tr>\n",
      '{% tablerow n in numbers cols:5%} {{n}} {% endtablerow %}',
      'numbers' => [1, 2, 3, 4, 5, 6])
  end

  def test_table_col_counter
    assert_template_result("<tr class=\"row1\">\n<td class=\"col1\">1</td><td class=\"col2\">2</td></tr>\n<tr class=\"row2\"><td class=\"col1\">1</td><td class=\"col2\">2</td></tr>\n<tr class=\"row3\"><td class=\"col1\">1</td><td class=\"col2\">2</td></tr>\n",
      '{% tablerow n in numbers cols:2%}{{tablerowloop.col}}{% endtablerow %}',
      'numbers' => [1, 2, 3, 4, 5, 6])
  end

  def test_quoted_fragment
    assert_template_result("<tr class=\"row1\">\n<td class=\"col1\"> 1 </td><td class=\"col2\"> 2 </td><td class=\"col3\"> 3 </td></tr>\n<tr class=\"row2\"><td class=\"col1\"> 4 </td><td class=\"col2\"> 5 </td><td class=\"col3\"> 6 </td></tr>\n",
      "{% tablerow n in collections.frontpage cols:3%} {{n}} {% endtablerow %}",
      'collections' => { 'frontpage' => [1, 2, 3, 4, 5, 6] })
    assert_template_result("<tr class=\"row1\">\n<td class=\"col1\"> 1 </td><td class=\"col2\"> 2 </td><td class=\"col3\"> 3 </td></tr>\n<tr class=\"row2\"><td class=\"col1\"> 4 </td><td class=\"col2\"> 5 </td><td class=\"col3\"> 6 </td></tr>\n",
      "{% tablerow n in collections['frontpage'] cols:3%} {{n}} {% endtablerow %}",
      'collections' => { 'frontpage' => [1, 2, 3, 4, 5, 6] })
  end

  def test_enumerable_drop
    assert_template_result("<tr class=\"row1\">\n<td class=\"col1\"> 1 </td><td class=\"col2\"> 2 </td><td class=\"col3\"> 3 </td></tr>\n<tr class=\"row2\"><td class=\"col1\"> 4 </td><td class=\"col2\"> 5 </td><td class=\"col3\"> 6 </td></tr>\n",
      '{% tablerow n in numbers cols:3%} {{n}} {% endtablerow %}',
      'numbers' => ArrayDrop.new([1, 2, 3, 4, 5, 6]))
  end

  def test_offset_and_limit
    assert_template_result("<tr class=\"row1\">\n<td class=\"col1\"> 1 </td><td class=\"col2\"> 2 </td><td class=\"col3\"> 3 </td></tr>\n<tr class=\"row2\"><td class=\"col1\"> 4 </td><td class=\"col2\"> 5 </td><td class=\"col3\"> 6 </td></tr>\n",
      '{% tablerow n in numbers cols:3 offset:1 limit:6%} {{n}} {% endtablerow %}',
      'numbers' => [0, 1, 2, 3, 4, 5, 6, 7])
  end

  def test_blank_string_not_iterable
    assert_template_result("<tr class=\"row1\">\n</tr>\n", "{% tablerow char in characters cols:3 %}I WILL NOT BE OUTPUT{% endtablerow %}", 'characters' => '')
  end
end
