---
permalink: /
title: "Chengyi Lyu"
excerpt: "About me"
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

About me
======

Hi, it's Chengyi. I am a first year PhD student University of Colorado, Boulder. I am fortunate to be advised by  [Prof. **Huanan Zhang**](http://huananzhang.mystrikingly.com/).  Before joining UCB, I received my bachelor's degree from USTC. 


I'm interested in the general field of **Data Mining** and **Machine Learning**. Particularly, I aspire to solve real-world problems using Machine Learning techniques. Big Data itself cannot be utilized and well-understood. I want to be a data scientist who is able to turn data into knowledge which, in the long run, make impacts and improve the living standard of human society.


- My [<span style="color:orange">**Curriculum Vitae** </span>](/files/Chengyi_CV.pdf).

## Education
- University of Science and Technology of China **(USTC)**, China
	- B.E. in Mathematics, Sep.2015 -- Jun.2019 (Expected)
	<!--- GPA: 3.68/4.0 (87.1/100) 
	- Advisor:  Prof. [**Weinan Zhang**](http://wnzhang.net/) and Prof. [**Zhenhui (Jessie) Li**](https://faculty.ist.psu.edu/jessieli/Site/index.html)-->

## Publication
- Hua Wei, **Chacha Chen**, Chang Liu, Guanjie Zheng, Zhenhui Li. Learning to Simulate on Sparse Data. In Proceedings of European Conference on Machine Learning and Principles and Practice of Knowledge Discovery in Databases (**ECML-PKDD 2020**), Ghent, Belgium, Sep 2020. (To appear)
- **Chacha Chen**, Hua Wei, Nan Xu, Guanjie Zheng, Ming Yang, Yuanhao Xiong, Kai Xu and Zhenhui Li. Toward A Thousand Lights: Decentralized Deep Reinforcement Learning for Large-Scale Traffic Signal Control. In Proceedings of the Thirty-Fourth AAAI Conference on Artificial Intelligence (**AAAI'20**). (Acceptance rate: ~20.6\%) [[**Paper**](/files/chacha-AAAI2020.pdf)]
- Hua Wei*, Nan Xu*, Huichu Zhang, Guanjie Zheng, Xinshi Zang, **Chacha Chen**, Weinan Zhang, Yanmin Zhu, Kai Xu, and Zhenhui Li, [CoLight: Learning Network-level Cooperation for Traffic Signal Control](https://arxiv.org/pdf/1905.05717.pdf). In Proceedings of the 28th ACM International Conference on Information and Knowledge Management (**CIKM 2019**), Beijing, China, Nov 2019. (Acceptance rate: ~200/1030=19.4%)[[**Paper**](http://personal.psu.edu/hzw77/publications/colight-cikm19.pdf)]
- Hua Wei, **Chacha Chen**, Guanjie Zheng, Kan Wu, Vikash V. Gayah, Kai Xu and Zhenhui Li, [PressLight: Learning Max Pressure Control to Coordinate Traffic Signals in Arterial Network](https://dl.acm.org/citation.cfm?id=3330949). In Proceedings of the 25th ACM SIGKDD International Conference on Knowledge Discovery and Data Mining (**KDD 2019**), Anchorage, AK, USA, Aug 2019. (Acceptance rate: ~170/1200=14.2%)[[**Paper**](http://personal.psu.edu/hzw77/publications/presslight-kdd19.pdf)]





## Research Experience

### Deep Reinforcement Learning for Traffic Signal Control 
_Research Intern, Advisor: Prof. Zhenhui (Jessie) Li Jul.2018 - Present_  

- Designed and implemented a reinforcement learning (RL) approach with justification on state and reward design for multi-intersection traffic signal control along arterials
- Draw a connection between RL method and classical transportation theory for the first time
- Justified our RL model in comparison to the closed form solution under the same simplified experiment settings
- Achieved state-of-the-art performance in simulation on both synthetic and real-world traffic data
- Started conducting field experiments in Hangzhou China

<span style="color:purple">**Here's a demo video showing how our intelligent traffic light learn the greenwave!** </span> 
<iframe width="560" height="315" src="https://www.youtube.com/embed/0zeHDpv361Q" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

<!--<span style="color:purple">**Hangzhou Intelligent Signal Control System Demo** </span> 

<iframe width="560" height="315" src="https://www.youtube.com/embed/Oj2rRASpPGQ" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>-->

<span style="color:purple">**Toward a Thousand Lights--Manhattan Experiment Demo** </span> 

<iframe width="560" height="315" src="https://www.youtube.com/embed/-UulnApXbjM" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

### Mining Homeownership Patterns 
_Research Assistant, Advisor: Prof. Tingting Lu (Social Science) and Prof. Weinan Zhang Mar.2018 - Present_

- Formulated the task into a multi-class classification problem in machine learning based on the data collected from a national scale survey
- Implemented logistic regression and tree model to predict the homeownership
- Interpreted the machine learning models with feature ranking and visualization which further reveals the
mechanism and pattern of homeownership

### SVM Toolbox for Both Indefinite and Semi-definite Kernel Learning 
_Research Assistant, Advisor: Prof. Xiaolin Huang Sep.2017 - Mar.2018_

- Coauthored a software package which accommodates Support Vector Machine (SVM) classification algorithms with indefinite kernels and semi-definite kernels
- Incorporated Sequential Minimal Optimization (SMO) in the traditional SVM algorithm
- Provided various kernel functions, including TAHN, TL1, Gaussian, polynomial and linear kernels
- Implemented various vector machine algorithms, including KVM, LSSVM, kPCA

## Contact
- Email: cjc6647@psu.edu
<!--- Tel: (+1)8146992243-->
<!--- Skype: chachachen1997-->
<!--- Address: 800 Dongchuan Rd, Minhang Campus, Shanghai Jiaotong University, Shanghai-->


<!--## Miscellaneous
- Volunteer: Organized a bazaar selling study notes to help people with kidney disease
- Programming: C/C++, Python, C#, Java, JavaScript, SQL
- Interests: badminton, swimming, photography-->

<!--Other places to find me: facebook, weibo (in Chinese)-->


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
