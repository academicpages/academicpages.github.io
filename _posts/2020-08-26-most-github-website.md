---
title: 'How to Host a Website on Github'
date: 2020-08-26
permalink: /posts/2020/08/host-github-website/
tags:
  - github
---

The purpose of this page is to remind myself how to create a nerdy-ass academic site on Github so I don't have to spend 10 hours re-learning it. Which is what happened this afternoon (boo!). If this tutorial somehow proves to be helpful for other people, that's cool too. Here are all the steps that I have collected from a bunch of Github tutorials (I cited them!! I am not smart enough to come up with this on my own!!), but placed in chronological order.

The best tutorials I've found thus far are the [official Hugo Quick Start tutorial](https://gohugo.io/getting-started/quick-start/) and the post by [Ivy Markwell from Inside the Embassy](https://inside.getambassador.com/creating-and-deploying-your-first-hugo-site-to-github-pages-1e1f496cf88d). So I'm going to combine these two and create a tutorial that's easy enough for me to follow along even if I get amnesia.

## Prerequisites

1. You should have Git 2.8 [installed on your machine](https://git-scm.com/downloads).
2. You should have a [Github](https://github.com) account.

## Step 1: Install Hugo

I play around with the terminal a lot, so I already have [homebrew](https://brew.sh/) installed. But if you do not have homebrew, you should definitely [install homebrew](https://brew.sh/).

After you install homebrew, you can install hugo through homebrew:

`brew install hugo`

You might want to verify that you have the latest version of hugo:

```
hugo version
```

## Step 2: Create a New Site

You can then create your own site.

```
hugo new site hugo_site
cd hugo_site
```

## Step 3: Add your Theme

So you want to create a new git repository:

```
git init
```

Since I'm exhausted from just installing Hugo and learning how to host it on Github, I'm just going to grab a pre-made [Hugo theme](https://themes.gohugo.io/). I decided to use the [hugo-book](https://themes.gohugo.io/hugo-book/) theme.

To use the theme, I went to the theme's github [homepage](https://github.com/alex-shpak/hugo-book), clicked on the green "Clone or download" button, and copied the web URL.

The basic template is, ```git submodule add <theme web URL from github> themes/<theme name>```. So once I fill in the blanks, it looks like this:
```
git submodule add https://github.com/alex-shpak/hugo-book.git themes/hugo-book
```

I then need to copy the ```config.toml``` file into the main hugo_site folder:

```
cp themes/hugo-book/exampleSite/config.toml .
```

## Step 4: Preview Your Site

To check if everything worked out okay, input this into the terminal:

```
hugo server -D
```

The terminal should give you a message telling you that your preview site is being hosted at [http://localhost:1313/](http://localhost:1313/).

Once everything looks okay, you need to ctrl+c to exit the preview mode. Only then will you be able to move on with your life.

## Step 5: Create Repositories

This is the most annoying part, which took me decades to figure out.

Now you log in to your [Github](https://github.com). So basically, when you land on the Github homepage, you should be able to create new repositories. You'll need to create two new repositories. The first one should be where you want your website to live. That is typically ```<your-username>.github.io```. The second is your project repository, which is where the files you edit live. The project repository should be named after your hugo site name, so in this tutorial's case, it's ```hugo_site```.

Your first repository name should be: ```<your-username>.github.io```
Your second repository name should be: ```hugo_site```

Now you have created two repositories.

## Step 6: Sync Your Repository

This pushes everything from the ```hugo_site``` on your computer to the ```hugo_site``` on Github.

```
git remote add origin git@github.com:<your-username>/hugo_site.git
git add .
git commit -m "Initial commit for our Hugo site."
git submodule add git@github.com:<your-username>/<your-username>.github.io.git
git add .
git commit -m "Initial commit for our generated HTML."
git push -u origin master
```

## Step 7: Change Config File

Then you need to open ```config.toml``` need to make sure you output to ```<your-username>.github.io```:

```
baseURL = 'https://<your-username>.github.io'
title = 'Hugo Book'
theme = 'hugo-book'
publishDir = "<your-username>.github.io"
```

## Step 8: Turn Files into HTML

You want to push your site onto ```<your-username>.github.io``` so it shows up in an HTML format. So, you need to type the following into the terminal:

```
hugo
```
Hugo compiles everything for you, so that's kind of nice.

## Step 9: Pre-Deployment Check

You want to make sure your remotes are set up correctly. You insert the following into the terminal:

```
cd marcyshieh.github.io
git remote -v
```

In return, you should get the following, which means everything is okay:

```
> origin git@github.com:<your-username>/<your-username>.github.io.git (fetch)
> origin git@github.com:<your-username>/<your-username>.github.io.git (push)
```

## Step 10: Deploy Everything

Here is the final push:

```
git add .
git commit -m "the final COUNTDOWN"
git push origin master
```

If you go to ```<your-username>.github.io```, you should be able to see your new site. It takes a while! All good things take time!!

But then you realize...you need to customize it.

## Step 11: Editing Your Hugo Site

Most Hugo themes (at least from the ones I've seen) have a folder located at ```themes/hugo-theme/exampleSite/content```. You need to copy the ```content``` folder to the main ```hugo_site``` folder and replace the default ```content``` folder.

Once you replace it, the rest is just some knowledge about Rmarkdown. I'd write more some other time but I am tired from doing this for hours.

Oh, then you do steps 8 to 11 again to make sure your edits actually end up on the live website.