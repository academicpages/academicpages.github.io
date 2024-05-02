---
title: "Fair Off-Policy Learning from Observational Data"
collection: publications
authors: 'D. Frauen, <b>V. Melnychuk</b>, S. Feuerriegel'
date: 2024-05-01
excerpt: "![fair-policy](/images/fair-policy.png){: style='float: left; height: 100px'}"
arxiv: 'https://arxiv.org/abs/2303.08516'
venue: ICML
---

Businesses and organizations must ensure that their algorithmic decision-making is fair in order to meet legislative, ethical, and societal demands. For example, decision-making in automated hiring must not discriminate with respect to gender or race. To achieve this, prior research has contributed approaches that ensure algorithmic fairness in machine learning predictions, while comparatively little effort has focused on algorithmic fairness in decision models, specifically off-policy learning. In this paper, we propose a novel framework for fair off-policy learning: we learn decision rules from observational data under different notions of fairness, where we explicitly assume that observational data were collected under a different -- potentially biased -- behavioral policy. For this, we first formalize different fairness notions for off-policy learning. We then propose a machine learning approach to learn optimal policies under these fairness notions. Specifically, we reformulate the fairness notions into unconstrained learning objectives that can be estimated from finite samples. Here, we leverage machine learning to minimize the objective constrained on a fair representation of the data, so that the resulting policies satisfy our fairness notions. We further provide theoretical guarantees in form of generalization bounds for the finite-sample version of our framework. We demonstrate the effectiveness of our framework through extensive numerical experiments using both simulated and real-world data. As a result, our work enables algorithmic decision-making in a wide array of practical applications where fairness must ensured.

Recommended citation: 
```bibtex
@inproceedings{frauen2024fair,
  title={Fair Off-Policy Learning from Observational Data},
  author={Frauen, Dennis and Melnychuk, Valentyn and Feuerriegel, Stefan},
  booktitle={International Conference on Machine Learning},
  year={2024}
}
```
