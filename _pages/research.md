---
layout: archive
title: "Selected Research Projects"
permalink: /research/
author_profile: true
---

<img src="/images/porl2.png" width="400" style="float: left; margin-right: 1em; margin-top: 0.5em; margin-bottom: 0.8em">

**Dealing with the Unknown:Pessimistic Offline Reinforcement Learning [[CoRL 2021]](https://openreview.net/forum?id=ftOqDUeLPn3)** <br />
_Jinning Li, Chen Tang, Masayoshi Tomizuka, Wei Zhan_ <br/> 
**Abstract**: Reinforcement Learning (RL) has been shown effective in domains where the agent can learn policies by actively interacting with its operating environment. However, if we change the RL scheme to offline setting where the agent can only update its policy via static datasets, one of the major issues in offline reinforcement learning emerges, i.e. distributional shift. We propose a Pessimistic Offline Reinforcement Learning (PessORL) algorithm to actively lead the agent back to the area where it is familiar by manipulating the value function. We focus on problems caused by out-of-distribution (OOD) states, and deliberately penalize high values at states that are absent in the training dataset, so that the learned pessimistic value function lower bounds the true value anywhere within the state space. We evaluate the PessORL algorithm on various benchmark tasks, where we show that our method gains better performance by explicitly handling OOD states, when compared to those methods merely considering OOD actions. 
<br />
<br />

<img src="/images/nips.png" width="400" style="float: left; margin-right: 1em; margin-top: 0.5em; margin-bottom: 0.8em">

**Exploring Social Posterior Collapse in VariationalAutoencoder for Interaction Modeling** <br />
_Chen Tang, Wei Zhan, Masayoshi Tomizuka_ <br/> 
**Abstract**: Multi-agent behavior modeling and trajectory forecasting is crucial for safe navigation of autonomous agents in interactive scenarios. Variational Autoencoder (VAE) has been widely applied in multi-agent interaction modeling for its ability in generating diverse behavior and learning a low-dimensional representation for interacting systems. However, existing literature did not formally discuss if a VAE-based model can properly encode interaction into its latent space. In this work, we argue that one of typical formulations of VAEs in multi-agent modeling suffers from an issue we refer to as social posterior collapse, i.e., the model is prone to ignore social context when predicting the future trajectory of an agent. It could cause large prediction errors and poor generalization performance. We analyze the reason behind this under-explored phenomenon and propose several measures to tackle it. Afterwards, we implement the proposed framework and experiment on real-world datasets for multi-agent trajectory prediction. In particular, we propose a novel sparse graph attention message-passing (sparse-GAMP) layer which helps us detect social posterior collapse in our experiments. In the experiments, we verify that social posterior collapse indeed occurs. Also, the proposed measures are effective in alleviating the issue. As a result, the model attains better generalization performance when social context is informative for prediction.
<br />
<br />

<img src="/images/gri.png" width="400" style="float: left; margin-right: 1em; margin-top: 0.5em; margin-bottom: 0.8em">

**Grounded Relational Inference: Domain Knowledge Driven Explainable Autonomous Driving [[arxiv]](https://arxiv.org/abs/2102.11905)** <br />
_Chen Tang, Nishan Srishankar, Sujitha Martin, Masayoshi Tomizuka_ <br /> 
**Abstract**: Explainability is essential for autonomous vehicles and other robotics systems interacting with humans and other objects during operation. Humans need to understand and anticipate the actions taken by the machines for trustful and safe cooperation. In this work, we aim to enable the explainability of an autonomous driving system at the design stage by incorporating expert domain knowledge into the model. We propose Grounded Relational Inference (GRI). It models an interactive system's underlying dynamics by inferring an interaction graph representing the agents' relations. We ensure an interpretable interaction graph by grounding the relational latent space into semantic behaviors defined with expert domain knowledge. We demonstrate that it can model interactive traffic scenarios under both simulation and real-world settings, and generate interpretable graphs explaining the vehicle's behavior by their interactions.
<br />
<br />

<img src="/images/rlrc.png" width="400" style="float: left; margin-right: 1em; margin-top: 0.5em; margin-bottom: 0.8em">

**Disturbance-Observer-Based Tracking Controller for Neural Network Driving Policy Transfer [[T-ITS](https://ieeexplore.ieee.org/abstract/document/8924943)] [[ITSC 2018](https://ieeexplore.ieee.org/abstract/document/8569612)]** <br />
_Chen Tang\*, Zhuo Xu\*, Masayoshi Tomizuka_ <br />
**Abstract**: Although deep reinforcement learning (deep RL) methods have lots of strengths that are favorable if applied to autonomous driving, real deep RL applications in autonomous driving have been slowed down by the modeling gap between the source (training) domain and the target (deployment) domain. Unlike current policy transfer approaches, which generally limit to the usage of uninterpretable neural network representations as the transferred features, we propose to transfer concrete kinematic quantities in autonomous driving. The proposed robust-control-based (RC) generic transfer architecture, which we call RL-RC, incorporates a transferable hierarchical RL trajectory planner and a robust tracking controller based on disturbance observer (DOB). The deep RL policies trained with known nominal dynamics model are transferred directly to the target domain, DOB-based robust tracking control is applied to tackle the modeling gap including the vehicle dynamics errors and the external disturbances such as side forces. We provide simulations validating the capability of the proposed method to achieve zero-shot transfer across multiple driving scenarios such as lane keeping, lane changing and obstacle avoidance.