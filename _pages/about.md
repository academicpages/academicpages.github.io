---
permalink: /
title: ""
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

My background is in Engineering Physics. I studied for my masters at the Lund Institute of 
  Technology from 1991 to 1996, specializing in statistics and applied nuclear physics. I obtained my Ph.D. in Mathematical Statistics from UC. Berkeley 
  in 2001 under the supervision of Professor <a href="https://binyu.stat.berkeley.edu/"> Bin Yu</a>. I was a tenure track assistant professor at the Department of Statistics, Rutgers University 2002-2008 and was 
  promoted to tenure associate professor in 2008. I returned to Sweden in 2009, joining the department of <a href="http://www.chalmers.se/math/EN"> Mathematical Sciences</a>
<br><a href="http://www.gu.se/english/?languageId=100001&contentId=-1&disableRedirect=true&returnUrl=http%3A%2F%2Fwww.gu.se%2F">University of Gothenburg/</a>
<a href="http://www.chalmers.se/en/Pages/default.aspx">Chalmers</a> as an associate professor of mathematical statistics and was 
 subsequently promoted to professor of applied statistics and biostatistics in 2016. <p>
 Since 2018 I serve as 
 <a href="https://science.gu.se/english/about/organisation/steering_group/?languageId=100001&disableRedirect=true&returnUrl=http%3A%2F%2Fscience.gu.se%2Ffakulteten%2FOrganisation%2Fledningsgruppen%2F"> Vice-Dean for Research and Research Infrastructures </a><br>
Faculty of Science, University of Gothenburg
<p>

div id="content">
		<div class="full">

	<h2> What's new? </h2>
&bull; <b>PhD opening in computational statistics with applications to cancer biology</b>  <p> Start date TBA.
<p>
 <!--Two positions are funded through the joint WASP-DDLS call. -->
 This position is funded through the <a href="https://kaw.wallenberg.org/en/research-projects-2022"> Knut and Alice Wallenberg Foundation.
<p>
Project: "The Routes of Glioblastoma and their Patient-Specific Vulnerabilities" </a> is coordinated through
<a  href="http://nelanderlab.org">Sven Nelander's group</a> at Uppsala. This PhD project centers on the development of new matrix- and tensor-imputation methods for 
accelerated drug discovery.  You would be
working closely with researchers in the Nelander lab on an innovative set of experiments that will be conducted to collect information on different
types of invasion. 
<br>
Link to the <a href=""> application system TBA. </a> <p>

======
Like many other Jekyll-based GitHub Pages templates, Academic Pages makes you separate the website's content from its form. The content & metadata of your website are in structured markdown files, while various other files constitute the theme, specifying how to transform that content & metadata into HTML pages. You keep these various markdown (.md), YAML (.yml), HTML, and CSS files in a public GitHub repository. Each time you commit and push an update to the repository, the [GitHub pages](https://pages.github.com/) service creates static HTML pages based on these files, which are hosted on GitHub's servers free of charge.

Many of the features of dynamic content management systems (like Wordpress) can be achieved in this fashion, using a fraction of the computational resources and with far less vulnerability to hacking and DDoSing. You can also modify the theme to your heart's content without touching the content of your site. If you get to a point where you've broken something in Jekyll/HTML/CSS beyond repair, your markdown files describing your talks, publications, etc. are safe. You can rollback the changes or even delete the repository and start over -- just be sure to save the markdown files! Finally, you can also write scripts that process the structured data on the site, such as [this one](https://github.com/academicpages/academicpages.github.io/blob/master/talkmap.ipynb) that analyzes metadata in pages about talks to display [a map of every location you've given a talk](https://academicpages.github.io/talkmap.html).

Getting started
======
1. Register a GitHub account if you don't have one and confirm your e-mail (required!)
2. Fork [this repository](https://github.com/academicpages/academicpages.github.io) by clicking the "fork" button in the top right. 
3. Go to the repository's settings (rightmost item in the tabs that start with "Code", should be below "Unwatch"). Rename the repository "[your GitHub username].github.io", which will also be your website's URL.
4. Set site-wide configuration and create content & metadata (see below -- also see [this set of diffs](http://archive.is/3TPas) showing what files were changed to set up [an example site](https://getorg-testacct.github.io) for a user with the username "getorg-testacct")
5. Upload any files (like PDFs, .zip files, etc.) to the files/ directory. They will appear at https://[your GitHub username].github.io/files/example.pdf.  
6. Check status by going to the repository settings, in the "GitHub pages" section

Site-wide configuration
------
The main configuration file for the site is in the base directory in [_config.yml](https://github.com/academicpages/academicpages.github.io/blob/master/_config.yml), which defines the content in the sidebars and other site-wide features. You will need to replace the default variables with ones about yourself and your site's github repository. The configuration file for the top menu is in [_data/navigation.yml](https://github.com/academicpages/academicpages.github.io/blob/master/_data/navigation.yml). For example, if you don't have a portfolio or blog posts, you can remove those items from that navigation.yml file to remove them from the header. 

Create content & metadata
------
For site content, there is one markdown file for each type of content, which are stored in directories like _publications, _talks, _posts, _teaching, or _pages. For example, each talk is a markdown file in the [_talks directory](https://github.com/academicpages/academicpages.github.io/tree/master/_talks). At the top of each markdown file is structured data in YAML about the talk, which the theme will parse to do lots of cool stuff. The same structured data about a talk is used to generate the list of talks on the [Talks page](https://academicpages.github.io/talks), each [individual page](https://academicpages.github.io/talks/2012-03-01-talk-1) for specific talks, the talks section for the [CV page](https://academicpages.github.io/cv), and the [map of places you've given a talk](https://academicpages.github.io/talkmap.html) (if you run this [python file](https://github.com/academicpages/academicpages.github.io/blob/master/talkmap.py) or [Jupyter notebook](https://github.com/academicpages/academicpages.github.io/blob/master/talkmap.ipynb), which creates the HTML for the map based on the contents of the _talks directory).

**Markdown generator**

I have also created [a set of Jupyter notebooks](https://github.com/academicpages/academicpages.github.io/tree/master/markdown_generator
) that converts a CSV containing structured data about talks or presentations into individual markdown files that will be properly formatted for the Academic Pages template. The sample CSVs in that directory are the ones I used to create my own personal website at stuartgeiger.com. My usual workflow is that I keep a spreadsheet of my publications and talks, then run the code in these notebooks to generate the markdown files, then commit and push them to the GitHub repository.

How to edit your site's GitHub repository
------
Many people use a git client to create files on their local computer and then push them to GitHub's servers. If you are not familiar with git, you can directly edit these configuration and markdown files directly in the github.com interface. Navigate to a file (like [this one](https://github.com/academicpages/academicpages.github.io/blob/master/_talks/2012-03-01-talk-1.md) and click the pencil icon in the top right of the content preview (to the right of the "Raw | Blame | History" buttons). You can delete a file by clicking the trashcan icon to the right of the pencil icon. You can also create new files or upload files by navigating to a directory and clicking the "Create new file" or "Upload files" buttons. 

Example: editing a markdown file for a talk
![Editing a markdown file for a talk](/images/editing-talk.png)

For more info
------
More info about configuring Academic Pages can be found in [the guide](https://academicpages.github.io/markdown/). The [guides for the Minimal Mistakes theme](https://mmistakes.github.io/minimal-mistakes/docs/configuration/) (which this theme was forked from) might also be helpful.
