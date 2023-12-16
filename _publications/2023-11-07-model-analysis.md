---
title: "Do Language Models Learn Semantics of Code? A Case Study in Vulnerability Detection"
collection: publications
permalink: /publication/model-analysis
excerpt: 'In this paper, we analyze language models to investigate whether the models have learned the semantics of code relevant to vulnerability detection, namely bug semantics, and if so, how the alignment to bug semantics relates to model performance.'
date: 2023-11-07
venue: 'ArXiv'
venue-type: conference-paper
paperurl: 'https://arxiv.org/abs/2311.04109'
citation: 'Benjamin Steenhoek, Md Mahbubur Rahman, Shaila Sharmin, & Wei Le. (2023). Do Language Models Learn Semantics of Code? A Case Study in Vulnerability Detection. https://arxiv.org/abs/2311.04109'
---

Language models are pretrained on a large corpus of source code, then fine-tuned on a smaller supervised vulnerability dataset. Due to the different training objectives and the performance of the models, it is interesting to consider whether the models have learned the semantics of code relevant to vulnerability detection, namely bug semantics, and if so, how the alignment to bug semantics relates to model performance. In this paper:
* We analyze the models using three distinct methods:
  * interpretability tools,
  * attention analysis, and
  * interaction matrix analysis.
* We compare the models' influential feature sets with the bug semantic features which define the causes of bugs, including buggy paths and Potentially Vulnerable Statements (PVS).

We find that:
* (1) better-performing models also aligned better with PVS,
* (2) the models failed to align strongly to PVS, and
* (3) the models failed to align at all to buggy paths.

Based on our analysis, we developed two annotation methods which highlight the bug semantics inside the model's inputs.
* Our annotations improved the models' performance in the majority of settings - 11 out of 16, with up to 9.57 points improvement in F1 score compared to conventional fine-tuning.
* ith our annotations, the models aligned up to 232% better to potentially vulnerable statements.
* Our code and data are available at [this https URL](https://figshare.com/s/4a16a528d6874aad51a0).
