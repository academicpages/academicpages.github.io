---
layout: single
permalink: /coding/unix-shell/
author_profile: false
sidebar:
  nav: "sidenav"
toc: true
---

# Introduction to Linux Shell and Shell Scripting

Before understanding shell scripting we have to get familiar with following terminologies –
- Kernel
- Shell
- Terminal

## what is kernel ?
The kernel is a computer program that is the core of a computer’s operating system, with complete control over everything in the system. It manages following resources of the Linux system –

- File management
- Process management
- I/O management
- Memory management
- Device management etc.


## what is shell ?
A shell is special user program which provide an interface to user to use operating system services. Shell accept human readable commands from user and convert them into something which kernel can understand. It is a command language interpreter that execute commands read from input devices such as keyboards or from files. The shell gets started when the user logs in or start the terminal.
BASH ([Bourne Again SHell](https://en.wikipedia.org/wiki/Bash_(Unix_shell))) is most widely used shell in Linux systems. It is used as default login shell in Linux systems and in macOS. It can also be installed on Windows OS.

## Shell Scripting

Usually shells are interactive that mean, they accept command as input from users and execute them. However some time we want to execute a bunch of commands routinely, so we have type in all commands each time in terminal.
As shell can also take commands as input from file we can write these commands in a file and can execute them in shell to avoid this repetitive work. These files are called Shell Scripts or Shell Programs. Shell scripts are similar to the batch file in MS-DOS. Each shell script is saved with .sh file extension eg. myscript.sh
