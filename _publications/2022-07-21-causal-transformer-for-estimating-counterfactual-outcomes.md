---
title: "Causal Transformer for Estimating Counterfactual Outcomes"
collection: publications
authors: '<b>V. Melnychuk</b>, D. Frauen, S. Feuerriegel'
date: 2022-07-21
excerpt: "![ct](/images/ct.png){: style='float: left; height: 100px'}"
venue: 'ICML'
arxiv: 'https://arxiv.org/abs/2204.07258'
paperurl: 'https://proceedings.mlr.press/v162/melnychuk22a/melnychuk22a.pdf'
code: 'https://github.com/Valentyn1997/CausalTransformer'
slides: 'https://icml.cc/media/icml-2022/Slides/17693.pdf'
poster: 'https://icml.cc/media/PosterPDFs/ICML%202022/ada5e0b63ef60e2239fa8abdd4aa2f8e.png?t=1657902801.7339456'
---

Estimating counterfactual outcomes over time from observational data is relevant for many applications (e.g., personalized medicine). Yet, state-of-the-art methods build upon simple long short-term memory (LSTM) networks, thus rendering inferences for complex, long-range dependencies challenging. In this paper, we develop a novel Causal Transformer for estimating counterfactual outcomes over time. Our model is specifically designed to capture complex, long-range dependencies among time-varying confounders. For this, we combine three transformer subnetworks with separate inputs for time-varying covariates, previous treatments, and previous outcomes into a joint network with in-between cross-attentions. We further develop a custom, end-to-end training procedure for our Causal Transformer. Specifically, we propose a novel counterfactual domain confusion loss to address confounding bias: it aims to learn adversarial balanced representations, so that they are predictive of the next outcome but non-predictive of the current treatment assignment. We evaluate our Causal Transformer based on synthetic and real-world datasets, where it achieves superior performance over current baselines. To the best of our knowledge, this is the first work proposing transformer-based architecture for estimating counterfactual outcomes from longitudinal data.

Recommended citation: 
```bibtex
@inproceedings{melnychuk2022causal,
  title={Causal Transformer for Estimating Counterfactual Outcomes},
  author={Melnychuk, Valentyn and Frauen, Dennis and Feuerriegel, Stefan},
  booktitle={International Conference on Machine Learning},
  year={2022}
}
```
