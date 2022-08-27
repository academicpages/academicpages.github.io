---
permalink: /
title: "About Me"
excerpt: "About me"
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---
I am a Ph.D. candidate at Monash University, supervised by [Prof. Shirui Pan](https://shiruipan.github.io/), [Dr. Daokun Zhang](https://research.monash.edu/en/persons/daokun-zhang), and [A/Prof. Vincent Lee](https://research.monash.edu/en/persons/vincent-lee). I obtained my B.S. degree and M.S. degree from Beihang University in 2017 and 2020, respectively. My research interests are in graph representation learning and graph neural networks, with a special focus on unsupervised and weak-supervised scenarios. I am a recipient of the Google Ph.D. Fellowship in 2022.

News
------
* 2022/08: I am honoured to receive the [Google Ph.D. Fellowship](https://research.google/outreach/phd-fellowship) in 2022.
* 2022/05: Our survey on [graph self-supervised learning](https://arxiv.org/pdf/2103.00111.pdf) has been accepted by IEEE TKDE.
* 2022/01: Our paper on [unsupervised graph structure learning](https://arxiv.org/pdf/2201.06367.pdf) has been accepted by WWW 2022.
* 2021/11: Our paper on [dynamic graph anomaly detection](https://arxiv.org/pdf/2106.09876.pdf) has been accepted by IEEE TKDE.
* 2021/10: Our paper on [graph anomaly detection](https://arxiv.org/pdf/2108.09896.pdf) has been accepted by IEEE TKDE.
* 2021/08: Our paper on [graph anomaly detection](https://shiruipan.github.io/publication/cikm-21-jin/cikm-21-jin.pdf) has been accepted by CIKM 2021. 
* 2021/06: Our paper on [label propagation](https://link.springer.com/content/pdf/10.1007/s11280-021-00906-2.pdf) has been accepted by World Wide Web. 
* 2021/03: Our paper on [graph anomaly detection](https://arxiv.org/pdf/2103.00113.pdf) has been accepted by IEEE TNNLS. 

Selected Papers 
------
<style>
td, th {
   font-size: 13px
}
th {
        display: none;
    }
</style>

| | |
|---- | --- |
|<img src="/images/ssl_survey.png" width="400"> | Graph Self-Supervised Learning: A Survey \[[PDF](https://arxiv.org/pdf/2103.00111.pdf)\] <br>**Yixin Liu**, Ming Jin, Shirui Pan, Chuan Zhou, Yu Zheng, Feng Xia, Philip S. Yu. <br>IEEE Transactions on Knowledge and Data Engineering (TKDE), 2022.|
|<img src="/images/sublime.png" width="400"> | Towards Unsupervised Deep Graph Structure Learning \[[PDF](https://arxiv.org/pdf/2201.06367.pdf)\] \[[Code](https://github.com/yixinliu233/SUBLIME)\]<br>**Yixin Liu**, Yu Zheng, Daokun Zhang, Hongxu Chen, Hao Peng, Shirui Pan.<br>The Web Conference (WWW), 2022.|
|<img src="/images/taddy.png" width="400"> | Anomaly Detection in Dynamic Graphs via Transformer \[[PDF](https://arxiv.org/pdf/2106.09876.pdf)\] \[[Code](https://github.com/yixinliu233/TADDY_pytorch)\]<br>**Yixin Liu**, Shirui Pan, Yu Guang Wang, Fei Xiong, Liang Wang, Qingfeng Chen, Vincent CS Lee. <br>IEEE Transactions on Knowledge and Data Engineering (TKDE), 2021.|
|<img src="/images/CoLA.png" width="400"> | Anomaly Detection on Attributed Networks via Contrastive Self-Supervised Learning \[[PDF](https://arxiv.org/pdf/2103.00113.pdf)\] \[[Code](https://github.com/yixinliu233/CoLA)\]<br>**Yixin Liu**, Zhao Li, Shirui Pan, Chen Gong, Chuan Zhou, George Karypis. <br>IEEE Transactions on Neural Networks and Learning Systems (TNNLS), 2021.|

Education 
------
* Ph.D. (2021-present) in Monash University

* M.S. (2017-2020) in Beihang University

* B.S. (2013-2017) in Beihang University

Experience 
------
* **Alibaba Inc.**, Research Intern (advised by [Dr. Zhao Li](https://sites.google.com/view/zhaoli)), 2020.

Contact
------
* Email: yixin.liu\[at\]monash\[dot\]edu

* Office: Level 2, 25 Exhibition Walk, Clayton, VIC 3800


<!--
A data-driven personal website
======
Like many other Jekyll-based GitHub Pages templates, academicpages makes you separate the website's content from its form. The content & metadata of your website are in structured markdown files, while various other files constitute the theme, specifying how to transform that content & metadata into HTML pages. You keep these various markdown (.md), YAML (.yml), HTML, and CSS files in a public GitHub repository. Each time you commit and push an update to the repository, the [GitHub pages](https://pages.github.com/) service creates static HTML pages based on these files, which are hosted on GitHub's servers free of charge.

Many of the features of dynamic content management systems (like Wordpress) can be achieved in this fashion, using a fraction of the computational resources and with far less vulnerability to hacking and DDoSing. You can also modify the theme to your heart's content without touching the content of your site. If you get to a point where you've broken something in Jekyll/HTML/CSS beyond repair, your markdown files describing your talks, publications, etc. are safe. You can rollback the changes or even delete the repository and start over -- just be sure to save the markdown files! Finally, you can also write scripts that process the structured data on the site, such as [this one](https://github.com/academicpages/academicpages.github.io/blob/master/talkmap.ipynb) that analyzes metadata in pages about talks to display [a map of every location you've given a talk](https://academicpages.github.io/talkmap.html).

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
More info about configuring academicpages can be found in [the guide](https://academicpages.github.io/markdown/). The [guides for the Minimal Mistakes theme](https://mmistakes.github.io/minimal-mistakes/docs/configuration/) (which this theme was forked from) might also be helpful. -->
