---
title: "Meta-Inverse Reinforcement Learning with Probabilistic Context Variables"
collection: publications
permalink: /publications/MetaIRL
venue: "The 33rd Conference on Neural Information Processing Systems (NeurIPS-2019)"
date: 2018-4-12
citation: '<b>Lantao Yu</b>*, Tianhe Yu* (equal contribution), Chelsea Finn, Stefano Ermon. <i>The 33rd Conference on Neural Information Processing Systems</i>. <b>NeurIPS 2019</b>.'
---
[[PDF]](https://arxiv.org/pdf/1909.09314.pdf) [[Website]](https://sites.google.com/view/pemirl)


## Abstract
Providing a suitable reward function to reinforcement learning can be difficult in many real world applications. While inverse reinforcement learning (IRL) holds promise for automatically learning reward functions from demonstrations, several major challenges remain. First, existing IRL methods learn reward functions from scratch, requiring large numbers of demonstrations to correctly infer the reward for each task the agent may need to perform. Second, existing methods typically assume homogeneous demonstrations for a single behavior or task, while in practice, it might be easier to collect datasets of heterogeneous but related behaviors. To this end, we propose a deep latent variable model that is capable of learning rewards from demonstrations of distinct but related tasks in an unsupervised way.  Critically, our model can infer rewards for new, structurally similar tasks from a single demonstration. Our experiments on multiple continuous control tasks demonstrate the effectiveness of our approach compared to state-of-the-art imitation and inverse reinforcement learning methods.