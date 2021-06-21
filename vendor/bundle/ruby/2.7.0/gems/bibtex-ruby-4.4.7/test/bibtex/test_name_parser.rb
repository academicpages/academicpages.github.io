require 'helper'

module BibTeX
  class NameParserTest < Minitest::Spec

    describe "parse a number of entries having a 'van' or 'van den' name prefix" do
      before do
        @a = Names.parse('van den Bout, D. E.')
        @b = Names.parse('Van den Bout, D. E.')
      end

      it "should parse 'van den' part starting with lowercase letter" do
        assert_equal(@a[0].to_s, "van den Bout, D. E.")
        assert_equal(@a[0].prefix, "van den")
      end

      it "should parse 'Van den' part starting with uppercase letter" do
        assert_equal(@b[0].to_s, "Van den Bout, D. E.")
        assert_equal(@b[0].prefix, "Van den")
      end

      it "should accept empty strings" do
        assert_equal '', Names.parse("").to_s
      end

    end

  end
end
