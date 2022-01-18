---
title: "General tips and tricks"
permalink: /resources/tips
excerpt: ''
font-family: Papyrus
collection: resources
---

# Leveling up with github


- I find that I usually set up a github repository after I've already starting writing some code for a project (or at least already have some documents in a project folder, like data). So I often return to the helpful instructions on how to initialize an existing repository [on the command line](https://kbroman.org/github_tutorial/pages/init.html) and [on GitHub Desktop](https://docs.github.com/en/desktop/contributing-and-collaborating-using-github-desktop/adding-and-cloning-repositories/adding-a-repository-from-your-local-computer-to-github-desktop)
- Add and Commit many small changes (and/or do this frequently) and use really helpful, [informative messages](https://gist.github.com/robertpainsi/b632364184e70900af4ab688decf6f53) about _what you actually did_ in the change using `git add -p; git commit -m "informative message"`. Or type in a longer message in the text editor with just typing `git commit` after you've added your change. In general, add and commit at the same time to make sure the informative messages are linked to specific changes!
- You can set your configuration settings to convert https urls to ssh, allowing for easy and pain-free switching between GitHub Desktop and command-line or CLI github. 
All it takes is one line of code! 
Thanks to [@cmeyerton for sharing the one-liner solution on github forums](https://github.com/desktop/desktop/issues/2085#issuecomment-397016061)
![Screenshot 2022-01-18 175400](https://user-images.githubusercontent.com/6642541/149873449-d93e3ee1-34af-47ae-a2fb-fa2fb5306dcb.png)
