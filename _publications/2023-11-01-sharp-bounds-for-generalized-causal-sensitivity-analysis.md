---
title: "Sharp Bounds for Generalized Causal Sensitivity Analysis"
collection: publications
authors: 'D. Frauen, <b>V. Melnychuk</b>, S. Feuerriegel'
date: 2023-11-01
venue: NeurIPS
excerpt: "![sharp-bounds](/images/sharp-bounds.png){: style='float: left; height: 100px'}"
arxiv: 'https://arxiv.org/abs/2305.16988'
code: 'https://github.com/DennisFrauen/SharpCausalSensitivity'
slides: 'https://nips.cc/media/neurips-2023/Slides/70747.pdf'
poster: 'https://nips.cc/media/PosterPDFs/NeurIPS%202023/70747.png'
paperurl: 'https://proceedings.neurips.cc/paper_files/paper/2023/file/7f8b8bc8ebac661c442c4dafd5d98c08-Paper-Conference.pdf'
---

Causal inference from observational data is crucial for many disciplines such as medicine and economics. However, sharp bounds for causal effects under relaxations of the unconfoundedness assumption (causal sensitivity analysis) are subject to ongoing research. So far, works with sharp bounds are restricted to fairly simple settings (e.g., a single binary treatment). In this paper, we propose a unified framework for causal sensitivity analysis under unobserved confounding in various settings. For this, we propose a flexible generalization of the marginal sensitivity model (MSM) and then derive sharp bounds for a large class of causal effects. This includes (conditional) average treatment effects, effects for mediation analysis and path analysis, and distributional effects. Furthermore, our sensitivity model is applicable to discrete, continuous, and time-varying treatments. It allows us to interpret the partial identification problem under unobserved confounding as a distribution shift in the latent confounders while evaluating the causal effect of interest. In the special case of a single binary treatment, our bounds for (conditional) average treatment effects coincide with recent optimality results for causal sensitivity analysis. Finally, we propose a scalable algorithm to estimate our sharp bounds from observational data.

Recommended citation: 
```bibtex
@inproceedings{frauen2023sharp,
  title={Sharp Bounds for Generalized Causal Sensitivity Analysis},
  author={Frauen, Dennis and Melnychuk, Valentyn and Feuerriegel, Stefan},
  booktitle={Advances in Neural Information Processing Systems},
  year={2023}
}
```
