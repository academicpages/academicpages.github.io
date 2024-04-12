---
title: "Bayesian Neural Controlled Differential Equations for Treatment Effect Estimation"
collection: publications
authors: 'K. Hess, <b>V. Melnychuk</b>, D. Frauen, S. Feuerriegel'
date: 2024-01-16
excerpt: "![fair-policy](/images/BNCDE.png){: style='float: left; height: 100px'}"
arxiv: 'https://arxiv.org/abs/2310.17463'
paperurl: 'https://openreview.net/pdf?id=uwO71a8wET'
poster: 'https://iclr.cc/media/PosterPDFs/ICLR%202024/17558.png?t=1712669639.339985'
code: 'https://github.com/konstantinhess/Bayesian-Neural-CDE'
venue: ICLR
---

Treatment effect estimation in continuous time is crucial for personalized medicine. However, existing methods for this task are limited to point estimates of the potential outcomes, whereas uncertainty estimates have been ignored. Needless to say, uncertainty quantification is crucial for reliable decision-making in medical applications. To fill this gap, we propose a novel Bayesian neural controlled differential equation (BNCDE) for treatment effect estimation in continuous time. In our BNCDE, the time dimension is modeled through a coupled system of neural controlled differential equations and neural stochastic differential equations, where the neural stochastic differential equations allow for tractable variational Bayesian inference. Thereby, for an assigned sequence of treatments, our BNCDE provides meaningful posterior predictive distributions of the potential outcomes. To the best of our knowledge, ours is the first tailored neural method to provide uncertainty estimates of treatment effects in continuous time. As such, our method is of direct practical value for promoting reliable decision-making in medicine.

Recommended citation: 
```bibtex
@inproceedings{hess2024bayesian,
  title={Bayesian Neural Controlled Differential Equations for Treatment Effect Estimation},
  author={Hess, Konstantin and Melnychuk, Valentyn and Frauen, Dennis and Feuerriegel, Stefan},
  booktitle={International Conference on Learning Representations},
  year={2024}
}
```
