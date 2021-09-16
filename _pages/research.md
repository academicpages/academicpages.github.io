---
layout: archive
title: "Selected Research Projects"
permalink: /research/
author_profile: true
---

<img src="/images/porl2.png" width="350" style="float: left; margin-right: 1em; margin-top: 0.5em; margin-bottom: 0.8em">

**Dealing with the Unknown:Pessimistic Offline Reinforcement Learning [[CoRL 2021]](https://openreview.net/forum?id=ftOqDUeLPn3)** <br />
_Jinning Li, Chen Tang, Masayoshi Tomizuka, Wei Zhan_ <br/> 
**Abstract**: Reinforcement Learning (RL) has been shown effective in domains where the agent can learn policies by actively interacting with its operating environment. However, if we change the RL scheme to offline setting where the agent can only update its policy via static datasets, one of the major issues in offline reinforcement learning emerges, i.e. distributional shift. We propose a Pessimistic Offline Reinforcement Learning (PessORL) algorithm to actively lead the agent back to the area where it is familiar by manipulating the value function. We focus on problems caused by out-of-distribution (OOD) states, and deliberately penalize high values at states that are absent in the training dataset, so that the learned pessimistic value function lower bounds the true value anywhere within the state space. We evaluate the PessORL algorithm on various benchmark tasks, where we show that our method gains better performance by explicitly handling OOD states, when compared to those methods merely considering OOD actions. 

<img src="/images/nips.png" width="350" style="float: left; margin-right: 1em; margin-top: 0.5em; margin-bottom: 0.8em">

**Exploring Social Posterior Collapse in VariationalAutoencoder for Interaction Modeling** <br />
_Chen Tang, Wei Zhan, Masayoshi Tomizuka_ <br/> 
**Abstract**: Multi-agent behavior modeling and trajectory forecasting is crucial for safe nav-igation of autonomous agents in interactive scenarios.  Variational Autoencoder(VAE) has been widely applied in multi-agent interaction modeling for its abilityin generating diverse behavior and learning a low-dimensional representation forinteracting systems.  However, existing literature did not formally discuss if aVAE-based model can properly encode interaction into its latent space.  In thiswork, we argue that one of typical formulations of VAEs in multi-agent modelingsuffers from an issue we refer to as social posterior collapse, i.e., the model is proneto ignore social context when predicting the future trajectory of an agent. It couldcause large prediction errors and poor generalization performance. We analyze thereason behind this under-explored phenomenon and propose several measures totackle it. Afterwards, we implement the proposed framework and experiment onreal-world datasets for multi-agent trajectory prediction. In particular, we proposea novel sparse graph attention message-passing (sparse-GAMP) layer which helpsus detect social posterior collapse in our experiments.  In the experiments, weverify that social posterior collapse indeed occurs. Also, the proposed measures areeffective in alleviating the issue. As a result, the model attains better generalizationperformance when social context is informative for prediction.
