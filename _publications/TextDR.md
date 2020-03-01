---
title: "Improving Maximum Likelihood Training for Text Generation with Density Ratio Estimation"
collection: publications
permalink: /publications/TextDR
venue: "The 23rd International Conference on Artificial Intelligence and Statistics."
date: 2020-1-9
citation: 'Yuxuan Song, Ning Miao, Hao Zhou, <b>Lantao Yu</b>, Mingxuan Wang, Lei Li. <b>AISTATS 2020</b>.'
---

[[PDF]](https://lantaoyu.github.io/files/aistats2020.pdf)

## Abstract
Autoregressive neural sequence generative models trained by Maximum Likelihood Estimation suffer the exposure bias problem in practical finite sample scenarios. The crux is that the number of training samples for Maximum Likelihood Estimation is usually limited and the input data distributions are different at training and inference stages. Many methods have been proposed to solve the above problem, which relies on sampling from the non-stationary model distribution and suffers from high variance or biased estimations. In this paper, we propose $\psi$-MLE, a new training scheme for autoregressive sequence generative models, which is effective and stable when operating at large sample space encountered in text generation. We derive our algorithm from a new perspective of self-augmentation and introduce bias correction with density ratio estimation. Extensive experimental results on synthetic data and real-world text generation tasks demonstrate that our method stably outperforms Maximum Likelihood Estimation and other state-of-the-art sequence generative models in terms of both quality and diversity.