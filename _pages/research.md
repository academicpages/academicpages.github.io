---
layout: archive
title: "Research Overview"
permalink: /research/
author_profile: true
---

My ultimate research goal is to develop **trustworthy autonomous agents interacting with humans**. My current research mainly focus on designing <em> explainable autonomous driving systems</em>, where the decision-making process of autonomous vehicles is <em>tractable</em> and <em>transparent</em> for humans. Such a transparent system is a prerequisite for building trust between humans and autonomous vehicles. My research efforts towards this goal mainly lie in the following aspects:

## Diagnosing Black-box Deep-Learning Functional Modules
<img src="/images/nips.png" width="300" style="float: left; margin-right: 1em; margin-top: 0.5em; margin-bottom: 0.8em">
Deep neural networks achieve state-of-the-art performance in multiple core autonomous driving tasks (e.g., behavior prediction and policy learning). However, their black-box nature is a crucial barrier to genuine trustworthiness. It is, therefore, essential to gain a deeper understanding of their behavior. In my research, **I utilize explainable AI techniques to develop analysis toolkits customized for deep-learning functional modules**. They serve as simple plug-ins to diagnose the models without interfering with the performance. With the help of these toolkits, we identified principled design flaws in popular trajectory prediction models that were previously ignored in the literature, motivating new designs with improved robustness and performance. For instance, we found that Variational-Autoencoder-based trajectory prediction models suffer from an issue we named <em>social posterior collapse</em>, i.e., the model is prone to ignoring all the surrounding agents when predicting the future trajectory of a target agent. Our work is the first in the literature that discovered such systematic defects in interaction modeling. Prior works only focused on the overall performance without studying whether their models encode social context as claimed. <br/>

**Related Publications:**
1. <font size=4> **C. Tang**, W. Zhan and M. Tomizuka, "Exploring Social Posterior Collapse in Variational Autoencoder for Interaction Modeling," *Conference on Neural Information Processing Systems (NeurIPS)*, 2021</font>
1. **C. Tang**, W. Zhan, and M. Tomizuka, “Interventional behavior prediction: Avoiding overly confident anticipation in interactive prediction,” *IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS)*, 2022

## Designing Domain-Knowledge-Driven Interpretable Prediction Models
<img src="/images/gri.png" width="300" style="float: left; margin-right: 1em; margin-top: 0.5em; margin-bottom: 0.8em">
Interpretable models ensure that the systems are intelligible for humans at the design stage, which is crucial for <em>high-stakes</em> and <em>safe-critical</em> applications. Therefore, finding interpretable substitutes is a more fundamental solution to ensure transparency, in contrast to explaining black-box deep neural networks. To design interpretable trajectory prediction models, **I investigate principled methods to incorporate domain knowledge of social interaction into prediction models, inducing models reasoning interactive behavior consistently with humans.** Specifically, the proposed methods aim to introduce an interpretable latent space encoding semantically meaningful interactions among the agents. <br/>

**Related Publications:** 
1. **C. Tang**, N. Srishankar, S. Martin and M. Tomizuka, "Grounded Relational Inference: Domain Knowledge-driven Explainable Autonomous Driving," under review for *IEEE Transactions on Intelligent Transportation System (T-ITS)*, 2022
1. L. Sun\*, **C. Tang**\*, Y. Niu, E. Sachdeva, C. Choi, T. Misu, M. Tomizuka, and W. Zhan, “Domain knowledge driven pseudo labels for interpretable goal-conditioned interactive trajectory prediction,” *IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS)*, 2022
