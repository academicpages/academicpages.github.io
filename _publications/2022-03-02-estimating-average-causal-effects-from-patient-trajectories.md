---
title: "Estimating Average Causal Effects from Patient Trajectories"
collection: publications
authors: 'D. Frauen, T. Hatt, V. Melnychuk, S. Feuerriegel'
date: 2022-03-02
excerpt: "![ct](/images/ct.png){: style='float: left; width: 350px'} We propose DeepACE: the first end-to-end neural network for estimating time-varying average causal effects using observational data. DeepACE builds upon the iterative G-computation formula to address time-varying
confounding. We develop a novel sequential targeting procedure which ensures that DeepACE provides a doubly robust and asymptotically efficient estimator. We perform an extensive series of computational experiments using state-of-the-art models for time-varying ACE estimation, establishing that DeepACE achieves a superior performance. We further demonstrate that DeepACE
generates important findings based on a medical case study for patients suffering from low back pain."
venue: 'ArXiv preprint'
paperurl: 'https://arxiv.org/abs/2203.01228'
---

In medical practice, treatments are selected based on the expected causal effects on patient outcomes. Here, the gold standard for estimating causal effects are randomized controlled trials; however, such trials are costly and sometimes even unethical. Instead, medical practice is increasingly interested in estimating causal effects among patient subgroups from electronic health records, that is, observational data. In this paper, we aim at estimating the average causal effect (ACE) from observational data (patient trajectories) that are collected over time. For this, we propose DeepACE: an end-to-end deep learning model. DeepACE leverages the iterative G-computation formula to adjust for the bias induced by time-varying confounders. Moreover, we develop a novel sequential targeting procedure which ensures that DeepACE has favorable theoretical properties, i.e., is doubly robust and asymptotically efficient. To the best of our knowledge, this is the first work that proposes an end-to-end deep learning model for estimating time-varying ACEs. We compare DeepACE in an extensive number of experiments, confirming that it achieves state-of-the-art performance. We further provide a case study for patients suffering from low back pain to demonstrate that DeepACE generates important and meaningful findings for clinical practice. Our work enables medical practitioners to develop effective treatment recommendations tailored to patient subgroups.

Recommended citation: 
```
@article{frauen2022estimating,
  title={Estimating average causal effects from patient trajectories},
  author={Frauen, Dennis and Hatt, Tobias and Melnychuk, Valentyn and Feuerriegel, Stefan},
  journal={arXiv preprint arXiv:2203.01228},
  year={2022}
}
```
