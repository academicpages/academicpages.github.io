require 'helper.rb'

require 'yaml'

module BibTeX
  class TestString < Minitest::Unit::TestCase

    # def test_yaml_roundtrip
    #   b1 = BibTeX.open(Test.fixtures(:bibdesk))
    #   b2 = Bibliography.new(YAML.load(b1.to_yaml))
    #   assert_equal b1, b2
    # end

    def test_yaml
      bib = BibTeX::Bibliography.open(Test.fixtures(:bibdesk), :debug => false)
      yaml = YAML.load(bib.to_yaml)
      refute_nil(yaml)
      assert_equal(3, yaml.length)
      assert_equal(%w[ dragon pickaxe rails], yaml.map { |y| y[:bibtex_key] }.sort)
      assert_equal('{The Facets of Ruby}', yaml[0][:series])
    end

    def test_json
      bib = BibTeX::Bibliography.open(Test.fixtures(:bibdesk), :debug => false)
      json = JSON.parse(bib.to_json)
      refute_nil(json)
      assert_equal(3, json.length)
      assert_equal(%w[ dragon pickaxe rails], json.map { |y| y['bibtex_key'] }.sort)
      assert_equal('{The Facets of Ruby}', json[0]['series'])
    end

  end
end
