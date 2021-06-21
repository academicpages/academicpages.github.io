require 'helper.rb'

module BibTeX
  class StringTest < Minitest::Spec

    describe 'when parsing a simple string' do
      before do
        @bib = BibTeX.parse('@string{ foo = "bar" }')
      end        
      it 'should should not be empty' do
        assert_equal 1, @bib.length
      end
      it 'should have a symbol as key' do
        assert_equal :foo, @bib[0].key
      end
      it 'should have a value string' do
        assert_equal 'bar', @bib[0].value.to_s
      end
      it 'should have been registered' do
        refute @bib.strings[:foo].nil?
      end
    end

    # 
    # def test_replacement
    #   bib = BibTeX::Bibliography.open(Test.fixtures(:string_replacement), :debug => false)
    #   refute_nil(bib)
    #   assert(bib.kind_of?(BibTeX::Bibliography))
    #   refute(bib.empty?)
    #   assert_equal(7,bib.length)
    #   assert_equal([BibTeX::String,BibTeX::Preamble,BibTeX::Entry], bib.data.map(&:class).uniq) 
    #   assert_equal(["foo"], bib.strings[:foo])
    #   assert_equal(["bar"], bib.strings[:bar])
    #   assert_equal([:foo, "bar"], bib.strings[:foobar])
    #   assert_equal([:foobar, :foo], bib.strings[:foobarfoo])
    #   assert_equal([:bar, "foo", :bar], bib.strings[:barfoobar])
    #   assert_equal('"foo" # foo # foobarfoo # "bar"', bib.preambles[0].content)
    #   assert_equal('"foo" # barfoobar', bib[:'manual:1'].title)
    # 
    #   bib.replace_strings({ :filter => [:preamble]})
    #   assert_equal(["foo"], bib.strings[:foo])
    #   assert_equal(["bar"], bib.strings[:bar])
    #   assert_equal([:foo, "bar"], bib.strings[:foobar])
    #   assert_equal([:foobar, :foo], bib.strings[:foobarfoo])
    #   assert_equal([:bar, "foo", :bar], bib.strings[:barfoobar])
    #   assert_equal('"foo" # "foo" # foobar # foo # "bar"', bib.preambles[0].content)
    #   assert_equal('"foo" # barfoobar', bib[:'manual:1'].title)
    # 
    #   bib.replace_strings({ :filter => [:string]})
    #   assert_equal(['foo','bar'], bib.strings[:foobar])
    #   assert_equal(['foo', 'bar','foo'], bib.strings[:foobarfoo])
    #   assert_equal(['bar','foo','bar'], bib.strings[:barfoobar])
    #   assert_equal('"foo" # "foo" # foobar # foo # "bar"', bib.preambles[0].content)
    #   assert_equal('"foo" # barfoobar', bib[:'manual:1'].title)
    # 
    #   bib.replace_strings({ :filter => [:preamble,:entry]})
    #   assert_equal('"foo" # "foo" # "foo" # "bar" # "foo" # "bar"', bib.preambles[0].content)
    #   assert_equal('"foo" # "bar" # "foo" # "bar"', bib[:'manual:1'].title)
    # end
    #   
    # def test_roundtrip
    #   bib = BibTeX::Bibliography.open(Test.fixtures(:string_replacement), :debug => false)
    #   refute_nil(bib)
    #   assert_equal('@string{ foo = "foo" }', bib.data[0].to_s)
    #   assert_equal('@string{ bar = "bar" }', bib.data[1].to_s)
    #   assert_equal('@string{ foobar = foo # "bar" }', bib.data[2].to_s)
    #   assert_equal('@string{ foobarfoo = foobar # foo }', bib.data[3].to_s)
    #   assert_equal('@string{ barfoobar = bar # "foo" # bar }', bib.data[4].to_s)
    #   bib.replace_strings
    #   assert_equal('@string{ foo = "foo" }', bib.data[0].to_s)
    #   assert_equal('@string{ bar = "bar" }', bib.data[1].to_s)
    #   assert_equal('@string{ foobar = "foo" # "bar" }', bib.data[2].to_s)
    #   assert_equal('@string{ foobarfoo = "foo" # "bar" # "foo" }', bib.data[3].to_s)
    #   assert_equal('@string{ barfoobar = "bar" # "foo" # "bar" }', bib.data[4].to_s)
    #   bib.join_strings
    #   assert_equal('@string{ foo = "foo" }', bib.data[0].to_s)
    #   assert_equal('@string{ bar = "bar" }', bib.data[1].to_s)
    #   assert_equal('@string{ foobar = "foobar" }', bib.data[2].to_s)
    #   assert_equal('@string{ foobarfoo = "foobarfoo" }', bib.data[3].to_s)
    #   assert_equal('@string{ barfoobar = "barfoobar" }', bib.data[4].to_s)
    # end
  end
end