---
date: 2023-02-13
tags:
- stream
- tools
title: friendship ended with `earlyoom`, now `nohang` is my best friend
---

![friendship ended with earlyoom, now nohang is my best friend](/files/earlyoom_nohang.jpg)

I used to use `earlyoom` to ensure that my desktop PC will still keep running if a program hogs all the memory (e.g. loading a too-large dataset into memory). I recently couldn't get `earlyoom` to work with Fedora 37, and while searching for a solution I found `nohang`. Here are some useful features of `nohang` which convinced me to switch:

* Desktop notification when a program is killed.
![OOM notification](/files/nohang_notification.jpg)
* Includes a demo command, `nohang --memload`, to safely test out a low-memory situation.
* Easy to build from source and sensible default config.

Both are very useful and well-made programs, but `nohang` was better for my situation. Try them out!
* [nohang@Github](https://github.com/hakavlad/nohang)
* [earlyoom@Github](https://github.com/rfjakob/earlyoom)
