if ENV["COVERALL"]
  require "coveralls"
  Coveralls.wear!
end

require "minitest/autorun"
require "minitest/reporters"
require "mocha/setup"

Minitest::Reporters.use! Minitest::Reporters::DefaultReporter.new(color: true)

$LOAD_PATH.unshift File.expand_path("../../lib", __FILE__)
require "public_suffix"

Minitest::Test.class_eval do
  unless method_exists?(:assert_not_equal)
    def assert_not_equal(exp, act, msg = nil)
      assert_operator(exp, :!=, act, msg)
    end
  end
end
