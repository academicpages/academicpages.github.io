---
title: 'How to Use Git to Share Your Work'
date: 2018-02-27
permalink: /posts/2018/02/how-to-use-git-to-share-your-work.md/
tags:
  - tutorial
  - R package
  - git
---

This post briefly introduces how to use Git to share your work and connect your Github with Rstudio.

I would suggest you to install git first by using brew install git.
Then you should have a github account. You can get an account here: github.com.

Once you set up these two things, you can configure your git settings:
```
git config --global user.name "First name Last name"
git config --global user.name "This email should be same as github account email"
```

After these, open your Rstudio and go to preferences to set up the git/svn, choose git. Then restart the rstudio and go to the previous same place to click view public key and paste it.

Go back to github.com and log in. Go to settings to create a ssh public key by pasting the key from Rstudio.

Once configuring these things, create a repo and click clone and downlod to get the link.

Open a terminal and cd to the directory.

Paste the following:
```
git clone "the link you copied from the repo you have created"
```
If it succeeds, then you should be able to download the entire repo to your local computer.

Then you can use git status, git add, git push, etc to syn your work with github repo.

For more details, you can check this book [happy git with r](http://happygitwithr.com/).
