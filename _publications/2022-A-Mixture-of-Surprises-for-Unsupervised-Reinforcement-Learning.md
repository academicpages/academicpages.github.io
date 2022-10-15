---
title: "A Mixture of Surprises for Unsupervised Reinforcement Learning"
collection: publications
permalink: /publication/2022-A-Mixture-of-Surprises-for-Unsupervised-Reinforcement-Learning
excerpt: ''
date: 2022-11-29
venue: 'NeurIPS'
tags:
  - Conference Publications
citation: 'Andrew Zhao, Matthieu Gaetan Lin, Yangguang Li, Yong-Jin Liu*, Gao Huang*. A Mixture of Surprises for Unsupervised Reinforcement Learning. Neural Information Processing Systems (NeurIPS) 2022, https://doi.org/10.48550/arXiv.2210.06702'
---



Abstract: Unsupervised reinforcement learning aims at learning a generalist policy in a reward-free manner for fast adaptation to downstream tasks. Most of the existing methods propose to provide an intrinsic reward based on surprise. Maximizing or minimizing surprise drives the agent to either explore or gain control over its environment. However, both strategies rely on a strong assumption: the entropy of the environment's dynamics is either high or low. This assumption may not always hold in real-world scenarios, where the entropy of the environment's dynamics may be unknown. Hence, choosing between the two objectives is a dilemma. We propose a novel yet simple mixture of policies to address this concern, allowing us to optimize an objective that simultaneously maximizes and minimizes the surprise. Concretely, we train one mixture component whose objective is to maximize the surprise and another whose objective is to minimize the surprise. Hence, our method does not make assumptions about the entropy of the environment's dynamics. We call our method a Mixture Of SurpriseS (MOSS) for unsupervised reinforcement learning. Experimental results show that our simple method achieves state-of-the-art performance on the URLB benchmark, outperforming previous pure surprise maximization-based objectives. 



[Download paper here](http://yongjinliu.github.io/files/2022-A-Mixture-of-Surprises-for-Unsupervised-Reinforcement-Learning.pdf)

[Download code here](https://github.com/LeapLabTHU/MOSS)

[More information](https://doi.org/10.1145/3503161.3551583)

Recommended citation: Andrew Zhao, Matthieu Gaetan Lin, Yangguang Li, **Yong-Jin Liu\***, Gao Huang\*. A Mixture of Surprises for Unsupervised Reinforcement Learning. Neural Information Processing Systems (NeurIPS) 2022, https://doi.org/10.48550/arXiv.2210.06702

