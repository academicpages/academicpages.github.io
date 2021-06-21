require 'test_helper'

class ContextTest < Minitest::Test
  include Liquid

  def test_override_global_filter
    global = Module.new do
      def notice(output)
        "Global #{output}"
      end
    end

    local = Module.new do
      def notice(output)
        "Local #{output}"
      end
    end

    with_global_filter(global) do
      assert_equal 'Global test', Template.parse("{{'test' | notice }}").render!
      assert_equal 'Local test', Template.parse("{{'test' | notice }}").render!({}, filters: [local])
    end
  end

  def test_has_key_will_not_add_an_error_for_missing_keys
    with_error_mode :strict do
      context = Context.new
      context.key?('unknown')
      assert_empty context.errors
    end
  end
end
