. "c:\var\vcap\packages\windows-ruby-dev-tools\prelude.ps1"

$env:RUBYOPT = "-rdevkit"

push-location mini_portile

    system-cmd "gem install bundler"
    system-cmd "bundle install"
    system-cmd "bundle exec rake test"

pop-location
