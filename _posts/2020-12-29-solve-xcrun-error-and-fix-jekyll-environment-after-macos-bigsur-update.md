---
title: "Solve macOS BigSur 'xcrun: error' and fix Jekyll/Homebrew environment issues after update"
date: 2020-12-29T22:00:00-00:00
categories:
  - blog
tags:
  - Jekyll
  - Homebrew
  - update
  - website
  - meta
  - macOS BigSur
  - xcrun error
# canonical_url: "https://d-romero.com/welcome"
excerpt: "Here is how I fixed my Jekyll (and Homebrew) environments on macOS BigSur and some tips on what to do before updating your Operating System."
header:
  overlay_image: "assets/images/bug-fix.png"
  og_image: "assets/images/website-preview-squared.png"
  caption: "Photo credit: [**AltumCode on Unsplash**](https://unsplash.com/@altumcode?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText)"
---

*If you only want the solution of the issue at hand, I suggest skipping to the ["Full fix"](#full-fix) section.*

## Background and some tips on updating your operating system

When a new version of an operating system comes out, I usually don't install it right away unless it's absolutely necessary. So when Apple rolled out its latest macOS (BigSur) back in November 2020, I decided to wait, especially since the University of Arizona warned its employees that there might be some compatibility issues regarding [Sophos security software](https://www.sophos.com/) (which I use).

However, it is finally winter break, and it was time to update to the newest OS. I knew I would have to fix several things in my development environment, so I **backed up my computer to an external drive** just in case I needed to revert to my previous OS for any reason. 

When I finally updated to BigSur, I was happy that I delayed my update because Sophos, Anaconda, and Git were all working correctly. However, I wanted to add some content to my website, and that is where I hit the jackpot. The command `bundle exec jekyll serve` was not working. Here is what happened and how I was able to solve the issue:

## Full fix

After updating to BigSur, I wanted to add content to my website, so I went through the usual steps:

```bash
bundle exec jekyll serve
```

This resulted in the following error:

```
Could not find concurrent-ruby-1.1.7 in any of the sources
Run `bundle install` to install missing gems.
```

Just running `bundle install` will throw a permission error, so I ran it with sudo:

```
sudo bundle install
```

But this failed again with:

```
An error occurred while installing json (2.3.1), and Bundler cannot continue.
Make sure that `gem install json -v '2.3.1' --source 'https://rubygems.org/'` succeeds before bundling
```

However, running `gem install json -v '2.3.1' --source 'https://rubygems.org/` also failed, prompting me to `install ruby-dev` or `ruby-devel`, so I tried to update brew first and see what happened:

```bash
brew update
```

Sure enough, I got to the root of the problem when I hit a `missing xcrun` error: 

```
invalid active developer path (/Library/Developer/CommandLineTools), missing xcrun at: /Library/Developer/CommandLineTools/usr/bin/xcrun
```

[Googling around](https://dev.to/o9uzdev/macos-xcrun-error-invalid-active-developer-path-missing-xcrun-411a), it turned out that the issue could be solved simply by re-installing xcode (step 1 in the [Jekyll documentation pre-requisites](https://jekyllrb.com/docs/installation/macos/))

```bash
xcode-select --install
```

Later, I found out that I needed to make one small change to my `.gitignore` file. I needed to add [the full `/vendor/` directory](https://jekyllrb.com/tutorials/using-jekyll-with-bundler/) as opposed to just the `/vendor/bundle` which was sufficient in macOs Catalina:

```diff
diff --git a/.gitignore b/.gitignore
index 7d3f845..68a8ee8 100644
--- a/.gitignore
+++ b/.gitignore
@@ -77,6 +77,7 @@ build-iPhoneSimulator/
 
 ## Environment normalization:
 /.bundle/
+/vendor/
 /vendor/bundle
 /lib/bundler/man/
```

Now you can just run `bundle install` (no sudo!) and this will get the correct configuration for your project.

```bash
bundle install
bundle exec jekyll serve
```

**Note that you do not need to install the `ruby-dev` or `ruby-devel` environments.**

 Also, as a side-effect, your `Homebrew` environment is also fixed.

```bash
brew update
# works
```

## Takeaways 

When updating to a new OS, I will minimally follow the checklist below:

- Get information about the new release.
  - Pay attention to what the developers of your most frequently used tools say about a new big release. In my case these are:
    - Python, Anaconda, Homebrew, Git & GitHub, my antivirus software, among others
  - (Re)read all IT team's emails regarding the subject.
  - Search the internet for possible issues of switching too quickly.
- If possible, allow 3-6 months before installing a big release.
  - For security reasons, smaller releases should almost always be installed asap, except when there is a known security issue.
- Make sure I have enough time to back up and solve any issues that might come up during or after the process.
- Back up my computer right before updating my OS (apart from my weekly backup).
- Once I have completed my backup and before working on anything else, i will check that my most essential tools are working correctly.

## That's it!

I hope this is useful for people trying to fix their Jekyll environments.

Special thanks to [o9uz.dev](https://dev.to/o9uzdev) for [this post](https://dev.to/o9uzdev/macos-xcrun-error-invalid-active-developer-path-missing-xcrun-411a) in dev.to and to Ernest Ojeh for [this post](https://ernestojeh.com/fix-jekyll-on-macos-big-sur) pre-[2.60 homebrew](https://brew.sh/2020/12/01/homebrew-2.6.0/), and of course to all the folks at Apple and Homebrew. So far I am enjoying my BigSur experience.

And remember to... 

Jump higher!

\- Damian

<p>
  <img alt="Visitors" src="https://visitor-badge.glitch.me/badge?page_id=damian-romero/damian-romero.github.io/blob/master/_posts/2020-12-29-solve-xcrun-error-and-fix-jekyll-environment-after-macos-bigsur-update.md" />
</p>
