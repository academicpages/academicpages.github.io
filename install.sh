#!/bin/bash
sudo apt install nodejs
curl -fsSL https://github.com/rbenv/rbenv-installer/raw/HEAD/bin/rbenv-installer | bash
echo 'eval "$(rbenv init - zsh)"' >> ~/.zshrc
rbenv install 2.7.6
rbenv global 2.7.6
ruby --version
gem install bundler

bundle clean
bundle install
