---
title: "MOPO: Model-based Offline Policy Optimization"
collection: publications
permalink: /publications/MOPO
venue: "The 34th Conference on Neural Information Processing Systems (NeurIPS 2020)"
date: 2020-6-1
citation: 'Tianhe Yu*, Garrett Thomas* (equal contribution), <b>Lantao Yu</b>, Stefano Ermon, James Zou, Sergey Levine, Chelsea Finn, Tengyu Ma.
<i>The 34th Conference on Neural Information Processing Systems</i>. <b>NeurIPS 2020</b>.'
---
[[PDF]](https://arxiv.org/pdf/2005.13239.pdf)


## Abstract
Offline reinforcement learning (RL) refers to the problem of learning policies entirely from a batch of previously collected data. This problem setting is compelling, because it offers the promise of utilizing large, diverse, previously collected datasets to acquire policies without any costly or dangerous active exploration, but it is also exceptionally difficult, due to the distributional shift between the offline training data and the learned policy. While there has been significant progress in model-free offline RL, the most successful prior methods constrain the policy to the support of the data, precluding generalization to new states. In this paper, we observe that an existing model-based RL algorithm on its own already produces significant gains in the offline setting, as compared to model-free approaches, despite not being designed for this setting. However, although many standard model-based RL methods already estimate the uncertainty of their model, they do not by themselves provide a mechanism to avoid the issues associated with distributional shift in the offline setting. We therefore propose to modify existing model-based RL methods to address these issues by casting offline model-based RL into a penalized MDP framework. We theoretically show that, by using this penalized MDP, we are maximizing a lower bound of the return in the true MDP. Based on our theoretical results, we propose a new model-based offline RL algorithm that applies the variance of a Lipschitz-regularized model as a penalty to the reward function. We find that this algorithm outperforms both standard model-based RL methods and existing state-of-the-art model-free offline RL approaches on existing offline RL benchmarks, as well as two challenging continuous control tasks that require generalizing from data collected for a different task.