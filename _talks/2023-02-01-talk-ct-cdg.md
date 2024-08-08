---
title: "Causal Transformer for Estimating Counterfactual Outcomes, ICML 2022 paper"
collection: talks
type: "Presentation"
venue: "<a href='https://matej-zecevic.de/cdg/'>Causality Discussion Group</a>"
date: 2023-02-01
location: "online"
recording: 'https://www.youtube.com/watch?v=mkacvr0csPs'
slides: 'https://drive.google.com/file/d/1fFHzt8Yee3ppc_K-rmVI87PzI1N6mjZk/view?usp=sharing'
---

**Title**: Causal Transformer for Estimating Counterfactual Outcomes

**Abstract**: Estimating counterfactual outcomes over time from observational data is relevant for many applications (e.g., personalized medicine). Yet, state-of-the-art methods build upon simple long short-term memory (LSTM) networks, thus rendering inferences for complex, long-range dependencies challenging. In this paper, we develop a novel Causal Transformer for estimating counterfactual outcomes over time. Our model is specifically designed to capture complex, long-range dependencies among time-varying confounders. For this, we combine three transformer subnetworks with separate inputs for time-varying covariates, previous treatments, and previous outcomes into a joint network with in-between cross-attentions. We further develop a custom, end-to-end training procedure for our Causal Transformer. Specifically, we propose a novel counterfactual domain confusion loss to address confounding bias: it aims to learn adversarial balanced representations, so that they are predictive of the next outcome but non-predictive of the current treatment assignment. We evaluate our Causal Transformer based on synthetic and real-world datasets, where it achieves superior performance over current baselines. To the best of our knowledge, this is the first work proposing transformer-based architecture for estimating counterfactual outcomes from longitudinal data.

**Paper Link**: [https://proceedings.mlr.press/v162/melnychuk22a/melnychuk22a.pdf](https://proceedings.mlr.press/v162/melnychuk22a/melnychuk22a.pdf)
