---
title: "Context Attribution with Multi-Armed Bandit Optimization"
collection: publications
category: preprints
permalink: /publication/2025-01-01-context-attribution
excerpt: 'This paper presents a novel approach to context attribution using multi-armed bandit optimization techniques.'
date: 2025-01-01
authors: 'Pan, D., Murugesan, K., Moniz, N., Chawla, N.'
paperurl: 'https://arxiv.org/pdf/2506.19977'
citation: 'Pan, D., Murugesan, K., Moniz, N., Chawla, N. (2025). &quot;Context Attribution with Multi-Armed Bandit Optimization.&quot; <i>Preprint</i>.'
---

**Abstract:**
Understanding which parts of the retrieved context contribute to a large language model's generated answer is essential for building interpretable and trustworthy generative QA systems. We propose a novel framework that formulates context attribution as a combinatorial multi-armed bandit (CMAB) problem. Each context segment is treated as a bandit arm, and we employ Combinatorial Thompson Sampling (CTS) to efficiently explore the exponentially large space of context subsets under a limited query budget. Our method defines a reward function based on normalized token likelihoods, capturing how well a subset of segments supports the original model response. Unlike traditional perturbation-based attribution methods such as SHAP, which sample subsets uniformly and incur high computational costs, our approach adaptively balances exploration and exploitation by leveraging posterior estimates of segment relevance. This leads to substantially improved query efficiency while maintaining high attribution fidelity. Extensive experiments on diverse datasets and LLMs demonstrate that our method achieves competitive attribution quality with fewer model queries.

