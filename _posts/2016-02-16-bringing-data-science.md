---
title: 'Bringing Data Science Back to Statistics'
date: 2016-02-16
permalink: /posts/2016/02/bringing-data-science/
tags:
  - data science
  - statistics
  - reproducibility
---

*This blog post originally appeared on the [BIDS blog](https://bids.berkeley.edu/news/bringing-data-science-back-statistics).*

One of the sessions that I attended at the 2015 Moore-Sloan Data Science Environment Summit was titled "Isn't Statistics Part of Data Science?" It is a niggling question I often consider, especially given how few statisticians there are at BIDS. A group of about forty people from statistics, computer science, and applied domains convened to discuss differences in practice and culture that divide statistics from data science. I am an applied statistician and a fellow at BIDS straddling these two worlds. I find it difficult to identify the line dividing these roles.

Although its role isn’t well defined, it seems obvious that statistics must play a part in data science. Like Drew Conway's famous [data science Venn diagram](http://drewconway.com/zia/2013/3/26/the-data-science-venn-diagram) points out, if you try to do data science without mathematical and statistical knowledge, you're in the "danger zone." However, the reverse is also true: successful applied statistics projects must incorporate ideas from data science. I'll illustrate a few points where statistics and data science intersect in my recent paper with my colleagues Anne Boring and Philip B. Stark, ["Student Evaluations of Teaching (Mostly) Do Not Measure Teaching Effectiveness." ](https://www.scienceopen.com/document?vid=818d8ec0-5908-47d8-86b4-5dc38f04b23e)

![Alt text](https://bids.berkeley.edu/sites/default/files/data_science_vd.png)

Reproducibility
===============

In the last several years, statistics, in particular hypothesis testing (null hypothesis significance testing [NHST]) has come under fire. Critics claim that NHST has resulted in irreproducible results, causing a large proportion of scientific studies to report “false discoveries”—that is, positive results that cannot be replicated. One psychology journal even went so far as to [ban p-values](http://www.nature.com/news/psychology-journal-bans-p-values-1.17001). These failures of replicability are caused by the misuse of statistical methods (amounting to [quantifauxcation](https://www.stat.berkeley.edu/~stark/Preprints/eucCurtain15.pdf)). Distorted incentives in science (i.e., a reward structure that values—and publishes—only positive results, thereby encouraging p-hacking and changing endpoints, and that does not value or publish software or labor-intensive scrutiny of data, thereby discouraging careful, reliable data analysis), inadequate training in statistical thinking, and a general lack of transparency are at the root of the problem. It’s not the fault of statistics. Indeed, better training in statistics—especially statistical reasoning—might go a long way in eliminating the problem. I hope that a move toward transparent, well-documented analyses will take the blame off of statistics. It is important to show all the steps of an analysis so anyone can trace where a result came from and what other tests were done before arriving at a conclusion. Statisticians have already been doing this, but tools and ideas that are commonly used in data science facilitate the process.

For our paper, we used GitHub to collaborate and to keep our analyses and manuscript under version control. The code and results of our analyses are in Jupyter notebooks, which users can modify and run interactively. We made the US dataset available; due to French privacy laws, we could not post the French dataset. The notebooks, data, and notes on the variables are publicly available in the [GitHub repository](https://github.com/kellieotto/SET-and-Gender-Bias). Finally, our paper appears in [ScienceOpen Research](https://www.scienceopen.com/document?vid=818d8ec0-5908-47d8-86b4-5dc38f04b23e), an open access publisher with post-publication peer review. Anyone can read our paper, think critically about the data, and comment about it online. Rewards are built into the system, as anyone who chooses to review the paper formally can get a DOI for his or her review. Making analyses and papers open is critical for advancing knowledge: this is how people catch errors and how science moves forward.

Software Tools
==============

Data science puts a greater emphasis on creating software than statistics. It would serve in the interest of statisticians who develop new statistical methods to spend more time thinking about software. After all, what's the point of developing theory if nobody can use it in practice?

We used permutation tests and the Neyman-Rubin potential outcomes framework in our paper. Permutation tests are based on invariances that come from the experimental design and require minimal assumptions about the data that are usually guaranteed by the experimental design. This approach is in contrast to many classical statistical tests, which were developed when computation was a barrier to data analysis. These methods require strong assumptions, but reduce complicated distributions to the standard normal curve. The scale of data is growing, but so is the scale of computation, reducing our dependence on classical methods. In tandem with the paper, we developed permute, a Python package for permutation tests. We used parts of this package for our analyses. Others can use our package to do permutation tests and look at our paper as a guide for how to design appropriate hypothesis tests.

Data Quality
============

There's a myth that data speaks for itself. It would be glamorous if a data scientist could take a dataset, throw some statistical methods at it, and uncover deep secrets. But there are some things that data simply can't tell you. Imagine you ran a perfect randomized control trial to study the effect of a drug on cardiovascular disease. If your study population consisted of all men, then no matter how well you conducted the trial, the data can't tell you anything about how the drug would affect women. Applied statisticians are trained to recognize these kinds of issues involving sampling, causal inference, and generalizability, all of which must be considered before data analysis begins.

Our paper gets at the heart of data quality: the premise is that student evaluations of teaching (SETs) don’t measure what they purport to measure. SETs are used as a proxy to measure teaching effectiveness, but we find that SETs correlate more strongly with grade expectations and instructor gender than with teaching effectiveness. University administrations use SETs to compare instructors and to make hiring, tenure, and promotion decisions. As such, actual teaching effectiveness is only a fraction of what factors into these decisions. It makes no sense to evaluate instruction using data that are unrelated to the quality or effectiveness of the instruction.

To answer the question for whether statistics is part of data science, I’d say that, yes, data science and statistics are fundamentally connected. Tools and ideas from data science enrich my practice as a statistician. However, lack of good software engineering habits holds statistics back from playing a greater role in data science, and this is a cause for concern. With the growing scale of modern data, data scientists need to worry about the statistical concepts around experimental design in order to extract meaningful inferences from data. The Moore-Sloan Data Science Environment can encourage the integration of statistics and data science by involving more statisticians, by teaching statistical concepts alongside computational tools in its regular events and workshops, and by continuing to emphasize statistical thinking in [data science education programs](http://data.berkeley.edu) on campus.
------