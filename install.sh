#!/bin/bash
set -e

# Install asdf
git clone https://github.com/asdf-vm/asdf.git ~/.asdf --branch v0.13.1
. "$HOME/.asdf/asdf.sh"

# Install ruby plugin
asdf plugin add ruby https://github.com/asdf-vm/asdf-ruby.git
asdf install ruby 2.7.6
asdf global ruby 2.7.6
ruby --version

# Install nodejs
asdf plugin add nodejs https://github.com/asdf-vm/asdf-nodejs.git
asdf install nodejs latest
node --version

# Install packages
gem install bundler
bundle clean
bundle install
