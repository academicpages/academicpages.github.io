require 'helper.rb'

module BibTeX
  class TestBibtex < Minitest::Unit::TestCase
    def test_empty?
      assert BibTeX.open(Test.fixtures(:empty)).empty?
      refute BibTeX.open(Test.fixtures(:bibdesk)).empty?
    end

    def test_parse
      bib = BibTeX.parse ' @book{ id, author = {Poe, Edgar Allen}, title = "Ligeia" } '
      assert_equal 1, bib.length
      assert_equal 'Ligeia', bib[:id].title
      assert_equal 'Poe, Edgar Allen', bib[:id].author.to_s
    end

    def test_validation
      log_level = BibTeX.log.level
      BibTeX.log.level = Logger::ERROR

      refute BibTeX.parse(' @book{ id, author = {Poe, Edgar Allen}, title = "Ligeia" } ').valid?
      assert BibTeX.parse(' @book{ id, author = {Poe, Edgar Allen}, title = "Ligeia", publisher = "Penguin", year = 1996 } ').valid?
      assert BibTeX.parse(' @book{ id, editor = {Poe, Edgar Allen}, title = "Ligeia", publisher = "Penguin", year = 1996 } ').valid?
      refute BibTeX.parse(' @book{ id, xxxxxx = {Poe, Edgar Allen}, title = "Ligeia", publisher = "Penguin", year = 1996 } ').valid?
      refute BibTeX.parse(' @book{ id, author = {Poe, Edgar Allen}, title = "Lig"eia", publisher = "Penguin", year = 1996 } ').valid?
      assert BibTeX.valid?(Test.fixtures(:bibdesk))

      BibTeX.log.level = log_level
    end
  end
end
