---
title: "A General Recipe for Likelihood-free Bayesian Optimization"
collection: publications
permalink: /publications/LFBO
venue: "The 39th International Conference on Machine Learning (ICML 2022)"
date: 2022-5-20
citation: 'Jiaming Song*, <b>Lantao Yu</b>* (equal contribution), Willie Neiswanger, Stefano Ermon.
<i>The 39th International Conference on Machine Learning</i>. <b>ICML 2022</b>. <b> <span style="color:red">(Long Oral, Top 2.2%)</span> </b>' 
---

## Abstract
The acquisition function, a critical component in Bayesian optimization (BO), can often be written as the expectation of a utility function under a surrogate model. However, to ensure that acquisition functions are tractable to optimize, restrictions must be placed on the surrogate model and utility function. To extend BO to a broader class of models and utilities, we propose likelihood-free BO (LFBO), an approach based on likelihood-free inference. LFBO directly models the acquisition function without having to separately perform inference with a probabilistic surrogate model. We show that computing the acquisition function in LFBO can be reduced to optimizing a weighted classification problem, where the weights correspond to the utility being chosen. By choosing the utility function for expected improvement (EI), LFBO outperforms various state-of-the-art black-box optimization methods on several real-world optimization problems. LFBO can also effectively leverage composite structures of the objective function, which further improves its regret by several orders of magnitude.