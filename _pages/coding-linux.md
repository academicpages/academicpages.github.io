---
layout: single
permalink: /coding/unix-shell/
author_profile: false
title: <center>Unix and Shell Programming
sidebar:
  nav: "sidenav"
toc: true
---

## What is UNIX? 
UNIX is an operating system which was first developed in the 1960s, and has been under constant development ever since. By operating system, we mean the suite of programs which make the computer work. It is a stable, multi-user, multi-tasking system for servers, desktops and laptops.UNIX systems also have a graphical user interface (GUI) similar to Microsoft Windows which provides an easy to use environment. However, knowledge of UNIX is required for operations which aren't covered by a graphical program, or for when there is no windows interface available, for example, in a telnet session.

## The UNIX operating system 
The UNIX operating system is made up of three parts; the kernel, the shell and the programs. 

- [The kernel](https://en.wikipedia.org/wiki/Linux_kernel)
- [The shell](https://en.wikipedia.org/wiki/Unix_shell): E.g. the most common [BASH](https://en.wikipedia.org/wiki/Bash_(Unix_shell)) shell.
- Files. Everything in UNIX are files. All the files are grouped together in the directory structure. The file-system is arranged in a hierarchical structure, like an inverted tree. The top of the hierarchy is traditionally called root (written as a slash / )

## Basic Operations

### Listing files and directories 
To find out what is in your home directory, type 
```ruby
ls
```
To list all files in your home directory including those whose names begin with a dot, type 
```ruby
ls -a
```
### make directory
To make a subdirectory called unixstuff in your current working directory type
```ruby
mkdir unixstuff 
```
### Change to directory
To change to the directory, note ./ is the current directory and ../ goes to the parent directory
```ruby
cd ./../../directory_name 
```


