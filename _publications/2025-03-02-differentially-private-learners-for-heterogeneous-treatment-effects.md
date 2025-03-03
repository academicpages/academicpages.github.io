---
title: "Differentially Private Learners for Heterogeneous Treatment Effects"
collection: publications
authors: 'M. Schröder, <b>V. Melnychuk</b>, S. Feuerriegel'
date: 2025-03-02
excerpt: "![private_cate](/images/private_cate.png){: style='float: left; height: 100px'}"
paperurl: 'https://openreview.net/pdf?id=1z3SOCwst9'
code: 'https://github.com/m-schroder/DP-CATE'
venue: ICLR
---

Patient data is widely used to estimate heterogeneous treatment effects and understand the effectiveness and safety of drugs. Yet, patient data includes highly sensitive information that must be kept private. In this work, we aim to estimate the conditional average treatment effect (CATE) from observational data under differential privacy. Specifically, we present DP-CATE, a novel framework for CATE estimation that is Neyman-orthogonal and ensures differential privacy of the estimates. Our framework is highly general: it applies to any two-stage CATE meta-learner with a Neyman-orthogonal loss function and any machine learning model can be used for nuisance estimation. We further provide an extension of our DP-CATE, where we employ RKHS regression to release the complete CATE function while ensuring differential privacy. We demonstrate the effectiveness of DP-CATE across various experiments using synthetic and real-world datasets. To the best of our knowledge, we are the first to provide a framework for CATE estimation that is doubly robust and differentially private.

Recommended citation: 
```bibtex
@inproceedings{schroder2025differentially,
  title={Differentially Private Learners for Heterogeneous Treatment Effects},
  author={Schr{\"o}der, Maresa and Melnychuk, Valentyn and Feuerriegel, Stefan},
  booktitle={International Conference on Learning Representations},
  year={2025}
}
```
