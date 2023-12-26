require File.expand_path('../helper', __FILE__)

class TestRecipe < TestCase
  def test_path
    recipe = MiniPortile.new("libfoo", "1.0.0")
    assert_equal(File.expand_path(File.join(recipe.target, recipe.host, recipe.name, recipe.version)), recipe.path)
  end

  def test_lib_path
    recipe = MiniPortile.new("libfoo", "1.0.0")
    assert_equal(File.join(recipe.path, "lib"), recipe.lib_path)
  end

  def test_include_path
    recipe = MiniPortile.new("libfoo", "1.0.0")
    assert_equal(File.join(recipe.path, "include"), recipe.include_path)
  end
end
