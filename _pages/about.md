---
permalink: /
<<<<<<< HEAD
title: ""
excerpt: "About me"
=======
title: "Academic Pages is a ready-to-fork GitHub Pages template for academic personal websites"
>>>>>>> 1acca92e64c8e345fdda983aca94f1ce0bbd3447
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

<<<<<<< HEAD
=======
This is the front page of a website that is powered by the [Academic Pages template](https://github.com/academicpages/academicpages.github.io) and hosted on GitHub pages. [GitHub pages](https://pages.github.com) is a free service in which websites are built and hosted from code and data stored in a GitHub repository, automatically updating when a new commit is made to the repository. This template was forked from the [Minimal Mistakes Jekyll Theme](https://mmistakes.github.io/minimal-mistakes/) created by Michael Rose, and then extended to support the kinds of content that academics have: publications, talks, teaching, a portfolio, blog posts, and a dynamically-generated CV. You can fork [this template](https://github.com/academicpages/academicpages.github.io) right now, modify the configuration and markdown files, add your own PDFs and other content, and have your own site for free, with no ads!
>>>>>>> 1acca92e64c8e345fdda983aca94f1ce0bbd3447

About me
======
<<<<<<< HEAD

I’m an Assistant Professor in Sociology at the Universidad Católica de Chile. Previously, I was a Max Weber Postdoctoral Fellow at the European University Institute and earned a Ph.D. in Sociology at Cornell University. I study labor market inequalities, intergenerational mobility and beliefs about inequality using a combination of statistical modeling, empirical strategies for causal inference, experimental and computational methods.
=======
Like many other Jekyll-based GitHub Pages templates, Academic Pages makes you separate the website's content from its form. The content & metadata of your website are in structured markdown files, while various other files constitute the theme, specifying how to transform that content & metadata into HTML pages. You keep these various markdown (.md), YAML (.yml), HTML, and CSS files in a public GitHub repository. Each time you commit and push an update to the repository, the [GitHub pages](https://pages.github.com/) service creates static HTML pages based on these files, which are hosted on GitHub's servers free of charge.

Many of the features of dynamic content management systems (like Wordpress) can be achieved in this fashion, using a fraction of the computational resources and with far less vulnerability to hacking and DDoSing. You can also modify the theme to your heart's content without touching the content of your site. If you get to a point where you've broken something in Jekyll/HTML/CSS beyond repair, your markdown files describing your talks, publications, etc. are safe. You can rollback the changes or even delete the repository and start over - just be sure to save the markdown files! Finally, you can also write scripts that process the structured data on the site, such as [this one](https://github.com/academicpages/academicpages.github.io/blob/master/talkmap.ipynb) that analyzes metadata in pages about talks to display [a map of every location you've given a talk](https://academicpages.github.io/talkmap.html).
>>>>>>> 1acca92e64c8e345fdda983aca94f1ce0bbd3447

Research
======
<<<<<<< HEAD
=======
1. Register a GitHub account if you don't have one and confirm your e-mail (required!)
1. Fork [this template](https://github.com/academicpages/academicpages.github.io) by clicking the "Use this template" button in the top right. 
1. Go to the repository's settings (rightmost item in the tabs that start with "Code", should be below "Unwatch"). Rename the repository "[your GitHub username].github.io", which will also be your website's URL.
1. Set site-wide configuration and create content & metadata (see below -- also see [this set of diffs](http://archive.is/3TPas) showing what files were changed to set up [an example site](https://getorg-testacct.github.io) for a user with the username "getorg-testacct")
1. Upload any files (like PDFs, .zip files, etc.) to the files/ directory. They will appear at https://[your GitHub username].github.io/files/example.pdf.  
1. Check status by going to the repository settings, in the "GitHub pages" section
>>>>>>> 1acca92e64c8e345fdda983aca94f1ce0bbd3447

My scholarly agenda is articulated around two core, complementary research streams. One series of projects examines key structural aspects of social inequality - intergenerational income mobility, gender- and race-based gaps in the labor market and educational assortative mating. Another line of research focuses on the cultural facets of social stratification as they crystallize in specific belief systems about inequalities and fairness. My work has been published in academic journals such as *Science Advances*, *Sociological Science*, *Sociological Methods and Research*, *RSF: The Russell Sage Foundation Journal of the Social Sciences*, *Socius*, and *Research in Social Stratification and Mobility*, and covered by popular media outlets such and the *New York Times*, *Washington Post*, *New Scientist*, *Science Daily*, among others.

I am currently the principal investigator for the Fondecyt Iniciación project, *'Inequality of Outcomes and Opportunity and Its Effects on the Legitimacy of Inequality and Social Cohesion,'* as well as for the [Millennium Nucleus for the Study of Labor Market Mismatch, Causes, and Consequences](https://www.lm2c2.cl/en/). In collaboration with my colleagues [Andrea Canales](https://scholar.google.com/citations?user=XDUh9coAAAAJ&hl=en) and [Tania Hutt](https://www.taniahutt.com/), I co-organize the ongoing [Workshop on Inequality and Stratification Research](https://github.com/mebucca/workshop_ineq) and the [Quantitative and Computational Social Science Research Group](https://github.com/mebucca/qCs2).


<<<<<<< HEAD
Methods
======

In tandem with my substantive research agenda, I have implemented novel statistical tools such as Bayesian models with structured dispersion for the study of sibling correlations, Lasso regularization for selection of log-linear models, micro-simulations for the study of educational assortative mating, and online large-scale experiments to study beliefs about inequality. 
=======
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
>>>>>>> 1acca92e64c8e345fdda983aca94f1ce0bbd3447
