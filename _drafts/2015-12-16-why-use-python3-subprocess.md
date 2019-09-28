---
date: '2015-12-16'
slug: why-use-python3-subprocess
title: Why use Python3? Subprocess!
---

The other day my boss asked me [why I was using Python3](https://wiki.python.org/moin/Python2orPython3). I wish I had had this answer at that time:

I have [some scripts](https://github.com/swo/caravan) that call [`usearch`](http://www.drive5.com/usearch/), a program that does DNA sequence searches and clustering. `usearch` is a command-line program that outputs some information to standard output (`stdout`) and some to standard error (`stderr`).

In an ideal world, I'd like to keep those two streams separate. In Perl or Python2, the easiest way I found to access `stderr` was to pipe it to `stdout`:


      # Perl
      my $output = `usearch foo-args 2>&1`;





      # Python2
      import subprocess
      output = subprocess.check_output(["usearch", "foo-args"], stderr=subprocess.STDOUT)



Both of these are clumsy, and the Python2 is remarkably inelegant.

I was pleased to find that the easy way in Python3 is also the nice way! Python3's `[subprocess](https://docs.python.org/3/library/subprocess.html)` module has a routine `run` that returns an object whose attributes contain (separately!) the two output streams from the command:


      # Python3
      import subprocess
      result = subprocess.run(["usearch", "foo-args"])
      # the stdout is in result.stdout
      # the sterr is in result.stderr
