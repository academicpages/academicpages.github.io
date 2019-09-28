---
date: '2015-05-27'
slug: cheaphints-for-hammerspoon
title: cheaphints for hammerspoon
---

I'm a big fan of using the keyboard. I was really excited when I found I could get vim-like control of Chrome with [vimium](https://vimium.github.io/). Basically, when in Chrome, I hit a key, and I get onscreen keyboard "hints" for each link. To follow a link, you press that key.





I wanted the same kind of functionality for managing my desktop. Rather than fumbling around with repeated cmd+tabs, I wanted to press a key, see a list of windows, and press another key to get there.





[Hammerspoon](http://www.hammerspoon.org/) seemed like the tool that would let me get there. There is even a builtin [hints functionality](http://www.hammerspoon.org/docs/hs.hints.html), but I didn't really like it: the pictures show up in random places on the screen, it's kind of slow, and I can't press escape to escape.





I wrote [my own extension](https://gist.github.com/swo/e75fb44e0c804619a152), which I called _cheaphints_ to get around those problems. You press cmd+alt+E, then just one key to get to your window of choice. Or press escape to escape! Voila.