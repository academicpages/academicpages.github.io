---
title: "How I built this website"
date: 2020-12-03T22:00:00-00:00
categories:
  - blog
tags:
  - Jekyll
  - update
  - website
  - meta
# canonical_url: "https://d-romero.com/blog/how-i-built-this-website/"
---

This is a very quick walkthrough of how I built this website in an afternoon using the [`Minimal Mistakes template`](https://github.com/mmistakes/minimal-mistakes) for Jekyll. Read this article to learn more!

 I have summarized the steps to the bare minimum you need to get started with your own website. For more detailed/additional information you can always consult the [resources section](#resources) below.

For this project I used a machine running MacOs Catalina. These steps may or may not work depending on your Operating System and version.

## Minimal steps I took:

### I. Install Prerequisites

I installed the [Jekyll prerequisites for MacOs](https://jekyllrb.com/docs/installation/macos/) (reproduced below). You can also look at the official prerequisites documentation [here](https://jekyllrb.com/docs/installation/).

```bash
## Install xcode if you haven't
xcode-select --install

# You will need homebrew
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Use homebrew to install Ruby (you may need to restart your terminal)
brew install ruby

# Add the following line to your .zshrc or your .bash_profile
PATH="/usr/local/opt/ruby/bin:$PATH"

# Relaunch your terminal or source it:
source ~/.zshrc # For Zsh
source ~/.bash_profile # for Bash

```

### II. Install `Jekyll` and `bundler` gems

```bash
gem install --user-install bundler jekyll

## Get your Ruby version:
ruby --version  # You will get something like 2.7.3

# Add the following line to your .zshrc or your .bash_profile
# BUT replace the X.X with the first two digits of your ruby version
PATH="$HOME/.gem/ruby/X.X.0/bin:$PATH" # Example for version 2.7.3: PATH="$HOME/.gem/ruby/2.7.0/bin:$PATH"
```

### III. Create a GitHub repo with the Minimal Mistakes theme starter

3. I clicked on the [Minimal Mistakes](https://github.com/mmistakes/mm-github-pages-starter/generate) theme starter on GitHub as my starting point. I named my repository with my user name `damian-romero` and the suffix `.github.io`. This will:
   - Generate a personal website hosted on GitHub ([GitHub pages](https://jekyllrb.com/docs/github-pages/)) with the contents of your repository as `username.github.io`.
   - Allow you to work and test locally on your computer before you push any changes to your website.
   - The `theme starter repo` that you click on already contains the correctly generated Gemfile that you need to use for GitHub pages, so I did not need to follow the [instructions for using the Minimal Mistakes as a remote theme](https://mmistakes.github.io/minimal-mistakes/docs/quick-start-guide/#remote-theme-method).

\* Note: If you do not have a GitHub account, go to the [resources](#resources) section and follow the link. You will need to learn how to use Git as well. 

### IV. Test your site locally

You can test your site on your computer before you push it to your remote.

```bash
bundle exec jekyll serve

# Go to http://127.0.0.1:4000 on your browser and look at your website
# Press ctrl + c to quit at any time
```

### V. Start adding content

1. In the sub-directory `_pages` you can add any markdown on html pages you want. Then you can display them by adding them to the `_data/navigation.yml` file. For instance, at the top of my page you can see `Home`, `About`, etc. These are [markdown](https://www.markdownguide.org/basic-syntax/) or html files that are listed in `_data/navigation.yml` as below:

```yml
main:
  - title: "Home"
    url: https://d-romero.com/
  - title: "About"
    url: /about/
  - title: "Portfolio"
    url: /portfolio/
  - title: "MCEC"
    url: /mcec_project/
  - title: "News"
    url: /news/
```
2. Play around with your _config.yml file. 
   - The _config.yml file is not loaded dynamically as the other contents of your website so you will need to run `bundle exec jekyll serve` every time you make a change 
   -  Look for inspiration from the full _config.yml file in the Minimal Mistakes GitHub repo: https://github.com/mmistakes/minimal-mistakes/blob/master/_config.yml
3. Add `posts` as markdown files to your `_posts`. Posts have a specific structure. For an example look at my first posts [here](https://github.com/damian-romero/damian-romero.github.io/blob/master/_posts/2020-12-03-welcome.md)
4. Further develop your site. You can follow the Minimal Mistakes customization documentation [here](https://mmistakes.github.io/minimal-mistakes/docs/configuration/).

### VI. Push to remote

Once you are happy with your progress, follow the normal [Git/GitHub steps](https://docs.github.com/en/free-pro-team@latest/github/using-git/git-workflows) to push to remote. **Make sure you are not pushing any confidential information**

```bash
git add -A
git commit -m 'First commit'
git push
```

### VII. Visit your site

```bash
open https://username.github.io # replace 'username' with your user name
```

### VIII. Custom domain

Because I wanted to have my custom domain instead of using `https://damian-romero.github.io`, I did the following (I linked a YouTube video tutorial on how to set up your custom domain in the references section, although it was a bit outdated):

1. I got a [Google domain](http://domains.google.com/) for $12 USD per year.
2. I created a text file inside my repository called `CNAME` (no file extension). The only content in this file is the domain for my website (d-romero.com)
```bash
cd my/repo/directory
touch CNAME
echo d-romero.com >> CNAME
```
3. Once I had my domain, I had to point my site to GitHub:
   - I went to `My domains` on the side bar.
   - I clicked on the domain I wanted to use (I've got several, but for this case I wanted to use d-romero.com)
   - I clicked on the the `DNS` link on the side bar.
   - I scrolled down to `Custom resource records`.
   - I followed the official [GitHub documentation](https://docs.github.com/en/free-pro-team@latest/github/working-with-github-pages/managing-a-custom-domain-for-your-github-pages-site) and created an "A" record with the following IP addresses:
     - 185.199.108.153
     - 185.199.109.153
     - 185.199.110.153
     - 185.199.111.153
   - I created an additional record as such:
     - www   CNAME   1h   damian-romero.github.io

The result looks like this:

![records](/assets/images/custom-resource-records.png)

# IX That is it!

You've made it!

## Resources

- [GitHub](https://github.com/)
- [Git](https://git-scm.com/)
  - [Some git and GitHub resources](https://github.com/damian-romero/gitflow_toy/blob/develop/resources/useful_links.md)
- [Jekyll](https://jekyllrb.com/)
  - [Learn more about GitHub pages and Git](https://docs.github.com/en/free-pro-team@latest/github/working-with-github-pages/setting-up-a-github-pages-site-with-jekyll)
- [Minimal Mistakes](https://mmistakes.github.io/minimal-mistakes/)
  - [Minimal Mistakes Theme Starter repo](https://github.com/mmistakes/mm-github-pages-starter)
- [Custom domain YouTube tutorial](https://youtu.be/nN6QuNqmAwk?t=234)
- [Custom GitHub domain configuration documentation](https://docs.github.com/en/free-pro-team@latest/github/working-with-github-pages/managing-a-custom-domain-for-your-github-pages-site)
- [Configuring a custom domain for your GitHub Pages site](https://docs.github.com/en/free-pro-team@latest/github/working-with-github-pages/configuring-a-custom-domain-for-your-github-pages-site)
- [Learn markdown](https://www.markdownguide.org/basic-syntax/)

You can check out my website repository [here](https://github.com/damian-romero/damian-romero.github.io)

---

Jump higher!

\- Damian
