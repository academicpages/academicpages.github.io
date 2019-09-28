---
date: '2015-06-11'
slug: git-for-smart-people
title: git for smart people
---

###### What's git?





[Git](https://git-scm.com/) is a form of [version control](https://git-scm.com/book/en/v2/Getting-Started-About-Version-Control). Like its peer Mercurial and its predecessor subversion, git is a tool that lets you set up and interact with repositories ("repos") of your code or text or whatever.





###### How do I use that?





In the simple case, you have just one local repo right in your working directory. You back up all the revisions of your code to that repo. The command you need to get started is `git init`.





All the commands you need to know in your early git days are in github's handy [cheat sheet](https://training.github.com/kit/downloads/github-git-cheat-sheet.pdf), but you can mostly focus on `git commit` and `git diff`. Github also has a cool interactive [tutorial](https://try.github.io) for getting started.





Things get a little more complicated when you have more than one repo. Here the key is `git clone`. If you start a new repo on [github](https://github.com/), the website is kind enough to show you exactly what commands you need to run to either connect an existing repo you have or to start a whole new repo. Now you'll need to now about `git push` and `git pull`.





###### What are some tricks of the trade?





Folks at MIT will be happy to know that they can go to [github.mit.edu](https://github.mit.edu/) and automatically have an enterprise-level account associated with their MIT certificate. This means that you can set up private repos for free! If you don't like github, you can take the jankier approach and use the [MIT scripts](http://scripts.mit.edu/) service, which has automation for hosting git repos on [Athena](https://ist.mit.edu/athena).





Learn just enough about `git config` to do `git config --global` for `user.name`, `user.email`, and `core.editor`. I can't stand it when nano comes up when I want vim.





I wrote an [earlier post](http://scottolesen.com/blog/using-git-with-word-documents/) on how you can use git with Word documents. Word documents are binary, which doesn't play well with the standard difference-finding methods, but there's a way to get clever about it.





Take a peek at github's other nice tool, the [gist](https://gist.github.com/). It's elegant.





Lots of software can integrate with git. Check to see if there's a plugin and if it's actually easier to use than simply returning to the command line.





###### What are the words to the wise?





Once you get comfortable with committing, diffing, pushing, and pulling, start branching. Learn `git branch`, `git merge`, and `git checkout -b`. Branch early and branch often.