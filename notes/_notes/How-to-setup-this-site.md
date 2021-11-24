---
title: How to setup this site
tags: Theme
season : summer
---

This is going to be a super simple post about how to setup and use this theme for your own website.

### Setup Prerequisites

For this tutorial, we’ll need to install a few things on your machine (you may have some of these already). Following the instructions on each website to install them.

- [[Ruby::https://www.ruby-lang.org/]]
- [[RubyGems::https://rubygems.org/]]
- [[Git::https://git-scm.com/downloads]]

You’ll also need to create accounts on the following services:

- [[GitHub::https://www.github.com/join]] (to store the website)
- [[Netlify::https://app.netlify.com/signup]] (to serve the website so others can see)

Once you are all set with the prerequisites, we can then get to the fun part of getting it to appear on your screen. Let's get started with that.

### 1. Create a fork of the template repository

To simplify things, I provide the template showed in the image above to get started. You can always tweak this template to your taste later.

Visit the GitHub page for my template repository [[Maxence-L/notenote.link::https://github.com/Maxence-L/notenote.link]], and fork it to your account using the Fork button:

> <img src="/assets/img/fork_button.jpg" style="box-shadow: 2px 2px 20px 0 #ddd;"/>

Once the forking process is complete, you should have a fork (essentially a copy) of my template in your own GitHub account. On the GitHub page for your repository, click on the green “Clone or download” button, and copy the URL: we’ll need it for the next step.

### 2. Clone your repository locally 

Next, we want to download the files from your GitHub repository onto your local machine. To do this, replace <YOUR_COPIED_URL_HERE> in the command below with the URL you copied in the previous step, then execute this command:

```
$ git clone <YOUR_COPIED_URL_HERE> my-personal-website
```

As a reference point, this is how it looks like for me (the difference is likely just the GitHub username):

```
$ git clone git@github.com/Maxence-L/notenote.link my-personal-website
```

Then, navigate into the directory that was just created:

```
$ cd my-personal-website
```

### 3. Test out the site locally

Sweet! You now have your repository’s source code on your machine. Within the my-personal-website directory, run the following command to install the necessary dependencies like Jekyll:

```
$ bundle
```

Once that’s done, ask Jekyll to start serving the site locally:

```
$ bundle exec jekyll serve
```

Then, open up [[http://localhost:4000::http://localhost:4000]] in your browser.

If everything’s done correctly, you should now see the home page of your Personal Jekyll Website with notenote.link Theme. 🎉

Keep in mind that this site is only available locally (notice the `localhost` part of the URL), so if we want it to be available on the Internet for everyone to enjoy, we need to deploy it to the Internet: we’ll use Netlify for that in the next step.

### 4. Connect your GitHub repository to Netlify

Netlify lets you automatically deploy your personal website on to the Internet when you update your GitHub repository. To do this, we need to connect your GitHub repository to Netlify:

1. Log in to Netlify
2. Once logged in, click the “New site from Git” button
3. On the next page, select GitHub as the continuous deployment provider (you may need to authorize the connection, in which case, approve it)
4. On the next page, select your website repository from the list.
5. On the next page, replace the basic build settings with the following.
    1. Type in "jekyll build" (without the quotes) inside the text field titled "Build Command".
    2. Similarly type in "_site/" (without the quotes) inside the text field titled "Publish Directory".
6. On the next page, keep the default settings, and click on “Deploy site”.

That was easy! We’re almost done.

Wait a couple of minutes for the initial deploy to complete.

Once that’s done, your website should be available on the Internet via a generic Netlify URL, which you can change to a custom domain later if you’d like.

Now the cool thing is this: whenever you push an update to your GitHub repository, Netlify will automatically deploy your updates to the Internet.

### 5. Start producing content :

At this point, you can start updating the files on your machine (in the my-personal-website folder) to change your jekyll seamless based website to your liking: update the copy, add some notes, tweak the layout, customize the colors, etc. Once you have something you’re happy with, push your changes to your GitHub repository with the following commands:

```
$ git add --all
$ git commit -m 'Update content'
$ git push origin master
```

If that command succeeds and the rest of the tutorial was done correctly, in a couple of minutes, you should see your changes live on your Netlify website. 🚀

And we’re done! You now have your own notenote.link based Personal Website .

