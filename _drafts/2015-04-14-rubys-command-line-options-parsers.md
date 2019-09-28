---
date: '2015-04-14'
slug: rubys-command-line-options-parsers
title: Parsing options and arguments in ruby
---

There are lots of command line parsers for ruby. To my mind, [optparse](http://ruby-doc.org/stdlib-2.2.0/libdoc/optparse/rdoc/OptionParser.html) seems clunky, [Thor](http://whatisthor.com/) is verbose and focused on a particular need (subcommands), and [Trollop](http://trollop.rubyforge.org/) has a beautiful DSL syntax but is an _option_ parser (and so doesn't do positional arguments).





A lot of the scripts I write are small and do one little thing, but I can never remember what the syntax is. I wanted a command-line parser that would have the nice syntax of Trollop but allow for positional arguments, automatic generation of help messages, etc.





I ended up writing [arginine](https://github.com/swo/arginine), which I bolted on top of optparse. It's maybe not the most beautiful code, but it does everything I want. Trollop uses will find its syntax familiar:





    <code>require 'arginine'
    par = Arginine::parse do
      arg :my_first_arg
      arg "my second arg"
      opt :my_option
      flag :my_flag
      argf "input files"
    end
    </code>





Calling `script.rb arg1 arg2 --my_option opt1 --my_flag file1 file2` returns a hash `par` with values `{:my_first_arg => 'arg1', "my second arg" => arg2, :my_option => 'opt1', :my_flag => true}`. The `file1 file2` are left available for line-by-line iteration with `ARGF`.