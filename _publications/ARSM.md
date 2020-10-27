---
title: "Autoregressive Score Matching"
collection: publications
permalink: /publications/ARSM
venue: "The 34th Conference on Neural Information Processing Systems (NeurIPS 2020)"
date: 2020-9-30
citation: 'Chenlin Meng, <b>Lantao Yu</b>, Yang Song, Jiaming Song, and Stefano Ermon. <i>The 34th Conference on Neural Information Processing Systems</i>. <b>NeurIPS 2020</b>.'
---

[[PDF]](https://arxiv.org/pdf/2010.12810.pdf)

## Abstract
Autoregressive models use the chain rule to define a joint probability distribution as a product of conditionals. These conditionals need to be normalized, imposing constraints on the functional families that can be used. To increase flexibility, we propose autoregressive conditional score models (AR-CSM) and parameterize the joint distribution in terms of the derivatives of univariate log-conditionals (scores), which need not be normalized. To train AR-CSM, we introduce a new divergence between distributions named Composite Score Matching (CSM). For AR-CSM models, this divergence between data and model distributions can be computed and optimized efficiently, requiring no expensive sampling or adversarial training. Compared to previous score matching algorithms, our method is more scalable to high dimensional data and more stable to optimize. We show with extensive experimental results that it can be applied to density estimation on synthetic data, image generation, image denoising, and training latent variable models with implicit encoders.