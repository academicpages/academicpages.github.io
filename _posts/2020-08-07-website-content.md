---
title: 'Adding Content to an Academic Website'
date: 2020-08-07
permalink: /posts/2020/08/website-content/
excerpt_separator: <!--more-->
toc: trueheader: 
  og_image: "posts/website-content/preview.png"
tags:
  - website
  - git
  - github
  - bash
---

One thing I haven't covered in my previous posts on [creating]({{ site.baseurl }}{% post_url 2020-06-30-academic-website %}) and [customizing]({{ site.baseurl }}{% post_url 2020-07-6-customizing-website %}) an academic website is how to actually add content to your site. You know, the stuff that's the reason why people go to your website in the first place? If you've followed those guides, your website should be professional looking and already feeling a little bit different from the stock template. However, adding new pages or tweaking the existing pages can be a little intimidating, and I realized I should probably walk through how to do so. Luckily Jekyll's use of Markdown makes it really easy to add new content!

<!--more-->

# #Content

Editing the welcome page for your site (`_pages/about.md`) is relatively straightforward. Things get a little trickier if you want to build an entirely new page to your website. You'll notice that I have a [software](/software) page on my site that isn't part of the [academicpages](https://academicpages.github.io/) template. I'll use that page as a running example to walk you through adding a new page to your site.

## First steps

First things first, we need to create a file for the page itself. The main pages for your website are generated from [Markdown](https://en.wikipedia.org/wiki/Markdown) files contained in the `_pages` directory. Create a new file called `software.md` in `_pages`. Now, open it up in RStudio or your text editor of choice. If you've looked at the `.md` files for other pages, you'll notice that they all start with a similar block of text. This is a [YAML](https://en.wikipedia.org/wiki/YAML) header that tells Jekyll the basic information needed to build the page. There are lots of different options you can include, but the only two you really need are the `permalink` for the page and its `title`. Add the following to the top of `software.md`:

```yaml
---
permalink: /software/
title: "Software"
---
```

Anything after that second line of dashes will be translated into actual content on the page.

## Fill it out

Now we need to make our new page actually say something. My software page lists the R packages I've contributed to and includes links to miscellaneous other bits of code like functions for working with video data in Python or the LaTeX template I used for my dissertation. You can check out the `.md` source file for my software page on my [GitHub](https://raw.githubusercontent.com/jayrobwilliams/jayrobwilliams.github.io/master/_pages/software.md).

A couple of things to notice:

- You can create headings using pound signs
  - More pound signs produce smaller headings
- You can create links using standard Markdown syntax, e.g., `[link text](url)`
  - If you're linking to a page generated from a source `.md` file in `_pages`, just put a slash before the page name and don't include any extension, e.g., `[software](/software)`
- You can embed images by adding an exclamation point before the opening `[` in Markdown link syntax, e.g., `![](/images/profile.png)`
- You can create code blocks like the ones on this page by enclosing text in triple backticks
  - Put the name of the programming language after the opening backticks to activate [syntax highlighting](https://en.wikipedia.org/wiki/Syntax_highlighting)
- You can also embed raw HTML directly like I used to include three images next to one another

These tools should be sufficient to let you build an awesome new page for your website. However, letting visitors actually get to your new page requires a little more work.

## You can't get there from here

If you want to just add a link to your new page from an existing page, like the homepage, that's easy and can be accomplished by adding a link to the Markdown source in `_pages/about.md`. That's how I added my [teaching materials](/teaching-materials) page; it's just a link on my [teaching](/teaching) page. But what about if you want your new page to be easily accessed from the fancy navigation bar at the top of the site?

To do that, we'll need to edit the files Jekyll uses to control navigation on the site. Open up `_data/navigation.yml` and get ready to add our new page to the to menu. This is what it looks like in the template:

```yaml
# main links links
main:
  - title: "Publications"
    url: /publications/

  - title: "Talks"
    url: /talks/    

  - title: "Teaching"
    url: /teaching/    
    
  - title: "Portfolio"
    url: /portfolio/
        
  - title: "Blog Posts"
    url: /year-archive/
    
  - title: "CV"
    url: /cv/
    
  - title: "Guide"
    url: /markdown/
```

The order that items appear in top-to-bottom in this file is also the order they'll appear in left-to-right in the navigation bar. So decide where you want your new page to go, and slot it in. This is what `_data/navigation.yml` looks like for my website:

```yaml
# main links links
main:
  - title: "Publications"
    url: /publications/
    
  - title: "Research"
    url: /research/

  - title: "Teaching"
    url: /teaching/

  - title: "Software"
    url: /software/

  - title: "Posts"
    url: /posts/
    
  - title: "CV"
    url: /cv/
```

Again, you can check out the current version of this file for my site at my [GitHub](https://github.com/jayrobwilliams/jayrobwilliams.github.io/blob/master/_data/navigation.yml) if you want. If I've changed anything in the navigation menu since I wrote this post, those changes will be reflected there.

You'll also notice that the Guide link is no longer there in my `_data/navigation.yml`. Removing elements from this file drops them from the navigation menu, so if there are any other pages in the template you don't plan to use, go ahead and remove them now.

Once you're happy with your new page, it's time to tell git about them, and then upload them to GitHub. You can do this with

```bash
git add _pages/software.md _data/navigation.yml
git commit -m "add software page"
git push
```

If you followed the guide on [uploading changes to GitHub]({{ site.baseurl }}{% post_url 2020-06-30-academic-website %}#uploading-changes-to-github) in my post on [making an academic website]({{ site.baseurl }}{% post_url 2020-06-30-academic-website %}), all of the above code should run smoothly and in a few minutes you'll have a new page on your website.

# Uploading files

One of the advantages of using GitHub pages to host your website is that you don't have to use Dropbox to host PDFs of your working papers and published articles, not to mention your CV. If you use Wix or WordPress, you may have to upload your files to Dropbox, and then link to them on your site. This process has three major downsides:

1. You have to update your website in two places to add or update a PDF
2. Google Scholar will ignore Dropbox links, so you won't get a record of your scholarship online
3. If someone clicks a Dropbox while viewing your site on their phone or tablet, it may take them to the Dropbox app or pop up a message about the app not being installed

All of these are less than ideal. Luckily, GitHub Pages has the capability to address all three already built in. When you make an update to your website and `git push` it to GitHub, *all* tracked files get uploaded with it. This means it's super easy to upload your PDFs to your site and link directly to them. I'll walk through how to do this with an example PDF called `working-paper.pdf`.

First, copy the PDF into the `files/pdf` directory in your site's directory. Next we need to tell git about this file, which we do with

```bash
git add files/pdf/working-paper.pdf
git commit -m "add working paper"
git push
```

Don't forget to add a link to the paper somewhere on your research page so that visitors can access it. Here's an example of what that link might look like: `[Working Paper](/files/pdf/working-paper.pdf)`. And if you want to use the [fancy button]({{ site.baseurl }}{% post_url 2020-07-6-customizing-website %}#pushing-buttons) from my post on [customizing your site]({{ site.baseurl }}{% post_url 2020-07-6-customizing-website %}), you would do this: `[Working Paper](/files/pdf/working-paper.pdf){: .btn--research}`.

# Designing for mobile
 
One of the advantages of the [academicpages](https://academicpages.github.io/) template is that it is [responsive](https://en.wikipedia.org/wiki/Responsive_web_design), meaning that layouts change automatically with screen size to present content in the most efficient manner. Take a look at my website on your phone to see how a smaller device changes the site's layout. When you're editing your website, it's a good idea to periodically check how it appears on a phone, as it's likely that a number of visitors to your site will view it on their phones.[^1]

To do so, you can use tools like Chrome's [device mode](https://developers.google.com/web/tools/chrome-devtools/device-mode), but this can be annoying and doesn't perfectly capture the experience of navigating your site on a small touchscreen. The best way to do that is, unsurprisingly, to use your actual phone. However, this requires a slight tweak to our usual `bundle exec jekyll serve` command. We need to add a `--host` argument to the command, where the value of the argument is our computer's IP address. There are many ways to look this up, but here are two quick ones you can execute from the terminal:

- On MacOS: `ifconfig en0 | grep inet | grep -v inet6 | awk '{print $2}'`
- On Linux: `hostname -I`

What each of these will do is capture the *local* IP address of the computer. Often this will be something like `192.168.1.x` or `10.0.0.x`. This won't let you access the site from outside your network over the internet, but it *will* let you access it locally on your own network. Once you've found your local IP address, you can serve your site on your local network, letting you view it on your phone or tablet. For example, my IP address is `192.168.1.6`, so putting it all together I get:

```bash
bundle exec jekyll serve --host 192.168.1.6
```

This is quite a lot to type, and your computer's local IP address can change occasionally, so you can't just keep putting in the same IP address each time. To save yourself some time by creating an [alias](https://en.wikipedia.org/wiki/Alias_(command)) for the command. An alias is simply a way to refer to a longer command with a shorter label. To do this, you'll need to edit your `.bash_profile` configuration file.[^2] The easiest way to do this is to run

```bash
nano ~/.bash_profile
```

This will open up your `.bash_profile` in [nano](https://en.wikipedia.org/wiki/GNU_nano), a simple text editor.[^3] I've decided to call my aliased command `serve-site`, but you could call it anything you want. Scroll down to the end of the file and add either

```bash
alias serve-site="bundle exec jekyll serve --host=$(ifconfig en0 | grep inet | grep -v inet6 | awk '{print $2}')"
```

for MacOS or

```bash
alias serve-site="bundle exec jekyll serve --host=$(hostname -I)"
```

for Linux. Once you've added this line, save the file by pressing <kbd>ctrl</kbd>+<kbd>o</kbd> and then <kbd>enter</kbd> to use the existing filename, overwriting the old version of `.bash_profile`. Then press <kbd>ctrl</kbd>+<kbd>x</kbd> to close nano. The last step is to tell your terminal about this new alias. You can accomplish this with

```bash
source ~/.bash_profile
```

regardless of whether you're on Linux or MacOS. Now whenever you want to check out your website on a mobile device, you can just navigate to your website's directory and use the new `serve-site` alias to launch it locally.

## Windows

If you're trying to figure out how to do this on Windows, I haven't forgotten about you, I just have no idea how to do this on Windows ¯\\\_(ツ)\_/¯. My recommendation would be to do a lot of googling, or to install the [Windows Subsystem for Linux](https://en.wikipedia.org/wiki/Windows_Subsystem_for_Linux), which will allow you to use a bash shell to interact with your files.

[^1]: As a senior faculty member once pointed out to me, the search committee member who didn't fully read your application is most likely to pull up your website on their phone during a committee meeting.

[^2]: I'm assuming that you're using bash as your shell. If you're using a different shell, see [this list](https://kb.iu.edu/d/abdy) for which configuration files you should be editing. Other shells may also define aliases in different ways.

[^3]: Feel free to use a different editor or use the `edit` command if you've set the default editor to your preferred editor.