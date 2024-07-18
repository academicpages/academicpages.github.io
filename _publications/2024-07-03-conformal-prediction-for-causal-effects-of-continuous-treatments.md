---
title: "Conformal Prediction for Causal Effects of Continuous Treatments"
collection: publications
authors: 'M. Schröder, D. Frauen, J. Schweisthal, K. Hess, <b>V. Melnychuk</b>, S. Feuerriegel'
date: 2024-07-03
excerpt: "![fair-policy](/images/conformal.png){: style='float: left; height: 100px'}"
arxiv: 'https://arxiv.org/abs/2407.03094'
preprint: true
---

Uncertainty quantification of causal effects is crucial for safety-critical applications such as personalized medicine. A powerful approach for this is conformal prediction, which has several practical benefits due to model-agnostic finite-sample guarantees. Yet, existing methods for conformal prediction of causal effects are limited to binary/discrete treatments and make highly restrictive assumptions such as known propensity scores. In this work, we provide a novel conformal prediction method for potential outcomes of continuous treatments. We account for the additional uncertainty introduced through propensity estimation so that our conformal prediction intervals are valid even if the propensity score is unknown. Our contributions are three-fold: (1) We derive finite-sample prediction intervals for potential outcomes of continuous treatments. (2) We provide an algorithm for calculating the derived intervals. (3) We demonstrate the effectiveness of the conformal prediction intervals in experiments on synthetic and real-world datasets. To the best of our knowledge, we are the first to propose conformal prediction for continuous treatments when the propensity score is unknown and must be estimated from data.

Recommended citation: 
```bibtex
@article{schroder2024conformal,
  title={Conformal Prediction for Causal Effects of Continuous Treatments},
  author={Schr{\"o}der, Maresa and Frauen, Dennis and Schweisthal, Jonas and Hess, Konstantin and Melnychuk, Valentyn and Feuerriegel, Stefan},
  journal={arXiv preprint arXiv:2407.03094},
  year={2024}
}
```
