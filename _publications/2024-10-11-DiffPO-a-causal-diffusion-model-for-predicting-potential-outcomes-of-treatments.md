---
title: "DiffPO: A causal diffusion model for predicting potential outcomes of treatments"
collection: publications
authors: 'Y. Ma, <b>V. Melnychuk</b>, J. Schweisthal, S. Feuerriegel'
date: 2024-10-11
excerpt: "![diffpo](/images/diffpo.png){: style='float: left; height: 100px'}"
arxiv: 'https://arxiv.org/abs/2410.08924'
venue: NeurIPS
---

Predicting potential outcomes of interventions from observational data is crucial for decision-making in medicine, but the task is challenging due to the fundamental problem of causal inference. Existing methods are largely limited to point estimates of potential outcomes with no uncertain quantification; thus, the full information about the distributions of potential outcomes is typically ignored. In this paper, we propose a novel causal diffusion model called DiffPO, which is carefully designed for reliable inferences in medicine by learning the distribution of potential outcomes. In our DiffPO, we leverage a tailored conditional denoising diffusion model to learn complex distributions, where we address the selection bias through a novel orthogonal diffusion loss. Another strength of our DiffPO method is that it is highly flexible (e.g., it can also be used to estimate different causal quantities such as CATE). Across a wide range of experiments, we show that our method achieves state-of-the-art performance.

Recommended citation: 
```bibtex
@inproceedings{ma2024diffpo,
  title={DiffPO: A causal diffusion model for predicting potential outcomes of treatments},
  author={Ma, Yuchen and Melnychuk, Valentyn and Schweisthal, Jonas and Feuerriegel, Stefan},
  booktitle={Advances in Neural Information Processing Systems},
  year={2024}
}
```
