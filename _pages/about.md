---
permalink: /
title: "About"
excerpt: "About me"
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

This is the front page of your Github pages website, using the [academicpages Jekyll theme](https://github.com/academicpages/academicpages.github.io). This repository was forked from the [Minimal Mistakes Jekyll Theme](https://mmistakes.github.io/minimal-mistakes/) by Michael Rose, and extended to support the kinds of content that academics have: publications, talks, teaching, a portfolio, blog posts, and a dynamically-generated CV. You can fork [this repository]((https://github.com/academicpages/academicpages.github.io)) right now, modify the configuration and markdown files, add your own images and other content, and have your own site for free!

A data-driven personal website
======
The academicpages Jekyll theme is entirely based on structured data in the [YAML metadata language](http://docs.ansible.com/ansible/YAMLSyntax.html), which is stored various markdown and .yml files. The free Github pages service creates static HTML pages for the entire site based on these files. The HTML pages are rebuilt every time the repository is updated. Many of the features of dynamic content management systems (like Wordpress) can be achieved in this fashion, using a fraction of the computational resources and with far less vulnerability to hacking and DDoSing. 

Site-wide configuration
------
The main configuration file for the site is in the base directory in [_config.yml](https://github.com/academicpages/academicpages.github.io/blob/master/_config.yml), which defines the content in the sidebars and other site-wide features. The configuration file for the top menu is in the _data directory under [navigation.yml](https://github.com/academicpages/academicpages.github.io/blob/master/_data/navigation.yml).

Data for site content/pages
------
For site content, there is one markdown file for each type of content, which are stored in directories like _talks, _posts, _teaching, or _pages. Each markdown file with metadata for various variables stored in YAML sections at the top. For example, each talk is a markdown file in the [_talks directory](https://github.com/academicpages/academicpages.github.io/tree/master/_talks). At the top of each markdown file is structured data about the talk, which the theme will parse to do lots of cool stuff. The same structured about a talk is used to generate the list of talks on the [Talks page](https://academicpages.github.io/talks), each [individual page](https://academicpages.github.io/talks/2012-03-01-talk-1) for specific talks, the talks section for the [CV page](https://academicpages.github.io/cv), and the [map of places you've given a talk](https://academicpages.github.io/talkmap.html) (if you run this python file or Jupyter notebook).

Example: editing a markdown file for a talk
![Editing a markdown file for a talk](/images/editing-talk.png "Editing a markdown file for a talk")

