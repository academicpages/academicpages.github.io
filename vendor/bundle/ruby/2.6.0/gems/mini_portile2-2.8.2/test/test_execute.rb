require_relative "helper"

class TestExecute < TestCase
  def setup
    super
    @env = {"TEST_ENV_VAR1" => "VAR1_VALUE", "TEST_ENV_VAR2" => "VAR2_VALUE"}
    @recipe = MiniPortile.new("test_execute", "1.0.0")
    @log_path = @recipe.send(:tmp_path)
    FileUtils.mkdir_p File.join(@log_path, "subdir") # normally created by `download`
  end

  def test_execute_one_big_string_arg
    class << @recipe
      def execute_with_env(env)
        execute("testenv1",
                %Q(ruby -e "puts ENV['TEST_ENV_VAR1'].inspect ; exit 0"),
                {:env => env, :initial_message => false, :debug => true})
      end
    end

    @recipe.execute_with_env(@env)

    assert_equal("VAR1_VALUE".inspect, IO.read(File.join(@log_path, "testenv1.log")).chomp)
  end

  def test_execute_array_args
    class << @recipe
      def execute_with_env(env)
        execute("testenv2",
                ["ruby", "-e", "puts ENV['TEST_ENV_VAR2'].inspect"],
                {:env => env, :initial_message => false, :debug => true})
      end
    end

    @recipe.execute_with_env(@env)

    assert_equal("VAR2_VALUE".inspect, IO.read(File.join(@log_path, "testenv2.log")).chomp)
  end
end
