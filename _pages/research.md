---
layout: archive
title: "Research Overview"
permalink: /research/
author_profile: true
---

My ultimate research goal is to develop <em>trustworthy autonomous agents interacting with humans</em>. My current research focuses on designing <em> explainable autonomous driving systems</em>, where the decision-making process of autonomous vehicles is <em>tractable</em> and <em>transparent</em> for humans. Such a transparent system is a prerequisite for building trust between humans and autonomous vehicles. My research efforts towards this goal mainly lie in the following aspects:

## Diagnosing Black-box Deep-Learning Functional Modules
<img src="/images/nips.png" width="300" style="float: left; margin-right: 1em; margin-top: 0.5em; margin-bottom: 0.8em">
Deep neural networks achieve state-of-the-art performance in multiple core autonomous driving tasks (e.g., behavior prediction and policy learning). However, their black-box nature is a crucial barrier to genuine trustworthiness. It is, therefore, essential to gain a deeper understanding of their behavior. In my research, **I utilize explainable AI techniques to develop analysis toolkits customized for deep-learning functional modules**. They serve as simple plug-ins to diagnose the models without interfering with the performance. With the help of these toolkits, we identified principled design flaws in popular trajectory prediction models that were previously ignored in the literature, motivating new designs with improved robustness and performance. For instance, we found that Variational-Autoencoder-based trajectory prediction models suffer from an issue we named <em>social posterior collapse</em>, i.e., the model is prone to ignoring all the surrounding agents when predicting the future trajectory of a target agent. Our work is the first in the literature that discovered such systematic defects in interaction modeling. Prior works only focused on the overall performance without studying whether their models encode social context as claimed. <br/>

**Related Publications:** 
1. **C. Tang**, W. Zhan and M. Tomizuka, "Exploring Social Posterior Collapse in Variational Autoencoder for Interaction Modeling," Conference on Neural Information Processing Systems (NeurIPS), 2021
1. **C. Tang**, W. Zhan, and M. Tomizuka, “Interventional behavior prediction: Avoiding overly confident anticipation in interactive prediction,” *IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS)*, 2022
