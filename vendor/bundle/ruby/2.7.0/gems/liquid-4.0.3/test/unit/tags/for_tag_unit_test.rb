require 'test_helper'

class ForTagUnitTest < Minitest::Test
  def test_for_nodelist
    template = Liquid::Template.parse('{% for item in items %}FOR{% endfor %}')
    assert_equal ['FOR'], template.root.nodelist[0].nodelist.map(&:nodelist).flatten
  end

  def test_for_else_nodelist
    template = Liquid::Template.parse('{% for item in items %}FOR{% else %}ELSE{% endfor %}')
    assert_equal ['FOR', 'ELSE'], template.root.nodelist[0].nodelist.map(&:nodelist).flatten
  end
end
