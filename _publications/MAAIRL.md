---
title: "Multi-Agent Adversarial Inverse Reinforcement Learning"
collection: publications
permalink: /publications/MAAIRL
venue: "The 36th International Conference on Machine Learning (ICML-19)"
date: 2018-4-12
citation: '<b>Lantao Yu</b>, Jiaming Song, Stefano Ermon. <i>The 36th International Conference on Machine Learning</i>. <b>ICML 2019</b>.'
---
[[PDF]](https://arxiv.org/abs/1907.13220)


## Abstract
Reinforcement learning agents are prone to undesired behaviors due to reward mis-specification. Finding a set of reward functions to properly guide agent behaviors is particularly challenging in multi-agent scenarios. Inverse reinforcement learning provides a framework to automatically acquire suitable reward functions from expert demonstrations. Its extension to multi-agent settings, however, is difficult due to the more complex notions of rational behaviors. In this paper, we propose MA-AIRL, a new framework for multi-agent inverse reinforcement learning, which is effective and scalable for Markov games with high-dimensional state-action space and unknown dynamics. We derive our algorithm based on a new solution concept and maximum pseudolikelihood estimation within an adversarial reward learning framework. In the experiments, we demonstrate that MA-AIRL can recover reward functions that are highly correlated with the ground truth rewards, while significantly outperforms prior methods in terms of policy imitation.