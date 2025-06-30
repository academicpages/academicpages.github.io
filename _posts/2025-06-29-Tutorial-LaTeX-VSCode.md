---
title: "Tutorial: Use LaTeX Locally with VS Code"
date: 2025-06-29
permalink: /posts/2025/06/LaTeX-VSCode/
tags:
  - tutorial
  - latex
  - vscode
---

This is my take on a quick set up that would allow me to write papers, resumes, or [dazzling "class notes"](https://github.com/junruren/MIT-Classes) using LaTeX **locally* without relying on Internet connectivity. That is, not on [Overleaf](https://www.overleaf.com/), but I can bring my laptop to anywhere and be able to work on my next big ideas...

## Why not Overleaf?

First off, let me praise that [Overleaf](https://www.overleaf.com/) is awesome! It is a very complete product crafted for all the heavy LaTeX writers with many desirable features, a huge library of [templates](https://www.overleaf.com/latex/templates), and a great collection of [LaTeX guides](https://www.overleaf.com/learn).

But it being a cloud-based service means us relying on just Overleaf have the following inconvenience:

### 1. Server down

Just like when occasionally your favorite social media site or streaming site refuses to load, Overleaf is subject to outages. See [Overleaf's status page](https://status.overleaf.com/history) for yourself.

One of my MIT LGO alumni friends mentioned to me that a few years ago, when they were writing their MIT thesis, an Overleaf outage definitely made for some uneasy times.

At the time of writing this blog, the most recent "blockbuster" incident was Overleaf being down on May 14 before the [NeurIPS manuscript deadline](https://x.com/DianboLiu/status/1922544766849257851). See how people reacted under [Overleaf's X post about this outage](https://x.com/overleaf/status/1922576431130759359).

### 2. Difficult to write without internet (e.g., onboard a flight)

Ideas come and go. Who doesn't like the idea of being able to jot them down and immediately see the LaTeX render? Many people seem to be more productive in the air, but are we going to pay for that in-flight Wi-Fi (assuming Wi-Fi is even available onboard)?

This is my attempt at the "WIIFT" of this blog. That said, Overleaf is truly a crucial product in academia and beyond. I like it, but I also want to be immune to risks. So here is how we can de-risk by having a local setup.

---

**Disclaimer:** I am a heavy macOS user, so for the rest of this guide, I will do my best to mention what might be different on Windows. (You use Unix? Ah, this guide _may_ already not be needed for you!) 
{: .notice}

## TLDR

My local setup is: VS Code + the "LaTeX Workshop" extension on VS Code + TeX Live.

This blog is aggressively simplified from the much more thorough [installation guide of the LaTeX Workshop extension](https://github.com/James-Yu/LaTeX-Workshop/wiki/Install). I envisioned this blog to be very light-weight and introductory (i.e., not quite loaded with info that would please "power users") but I will iterate and try to find the right balance with too-basic and too-hardcore. Your feedback is greatly appreciated!

## 1. Install TeX Live

[TeX Live](https://www.tug.org/texlive/) is a LaTeX distribution compatible with and recommended by the LaTeX Workshop extension.

* macOS: https://www.tug.org/mactex/mactex-download.html
* Windows: https://www.tug.org/texlive/windows.html#install

## 2. Install VS Code

Link: https://code.visualstudio.com/download

## 3. LaTeX Workshop Extension for VS Code

Look up the "LaTeX Workshop" extension in your VS Code's Extension Marketplace:

1. Bring up the Extensions view by clicking on the Extensions icon in the Activity Bar on the side of VS Code.
2. In the search bar, type "LaTeX Workshop" and look for the one authored by James Yu.
3. Click "Install"

![Screenshot of LaTeX Workshop shwon in VS Code's Extension Marketplace](/images/2025-06-29-Tutorial-LaTeX-VSCode/LaTeXWorkshop-Extension-VSCode-Screenshot.png)

## 4. Test: Your first locally built PDF

In VS Code, create a new file. I named it `hello.tex` and typed in the following content ([source: Overleaf guide](https://www.overleaf.com/learn/latex/Learn_LaTeX_in_30_minutes#Writing_your_first_piece_of_LaTeX) -- I told you Overleaf is awesome):

```tex
\documentclass{article}
\begin{document}
First document. This is a simple example, with no 
extra parameters or packages included.
\end{document}
```

![Screenshot of a simple tex file created on VS Code before saving](/images/2025-06-29-Tutorial-LaTeX-VSCode/VSCode-First-LaTeX-Before-Build.png)

Then save your file in VS Code:
* macOS: `command` + `S`
* Windows: `Ctrl` + `S`

_I believe_, by default, LaTeX Workshop extension has a convenient feature turned on: that is, whenever you save or even change the `tex` file, compilation of your LaTeX project is triggered. If nothing seems to have happened, try clicking on green triangle icon on the top right corner.

Like anything you'd encounter in the world of developers, LaTeX Workshop extension comes with so many opportunities to be customized. For example, the auto build trigger is available in the extension's setting. ![Screenshot of LaTeX Workshop Setting on Auto Build](/images/2025-06-29-Tutorial-LaTeX-VSCode/LaTeXWorkshop-AutoBuild.png) For simplicity, I will not touch on this topic here.
{: .notice}

Now, you should see something similar to the following screenshot:

![Screenshot of a simple tex file created on VS Code after saving](/images/2025-06-29-Tutorial-LaTeX-VSCode/VSCode-First-LaTeX-After-Build.png)

In the same folder as your `hello.tex`, we can see

* a `hello.pdf` (what we really care the most) and
* a bunch of auxiliary files (again, I will not touch on this topic here.)

You can click on that `hello.pdf` and expect to see exactly what our simple `.tex` file should be rendered into.

A very convenient feature here is to show the PDF file side-by-side with your `.tex` file. Find that green triangle Build button at the top right corner; right next to it is another icon: with a little magnifier over two rectangles; click it.

![Screenshot of the simple tex file with its compiled PDF opened side-by-side](/images/2025-06-29-Tutorial-LaTeX-VSCode/LaTeX-Compiled-PDF-Example.png)

Congratulations, you now should have a "barebone" setup of working on LaTeX documents locally. Convince yourself by disconnecting your computer from the internet, making some random edits to our simple `.tex` file, and saving your changes again.

### Troubleshooting

I came across `LaTeX fatal error on PID undefined. Error: spawn latexmk ENOENT` initially. My solution was simply: restart VS Code.

Please let me know if you encountered any other issues!

---

## Coming soon...

I plan to have a mini-series of blogs on LaTeX specifically in the context of writing a thesis at MIT. In the future, I plan to write about:

* How to use `git` to track our progress and backup with GitHub
* How to use MIT thesis template with this local setup

Meanwhile, please let me know if you have any suggestions for this tutorial or future topics.