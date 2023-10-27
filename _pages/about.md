---
permalink: /
title: "Andy Stefan: Writer and Science Communicator"
excerpt: "About me"
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

I spend as much time as I can walking in the fields and woods of Canada. The English language often falls short in describing the natural world, but I find great joy in trying to bridge that gap. My two greatest loves are writing and biology, and my writing is the best way that I know how to communicate the wonderous world we live in to as many as people as possible. I want the whole world to know about the softness of milkweed silk, sharp scent of wintergreen, and the marvel of holding a tiny chorus frog in cupped palms.

My experience with science is another asset to my ability to communicate such things. The truth of the world is remarkable, and scientific papers communicate that truth with an efficiency that can seldom be matched. However, something is lost in the data and jargon of science journals. It takes years of practice and training to be able to translate the information found in such papers into something a human can understand. At its best, science is a bridge of understanding, but in our pursuit of efficiency, we have built a wall. I have the training and practice to climb that wall, and I have the skills needed to help people see the world as it truly is and, in doing so, help them to care about the wonderous world we live in.

If you ask someone if they care about “Spilomyia longicornis,” they are likely to say that they do not know what it is. How is anyone meant to care about something they do not know? However, if you tell them about the flies that have no stingers yet appear as remarkable imitations of wasps, they listen. They smile when you tell them about the way it waggles its wings and hold out its forelegs like a pair of long, waspish antennae, as if it is saying “I am a wasp, and you should not eat me!” A connection is made, and instead of an unfamiliar Latin name, suddenly Spilomyia longicornis is something worth caring about. 



Master of Science, knowledge of the scientific method
======
My time in university, and as a member of Tom Sherratt’s research team at Carleton University, have given me excellent insight into how science is conducted and the methods that are used. I have hands-on experience in developing and conducting experiments, analysing data, and writing up results. I’m even quite good at it! This has given me essential skills in interpreting scientific writings and coming to conclusions about the true state of the world. To say that one has “mastered” science makes me laugh, as any expert will tell you that there is always so much more to learn, but I have honed the skills required to view the world through a scientific lens, as well as to understand the words of those who have similar training. It has also given me excellent experience in project management, coding, effective budgeting, and completing all of these tasks in a quick and efficient manner.

Getting started
======
1. Register a GitHub account if you don't have one and confirm your e-mail (required!)
1. Fork [this repository](https://github.com/academicpages/academicpages.github.io) by clicking the "fork" button in the top right. 
1. Go to the repository's settings (rightmost item in the tabs that start with "Code", should be below "Unwatch"). Rename the repository "[your GitHub username].github.io", which will also be your website's URL.
1. Set site-wide configuration and create content & metadata (see below -- also see [this set of diffs](http://archive.is/3TPas) showing what files were changed to set up [an example site](https://getorg-testacct.github.io) for a user with the username "getorg-testacct")
1. Upload any files (like PDFs, .zip files, etc.) to the files/ directory. They will appear at https://[your GitHub username].github.io/files/example.pdf.  
1. Check status by going to the repository settings, in the "GitHub pages" section

Site-wide configuration
------
The main configuration file for the site is in the base directory in [_config.yml](https://github.com/academicpages/academicpages.github.io/blob/master/_config.yml), which defines the content in the sidebars and other site-wide features. You will need to replace the default variables with ones about yourself and your site's github repository. The configuration file for the top menu is in [_data/navigation.yml](https://github.com/academicpages/academicpages.github.io/blob/master/_data/navigation.yml). For example, if you don't have a portfolio or blog posts, you can remove those items from that navigation.yml file to remove them from the header. 

Create content & metadata
------
For site content, there is one markdown file for each type of content, which are stored in directories like _publications, _talks, _posts, _teaching, or _pages. For example, each talk is a markdown file in the [_talks directory](https://github.com/academicpages/academicpages.github.io/tree/master/_talks). At the top of each markdown file is structured data in YAML about the talk, which the theme will parse to do lots of cool stuff. The same structured data about a talk is used to generate the list of talks on the [Talks page](https://academicpages.github.io/talks), each [individual page](https://academicpages.github.io/talks/2012-03-01-talk-1) for specific talks, the talks section for the [CV page](https://academicpages.github.io/cv), and the [map of places you've given a talk](https://academicpages.github.io/talkmap.html) (if you run this [python file](https://github.com/academicpages/academicpages.github.io/blob/master/talkmap.py) or [Jupyter notebook](https://github.com/academicpages/academicpages.github.io/blob/master/talkmap.ipynb), which creates the HTML for the map based on the contents of the _talks directory).

**Markdown generator**

I have also created [a set of Jupyter notebooks](https://github.com/academicpages/academicpages.github.io/tree/master/markdown_generator
) that converts a CSV containing structured data about talks or presentations into individual markdown files that will be properly formatted for the academicpages template. The sample CSVs in that directory are the ones I used to create my own personal website at stuartgeiger.com. My usual workflow is that I keep a spreadsheet of my publications and talks, then run the code in these notebooks to generate the markdown files, then commit and push them to the GitHub repository.

How to edit your site's GitHub repository
------
Many people use a git client to create files on their local computer and then push them to GitHub's servers. If you are not familiar with git, you can directly edit these configuration and markdown files directly in the github.com interface. Navigate to a file (like [this one](https://github.com/academicpages/academicpages.github.io/blob/master/_talks/2012-03-01-talk-1.md) and click the pencil icon in the top right of the content preview (to the right of the "Raw | Blame | History" buttons). You can delete a file by clicking the trashcan icon to the right of the pencil icon. You can also create new files or upload files by navigating to a directory and clicking the "Create new file" or "Upload files" buttons. 

Example: editing a markdown file for a talk
![Editing a markdown file for a talk](/images/editing-talk.png)

For more info
------
More info about configuring academicpages can be found in [the guide](https://academicpages.github.io/markdown/). The [guides for the Minimal Mistakes theme](https://mmistakes.github.io/minimal-mistakes/docs/configuration/) (which this theme was forked from) might also be helpful.
