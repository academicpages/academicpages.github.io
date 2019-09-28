---
date: '2015-04-14'
slug: eternal-ssh
title: Eternal ssh
---

[Mosh](https://mosh.mit.edu/) is an awesome tool for folks who repeatedly ssh to one machine. In an ideal world, you can keep stay logged in to the machine even as your computer's internet connection turns on and off. Mosh does exactly this. I keep one terminal window open with mosh; whenever my computer reconnects to the internet, it automatically restarts the ssh session right where it left off, with no password entry or anything.





I wanted to use Mosh to connect to my computing cluster, but some dependencies were missing. It was a little confusing to get them set up, so I give the play-by-play here. First I got `protobuf`:





    <code>cd ~
    mkdir src && cd src
    wget https://protobuf.googlecode.com/files/protobuf-2.5.0.tar.gz
    tar xvzf protobuf-2.5.0.tar.gz
    cd protobuf-2.5.0
    ./autogen.sh
    ./configure --prefix=/home/my_name/local
    make
    make install
    </code>





Then I got mosh:





    <code>cd ~/src
    git clone https://github.com/keithw/mosh
    cd mosh
    ./autogen.sh
    PKG_CONFIG_PATH=/home/my_name/local/lib/pkgconfig ./configure --prefix=/home/my_name/local
    make
    make install
    </code>





If I don't specify the package config path, I get a message:





    <code>No package 'protobuf' found
    </code>





Don't be so sure that your home folder is in `/home/your_name` on every cluster! Just do a quick `pwd -P` to make sure you know where you are. The package config path must be absolute.





Then I can use mosh to log into the cluster. This whole bit is a single command on a single line:





    <code>mosh cluster_name server='LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/home/my_name/local/lib /home/my_name/local/bin/mosh-server'
    </code>





Without specifying the library path, I get an error:





    <code>error while loading shared libraries: libprotobuf.so.8: cannot open shared object file: No such file or directory
    </code>





Naturally I wrote an alias for that horrible line.