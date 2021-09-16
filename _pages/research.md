---
layout: archive
title: "Selected Research Projects"
permalink: /research/
author_profile: true
---

<img src="/images/porl2.png" width="350" style="float: right; margin-left: 2em; margin-top: 0.5em; margin-bottom: 0.8em">

**Dealing with the Unknown:Pessimistic Offline Reinforcement Learning [[CoRL 2021]](https://openreview.net/forum?id=ftOqDUeLPn3)** <br />
_Jinning Li, Chen Tang, Masayoshi Tomizuka, Wei Zhan_ <br/> 
**Abstract**: Reinforcement Learning (RL) has been shown effective in domains where the agent can learn policies by actively interacting with its operating environment. However, if we change the RL scheme to offline setting where the agent can only update its policy via static datasets, one of the major issues in offline reinforcement learning emerges, i.e. distributional shift. We propose a Pessimistic Offline Reinforcement Learning (PessORL) algorithm to actively lead the agent back to the area where it is familiar by manipulating the value function. We focus on problems caused by out-of-distribution (OOD) states, and deliberately penalize high values at states that are absent in the training dataset, so that the learned pessimistic value function lower bounds the true value anywhere within the state space. We evaluate the PessORL algorithm on various benchmark tasks, where we show that our method gains better performance by explicitly handling OOD states, when compared to those methods merely considering OOD actions. 

