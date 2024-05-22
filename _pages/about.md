---
hide:
- permalink: /
- title: "Yufan Kang"
- author_profile: true
- redirect_from: 
  - /about/
  - /about.html
---

I'm currently a PhD Student from the School of Computing Technologies at RMIT University under the supervision of Prof. Jeffrey Chan and Prof. Flora D. Salim. I'm also a student member of [Australian Research Council (ARC) Centre of Excellence for Automated Decision-Making and Society (ADM+S)](https://www.admscentre.org.au). I started her PhD in 2021 and expected to finish in 2025, and I mainly work in the direction of Responsible AI in Spatial-Temporal Data Mining.

Before starting my PhD degree, I completed my Honours degree in Computer Science in the direction of Pervasive Mobile Computing, and I was a research intern in Microsoft Cortana Intelligence Institute after my Honours degree. Before that, I completed my Bachelor degree in the University of Melbourne in major of both Discrete Mathematics and Statistics and Computer Science. 

Selected Publications
======
- Shao, Wei*, Yufan Kang*, Ziyan Peng, Xiao Xiao, Lei Wang, Yuhui Yang, Flora D. Salim, Spatio-temporal Early Prediction based on Multi-objective Reinforcement Learning. Proceedings of the 29th ACM SIGKDD Conference on Knowledge Discovery and Data Mining. 2024.
- Kang, Yufan, Rongsheng Zhang, Wei Shao, Flora D. Salim, and Jeffrey Chan, 2024, July. Promoting Two-sided Fairness in Dynamic Vehicle Routing Problems. In Proceedings of the Genetic and Evolutionary Computation Conference. 
- Shao, Wei*, Ziyan Peng*, Yufan Kang*, Xiao Xiao, and Zhiling Jin. [Early Spatiotemporal Event Prediction via Adaptive Controller and Spatiotemporal Embedding](https://ieeexplore.ieee.org/abstract/document/10415705). In 2023 IEEE International Conference on Data Mining (ICDM), pp. 1307-1312. IEEE, 2023.
- Shao, Wei* & Zhiling, Jin* & Wang, Shuo & Kang, Yufan & Xiao, Xiao & Menouar, Hamid & Zhang, Zhaofeng & Zhang, Junshan & Salim, Flora. (2022). [Long-term Spatio-Temporal Forecasting via Dynamic Multiple-Graph Attention](https://arxiv.org/abs/2204.11008). 2200-2207. 10.24963/ijcai.2022/306. 
- Kang, Yufan, Mohammad Saiedur Rahaman, Yongli Ren, Mark Sanderson, Ryen W. White, and Flora D. Salim. [App usage on-the-move: Context-and commute-aware next app prediction](http://ryenwhite.com/papers/KangPMC2022.pdf). Pervasive and Mobile Computing 87 (2022): 101704.

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
) that converts a CSV containing structured data about talks or presentations into individual markdown files that will be properly formatted for the Academic Pages template. The sample CSVs in that directory are the ones I used to create my own personal website at stuartgeiger.com. My usual workflow is that I keep a spreadsheet of my publications and talks, then run the code in these notebooks to generate the markdown files, then commit and push them to the GitHub repository.

How to edit your site's GitHub repository
------
Many people use a git client to create files on their local computer and then push them to GitHub's servers. If you are not familiar with git, you can directly edit these configuration and markdown files directly in the github.com interface. Navigate to a file (like [this one](https://github.com/academicpages/academicpages.github.io/blob/master/_talks/2012-03-01-talk-1.md) and click the pencil icon in the top right of the content preview (to the right of the "Raw | Blame | History" buttons). You can delete a file by clicking the trashcan icon to the right of the pencil icon. You can also create new files or upload files by navigating to a directory and clicking the "Create new file" or "Upload files" buttons. 

Example: editing a markdown file for a talk
![Editing a markdown file for a talk](/images/editing-talk.png)

For more info
------
More info about configuring Academic Pages can be found in [the guide](https://academicpages.github.io/markdown/). The [guides for the Minimal Mistakes theme](https://mmistakes.github.io/minimal-mistakes/docs/configuration/) (which this theme was forked from) might also be helpful.
