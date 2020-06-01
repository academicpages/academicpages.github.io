---
title: "Training Deep Energy-Based Models with f-Divergence Minimization"
collection: publications
permalink: /publications/fEBM
venue: "The 37th International Conference on Machine Learning (ICML 2020)"
date: 2020-3-9
citation: '<b>Lantao Yu</b>, Yang Song, Jiaming Song, Stefano Ermon.
<i>The 37th International Conference on Machine Learning</i>. <b>ICML 2020</b>.'
---
[[PDF]](https://arxiv.org/pdf/2003.03463.pdf)


## Abstract
Deep energy-based models (EBMs) are very flexible in distribution parametrization but computationally challenging because of the intractable partition function. They are typically trained via maximum likelihood, using contrastive divergence to approximate the gradient of the KL divergence between data and model distribution. While KL divergence has many desirable properties, other f-divergences have shown advantages in training implicit density generative models such as generative adversarial networks. In this paper, we propose a general variational framework termed f-EBM to train EBMs using any desired f-divergence. We introduce a corresponding optimization algorithm and prove its local convergence property with non-linear dynamical systems theory. Experimental results demonstrate the superiority of f-EBM over contrastive divergence, as well as the benefits of training EBMs using f-divergences other than KL.