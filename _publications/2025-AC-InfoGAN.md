---
title: "Unsupervised and controllable synthesizing for imbalanced energy dataset based on AC-InfoGAN"
collection: publications
type: journal  
permalink: /publication/2025-AC-InfoGAN
excerpt: 'In this paper, we introduce the Adaptive and Contrastive Information Maximizing Generative Adversarial Nets (AC-InfoGAN) to achieve controllable synthesizing for the unlabeled and imbalanced energy dataset.'
date: 2025-07-01
author: <b>Zhenghao Zhou</b>, Yiyan Li*, Runlong Liu, Xiaoyuan Xu, Zheng Yan
venue: 'Applied Energy'
#slidesurl: ''
paperurl: 'http://academicpages.github.io/files/AC-InfoGAN.pdf'
citation: 'Zhou Z, Li Y, Liu R, et al. Unsupervised and controllable synthesizing for imbalanced energy dataset based on AC-InfoGAN[J]. Applied Energy, 2025, 393: 126107.'
---

Generating synthetic data has become a popular alternative solution to deal with the difficulties in accessing and 
sharing field measurement data in power systems. However, to make the generation results controllable, existing 
methods (e.g., Conditional Generative Adversarial Nets, cGAN) require labeled dataset to train the model, which 
is demanding in practice because many field measurement data lack descriptive labels. Meanwhile, real-world 
datasets are naturally imbalanced, causing bias in neural network training. In this paper, we introduce the 
Adaptive and Contrastive Information Maximizing Generative Adversarial Nets (AC-InfoGAN) to achieve 
controllable synthesizing for the unlabeled and imbalanced energy dataset. Features with physical meanings can 
be automatically extracted by maximizing the mutual information between the input latent code and the classifier output. Then the extracted features are used to control the generation results similar to a vanilla cGAN 
framework. We employ the Gumbel-Softmax distribution and frequency-based contrastive learning techniques to 
dynamically adapt to the imbalanced dataset to avoid the model training bias. Meanwhile, frequency-domain 
neural network modules are introduced to the AC-InfoGAN framework to enhance the model performances. 
Case study is based on the unlabeled and imbalanced energy datasets of power load and renewable energy 
output. Results demonstrate that AC-InfoGAN can extract both discrete and continuous features with certain 
physical meanings, as well as generating realistic synthetic energy data that satisfy given features