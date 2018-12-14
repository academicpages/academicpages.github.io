{% comment %}
---
permalink: /
title: "academicpages is a ready-to-fork GitHub Pages template for academic personal websites"
excerpt: "About me"
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---
{% endcomment %}

Pablo is currently a lecturer in the Department of Civil Engineering at the [University of Concepcion](http://www.ing.udec.cl/Departamento/ingenieria-civil), Chile teaching courses on (1) Optimization, (2) Fundamentals of Transportation Engineering and (3) Transportation Planning. He is also collaborating with research projects at the office of the Centre for Sustainable Urban Development (CEDEUS) in Concepción. Until the first semester of 2018, Pablo was research associate for the Bus Rapid Transit Centre of Excellence (BRT-CoE) and external consultant for the Inter-American Development Bank (IDB). 

<strong>Education<strong>
Pablo completed a B.A in Civil Engineering, a minor in Social Psychology and a MSc in Transportation Engineering at Pontifical Catholic University of Chile (PUC) in 2015. In 2017, he graduated with a MSc in Cognitive and Decision Sciences from University College London (UCL). With his interdisciplinary background, Pablo aims to build bridges between researchers, academics and practitioners from  transportation engineering, behavioral and computer sciences. In his view, an interdisciplinary and data-driven approach is the key to understand human behavior in transportation systems.

<strong>Research experience<strong>
After finishing his MSc at PUC in 2014, Pablo was a research assistant at the office of CEDEUS in Santiago and the Bus Rapid Transit Centre of Excellence (BRT-CoE), Chile. At CEDEUS, he conducted research on fare evasion in public transport and presented this work in various international conferences. During this period, Pablo was the recipient of the Michael Beesley Award for his article Decreasing fare evasion without fines? A microeconomic analysis, which was later published in the journal Research in Transportation Economics. As a result of his master's thesis work, he previously published the article What is behind fare evasion in urban bus systems? An econometric approach in Transport Research Part A: Policy and Practice.​ Pablo has been always interested in the policy implications of his research on fare evasion and thus, he has been actively collaborating in public events and academic workshops held in Santiago, Chile.

<strong>Work experience<strong>
During 2016 Pablo worked for 5 months as a Transport Research Intern at the Ross Center for Sustainable Cities at the World Resources Institute (WRI) in Washington DC. At WRI, he conducted research and data analysis as part of a project with the IDB and the Global Environment Facility (GEF) to promote low carbon technology transfer in Latin America and the Caribbean. He also collaborated with the BRT-CoE in a project aimed at rethinking the next generation of BRT in China. As part of this project, Pablo and researchers from WRI and the China Urban Sustainable Transport Research Center (CUSTReC) coauthored the article Comparing Chinese and Non-Chinese Bus Rapid Transit: Evidence from Evaluation of Global BRT Based on BRT Design Indicators, which was published in the journal Transportation Research Record. This paper was an input for a policy paper led by researchers from WRI where Pablo is also co-author. After finishing his internship, he worked as a external consultant for WRI in a research article studying the relationships between design elements and operational performance in BRTs.

{% comment %}
---
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
More info about configuring academicpages can be found in [the guide](https://academicpages.github.io/markdown/). The [guides for the Minimal Mistakes theme](https://mmistakes.github.io/minimal-mistakes/docs/configuration/) (which this theme was forked from) might also be helpful.
---
{% endcomment %}