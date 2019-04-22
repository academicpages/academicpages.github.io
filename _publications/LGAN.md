---
title: "Lipschitz Generative Adversarial Nets"
collection: publications
permalink: /publications/LGAN
venue: "The 36th International Conference on Machine Learning (ICML-19)"
date: 2019-2-23
citation: 'Zhiming Zhou, Jiadong Liang, Yuxuan Song, <b>Lantao Yu</b>, Hongwei Wang, Weinan Zhang, Yong Yu, Zhihua Zhang. <i>The 36th International Conference on Machine Learning</i>. <b>ICML 2019</b>.'
---

[[ArXiv]](https://arxiv.org/abs/1902.05687)

## Abstract
In this paper we study the convergence of generative adversarial networks (GANs) from the perspective of the informativeness of the gradient of the optimal discriminative function. We show that GANs without restriction on the discriminative function space commonly suffer from the problem that the gradient produced by the discriminator is uninformative to guide the generator. By contrast, Wasserstein GAN (WGAN), where the discriminative function is restricted to 1-Lipschitz, does not suffer from such a gradient uninformativeness problem. We further show in the paper that the model with a compact dual form of Wasserstein distance, where the Lipschitz condition is relaxed, also suffers from this issue. This implies the importance of Lipschitz condition and motivates us to study the general formulation of GANs with Lipschitz constraint, which leads to a new family of GANs that we call Lipschitz GANs (LGANs). We show that LGANs guarantee the existence and uniqueness of the optimal discriminative function as well as the existence of a unique Nash equilibrium. We prove that LGANs are generally capable of eliminating the gradient uninformativeness problem. According to our empirical analysis, LGANs are more stable and generate consistently higher quality samples compared with WGAN.
