---
title: "Quantifying Aleatoric Uncertainty of the Treatment Effect: A Novel Orthogonal Learner"
collection: publications
authors: '<b>V. Melnychuk</b>, S. Feuerriegel, M. van der Schaar'
date: 2024-11-06
excerpt: "![diffpo](/images/au-learner.png){: style='float: left; height: 100px'}"
arxiv: 'https://arxiv.org/abs/2411.03387'
code: 'https://github.com/Valentyn1997/AU-CNFs'
venue: NeurIPS
---

Estimating causal quantities from observational data is crucial for understanding the safety and effectiveness of medical treatments. However, to make reliable inferences, medical practitioners require not only estimating averaged causal quantities, such as the conditional average treatment effect, but also understanding the randomness of the treatment effect as a random variable. This randomness is referred to as aleatoric uncertainty and is necessary for understanding the probability of benefit from treatment or quantiles of the treatment effect. Yet, the aleatoric uncertainty of the treatment effect has received surprisingly little attention in the causal machine learning community. To fill this gap, we aim to quantify the aleatoric uncertainty of the treatment effect at the covariate-conditional level, namely, the conditional distribution of the treatment effect (CDTE). Unlike average causal quantities, the CDTE is not point identifiable without strong additional assumptions. As a remedy, we employ partial identification to obtain sharp bounds on the CDTE and thereby quantify the aleatoric uncertainty of the treatment effect. We then develop a novel, orthogonal learner for the bounds on the CDTE, which we call AU-learner. We further show that our AU-learner has several strengths in that it satisfies Neyman-orthogonality and is doubly robust. Finally, we propose a fully-parametric deep learning instantiation of our AU-learner.

Recommended citation: 
```bibtex
@inproceedings{melnychuk2024quantifying,
  title={Quantifying Aleatoric Uncertainty of the Treatment Effect: A Novel Orthogonal Learner},
  author={Melnychuk, Valentyn and Feuerriegel, Stefan and van der Schaar, Mihaela},
  booktitle={Advances in Neural Information Processing Systems},
  year={2024}
}
```
