---
title: "Fair Off-Policy Learning from Observational Data"
collection: publications
authors: 'D. Frauen, <b>V. Melnychuk</b>, S. Feuerriegel'
date: 2024-05-01
excerpt: "![fair-policy](/images/fair-policy.png){: style='float: left; height: 100px'}"
arxiv: 'https://arxiv.org/abs/2303.08516'
paperurl: 'https://proceedings.mlr.press/v235/frauen24a.html'
code: 'https://github.com/DennisFrauen/FairPol'
poster: 'https://icml.cc/media/PosterPDFs/ICML%202024/33022.png?t=1721725751.2503126'
venue: ICML
---

Algorithmic decision-making in practice must be fair for legal, ethical, and societal reasons. To achieve this, prior research has contributed various approaches that ensure fairness in machine learning predictions, while comparatively little effort has focused on fairness in decision-making, specifically off-policy learning. In this paper, we propose a novel framework for fair off-policy learning: we learn decision rules from observational data under different notions of fairness, where we explicitly assume that observational data were collected under a different – potentially discriminatory – behavioral policy. Importantly, our framework applies to different fairness notions for off-policy learning, where fairness is formalized based on actions or policy values. As our main contribution, we propose a neural network-based framework to learn optimal policies under different fairness notions. We further provide theoretical guarantees in the form of generalization bounds for the finite-sample version of our framework. We demonstrate the effectiveness of our framework through extensive numerical experiments using both simulated and real-world data. Altogether, our work enables algorithmic decision-making in a wide array of practical applications where fairness must be ensured.

Recommended citation: 
```bibtex
@inproceedings{frauen2024fair,
  title={Fair Off-Policy Learning from Observational Data},
  author={Frauen, Dennis and Melnychuk, Valentyn and Feuerriegel, Stefan},
  booktitle={International Conference on Machine Learning},
  year={2024}
}
```
