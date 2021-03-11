---
title: "Adversarial Inverse Reinforcement Learning with Self-attention Dynamics Model"
collection: publications
permalink: /publications/RAL21
venue: "IEEE Robotics and Automation Letters (RA-L), 2021"
date: 2018-4-12
citation: 'Jiankai Sun, <b>Lantao Yu</b>, Pinqian Dong, Bo Lu, Bolei Zhou. <i>IEEE Robotics and Automation Letters</i>. <b>RA-L 2021</b>.'
---
[[PDF]](https://ieeexplore.ieee.org/document/9361118?source=authoralert)


## Abstract
In many real-world applications where specifying a proper reward function is difficult, it is desirable to learn policies from expert demonstrations. Adversarial Inverse Reinforcement Learning (AIRL) is one of the most common approaches for learning from demonstrations. However, due to the stochastic policy, current computation graph of AIRL is no longer end-to-end differentiable like Generative Adversarial Networks (GANs), resulting in the need for high-variance gradient estimation methods and large sample size. In this work, we propose the Model-based Adversarial Inverse Reinforcement Learning (MAIRL), an end-to-end model-based policy optimization method with self-attention. Considering the problem of learning robust reward and policy from expert demonstrations under learned environment dynamics. MAIRL has the advantage of the low variance for policy updating, thus addressing the key issue of AIRL. We evaluate our approach thoroughly on various control tasks as well as the challenging transfer learning problems where training and test environments are made to be different. The results show that our approach not only learns near-optimal rewards and policies that match expert behavior but also outperforms previous inverse reinforcement learning algorithms in real robot experiments.