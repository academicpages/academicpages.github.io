---
layout: single
permalink: /coding/versio-control/
author_profile: false
title: <center>VERSION CONTROL WITH GIT
sidebar:
  nav: "sidenav"
toc: true
---
  
In this web I will take you through Version Control with [Git](https://git-scm.com/) by summarizing important concepts and operations. Most of the materials can be found in the [Git Book](https://git-scm.com/book/en/v2). I assume that you have a Git account registered, otherwise you can do that quickly on the [GItHub website](https://github.com/)
  
## What is version control
Version control is a system that records changes to a file or set of files over time so that you can recall specific versions later. Many people’s version-control method of choice is to copy files into another directory (perhaps a time-stamped directory). This approach is very common because it is so simple, but it is also incredibly error prone. It is easy to forget which directory you’re in and accidentally write to the wrong file or copy over files you don’t mean to. To deal with this issue, programmers long ago developed local VCSs that had a simple database that kept all the changes to files under revision control.

## Git Basics
 Git thinks of its data more like a series of snapshots of a miniature filesystem. With Git, every time you commit, or save the state of your project, Git basically takes a picture of what all your files look like at that moment and stores a reference to that snapshot. To be efficient, if files have not changed, Git doesn’t store the file again, just a link to the previous identical file it has already stored. Git thinks about its data more like a stream of snapshots.
 
### Git Has Integrity

Everything in Git is checksummed before it is stored and is then referred to by that checksum. This means it’s impossible to change the contents of any file or directory without Git knowing about it. This functionality is built into Git at the lowest levels and is integral to its philosophy. You can’t lose information in transit or get file corruption without Git being able to detect it.

### The Three States

Pay attention now — here is the main thing to remember about Git if you want the rest of your learning process to go smoothly. Git has three main states that your files can reside in: committed, modified, and staged:

- Committed means that the data is safely stored in your local database.
- Modified means that you have changed the file but have not committed it to your database yet.
- Staged means that you have marked a modified file in its current version to go into your next commit snapshot.

This leads us to the three main sections of a Git project: the Git directory, the working tree, and the staging area.
The Git directory is where Git stores the metadata and object database for your project. This is the most important part of Git, and it is what is copied when you clone a repository from another computer.
The working tree is a single checkout of one version of the project. These files are pulled out of the compressed database in the Git directory and placed on disk for you to use or modify.
The staging area is a file, generally contained in your Git directory, that stores information about what will go into your next commit. Its technical name in Git parlance is the “index”, but the phrase “staging area” works just as well.
The basic Git workflow goes something like this:

1. You modify files in your working tree.
2. You selectively stage just those changes you want to be part of your next commit, which adds only those changes to the staging area.
3. You do a commit, which takes the files as they are in the staging area and stores that snapshot permanently to your Git directory.

## [Installng git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)

## Working with Git

### Set-up the environment

We assume that you are working on LINUX command line,NOte that all materials summarized here can be found in the [Git book] (https://git-scm.com/book/en/v2). The first thing you should do when you install Git is to set your user name and email address. This is important because every Git commit uses this information, and it’s immutably baked into the commits you start creating:
<pre>
$ git config --global user.name "aldzhao"
$ git config --global user.email zhao.alcide@gmail.com
</pre>
Once you have installed Git, you can call it by
<pre>
$ git
</pre>




