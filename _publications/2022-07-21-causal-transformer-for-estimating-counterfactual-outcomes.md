---
title: "Causal Transformer for Estimating Counterfactual Outcomes"
collection: publications
authors: 'V. Melnychuk, D. Frauen, S. Feuerriegel'
date: 2022-07-21
excerpt: "![anomalies](/images/anomalies.png){: style='float: left; width: 350px'} We propose a new end-to-end model for estimating counterfactual outcomes over time: the Causal Transformer (CT). To the best of our knowledge, this is the first transformer tailored to causal inference. We develop a custom training procedure for our CT based on a novel counterfactual domain confusion (CDC) loss. We use synthetic and real-world data to demonstrate that our CT achieves state-of-the-art performance. We further achieve this both for one- and multi-step-ahead predictions."
venue: 'ICML 2022'
paperurl: 'https://arxiv.org/abs/2204.07258'
---

Estimating counterfactual outcomes over time from observational data is relevant for many applications (e.g., personalized medicine). Yet, state-of-the-art methods build upon simple long short-term memory (LSTM) networks, thus rendering inferences for complex, long-range dependencies challenging. In this paper, we develop a novel Causal Transformer for estimating counterfactual outcomes over time. Our model is specifically designed to capture complex, long-range dependencies among time-varying confounders. For this, we combine three transformer subnetworks with separate inputs for time-varying covariates, previous treatments, and previous outcomes into a joint network with in-between cross-attentions. We further develop a custom, end-to-end training procedure for our Causal Transformer. Specifically, we propose a novel counterfactual domain confusion loss to address confounding bias: it aims to learn adversarial balanced representations, so that they are predictive of the next outcome but non-predictive of the current treatment assignment. We evaluate our Causal Transformer based on synthetic and real-world datasets, where it achieves superior performance over current baselines. To the best of our knowledge, this is the first work proposing transformer-based architecture for estimating counterfactual outcomes from longitudinal data.

Recommended citation: 
```
@inproceedings{melnychuk2022causal,
  title={Causal Transformer for Estimating Counterfactual Outcomes},
  author={Melnychuk, Valentyn and Frauen, Dennis and Feuerriegel, Stefan},
  booktitle={International Conference on Machine Learning},
  year={2022}
}
```
