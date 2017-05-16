---
title: "SeqGAN: Sequence Generative Adversarial Nets with Policy Gradient"
collection: publications
permalink: /publications/SeqGAN
venue: "The Thirty-First AAAI conference on Artificial Intelligence (AAAI-17)"
date: 2017-2-7
citation: '<b>Lantao Yu</b>, Weinan Zhang, Jun Wang, and Yong Yu. <i>The 31st AAAI conference on Artificial Intelligence</i>. <b>AAAI 2017</b>.'
---
[[ArXiv]](https://arxiv.org/abs/1609.05473) [[AAAI Version]](https://www.aaai.org/ocs/index.php/AAAI/AAAI17/paper/view/14344/14489) [[Code]](https://github.com/LantaoYu/SeqGAN) [[Slide]](http://lantaoyu.github.io/files/2017-02-07-aaai-seqgan.pdf)


## Abstract
As a new way of training generative models, Generative Adversarial Net (GAN) that uses a discriminative model to guide the training of the generative model has enjoyed considerable success in generating real-valued data. However, it has limitations when the goal is for generating sequences of discrete tokens. A major reason lies in that the discrete outputs from the generative model make it difficult to pass the gradient update from the discriminative model to the generative model. Also, the discriminative model can only assess a complete sequence, while for a partially generated sequence, it is non-trivial to balance its current score and the future one once the entire sequence has been generated. In this paper, we propose a sequence generation framework, called SeqGAN, to solve the problems. Modeling the data generator as a stochastic policy in reinforcement learning (RL), SeqGAN bypasses the generator differentiation problem by directly performing gradient policy update. The RL reward signal comes from the GAN discriminator judged on a complete sequence, and is passed back to the intermediate state-action steps using Monte Carlo search. Extensive experiments on synthetic data and real-world tasks demonstrate significant improvements over strong baselines.
