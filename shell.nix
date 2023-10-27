# Nix environment for Jekyll blog development

# The instructions from this blog post worked.
# https://nathan.gs/2019/04/19/using-jekyll-and-nix-to-blog/

with import <nixpkgs> { };

let jekyll_env = bundlerEnv rec {
    name = "jekyll_env";
    inherit ruby;
    gemfile = ./Gemfile;
    lockfile = ./Gemfile.lock;
    gemset = ./gemset.nix;
  };
in
  stdenv.mkDerivation rec {
    name = "jekyll";
    buildInputs = [ jekyll_env bundler ruby zlib ];

    shellHook = ''
      exec ${jekyll_env}/bin/jekyll serve --watch --force_polling --future
    '';
  }

# echo "Use `bundle exec jekyll serve`"
# BUNDLE_FORCE_RUBY_PLATFORM = "true";