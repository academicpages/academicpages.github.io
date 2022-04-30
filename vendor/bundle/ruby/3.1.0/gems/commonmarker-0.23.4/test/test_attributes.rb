# frozen_string_literal: true

require 'test_helper'

class TestAttributes < Minitest::Test
  def setup
    contents = fixtures_file('dingus.md')
    @doc = CommonMarker.render_doc(contents.strip)
  end

  def test_sourcepos
    sourcepos = []

    @doc.walk do |node|
      sourcepos << node.sourcepos
    end

    sourcepos.delete_if { |h| h.values.all?(&:zero?) }

    result = [{ start_line: 1, start_column: 1, end_line: 10, end_column: 12 }, { start_line: 1, start_column: 1, end_line: 1, end_column: 17 }, { start_line: 1, start_column: 4, end_line: 1, end_column: 17 }, { start_line: 3, start_column: 1, end_line: 5, end_column: 36 }, { start_line: 3, start_column: 1, end_line: 3, end_column: 55 }, { start_line: 4, start_column: 1, end_line: 4, end_column: 53 }, { start_line: 4, start_column: 2, end_line: 4, end_column: 14 }, { start_line: 4, start_column: 54, end_line: 4, end_column: 58 }, { start_line: 5, start_column: 1, end_line: 5, end_column: 36 }, { start_line: 7, start_column: 1, end_line: 10, end_column: 12 }, { start_line: 7, start_column: 1, end_line: 7, end_column: 11 }, { start_line: 7, start_column: 4, end_line: 7, end_column: 11 }, { start_line: 7, start_column: 4, end_line: 7, end_column: 11 }, { start_line: 8, start_column: 1, end_line: 10, end_column: 12 }, { start_line: 8, start_column: 4, end_line: 8, end_column: 11 }, { start_line: 8, start_column: 4, end_line: 8, end_column: 11 }, { start_line: 9, start_column: 4, end_line: 10, end_column: 12 }, { start_line: 9, start_column: 4, end_line: 9, end_column: 12 }, { start_line: 9, start_column: 6, end_line: 9, end_column: 12 }, { start_line: 9, start_column: 6, end_line: 9, end_column: 12 }, { start_line: 10, start_column: 4, end_line: 10, end_column: 12 }, { start_line: 10, start_column: 6, end_line: 10, end_column: 12 }, { start_line: 10, start_column: 6, end_line: 10, end_column: 12 }]

    assert_equal result, sourcepos
  end
end
