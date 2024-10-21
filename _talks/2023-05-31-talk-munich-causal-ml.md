---
title: "Causal Transformer for Estimating Counterfactual Outcomes & Normalizing Flows for Interventional Density Estimation, ICML 2022 & 2023 papers"
collection: talks
type: "Presentation"
venue: "1st Munich Causal ML Workshop"
date: 2023-05-31
location: "LMU Munich, Munich, Germany"
slides: 'https://valentyn1997.github.io/doc/2023-05-31-Workshop.pdf'
---


**Title**: Causal Transformer for Estimating Counterfactual Outcomes

**Abstract**: Estimating counterfactual outcomes over time from observational data is relevant for many applications (e.g., personalized medicine). Yet, state-of-the-art methods build upon simple long short-term memory (LSTM) networks, thus rendering inferences for complex, long-range dependencies challenging. In this paper, we develop a novel Causal Transformer for estimating counterfactual outcomes over time. Our model is specifically designed to capture complex, long-range dependencies among time-varying confounders. For this, we combine three transformer subnetworks with separate inputs for time-varying covariates, previous treatments, and previous outcomes into a joint network with in-between cross-attentions. We further develop a custom, end-to-end training procedure for our Causal Transformer. Specifically, we propose a novel counterfactual domain confusion loss to address confounding bias: it aims to learn adversarial balanced representations, so that they are predictive of the next outcome but non-predictive of the current treatment assignment. We evaluate our Causal Transformer based on synthetic and real-world datasets, where it achieves superior performance over current baselines. To the best of our knowledge, this is the first work proposing transformer-based architecture for estimating counterfactual outcomes from longitudinal data.

**Paper Link**: [https://proceedings.mlr.press/v162/melnychuk22a/melnychuk22a.pdf](https://proceedings.mlr.press/v162/melnychuk22a/melnychuk22a.pdf)

---

**Title**: Normalizing Flows for Interventional Density Estimation

**Abstract**: Existing machine learning methods for causal inference usually estimate quantities expressed via the mean of potential outcomes (e.g., average treatment effect). However, such quantities do not capture the full information about the distribution of potential outcomes. In this work, we estimate the density of potential outcomes after interventions from observational data. For this, we propose a novel, fully-parametric deep learning method called Interventional Normalizing Flows. Specifically, we combine two normalizing flows, namely (i) a nuisance flow for estimating nuisance parameters and (ii) a target flow for parametric estimation of the density of potential outcomes. We further develop a tractable optimization objective based on a one-step bias correction for efficient and doubly robust estimation of the target flow parameters. As a result, our Interventional Normalizing Flows offer a properly normalized density estimator. Across various experiments, we demonstrate that our Interventional Normalizing Flows are expressive and highly effective, and scale well with both sample size and high-dimensional confounding. To the best of our knowledge, our Interventional Normalizing Flows are the first proper fully-parametric, deep learning method for density estimation of potential outcomes.

**Paper Link**: [https://proceedings.mlr.press/v202/melnychuk23a/melnychuk23a.pdf](https://proceedings.mlr.press/v202/melnychuk23a/melnychuk23a.pdf)

