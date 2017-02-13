---
permalink: /
title: "academicpages is a ready-to-fork GitHub Pages template for academic personal websites"
excerpt: "About me"
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

This is the front page of a generic Github pages website that uses the [academicpages template](https://github.com/academicpages/academicpages.github.io). This template was forked from the [Minimal Mistakes Jekyll Theme](https://mmistakes.github.io/minimal-mistakes/) by Michael Rose, and then extended to support the kinds of content that academics have: publications, talks, teaching, a portfolio, blog posts, and a dynamically-generated CV. You can fork [this repository](https://github.com/academicpages/academicpages.github.io) right now, modify the configuration and markdown files, add your own images and other content, and have your own site for free, with no ads! You can also see [my own personal website](http://stuartgeiger.com), which uses [this Github repository](https://github.com/staeiou/staeiou.github.io).

A data-driven personal website
======
The academicpages template is based on structured data in the [YAML metadata language](http://docs.ansible.com/ansible/YAMLSyntax.html), which is stored various markdown (.md) and .yml files in your own public Github repository. The free [Github pages](https://pages.github.com/) service creates static HTML pages for the entire site based on these files. The HTML pages are automatically rebuilt every time the repository is updated. Many of the features of dynamic content management systems (like Wordpress) can be achieved in this fashion, using a fraction of the computational resources and with far less vulnerability to hacking and DDoSing. 

This approach is also useful because it makes you separate the website's content from its form. The content & metadata of your website are in structured markdown files, while various other files constitute the theme, telling GitHub Pages how to transform that content & metadata into HTML pages. You can modify the theme to your heart's content without touching the content of your site. If you get to a point where you've broken something in Jekyll/HTML/CSS beyond repair, your markdown files with the content & metadata your talks, publications, etc. are safe. You can rollback the changes or even delete the repository and start over-- just be sure to save the markdown files!

Site-wide configuration
------
The main configuration file for the site is in the base directory in [_config.yml](https://github.com/academicpages/academicpages.github.io/blob/master/_config.yml), which defines the content in the sidebars and other site-wide features. The configuration file for the top menu is in the _data directory under [navigation.yml](https://github.com/academicpages/academicpages.github.io/blob/master/_data/navigation.yml).

Data for site content/pages
------
For site content, there is one markdown file for each type of content, which are stored in directories like _talks, _posts, _teaching, or _pages. For example, each talk is a markdown file in the [_talks directory](https://github.com/academicpages/academicpages.github.io/tree/master/_talks). At the top of each markdown file is structured data in YAML about the talk, which the theme will parse to do lots of cool stuff. The same structured about a talk is used to generate the list of talks on the [Talks page](https://academicpages.github.io/talks), each [individual page](https://academicpages.github.io/talks/2012-03-01-talk-1) for specific talks, the talks section for the [CV page](https://academicpages.github.io/cv), and the [map of places you've given a talk](https://academicpages.github.io/talkmap.html) (if you run this [python file](https://github.com/academicpages/academicpages.github.io/blob/master/talkmap.py) or [Jupyter notebook](https://github.com/academicpages/academicpages.github.io/blob/master/talkmap.ipynb), which creates the HTML for the map based on the contents of the _talks directory).

Example: editing a markdown file for a talk
![Editing a markdown file for a talk](/images/editing-talk.png "Editing a markdown file for a talk")

For more info
------
More info about configuring academicpages can be found in [the guide](https://academicpages.github.io/markdown/). The [guides for the Minimal Mistakes theme](https://mmistakes.github.io/minimal-mistakes/docs/configuration/) (which this theme was forked from) might also be helpful.
