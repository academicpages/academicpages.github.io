---
title: "Orthogonal Representation Learning for Estimating Causal Quantities"
collection: publications
authors: '<b>V. Melnychuk</b>, D. Frauen, J. Schweisthal, S. Feuerriegel'
date: 2025-02-06
excerpt: "![orht-repr](/images/orht-repr.png){: style='float: left; height: 100px'}"
arxiv: 'https://arxiv.org/abs/2502.04274'
preprint: true
---

Representation learning is widely used for estimating causal quantities (e.g., the conditional average treatment effect) from observational data. While existing representation learning methods have the benefit of allowing for end-to-end learning, they do not have favorable theoretical properties of Neyman-orthogonal learners, such as double robustness and quasi-oracle efficiency. Also, such representation learning methods often employ additional constraints, like balancing, which may even lead to inconsistent estimation. In this paper, we propose a novel class of Neyman-orthogonal learners for causal quantities defined at the representation level, which we call OR-learners. Our OR-learners have several practical advantages: they allow for consistent estimation of causal quantities based on any learned representation, while offering favorable theoretical properties including double robustness and quasi-oracle efficiency. In multiple experiments, we show that, under certain regularity conditions, our OR-learners improve existing representation learning methods and achieve state-of-the-art performance. To the best of our knowledge, our OR-learners are the first work to offer a unified framework of representation learning methods and Neyman-orthogonal learners for causal quantities estimation.

Recommended citation: 
```bibtex
@article{melnychuk2025orthogonal,
  title={Orthogonal representation learning for estimating causal quantities},
  author={Melnychuk, Valentyn and Frauen, Dennis and Schweisthal, Jonas and Feuerriegel, Stefan},
  journal={arXiv preprint arXiv:2502.04274},
  year={2025}
}
```
