require 'helper'

module BibTeX
  class ElementTest < Minitest::Spec
    describe '.parse' do
      it 'accepts a BibTeX string' do
        Element.parse('@misc{x,},@misc{y,}').length.must_be :==, 2
      end

      it 'accepts an Element' do
        Element.parse(Comment.new('blah')).length.must_be :==, 1
      end

      it 'accepts a Hash and returns an Entry' do
        Element.parse(bibtex_type: :book)[0].type.must_be :==, :book
      end

      it 'accepts an array of hashes' do
        Element.parse([{ bibtex_type: :book }, { bibtex_type: :misc }])[1].type.must_be :==, :misc
      end
    end
  end

  class PreambleTest < Minitest::Spec
    describe 'a new preamble instance' do
      before do
        @preamble = Preamble.new
      end

      it 'should not be nil' do
        assert @preamble
      end
    end

    describe 'given a set of @preambles' do
      before do
        @bib = BibTeX.open(Test.fixtures(:preamble))
        @preambles = @bib.preambles
      end

      it 'should support round-trips of all parsed preambles' do
        assert_equal %(@preamble{ "This bibliography was created \\today" }\n), @preambles[0].to_s
        assert_equal %(@preamble{ "Bib\\TeX" }\n), @preambles[1].to_s
        assert_equal %(@preamble{ "Maintained by " # maintainer }\n), @preambles[2].to_s
      end

      it 'should support string replacement of preamble contents' do
        assert_equal '"Maintained by " # maintainer', @preambles[2].value.to_s
        @bib.replace_strings
        assert_equal '"Maintained by " # "Myself"', @preambles[2].value.to_s
        @bib.join_strings
        assert_equal 'Maintained by Myself', @preambles[2].value.to_s
      end
    end
  end
end
