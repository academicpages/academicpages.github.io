---
title: What&#x27;s wrong with Ubuntu on my laptop
date: 2020-12-16
permalink: /posts/2020/12/whats-wrong-with-ubuntu-on-my-laptop/
tags:
---

I've been a many-years user of Macs, and so I was a little deflated when my job
sent me a Windows machine, a Lenovo T490S. So I immediately installed Ubuntu as
a dual-boot, hoping that I could live forever in Linux-land and closely
approximately my Mac experience. Here was the result:

Pro's of Linux-land:

- Boot-up is fast. Once I enter my login credentials, the desktop is up and
  ready to go in a second. This is a big contrast from the slow, churning
startup of both Mac and Windows.
- There's no bloat. There's nothing I didn't ask for here.
- For a modeler/data scientist, there's no better environment than being able
  to fire up the terminal and be ready to compute.
  [Conda](https://docs.conda.io/en/latest/miniconda.html) helped a lot on Mac to
  get the OS environment (with its Python 2) separated from my work environment,
  and [WSL](https://docs.microsoft.com/en-us/windows/wsl/install-win10) gave me
  Linux within Windows. But nothing beats Linux for this.

Con's of Linux-land:

- A few things didn't work on my laptop. It's amazing how these small things
  can become such a part of your routine that they seem almost essential.
    - Swipe gestures to go forward/back in my web browser. Apparently there's a
      [Chrome extension](https://chrome.google.com/webstore/detail/swipe-gesture/mgegfjnccpnkdppohmfgnjalkediapkc)
      that kind of does this, but not well enough to be seamless.
    - Windows and ChromeOS use the same keystroke (Ctrl+Tab) to move between
      browser tabs and terminal tabs. Weirdly, in Ubuntu, the terminal tabs
      need Ctrl+PageUp, which I find tremendously unnatural. For reasons I had to dig
      to find and then didn't understand, you can't remap the terminal to accept
      Ctrl+Tab instead.
- There's no Word or Excel on Linux. I know, there are ways around it, but it's
  going to be that much of a pain, I'd rather just fire up Windows instead.
  (Google Drive has gotten really close, so that I know edit even my `.docx`
  resume in Drive. But it's not sufficiently seamless to collaborate.)
- There's no Google Drive backup program. For most things, it's OK to use the
  online interface, but I still like the idea of being able to interact with my
  files locally.

I recognize that these are such small things (aside from Office software!) that
I might be able to hunt around among other distros to get a better experience.
