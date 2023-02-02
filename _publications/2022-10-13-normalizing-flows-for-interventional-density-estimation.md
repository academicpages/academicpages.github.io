---
title: "Normalizing Flows for Interventional Density Estimation"
collection: publications
authors: '<b>V. Melnychuk</b>, D. Frauen, S. Feuerriegel'
date: 2022-10-13
excerpt: "![infs](/images/infs.png){: style='float: left; height: 100px'}"
arxiv: 'https://arxiv.org/abs/2209.06203'
---

Existing machine learning methods for causal inference usually estimate quantities expressed via the mean of potential outcomes (e.g., average treatment effect). However, such quantities do not capture the full information about the distribution of potential outcomes. In this work, we estimate the density of potential outcomes after interventions from observational data. For this, we propose a novel, fully-parametric deep learning method called Interventional Normalizing Flows. Specifically, we combine two normalizing flows, namely (i) a teacher flow for estimating nuisance parameters and (ii) a student flow for a parametric estimation of the density of potential outcomes. We further develop a tractable optimization objective based on a one-step bias correction for an efficient and doubly robust estimation of the student flow parameters. As a result our Interventional Normalizing Flows offer a properly normalized density estimator. Across various experiments, we demonstrate that our Interventional Normalizing Flows are expressive and highly effective, and scale well with both sample size and high-dimensional confounding. To the best of our knowledge, our Interventional Normalizing Flows are the first fully-parametric, deep learning method for density estimation of potential outcomes.

Recommended citation:
```bibtex
@article{melnychuk2022normalizing,
  title={Normalizing Flows for Interventional Density Estimation},
  author={Melnychuk, Valentyn and Frauen, Dennis and Feuerriegel, Stefan},
  journal={arXiv preprint arXiv:2209.06203},
  year={2022}
}
```

