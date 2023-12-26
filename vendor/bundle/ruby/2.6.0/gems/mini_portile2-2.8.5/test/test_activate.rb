require File.expand_path('../helper', __FILE__)

class TestActivate < TestCase
  attr_reader :recipe

  def setup
    super

    @save_env = %w[PATH CPATH LIBRARY_PATH LDFLAGS].inject({}) do |env, var|
      env.update(var => ENV[var])
    end

    FileUtils.rm_rf(["tmp", "ports"]) # remove any previous test files

    @recipe = MiniPortile.new("foo", "1.0.0").tap do |recipe|
      recipe.logger = StringIO.new
    end
  end

  def teardown
    FileUtils.rm_rf(["tmp", "ports"]) # remove any previous test files

    @save_env.each do |var, val|
      ENV[var] = val
    end

    super
  end

  def test_PATH_env_var_when_bin_does_not_exist
    ENV["PATH"] = "foo"
    refute(Dir.exist?(bin_path))
    refute_includes(path_elements('PATH'), bin_path)

    recipe.activate

    refute_includes(path_elements('PATH'), bin_path)
  end

  def test_PATH_env_var_when_bin_exists
    ENV["PATH"] = "foo"
    FileUtils.mkdir_p(bin_path)
    refute_includes(path_elements('PATH'), bin_path)

    recipe.activate

    assert_includes(path_elements('PATH'), bin_path)
    assert_equal(path_elements('PATH').first, bin_path)
  end

  def test_CPATH_env_var_when_include_does_not_exist
    ENV["CPATH"] = "foo"
    refute(Dir.exist?(include_path))
    refute_includes(path_elements('CPATH'), include_path)

    recipe.activate

    refute_includes(path_elements('CPATH'), include_path)
  end

  def test_CPATH_env_var_when_include_exists
    ENV["CPATH"] = "foo"
    FileUtils.mkdir_p(include_path)
    refute_includes(path_elements('CPATH'), include_path)

    recipe.activate

    assert_includes(path_elements('CPATH'), include_path)
    assert_equal(path_elements('CPATH').first, include_path)
  end

  def test_LIBRARY_PATH_env_var_when_lib_does_not_exist
    ENV["LIBRARY_PATH"] = "foo"
    refute(Dir.exist?(lib_path))
    refute_includes(path_elements('LIBRARY_PATH'), lib_path)

    recipe.activate

    refute_includes(path_elements('LIBRARY_PATH'), lib_path)
  end

  def test_LIBRARY_PATH_env_var_when_lib_exists
    ENV["LIBRARY_PATH"] = "foo"
    FileUtils.mkdir_p(lib_path)
    refute_includes(path_elements('LIBRARY_PATH'), lib_path)

    recipe.activate

    assert_includes(path_elements('LIBRARY_PATH'), lib_path)
    assert_equal(path_elements('LIBRARY_PATH').first, lib_path)
  end

  def test_LDFLAGS_env_var_when_not_cross_compiling
    ENV["LDFLAGS"] = "-lfoo"
    FileUtils.mkdir_p(lib_path)
    assert_equal(recipe.host, recipe.original_host) # assert on setup)

    refute_includes(flag_elements('LDFLAGS'), "-L#{lib_path}")

    recipe.activate

    refute_includes(flag_elements('LDFLAGS'), "-L#{lib_path}")
  end

  def test_LDFLAGS_env_var_when_cross_compiling
    ENV["LDFLAGS"] = "-lfoo"
    recipe.host = recipe.original_host + "-x" # make them not-equal
    FileUtils.mkdir_p(lib_path)

    refute_includes(flag_elements('LDFLAGS'), "-L#{lib_path}")

    recipe.activate

    assert_includes(flag_elements('LDFLAGS'), "-L#{lib_path}")
    assert_equal(flag_elements('LDFLAGS').first, "-L#{lib_path}")
  end

  private

  def path_elements(varname)
    ENV.fetch(varname, "").split(File::PATH_SEPARATOR)
  end

  def flag_elements(varname)
    ENV.fetch(varname, "").split
  end

  def bin_path
    MiniPortile.native_path(File.join(recipe.path, "bin"))
  end

  def include_path
    MiniPortile.native_path(File.join(recipe.path, "include"))
  end

  def lib_path
    MiniPortile.native_path(File.join(recipe.path, "lib"))
  end
end
