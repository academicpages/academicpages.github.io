---
title: "Partial Counterfactual Identification of Continuous Outcomes with a Curvature Sensitivity Model"
collection: publications
authors: '<b>V. Melnychuk</b>, D. Frauen, S. Feuerriegel'
date: 2023-11-01
venue: NeurIPS
excerpt: "![part-counter](/images/part-counter.png){: style='float: left; height: 100px'}"
arxiv: 'https://arxiv.org/abs/2306.01424'
code: 'https://github.com/Valentyn1997/CSM-APID'
slides: 'https://nips.cc/media/neurips-2023/Slides/72517_T1XRQ1a.pdf'
poster: 'https://nips.cc/media/PosterPDFs/NeurIPS%202023/72517.png?t=1701185231.180074'
paperurl: 'https://proceedings.neurips.cc/paper_files/paper/2023/file/65cbe3e21ac62553111d9ecf7d60c18e-Paper-Conference.pdf'
---

Counterfactual inference aims to answer retrospective ''what if'' questions and thus belongs to the most fine-grained type of inference in Pearl's causality ladder. Existing methods for counterfactual inference with continuous outcomes aim at point identification and thus make strong and unnatural assumptions about the underlying structural causal model. In this paper, we relax these assumptions and aim at partial counterfactual identification of continuous outcomes, i.e., when the counterfactual query resides in an ignorance interval with informative bounds. We prove that, in general, the ignorance interval of the counterfactual queries has non-informative bounds, already when functions of structural causal models are continuously differentiable. As a remedy, we propose a novel sensitivity model called Curvature Sensitivity Model. This allows us to obtain informative bounds by bounding the curvature of level sets of the functions. We further show that existing point counterfactual identification methods are special cases of our Curvature Sensitivity Model when the bound of the curvature is set to zero. We then propose an implementation of our Curvature Sensitivity Model in the form of a novel deep generative model, which we call Augmented Pseudo-Invertible Decoder. Our implementation employs (i) residual normalizing flows with (ii) variational augmentations. We empirically demonstrate the effectiveness of our Augmented Pseudo-Invertible Decoder. To the best of our knowledge, ours is the first partial identification model for Markovian structural causal models with continuous outcomes.

Recommended citation: 
```bibtex
@inproceedings{melnychuk2023partial,
  title={Partial Counterfactual Identification of Continuous Outcomes with a Curvature Sensitivity Model},
  author={Melnychuk, Valentyn and Frauen, Dennis and Feuerriegel, Stefan},
  booktitle={Advances in Neural Information Processing Systems},
  year={2023}
}
```
