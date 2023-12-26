require File.expand_path('../helper', __FILE__)

require "mkmf" # initialize $LDFLAGS et al here, instead of in the middle of a test

class TestMkmfConfig < TestCase
  attr_reader :recipe

  LIBXML_PCP = File.join(__dir__, "assets", "pkgconf", "libxml2")
  LIBXSLT_PCP = File.join(__dir__, "assets", "pkgconf", "libxslt")

  def make_recipe(name, version)
    MiniPortile.new(name, version).tap do |recipe|
      recipe.logger = StringIO.new # hush output
    end
  end

  def setup
    super

    @save_env = %w[PATH CPATH LIBRARY_PATH LDFLAGS PKG_CONFIG_PATH].inject({}) do |env, var|
      env.update(var => ENV[var])
    end
    $INCFLAGS = "-I/xxx"
    $LIBPATH = ["xxx"]
    $CFLAGS = "-xxx"
    $CXXFLAGS = "-xxx"
    $libs = "-lxxx"
    $MINI_PORTILE_STATIC_LIBS = {}

    FileUtils.rm_rf(["tmp", "ports"]) # remove any previous test files

    @recipe = make_recipe("libfoo", "1.0.0")
  end

  def teardown
    FileUtils.rm_rf(["tmp", "ports"]) # remove any previous test files

    $INCFLAGS = ""
    $LIBPATH = []
    $CFLAGS = ""
    $CXXFLAGS = ""
    $libs = ""
    $MINI_PORTILE_STATIC_LIBS = {}
    @save_env.each do |var, val|
      ENV[var] = val
    end

    super
  end

  def test_mkmf_config_recipe_LIBPATH_global_lib_dir_does_not_exist
    recipe.mkmf_config

    refute_includes($LIBPATH, recipe.lib_path)
    refute_includes($libs.shellsplit, "-lfoo")
  end

  def test_mkmf_config_recipe_LIBPATH_global_not_static
    FileUtils.mkdir_p(recipe.lib_path)

    recipe.mkmf_config

    assert_includes($LIBPATH, recipe.lib_path)
    assert_operator($LIBPATH.index(recipe.lib_path), :<, $LIBPATH.index("xxx")) # prepend

    assert_includes($libs.shellsplit, "-lfoo") # note the recipe name is "libfoo"
    assert_match(%r{-lfoo.*-lxxx}, $libs) # prepend
  end

  def test_mkmf_config_recipe_LIBPATH_global_static
    FileUtils.mkdir_p(recipe.lib_path)
    static_lib_path = File.join(recipe.lib_path, "libfoo.#{$LIBEXT}")

    recipe.mkmf_config(static: "foo")

    refute_includes($LIBPATH, recipe.lib_path)

    refute_includes($libs.shellsplit, "-lfoo") # note the recipe name is "libfoo"
    assert_includes($libs.shellsplit, static_lib_path)
    assert_match(%r{#{static_lib_path}.*-lxxx}, $libs) # prepend
  end

  def test_mkmf_config_recipe_INCFLAGS_global_include_dir_does_not_exist
    recipe.mkmf_config

    refute_includes($INCFLAGS.shellsplit, "-I#{recipe.include_path}")
  end

  def test_mkmf_config_recipe_INCFLAGS_global
    FileUtils.mkdir_p(recipe.include_path)

    recipe.mkmf_config

    assert_includes($INCFLAGS.shellsplit, "-I#{recipe.include_path}")
    assert_match(%r{-I#{recipe.include_path}.*-I/xxx}, $INCFLAGS) # prepend
  end

  def test_mkmf_config_pkgconf_does_not_exist
    assert_raises(ArgumentError) do
      recipe.mkmf_config(pkg: "foo")
    end
  end

  def test_mkmf_config_pkgconf_LIBPATH_global_not_static
    # can't get the pkgconf utility to install on windows with ruby 2.3 in CI
    skip if MiniPortile.windows? && RUBY_VERSION < "2.4"

    recipe.mkmf_config(pkg: "libxml-2.0", dir: LIBXML_PCP)

    assert_includes($LIBPATH, "/foo/libxml2/2.11.5/lib")
    assert_operator($LIBPATH.index("/foo/libxml2/2.11.5/lib"), :<, $LIBPATH.index("xxx")) # prepend
    refute_includes($LIBPATH, "/foo/zlib/1.3/lib")

    assert_includes($libs.shellsplit, "-lxml2")
    assert_match(%r{-lxml2.*-lxxx}, $libs) # prepend
    refute_includes($libs.shellsplit, "-lz")
  end

  def test_mkmf_config_pkgconf_LIBPATH_global_static
    # can't get the pkgconf utility to install on windows with ruby 2.3 in CI
    skip if MiniPortile.windows? && RUBY_VERSION < "2.4"

    static_lib_path = "/foo/libxml2/2.11.5/lib/libxml2.#{$LIBEXT}"

    recipe.mkmf_config(pkg: "libxml-2.0", dir: LIBXML_PCP, static: "xml2")

    refute_includes($LIBPATH, "/foo/libxml2/2.11.5/lib")
    refute_includes($libs.shellsplit, "-lxml2")
    assert_includes($libs.shellsplit, static_lib_path)
    assert_match(%r{#{static_lib_path}.*-lxxx}, $libs) # prepend

    assert_includes($LIBPATH, "/foo/zlib/1.3/lib") # from --static
    assert_includes($libs.shellsplit, "-lz") # from --static
  end

  def test_mkmf_config_pkgconf_CFLAGS_global
    # can't get the pkgconf utility to install on windows with ruby 2.3 in CI
    skip if MiniPortile.windows? && RUBY_VERSION < "2.4"

    recipe.mkmf_config(pkg: "libxml-2.0", dir: LIBXML_PCP)

    assert_includes($INCFLAGS.shellsplit, "-I/foo/libxml2/2.11.5/include/libxml2")
    assert_match(%r{-I/foo/libxml2/2.11.5/include/libxml2.*-I/xxx}, $INCFLAGS) # prepend

    assert_includes($CFLAGS.shellsplit, "-ggdb3")
    assert_match(%r{-xxx.*-ggdb3}, $CFLAGS) # append

    assert_includes($CXXFLAGS.shellsplit, "-ggdb3")
    assert_match(%r{-xxx.*-ggdb3}, $CXXFLAGS) # append
  end

  def test_mkmf_config_pkgconf_path_accumulation
    # can't get the pkgconf utility to install on windows with ruby 2.3 in CI
    skip if MiniPortile.windows? && RUBY_VERSION < "2.4"

    (ENV["PKG_CONFIG_PATH"] || "").split(File::PATH_SEPARATOR).tap do |pcpaths|
      refute_includes(pcpaths, LIBXML_PCP)
      refute_includes(pcpaths, LIBXSLT_PCP)
    end

    make_recipe("libxml2", "2.11.5").tap do |recipe|
      recipe.mkmf_config(pkg: "libxml-2.0", dir: LIBXML_PCP, static: "xml2")

      ENV["PKG_CONFIG_PATH"].split(File::PATH_SEPARATOR).tap do |pcpaths|
        assert_includes(pcpaths, LIBXML_PCP)
        refute_includes(pcpaths, LIBXSLT_PCP)
      end
    end

    make_recipe("libxslt", "1.13.8").tap do |recipe|
      recipe.mkmf_config(pkg: "libxslt", dir: LIBXSLT_PCP, static: "xslt")

      ENV["PKG_CONFIG_PATH"].split(File::PATH_SEPARATOR).tap do |pcpaths|
        assert_includes(pcpaths, LIBXML_PCP)
        assert_includes(pcpaths, LIBXSLT_PCP)
      end

      recipe.mkmf_config(pkg: "libexslt", dir: LIBXSLT_PCP, static: "exslt")
    end

    $INCFLAGS.shellsplit.tap do |incflags|
      assert_includes(incflags, "-I/foo/libxml2/2.11.5/include/libxml2")
      assert_includes(incflags, "-I/foo/libxslt/1.1.38/include")
    end
    $CFLAGS.shellsplit.tap do |cflags|
      assert_includes(cflags, "-ggdb3")
      assert_includes(cflags, "-Wno-deprecated-enum-enum-conversion")
    end
    refute_includes($LIBPATH, "/foo/libxml2/2.11.5/lib")
    refute_includes($LIBPATH, "/foo/libxslt/1.1.38/lib")
    assert_includes($LIBPATH, "/foo/zlib/1.3/lib") # from `--static`
    $libs.shellsplit.tap do |libflags|
      refute_includes(libflags, "-lxml2")
      assert_includes(libflags, "/foo/libxml2/2.11.5/lib/libxml2.#{$LIBEXT}")
      refute_includes(libflags, "-lxslt")
      assert_includes(libflags, "/foo/libxslt/1.1.38/lib/libxslt.#{$LIBEXT}")
      refute_includes(libflags, "-lexslt")
      assert_includes(libflags, "/foo/libxslt/1.1.38/lib/libexslt.#{$LIBEXT}")
      assert_includes(libflags, "-lz") # from `--static`
    end
  end
end
