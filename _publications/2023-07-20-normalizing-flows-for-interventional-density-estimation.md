---
title: "Normalizing Flows for Interventional Density Estimation"
collection: publications
authors: '<b>V. Melnychuk</b>, D. Frauen, S. Feuerriegel'
date: 2023-07-20
venue: ICML
excerpt: "![infs](/images/infs.png){: style='float: left; height: 100px'}"
code: 'https://github.com/Valentyn1997/INFs'
paperurl: 'https://proceedings.mlr.press/v202/melnychuk23a/melnychuk23a.pdf'
arxiv: 'https://arxiv.org/abs/2209.06203'
poster: 'https://icml.cc/media/PosterPDFs/ICML%202023/24936.png?t=1687178238.3771722'
slides: 'https://icml.cc/media/icml-2023/Slides/24936_vMHUl2y.pdf'
---

Existing machine learning methods for causal inference usually estimate quantities expressed via the mean of potential outcomes (e.g., average treatment effect). However, such quantities do not capture the full information about the distribution of potential outcomes. In this work, we estimate the density of potential outcomes after interventions from observational data. For this, we propose a novel, fully-parametric deep learning method called Interventional Normalizing Flows. Specifically, we combine two normalizing flows, namely (i) a nuisance flow for estimating nuisance parameters and (ii) a target flow for parametric estimation of the density of potential outcomes. We further develop a tractable optimization objective based on a one-step bias correction for efficient and doubly robust estimation of the target flow parameters. As a result, our Interventional Normalizing Flows offer a properly normalized density estimator. Across various experiments, we demonstrate that our Interventional Normalizing Flows are expressive and highly effective, and scale well with both sample size and high-dimensional confounding. To the best of our knowledge, our Interventional Normalizing Flows are the first proper fully-parametric, deep learning method for density estimation of potential outcomes.

Recommended citation:
```bibtex
@inproceedings{melnychuk2023normalizing,
  title={Normalizing Flows for Interventional Density Estimation},
  author={Melnychuk, Valentyn and Frauen, Dennis and Feuerriegel, Stefan},
  booktitle={International Conference on Machine Learning},
  year={2023}
}
```

