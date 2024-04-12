---
title: "A Neural Framework for Generalized Causal Sensitivity Analysis"
collection: publications
authors: 'D. Frauen, F. Imrie, A. Curth, <b>V. Melnychuk</b>, S. Feuerriegel, M. van der Schaar'
date: 2024-01-16
excerpt: "![neural-sens](/images/neural-sens.png){: style='float: left; height: 100px'}"
arxiv: 'https://arxiv.org/abs/2311.16026'
poster: 'https://iclr.cc/media/PosterPDFs/ICLR%202024/18052.png?t=1712666669.7898104'
paperurl: 'https://openreview.net/pdf?id=ikX6D1oM1c'
code: 'https://github.com/DennisFrauen/NeuralCSA'
venue: ICLR
---

Unobserved confounding is common in many applications, making causal inference from observational data challenging. As a remedy, causal sensitivity analysis is an important tool to draw causal conclusions under unobserved confounding with mathematical guarantees. In this paper, we propose NeuralCSA, a neural framework for generalized causal sensitivity analysis. Unlike previous work, our framework is compatible with (i) a large class of sensitivity models, including the marginal sensitivity model, f-sensitivity models, and Rosenbaum's sensitivity model; (ii) different treatment types (i.e., binary and continuous); and (iii) different causal queries, including (conditional) average treatment effects and simultaneous effects on multiple outcomes. The generality of NeuralCSA is achieved by learning a latent distribution shift that corresponds to a treatment intervention using two conditional normalizing flows. We provide theoretical guarantees that NeuralCSA is able to infer valid bounds on the causal query of interest and also demonstrate this empirically using both simulated and real-world data.

Recommended citation: 
```bibtex
@inproceedings{frauen2024neural,
  title={A Neural Framework for Generalized Causal Sensitivity Analysis},
  author={Frauen, Dennis and Imrie, Fergus and Curth, Alicia and Melnychuk, Valentyn and Feuerriegel, Stefan and van der Schaar, Mihaela},
  booktitle={International Conference on Learning Representations},
  year={2024}
}
```
