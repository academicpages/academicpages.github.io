---
date: '2017-02-14'
slug: what-to-do-when-working-on-a-python-project
title: What to do when working on a Python project
---

Sometimes people ask me what they should learn about if they want to learn to be a better programmer. (These are mostly scientists who write programs only for their own consumption.) My answer usually surprises them:





  1. Learn a real language. That can be [Python](https://www.jeffknupp.com/writing-idiomatic-python-ebook/), [R](https://github.com/hadley/dplyr), or whatever, so long as it's not Matlab. (A note about Matlab: I will never say that Matlab is not useful or not good, but I will say that Matlab is not a "real" programming language. Programming is a lot about abstraction: you write functions and more functions. In Matlab, every function has to be in its own file with a name that matches the name of the function. This is not a good paradigm for hierarchical organization of code. If you don't understand what that means, see #1.)


  2. Use version control, probably [git](https://git-scm.com/) and [github](https://github.com/) (or [bitbucket](https://bitbucket.org/)). MIT students get [free private repositories](https://github.mit.edu/), which is sweet.


  3. Write [unit tests](http://docs.python-guide.org/en/latest/writing/tests/). The more I write code the more I realize I code have saved time by writing the tests first.



To get more advanced around Python, I found [this post](https://jeffknupp.com/blog/2013/08/16/open-sourcing-a-python-project-the-right-way/) by Jeff Knupp to be really useful (if a bit dated). Python, for being so nice in some respects, has some really confusing parts (for me, that's project dependencies and project file structure). This post was one of the best ways I saw to clean that up. It taught me about [tox](https://tox.readthedocs.io/en/latest/), and I used it as a guide in setting up [a recent project](https://github.com/swo/magibib).

It's tempting to think that the way to get better is to dive into the sexy stuff. (I just learned that Python has [macros](https://github.com/lihaoyi/macropy), waaaa.) But it's mostly about this bread and butter!

