---
title: Using git with Word documents
date: 2015-04-14
permalink: /posts/2015/04/using-git-with-word/
tags:
  - hacks
---

I like git, and I like to use it with most of my projects. But I mostly need to use Word to write manuscripts because it what and my co-authors and journals know how to work with.

Word uses a binary format, so `git diff` normally displays nothing useful. Martin Fenner posted an incredibly useful [blog post](http://blog.martinfenner.org/2014/08/25/using-microsoft-word-with-git/) that solved this whole problem for me.

I'm on OSX. First, I got [Pandoc](https://pandoc.org/), a tool that turns Word files into simpler text formats that can be more easily piped into `diff`.

Second, I needed to add some lines to the `.gitconfig` file in my home directory:

```toml
[diff "pandoc"]
  textconv=pandoc --to=markdown
  prompt=false
[alias]
  wdiff=diff --word-diff=color --unified=1
```

Third, in the git repo, I needed to create a new file `.gitattributes` with contents:

```toml
*.docx diff=pandoc
```

Et voila! `git diff` works just like I would hope.
