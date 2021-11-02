---
title: "Pseudo-Spherical Contrastive Divergence"
collection: publications
permalink: /publications/PSCD
venue: "The 35th Conference on Neural Information Processing Systems (NeurIPS 2021)"
date: 2021-9-28
citation: '<b>Lantao Yu</b>, Jiaming Song, Yang Song, Stefano Ermon. <i>The 35th Conference on Neural Information Processing Systems</i>. <b>NeurIPS 2021</b>.'
---

[[PDF]](https://arxiv.org/pdf/2111.00780.pdf)

## Abstract
Energy-based models (EBMs) offer flexible distribution parametrization. However, due to the intractable partition function, they are typically trained via contrastive divergence for maximum likelihood estimation. In this paper, we propose pseudo-spherical contrastive divergence (PS-CD) to generalize maximum likelihood learning of EBMs. PS-CD is derived from the maximization of a family of strictly proper homogeneous scoring rules, which avoids the computation of the intractable partition function and provides a generalized family of learning objectives that include contrastive divergence as a special case. Moreover, PS-CD allows us to flexibly choose various learning objectives to train EBMs without additional  computational cost or variational minimax optimization. Theoretical analysis on the proposed method and extensive experiments on both synthetic data and commonly used image datasets demonstrate the effectiveness and modeling flexibility of PS-CD, as well as its robustness to data contamination, thus showing its superiority over maximum likelihood and f-EBMs.