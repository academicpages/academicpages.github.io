require 'test_helper'

class HashOrderingTest < Minitest::Test
  module MoneyFilter
    def money(input)
      sprintf(' %d$ ', input)
    end
  end

  module CanadianMoneyFilter
    def money(input)
      sprintf(' %d$ CAD ', input)
    end
  end

  include Liquid

  def test_global_register_order
    with_global_filter(MoneyFilter, CanadianMoneyFilter) do
      assert_equal " 1000$ CAD ", Template.parse("{{1000 | money}}").render(nil, nil)
    end
  end
end
