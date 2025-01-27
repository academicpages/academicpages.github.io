---
permalink: /
title: "Academic Pages is a ready-to-fork GitHub Pages template for academic personal websites"
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---
Welcome to Fang Gong's Website欢迎来到我的个人网站
======
About Me
======
Hi, I'm Fang Gong. I recieved my Ph.D. degree in Control Science and Engineering from China University of Geosciences (CUG-Wuhan) in Dec 2022, supervised by prof. [Liangxiao Jiang](https://grzy.cug.edu.cn/jlx/zh_CN/). Currently, I'm a lecturer in School of Computer Science at Wuhan Institute of Technology. From Dec 2019 to Dec 2020, I visited at the Schulich School of Engineering Intelligent Geospatial Data Mining Lab in Department of Geomatics at University of Calgary, supervised by prof.[Xin Wang](https://profiles.ucalgary.ca/xin-wang). 

Research Interest
======
Currently, I am broadly interested in data mining and machine learning.

In particular, the goal is to develop machine learning-based algorithms for categorical data analysis, e.g., distance metric and representation learning. The difficulties in categorical data analysis is, but not limited to, how to represent the complex coupling relationships, how to handle the concept shift, and how to handle the imbalance data, which bring in the consiferable challanges. We wish to develop the effective and efficient methods about structure extension, multi-view learning, dynamic ensemble learning, few-shot learning to tackle these challenges. 

Selected Publication
======
1. Fine-grained attribute weighted inverted specific-class distance measure for nominal attributes
   Fang Gong, Xin wang, Liangxiao Jiang, Seyyed Mohammadreza Rahimi, Dianhong Wang
   Information Sciences, 2021, 578: 848–869[Link](https://doi.org/10.1016/j.ins.2021.08.041)
2. Gain ratio weighted inverted specific-class distance measure for nominal attributes
   Fang Gong, Liangxiao Jiang, Huan Zhang, Dianhong Wang, Xingfeng Guo
   International Journal of Machine Learning and Cybernetics, 2020, 11: 2237–2246[Link](https://doi.org/10.1007/s13042-020-01112-8)
3. Using differential evolution for an attribute-weighted inverted specific-class distance measure for nominal attributes.
   Fang Gong, Xingfeng Guo, Dianhong Wang
   Data Mining and Knowledge Discovery, 2023, 37: 409–433[Link](https://doi.org/10.1007/s10618-022-00881-w)
4. Averaged one dependence inverted specific class distance measure for nominal attributes
   Fang Gong, Liangxiao Jiang, Dianhong Wang, Xingfeng Guo
   Journal of Experimental & Theoretical Artificial Intelligence, 2019, 32(4): 651–663[Link](https://doi.org/10.1080/0952813X.2019.1661587)

Many of the features of dynamic content management systems (like Wordpress) can be achieved in this fashion, using a fraction of the computational resources and with far less vulnerability to hacking and DDoSing. You can also modify the theme to your heart's content without touching the content of your site. If you get to a point where you've broken something in Jekyll/HTML/CSS beyond repair, your markdown files describing your talks, publications, etc. are safe. You can rollback the changes or even delete the repository and start over - just be sure to save the markdown files! Finally, you can also write scripts that process the structured data on the site, such as [this one](https://github.com/academicpages/academicpages.github.io/blob/master/talkmap.ipynb) that analyzes metadata in pages about talks to display [a map of every location you've given a talk](https://academicpages.github.io/talkmap.html).

Getting started
======
1. Register a GitHub account if you don't have one and confirm your e-mail (required!)
1. Fork [this template](https://github.com/academicpages/academicpages.github.io) by clicking the "Use this template" button in the top right. 
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

The repository includes [a set of Jupyter notebooks](https://github.com/academicpages/academicpages.github.io/tree/master/markdown_generator
) that converts a CSV containing structured data about talks or presentations into individual markdown files that will be properly formatted for the Academic Pages template. The sample CSVs in that directory are the ones I used to create my own personal website at stuartgeiger.com. My usual workflow is that I keep a spreadsheet of my publications and talks, then run the code in these notebooks to generate the markdown files, then commit and push them to the GitHub repository.

How to edit your site's GitHub repository
------
Many people use a git client to create files on their local computer and then push them to GitHub's servers. If you are not familiar with git, you can directly edit these configuration and markdown files directly in the github.com interface. Navigate to a file (like [this one](https://github.com/academicpages/academicpages.github.io/blob/master/_talks/2012-03-01-talk-1.md) and click the pencil icon in the top right of the content preview (to the right of the "Raw | Blame | History" buttons). You can delete a file by clicking the trashcan icon to the right of the pencil icon. You can also create new files or upload files by navigating to a directory and clicking the "Create new file" or "Upload files" buttons. 

Example: editing a markdown file for a talk
![Editing a markdown file for a talk](/images/editing-talk.png)

For more info
------
More info about configuring Academic Pages can be found in [the guide](https://academicpages.github.io/markdown/), the [growing wiki](https://github.com/academicpages/academicpages.github.io/wiki), and you can always [ask a question on GitHub](https://github.com/academicpages/academicpages.github.io/discussions). The [guides for the Minimal Mistakes theme](https://mmistakes.github.io/minimal-mistakes/docs/configuration/) (which this theme was forked from) might also be helpful.
