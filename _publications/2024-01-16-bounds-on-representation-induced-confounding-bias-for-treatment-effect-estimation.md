---
title: "Bounds on Representation-Induced Confounding Bias for Treatment Effect Estimation"
collection: publications
authors: '<b>V. Melnychuk</b>, D. Frauen, S. Feuerriegel'
date: 2024-01-16
excerpt: "![ricb](/images/ricb.png){: style='float: left; height: 100px'}"
arxiv: 'https://arxiv.org/abs/2311.11321'
poster: 'https://iclr.cc/media/PosterPDFs/ICLR%202024/18278.png?t=1712930874.2539537'
paperurl: 'https://openreview.net/pdf?id=d3xKPQVjSc'
code: 'https://github.com/Valentyn1997/RICB'
venue: ICLR
---

State-of-the-art methods for conditional average treatment effect (CATE) estimation make widespread use of representation learning. Here, the idea is to reduce the variance of the low-sample CATE estimation by a (potentially constrained) low-dimensional representation. However, low-dimensional representations can lose information about the observed confounders and thus lead to bias, because of which the validity of representation learning for CATE estimation is typically violated. In this paper, we propose a new, representation-agnostic framework for estimating bounds on the representation-induced confounding bias that comes from dimensionality reduction (or other constraints on the representations) in CATE estimation. First, we establish theoretically under which conditions CATEs are non-identifiable given low-dimensional (constrained) representations. Second, as our remedy, we propose to perform partial identification of CATEs or, equivalently, aim at estimating of lower and upper bounds of the representation-induced confounding bias. We demonstrate the effectiveness of our bounds in a series of experiments. In sum, our framework is of direct relevance in practice where the validity of CATE estimation is of importance.

Recommended citation: 
```bibtex
@inproceedings{melnychuk2024bounds,
  title={Bounds on Representation-Induced Confounding Bias for Treatment Effect Estimation},
  author={Melnychuk, Valentyn and Frauen, Dennis and Feuerriegel, Stefan},
  booktitle={International Conference on Learning Representations},
  year={2024}
}
```
