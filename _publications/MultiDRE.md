---
title: "A Unified Framework for Multi-distribution Density Ratio Estimation"
collection: publications
permalink: /publications/MultiDRE
venue: "ArXiv 2021"
date: 2021-12-7
citation: '<b>Lantao Yu</b>, Yujia Jin, Stefano Ermon. <i>Preprint. arXiv:2112.03440</i>'
---

[[PDF]](https://arxiv.org/pdf/2112.03440.pdf)

## Abstract
Binary density ratio estimation (DRE), the problem of estimating the ratio p1/p2 given their empirical samples, provides the foundation for many state-of-the-art machine learning algorithms such as contrastive representation learning and covariate shift adaptation. In this work, we consider a generalized setting where given samples from multiple distributions p1,…,pk (for k>2), we aim to efficiently estimate the density ratios between all pairs of distributions. Such a generalization leads to important new applications such as estimating statistical discrepancy among multiple random variables like multi-distribution f-divergence, and bias correction via multiple importance sampling. We then develop a general framework from the perspective of Bregman divergence minimization, where each strictly convex multivariate function induces a proper loss for multi-distribution DRE. Moreover, we rederive the theoretical connection between multi-distribution density ratio estimation and class probability estimation, justifying the use of any strictly proper scoring rule composite with a link function for multi-distribution DRE. We show that our framework leads to methods that strictly generalize their counterparts in binary DRE, as well as new methods that show comparable or superior performance on various downstream tasks.