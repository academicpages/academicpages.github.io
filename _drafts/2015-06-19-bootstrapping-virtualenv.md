---
date: '2015-06-19'
slug: bootstrapping-virtualenv
title: bootstrapping virtualenv
---

I worked on a cluster, and I wanted to set up my own python environment. The network of incompatibilities eventually showed me that I would need to download my own Python source code (I wanted 3.4) and my own version of [virtualenv](https://pypi.python.org/pypi/virtualenv). I installed Python locally using the typical





    <code>./configure --prefix=$HOME/local
    make
    make install
    </code>





but I was suddenly in a pickle, because when I tried to open a virtual environment [by bootstrapping](http://eli.thegreenplace.net/2013/04/20/bootstrapping-virtualenv), I was told that Python did not have the `zlib` module installed.





Only after some consternation did [I find that](http://www.1stbyte.com/2005/06/26/configure-and-compile-python-with-zlib/) I had to separately download and install [zlib](http://www.zlib.net/) from source, and then re-install Python using





    <code>./configure --prefix=$HOME/local --with-zlib=$HOME/local/include
    </code>





After this, I could start up my own virtual environment





    <code>cd ~
    /path/to/local/python3 /path/to/virtualenv-13.0.3/virtualenv.py my_env_name
    </code>