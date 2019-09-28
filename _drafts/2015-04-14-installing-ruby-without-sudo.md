---
date: '2015-04-14'
slug: installing-ruby-without-sudo
title: Installing ruby without sudo
---

I do a lot of work on a compute cluster where I don't have administrative privileges. I wanted ruby, but I didn't want to ask it to be installed. It turns out that you should probably use version control for all your languages! Python has [virtualenv](http://docs.python-guide.org/en/latest/dev/virtualenvs/), ruby has [rvm](https://rvm.io/).





The first step is the hair-raising `curl | bash` listed on the rvm website. This should set up rvm. It’s nice and made for non-sudoers; it installs in a local directory by default. If you get any warnings, probably check up on those.





I wanted to use ruby 2.0.0 because that’s what I have on my personal machine. Running the recommended `rvm install 2.0` led to requests for a password, which are due to rvm’s desire to install some dependencies as necessary. I crossed my fingers and tried to do without these libraries: `rvm install 2.0.0 --autolibs=0`.





rvm automatically gives you `gem`, so I was happy to be able to install my favorite gem: `gem install arginine`. Worked like a charm.