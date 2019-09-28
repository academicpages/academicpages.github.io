---
date: '2015-05-14'
slug: swig-mac-osx-and-python3
title: swig, Mac OSX, and python3
---

I had my eye on a new tool, snakemake, that a friend pointed out to me. I decided it was the moment to switch to Python 3.





I installed Python 3 using [MacPorts](https://www.macports.org/):





    <code>sudo port install python34
    sudo port select --set python python34
    </code>





That seemed pretty easy. The trouble came when I decided that it was _also_ time to start using [swig](http://www.swig.org/). In short, I was thinking about running some simulations that were conceptually simple but computationally expensive, and writing the heavy lifting sections in C sounded like just the ticket.





I tried to run the [example swig files](http://www.swig.org/tutorial.html) using the [library linking commands for OSX](http://www.dabeaz.com/cgi-bin/wiki.pl?SwigFaqMaxOSXSharedLibraries). I got an error `ld: library not found for -lintl`. When I switched back to `python27` using `port`, the compilation and library linking worked just fine.





I found the answer in an out-of-the-way post:





    <code> swig -python foo.i
     gcc -c foo.c
     gcc -c -I/opt/local/Library/Frameworks/Python.framework/Versions/3.4/include/python3.4m foo_wrap.c
     ld -bundle -flat_namespace -undefined suppress -o _foo.so foo.o foo_wrap.o
    </code>